# Fluxo: Pré-Notificação do Índice de Desempenho de Fornecedores (IDF)  (IDFINDIVIDUAL) — versão 45
Caminho: Fluxos > Administração - Contratos Versão 45 Pré-Notificação do Índice de Desempenho de Fornecedores (IDF) 
XML: `XMLs para teste/Administração_-_Contratos_Versão_45_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_.xml` | Supravizio 19.1.1 | SubProcessoId 21989 | DesenhoProcessoId 3021 | ProcessoId 127
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Pré-Notificação do Índice de Desempenho de Fornecedores (IDF); CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Pré-Notificação do Índice de Desempenho de Fornecedores (IDF)  (IDFSERVICO)

## Grafo do fluxo
- [349137] Tarefa "Preenchimeneto dos campos" {Fiscal Administrativo Papel} → [G78848] Média menor que 2?
- [349138] LinkInicial "" {Cliente} → [349132] Atribuição de responsáveis e leitura da API
- [349132] Tarefa "Atribuição de responsáveis e leitura da API" {Fiscal Administrativo Papel} → [G78849] Há fiscal administrativo?
- [349134] Tarefa "Atribuição manual" {Fila CSC - Contratos} → [349137] Preenchimeneto dos campos
- [349135] EventoIntermediarioMensagem "E-mail avaliação Fiscal" → [349136] 
- [349136] EventoFinal "" → (fim)
- [349140] Tarefa "Aprovação" {Gestor do Responsável} → [G78847] Aprovado?
- [G78847] Gateway "Aprovado?" → «Reprovado» [349137] Preenchimeneto dos campos | «Aprovado» [349135] E-mail avaliação Fiscal
- [G78848] Gateway "Média menor que 2?" → «Sim» [349140] Aprovação | «Não» [349136] 
- [G78849] Gateway "Há fiscal administrativo?" → «Sim» [349137] Preenchimeneto dos campos | «Não» [349134] Atribuição manual

## Gateways
### [G78847] Aprovado? (DataBasedExclusiveDecision)
Codigo=APROV
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV")
```
- alternativa → [349137] Preenchimeneto dos campos: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [349135] E-mail avaliação Fiscal: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G78848] Média menor que 2? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
Convert.ToDecimal(OrdemServico.GetCustom("TEXT")) < 2.0
```
- alternativa → [349140] Aprovação: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [349136] : OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G78849] Há fiscal administrativo? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom('FISCAL_ADM_SGPS') == ""
```
- alternativa → [349137] Preenchimeneto dos campos: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [349134] Atribuição manual: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [349137] Tarefa "Preenchimeneto dos campos"
Responsável: Fiscal Administrativo Papel (papel 980)
**ScriptFormCarregado**
```python
#Formulario['COMBOBOX_V'].Itens = '1- Não atendimento às exigências contratuais;2- Atendimento parcial às exigências contratuais;3- Pleno atendimento às exigências contratuais'
#
#Formulario['COMBOBOX_XX'].Itens = '1- Não atendimento às exigências contratuais;2- Atendimento parcial às exigências contratuais;3- Pleno atendimento às exigências contratuais'

Formulario['TEXT'].Habilitado = False

campos = ['CSC_NUMERO5', 'CSC_NUMERO6', 'DESCRICAO_UM', 'DESCRICAO_DOIS', 'PENF_EMAIL']

for i in campos:
    Formulario[i].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - GRID_IDF "Dados capturados" [DataGrid RecordList → Z_00143_GRID_IDF.GRID_IDF] — LarguraJanelaPopup=500
    - coluna DGCO obrigatório
    - coluna STATUS obrigatório
    - coluna IDF obrigatório
    - coluna ULTIMO_PERIODO obrigatório
    - coluna RISCO_APURADO
    - coluna QUALIDADE_IDF
    - coluna FORNECEDOR obrigatório
**GRID_IDF.FORNECEDOR.ScriptModificado**
```python
OrdemServico['FORNECEDOR'] = FormularioRegistro['FORNECEDOR'].Valor
```
- Operação PR0001 Preencher Campos
  - TEXT "Média das Notas" [TextBox String(1000) → CPE_CSC.TEXT]
  - DESCRICAO_UM "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_UM] obrigatório
  - CSC_NUMERO6 "Nota de Avaliação do Fiscal Administrativo" [TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO6] obrigatório
**CSC_NUMERO6.ScriptModificado**
```python
from Venki.Services.Dictionary.Custom import Culture
import clr
import System

from System import Convert, DBNull
from System.Globalization import CultureInfo


def ConverterNumero(valor):
    try:
        if valor is None or valor == DBNull.Value:
            return None

        texto = Convert.ToString(valor)

        if texto is None:
            return None

        texto = texto.Trim().Replace(" ", "")

        if texto == "":
            return None

        # Aceita:
        # 10
        # 10,5
        # 10.5
        texto = texto.Replace(",", ".")

        return Convert.ToDouble(
            texto,
            CultureInfo.InvariantCulture
        )

    except:
        return None


valor_servico = ConverterNumero(
    Formulario["CSC_NUMERO5"].Valor
)

valor_administrativo = ConverterNumero(
    Formulario["CSC_NUMERO6"].Valor
)


# Só calcula quando os dois valores forem válidos.
if (
    valor_servico is not None and
    valor_administrativo is not None
):
    media = (
        valor_servico +
        valor_administrativo
    ) / 2.0

    # Exibe o resultado com vírgula e duas casas decimais.
    Formulario["TEXT"].Valor = media.ToString(
        "0.00",
        CultureInfo.GetCultureInfo("pt-BR")
    )

else:
    # Se um dos campos estiver vazio ou inválido,
    # limpa o resultado sem apresentar erro.
    try:
        Formulario["TEXT"].Valor = ""
    except:
        pass
```
  - CSC_NUMERO5 "Nota de Avaliação do Fiscal de Serviço" [TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO5] obrigatório
**CSC_NUMERO5.ScriptModificado**
```python
from Venki.Services.Dictionary.Custom import Culture
import clr
import System

from System import Convert, DBNull
from System.Globalization import CultureInfo


def ConverterNumero(valor):
    try:
        if valor is None or valor == DBNull.Value:
            return None

        texto = Convert.ToString(valor)

        if texto is None:
            return None

        texto = texto.Trim().Replace(" ", "")

        if texto == "":
            return None

        # Aceita:
        # 10
        # 10,5
        # 10.5
        texto = texto.Replace(",", ".")

        return Convert.ToDouble(
            texto,
            CultureInfo.InvariantCulture
        )

    except:
        return None


valor_servico = ConverterNumero(
    Formulario["CSC_NUMERO5"].Valor
)

valor_administrativo = ConverterNumero(
    Formulario["CSC_NUMERO6"].Valor
)


# Só calcula quando os dois valores forem válidos.
if (
    valor_servico is not None and
    valor_administrativo is not None
):
    media = (
        valor_servico +
        valor_administrativo
    ) / 2.0

    # Exibe o resultado com vírgula e duas casas decimais.
    Formulario["TEXT"].Valor = media.ToString(
        "0.00",
        CultureInfo.GetCultureInfo("pt-BR")
    )

else:
    # Se um dos campos estiver vazio ou inválido,
    # limpa o resultado sem apresentar erro.
    try:
        Formulario["TEXT"].Valor = ""
    except:
        pass
```
  - DESCRICAO_DOIS "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_DOIS] obrigatório
  - PENF_EMAIL "E-mails do Fornecedor que serão notificados sobre o IDF abaixo do esperado (separados por ponto e vírgula):" [TextBox String(2000) → CPE_PENF.PENF_EMAIL]

### [349138] LinkInicial ""
Responsável: Cliente (papel 18)
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=1662; Nome=RONY BALDOINO DA SILVA; FraseAssociacao=IDF Lote -> IDF Individual

### [349132] Tarefa "Atribuição de responsáveis e leitura da API"
Responsável: Fiscal Administrativo Papel (papel 980)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Pesquisa
import clr

clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

import System

from System import TimeSpan, Convert
from Newtonsoft.Json.Linq import JArray
from Newtonsoft.Json import JsonConvert
from System.Net.Http import HttpClient
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

dgco = ""
nomeFornecedor = ""

token = "***MASCARADO***"
url = ""
resultado = ""

nomeFiscal = ""
matriculaFiscal = ""
idFiscal = ""

nomeFiscalAdministrativo = ""
matriculaFiscalAdministrativo = ""
idFiscalAdministrativo = ""

nomeGestor = ""
matriculaGestor = ""
idGestor = ""

client = None

grid = OrdemServico.GetCustom("GRID_IDF")

if grid != None:
    if grid.Rows.Count > 0:
        for linhaGrid in grid.Rows:
            if linhaGrid["DGCO"] != None:
                if linhaGrid["DGCO"].ToString().Trim() != "":
                    dgco = linhaGrid["DGCO"].ToString().Trim()
                    #Formulario["DGCO_BB"].Valor = dgco
                    OrdemServico['DGCO_BB'] = dgco

            if linhaGrid["FORNECEDOR"] != None:
                if linhaGrid["FORNECEDOR"].ToString().Trim() != "":
                    nomeFornecedor = linhaGrid["FORNECEDOR"].ToString().Trim()
                    #Formulario["FORNECEDOR1"].Valor = nomeFornecedor
                    #Formulario['FORNECEDOR1'].Habilitado = False
                    OrdemServico['FORNECEDOR1'] = nomeFornecedor
                    OrdemServico.ModificaCampoFormularioHabilitado('FORNECEDOR1', False)

            break

#Formulario["FISCAL_SERVI_SGPS"].Valor = None
#Formulario["FISCAL_ADM_SGPS"].Valor = None
#Formulario["FAVORECIDO_TODOS"].Valor = None
OrdemServico['FISCAL_SERVI_SGPS'] = None
OrdemServico['FISCAL_ADM_SGPS'] = None
OrdemServico['FAVORECIDO_TODOS'] = None

if dgco == "":
    #Formulario.ExibeMensagem("Não foi encontrado um DGCO na grade GRID_IDF.")

    OrdemServico.AdicionaComentario(
        "A API não foi consultada porque nenhum DGCO foi encontrado na grade GRID_IDF.",
        False
    )

else:
    sqlDominio = "select name from sv_domain where enabled = 'Sim'"
    dom = DB.ExecuteScalar(sqlDominio)

    if dom != None:
        dom = dom.ToString().Trim()
    else:
        dom = ""

    if dom == "HOMOLOGAÇÃO":
        url = "https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=" + dgco
    elif dom == "PRODUÇÃO":
        url = "https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=" + dgco
    elif dom == "DESENVOLVIMENTO":
        url = "https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=" + dgco
    else:
        #Formulario.ExibeMensagem("Não foi possível identificar o domínio ativo.")

        OrdemServico.AdicionaComentario(
            "Não foi possível montar a URL da API. Domínio encontrado: " + dom + ".",
            False
        )

    if url != "":
        try:
            client = HttpClient()
            client.Timeout = TimeSpan.FromSeconds(60)

            client.DefaultRequestHeaders.Accept.Clear()
            client.DefaultRequestHeaders.Accept.Add(
                MediaTypeWithQualityHeaderValue("application/json")
            )

            client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue(
                "Bearer",
                token
            )

            response = client.GetAsync(url).Result
            resultado = response.Content.ReadAsStringAsync().Result

            if response.IsSuccessStatusCode:
                try:
                    if resultado != None:
                        resultado = resultado.Trim()

                    if resultado.StartsWith('"') and resultado.EndsWith('"'):
                        resultado = JsonConvert.DeserializeObject(resultado)

                    jsonArray = JArray.Parse(resultado)

                    if jsonArray.Count > 0:
                        for item in jsonArray:

                            # Fiscal de serviço
                            if item["fiscal_servico_titular"] != None:
                                if item["fiscal_servico_titular"].ToString().Trim() != "":
                                    nomeFiscal = item["fiscal_servico_titular"].ToString().Trim()

                            if item["matricula_fiscal_servico_titular"] != None:
                                if item["matricula_fiscal_servico_titular"].ToString().Trim() != "":
                                    matriculaFiscal = item["matricula_fiscal_servico_titular"].ToString().Trim()

                            # Nomes alternativos do fiscal de serviço
                            if nomeFiscal == "":
                                if item["fiscal_titular"] != None:
                                    if item["fiscal_titular"].ToString().Trim() != "":
                                        nomeFiscal = item["fiscal_titular"].ToString().Trim()

                            if matriculaFiscal == "":
                                if item["matricula_fiscal_titular"] != None:
                                    if item["matricula_fiscal_titular"].ToString().Trim() != "":
                                        matriculaFiscal = item["matricula_fiscal_titular"].ToString().Trim()

                            if nomeFiscal == "":
                                if item["fiscalizacao_servico_titular"] != None:
                                    if item["fiscalizacao_servico_titular"].ToString().Trim() != "":
                                        nomeFiscal = item["fiscalizacao_servico_titular"].ToString().Trim()

                            if matriculaFiscal == "":
                                if item["matricula_fiscalizacao_servico_titular"] != None:
                                    if item["matricula_fiscalizacao_servico_titular"].ToString().Trim() != "":
                                        matriculaFiscal = item["matricula_fiscalizacao_servico_titular"].ToString().Trim()

                            # Fiscal administrativo titular
                            if item["fiscal_administrativo_titular"] != None:
                                if item["fiscal_administrativo_titular"].ToString().Trim() != "":
                                    nomeFiscalAdministrativo = item["fiscal_administrativo_titular"].ToString().Trim()

                            if item["matricula_fiscal_administrativo_titular"] != None:
                                if item["matricula_fiscal_administrativo_titular"].ToString().Trim() != "":
                                    matriculaFiscalAdministrativo = item["matricula_fiscal_administrativo_titular"].ToString().Trim()

                            # Gestor titular
                            if item["gestor_titular"] != None:
                                if item["gestor_titular"].ToString().Trim() != "":
                                    nomeGestor = item["gestor_titular"].ToString().Trim()

                            if item["matricula_gestor_titular"] != None:
                                if item["matricula_gestor_titular"].ToString().Trim() != "":
                                    matriculaGestor = item["matricula_gestor_titular"].ToString().Trim()

                            # Fornecedor: usa a API caso a grade não tenha retornado
                            if nomeFornecedor == "":
                                if item["fornecedor"] != None:
                                    if item["fornecedor"].ToString().Trim() != "":
                                        nomeFornecedor = item["fornecedor"].ToString().Trim()
                                        Formulario["FORNECEDOR"].Valor = nomeFornecedor

                            break

                        # Pesquisa ID_PESSOA do fiscal de serviço
                        if matriculaFiscal != "":
                            matriculaFiscalConsulta = matriculaFiscal.Replace("'", "''")

                            sqlFiscal = "SELECT TO_CHAR(id_pessoa) FROM cp_pessoa WHERE TO_CHAR(matricula) = '" + matriculaFiscalConsulta + "' AND ROWNUM = 1"

                            resultadoFiscal = DB.ExecuteScalar(sqlFiscal)

                            if resultadoFiscal != None:
                                idFiscal = resultadoFiscal.ToString().Trim()

                        # Pesquisa ID_PESSOA do fiscal administrativo
                        if matriculaFiscalAdministrativo != "":
                            matriculaFiscalAdministrativoConsulta = matriculaFiscalAdministrativo.Replace("'", "''")

                            sqlFiscalAdministrativo = "SELECT TO_CHAR(id_pessoa) FROM cp_pessoa WHERE TO_CHAR(matricula) = '" + matriculaFiscalAdministrativoConsulta + "' AND ROWNUM = 1"

                            resultadoFiscalAdministrativo = DB.ExecuteScalar(
                                sqlFiscalAdministrativo
                            )

                            if resultadoFiscalAdministrativo != None:
                                idFiscalAdministrativo = resultadoFiscalAdministrativo.ToString().Trim()

                        # Pesquisa ID_PESSOA do gestor
                        if matriculaGestor != "":
                            matriculaGestorConsulta = matriculaGestor.Replace("'", "''")

                            sqlGestor = "SELECT TO_CHAR(id_pessoa) FROM cp_pessoa WHERE TO_CHAR(matricula) = '" + matriculaGestorConsulta + "' AND ROWNUM = 1"

                            resultadoGestor = DB.ExecuteScalar(sqlGestor)

                            if resultadoGestor != None:
                                idGestor = resultadoGestor.ToString().Trim()

                        # Preenche o fiscal de serviço
                        if idFiscal != "":
                            #Formulario["FISCAL_SERVI_SGPS"].Valor = Convert.ToInt32(idFiscal)
                            OrdemServico['FISCAL_SERVI_SGPS'] = Convert.ToInt32(idFiscal)
                        else:
                            #Formulario["FISCAL_SERVI_SGPS"].Valor = None
                            OrdemServico['FISCAL_SERVI_SGPS'] = None

                            if matriculaFiscal == "":
                                OrdemServico.AdicionaComentario(
                                    "A API não retornou fiscal de serviço titular para o DGCO " + dgco + ".",
                                    False
                                )
                            else:
                                OrdemServico.AdicionaComentario(
                                    "A API retornou o fiscal de serviço " + nomeFiscal + ", matrícula " + matriculaFiscal + ", mas não foi encontrado ID_PESSOA em CP_PESSOA.",
                                    False
                                )

                        # Preenche o fiscal administrativo
                        if idFiscalAdministrativo != "":
                            #Formulario["FISCAL_ADM_SGPS"].Valor = Convert.ToInt32(
                                #idFiscalAdministrativo
                            #)
                            OrdemServico['FISCAL_ADM_SGPS'] = Convert.ToInt32(idFiscalAdministrativo)
                        else:
                            #Formulario["FISCAL_ADM_SGPS"].Valor = None
                            OrdemServico['FISCAL_ADM_SGPS'] = None

                            if matriculaFiscalAdministrativo == "":
                                OrdemServico.AdicionaComentario(
                                    "A API não retornou fiscal administrativo titular para o DGCO " + dgco + ".",
                                    False
                                )
                            else:
                                OrdemServico.AdicionaComentario(
                                    "A API retornou o fiscal administrativo " + nomeFiscalAdministrativo + ", matrícula " + matriculaFiscalAdministrativo + ", mas não foi encontrado ID_PESSOA em CP_PESSOA.",
                                    False
                                )

                        # Preenche o gestor
                        if idGestor != "":
                            #Formulario["FAVORECIDO_TODOS"].Valor = Convert.ToInt32(
                                #idGestor
                            #)
                            OrdemServico['FAVORECIDO_TODOS'] = Convert.ToInt32(idGestor)
                        else:
                            OrdemServico['FAVORECIDO_TODOS'] = None

                            if matriculaGestor == "":
                                OrdemServico.AdicionaComentario(
                                    "A API não retornou gestor titular para o DGCO " + dgco + ".",
                                    False
                                )
                            else:
                                OrdemServico.AdicionaComentario(
                                    "A API retornou o gestor " + nomeGestor + ", matrícula " + matriculaGestor + ", mas não foi encontrado ID_PESSOA em CP_PESSOA.",
                                    False
                                )

                        OrdemServico.AdicionaComentario(
                            "Consulta concluída para o DGCO " + dgco +
                            ". Fiscal de serviço: " + nomeFiscal +
                            ". Matrícula fiscal de serviço: " + matriculaFiscal +
                            ". ID fiscal de serviço: " + idFiscal +
                            ". Fiscal administrativo: " + nomeFiscalAdministrativo +
                            ". Matrícula fiscal administrativo: " + matriculaFiscalAdministrativo +
                            ". ID fiscal administrativo: " + idFiscalAdministrativo +
                            ". Gestor: " + nomeGestor +
                            ". Matrícula gestor: " + matriculaGestor +
                            ". ID gestor: " + idGestor + ".",
                            False
                        )

                    else:
                        OrdemServico.AdicionaComentario(
                            "A API retornou uma lista vazia para o DGCO " + dgco + ".",
                            False
                        )

                except System.Exception as erroJson:
                    OrdemServico.AdicionaComentario(
                        "Erro ao interpretar a resposta da API para o DGCO " + dgco +
                        ". Erro: " + erroJson.Message +
                        ". Resposta: " + resultado,
                        False
                    )

            else:
                OrdemServico.AdicionaComentario(
                    "Erro HTTP ao consultar a API. DGCO: " + dgco +
                    ". Status: " + response.StatusCode.ToString() +
                    ". Resposta: " + resultado,
                    False
                )

        except System.Exception as erroApi:
            OrdemServico.AdicionaComentario(
                "Erro ao consultar a API para o DGCO " + dgco +
                ": " + erroApi.Message,
                False
            )

        finally:
            if client != None:
                client.Dispose()

#Formulario["FISCAL_SERVI_SGPS"].Habilitado = False
#Formulario["FISCAL_ADM_SGPS"].Habilitado = False
#Formulario["FAVORECIDO_TODOS"].Habilitado = False
OrdemServico.ModificaCampoFormularioHabilitado('FISCAL_SERVI_SGPS', False)
OrdemServico.ModificaCampoFormularioHabilitado('FISCAL_ADM_SGPS', False)
OrdemServico.ModificaCampoFormularioHabilitado('FAVORECIDO_TODOS', False)

AvancaProximaAtividade = True
```
**ScriptFim**
```python
#OrdemServico.AdicionaComentario((OrdemServico.GetCustom('FISCAL_ADM_SGPS') == '').ToString(), False)
#OrdemServico.AdicionaComentario(OrdemServico.GetCustom('FISCAL_ADM_SGPS'), False)
```
- Operação PR0001 Preencher Campos
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
    - coluna CHAVE_PIX obrigatório
    - coluna BANCO obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA_CORR obrigatório
    - coluna TIPO_CHAVE obrigatório
  - FISCAL_SERVI_SGPS "Fiscal de Serviço" [DropDownList String → CPE_PESSOAS.FISCAL_SERVI_SGPS]
  - FAVORECIDO_TODOS "Gestor do Contrato" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - FISCAL_ADM_SGPS "Fiscal Administrativo" [DropDownList String → CPE_PESSOAS.FISCAL_ADM_SGPS]
  - FORNECEDOR1 "Fornecedor" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1]

### [349134] Tarefa "Atribuição manual"
Responsável: Fila CSC - Contratos (papel 688)
**ScriptFormCarregado**
```python
campos = ['DGCO_BB', 'FISCAL_SERVI_SGPS', 'FISCAL_ADM_SGPS', 'FORNECEDOR1', 'FAVORECIDO_TODOS']

for i in campos:
    Formulario[i].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
    - coluna BANCO obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA_CORR obrigatório
    - coluna TIPO_CHAVE obrigatório
    - coluna CHAVE_PIX obrigatório
  - FISCAL_SERVI_SGPS "Fiscal de Serviço" [DropDownList String → CPE_PESSOAS.FISCAL_SERVI_SGPS]
  - FAVORECIDO_TODOS "Gestor do Contrato" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - FISCAL_ADM_SGPS "Fiscal Administrativo" [DropDownList String → CPE_PESSOAS.FISCAL_ADM_SGPS] obrigatório
  - FORNECEDOR1 "Fornecedor" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1]
  - LABEL1 "Atenção, se a OS caiu nessa tarefa, significa que ou o Fiscal de Serviço ou Administrativo, não foi preenchido automáticamente pela API, favor atribuir manualmente e avançar." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]

### [349135] EventoIntermediarioMensagem "E-mail avaliação Fiscal"
Destinatário: Fiscal Administrativo Papel (papel 980)
Config: EmailRemetente=fiscalizacaoadministrativa@bbts.com.br; ListaDestinatarios=fiscalizacaoadministrativa@bbts.com.br;canaldofornecedor@bbts.com.br
ModeloComunicado: IDF - Notificação
Corpo do comunicado: Prezado Fornecedor OrdemServico.Customizado.FORNECEDOR1 
Contrato DGCO: OrdemServico.Customizado.DGCO_BB 
Último período apurado: OrdemServico.Customizado.PERIODO01 
Informamos que, na última Avaliação Trimestral de Fornecedores, o desempenho apresentado ficou abaixo do esperado, conforme evidenciado pelas notas atribuídas e pelas respectivas ocorrências registradas abaixo.
Esclarecemos que a avaliação realizada pelos fiscais do contrato possui caráter exclusivamente informativo, tendo por finalidade pré-notificar o fornecedor acerca dos pontos que necessitam de melhoria no cumprimento das obrigações contratuais.
Ressalta-se, ainda, que a referida avaliação possui caráter interno e não impli…
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
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
            return valor.ToString().Trim()
        except:
            return ""


def EscaparSql(valor):
    try:
        return Texto(valor).Replace("'", "''")
    except:
        return ""


def EmailValido(email):
    try:
        email = Texto(email)

        if email == "":
            return False

        if not email.Contains("@"):
            return False

        partes = email.Split("@")

        if len(partes) != 2:
            return False

        if Texto(partes[0]) == "":
            return False

        if Texto(partes[1]) == "":
            return False

        return True

    except:
        return False


def EhNumeroInteiro(valor):
    try:
        texto = Texto(valor)

        if texto == "":
            return False

        Convert.ToInt32(texto)

        return True

    except:
        return False


def RegistrarComentario(texto, interno):
    try:
        OrdemServico.AdicionaComentario(
            texto,
            interno
        )
    except:
        pass


# ============================================================
# OBTEM O VALOR DE UM CAMPO
# ============================================================

def ObterValorCampo(campo):

    # Primeira tentativa: mesma forma usada no script original.
    try:
        valor = OrdemServico[campo]
        texto = Texto(valor)

        if texto != "":
            return texto
    except:
        pass

    # Segunda tentativa: campo customizado.
    try:
        valor = OrdemServico.GetCustom(campo)
        texto = Texto(valor)

        if texto != "":
            return texto
    except:
        pass

    return ""


# ============================================================
# CONSULTAS ORACLE
# ============================================================

def BuscarEmailPorIdPessoa(idPessoa):
    try:
        idNumero = Convert.ToInt32(
            Texto(idPessoa)
        )

        sql = (
            "SELECT P.EMAIL "
            "FROM PESSOA P "
            "WHERE P.ID_PESSOA = {0} "
            "AND P.EMAIL IS NOT NULL "
            "AND TRIM(P.EMAIL) IS NOT NULL "
            "AND ROWNUM = 1"
        ).format(
            idNumero
        )

        return Texto(
            Utils.ExecuteScalar(sql)
        )

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao buscar e-mail pelo ID_PESSOA {0}: {1}"
            ).format(
                Texto(idPessoa),
                Texto(ex)
            ),
            True
        )

        return ""


def BuscarNomePorIdPessoa(idPessoa):
    try:
        idNumero = Convert.ToInt32(
            Texto(idPessoa)
        )

        sql = (
            "SELECT P.NOME "
            "FROM PESSOA P "
            "WHERE P.ID_PESSOA = {0} "
            "AND ROWNUM = 1"
        ).format(
            idNumero
        )

        return Texto(
            Utils.ExecuteScalar(sql)
        )

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao buscar nome pelo ID_PESSOA {0}: {1}"
            ).format(
                Texto(idPessoa),
                Texto(ex)
            ),
            True
        )

        return ""


def BuscarEmailPorMatricula(matricula):
    try:
        matriculaTexto = Texto(
            matricula
        )

        if matriculaTexto == "":
            return ""

        sql = (
            "SELECT P.EMAIL "
            "FROM PESSOA P "
            "INNER JOIN CP_PESSOA CP "
            "ON CP.ID_PESSOA = P.ID_PESSOA "
            "WHERE TRIM(CP.MATRICULA) = TRIM('{0}') "
            "AND P.EMAIL IS NOT NULL "
            "AND TRIM(P.EMAIL) IS NOT NULL "
            "AND ROWNUM = 1"
        ).format(
            EscaparSql(matriculaTexto)
        )

        return Texto(
            Utils.ExecuteScalar(sql)
        )

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao buscar e-mail pela matricula {0}: {1}"
            ).format(
                Texto(matricula),
                Texto(ex)
            ),
            True
        )

        return ""


def BuscarNomePorMatricula(matricula):
    try:
        matriculaTexto = Texto(
            matricula
        )

        if matriculaTexto == "":
            return ""

        sql = (
            "SELECT P.NOME "
            "FROM PESSOA P "
            "INNER JOIN CP_PESSOA CP "
            "ON CP.ID_PESSOA = P.ID_PESSOA "
            "WHERE TRIM(CP.MATRICULA) = TRIM('{0}') "
            "AND ROWNUM = 1"
        ).format(
            EscaparSql(matriculaTexto)
        )

        return Texto(
            Utils.ExecuteScalar(sql)
        )

    except:
        return ""


def BuscarEmailPorNome(nome):
    try:
        nomeTexto = Texto(nome)

        if nomeTexto == "":
            return ""

        sql = (
            "SELECT P.EMAIL "
            "FROM PESSOA P "
            "WHERE UPPER(TRIM(P.NOME)) = UPPER(TRIM('{0}')) "
            "AND P.EMAIL IS NOT NULL "
            "AND TRIM(P.EMAIL) IS NOT NULL "
            "AND ROWNUM = 1"
        ).format(
            EscaparSql(nomeTexto)
        )

        return Texto(
            Utils.ExecuteScalar(sql)
        )

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao buscar e-mail pelo nome {0}: {1}"
            ).format(
                Texto(nome),
                Texto(ex)
            ),
            True
        )

        return ""


# ============================================================
# CONTROLE DE DESTINATARIOS
# ============================================================

emailsAdicionados = {}
listaEmailsAdicionados = []


def AdicionarDestinatario(email):
    try:
        emailTexto = Texto(email).ToLower()

        if not EmailValido(emailTexto):
            return False

        chave = emailTexto.ToUpper()

        # Impede que o mesmo e-mail seja adicionado duas vezes.
        if chave in emailsAdicionados:
            return False

        Mensagem.Destinatarios.Add(
            emailTexto
        )

        emailsAdicionados[chave] = True

        listaEmailsAdicionados.append(
            emailTexto
        )

        return True

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao adicionar destinatario '{0}': {1}"
            ).format(
                Texto(email),
                Texto(ex)
            ),
            True
        )

        return False


# ============================================================
# EMAILS FIXOS
# ============================================================

def AdicionarEmailsFixos():
    try:
        emailsFixos = [
            "fiscalizacaoadministrativa@bbts.com.br",
            "canaldofornecedor@bbts.com.br"
        ]

        for emailFixo in emailsFixos:
            AdicionarDestinatario(
                emailFixo
            )

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao adicionar os e-mails fixos: {0}"
            ).format(
                Texto(ex)
            ),
            True
        )


# ============================================================
# EMAILS MANUAIS DO PENF_EMAIL
# ============================================================

def AdicionarEmailsManuais():
    try:
        textoEmails = ObterValorCampo(
            "PENF_EMAIL"
        )

        if textoEmails == "":
            return

        # Mantem o padrao original:
        # e-mails separados por ponto e virgula.
        textoEmails = textoEmails.Replace(
            "\r\n",
            ";"
        )

        textoEmails = textoEmails.Replace(
            "\n",
            ";"
        )

        listaEmails = textoEmails.Split(
            ";"
        )

        for email in listaEmails:
            emailTexto = Texto(email)

            if emailTexto == "":
                continue

            if not EmailValido(emailTexto):
                RegistrarComentario(
                    (
                        "E-mail invalido no campo PENF_EMAIL: {0}"
                    ).format(
                        emailTexto
                    ),
                    True
                )

                continue

            AdicionarDestinatario(
                emailTexto
            )

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao processar PENF_EMAIL: {0}"
            ).format(
                Texto(ex)
            ),
            True
        )


# ============================================================
# LOCALIZA EMAIL DE UMA PESSOA
# ============================================================

def BuscarEmailPessoa(valorPessoa):
    valorTexto = Texto(
        valorPessoa
    )

    if valorTexto == "":
        return "", "", ""

    # Se o controle ja retornar um e-mail.
    if EmailValido(valorTexto):
        return (
            valorTexto,
            "",
            "e-mail direto"
        )

    # Se for numerico, tenta primeiro como ID_PESSOA
    # e depois como matricula.
    if EhNumeroInteiro(valorTexto):
        email = BuscarEmailPorIdPessoa(
            valorTexto
        )

        nome = BuscarNomePorIdPessoa(
            valorTexto
        )

        if EmailValido(email):
            return (
                email,
                nome,
                "ID_PESSOA"
            )

        email = BuscarEmailPorMatricula(
            valorTexto
        )

        nomeMatricula = BuscarNomePorMatricula(
            valorTexto
        )

        if nome == "":
            nome = nomeMatricula

        if EmailValido(email):
            return (
                email,
                nome,
                "MATRICULA"
            )

        return (
            "",
            nome,
            "ID_PESSOA e MATRICULA"
        )

    # Se for texto, tenta como nome completo.
    email = BuscarEmailPorNome(
        valorTexto
    )

    if EmailValido(email):
        return (
            email,
            valorTexto,
            "NOME"
        )

    return (
        "",
        valorTexto,
        "NOME"
    )


# ============================================================
# PROCESSA CAMPO DE PESSOA
# ============================================================

def AdicionarEmailsPorCampo(campo):
    try:
        valorCampo = ObterValorCampo(
            campo
        )

        if valorCampo == "":
            return

        valoresPessoas = valorCampo.Split(
            ";"
        )

        for valorPessoa in valoresPessoas:
            valorPessoa = Texto(
                valorPessoa
            )

            if valorPessoa == "":
                continue

            email, nome, metodo = BuscarEmailPessoa(
                valorPessoa
            )

            if EmailValido(email):
                AdicionarDestinatario(
                    email
                )
            else:
                RegistrarComentario(
                    (
                        "Nao foi encontrado e-mail cadastrado. "
                        "Campo: {0}; "
                        "valor recebido: {1}; "
                        "nome localizado: {2}; "
                        "consultas realizadas por: {3}."
                    ).format(
                        campo,
                        valorPessoa,
                        nome,
                        metodo
                    ),
                    True
                )

    except Exception as ex:
        RegistrarComentario(
            (
                "Erro ao processar campo {0}: {1}"
            ).format(
                campo,
                Texto(ex)
            ),
            True
        )


# ============================================================
# EXECUCAO
# ============================================================

# Adiciona os dois e-mails fixos.
AdicionarEmailsFixos()

# Adiciona os e-mails informados manualmente no PENF_EMAIL.
AdicionarEmailsManuais()

# Adiciona os e-mails das pessoas selecionadas.
camposPessoas = [
    "FISCAL_ADM_SGPS",
    "FISCAL_SERVI_SGPS",
    "FAVORECIDO_TODOS"
]

for campoPessoa in camposPessoas:
    AdicionarEmailsPorCampo(
        campoPessoa
    )


# ============================================================
# REMETENTE
# ============================================================

try:
    remetente = Texto(
        OrdemServico.Responsavel
    )

    if remetente != "":
        Mensagem.Remetente = remetente

except:
    pass


# ============================================================
# LOG FINAL
# ============================================================

try:
    if len(listaEmailsAdicionados) > 0:
        # Comentario com a lista de destinatarios.
        RegistrarComentario(
            (
                "Destinatarios adicionados a mensagem: {0}"
            ).format(
                "; ".join(
                    listaEmailsAdicionados
                )
            ),
            False
        )

        # Comentario separado para evidenciar o envio.
        RegistrarComentario(
            "E-mail de Pré-Notificação do Índice de Desempenho "
            "de Fornecedores (IDF) enviado com sucesso!",
            False
        )

    else:
        RegistrarComentario(
            "Nenhum destinatario valido foi adicionado a mensagem.",
            False
        )

except:
    pass
```

### [349136] EventoFinal ""
**ScriptFim**
```python
OrdemServico.FinalizadorId = Convert.ToInt32(OrdemServico.ResponsavelId)
```

### [349140] Tarefa "Aprovação"
Responsável: Gestor do Responsável (papel 350)
Config: Codigo=APROV
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptFormCarregado**
```python
import clr
import System

from System import Convert, DBNull


def Texto(valor):
    try:
        if valor is None or valor == DBNull.Value:
            return ""

        texto = Convert.ToString(valor)

        if texto is None:
            return ""

        return texto.Trim()

    except:
        return ""


def DesabilitarCampo(campo):
    try:
        controle = Formulario[campo]
        controle.Habilitado = False
        return True

    except:
        return False


def PreencherCampo(campo, valor):
    try:
        controle = Formulario[campo]
        valorTexto = Texto(valor)

        if valorTexto != "":
            controle.Valor = valorTexto

        controle.Habilitado = False
        return True

    except:
        return False


# ============================================================
# DESABILITA OS CAMPOS DA TAREFA
# ============================================================

campos_desabilitados = [
    "CSC_NUMERO5",
    "CSC_NUMERO6",
    "PENF_EMAIL",
    "DESCRICAO_UM",
    "DESCRICAO_DOIS",
    "FISCAL_DE_SERVICO",
    "FAVORECIDO_COBRA1"
]

for campo in campos_desabilitados:
    DesabilitarCampo(campo)


# ============================================================
# RECUPERA OS DADOS DA PRIMEIRA LINHA DA GRID_IDF
# ============================================================

nome_fornecedor = ""
numero_dgco = ""
ultimo_periodo = ""
erro_grid = ""

try:
    grid = OrdemServico.GetCustom("GRID_IDF")

    for linha in grid.Rows:

        nome_fornecedor = Texto(
            linha["FORNECEDOR"]
        )

        numero_dgco = Texto(
            linha["DGCO"]
        )

        ultimo_periodo = Texto(
            linha["ULTIMO_PERIODO"]
        )

        # Cada associada possui somente uma linha.
        break

except Exception as ex:
    erro_grid = Texto(ex)


# ============================================================
# PREENCHE OS CAMPOS DA TAREFA
# ============================================================

campos_nao_encontrados = []


if not PreencherCampo(
    "FORNECEDOR1",
    nome_fornecedor
):
    campos_nao_encontrados.append(
        "FORNECEDOR1"
    )


if not PreencherCampo(
    "DGCO_BB",
    numero_dgco
):
    campos_nao_encontrados.append(
        "DGCO_BB"
    )


if not PreencherCampo(
    "PERIODO01",
    ultimo_periodo
):
    campos_nao_encontrados.append(
        "PERIODO01"
    )


# ============================================================
# DIAGNÓSTICO
# ============================================================

mensagens = []

if erro_grid != "":
    mensagens.append(
        "Erro ao consultar a GRID_IDF: " +
        erro_grid
    )


if len(campos_nao_encontrados) > 0:
    mensagens.append(
        "Os seguintes controles não foram encontrados "
        "no formulário da tarefa corrente: " +
        ", ".join(campos_nao_encontrados) +
        ". Verifique se os campos foram adicionados à tarefa "
        "e confirme os nomes técnicos."
    )


if len(mensagens) > 0:
    try:
        Formulario.ExibeMensagem(
            "\n\n".join(mensagens)
        )
    except:
        pass
```
- Operação PR0002 Aprovar
  - (aprovação) PERIODO01 "Último Período Avaliado" [TextBox String → CPE_CONTRATOS.PERIODO01]
  - (aprovação) DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
  - (aprovação) FISCAL_SERVI_SGPS "Fiscal de Serviço" [DropDownList String → CPE_PESSOAS.FISCAL_SERVI_SGPS]
  - (aprovação) FISCAL_ADM_SGPS "Fiscal Administrativo" [DropDownList String → CPE_PESSOAS.FISCAL_ADM_SGPS]
  - (aprovação) FAVORECIDO_TODOS "Gestor do Contrato" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - (aprovação) FORNECEDOR1 "Fornecedor" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1]
  - (aprovação) CSC_NUMERO5 "Nota de Avaliação do Fiscal de Serviço" [TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO5]
  - (aprovação) DESCRICAO_UM "Ocorrências Fiscal de Serviço" [Memo String(2000) → CPE_CSC.DESCRICAO_UM]
  - (aprovação) CSC_NUMERO6 "Nota de Avaliação do Fiscal Administrativo" [TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO6]
  - (aprovação) DESCRICAO_DOIS "Ocorrências Fiscal Administrativo" [Memo String(2000) → CPE_CSC.DESCRICAO_DOIS]
  - (aprovação) PENF_EMAIL "E-mails a serem enviados" [TextBox String(2000) → CPE_PENF.PENF_EMAIL]
  - (aprovação) TEXT "Média das Notas dos fiscais" [TextBox String(1000) → CPE_CSC.TEXT]
  - aprovador: Gestor do Responsável (Unico)
- Operação PR0001 Preencher Campos
  - FISCAL_ADM_SGPS "Fiscal Administrativo" [DropDownList String → CPE_PESSOAS.FISCAL_ADM_SGPS]
  - FORNECEDOR1 "Nome do fornecedor" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1]
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
    - coluna BANCO obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA_CORR obrigatório
    - coluna TIPO_CHAVE obrigatório
    - coluna CHAVE_PIX obrigatório
  - PERIODO01 "Último Período Avaliado" [TextBox String → CPE_CONTRATOS.PERIODO01]
  - CSC_NUMERO5 "Nota de Avaliação do Fiscal de Serviço" [TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO5]
  - DESCRICAO_UM "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_UM]
  - CSC_NUMERO6 "Nota de Avaliação do Fiscal Administrativo" [TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO6]
  - DESCRICAO_DOIS "Ocorrências (informe, de forma detalhada, as ocorrências atribuídas ao fornecedor que fundamentaram a avaliação abaixo do esperado. As ocorrências devem ser enumeradas, datadas e separadas por espaço conforme o respectivo IDF registrado no Sissccon/Chamado Avaliativo)" [Memo String(2000) → CPE_CSC.DESCRICAO_DOIS]
  - FISCAL_SERVI_SGPS "Fiscal de Serviço" [DropDownList String → CPE_PESSOAS.FISCAL_SERVI_SGPS]
  - FAVORECIDO_TODOS "Gestor do Contrato" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - PENF_EMAIL "E-mails" [TextBox String(2000) → CPE_PENF.PENF_EMAIL]

## Papéis usados
### papel 980: Fiscal Administrativo Papel
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
fiscalAdministrativo = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_ADM_SGPS")))

if fiscalAdministrativo != None:
    Atores.Adiciona(fiscalAdministrativo, "Fiscal Administrativo")
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos
### papel 350: Gestor do Responsável
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Responsavel.ObtemChefia(False)

# se for um diretor ou presidente (mudar os identificadores e relacionar todos)
if gestor.Id == 4458 or gestor.Id == 4459 or gestor.Id == 4460 or gestor.Id == 4461 or gestor.Id == 3805 or gestor.Id == 5313 or gestor.Id == 5457 or gestor.Id == 5903 or gestor.Id == 13787:
    gestor = Pessoa.Carrega(1194)

Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Responsavel.ToString())
```

## Campos customizados usados (definição global)

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

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### DESCRICAO_UM — Descrições gerais
Memo String(2000) → CPE_CSC.DESCRICAO_UM

### CSC_NUMERO6 — CSC_NUMERO6
TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO6

### CSC_NUMERO5 — CSC_NUMERO5
TextBox String(100) → CPE_BOOTCAMP.CSC_NUMERO5

### DESCRICAO_DOIS — Descrições gerais
Memo String(2000) → CPE_CSC.DESCRICAO_DOIS

### PENF_EMAIL — E-mails que serão notificados sobre o andamento da ordem de serviço (separados por ponto e vírgula)
TextBox String(2000) → CPE_PENF.PENF_EMAIL

### DGCO_BB — DGCO
TextBox String(300) → CPE_FINANCEIRO.DGCO_BB

### FISCAL_SERVI_SGPS — Fiscal de Serviço
DropDownList String → CPE_PESSOAS.FISCAL_SERVI_SGPS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### FISCAL_ADM_SGPS — Fiscal Administrativo
DropDownList String → CPE_PESSOAS.FISCAL_ADM_SGPS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### FORNECEDOR1 — Fornecedor
TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### PERIODO01 — Período 01
TextBox String → CPE_CONTRATOS.PERIODO01

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
