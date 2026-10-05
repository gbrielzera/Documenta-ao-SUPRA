"""Mascara credenciais fixas em catalogo/ e fluxos/ (rodar depois de fluxo.py e antes de commitar).

Uso: python tools/mascarar.py [--verificar]
  --verificar: só lista o que seria mascarado (sai com código 1 se houver algo)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTAS = ("catalogo", "fluxos", "guias")
MASCARA = "***MASCARADO***"
# nome = "valor"  (senha, token, usuário, login...)
RE_ATRIB = re.compile(
    r"""(?ix)
    (\b\w*(?:password|passwd|senha|secret|api[_-]?key|token|username|user|usuario|login|pwd)\w*
     \s*[=:]\s*)(["'])([^"'\n]{4,})\2""")
RE_AUTH = re.compile(r"(?i)\b(Basic|Bearer)\s+([A-Za-z0-9+/=._-]{16,})")
RE_JWT = re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]*")
RE_URLCRED = re.compile(r"(?i)\b([a-z][a-z0-9+.-]*://[^/\s:@]+):([^@\s/]{3,})@")
# rótulos que contêm "user" mas não são credenciais
IGNORAR_NOME = re.compile(r"(?i)USER_JE_SOURCE_NAME|UsuarioRede|USUARIO_REDE|UsuarioAutoAtendimento")


def mascarar(texto):
    n = 0

    def atrib(m):
        nonlocal n
        if IGNORAR_NOME.search(m.group(1)) or m.group(3) == MASCARA:
            return m.group(0)
        n += 1
        return f"{m.group(1)}{m.group(2)}{MASCARA}{m.group(2)}"

    def auth(m):
        nonlocal n
        n += 1
        return f"{m.group(1)} {MASCARA}"

    def jwt(m):
        nonlocal n
        n += 1
        return MASCARA

    def url(m):
        nonlocal n
        n += 1
        return f"{m.group(1)}:{MASCARA}@"

    texto = RE_ATRIB.sub(atrib, texto)
    texto = RE_AUTH.sub(auth, texto)
    texto = RE_JWT.sub(jwt, texto)
    texto = RE_URLCRED.sub(url, texto)
    return texto, n


def main():
    so_verificar = "--verificar" in sys.argv
    total = 0
    for pasta in PASTAS:
        for p in sorted((RAIZ / pasta).rglob("*")):
            if not p.is_file() or p.suffix not in (".md", ".py", ".tsv", ".txt"):
                continue
            original = p.read_text(encoding="utf-8")
            novo, n = mascarar(original)
            if n:
                total += n
                print(f"{p.relative_to(RAIZ).as_posix()[:80]}: {n}")
                if not so_verificar:
                    p.write_text(novo, encoding="utf-8")
    print(f"{'a mascarar' if so_verificar else 'mascarados'}: {total}")
    return 1 if (so_verificar and total) else 0


if __name__ == "__main__":
    sys.exit(main())
