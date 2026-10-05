"""Monta kb.sqlite (FTS5) com docs/, fluxos/ e catalogo/.

Uso: python tools/indexar.py
"""
import re
import sqlite3
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BANCO = RAIZ / "kb.sqlite"
# pasta -> (tipo, extensões)
FONTES = {
    "docs": ("doc", (".md",)),
    "fluxos": ("fluxo", (".md",)),
    "catalogo": ("catalogo", (".md", ".py", ".sql")),
    "guias": ("guia", (".md",)),
}
MAX_TRECHO = 6000  # páginas maiores são divididas por título


def trechos(texto):
    """Divide um documento grande em seções (## / ###) de tamanho razoável."""
    if len(texto) <= MAX_TRECHO:
        return [("", texto)]
    partes, atual, secao = [], [], ""
    for linha in texto.split("\n"):
        if re.match(r"#{2,4} ", linha) and sum(len(l) for l in atual) > 1500:
            partes.append((secao, "\n".join(atual)))
            atual, secao = [], linha.lstrip("# ").strip()
        atual.append(linha)
    partes.append((secao, "\n".join(atual)))
    return partes


def main():
    if BANCO.exists():
        BANCO.unlink()
    con = sqlite3.connect(BANCO)
    con.execute(
        "CREATE VIRTUAL TABLE kb USING fts5("
        "tipo UNINDEXED, arquivo UNINDEXED, linha UNINDEXED, titulo, caminho, corpo, "
        "tokenize=\"unicode61 remove_diacritics 2 tokenchars '_'\")")
    total = {}
    for pasta, (tipo, exts) in FONTES.items():
        base = RAIZ / pasta
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if p.suffix.lower() not in exts or p.name.startswith("_"):
                continue
            texto = p.read_text(encoding="utf-8", errors="replace")
            if tipo == "doc" and p.name.startswith("prop_") and len(texto) < 350:
                continue  # página de uma propriedade só: o conteúdo já está em objetos_<classe>.md
            m = re.match(r"# (.+)", texto)
            titulo = m.group(1).strip() if m else p.stem
            m = re.search(r"^Caminho: (.+)$", texto, re.M)
            caminho = m.group(1).strip() if m else ""
            rel = p.relative_to(RAIZ).as_posix()
            pos = 0
            for secao, corpo in trechos(texto):
                linha = texto.count("\n", 0, texto.find(corpo, pos)) + 1
                pos = texto.find(corpo, pos) + len(corpo)
                con.execute("INSERT INTO kb VALUES (?,?,?,?,?,?)",
                            (tipo, rel, linha, titulo + (" — " + secao if secao else ""),
                             caminho, corpo))
                total[tipo] = total.get(tipo, 0) + 1
    con.commit()
    con.execute("INSERT INTO kb(kb) VALUES ('optimize')")
    con.commit()
    con.close()
    print("indexado:", ", ".join(f"{k}={v}" for k, v in total.items()),
          f"| {BANCO.stat().st_size/1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
