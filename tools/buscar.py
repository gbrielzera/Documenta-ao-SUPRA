"""Busca na base de conhecimento do Supravizio (kb.sqlite).

Uso:
  python tools/buscar.py "termos da busca"            # top 8, todos os tipos
  python tools/buscar.py "ExecuteDataTable" -n 5 -t doc
  python tools/buscar.py "reembolso gateway" -t fluxo,catalogo

Tipos: doc (documentação oficial), fluxo (resumos dos XMLs), catalogo
(scripts/campos/tabelas extraídos dos XMLs), guia (guias destilados).
A saída traz arquivo:linha para abrir só o trecho necessário.
"""
import argparse
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

BANCO = Path(__file__).resolve().parent.parent / "kb.sqlite"
PARADAS = set("a o e de da do das dos em no na nos nas um uma para por com como que se ao aos "
              "os as ou é the of to in".split())


def consulta(termos, operador):
    return f" {operador} ".join('"' + t.replace('"', "") + '"*' for t in termos)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("texto")
    ap.add_argument("-n", type=int, default=8, help="quantidade de resultados")
    ap.add_argument("-t", default="", help="tipos separados por vírgula")
    ap.add_argument("-c", type=int, default=24, help="tamanho do trecho (palavras)")
    a = ap.parse_args()

    termos = [t for t in re.findall(r"[\w.]+", a.texto, re.U) if t.lower() not in PARADAS]
    # "Utils.ExecuteDataTable" -> busca também pelas partes
    termos = [p for t in termos for p in ([t] if "." not in t else t.split(".")) if p]
    if not termos:
        print("nenhum termo útil")
        return 1
    filtro, params = "", []
    if a.t:
        tipos = [t.strip() for t in a.t.split(",") if t.strip()]
        filtro = f" AND tipo IN ({','.join('?' * len(tipos))})"
        params = tipos
    if not BANCO.exists():  # ambiente novo (clone do GitHub): o índice não é versionado
        print("kb.sqlite não encontrado; criando o índice (alguns segundos)...", file=sys.stderr)
        subprocess.run([sys.executable, "-X", "utf8", str(BANCO.parent / "tools" / "indexar.py")],
                       check=True)
    con = sqlite3.connect(BANCO)
    sql = ("SELECT tipo, arquivo, linha, titulo, caminho, "
           f"snippet(kb, 5, '', '', ' … ', {a.c}) "
           "FROM kb WHERE kb MATCH ?" + filtro +
           " ORDER BY bm25(kb, 0, 0, 0, 12.0, 4.0, 1.0) LIMIT ?")
    # primeiro as páginas com todos os termos; completa com correspondências parciais
    linhas = con.execute(sql, [consulta(termos, "AND"), *params, a.n]).fetchall()
    completas = len(linhas)
    if completas < a.n and len(termos) > 1:
        vistos = {(l[1], l[2]) for l in linhas}
        for l in con.execute(sql, [consulta(termos, "OR"), *params, a.n * 2]).fetchall():
            if (l[1], l[2]) not in vistos and len(linhas) < a.n:
                linhas.append(l)
    if not linhas:
        print("sem resultados")
        return 0
    for i, (tipo, arquivo, linha, titulo, caminho, trecho) in enumerate(linhas):
        if i == completas and len(termos) > 1:
            print("-- correspondências parciais --")
        trecho = re.sub(r"\s+", " ", trecho).strip()
        local = caminho if caminho and caminho != titulo else ""
        print(f"[{tipo}] {arquivo}:{linha} — {titulo}" + (f"  ({local})" if local else ""))
        print(f"    {trecho}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
