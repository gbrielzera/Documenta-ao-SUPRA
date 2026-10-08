"""Gera a referência da API de scripts a partir de catalogo/api/_api.json
(produzido por tools/extrair_api.ps1 a partir das DLLs do Supravizio Client).

Saídas (não editar à mão):
  catalogo/api/<Classe>.md   uma página por classe/enum, com propriedades e métodos
  guias/api_scripts.md       resumo dos objetos disponíveis nos scripts, com herança achatada

Uso: python tools/api.py
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
API = RAIZ / "catalogo" / "api"
DOCS = RAIZ / "docs"
RUIDO = {"ToString", "Equals", "GetHashCode", "Dispose", "CompareTo"}
APELIDOS = {"Void": "void", "String": "string", "Int32": "int", "Int64": "long", "Boolean": "bool",
            "Object": "object", "Decimal": "decimal", "Double": "double", "DateTime": "DateTime"}

# variável disponível no script -> (classe, onde aparece). Correspondência inferida pelos membros:
# os métodos destas classes são exatamente os usados nos scripts reais dos fluxos.
GLOBAIS = [
    ("OrdemServico", "OrdemServico", "quase todos os scripts; herda de Ocorrencia e SessionObjectProxy"),
    ("Formulario", "FormularioTarefa", "Script Formulário carregado, Script Modificado e demais scripts de formulário"),
    ('Formulario["CAMPO"] / Controle', "ControleFormulario", "um campo do formulário"),
    ("FormularioRegistro", "FormularioRegistro", "linha em edição de uma Listagem de Registros (grid)"),
    ("Criticas", "CriticaValidacaoList", "Script Validação"),
    ("Atores", "ListaAtores", "Script Seleção de Atores (papel customizado por script)"),
    ("Mensagem", "TemplateMensagem", "Script Evento de eventos de mensagem / tipos de evento"),
    ("DB", "DB", "todos os scripts"),
    ("Utils", "Utils", "todos os scripts"),
    ("AD", "AD", "todos os scripts (Active Directory)"),
    ("LDAP", "OpenLDAP", "todos os scripts (OpenLDAP)"),
]
ENTIDADES = ["Pessoa", "Orgao", "Servico", "Atividade", "ClasseSubProcesso", "SubProcesso", "ItemConfiguracao",
             "Tecnico", "GrupoTrabalho", "Empresa", "Fornecedor", "Contrato"]


def amigavel(s):
    s = re.sub(r"Nullable<(\w+)>", r"\1?", s)
    return re.sub(r"\b(" + "|".join(APELIDOS) + r")\b", lambda m: APELIDOS[m.group(1)], s)


def lista(x):
    return x if isinstance(x, list) else ([x] if x else [])


def membros(t):
    props = [amigavel(p) for p in lista(t["props"])]
    mets = [amigavel(m) for m in lista(t["metodos"])
            if not any(re.search(r"\b" + r + r"\(", m) for r in RUIDO)]
    return props, mets


def main():
    dados = json.loads((API / "_api.json").read_text(encoding="utf-8-sig"))
    tipos = dados["tipos"]
    versao = dados["versoes"].get("supravizio.custom.dll", "?")
    por_nome = defaultdict(list)
    for t in tipos:
        por_nome[t["nome"]].append(t)

    def principal(nome):
        """Em nomes repetidos, prefere a classe exposta aos scripts (*.Custom / *.Script)."""
        c = por_nome.get(nome, [])
        c = sorted(c, key=lambda t: (".Custom" not in t["ns"] and ".Script" not in t["ns"]
                                     and "Connectors" not in t["ns"], t["ns"]))
        return c[0] if c else None

    for antigo in API.glob("*.md"):
        antigo.unlink()
    nomes_arquivo = {}
    for t in tipos:
        nome = t["nome"]
        arq = nome if principal(nome) is t else f"{nome}__{t['ns'].split('.')[-2] if t['ns'].endswith('Custom') else t['ns'].split('.')[-1]}"
        nomes_arquivo[id(t)] = arq

    for t in tipos:
        props, mets = membros(t)
        arq = nomes_arquivo[id(t)]
        l = [f"# {t['nome']} (API de script)",
             f"Caminho: Catálogo > API de scripts > {t['ns']} > {t['nome']}", "",
             f"{t['tipo']} `{t['ns']}.{t['nome']}` — {t['dll']} v{dados['versoes'].get(t['dll'], '?')}"]
        base = t["base"]
        if base and base not in ("Object", "Enum", "?"):
            alvo = principal(base)
            l.append(f"Herda de **{base}**" + (f" (ver catalogo/api/{nomes_arquivo[id(alvo)]}.md)" if alvo else "")
                     + ": os membros da classe base também valem aqui.")
        doc = DOCS / f"objetos_{t['nome'].lower()}.md"
        if doc.exists():
            l.append(f"Descrição de cada propriedade: docs/objetos_{t['nome'].lower()}.md")
        enum_doc = DOCS / f"enum_{t['nome'].lower()}.md"
        if t["tipo"] == "enum":
            l += ["", "Valores: " + ", ".join(lista(t["valores"]))]
            if enum_doc.exists():
                l.append(f"Significado dos valores: docs/enum_{t['nome'].lower()}.md")
        if props:
            l += ["", f"## Propriedades ({len(props)})"] + [f"- {p}" for p in props]
        if mets:
            l += ["", f"## Métodos ({len(mets)})"] + [f"- {m}" for m in mets]
        (API / f"{arq}.md").write_text("\n".join(l) + "\n", encoding="utf-8")

    # ---------------- guia resumido
    def cadeia(nome):
        r, visto = [], set()
        t = principal(nome)
        while t and t["nome"] not in visto:
            r.append(t)
            visto.add(t["nome"])
            t = principal(t["base"]) if t["base"] not in ("Object", "?", "") else None
        return r

    g = ["# API de scripts — objetos e assinaturas reais",
         "Caminho: Guias > Scripts > API (assinaturas das DLLs)", "",
         f"Gerado por tools/api.py a partir dos metadados públicos das DLLs do Supravizio Client **v{versao}**.",
         "São as assinaturas reais (o mesmo que o autocompletar do Editor de Scripts mostra), sem descrição.",
         "Atenção: os fluxos exportados são da versão 19.1.1; o que existe aqui deve continuar existindo, "
         "mas a 19 pode ter membros a mais. Página completa de cada classe: `catalogo/api/<Classe>.md` "
         f"({len(tipos)} classes). Descrições das propriedades: `docs/objetos_<classe>.md`.", "",
         "A relação variável → classe abaixo é inferida pelos membros (batem com o uso nos fluxos reais).", ""]
    for var, classe, onde in GLOBAIS:
        cad = cadeia(classe)
        if not cad:
            continue
        g.append(f"## {var}  →  {classe}")
        g.append(f"Onde: {onde}. Classe: `{cad[0]['ns']}.{classe}`"
                 + (" → " + " → ".join(c["nome"] for c in cad[1:]) if len(cad) > 1 else ""))
        for c in cad:
            props, mets = membros(c)
            estaticos = [m for m in mets if m.startswith("static ")]
            inst = [m for m in mets if not m.startswith("static ")]
            rot = "" if c is cad[0] else f" (herdado de {c['nome']})"
            if inst:
                g.append(f"Métodos{rot}:")
                g += [f"- {m}" for m in inst]
            if estaticos and c["nome"] in ("OrdemServico", "Ocorrencia"):
                uteis = [m for m in estaticos if re.search(r" (Carrega|CarregaLista|Novo|Salva)\(", m)]
                if uteis:
                    g.append(f"Estáticos{rot}: " + "; ".join(m.replace("static ", "") for m in uteis))
            if props:
                nomes = [re.sub(r" \{.*\}$", "", p) for p in props]
                g.append(f"Propriedades{rot} ({len(nomes)}): " + "; ".join(nomes))
        g.append("")

    g.append("## Entidades mais usadas (carregar com `Classe.Carrega(id)` ou `Classe.Carrega(\"Propriedade\", valor)`)")
    for nome in ENTIDADES:
        t = principal(nome)
        if not t:
            continue
        props, mets = membros(t)
        proprios = [m for m in mets if not re.search(r"\b(New\w*|Load|Novo|Nova)\(", m) or " Nova(" in m]
        g.append(f"- **{nome}** ({len(props)} propriedades, {len(mets)} métodos) → catalogo/api/{nomes_arquivo[id(t)]}.md"
                 + (". Métodos: " + "; ".join(re.sub(r"^static ", "", m) for m in proprios[:14]) if proprios else ""))
    g.append("")

    g.append("## Tipos de script existentes no produto (classes de contexto)")
    g.append("Cada classe abaixo é um ponto do sistema que executa script. A lista de variáveis de cada um "
             "não está nos metadados; ver guias/scripts.md e guias/scripts_contexto.md.")
    for t in sorted((t for t in tipos if t["nome"].endswith("ScriptContext")), key=lambda t: t["nome"]):
        props, _ = membros(t)
        alvo = "; ".join(re.sub(r" \{.*\}$", "", p) for p in props)
        g.append(f"- {t['nome'].replace('ScriptContext', '')}" + (f" (objeto: {alvo})" if alvo else ""))

    (RAIZ / "guias" / "api_scripts.md").write_text("\n".join(g) + "\n", encoding="utf-8")
    print(f"catalogo/api: {len(tipos)} páginas; guias/api_scripts.md: {len(g)} linhas (DLLs v{versao})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
