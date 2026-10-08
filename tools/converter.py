"""Converte raw/*.htm (Help & Manual) em docs/*.md enxutos e gera docs/_INDICE.md.

Uso: python tools/converter.py
"""
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "raw"
DOCS = RAIZ / "docs"
TOC = "supravizio_content.htm"
IGNORAR = {TOC, "supravizio_ftsearch.htm", "supravizio_kwindex.htm", "supravizio.htm"}
BLOCOS = ("p", "h1", "h2", "h3", "h4", "li")
RE_RECUO = re.compile(r"(?:text-indent|padding-left|margin-left)\s*:\s*(\d+)px")
RE_LARGURA = re.compile(r"\s*width\s*:\s*(\d+)px")
MARCADORES = {"•", "·", "o", "-", "–", "§", "▪", "■"}


class Conversor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.saida = []      # blocos finais: (tipo, texto)
        self.buf = []        # texto do bloco corrente
        self.codigo = False  # parágrafo de código
        self.mono = 0        # caracteres em fonte monoespaçada no bloco
        self.total = 0       # caracteres visíveis no bloco
        self.recuo = ""      # indentação do parágrafo (código)
        self.spans = []      # pilha de (negrito, mono, indentacao)
        self.link = None
        self.ignorar = 0     # dentro de <script>/<style>
        self.tabelas = []    # pilha de tabelas: lista de linhas
        self.linhas = []     # pilha de linhas em construção
        self.celulas = []    # pilha de células em construção
        self.titulo = None   # nível do heading corrente

    def _emitir(self, bloco, tipo="p"):
        if not bloco.strip():
            return
        if self.celulas:
            self.celulas[-1].append((tipo, bloco))
        else:
            self.saida.append((tipo, bloco))

    def _fechar_bloco(self):
        t = "".join(self.buf).replace("\xa0", " ")
        self.buf = []
        if not self.codigo and not self.titulo and self.total and self.mono / self.total >= 0.6:
            self.codigo = True
            t = t.replace("**", "")
        if self.codigo:
            self._emitir(self.recuo + t.rstrip(), "code")
        else:
            t = re.sub(r"\s+", " ", t).strip()
            if t and self.titulo:
                self._emitir("#" * self.titulo + " " + t.replace("**", ""), "h")
            else:
                self._emitir(t)
        self.codigo = False
        self.titulo = None
        self.recuo = ""
        self.mono = self.total = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        estilo = a.get("style") or ""
        if tag in ("script", "style"):
            self.ignorar += 1
        elif tag in BLOCOS:
            self._fechar_bloco()
            classe = a.get("class") or ""
            self.codigo = "CodeExample" in classe
            m = RE_RECUO.search(estilo)
            self.recuo = " " * (int(m.group(1)) // 12) if m else ""
            if tag[0] == "h" or "Heading" in classe:
                m = re.search(r"Heading(\d)", classe)
                self.titulo = (int(m.group(1)) if m else int(tag[1])) + 1
        elif tag == "br":
            self.buf.append("\n" if self.codigo else " ")
        elif tag == "span":
            negrito = "bold" in estilo and not self.codigo and not self.titulo
            mono = any(f in estilo for f in ("Courier", "Consolas", "monospace"))
            m = RE_LARGURA.match(estilo)
            self.spans.append((negrito, mono, bool(m)))
            if m:
                self.buf.append(" " * (int(m.group(1)) // 12))
            if negrito:
                self.buf.append("**")
        elif tag == "a":
            href = a.get("href") or ""
            if href.startswith("http"):
                self.link = href
            elif href and not href.startswith(("javascript", "#", "mailto")):
                self.link = re.sub(r"\.html?(#.*)?$", "", href.lower())
            if self.link:
                self.buf.append("[")
        elif tag == "table":
            self._fechar_bloco()
            self.tabelas.append([])
        elif tag == "tr" and self.tabelas:
            self.linhas.append([])
        elif tag in ("td", "th") and self.linhas:
            self._fechar_bloco()
            self.celulas.append([])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.ignorar = max(0, self.ignorar - 1)
        elif tag in BLOCOS:
            self._fechar_bloco()
        elif tag == "span" and self.spans:
            if self.spans.pop()[0]:
                self.buf.append("**")
        elif tag == "a" and self.link:
            self.buf.append(f"]({self.link})")
            self.link = None
        elif tag in ("td", "th") and self.celulas:
            self._fechar_bloco()
            self.linhas[-1].append(self.celulas.pop())
        elif tag == "tr" and self.linhas:
            linha = self.linhas.pop()
            if any(linha):
                self.tabelas[-1].append(linha)
        elif tag == "table" and self.tabelas:
            self._fechar_bloco()
            self._fechar_tabela(self.tabelas.pop())

    def _fechar_tabela(self, linhas):
        if not linhas:
            return
        colunas = max(len(l) for l in linhas)
        # tabela usada como marcador de lista: "• | texto"
        if colunas == 2 and all(
                len(l) == 2 and "".join(b for _, b in l[0]).strip() in MARCADORES for l in linhas):
            for l in linhas:
                blocos = l[1]
                if blocos and all(t != "code" for t, _ in blocos):
                    self._emitir("- " + " ".join(b.strip() for _, b in blocos), "li")
                else:
                    for t, b in blocos:
                        self._emitir(b, t)
            return
        # tabela de layout (uma coluna) ou contendo blocos de código: vira blocos soltos
        tem_codigo = any(sum(1 for t, _ in c if t == "code") > 1 for l in linhas for c in l)
        if colunas == 1 or tem_codigo:
            for l in linhas:
                for c in l:
                    for t, b in c:
                        self._emitir(b, t)
            return
        md = []
        for i, l in enumerate(linhas):
            cels = [" ".join("`" + b.strip() + "`" if t == "code" else b.strip() for t, b in c)
                    .replace("|", "\\|").replace("\n", " ") for c in l]
            md.append("| " + " | ".join(cels) + " |")
            if i == 0:
                md.append("|" + "---|" * len(cels))
        self._emitir("\n".join(md), "table")

    def handle_data(self, data):
        if self.ignorar:
            return
        if self.spans and self.spans[-1][2]:
            return  # span de indentação: o espaçamento já foi inserido
        if not self.codigo:
            data = data.replace("\r", " ").replace("\n", " ")
        visiveis = len(data.replace("\xa0", "").strip())
        self.total += visiveis
        if any(s[1] for s in self.spans):
            self.mono += visiveis
        self.buf.append(data)


def limpar_negrito(t):
    t = re.sub(r"\*\*(\s*)\*\*", r"\1", t)
    t = re.sub(r"(\s+)\*\*(?=\W|$)", r"**\1", t)
    return re.sub(r"\*{4,}", "", t)


def converter(html_txt):
    m = re.search(r"<title>(.*?)</title>", html_txt, re.S | re.I)
    caminho = html.unescape(m.group(1)).strip() if m else ""
    i = html_txt.find("<!--ZOOMRESTART-->")
    c = Conversor()
    c.feed(html_txt[i:] if i >= 0 else html_txt)
    c._fechar_bloco()
    partes, cod, lista = [], [], []

    def descarregar():
        if cod:
            partes.append("```\n" + "\n".join(cod).strip("\n") + "\n```")
            cod.clear()
        if lista:
            partes.append("\n".join(lista))
            lista.clear()

    for tipo, bloco in c.saida:
        if tipo == "code":
            if lista:
                descarregar()
            cod.append(bloco)
        elif tipo == "li":
            if cod:
                descarregar()
            lista.append(limpar_negrito(bloco))
        else:
            descarregar()
            partes.append(bloco if tipo == "table" else limpar_negrito(bloco))
    descarregar()
    return caminho, "\n\n".join(p for p in partes if p.strip())


def indice():
    """Árvore do sumário: uma linha por tópico, indentada pelo nível."""
    toc = (RAW / TOC).read_text(encoding="utf-8", errors="replace")
    linhas = []
    padrao = re.compile(
        r'<(ul|/ul)\b|<a\s[^>]*href="([^"#]+)\.htm[^"]*"[^>]*>(.*?)</a>', re.S | re.I)
    nivel = 0
    for m in padrao.finditer(toc):
        if m.group(1):
            nivel += 1 if m.group(1).lower() == "ul" else -1
            continue
        arquivo = m.group(2).lower()
        titulo = html.unescape(re.sub(r"<[^>]+>", "", m.group(3))).strip()
        if titulo and arquivo + ".htm" not in IGNORAR:
            linhas.append("  " * max(0, nivel - 1) + f"- {titulo} ({arquivo})")
    return linhas


def main():
    DOCS.mkdir(exist_ok=True)
    n = bytes_in = bytes_out = 0
    for p in sorted(RAW.glob("*.htm")):
        if p.name.lower() in IGNORAR:
            continue
        bruto = p.read_text(encoding="utf-8", errors="replace")
        caminho, corpo = converter(bruto)
        nome = caminho.split(" > ")[-1] if caminho else p.stem
        md = f"# {nome}\n\nCaminho: {caminho}\n\n{corpo}\n"
        (DOCS / (p.stem.lower() + ".md")).write_text(md, encoding="utf-8")
        n += 1
        bytes_in += len(bruto)
        bytes_out += len(md)
    # alguns tópicos do CHM têm "_" no fim do nome e os links apontam sem ele
    nomes = {p.stem for p in DOCS.glob("*.md")}
    for p in DOCS.glob("*.md"):
        t = p.read_text(encoding="utf-8")
        novo = re.sub(r"\]\(([a-z0-9_\-]+)\)",
                      lambda m: f"]({m.group(1)}_)" if m.group(1) not in nomes and m.group(1) + "_" in nomes else m.group(0), t)
        if novo != t:
            p.write_text(novo, encoding="utf-8")
    arv = indice()
    (DOCS / "_INDICE.md").write_text(
        "# Sumário da documentação — título (arquivo em docs/, sem .md)\n\n"
        + "\n".join(arv) + "\n", encoding="utf-8")
    print(f"{n} páginas: {bytes_in/1e6:.1f} MB de HTML -> {bytes_out/1e6:.1f} MB de Markdown; "
          f"índice com {len(arv)} entradas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
