"""Consulta a base de conhecimento do Supravizio empacotada na skill (assets/kb.sqlite, somente leitura).

Uso (a partir da pasta da skill):
  python scripts/kb.py buscar "termos" [-t doc,fluxo,catalogo,guia] [-n 8]
  python scripts/kb.py ler docs/objeto_db.md [--de 1 --ate 120]
  python scripts/kb.py listar fluxos/
Tipos: doc (documentação oficial), fluxo (resumos dos fluxos reais), catalogo (API de scripts, biblioteca de
scripts do cliente, erros, classes), guia (guias escritos à mão). Os caminhos que a busca imprime
(arquivo:linha) são os mesmos que o comando `ler` aceita.
"""
import argparse
import re
import sqlite3
import sys
from pathlib import Path

BANCO = Path(__file__).resolve().parent.parent / "assets" / "kb.sqlite"
PARADAS = set("a o e de da do das dos em no na nos nas um uma para por com como que se ao aos os as ou é the of to in".split())


def abrir():
    if not BANCO.exists():
        sys.exit(f"banco não encontrado: {BANCO}")
    return sqlite3.connect(BANCO.as_uri() + "?mode=ro", uri=True)


def consulta(termos, operador):
    return f" {operador} ".join('"' + t.replace('"', "") + '"*' for t in termos)


def buscar(a):
    termos = [t for t in re.findall(r"[\w.]+", a.texto, re.U) if t.lower() not in PARADAS]
    termos = [p for t in termos for p in ([t] if "." not in t else t.split(".")) if p]
    if not termos:
        print("nenhum termo útil")
        return 1
    filtro, params = "", []
    if a.t:
        tipos = [t.strip() for t in a.t.split(",") if t.strip()]
        filtro = f" AND tipo IN ({','.join('?' * len(tipos))})"
        params = tipos
    con = abrir()
    sql = ("SELECT tipo, arquivo, linha, titulo, caminho, "
           f"snippet(kb, 5, '', '', ' … ', {a.c}) FROM kb WHERE kb MATCH ?" + filtro +
           " ORDER BY bm25(kb, 0, 0, 0, 12.0, 4.0, 1.0) LIMIT ?")
    try:
        linhas = con.execute(sql, [consulta(termos, "AND"), *params, a.n]).fetchall()
        completas = len(linhas)
        if completas < a.n and len(termos) > 1:
            vistos = {(l[1], l[2]) for l in linhas}
            for l in con.execute(sql, [consulta(termos, "OR"), *params, a.n * 2]).fetchall():
                if (l[1], l[2]) not in vistos and len(linhas) < a.n:
                    linhas.append(l)
    except sqlite3.OperationalError as e:
        print(f"erro na busca ({e}). Se o SQLite local não tem FTS5, use grep em references/.")
        return 1
    if not linhas:
        print("sem resultados")
        return 0
    for i, (tipo, arquivo, linha, titulo, caminho, trecho) in enumerate(linhas):
        if i == completas and len(termos) > 1:
            print("-- correspondências parciais --")
        local = caminho if caminho and caminho != titulo else ""
        print(f"[{tipo}] {arquivo}:{linha} — {titulo}" + (f"  ({local})" if local else ""))
        print("    " + re.sub(r"\s+", " ", trecho).strip())
    return 0


def ler(a):
    arq = a.arquivo.replace("\\", "/").lstrip("./")
    con = abrir()
    partes = con.execute("SELECT corpo FROM kb WHERE arquivo = ? ORDER BY linha", (arq,)).fetchall()
    if not partes:
        print(f"'{arq}' não está no banco. Páginas de uma propriedade só não são indexadas: veja objetos_<classe>.md. "
              "Use `listar` para conferir o nome.")
        return 1
    linhas = "\n".join(p[0] for p in partes).split("\n")
    ini = max(1, a.de)
    fim = a.ate if a.ate else min(len(linhas), ini + 299)
    print("\n".join(linhas[ini - 1:fim]))
    if fim < len(linhas):
        print(f"\n[... linhas {ini}-{fim} de {len(linhas)}; continue com --de {fim + 1}]")
    return 0


def listar(a):
    con = abrir()
    pref = a.prefixo.replace("\\", "/").lstrip("./")
    for (arq,) in con.execute("SELECT DISTINCT arquivo FROM kb WHERE arquivo LIKE ? ORDER BY arquivo", (pref + "%",)):
        print(arq)
    return 0


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    b = sp.add_parser("buscar")
    b.add_argument("texto")
    b.add_argument("-n", type=int, default=8)
    b.add_argument("-t", default="")
    b.add_argument("-c", type=int, default=24)
    b.set_defaults(fn=buscar)
    r = sp.add_parser("ler")
    r.add_argument("arquivo")
    r.add_argument("--de", type=int, default=1)
    r.add_argument("--ate", type=int, default=0)
    r.set_defaults(fn=ler)
    l = sp.add_parser("listar")
    l.add_argument("prefixo")
    l.set_defaults(fn=listar)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
