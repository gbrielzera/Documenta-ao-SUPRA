"""Incorpora ao projeto o MAPA OFICIAL de campos customizados, lido do banco (SV_CUSTOM_PROPERTY).

Gerado por (somente leitura):
    SELECT P.NAME, P.TEXT, P.TYPE, P.CONTROL, P.TABLE_NAME, P.TABLE_COLUMN, P.LENGTH, P.INVALID, C.NAME AS CLASSE
    FROM SV_CUSTOM_PROPERTY P INNER JOIN SV_CLASS C ON C.ID_CLASS = P.ID_CLASS
    ORDER BY C.NAME, P.TABLE_NAME, P.NAME;
Formato: TAB, sem cabeçalho, primeira coluna pode vir vazia; o RÓTULO pode conter quebra de linha.

Uso:
    python tools/campos_banco.py <export.txt> [--ambiente producao] [--data 2026-10-08]

Saídas:
    catalogo/campos_banco.tsv   classe, nome, rotulo, tipo, controle, tabela, coluna, tamanho_caracteres,
                                invalido, ambiente, data   (substitui o arquivo inteiro)
    catalogo/campos_vs_banco.md cruzamento com os XMLs (catalogo/campos.tsv): campos que o banco não tem,
                                campos em outra tabela, tamanhos diferentes
"""
import argparse
import csv
import datetime
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "catalogo" / "campos_banco.tsv"
XML = RAIZ / "catalogo" / "campos.tsv"
RELATORIO = RAIZ / "catalogo" / "campos_vs_banco.md"
CAMPOS_EXPORT = 10  # vazio + 9 colunas


def ler(caminho):
    registros, pendente = [], ""
    for linha in Path(caminho).read_text(encoding="utf-8-sig").replace("\r", "").split("\n"):
        if not linha.strip() and not pendente:
            continue
        atual = (pendente + " " + linha) if pendente else linha
        f = atual.split("\t")
        if len(f) >= CAMPOS_EXPORT:
            registros.append([x.strip() for x in f[1:CAMPOS_EXPORT]])
            pendente = ""
        else:
            pendente = atual
    return registros


def classe_curta(nome):
    return nome.split(",")[0].split(".")[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("export")
    ap.add_argument("--ambiente", default="producao")
    ap.add_argument("--data", default=datetime.date.fromtimestamp(Path(sys.argv[1]).stat().st_mtime).isoformat()
                    if len(sys.argv) > 1 and Path(sys.argv[1]).exists() else "")
    a = ap.parse_args()

    regs = ler(a.export)
    if not regs:
        print("nenhum registro reconhecido")
        return 1
    linhas = []
    for nome, rotulo, tipo, controle, tabela, coluna, tam, invalido, classe in regs:
        linhas.append([classe_curta(classe), nome, rotulo, tipo, controle, tabela, coluna, tam,
                       invalido, a.ambiente, a.data])
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["classe", "nome", "rotulo", "tipo", "controle", "tabela", "coluna",
                    "tamanho_caracteres", "invalido", "ambiente", "data"])
        w.writerows(linhas)

    prod = {(l[0], l[1]): l for l in linhas}
    xml = {}
    if XML.exists():
        for linha in XML.read_text(encoding="utf-8").splitlines()[1:]:
            c = linha.split("\t")
            if len(c) > 7:
                xml[(c[0], c[1])] = c
    so_xml = sorted(k for k in xml if k not in prod)
    so_prod = [k for k in prod if k not in xml]
    outra_tabela = sorted((k, xml[k][5], prod[k][5]) for k in prod if k in xml and xml[k][5] != prod[k][5])
    tam_dif = sorted((k, xml[k][7], prod[k][7]) for k in prod if k in xml and xml[k][5] == prod[k][5]
                     and xml[k][7] and prod[k][7] and xml[k][7] != prod[k][7])
    invalidos = [l for l in linhas if l[8].lower().startswith("s")]
    por_nome = defaultdict(set)
    for l in linhas:
        por_nome[(l[0], l[1])].add(l[5])
    repetidos = {k: v for k, v in por_nome.items() if len(v) > 1}
    por_tabela = defaultdict(int)
    for l in linhas:
        por_tabela[l[5]] += 1

    md = ["# Campos customizados: mapa oficial do banco x XMLs dos fluxos",
          "Caminho: Catálogo > Banco > Campos x banco", "",
          f"Gerado por tools/campos_banco.py. Fonte do banco: `catalogo/campos_banco.tsv` "
          f"({len(linhas)} campos, {a.ambiente}, {a.data}). Fonte dos XMLs: `catalogo/campos.tsv`.",
          "Regra de ouro: o **banco é a verdade**. Um XML exportado de Qualidade pode apontar um campo para outra "
          "tabela ou trazer campos que a produção ainda não tem; ao importar na produção, o importador cria o que faltar.", "",
          "## Resumo",
          f"- Campos no banco: {len(linhas)}; nos XMLs (todas as classes): {len(xml)}.",
          f"- Nos XMLs e **ausentes** no banco: {len(so_xml)}.",
          f"- No banco e fora dos XMLs: {len(so_prod)} (criados em fluxos que não temos).",
          f"- **Mesma classe e nome, tabela diferente**: {len(outra_tabela)}.",
          f"- Mesma tabela, tamanho (caracteres) diferente: {len(tam_dif)}.",
          f"- Campos marcados como inválidos no banco: {len(invalidos)}.",
          f"- Nomes repetidos em mais de uma tabela no banco: {len(repetidos)}.", ""]
    if outra_tabela:
        md += ["## Campo existe nos dois, mas em tabela diferente (usar a do banco em SQL)",
               "| classe.campo | tabela no XML | tabela no banco |", "|---|---|---|"]
        md += [f"| {k[0]}.{k[1]} | {x} | {p} |" for k, x, p in outra_tabela]
        md.append("")
    if tam_dif:
        md += ["## Tamanho diferente (caracteres; vazio = padrão de 250)",
               "| classe.campo | XML | banco |", "|---|---|---|"]
        md += [f"| {k[0]}.{k[1]} | {x} | {p} |" for k, x, p in tam_dif]
        md.append("")
    if invalidos:
        md += ["## Marcados como inválidos no banco", ""]
        md += [f"- {l[0]}.{l[1]} ({l[5]}.{l[6]}) \"{l[2]}\"" for l in invalidos]
        md.append("")
    if repetidos:
        md += ["## Mesmo nome em mais de uma tabela (a tabela decide qual valor é lido)", ""]
        md += [f"- {k[0]}.{k[1]}: {', '.join(sorted(v))}" for k, v in sorted(repetidos.items())]
        md.append("")
    md += ["## Campos por tabela no banco (colunas customizadas; sem contar a chave)", "",
           ", ".join(f"{t} ({n})" for t, n in sorted(por_tabela.items(), key=lambda x: -x[1])
                     if not t.startswith("Z_")),
           f"; mais {sum(1 for t in por_tabela if t.startswith('Z_'))} tabelas de grid `Z_<id>_<NOME>` "
           "(uma por campo DataGrid; o campo do grid grava na própria tabela).", ""]
    md += [f"## Nos XMLs e ausentes no banco ({len(so_xml)})",
           "Cada item: classe.campo → tabela que o XML indica.", ""]
    md += [", ".join(f"{k[1]}→{xml[k][5]}" for k in so_xml if k[0] == classe)
           and f"**{classe}**: " + ", ".join(f"{k[1]}→{xml[k][5]}" for k in so_xml if k[0] == classe)
           for classe in sorted({k[0] for k in so_xml})]
    RELATORIO.write_text("\n".join(m for m in md if m is not None) + "\n", encoding="utf-8")

    print(f"campos_banco.tsv: {len(linhas)} campos em {len(por_tabela)} tabelas ({a.ambiente}, {a.data})")
    print(f"  só nos XMLs: {len(so_xml)} | só no banco: {len(so_prod)} | tabela diferente: {len(outra_tabela)} "
          f"| tamanho diferente: {len(tam_dif)} | inválidos: {len(invalidos)} | nomes repetidos: {len(repetidos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
