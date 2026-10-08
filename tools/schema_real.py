"""Incorpora ao projeto o schema REAL do banco, a partir de um export de ALL_TAB_COLUMNS.

Formato esperado (colunas separadas por TAB, uma coluna por linha, sem cabeçalho; a primeira coluna
pode vir vazia):  [vazio]  TABELA  COLUNA  TIPO  TAMANHO  NULAVEL(Y/N)
Gerado por:
    SELECT table_name, column_name, data_type, data_length, nullable
    FROM all_tab_columns WHERE owner = USER AND table_name IN (...) ORDER BY table_name, column_id;

Uso:
    python tools/schema_real.py <export.txt> [--ambiente producao] [--data 2026-10-08]

Saídas:
    catalogo/schema_real.tsv   tabela, coluna, ordem, tipo, tamanho, nulo, ambiente, data
                               (reexportar uma tabela substitui as linhas dela; as outras são mantidas)
    (o cruzamento com os campos dos XMLs é feito por tools/campos_banco.py)
"""
import argparse
import csv
import datetime
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TSV = RAIZ / "catalogo" / "schema_real.tsv"
CABECALHO = ["tabela", "coluna", "ordem", "tipo", "tamanho", "nulo", "ambiente", "data"]


def ler_export(caminho):
    tabelas = defaultdict(list)
    for linha in Path(caminho).read_text(encoding="utf-8-sig").splitlines():
        c = [x.strip() for x in linha.split("\t")]
        while c and c[0] == "":
            c.pop(0)
        if len(c) < 5 or c[0].upper() == "TABLE_NAME":
            continue
        tabelas[c[0].upper()].append(c[1:5])
    return tabelas


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("export")
    ap.add_argument("--ambiente", default="producao")
    ap.add_argument("--data", default=datetime.date.fromtimestamp(Path(sys.argv[1]).stat().st_mtime).isoformat()
                    if len(sys.argv) > 1 and Path(sys.argv[1]).exists() else "")
    a = ap.parse_args()

    novas = ler_export(a.export)
    if not novas:
        print("nenhuma linha reconhecida")
        return 1

    existentes = defaultdict(list)
    if TSV.exists():
        with TSV.open(encoding="utf-8", newline="") as f:
            for r in csv.reader(f, delimiter="\t"):
                if r and r[0] != "tabela":
                    existentes[r[0]].append(r)
    for tab, cols in novas.items():
        existentes[tab] = [[tab, c[0], str(i), c[1], c[2], c[3], a.ambiente, a.data]
                           for i, c in enumerate(cols, 1)]
    TSV.parent.mkdir(exist_ok=True)
    with TSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(CABECALHO)
        for tab in sorted(existentes):
            w.writerows(existentes[tab])

    print(f"schema_real.tsv: {sum(len(v) for v in existentes.values())} colunas em {len(existentes)} tabelas "
          f"(+{len(novas)} desta carga, ambiente {a.ambiente})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
