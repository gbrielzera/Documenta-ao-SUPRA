"""Gera os guias derivados automaticamente (não editar à mão os arquivos gerados):

  guias/banco.md             lista de tabelas do modelo de dados oficial, por módulo
  catalogo/schema.txt        uma linha por tabela com todas as colunas (para grep)
  guias/scripts_contexto.md  objetos disponíveis por tipo de script + exemplos reais dos XMLs
  fluxos/_INDICE.md          uma linha por fluxo resumido

Uso: python tools/guias.py
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fluxo  # noqa: E402

RAIZ = fluxo.RAIZ
DOCS = RAIZ / "docs"
GUIAS = RAIZ / "guias"

# tipo de script -> onde é configurado
ONDE = {
    "LookupScript": "campo customizado (DropDownList/SearchList/DataGrid): script de recuperação de opções; preenche `Itens`",
    "ScriptModificado": "campo de formulário: executa quando o valor do campo muda (formulário dinâmico)",
    "ScriptFormCarregado": "atividade: executa ao carregar o formulário da atividade",
    "ScriptConfirmado": "campo/registro de formulário: executa ao confirmar a edição",
    "ScriptAdicionado": "campo de registro (grid): executa ao adicionar linha",
    "ScriptInicio": "atividade: executa quando a atividade inicia (evento Inicialização)",
    "ScriptFim": "atividade: executa quando a atividade termina",
    "ScriptValidacao": "atividade: valida antes de avançar; pendências impedem a transição",
    "ScriptEvento": "evento intermediário de mensagem: ajusta a `Mensagem` antes do envio",
    "ScriptSelecaoAtores": "papel customizado por script: adiciona pessoas em `Atores`",
    "ExpressaoComparacaoDecision": "gateway: expressão cujo resultado é comparado com cada alternativa",
    "ValorComparacaoDecision": "alternativa do gateway: valor comparado com a expressão do gateway",
    "ExpressaoValor": "ValorInput de atividade (ex.: chamada de subprocesso/iniciador): expressão do valor",
    "ExpressaoCalculo": "expressão de cálculo de campo",
    "Regra": "iniciador por regra/temporizador: fórmula que decide a geração de ocorrências",
    "Source": "módulo da Biblioteca de Scripts (funções reutilizáveis; fonte em catalogo/biblioteca/)",
}
DOTNET = {"True", "False", "None", "String", "Convert", "DateTime", "Exception", "Int32", "Decimal",
          "Math", "Double", "System", "TimeSpan", "Environment", "Array", "Object", "List", "Int64",
          "CultureInfo", "StringComparison", "Globalization", "Text", "Regex", "Encoding", "IO", "Net",
          "Venki", "DBNull", "StringBuilder", "DataSet", "Newtonsoft"}
OBJETOS = ("OrdemServico", "Utils", "DB", "Formulario", "FormularioRegistro", "Criticas", "Atores",
           "Mensagem", "Pessoa", "Orgao", "Servico", "Webservices", "Ocorrencia", "Atividade", "Controle")


def gerar_banco():
    indice = (DOCS / "_INDICE.md").read_text(encoding="utf-8").split("\n")
    ini = next(i for i, l in enumerate(indice) if "(modelo_de_dados)" in l)
    fim = next(i for i, l in enumerate(indice) if "(modelo_de_objetos)" in l)
    md = ["# Banco de dados do Supravizio — tabelas do modelo oficial",
          "Caminho: Guias > Banco de dados", "",
          "Fonte: docs/dados_<tabela>.md (colunas, descrição, tipo SQL Server e Oracle, nulos).",
          "Colunas de todas as tabelas em uma linha cada: `catalogo/schema.txt` "
          "(ex.: `grep -i '^OCORRENCIA:' catalogo/schema.txt`).",
          "Tabelas de campos customizados (CP_*/CPE_*) não estão no modelo oficial: "
          "ver `catalogo/tabelas_customizadas.md` e `catalogo/campos.tsv`.",
          "Tabelas/views realmente usadas nos scripts do cliente: `catalogo/tabelas_usadas_em_sql.md`.",
          "Estrutura REAL de produção (4 tabelas, 2026-10-08): `catalogo/schema_real.tsv`; regras, índices e consultas: `guias/sql.md`.",
          "O ambiente dos XMLs é Oracle (TO_CHAR, NVL, SYSDATE, ||).", ""]
    schema = []
    n = 0
    for l in indice[ini + 1:fim]:
        m = re.match(r"(\s*)- (.+) \(([^)]+)\)$", l)
        if not m:
            continue
        nivel, titulo, arq = len(m.group(1)) // 2, m.group(2), m.group(3)
        p = DOCS / f"{arq}.md"
        if not arq.startswith("dados_") or not p.exists():
            md.append(f"\n## {titulo}")
            continue
        txt = p.read_text(encoding="utf-8")
        corpo = txt.split("\n\n")
        desc = next((b for b in corpo[2:] if b and not b.startswith(("|", "Campos desta", "#"))), "")
        desc = re.sub(r"\s+", " ", desc)[:140]
        cols = []
        for linha in txt.split("\n"):
            c = [x.strip() for x in linha.strip().strip("|").split(" | ")]
            if len(c) >= 5 and c[0].startswith("**") and c[0] != "**Nome**":
                nome = c[0].strip("*")
                cols.append(f"{nome} {c[-2]}" + (" NN" if c[-1].lower().startswith("n") else ""))
        md.append(f"- **{titulo}** ({len(cols)} col.) — {desc} → docs/{arq}.md")
        schema.append(f"{titulo}: " + "; ".join(cols))
        n += 1
    GUIAS.mkdir(exist_ok=True)
    (GUIAS / "banco.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (RAIZ / "catalogo").mkdir(exist_ok=True)
    (RAIZ / "catalogo" / "schema.txt").write_text(
        "# TABELA: COLUNA tipo_oracle [NN = não nulo]; ...  (fonte: docs/dados_*.md)\n"
        + "\n".join(schema) + "\n", encoding="utf-8")
    return n


def gerar_contexto():
    usos = defaultdict(Counter)      # tipo -> identificador -> nº scripts
    membros = defaultdict(Counter)   # objeto -> membro -> nº scripts
    exemplos = defaultdict(dict)     # tipo -> código -> fluxo de origem
    total = Counter()
    vistos = set()
    for arq in sorted(fluxo.PASTA_XML.glob("*.xml")):
        root = fluxo.carregar(arq)
        for e in root.iter():
            t = e.text or ""
            k = fluxo.tag(e)
            if len(e) or k not in ONDE:
                continue
            if k != "Source" and not fluxo.eh_script(t):
                continue
            cod = fluxo.limpar_script(t)
            if not cod.strip() or (k, cod) in vistos:
                continue
            vistos.add((k, cod))
            total[k] += 1
            exemplos[k].setdefault(cod, arq.stem)
            limpo = re.sub(r'"[^"\n]*"|\'[^\'\n]*\'|#.*', "", cod)
            for idn in set(re.findall(r"(?<![\w.])([A-Z][A-Za-z0-9_]+)\b", limpo)):
                usos[k][idn] += 1
            for o, m in set(re.findall(r"(?<![\w.])(" + "|".join(OBJETOS) + r")\.([A-Za-z_]+)", limpo)):
                membros[o][m] += 1
            for m in set(re.findall(r"Formulario\[[^\]]*\]\.([A-Za-z_]+)", limpo)):
                membros["Formulario[\"CAMPO\"]"][m] += 1
            for m in set(re.findall(r"FormularioRegistro\[[^\]]*\]\.([A-Za-z_]+)", limpo)):
                membros["FormularioRegistro[\"COLUNA\"]"][m] += 1

    md = ["# Scripts IronPython — contexto por tipo de script (extraído dos fluxos reais)",
          "Caminho: Guias > Scripts > Contexto por tipo", "",
          "Gerado por tools/guias.py a partir dos scripts distintos de todos os XMLs. "
          "Os números são a quantidade de scripts distintos que usam o identificador: "
          "é evidência de uso real, não a API completa. A documentação oficial cobre pouco "
          "destes objetos; quando houver página, ela está indicada em guias/scripts.md.", ""]
    md.append("## Membros mais usados por objeto")
    for o, c in sorted(membros.items(), key=lambda x: -sum(x[1].values())):
        md.append(f"- **{o}**: " + ", ".join(f"{m} ({v})" for m, v in c.most_common(40)))
    for k, n in total.most_common():
        md.append(f"\n## {k} — {n} scripts distintos")
        md.append(f"Onde: {ONDE[k]}")
        ids = [(i, v) for i, v in usos[k].most_common(60) if i not in DOTNET and v >= max(2, n // 40)]
        if ids:
            md.append("Identificadores de contexto: " + ", ".join(f"{i} ({v})" for i, v in ids[:25]))
        # exemplos: curtos e representativos (contêm o identificador principal)
        principal = ids[0][0] if ids else ""
        cands = sorted((c for c in exemplos[k] if 60 <= len(c) <= 900 and principal in c), key=len)
        if not cands:
            cands = sorted(exemplos[k], key=len)
        passo = max(1, len(cands) // 3)
        for cod in cands[::passo][:3]:
            md.append(f"Exemplo (de {exemplos[k][cod]}):\n```python\n{cod}\n```")
    (GUIAS / "scripts_contexto.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return sum(total.values())


def gerar_indice_fluxos():
    """fluxos/_INDICE.md: uma linha por fluxo resumido, para escolher qual abrir."""
    linhas = []
    for p in sorted((RAIZ / "fluxos").glob("*.md")):
        if p.name.startswith("_"):
            continue
        t = p.read_text(encoding="utf-8")
        m = re.match(r"# Fluxo: (.+)", t)
        titulo = m.group(1).strip() if m else p.stem
        tipos = Counter(re.findall(r"^- \[\d+\] (\w+) ", t, re.M))
        marcas = []
        if "DataGrid RecordList" in t:
            marcas.append("grid")
        if "Operação PR0002" in t:
            marcas.append("aprovação")
        if tipos.get("SubProcesso"):
            marcas.append("chama subprocesso")
        if tipos.get("LinkInicial"):
            marcas.append("link inicial")
        if "HttpClient" in t:
            marcas.append("API REST")
        if "LerXlsx" in t:
            marcas.append("lê planilha")
        if tipos.get("EventoIntermediarioTimer"):
            marcas.append("timer")
        scripts = t.count("```python")
        gateways = len(re.findall(r"^- \[G\d+\] Gateway", t, re.M))
        linhas.append(f"- **{titulo}** — {tipos.get('Tarefa', 0)} tarefas, {gateways} gateways, "
                      f"{scripts} scripts, {len(t) // 1024} KB"
                      + (f" — {', '.join(marcas)}" if marcas else "") + f" → fluxos/{p.name}")
    cabecalho = ("# Índice dos fluxos resumidos\n\n"
                 "Uma linha por XML resumido: título (sigla) e versão, tamanho e o que o fluxo contém. "
                 "Gerado por tools/guias.py.\n\n")
    (RAIZ / "fluxos" / "_INDICE.md").write_text(
        cabecalho + "\n".join(linhas) + "\n", encoding="utf-8")
    return len(linhas)


def main():
    n = gerar_banco()
    s = gerar_contexto()
    f = gerar_indice_fluxos()
    print(f"guias/banco.md e catalogo/schema.txt: {n} tabelas; guias/scripts_contexto.md: {s} scripts distintos; fluxos/_INDICE.md: {f} fluxos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
