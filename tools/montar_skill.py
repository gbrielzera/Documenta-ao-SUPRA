"""Monta a skill do Claude a partir do projeto: skill-build/supravizio/ e dist/supravizio.skill.

Uso:  python tools/montar_skill.py [--sem-indexar]

Layout da skill gerada:
  SKILL.md                 de skill-src/SKILL.md
  scripts/kb.py            de skill-src/scripts/kb.py (busca e leitura no banco)
  assets/kb.sqlite         índice FTS5 de docs/, fluxos/, catalogo/ e guias/ (gerado por tools/indexar.py)
  references/guias/        guias/*.md
  references/catalogo/     tabelas e catálogos pequenos (tsv, schema, erros...)
  references/docs/_INDICE.md, references/fluxos/_INDICE.md
Rode antes: mascarar.py --verificar (a skill leva o mesmo conteúdo do repositório, sem credenciais).
"""
import re
import shutil
import sqlite3
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "skill-src"
SAIDA = RAIZ / "skill-build" / "supravizio"
DIST = RAIZ / "dist"
CATALOGO = ["campos_banco.tsv", "campos.tsv", "schema_real.tsv", "schema.txt", "dicionario_dll.tsv",
            "classes_supravizio.tsv", "modulos_supravizio.tsv", "tabelas_customizadas.md",
            "tabelas_usadas_em_sql.md", "campos_vs_banco.md", "erros_supravizio.md"]


def adaptar(texto):
    """Comandos de manutenção do projeto viram os da skill."""
    texto = re.sub(r"python(?: -X utf8)? tools/buscar\.py", "python scripts/kb.py buscar", texto)
    return texto


RE_EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@(?:bbts|bbtecno)\.com\.br", re.I)
RE_RESP = re.compile(r"(Responsável: )[A-ZÀ-Ú][A-ZÀ-Ú .'-]{5,}")
RE_PESSOAS = re.compile(r"(\| pessoas: )[^\n]+")


def mascarar_pessoais(banco):
    """A skill não precisa de e-mails corporativos nem de nomes de pessoas: troca por marcadores só no pacote."""
    con = sqlite3.connect(banco)
    trocas = {"email": 0, "responsavel": 0, "pessoas": 0}
    for rowid, corpo in con.execute("SELECT rowid, corpo FROM kb").fetchall():
        novo = corpo
        novo, n1 = RE_EMAIL.subn("<email-corporativo>", novo)
        novo, n2 = RE_RESP.subn(lambda m: m.group(1) + "<nome>", novo)
        novo, n3 = RE_PESSOAS.subn(lambda m: m.group(1) + "<omitidas>", novo)
        if novo != corpo:
            con.execute("UPDATE kb SET corpo = ? WHERE rowid = ?", (novo, rowid))
            trocas["email"] += n1
            trocas["responsavel"] += n2
            trocas["pessoas"] += n3
    con.execute("INSERT INTO kb(kb) VALUES ('optimize')")
    con.commit()
    con.execute("VACUUM")
    con.close()
    return trocas


def main():
    if "--sem-indexar" not in sys.argv:
        subprocess.run([sys.executable, "-X", "utf8", str(RAIZ / "tools" / "indexar.py")], check=True)
    if SAIDA.parent.exists():
        shutil.rmtree(SAIDA.parent)
    (SAIDA / "scripts").mkdir(parents=True)
    (SAIDA / "assets").mkdir()
    ref = SAIDA / "references"
    for sub in ("guias", "catalogo", "docs", "fluxos"):
        (ref / sub).mkdir(parents=True)

    shutil.copy2(FONTE / "SKILL.md", SAIDA / "SKILL.md")
    shutil.copy2(FONTE / "scripts" / "kb.py", SAIDA / "scripts" / "kb.py")
    shutil.copy2(RAIZ / "kb.sqlite", SAIDA / "assets" / "kb.sqlite")
    print("mascarado no pacote:", mascarar_pessoais(SAIDA / "assets" / "kb.sqlite"))
    for g in sorted((RAIZ / "guias").glob("*.md")):
        (ref / "guias" / g.name).write_text(adaptar(g.read_text(encoding="utf-8")), encoding="utf-8")
    for nome in CATALOGO:
        shutil.copy2(RAIZ / "catalogo" / nome, ref / "catalogo" / nome)
    shutil.copy2(RAIZ / "docs" / "_INDICE.md", ref / "docs" / "_INDICE.md")
    shutil.copy2(RAIZ / "fluxos" / "_INDICE.md", ref / "fluxos" / "_INDICE.md")

    DIST.mkdir(exist_ok=True)
    destino = DIST / "supravizio.skill"
    if destino.exists():
        destino.unlink()
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(SAIDA.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                z.write(p, Path("supravizio") / p.relative_to(SAIDA))
    arquivos = [p for p in SAIDA.rglob("*") if p.is_file()]
    bruto = sum(p.stat().st_size for p in arquivos)
    print(f"skill: {len(arquivos)} arquivos, {bruto / 1e6:.1f} MB; pacote {destino.stat().st_size / 1e6:.1f} MB em {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
