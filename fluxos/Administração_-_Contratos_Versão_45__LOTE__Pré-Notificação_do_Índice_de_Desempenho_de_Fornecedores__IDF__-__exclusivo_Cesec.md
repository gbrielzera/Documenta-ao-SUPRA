# Fluxo: [LOTE] Pré-Notificação do Índice de Desempenho de Fornecedores (IDF) - (exclusivo Cesec) (IDF) — versão 45
Caminho: Fluxos > Administração - Contratos Versão 45 [LOTE] Pré-Notificação do Índice de Desempenho de Fornecedores (IDF) - (exclusivo Cesec)
XML: `XMLs para teste/Administração_-_Contratos_Versão_45_[LOTE]_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_-_(exclusivo_Cesec).xml` | Supravizio 19.1.1 | SubProcessoId 21990 | DesenhoProcessoId 3021 | ProcessoId 127
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=[LOTE] Pré-Notificação do Índice de Desempenho de Fornecedores (IDF) - (exclusivo Cesec); CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Pré-Notificação do Índice de Desempenho de Fornecedores (IDF)  (IDFSERVICO)

## Grafo do fluxo
- [349141] EventoInicial "" {Cliente} → [349143] Abertura da associada
- [349142] EventoFinal "" → (fim)
- [349143] SubProcesso "Abertura da associada" {Cliente} → [349144] Finalização
- [349144] EventoIntermediarioMensagem "Finalização" → [349142] 

## Atividades

### [349141] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"IDFSERVICO"}
TipoSolicitacao: 05.04. Suprimentos Corporativos, Licitações e Contratos - Contratos
- Operação PR0004 Associar Itens Configuração
  - anexo "Planilha" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CHECKBOX1 "Clique aqui para ler a planilha" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]
**CHECKBOX1.ScriptModificado**
```python
from Venki.Services.Dictionary.Custom import Culture
if Controle.Valor == True:

    if OrdemServico.PossuiItem("ARQUIVO"):

        import clr
        import System

        clr.AddReference("System")
        clr.AddReference("System.Core")
        clr.AddReference("System.Xml")
        clr.AddReference("System.Xml.Linq")
        clr.AddReference("System.IO.Compression")
        clr.AddReference("System.IO.Compression.FileSystem")

        from System import DBNull, Convert, Char
        from System.Globalization import CultureInfo
        from System.IO import File, MemoryStream
        from System.IO.Compression import ZipArchive, ZipArchiveMode
        from System.Xml.Linq import XDocument


        # ============================================================
        # FUNÇÕES AUXILIARES
        # ============================================================

        def Texto(valor):
            try:
                if valor is None:
                    return ""

                if valor == DBNull.Value:
                    return ""

                texto = Convert.ToString(valor)

                if texto is None:
                    return ""

                texto = texto.Trim()

                if texto == "":
                    return ""

                return texto

            except:
                try:
                    texto = valor.ToString()

                    if texto is None:
                        return ""

                    return texto.Trim()

                except:
                    return ""


        def Inteiro(valor):
            try:
                texto = Texto(valor)

                if texto == "":
                    raise Exception(
                        "IDF não informado."
                    )

                texto = texto.Replace(",", ".")

                return Convert.ToInt32(
                    Convert.ToDouble(
                        texto,
                        CultureInfo.InvariantCulture
                    )
                )

            except Exception as ex:
                raise Exception(
                    "IDF inválido: '{0}'. {1}".format(
                        Texto(valor),
                        Texto(ex)
                    )
                )


        def NormalizarDGCO(valor):
            texto = Texto(valor)

            if texto == "":
                return ""

            texto = texto.Replace(",", ".").Trim()

            if texto.EndsWith(".0"):
                texto = texto.Substring(
                    0,
                    texto.Length - 2
                )

            return texto


        def GridPossuiDGCO(dgco):
            try:
                grid = OrdemServico.GetCustom(
                    "GRID_IDF"
                )

                for linhaGrid in grid.Rows:
                    try:
                        dgcoGrid = Texto(
                            linhaGrid["DGCO"]
                        )

                        if (
                            dgcoGrid.ToUpper() ==
                            dgco.ToUpper()
                        ):
                            return True

                    except:
                        pass

            except:
                pass

            return False


        def ObterEntradaZip(zipArquivo, caminho):
            try:
                caminhoNormalizado = caminho.Replace(
                    "\\",
                    "/"
                )

                return zipArquivo.GetEntry(
                    caminhoNormalizado
                )

            except:
                return None


        def LerDocumentoXml(zipArquivo, caminho):
            entrada = ObterEntradaZip(
                zipArquivo,
                caminho
            )

            if entrada is None:
                return None

            stream = None

            try:
                stream = entrada.Open()

                return XDocument.Load(
                    stream
                )

            finally:
                try:
                    if stream is not None:
                        stream.Close()
                except:
                    pass


        def NomeLocal(elemento):
            try:
                return Texto(
                    elemento.Name.LocalName
                )

            except:
                return ""


        def Atributo(elemento, nome):
            try:
                atributo = elemento.Attribute(
                    nome
                )

                if atributo is None:
                    return ""

                return Texto(
                    atributo.Value
                )

            except:
                return ""


        def ElementosPorNome(documentoOuElemento, nome):
            encontrados = []

            try:
                for elemento in documentoOuElemento.Descendants():
                    try:
                        if NomeLocal(elemento) == nome:
                            encontrados.append(
                                elemento
                            )

                    except:
                        pass

            except:
                pass

            return encontrados


        def PrimeiroFilho(elemento, nome):
            if elemento is None:
                return None

            try:
                for filho in elemento.Elements():
                    try:
                        if NomeLocal(filho) == nome:
                            return filho

                    except:
                        pass

            except:
                pass

            return None


        def TextoCompleto(elemento):
            try:
                if elemento is None:
                    return ""

                return Texto(
                    elemento.Value
                )

            except:
                return ""


        def IndiceColuna(referencia):
            # Exemplos:
            # A2  -> 0
            # B2  -> 1
            # AA2 -> 26

            try:
                referenciaTexto = Texto(
                    referencia
                )

                letras = ""

                for caractere in referenciaTexto:
                    if Char.IsLetter(caractere):
                        letras += Convert.ToString(
                            caractere
                        ).ToUpper()
                    else:
                        break

                if letras == "":
                    return -1

                resultado = 0

                for letra in letras:
                    codigoLetra = ord(letra)

                    resultado = (
                        resultado * 26 +
                        codigoLetra -
                        ord("A") +
                        1
                    )

                return resultado - 1

            except:
                return -1


        # ============================================================
        # LEITURA DIRETA DO XLSX
        # ============================================================

        def LerXlsx(caminhoArquivo):

            arquivoBytes = File.ReadAllBytes(
                caminhoArquivo
            )

            memoria = MemoryStream(
                arquivoBytes
            )

            zipArquivo = ZipArchive(
                memoria,
                ZipArchiveMode.Read
            )

            try:
                # ====================================================
                # SHARED STRINGS
                # ====================================================

                sharedStrings = []

                documentoShared = LerDocumentoXml(
                    zipArquivo,
                    "xl/sharedStrings.xml"
                )

                if documentoShared is not None:

                    elementosSi = ElementosPorNome(
                        documentoShared,
                        "si"
                    )

                    for si in elementosSi:
                        try:
                            valorShared = Texto(
                                si.Value
                            )

                        except:
                            valorShared = TextoCompleto(
                                si
                            )

                        sharedStrings.append(
                            valorShared
                        )


                # ====================================================
                # FUNÇÃO PARA LER UMA CÉLULA
                # ====================================================

                def ValorCelula(celula):
                    try:
                        tipoCelula = Atributo(
                            celula,
                            "t"
                        )

                        valorFinal = ""


                        # --------------------------------------------
                        # SHARED STRING
                        # --------------------------------------------

                        if tipoCelula == "s":

                            elementoValor = PrimeiroFilho(
                                celula,
                                "v"
                            )

                            if elementoValor is not None:
                                try:
                                    indiceTexto = Convert.ToInt32(
                                        Texto(
                                            elementoValor.Value
                                        )
                                    )

                                    if (
                                        indiceTexto >= 0 and
                                        indiceTexto < len(sharedStrings)
                                    ):
                                        valorFinal = Texto(
                                            sharedStrings[indiceTexto]
                                        )

                                except:
                                    valorFinal = ""


                        # --------------------------------------------
                        # TEXTO INLINE
                        # --------------------------------------------

                        elif tipoCelula == "inlineStr":

                            elementoInline = PrimeiroFilho(
                                celula,
                                "is"
                            )

                            if elementoInline is not None:
                                try:
                                    valorFinal = Texto(
                                        elementoInline.Value
                                    )

                                except:
                                    valorFinal = TextoCompleto(
                                        elementoInline
                                    )


                        # --------------------------------------------
                        # STRING DIRETA
                        # --------------------------------------------

                        elif tipoCelula == "str":

                            elementoValor = PrimeiroFilho(
                                celula,
                                "v"
                            )

                            if elementoValor is not None:
                                valorFinal = Texto(
                                    elementoValor.Value
                                )


                        # --------------------------------------------
                        # NÚMERO, BOOLEANO OU VALOR COMUM
                        # --------------------------------------------

                        else:

                            elementoValor = PrimeiroFilho(
                                celula,
                                "v"
                            )

                            if elementoValor is not None:
                                valorFinal = Texto(
                                    elementoValor.Value
                                )


                        return Texto(
                            valorFinal
                        )

                    except:
                        return ""


                # ====================================================
                # LEITURA DAS LINHAS DE UMA ABA
                # ====================================================

                def LerLinhasAba(documentoAba):

                    resultado = []

                    linhasXml = ElementosPorNome(
                        documentoAba,
                        "row"
                    )

                    for linhaXml in linhasXml:

                        numeroLinhaTexto = Atributo(
                            linhaXml,
                            "r"
                        )

                        try:
                            numeroLinha = Convert.ToInt32(
                                numeroLinhaTexto
                            )

                        except:
                            numeroLinha = 0


                        valoresLinha = [
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            ""
                        ]


                        for celula in linhaXml.Elements():

                            if NomeLocal(celula) != "c":
                                continue

                            referencia = Atributo(
                                celula,
                                "r"
                            )

                            indice = IndiceColuna(
                                referencia
                            )

                            if indice < 0 or indice > 6:
                                continue

                            valoresLinha[indice] = ValorCelula(
                                celula
                            )


                        resultado.append({
                            "NUMERO": numeroLinha,
                            "VALORES": valoresLinha
                        })


                    return resultado


                # ====================================================
                # PROCURA AS ABAS DIRETAMENTE
                # ====================================================

                abaEncontrada = ""
                linhasEncontradas = None


                for entrada in zipArquivo.Entries:

                    try:
                        caminhoEntrada = Texto(
                            entrada.FullName
                        ).Replace(
                            "\\",
                            "/"
                        )

                        caminhoMinusculo = caminhoEntrada.ToLower()

                        if not caminhoMinusculo.StartsWith(
                            "xl/worksheets/"
                        ):
                            continue

                        if not caminhoMinusculo.EndsWith(
                            ".xml"
                        ):
                            continue


                        streamAba = None

                        try:
                            streamAba = entrada.Open()

                            documentoAba = XDocument.Load(
                                streamAba
                            )

                        finally:
                            try:
                                if streamAba is not None:
                                    streamAba.Close()
                            except:
                                pass


                        linhasAba = LerLinhasAba(
                            documentoAba
                        )

                        if len(linhasAba) == 0:
                            continue


                        # ---------------------------------------------
                        # PROCURA O CABEÇALHO
                        # ---------------------------------------------

                        indiceCabecalho = -1

                        limiteBusca = len(linhasAba)

                        if limiteBusca > 20:
                            limiteBusca = 20


                        for indiceLinha in range(
                            0,
                            limiteBusca
                        ):

                            valoresCabecalho = linhasAba[
                                indiceLinha
                            ]["VALORES"]

                            primeiraColuna = Texto(
                                valoresCabecalho[0]
                            ).ToUpper()

                            quartaColuna = Texto(
                                valoresCabecalho[3]
                            ).ToUpper()

                            sextaColuna = Texto(
                                valoresCabecalho[5]
                            ).ToUpper()

                            setimaColuna = Texto(
                                valoresCabecalho[6]
                            ).ToUpper()


                            if (
                                primeiraColuna == "DGCO" and
                                quartaColuna == "IDF"
                            ):
                                indiceCabecalho = indiceLinha
                                break


                            if (
                                primeiraColuna == "DGCO" and
                                (
                                    sextaColuna.Contains("RISCO") or
                                    setimaColuna.Contains("QUALIDADE")
                                )
                            ):
                                indiceCabecalho = indiceLinha
                                break


                        if indiceCabecalho >= 0:

                            linhasEncontradas = []

                            for indiceDados in range(
                                indiceCabecalho + 1,
                                len(linhasAba)
                            ):
                                linhasEncontradas.append(
                                    linhasAba[
                                        indiceDados
                                    ]["VALORES"]
                                )

                            abaEncontrada = caminhoEntrada
                            break


                    except:
                        continue


                # ====================================================
                # FALLBACK PARA PLANILHA SEM CABEÇALHO
                # ====================================================

                if linhasEncontradas is None:

                    for entrada in zipArquivo.Entries:

                        try:
                            caminhoEntrada = Texto(
                                entrada.FullName
                            ).Replace(
                                "\\",
                                "/"
                            )

                            caminhoMinusculo = caminhoEntrada.ToLower()

                            if not caminhoMinusculo.StartsWith(
                                "xl/worksheets/"
                            ):
                                continue

                            if not caminhoMinusculo.EndsWith(
                                ".xml"
                            ):
                                continue


                            streamAba = None

                            try:
                                streamAba = entrada.Open()

                                documentoAba = XDocument.Load(
                                    streamAba
                                )

                            finally:
                                try:
                                    if streamAba is not None:
                                        streamAba.Close()
                                except:
                                    pass


                            linhasAba = LerLinhasAba(
                                documentoAba
                            )

                            if len(linhasAba) == 0:
                                continue


                            primeiraLinha = linhasAba[0][
                                "VALORES"
                            ]

                            primeiroDGCO = Texto(
                                primeiraLinha[0]
                            )


                            if primeiroDGCO.Contains("/"):

                                linhasEncontradas = []

                                for registro in linhasAba:
                                    linhasEncontradas.append(
                                        registro["VALORES"]
                                    )

                                abaEncontrada = (
                                    caminhoEntrada +
                                    " (sem cabeçalho)"
                                )

                                break


                        except:
                            continue


                if linhasEncontradas is None:
                    raise Exception(
                        "Não foi possível localizar uma aba com os "
                        "cabeçalhos DGCO e IDF, nem uma aba cuja "
                        "primeira coluna contenha valores no formato "
                        "00000/0000."
                    )


                return (
                    abaEncontrada,
                    linhasEncontradas
                )


            finally:
                try:
                    zipArquivo.Dispose()
                except:
                    pass

                try:
                    memoria.Dispose()
                except:
                    pass


        # ============================================================
        # LOCALIZAÇÃO DO ARQUIVO
        # ============================================================

        repositorio = Utils.ExecuteScalar(
            "select FILES_PATH from SERVICES_PARAM"
        )

        anexo = OrdemServico.ObtemItem(
            "ARQUIVO"
        )

        caminhoArquivo = (
            Texto(repositorio) +
            "\\" +
            Texto(anexo.Localizacao)
        )

        posBarra = caminhoArquivo.LastIndexOf(
            "\\"
        )

        if posBarra >= 0:
            nomeArquivo = caminhoArquivo.Substring(
                posBarra + 1
            )
        else:
            nomeArquivo = caminhoArquivo


        posPonto = nomeArquivo.LastIndexOf(
            "."
        )

        if posPonto >= 0:
            extensao = nomeArquivo.Substring(
                posPonto
            ).ToLower()
        else:
            extensao = ""


        # ============================================================
        # INICIALIZAÇÃO
        # ============================================================

        totalLinhas = 0
        adicionadas = 0
        duplicadas = 0
        erros = 0
        linhasVazias = 0
        ignoradasPorIdf = 0

        detalhes = ""
        nomeAbaEncontrada = ""


        # ============================================================
        # IMPORTAÇÃO
        # ============================================================

        try:
            if extensao != ".xlsx":
                raise Exception(
                    "Esta versão da importação aceita somente XLSX. "
                    "Salve a planilha no formato .xlsx."
                )


            nomeAbaEncontrada, linhasExcel = LerXlsx(
                caminhoArquivo
            )


            for valoresLinha in linhasExcel:

                totalLinhas += 1

                try:
                    dgco = NormalizarDGCO(
                        valoresLinha[0]
                    )

                    fornecedor = Texto(
                        valoresLinha[1]
                    )

                    status = Texto(
                        valoresLinha[2]
                    )

                    idfTexto = Texto(
                        valoresLinha[3]
                    )

                    ultimoPeriodo = Texto(
                        valoresLinha[4]
                    )

                    riscoApurado = Texto(
                        valoresLinha[5]
                    )

                    qualidadeIdf = Texto(
                        valoresLinha[6]
                    )


                    # ------------------------------------------------
                    # LINHA VAZIA
                    # ------------------------------------------------

                    if (
                        dgco == "" and
                        fornecedor == "" and
                        status == "" and
                        idfTexto == "" and
                        ultimoPeriodo == "" and
                        riscoApurado == "" and
                        qualidadeIdf == ""
                    ):
                        linhasVazias += 1
                        continue


                    # ------------------------------------------------
                    # VALIDAÇÕES
                    # ------------------------------------------------

                    if dgco == "":
                        raise Exception(
                            "DGCO não informado."
                        )

                    if fornecedor == "":
                        raise Exception(
                            "FORNECEDOR não informado."
                        )

                    if idfTexto == "":
                        raise Exception(
                            "IDF não informado."
                        )


                    idf = Inteiro(
                        idfTexto
                    )


                    # ------------------------------------------------
                    # FILTRO DO IDF
                    # Importa somente IDF menor ou igual a 60.
                    # ------------------------------------------------

                    if idf > 60:

                        ignoradasPorIdf += 1

                        if ignoradasPorIdf <= 20:
                            detalhes += (
                                "\nLinha {0} ignorada: "
                                "IDF {1} é maior que 60. "
                                "DGCO={2}; FORNECEDOR={3}."
                            ).format(
                                totalLinhas,
                                idf,
                                dgco,
                                fornecedor
                            )

                        continue


                    # ------------------------------------------------
                    # DUPLICIDADE
                    # ------------------------------------------------

                    if GridPossuiDGCO(dgco):

                        duplicadas += 1

                        if duplicadas <= 20:
                            detalhes += (
                                "\nLinha {0} ignorada: "
                                "DGCO {1} já existe na GRID_IDF."
                            ).format(
                                totalLinhas,
                                dgco
                            )

                        continue


                    # ------------------------------------------------
                    # ADICIONA NA GRID
                    # ------------------------------------------------

                    OrdemServico.AdicionaLinhaRegistro(
                        "GRID_IDF",
                        [
                            "DGCO",
                            "FORNECEDOR",
                            "STATUS",
                            "IDF",
                            "ULTIMO_PERIODO",
                            "RISCO_APURADO",
                            "QUALIDADE_IDF"
                        ],
                        [
                            dgco,
                            fornecedor,
                            status,
                            idf,
                            ultimoPeriodo,
                            riscoApurado,
                            qualidadeIdf
                        ]
                    )

                    adicionadas += 1


                    if adicionadas <= 10:
                        detalhes += (
                            "\nLinha {0} adicionada: "
                            "DGCO={1}; "
                            "IDF={2}; "
                            "RISCO_APURADO={3}; "
                            "QUALIDADE_IDF={4}"
                        ).format(
                            totalLinhas,
                            dgco,
                            idf,
                            riscoApurado,
                            qualidadeIdf
                        )


                except Exception as exLinha:

                    erros += 1

                    if erros <= 30:
                        detalhes += (
                            "\nErro na linha {0}: {1}"
                        ).format(
                            totalLinhas,
                            Texto(exLinha)
                        )


            # ========================================================
            # COMPLEMENTO DOS CONTADORES DO LOG
            # ========================================================

            if erros > 30:
                detalhes += (
                    "\nExistem mais {0} erro(s) "
                    "não exibidos no resumo."
                ).format(
                    erros - 30
                )


            if duplicadas > 20:
                detalhes += (
                    "\nExistem mais {0} duplicidade(s) "
                    "não exibidas no resumo."
                ).format(
                    duplicadas - 20
                )


            if ignoradasPorIdf > 20:
                detalhes += (
                    "\nExistem mais {0} linha(s) com "
                    "IDF maior que 60 não exibidas no resumo."
                ).format(
                    ignoradasPorIdf - 20
                )


        except Exception as ex:

            erros += 1

            detalhes += (
                "\nErro geral da importação: " +
                Texto(ex)
            )


        # ============================================================
        # TOTAL DA GRID
        # ============================================================

        totalGrid = 0

        try:
            totalGrid = OrdemServico.GetCustom(
                "GRID_IDF"
            ).Rows.Count

        except:
            pass


        # ============================================================
        # RESUMO
        # ============================================================

        resumo = (
            "Importação concluída!\n\n"
            "Arquivo: {0}\n"
            "Aba utilizada: {1}\n"
            "Método de leitura: Open XML / Unicode\n"
            "Regra aplicada: importar somente IDF menor ou igual a 60\n"
            "Linhas lidas: {2}\n"
            "Linhas vazias/ignoradas: {3}\n"
            "Ignoradas por IDF maior que 60: {4}\n"
            "Adicionadas: {5}\n"
            "Duplicadas: {6}\n"
            "Erros: {7}\n"
            "Total na GRID_IDF: {8}\n\n"
            "Detalhes:{9}"
        ).format(
            nomeArquivo,
            nomeAbaEncontrada,
            totalLinhas,
            linhasVazias,
            ignoradasPorIdf,
            adicionadas,
            duplicadas,
            erros,
            totalGrid,
            detalhes
        )

        Formulario.ExibeMensagem(
            resumo
        )


    else:

        Formulario.ExibeMensagem(
            "Não há arquivo anexado para importação."
        )

        Controle.Valor = False
```
  - GRID_IDF "Inserção de dados" [DataGrid RecordList → Z_00143_GRID_IDF.GRID_IDF] obrigatório — QtdColunasFormulario=3
    - coluna FORNECEDOR obrigatório
    - coluna DGCO obrigatório
    - coluna STATUS obrigatório
    - coluna IDF obrigatório
    - coluna ULTIMO_PERIODO obrigatório
    - coluna RISCO_APURADO obrigatório
    - coluna QUALIDADE_IDF obrigatório

### [349142] EventoFinal ""
**ScriptFim**
```python
OrdemServico.FinalizadorId = Convert.ToInt32(OrdemServico.ResponsavelId)
```

### [349143] SubProcesso "Abertura da associada"
Responsável: Cliente (papel 18)
Config: AssociacaoId=1662
MotivoInterrupcaoSLA: Aguardando Fim Subprocesso associado
**ScriptInicio**
```python
import clr
import System

clr.AddReference("Supravizio.Custom")

from System import Convert, DBNull


# ============================================================
# FUNCOES AUXILIARES
# ============================================================

def Texto(valor):
    try:
        if valor is None:
            return ""

        if valor == DBNull.Value:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        try:
            texto = valor.ToString()

            if texto is None:
                return ""

            return texto.Trim()

        except:
            return ""


def Inteiro(valor):
    try:
        texto = Texto(valor)

        if texto == "":
            return 0

        texto = texto.Replace(",", ".")

        return Convert.ToInt32(
            Convert.ToDouble(texto)
        )

    except:
        return 0


def ValorLinha(linha, campo):
    try:
        valor = linha[campo]

        if valor is None:
            return ""

        if valor == DBNull.Value:
            return ""

        return Texto(valor)

    except:
        return ""


def RegistrarLog(texto):
    try:
        Formulario.ExibeMensagem(
            texto
        )
    except:
        pass

    try:
        OrdemServico.AdicionaComentario(
            texto,
            True
        )
    except:
        pass


def LimparGridSubprocesso(sub, nomeGrid):
    try:
        gridSub = sub.GetCustom(
            nomeGrid
        )

        try:
            gridSub.Rows.Clear()
            return True

        except:
            pass

        try:
            while gridSub.Rows.Count > 0:
                gridSub.Rows.RemoveAt(0)

            return True

        except:
            pass

    except:
        pass

    return False


def MontarAssuntoSubprocesso(dgco, fornecedor):
    dgcoTexto = Texto(
        dgco
    )

    fornecedorTexto = Texto(
        fornecedor
    )

    if dgcoTexto != "" and fornecedorTexto != "":
        return (
            "IDF - {0} - {1}"
        ).format(
            dgcoTexto,
            fornecedorTexto
        )

    if fornecedorTexto != "":
        return (
            "IDF - {0}"
        ).format(
            fornecedorTexto
        )

    if dgcoTexto != "":
        return (
            "IDF - {0}"
        ).format(
            dgcoTexto
        )

    return "IDF"


def DefinirAssunto(sub, assunto):
    try:
        sub.Assunto = assunto
        return True

    except:
        return False


def DefinirCampoSubprocesso(sub, campo, valor):
    # Primeira tentativa.
    try:
        sub.SetCustom(
            campo,
            valor
        )

        return True

    except:
        pass

    # Segunda tentativa.
    try:
        sub[campo] = valor
        return True

    except:
        pass

    # Terceira tentativa.
    try:
        custom = sub.GetCustom(
            campo
        )

        custom.Valor = valor

        return True

    except:
        pass

    return False


def ObterPrimeiraLinhaSubprocesso(sub):
    resultado = {
        "DGCO": "",
        "FORNECEDOR": "",
        "STATUS": "",
        "IDF": "",
        "ULTIMO_PERIODO": "",
        "RISCO_APURADO": "",
        "QUALIDADE_IDF": ""
    }

    try:
        gridSub = sub.GetCustom(
            "GRID_IDF"
        )

        for linhaSub in gridSub.Rows:

            resultado["DGCO"] = ValorLinha(
                linhaSub,
                "DGCO"
            )

            resultado["FORNECEDOR"] = ValorLinha(
                linhaSub,
                "FORNECEDOR"
            )

            resultado["STATUS"] = ValorLinha(
                linhaSub,
                "STATUS"
            )

            resultado["IDF"] = ValorLinha(
                linhaSub,
                "IDF"
            )

            resultado["ULTIMO_PERIODO"] = ValorLinha(
                linhaSub,
                "ULTIMO_PERIODO"
            )

            resultado["RISCO_APURADO"] = ValorLinha(
                linhaSub,
                "RISCO_APURADO"
            )

            resultado["QUALIDADE_IDF"] = ValorLinha(
                linhaSub,
                "QUALIDADE_IDF"
            )

            break

    except:
        pass

    return resultado


# ============================================================
# COPIA TODAS AS LINHAS ANTES DE CRIAR O PRIMEIRO SUBPROCESSO
# ============================================================

linhas = []
log = ""

try:
    gridPai = OrdemServico.GetCustom(
        "GRID_IDF"
    )

    indice = 0

    for linha in gridPai.Rows:

        indice += 1

        dgco = ValorLinha(
            linha,
            "DGCO"
        )

        fornecedor = ValorLinha(
            linha,
            "FORNECEDOR"
        )

        status = ValorLinha(
            linha,
            "STATUS"
        )

        idfTexto = ValorLinha(
            linha,
            "IDF"
        )

        ultimoPeriodo = ValorLinha(
            linha,
            "ULTIMO_PERIODO"
        )

        riscoApurado = ValorLinha(
            linha,
            "RISCO_APURADO"
        )

        qualidadeIdf = ValorLinha(
            linha,
            "QUALIDADE_IDF"
        )


        if (
            dgco == "" and
            fornecedor == "" and
            status == "" and
            idfTexto == "" and
            ultimoPeriodo == "" and
            riscoApurado == "" and
            qualidadeIdf == ""
        ):
            continue


        linhas.append({
            "LINHA": indice,
            "DGCO": dgco,
            "FORNECEDOR": fornecedor,
            "STATUS": status,
            "IDF": Inteiro(idfTexto),
            "ULTIMO_PERIODO": ultimoPeriodo,
            "RISCO_APURADO": riscoApurado,
            "QUALIDADE_IDF": qualidadeIdf
        })


except Exception as ex:

    log += (
        "\nErro ao copiar GRID_IDF para a lista: {0}"
    ).format(
        Texto(ex)
    )


quantidadeOriginal = len(
    linhas
)


# ============================================================
# CONTADORES
# ============================================================

criados = 0
avancados = 0
ignorados = 0
erros = 0

assuntosConfirmados = 0
errosAssunto = 0

gridsConferidas = 0
divergenciasGrid = 0

camposIndividuaisGravados = 0
errosCamposIndividuais = 0


# ============================================================
# CRIA UMA ASSOCIADA PARA CADA LINHA
# ============================================================

if quantidadeOriginal == 0:

    log += (
        "\nA GRID_IDF nao possui linhas validas "
        "para gerar subprocessos."
    )

else:

    for dadosLinha in linhas:

        numeroLinha = dadosLinha["LINHA"]
        dgco = dadosLinha["DGCO"]
        fornecedor = dadosLinha["FORNECEDOR"]
        status = dadosLinha["STATUS"]
        idf = dadosLinha["IDF"]
        ultimoPeriodo = dadosLinha["ULTIMO_PERIODO"]
        riscoApurado = dadosLinha["RISCO_APURADO"]
        qualidadeIdf = dadosLinha["QUALIDADE_IDF"]

        try:
            # ====================================================
            # VALIDACOES
            # ====================================================

            if dgco == "":

                ignorados += 1

                log += (
                    "\nLinha {0} ignorada: "
                    "DGCO nao informado."
                ).format(
                    numeroLinha
                )

                continue


            if fornecedor == "":

                ignorados += 1

                log += (
                    "\nLinha {0} ignorada: "
                    "FORNECEDOR nao informado. DGCO={1}"
                ).format(
                    numeroLinha,
                    dgco
                )

                continue


            # ====================================================
            # MONTA O ASSUNTO COM OS DADOS DA LINHA ATUAL
            # ====================================================

            assuntoSubprocesso = MontarAssuntoSubprocesso(
                dgco,
                fornecedor
            )


            # ====================================================
            # INICIA O SUBPROCESSO
            # ====================================================

            sub = OrdemServico.IniciaSubProcesso(
                OrdemServico.Atividade
            )


            # ====================================================
            # DEFINE O ASSUNTO ANTES DO PRIMEIRO SALVAMENTO
            # ====================================================

            if not DefinirAssunto(
                sub,
                assuntoSubprocesso
            ):

                errosAssunto += 1

                log += (
                    "\nLinha {0}: nao foi possivel definir "
                    "o assunto antes do primeiro salvamento. "
                    "Assunto pretendido: '{1}'."
                ).format(
                    numeroLinha,
                    assuntoSubprocesso
                )


            # ====================================================
            # LIMPA A GRID HERDADA DO SUBPROCESSO
            # ====================================================

            limpou = LimparGridSubprocesso(
                sub,
                "GRID_IDF"
            )

            if not limpou:

                log += (
                    "\nLinha {0}: aviso - nao foi possivel "
                    "limpar GRID_IDF no subprocesso."
                ).format(
                    numeroLinha
                )


            # ====================================================
            # ADICIONA SOMENTE A LINHA ATUAL
            # ====================================================

            sub.AdicionaLinhaRegistro(
                "GRID_IDF",
                [
                    "DGCO",
                    "FORNECEDOR",
                    "STATUS",
                    "IDF",
                    "ULTIMO_PERIODO",
                    "RISCO_APURADO",
                    "QUALIDADE_IDF"
                ],
                [
                    dgco,
                    fornecedor,
                    status,
                    idf,
                    ultimoPeriodo,
                    riscoApurado,
                    qualidadeIdf
                ]
            )


            # ====================================================
            # GRAVA CAMPOS INDIVIDUAIS
            # ====================================================

            gravouDgco = DefinirCampoSubprocesso(
                sub,
                "DGCO_BB",
                dgco
            )

            gravouFornecedor = DefinirCampoSubprocesso(
                sub,
                "FORNECEDOR1",
                fornecedor
            )

            gravouPeriodo = DefinirCampoSubprocesso(
                sub,
                "PERIODO01",
                ultimoPeriodo
            )


            if gravouDgco:
                camposIndividuaisGravados += 1
            else:
                errosCamposIndividuais += 1

                log += (
                    "\nLinha {0}: aviso - nao foi possivel "
                    "gravar DGCO_BB no subprocesso."
                ).format(
                    numeroLinha
                )


            if gravouFornecedor:
                camposIndividuaisGravados += 1
            else:
                errosCamposIndividuais += 1

                log += (
                    "\nLinha {0}: aviso - nao foi possivel "
                    "gravar FORNECEDOR1 no subprocesso."
                ).format(
                    numeroLinha
                )


            if gravouPeriodo:
                camposIndividuaisGravados += 1
            else:
                errosCamposIndividuais += 1

                log += (
                    "\nLinha {0}: aviso - nao foi possivel "
                    "gravar PERIODO01 no subprocesso."
                ).format(
                    numeroLinha
                )


            # ====================================================
            # PRIMEIRO SALVAMENTO
            # ====================================================

            sub.Salva()


            # ====================================================
            # REAPLICA E SALVA O ASSUNTO
            # ====================================================

            if DefinirAssunto(
                sub,
                assuntoSubprocesso
            ):

                try:
                    sub.Salva()

                    assuntosConfirmados += 1

                except Exception as exSalvaAssunto:

                    errosAssunto += 1

                    log += (
                        "\nLinha {0}: assunto reaplicado, "
                        "mas nao foi possivel salvar novamente. "
                        "Assunto='{1}'. Erro: {2}"
                    ).format(
                        numeroLinha,
                        assuntoSubprocesso,
                        Texto(exSalvaAssunto)
                    )

            else:

                errosAssunto += 1

                log += (
                    "\nLinha {0}: nao foi possivel reaplicar "
                    "o assunto '{1}' depois do primeiro salvamento."
                ).format(
                    numeroLinha,
                    assuntoSubprocesso
                )


            # ====================================================
            # CONFERE A GRID DO FILHO ANTES DE AVANCAR
            # ====================================================

            dadosConferidos = ObterPrimeiraLinhaSubprocesso(
                sub
            )

            dgcoConferido = Texto(
                dadosConferidos["DGCO"]
            )

            fornecedorConferido = Texto(
                dadosConferidos["FORNECEDOR"]
            )


            if (
                dgcoConferido == dgco and
                fornecedorConferido == fornecedor
            ):

                gridsConferidas += 1

            else:

                divergenciasGrid += 1

                log += (
                    "\nDIVERGENCIA na linha {0} antes do avanco. "
                    "DGCO esperado='{1}'; "
                    "DGCO encontrado='{2}'; "
                    "FORNECEDOR esperado='{3}'; "
                    "FORNECEDOR encontrado='{4}'; "
                    "ASSUNTO='{5}'."
                ).format(
                    numeroLinha,
                    dgco,
                    dgcoConferido,
                    fornecedor,
                    fornecedorConferido,
                    assuntoSubprocesso
                )


                # Tenta corrigir a grid do filho antes de avançar.
                corrigiuGrid = LimparGridSubprocesso(
                    sub,
                    "GRID_IDF"
                )

                if corrigiuGrid:

                    sub.AdicionaLinhaRegistro(
                        "GRID_IDF",
                        [
                            "DGCO",
                            "FORNECEDOR",
                            "STATUS",
                            "IDF",
                            "ULTIMO_PERIODO",
                            "RISCO_APURADO",
                            "QUALIDADE_IDF"
                        ],
                        [
                            dgco,
                            fornecedor,
                            status,
                            idf,
                            ultimoPeriodo,
                            riscoApurado,
                            qualidadeIdf
                        ]
                    )

                    DefinirAssunto(
                        sub,
                        assuntoSubprocesso
                    )

                    sub.Salva()

                    dadosDepoisCorrecao = ObterPrimeiraLinhaSubprocesso(
                        sub
                    )

                    if (
                        Texto(dadosDepoisCorrecao["DGCO"]) == dgco and
                        Texto(dadosDepoisCorrecao["FORNECEDOR"]) == fornecedor
                    ):

                        log += (
                            "\nLinha {0}: GRID_IDF do subprocesso "
                            "corrigida antes do avanco."
                        ).format(
                            numeroLinha
                        )

                    else:

                        log += (
                            "\nLinha {0}: a GRID_IDF continuou "
                            "divergente mesmo depois da correcao."
                        ).format(
                            numeroLinha
                        )


            # ====================================================
            # PROCESSO CRIADO
            # ====================================================

            criados += 1

            if criados <= 20:

                log += (
                    "\nLinha {0}: subprocesso salvo. "
                    "DGCO={1}; FORNECEDOR={2}; ASSUNTO={3}."
                ).format(
                    numeroLinha,
                    dgco,
                    fornecedor,
                    assuntoSubprocesso
                )


            # ====================================================
            # AVANCA O SUBPROCESSO
            # ====================================================

            try:
                sub.AvancaAtividade()
                avancados += 1

            except Exception as exAvanca:

                log += (
                    "\nLinha {0}: subprocesso criado, "
                    "mas nao avancou: {1}"
                ).format(
                    numeroLinha,
                    Texto(exAvanca)
                )


        except Exception as ex:

            erros += 1

            if erros <= 30:

                log += (
                    "\nERRO na linha {0}, DGCO={1}: {2}"
                ).format(
                    numeroLinha,
                    dgco,
                    Texto(ex)
                )


# ============================================================
# ATENCAO
#
# NAO RESTAURA A GRID_IDF PRINCIPAL AQUI.
#
# A RESTAURACAO ANTERIOR PODIA INTERFERIR NAS GRIDS DOS
# SUBPROCESSOS JA SALVOS, POIS PAI E FILHOS USAM O MESMO
# NOME TECNICO GRID_IDF.
# ============================================================


# ============================================================
# COMPLEMENTO DO LOG
# ============================================================

if criados > 20:

    log += (
        "\nExistem mais {0} subprocesso(s) criado(s) "
        "nao detalhados no resumo."
    ).format(
        criados - 20
    )


if erros > 30:

    log += (
        "\nExistem mais {0} erro(s) de criacao "
        "nao detalhados no resumo."
    ).format(
        erros - 30
    )


# ============================================================
# RESUMO
# ============================================================

resumo = (
    "Geracao de subprocessos IDF concluida!\n\n"
    "Linhas encontradas inicialmente: {0}\n"
    "Subprocessos criados: {1}\n"
    "Subprocessos avancados: {2}\n"
    "Assuntos personalizados confirmados: {3}\n"
    "Erros ao definir ou salvar assunto: {4}\n"
    "Grids conferidas antes do avanco: {5}\n"
    "Divergencias encontradas nas grids: {6}\n"
    "Campos individuais gravados: {7}\n"
    "Falhas nos campos individuais: {8}\n"
    "Linhas ignoradas: {9}\n"
    "Erros na criacao: {10}\n\n"
    "Detalhes:{11}"
).format(
    quantidadeOriginal,
    criados,
    avancados,
    assuntosConfirmados,
    errosAssunto,
    gridsConferidas,
    divergenciasGrid,
    camposIndividuaisGravados,
    errosCamposIndividuais,
    ignorados,
    erros,
    log
)

RegistrarLog(
    resumo
)

# Se o fluxo principal precisar avançar:
# AvancaProximaAtividade = True
```
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
  - PropertyId=1295; Property=Servico
  - CustomPropertyId=5474; CustomProperty=GRID_IDF
- Associação: Ativo=true; FraseAssociacao=IDF Lote -> IDF Individual; FraseInversaAssociacao=IDF Individual -> IDF Lote; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=IDFLOTE; SeparadorSequencial=. | fonte: [LOTE] Pré-Notificação do Índice de Desempenho de Fornecedores (IDF) - (exclusivo Cesec) → alvo: Pré-Notificação do Índice de Desempenho de Fornecedores (IDF) 

### [349144] EventoIntermediarioMensagem "Finalização"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado Finalizado
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
Atenciosamente,
Central de Serviços

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### GRID_IDF — GRID_IDF
DataGrid RecordList → Z_00143_GRID_IDF.GRID_IDF
Colunas do registro:
- FORNECEDOR "FORNECEDOR" [TextBox String]
- DGCO "DGCO" [TextBox String]
- STATUS "STATUS" [TextBox String]
- IDF "IDF" [TextBox Integer]
- ULTIMO_PERIODO "Último Período Avaliado" [TextBox String]
- RISCO_APURADO "Risco Apurado" [TextBox String]
- QUALIDADE_IDF "Qualidade do IDF" [TextBox String]

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
