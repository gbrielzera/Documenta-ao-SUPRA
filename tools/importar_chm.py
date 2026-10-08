"""Importa para raw/ os tópicos que existem no Supravizio.chm mas não no site.

O CHM e o site têm o mesmo conteúdo; o CHM só traz algumas dezenas de tópicos a mais.
Primeiro descompacte o CHM (em uma pasta de caminho curto):
    hh.exe -decompile C:\\Temp\\chm C:\\Temp\\Supravizio.chm
Depois:
    python tools/importar_chm.py C:\\Temp\\chm
    python tools/converter.py && python tools/indexar.py
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "raw"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    origem = Path(sys.argv[1])
    existentes = {p.stem.lower() for p in RAW.glob("*.htm")}
    novos = []
    for p in sorted(origem.rglob("*.html")):
        nome = p.stem.lower()
        if nome in existentes:
            continue
        bruto = p.read_bytes()
        try:
            texto = bruto.decode("utf-8")
        except UnicodeDecodeError:
            texto = bruto.decode("cp1252", errors="replace")
        texto = re.sub(r"charset=[\w-]+", "charset=UTF-8", texto, count=1, flags=re.I)
        (RAW / f"{nome}.htm").write_text(texto, encoding="utf-8")
        novos.append(nome)
    (RAIZ / "raw_somente_chm.txt").write_text("\n".join(novos) + "\n", encoding="utf-8")
    print(f"{len(novos)} tópicos importados do CHM para raw/ (lista em raw_somente_chm.txt)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
