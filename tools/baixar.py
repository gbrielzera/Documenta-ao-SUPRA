"""Baixa a documentação do Supravizio (help.supravizio.com) para raw/.

Uso: python tools/baixar.py
Retomável: páginas já baixadas são puladas. Segue também links internos
para tópicos que não aparecem no sumário.
"""
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = "https://help.supravizio.com/"
RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "raw"
TOC = "supravizio_content.htm"
WORKERS = 6
HREF = re.compile(r'href="([^"#?:]+\.htm)(?:#[^"]*)?"', re.I)


def baixar(nome):
    destino = RAW / nome
    if destino.exists() and destino.stat().st_size > 0:
        return nome, "ok"
    for tentativa in range(4):
        try:
            req = urllib.request.Request(BASE + nome, headers={"User-Agent": "kb-supravizio/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                destino.write_bytes(r.read())
            return nome, "novo"
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return nome, "404"
            time.sleep(2 * (tentativa + 1))
        except Exception:
            time.sleep(2 * (tentativa + 1))
    return nome, "falha"


def links(nome):
    try:
        html = (RAW / nome).read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return set()
    return {h.lower() for h in HREF.findall(html) if "/" not in h}


def main():
    RAW.mkdir(exist_ok=True)
    baixar(TOC)
    fila = links(TOC)
    vistos = {TOC}
    falhas = []
    rodada = 0
    while fila:
        rodada += 1
        lote = sorted(fila - vistos)
        vistos |= fila
        fila = set()
        print(f"rodada {rodada}: {len(lote)} páginas", flush=True)
        with ThreadPoolExecutor(WORKERS) as ex:
            for i, (nome, status) in enumerate(ex.map(baixar, lote), 1):
                if status in ("falha", "404"):
                    falhas.append(f"{nome}\t{status}")
                else:
                    fila |= links(nome) - vistos
                if i % 250 == 0:
                    print(f"  {i}/{len(lote)}", flush=True)
    (RAIZ / "raw_falhas.txt").write_text("\n".join(falhas), encoding="utf-8")
    total = sum(1 for _ in RAW.glob("*.htm"))
    print(f"fim: {total} arquivos em raw/, {len(falhas)} falhas (raw_falhas.txt)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
