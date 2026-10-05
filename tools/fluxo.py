"""Resume os XMLs de fluxo exportados do Supravizio (ModeloImportacaoXml).

Uso:
  python tools/fluxo.py resumir "XMLs para teste/arquivo.xml" [...]   # gera fluxos/<nome>.md
  python tools/fluxo.py resumir --todos                               # todos os XMLs da pasta
  python tools/fluxo.py catalogo                                      # catalogo/ (biblioteca, campos, tabelas)
  python tools/fluxo.py bruto <xml> <Id|NOME_CAMPO>                   # despeja um elemento sem ruído

Cerca de 80% de cada XML é o catálogo global de campos customizados; o resumo
traz só o que o fluxo usa. Abra o XML original apenas via `bruto`.
"""
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA_XML = RAIZ / "XMLs para teste"
FLUXOS = RAIZ / "fluxos"
CATALOGO = RAIZ / "catalogo"
RUIDO = {"UseParentChangeLog", "isLoading", "isImporting"}
NIL = "{http://www.w3.org/2001/XMLSchema-instance}nil"
MARCA = "# INICIO SCRIPT USUARIO"
# valores que não merecem aparecer no resumo de uma atividade
PADRAO_ATIVIDADE = {
    "TipoFinalizacao": "Sucesso", "TipoCiclo": "Diario", "DisponibilidadeAplicacoes": "Todos",
    "UnidadeANO": "PercentualANS", "TipoMensagem": "Email", "Ativo": "true",
    "TipoAberturaLinkInicial": "ApenasChamador", "ReferenciaContagemTempo": "ExecucaoCorrente",
    "IncluiValidacaoFinal": "true", "PermiteVoltar": "true", "TransicaoAutomatica": "true",
    "PreencheMotivoReprovacao": "true", "PreencheClienteSolucionador": "true",
    "CicloSemanalDiaSemana": "Domingo",
}
PULAR_ATIVIDADE = {"Id", "Tipo", "SubProcessoId", "Descricao", "Referencia", "PapelResponsavelId",
                   "PapelDestinatarioId", "ModeloComunicadoId", "MotivoInterrupcaoSLAId",
                   "TipoSolicitacaoId", "ClassePesquisaSatisfacaoId"}
PADRAO_CAMPO = {
    "Coluna": "1", "FormaEdicaoWeb": "Formulario", "QtdColunasFormulario": "2",
    "PosicaoRotulo": "LadoEsquerdo", "PermiteEditarRegistros": "true",
    "PermiteExcluirRegistros": "true", "PermiteIncluirRegistros": "true",
    "ExibeAutoAtendimento": "true", "Habilitado": "true", "Visivel": "true", "VisivelAA": "true",
    "ExibeIncluirClienteAA": "true", "PermiteVariosFavorecidosPortal": "true",
    "PermiteOrdenacao": "true", "VisualizaAposEdicao": "true",
}
PULAR_CAMPO = {"Id", "OperacaoAtividadeId", "Sequencia", "Nome", "NomeCustomizado", "Rotulo",
               "Obrigatorio", "CampoPreenchimentoId"}
PADRAO_OPERACAO = {"Ativo": "true", "ObrigatoriedadeMotivo": "Reprovacao", "IniciaAutomatico": "true",
                   "BloquearPendencia": "true"}
PULAR_OPERACAO = {"Id", "OperacaoId", "AtividadeId", "Sequencia"}


def tag(e):
    return e.tag.split("}")[-1]


def carregar(caminho):
    txt = Path(caminho).read_bytes().decode("utf-8", errors="replace").lstrip("﻿")
    return ET.fromstring(txt)


def eh_script(txt):
    return bool(txt) and (MARCA in txt or txt.lstrip().startswith("import clr"))


def limpar_script(txt):
    """Remove o preâmbulo gerado pelo editor; mantém imports não triviais."""
    if MARCA not in txt:
        return txt.strip()
    cab, corpo = txt.split(MARCA, 1)
    extras = [l for l in cab.splitlines()
              if l.startswith("from Venki") and "import OrdemServico" not in l]
    return ("\n".join(extras) + "\n" if extras else "") + corpo.strip("\n").rstrip()


def html_para_texto(txt):
    txt = re.sub(r"<(style|script)\b.*?</\1>", "", txt or "", flags=re.I | re.S)
    txt = re.sub(r"<(br|/p|/div|/li)[^>]*>", "\n", txt, flags=re.I)
    txt = re.sub(r"<[^>]+>", "", txt)
    import html as _h
    txt = _h.unescape(txt).replace("\xa0", " ")
    return re.sub(r"\n\s*\n+", "\n", re.sub(r"[ \t]+", " ", txt)).strip()


def folhas(e, pular=(), padrao=None):
    """Filhos escalares relevantes: sem nil, vazios, 'false', ruído, scripts ou valores padrão."""
    r = {}
    for c in e:
        k = tag(c)
        if k in RUIDO or k in pular or len(c) or c.attrib.get(NIL) == "true":
            continue
        v = (c.text or "").strip()
        if not v or v == "false" or eh_script(v) or (padrao and padrao.get(k) == v):
            continue
        if v.startswith("<!DOCTYPE") or v.startswith("<p") or v.startswith("<span"):
            v = html_para_texto(v)
            if not v:
                continue
        r[k] = v
    return r


def fmt(d, limite=160):
    return "; ".join(f"{k}={v if len(v) <= limite else v[:limite] + '…'}" for k, v in d.items())


def scripts_de(e):
    """(nome, código) para cada filho direto que é script."""
    r = []
    for c in e:
        v = c.text or ""
        if not len(c) and eh_script(v):
            cod = limpar_script(v)
            if cod.strip():
                r.append((tag(c), cod))
    return r


def bloco_script(nome, cod, nivel="**"):
    return f"{nivel}{nome}{nivel}\n```python\n{cod}\n```"


# ---------------------------------------------------------------- campos customizados
def mapa_campos(root):
    """Nome -> CustomProperty, priorizando a classe OrdemServico."""
    mapa = {}
    membros = sorted(root.findall("ListaCustomProperty/CustomPropertyClassMember"),
                     key=lambda m: "OrdemServico" not in (m.findtext("ClassName") or ""))
    for m in membros:
        for cp in m.findall("CustomPropertyList/CustomProperty"):
            mapa.setdefault(cp.findtext("Name") or "", cp)
    return mapa


def desc_campo(cp):
    tipo = cp.findtext("Type") or ""
    ctrl = cp.findtext("Control") or ""
    tab, col = cp.findtext("TableName") or "", cp.findtext("TableColumn") or ""
    tam = cp.findtext("Length") or ""
    s = f"{ctrl} {tipo}" + (f"({tam})" if tam and tam != "0" and tipo == "String" else "")
    if tab:
        s += f" → {tab}.{col}"
    return s


def definicao_campo(nome, cp):
    linhas = [f"### {nome} — {cp.findtext('Text') or ''}", desc_campo(cp)]
    d = cp.findtext("Description") or ""
    if d and d != (cp.findtext("Text") or ""):
        linhas.append("Descrição: " + d[:400])
    itens = cp.findtext("ListItems") or ""
    if itens:
        linhas.append("Itens: " + (itens if len(itens) < 600 else itens[:600] + "…"))
    extras = folhas(cp, pular={"Id", "ClassId", "Name", "Text", "Description", "Type", "Control",
                               "TableName", "TableColumn", "Length", "ListItems", "DomainId",
                               "Sequence", "Width", "Height", "Enabled", "Visible", "ClassReferenceId",
                               "ShowInListView", "IsCripto", "Scopes"})
    if extras:
        linhas.append(fmt(extras))
    for nome_s, cod in scripts_de(cp):
        linhas.append(bloco_script(nome_s, cod))
    colunas = cp.findall("RecordColumns/RecordColumn")
    if colunas:
        linhas.append("Colunas do registro:")
        for rc in colunas:
            l = f"- {rc.findtext('Name')} \"{rc.findtext('Text') or ''}\" [{rc.findtext('Control')} {rc.findtext('Type')}]"
            it = rc.findtext("ListItems") or ""
            if it:
                l += " itens: " + (it if len(it) < 300 else it[:300] + "…")
            linhas.append(l)
            for nome_s, cod in scripts_de(rc):
                linhas.append(bloco_script(f"{rc.findtext('Name')}.{nome_s}", cod))
    return "\n".join(linhas)


# ---------------------------------------------------------------- resumo de um fluxo
def resumir(caminho):
    root = carregar(caminho)
    campos = mapa_campos(root)
    usados = []          # nomes de campos customizados, na ordem de uso
    papeis = {}          # PapelClasseNegocioId -> elemento
    out = []
    xml_rel = Path(caminho).resolve().relative_to(RAIZ).as_posix() \
        if RAIZ in Path(caminho).resolve().parents else str(caminho)
    desenho = None
    ds = root.findtext("DesenhoProcessoString")
    if ds:
        try:
            desenho = ET.fromstring(ds.lstrip("﻿"))
        except ET.ParseError:
            pass

    for spd in root.findall("ListaSubProcessoDiagrama/SubProcessoDiagramaXml"):
        sp = spd.find("SubProcesso")
        cls = sp.find("ClasseSubProcesso")
        nome = spd.findtext("NomeSubProcesso") or (cls.findtext("Descricao") if cls is not None else "")
        sigla = cls.findtext("Sigla") if cls is not None else ""
        versao = desenho.findtext("Versao") if desenho is not None else "?"
        out.append(f"# Fluxo: {nome} ({sigla}) — versão {versao}")
        out.append(f"Caminho: Fluxos > {Path(caminho).stem.replace('_', ' ')}")
        out.append(f"XML: `{xml_rel}` | Supravizio {root.findtext('VersaoSupravizio')} | "
                   f"SubProcessoId {sp.findtext('Id')} | DesenhoProcessoId {sp.findtext('DesenhoProcessoId')}"
                   + (f" | ProcessoId {desenho.findtext('ProcessoId')}" if desenho is not None else ""))
        if cls is not None:
            info = folhas(cls, pular={"Id", "Descricao", "Sigla", "DomainId", "OrgaoDonoId",
                                      "ResponsavelId", "FatorPrioridadeId", "Ativo"})
            dono = cls.findtext("OrgaoDono/Descricao")
            resp = cls.findtext("Responsavel/Nome")
            out.append(f"Órgão dono: {dono} | Responsável: {resp}")
            if info:
                out.append("Classe do subprocesso: " + fmt(info, 300))
            servs = [f"{r.findtext('Servico/Descricao')} ({r.findtext('Servico/Sigla')})"
                     for r in cls.findall("RestricoesServicos/RestricaoServico")]
            if servs:
                out.append("Serviços: " + "; ".join(servs))

        ativs = sp.findall("Atividades/Atividade")
        gws = sp.findall("Gateways/Gateway")
        rot = {}
        for a in ativs:
            rot[a.findtext("Id")] = f"[{a.findtext('Id')}] {a.findtext('Tipo')} \"{a.findtext('Descricao') or ''}\""
        for g in gws:
            rot["G" + g.findtext("Id")] = f"[G{g.findtext('Id')}] Gateway \"{g.findtext('Descricao') or ''}\""

        def curto(k):
            return rot.get(k, f"[{k}]").split(" ", 1)[0] + " " + rot.get(k, "").split('"')[1][:50] \
                if k in rot else f"[{k}]"

        # ---- grafo
        saidas = defaultdict(list)
        for a in ativs:
            for f in a.findall("FluxosSaida/FluxoSequencia"):
                d = f.findtext("AtividadeDestinoId")
                if d:
                    saidas[a.findtext("Id")].append(("", d))
        for g in gws:
            gid = "G" + g.findtext("Id")
            for r in g.findall("Entradas/Receptor"):
                o = r.findtext("AtividadeId") or ("G" + r.findtext("GatewayEntradaId") if r.findtext("GatewayEntradaId") else "")
                if o:
                    saidas[o].append(("", gid))
            for em in g.findall("Alternativas/Emissor"):
                d = em.findtext("AtividadeId") or ("G" + em.findtext("GatewaySaidaId") if em.findtext("GatewaySaidaId") else "")
                if d:
                    saidas[gid].append((em.findtext("ReferenciaDecision") or em.findtext("RotuloMotivo") or "", d))
        out.append("\n## Grafo do fluxo")
        for k in rot:
            dest = []
            arestas = list(dict.fromkeys(saidas.get(k, [])))
            rotulados = {d for r, d in arestas if r}
            for rotulo, d in arestas:
                if not rotulo and d in rotulados:
                    continue
                dest.append((f"«{rotulo}» " if rotulo else "") + curto(d))
            papel = ""
            if not k.startswith("G"):
                a = next(x for x in ativs if x.findtext("Id") == k)
                p = a.findtext("PapelResponsavel/Nome")
                papel = f" {{{p}}}" if p else ""
            out.append(f"- {rot[k]}{papel} → " + (" | ".join(dest) if dest else "(fim)"))

        # ---- gateways
        if gws:
            out.append("\n## Gateways")
            for g in gws:
                out.append(f"### [G{g.findtext('Id')}] {g.findtext('Descricao') or ''} ({g.findtext('Tipo')})")
                ex = folhas(g, pular={"Id", "Descricao", "Tipo", "SubProcessoId"})
                if ex:
                    out.append(fmt(ex))
                for n, cod in scripts_de(g):
                    out.append(bloco_script(n, cod))
                for em in g.findall("Alternativas/Emissor"):
                    d = em.findtext("AtividadeId") or ("G" + (em.findtext("GatewaySaidaId") or "?"))
                    ex = folhas(em, pular={"Id", "AtividadeId", "GatewayId", "GatewaySaidaId"},
                                padrao={"PermiteCancelarPubAA": "true"})
                    out.append(f"- alternativa → {curto(d)}: {fmt(ex)}")
                    for n, cod in scripts_de(em):
                        out.append(bloco_script(n, cod))

        # ---- atividades
        out.append("\n## Atividades")
        for a in ativs:
            out.append(f"\n### {rot[a.findtext('Id')]}")
            ref = html_para_texto(a.findtext("Referencia") or "")
            if ref:
                out.append("Referência: " + ref[:600])
            for rotulo, caminho_papel in (("Responsável", "PapelResponsavel"), ("Destinatário", "PapelDestinatario")):
                p = a.find(caminho_papel)
                if p is not None and len(p):
                    pid = p.findtext("PapelClasseNegocioId")
                    out.append(f"{rotulo}: {p.findtext('Nome')} (papel {pid})")
                    if p.find("PapelClasseNegocio") is not None:
                        papeis.setdefault(pid, p.find("PapelClasseNegocio"))
            conf = folhas(a, pular=PULAR_ATIVIDADE, padrao=PADRAO_ATIVIDADE)
            conf = {k: v for k, v in conf.items() if not k.startswith("Ciclo") or v != "true"}
            if conf:
                out.append("Config: " + fmt(conf))
            for sub, campo in (("ModeloComunicado", "Descricao"), ("MotivoInterrupcaoSLA", "Descricao"),
                               ("TipoSolicitacao", "Descricao"), ("ClassePesquisaSatisfacao", "Descricao"),
                               ("ClasseAnexoResposta", "Descricao")):
                v = a.findtext(f"{sub}/{campo}")
                if v:
                    out.append(f"{sub}: {v}")
            corpo = html_para_texto(a.findtext("ModeloComunicado/Corpo") or "")
            if corpo:
                out.append("Corpo do comunicado: " + corpo[:700] + ("…" if len(corpo) > 700 else ""))
            for n, cod in scripts_de(a):
                out.append(bloco_script(n, cod))

            for op in a.findall("Operacoes/OperacaoAtividade"):
                ex = folhas(op, pular=PULAR_OPERACAO, padrao=PADRAO_OPERACAO)
                out.append(f"- Operação {op.findtext('Operacao/Codigo')} {op.findtext('Operacao/Descricao')}"
                           + (f": {fmt(ex)}" if ex else ""))
                for n, cod in scripts_de(op):
                    out.append(bloco_script(n, cod))
                for grupo in ("Campos", "CamposAprovacao", "CamposPreenchimentoAprovacao"):
                    for c in op.findall(f"{grupo}/*"):
                        nome_c = c.findtext("NomeCustomizado") or c.findtext("Nome") or "?"
                        nativo = not c.findtext("NomeCustomizado")
                        cp = campos.get(nome_c) if not nativo else None
                        if cp is not None and nome_c not in usados:
                            usados.append(nome_c)
                        rotulo = c.findtext("Rotulo") or (cp.findtext("Text") if cp is not None else "")
                        l = f"  - {'(aprovação) ' if grupo != 'Campos' else ''}{nome_c}"
                        l += " (nativo)" if nativo else ""
                        l += f" \"{rotulo}\"" if rotulo else ""
                        l += f" [{desc_campo(cp)}]" if cp is not None else ""
                        l += " obrigatório" if c.findtext("Obrigatorio") == "true" else ""
                        ex = folhas(c, pular=PULAR_CAMPO, padrao=PADRAO_CAMPO)
                        l += f" — {fmt(ex)}" if ex else ""
                        out.append(l)
                        for n, cod in scripts_de(c):
                            out.append(bloco_script(f"{nome_c}.{n}", cod))
                        for reg in c.iter("CampoPreenchimentoRegistro"):
                            if reg.findtext("CampoPreenchimentoId") not in (None, c.findtext("Id")):
                                continue
                            ex = folhas(reg, pular=PULAR_CAMPO | {"PosicaoRotulo"}, padrao=PADRAO_CAMPO)
                            l = f"    - coluna {reg.findtext('Nome')}"
                            l += " obrigatório" if reg.findtext("Obrigatorio") == "true" else ""
                            l += f" — {fmt(ex)}" if ex else ""
                            out.append(l)
                            for n, cod in scripts_de(reg):
                                out.append(bloco_script(f"{nome_c}.{reg.findtext('Nome')}.{n}", cod))
                for ca in op.findall("ClassesAnexos/ClasseAnexo"):
                    ex = folhas(ca, pular={"Id", "OperacaoAtividadeId", "Descricao", "Sequencial"},
                                padrao={"ConfiguracaoUsuarios": "Nenhuma", "IncluirQRCode": "true"})
                    classes = [x.findtext("ClasseConfiguracao/Descricao") or x.findtext("ClasseConfiguracaoId")
                               for x in ca.findall("EscopoClasses/EscopoClasseAnexo")]
                    out.append(f"  - anexo \"{ca.findtext('Descricao') or ''}\" classes: {', '.join(c for c in classes if c)}"
                               + (f" — {fmt(ex)}" if ex else ""))
                for ca in op.findall("ClassesAprovacao/ClasseAprovacao"):
                    out.append(f"  - item para aprovação \"{ca.findtext('Descricao') or ''}\"")
                for ap in op.findall("Aprovadores/Aprovador"):
                    out.append(f"  - aprovador: {ap.findtext('PapelAprovador/Nome')} ({ap.findtext('Hierarquia')})")
                    pc = ap.find("PapelAprovador/PapelClasseNegocio")
                    if pc is not None:
                        papeis.setdefault(ap.findtext("PapelAprovador/PapelClasseNegocioId"), pc)
                for rel in op.findall("Relatorios/*"):
                    out.append(f"  - relatório: {fmt(folhas(rel, pular={'Id', 'OperacaoAtividadeId'}))}")

            # coleções menos comuns: despejo genérico
            for col in ("ValoresInputs", "PassagemItens", "RetornoItens", "ClientesAutorizados", "Acoes",
                        "Opcoes", "Relatorios", "TiposAnexosMensagem"):
                itens = a.findall(f"{col}/*")
                if not itens:
                    continue
                out.append(f"- {col}:")
                for it in itens:
                    d = folhas(it, pular={"Id", "AtividadeId"})
                    for sub in it:
                        if len(sub) and tag(sub) not in RUIDO:
                            ds_ = sub.findtext("Descricao") or sub.findtext("Nome") or sub.findtext("Name")
                            if ds_:
                                d[tag(sub)] = ds_
                    out.append(f"  - {fmt(d)}")
                    for n, cod in scripts_de(it):
                        out.append(bloco_script(n, cod))
            assoc = a.find("Associacao")
            if assoc is not None and len(assoc):
                out.append("- Associação: " + fmt(folhas(assoc, pular={"Id", "DomainId", "ClasseAlvoId", "ClasseFonteId"}))
                           + f" | fonte: {assoc.findtext('ClasseFonte/Descricao')} → alvo: {assoc.findtext('ClasseAlvo/Descricao')}")
            for asub in a.findall("AssociacoesSubprocesso/AssociacaoSubprocesso"):
                d = folhas(asub, pular={"AtividadeId"})
                for sub in asub.iter():
                    if tag(sub) in ("Nome", "FraseAssociacao") and sub.text:
                        d.setdefault(tag(sub), sub.text.strip())
                out.append("- Associação de subprocesso: " + fmt(d))

    # ---- papéis
    if papeis:
        out.append("\n## Papéis usados")
        for pid, p in papeis.items():
            ex = folhas(p, pular={"Id", "Nome", "DomainId", "Referencia"},
                        padrao={"Ativo": "true", "ExcluiAprovacoes": "true", "SomenteUltimaExecucao": "true",
                                "AtorGrupoTrabalho": "TodosMembros", "ClasseNegocio": "OrdemServico",
                                "OpcaoCampoOcorrencia": "Pessoa", "PessoaItemConfiguracao": "ResponsavelUsuario",
                                "EnvolvimentoAtividadeExecutada": "Final"})
            pessoas = [x.findtext("Pessoa/Nome") for x in p.findall("RelacaoPessoas/PessoaPapel")]
            out.append(f"### papel {pid}: {p.findtext('Nome')}")
            out.append(fmt(ex) + (f" | pessoas: {', '.join(x for x in pessoas if x)}" if pessoas else ""))
            for n, cod in scripts_de(p):
                out.append(bloco_script(n, cod))
            for comp in p.findall(".//PapelComposicao"):
                out.append(f"- composto por: {comp.findtext('Nome')} ({comp.findtext('Tipo')})")

    # ---- campos customizados usados
    if usados:
        out.append("\n## Campos customizados usados (definição global)")
        for n in usados:
            out.append("\n" + definicao_campo(n, campos[n]))

    # ---- funções da biblioteca chamadas
    texto = "\n".join(out)
    libs = [m.findtext("Name") for m in root.findall("ListaBibliotecaScript/ScriptModule")]
    chamadas = sorted(n for n in libs if n and re.search(r"\b" + re.escape(n) + r"\b", texto))
    if chamadas:
        out.append("\n## Biblioteca de scripts referenciada\n" + ", ".join(chamadas)
                   + "\n(fonte em catalogo/biblioteca/<Nome>.py)")
    return "\n".join(out) + "\n"


def nome_saida(caminho):
    return re.sub(r"[^\w\-.]+", "_", Path(caminho).stem, flags=re.U).strip("_") + ".md"


def cmd_resumir(args):
    arquivos = sorted(PASTA_XML.glob("*.xml")) if "--todos" in args else [Path(a) for a in args]
    FLUXOS.mkdir(exist_ok=True)
    tot_in = tot_out = 0
    for arq in arquivos:
        try:
            md = resumir(arq)
        except Exception as e:  # um XML ruim não deve parar o lote
            print(f"ERRO {arq.name}: {type(e).__name__}: {e}")
            continue
        dest = FLUXOS / nome_saida(arq)
        dest.write_text(md, encoding="utf-8")
        tot_in += arq.stat().st_size
        tot_out += len(md.encode("utf-8"))
        if len(arquivos) <= 5:
            print(f"{arq.name}: {arq.stat().st_size/1e6:.1f} MB -> {len(md)/1e3:.0f} KB ({dest.relative_to(RAIZ).as_posix()})")
    print(f"{len(arquivos)} XMLs: {tot_in/1e6:.0f} MB -> {tot_out/1e6:.2f} MB em fluxos/")


# ---------------------------------------------------------------- catálogo global
RE_TABELA = re.compile(r"\b(?:FROM|JOIN|UPDATE|INTO)\s+([A-Za-z_][\w$.]*)", re.I)
NAO_TABELA = {"SELECT", "SET", "DUAL", "THE", "WHERE", "TABLE", "VALUES"}


def cmd_catalogo(_args):
    (CATALOGO / "biblioteca").mkdir(parents=True, exist_ok=True)
    arquivos = sorted(PASTA_XML.glob("*.xml"), key=lambda p: p.stat().st_mtime)
    libs, campos, variantes = {}, {}, defaultdict(set)
    tabelas = Counter()
    onde = defaultdict(set)
    sql_vistos = set()
    for arq in arquivos:  # o mais recente sobrescreve
        root = carregar(arq)
        for sm in root.findall("ListaBibliotecaScript/ScriptModule"):
            n, src = sm.findtext("Name") or "", sm.findtext("Source") or ""
            libs[n] = (src, arq.name)
            variantes[n].add(hash(src))
        for m in root.findall("ListaCustomProperty/CustomPropertyClassMember"):
            classe = (m.findtext("ClassName") or "").split(",")[0].split(".")[-1]
            for cp in m.findall("CustomPropertyList/CustomProperty"):
                campos[(classe, cp.findtext("Name"))] = cp
        for e in root.iter():
            t = e.text or ""
            if len(e) or len(t) < 20 or tag(e) == "DesenhoProcessoString" \
                    or not re.search(r"\b(select|update|insert)\b", t, re.I):
                continue
            h = hash(t)
            if h in sql_vistos:  # o mesmo script aparece em vários XMLs
                continue
            sql_vistos.add(h)
            sem_imports = re.sub(r"^\s*(from\s+\S+\s+import|import)\b.*$", "", t, flags=re.M)
            for nome in {n.upper().rstrip(".") for n in RE_TABELA.findall(sem_imports)}:
                if nome in NAO_TABELA or len(nome) < 3:
                    continue
                tabelas[nome] += 1
                onde[nome].add(tag(e))

    for n, (src, origem) in libs.items():
        nome_arq = re.sub(r"[^\w\-]+", "_", n) + ".py"
        (CATALOGO / "biblioteca" / nome_arq).write_text(
            f"# {n}\n# Caminho: Catálogo > Biblioteca de scripts > {n}\n"
            f"# Fonte: {origem}" + (f" ({len(variantes[n])} variantes entre os XMLs; esta é a mais recente)"
                                    if len(variantes[n]) > 1 else "") + f"\n\n{src.strip()}\n",
            encoding="utf-8")

    linhas = ["classe\tnome\trotulo\ttipo\tcontrole\ttabela\tcoluna\ttamanho\tlookup\titens"]
    por_tabela = defaultdict(list)
    for (classe, nome), cp in sorted(campos.items(), key=lambda x: (x[0][0], x[0][1] or "")):
        itens = (cp.findtext("ListItems") or "").replace("\t", " ").replace("\n", " ")
        tab = cp.findtext("TableName") or ""
        linhas.append("\t".join([
            classe, nome or "", (cp.findtext("Text") or "").replace("\t", " ").replace("\n", " "),
            cp.findtext("Type") or "", cp.findtext("Control") or "", tab,
            cp.findtext("TableColumn") or "", cp.findtext("Length") or "",
            "S" if (cp.findtext("LookupScript") or "").strip() else "",
            itens[:120]]))
        if tab:
            por_tabela[(tab, classe)].append(f"{cp.findtext('TableColumn')} ({cp.findtext('Type')})")
    (CATALOGO / "campos.tsv").write_text("\n".join(linhas) + "\n", encoding="utf-8")

    md = ["# Tabelas de campos customizados (CPE_*)", "Caminho: Catálogo > Banco > Tabelas customizadas", "",
          "Uma linha por tabela física que guarda campos customizados, com a classe dona e as colunas.",
          "Detalhe de cada campo: `catalogo/campos.tsv` (grep pelo nome).", ""]
    for (tab, classe), cols in sorted(por_tabela.items()):
        md.append(f"- **{tab}** ({classe}, {len(cols)} colunas): " + ", ".join(sorted(set(cols))))
    (CATALOGO / "tabelas_customizadas.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    md = ["# Tabelas e views referenciadas em SQL nos fluxos reais",
          "Caminho: Catálogo > Banco > Tabelas usadas em SQL", "",
          "Extraído de todos os scripts dos XMLs (FROM/JOIN/UPDATE/INTO). Número = scripts distintos que a citam.",
          "Tabelas ausentes do modelo de dados oficial (docs/dados_*.md) são views ou tabelas do cliente.", ""]
    for nome, n in tabelas.most_common():
        doc = (RAIZ / "docs" / f"dados_{nome.lower()}.md").exists()
        md.append(f"- {nome}: {n}" + (" — docs/dados_" + nome.lower() + ".md" if doc else ""))
    (CATALOGO / "tabelas_usadas_em_sql.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"catálogo: {len(libs)} módulos de biblioteca, {len(campos)} campos, "
          f"{len(por_tabela)} tabelas customizadas, {len(tabelas)} tabelas citadas em SQL")


# ---------------------------------------------------------------- despejo sem ruído
def despejar(e, nivel=0, limite=4000):
    v = (e.text or "").strip()
    if e.attrib.get(NIL) == "true" or tag(e) in RUIDO or (not len(e) and (not v or v == "false")):
        return
    if eh_script(v):
        v = "\n" + limpar_script(v)
    elif v.startswith("<"):
        v = html_para_texto(v)
    print("  " * nivel + tag(e) + (": " + v[:limite] if v else ""))
    for c in e:
        despejar(c, nivel + 1, limite)


def cmd_bruto(args):
    root = carregar(args[0])
    alvo = args[1]
    for e in root.iter():
        if tag(e) in ("Atividade", "Gateway", "CustomProperty", "OperacaoAtividade", "ScriptModule",
                      "PapelClasseNegocio", "CampoPreenchimento"):
            if e.findtext("Id") == alvo or e.findtext("Name") == alvo or e.findtext("NomeCustomizado") == alvo:
                despejar(e)
                return
    print("não encontrado")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("resumir", "catalogo", "bruto"):
        print(__doc__)
        return 1
    {"resumir": cmd_resumir, "catalogo": cmd_catalogo, "bruto": cmd_bruto}[sys.argv[1]](sys.argv[2:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
