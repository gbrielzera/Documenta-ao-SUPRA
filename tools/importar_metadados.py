"""Importa exports do banco do Supravizio feitos em planilha (somente leitura no banco).

Uso:
    python tools/importar_metadados.py <pasta com os .xlsx> [--ambiente producao] [--data 2026-10-19]

Reconhece pelo nome do arquivo:
    Tabela_Erros*.xlsx          códigos de erro (SV_EXCEPTION_CLASS) -> catalogo/erros_supravizio.md
    dicionarios_de_classes*.xlsx  classes do produto (SV_CLASS)       -> catalogo/classes_supravizio.tsv
    modulos_sistema*.xlsx       módulos (SV_MODULE)                   -> catalogo/modulos_supravizio.tsv
"""
import argparse
import csv
import datetime
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parent.parent
CAT = RAIZ / "catalogo"


def linhas(caminho):
    ws = openpyxl.load_workbook(caminho, read_only=True, data_only=True).active
    rows = [[("" if c is None else str(c).replace("\xa0", " ").strip()) for c in r] for r in ws.iter_rows(values_only=True)]
    return rows[0], rows[1:]


def curta(nome):
    return nome.split(",")[0].split(".")[-1]


def erros(arq, amb, data):
    _, rows = linhas(arq)
    por_mod = defaultdict(list)
    for r in rows:
        ident, cod, msg, causa, efeito, acao = r[:6]
        id_classe = r[10] if len(r) > 10 else ""
        por_mod[cod[:2]].append((cod, msg, causa, efeito, acao, id_classe))
    nomes = {"SV": "Utilitários (SV)", "CF": "Configuração/Ativos (CF)", "RH": "Recurso (RH)",
             "PR": "Processo (PR)", "PT": "Portal (PT)", "RE": "Recurso? (RE, prefixo fora do padrão)"}
    md = ["# Códigos de erro do Supravizio",
          "Caminho: Catálogo > Erros do sistema", "",
          f"Importado de `SV_EXCEPTION_CLASS` ({amb}, {data}) por tools/importar_metadados.py: {len(rows)} códigos. "
          "Texto em colchetes (`[NomePapel]`, `[NomeAtividade]`) é parâmetro preenchido pelo sistema. O prefixo do código "
          "indica o módulo: SV Utilitários, CF Configuração (Ativos), RH Recurso, PR Processo, PT Portal. "
          "A coluna `Identificador Classe` da planilha liga o erro à classe de exceção em `catalogo/classes_supravizio.tsv`. "
          "As colunas 'originais' da planilha são idênticas às traduzidas.", ""]
    for mod in ("SV", "CF", "RH", "RE", "PR", "PT"):
        if mod not in por_mod:
            continue
        md.append(f"## {nomes[mod]}")
        for cod, msg, causa, efeito, acao, idc in sorted(por_mod[mod]):
            md += [f"### {cod} — {msg}",
                   f"- Causa: {causa}", f"- Efeito: {efeito}", f"- Ação: {acao}", ""]
    (CAT / "erros_supravizio.md").write_text("\n".join(md), encoding="utf-8")
    return len(rows)


def classes(arq, amb, data):
    _, rows = linhas(arq)
    with (CAT / "classes_supravizio.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["id_classe", "classe", "nome_completo", "descricao_resumida", "descricao", "log_modificacoes",
                    "tabela", "existe_na_versao", "ambiente", "data"])
        for r in rows:
            w.writerow([r[0], curta(r[1]), r[1], r[2], r[3].replace("\n", " "), r[4], r[5], r[6], amb, data])
    return len(rows)


def modulos(arq, amb, data):
    _, rows = linhas(arq)
    with (CAT / "modulos_supravizio.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["nome", "abreviatura", "ativo", "descricao_resumida", "descricao", "ambiente", "data"])
        for r in rows:
            w.writerow(r[:5] + [amb, data])
    return len(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("pasta")
    ap.add_argument("--ambiente", default="producao")
    ap.add_argument("--data", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    pasta = Path(a.pasta)
    feito = 0
    for padrao, fn, rotulo in (("Tabela_Erros*.xlsx", erros, "códigos de erro"),
                               ("dicionarios_de_classes*.xlsx", classes, "classes"),
                               ("modulos_sistema*.xlsx", modulos, "módulos")):
        for arq in sorted(pasta.glob(padrao)):
            print(f"{rotulo}: {fn(arq, a.ambiente, a.data)} registros ({arq.name})")
            feito += 1
    return 0 if feito else 1


if __name__ == "__main__":
    sys.exit(main())
