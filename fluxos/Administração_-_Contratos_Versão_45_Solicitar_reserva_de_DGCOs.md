# Fluxo: Solicitar reserva de DGCOs (SOLICITRESERVDG) — versão 45
Caminho: Fluxos > Administração - Contratos Versão 45 Solicitar reserva de DGCOs
XML: `XMLs para teste/Administração_-_Contratos_Versão_45_Solicitar_reserva_de_DGCOs.xml` | Supravizio 19.1.1 | SubProcessoId 21949 | DesenhoProcessoId 3021 | ProcessoId 127
Órgão dono: 3000003341 - CENTRO DE SERVICOS COMPARTILHADOS DE CONTRATOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadoresGrupoEnvolvido; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Solicitar reserva de DGCO (DGCO)

## Grafo do fluxo
- [348475] LinkInicial "" → [348481] Verificar Solicitação
- [348477] EventoInicial "Solicitar Reserva de DGCO" → [348483] Verificar Solicitação
- [348476] EventoIntermediarioMensagem "Conclusão do Chamado" → [348484] 
- [348478] Tarefa "Inserir DGCO" {Responsável atual} → [348476] Conclusão do Chamado
- [348479] LinkInicial "" → [348481] Verificar Solicitação
- [348480] LinkInicial "" → [348483] Verificar Solicitação
- [348481] Tarefa "Verificar Solicitação" {Fila CSC - Contratos} → [348478] Inserir DGCO
- [348482] LinkInicial "" → [348481] Verificar Solicitação
- [348483] Tarefa "Verificar Solicitação" {Fila CSC - Contratos} → [348478] Inserir DGCO
- [348484] EventoFinal "" {Responsável atual} → (fim)
- [348485] LinkInicial "" → [348483] Verificar Solicitação

## Atividades

### [348475] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
OrdemServico.SetCustom('NOME_DAS', OrdemServico.Numero.ToString())
OrdemServico.ModificaCampoFormularioHabilitado('NOME_DAS', False)
OrdemServico.ModificaCampoFormularioVisivel('NOME_DAS', False)

AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
Formulario['CNPJ'].Visivel = False
Formulario['CSC_CPF'].Visivel = False
```
- Operação PR0001 Preencher Campos
  - JURIDICA_FISICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.JURIDICA_FISICA]
**JURIDICA_FISICA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CNPJ'].Visivel = True
    Formulario['CNPJ'].Habilitado = True

if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Física":
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CNPJ'].Visivel = False
    Formulario['CNPJ'].Habilitado = False
```
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
  - RAZAO_SOCIAL_CLIENTE "Razão Social" [TextBox String → CPE_NEGOCIOS.RAZAO_SOCIAL_CLIENTE]
  - COMBOBOX1 "Fornecedor ou Cliente?" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO]
  - DescricaoDetalhada (nativo) "Motivo do cadastro"
  - NOME_DAS "Numero OS PAI" [TextBox String → CP_ORDEM_SERVICO.NOME_DAS]
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Associação de subprocesso: AssociacaoId=1018; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Assinatura de Novos Contratos e Aditivos -> Solicitar reserva de DGCO

### [348477] EventoInicial "Solicitar Reserva de DGCO"
Config: Codigo=RESERVDGCO; Configuracao={"ServicoIniciador":"<Nenhum>"}
TipoSolicitacao: 05.04. Suprimentos Corporativos, Licitações e Contratos - Contratos
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
Formulario['COMBOBOX1'].Itens = 'Fornecedor;Cliente;Demais Intervenientes'
Formulario['CNPJ'].Visivel = False
Formulario['CSC_CPF'].Visivel = False
```
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) "Motivo do cadastro" obrigatório
  - JURIDICA_FISICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.JURIDICA_FISICA] obrigatório
**JURIDICA_FISICA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CNPJ'].Visivel = True
    Formulario['CNPJ'].Habilitado = True

if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Física":
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CNPJ'].Visivel = False
    Formulario['CNPJ'].Habilitado = False
```
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
**CSC_CPF.ScriptModificado**
```python
#sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
#
#lista = DB.ExecuteDataTable(sql)
#if lista.Rows.Count == 0:
#    Formulario.ExibeMensagem("Este CPF não está cadastrado no Gescon, preencha os campos para o cadastro.")
#    Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = True
#else:
#    for linha in lista.Rows:
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Valor = linha["NOME_RAZAO_SOCIAL"]
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = False
```
  - RAZAO_SOCIAL_CLIENTE "Razão Social" [TextBox String → CPE_NEGOCIOS.RAZAO_SOCIAL_CLIENTE] obrigatório
  - COMBOBOX1 "Fornecedor ou Cliente?" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO] obrigatório
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
**CNPJ.ScriptModificado**
```python
#sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
#lista = DB.ExecuteDataTable(sql)
#if lista.Rows.Count == 0:
#    Formulario.ExibeMensagem("Este CNPJ não está cadastrado no Gescon, preencha os campos para o cadastro.")
#    Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = True
#else:
#    for linha in lista.Rows:
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Valor = linha["NOME_RAZAO_SOCIAL"]
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true

### [348476] EventoIntermediarioMensagem "Conclusão do Chamado"
Destinatário: Cliente (papel 18)
Config: Codigo=CONCLUSÃO DO CHAMADO
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Empresa
dgco = OrdemServico.GetCustom("CSC_DGCO").ToString()
razaoSocial = OrdemServico.GetCustom('RAZAO_SOCIAL_CLIENTE').ToString()
nmOs = OrdemServico.Numero.ToString()


mensagem_html = "<html><body style=\"font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px;\"><table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\"><tr><td align=\"center\"><table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); overflow: hidden;\"><tr><td align=\"left\" style=\"background-color: #007BFF; padding: 20px 30px;\"><h1 style=\"color: #ffffff; font-size: 24px; margin: 0; font-weight: 500;\">Chamado Finalizado</h1></td></tr><tr><td align=\"left\" style=\"padding: 30px 30px 40px 30px; color: #333333;\"><p style=\"font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;\">Prezado(a),</p><p style=\"font-size: 16px; line-height: 1.6; margin: 0 0 20px 0;\">O chamado <strong>" + nmOs + "</strong> foi finalizado com sucesso.</p><div style=\"font-size: 16px; line-height: 1.6; background-color: #f8f9fa; border-left: 4px solid #007BFF; padding: 15px; margin-top: 10px;\"><p style=\"margin: 0 0 10px 0;\"><strong>Empresa:</strong> " + razaoSocial + "</p><p style=\"margin: 0;\"><strong>DGCO para referência:</strong> " + dgco + "</p></div></td></tr><tr><td align=\"left\" style=\"padding: 20px 30px; background-color: #f8f9fa; border-top: 1px solid #dee2e6;\"><p style=\"font-size: 14px; color: #6c757d; margin: 0;\">Atenciosamente,<br><span style=\"font-weight: bold;\">Gerência de Suprimentos Corporativos</span></p></td></tr></table></td></tr></table></body></html>"
Mensagem.Assunto = "Solicitar Reserva de DGCO"
Mensagem.Corpo = mensagem_html
```

### [348478] Tarefa "Inserir DGCO"
Responsável: Responsável atual (papel 36)
Config: Codigo=DGCO
**ScriptInicio**
```python
AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - JURIDICA_FISICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.JURIDICA_FISICA] obrigatório
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ]
  - LABEL12 "LABEL12" [Label String(700) → CPE_PDCI2019.LABEL12]
  - CSC_DGCO "Insira o número do DGCO" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}

### [348479] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
OrdemServico.SetCustom('NOME_DAS', OrdemServico.Numero.ToString())
OrdemServico.ModificaCampoFormularioHabilitado('NOME_DAS', False)
OrdemServico.ModificaCampoFormularioVisivel('NOME_DAS', False)

AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
Formulario['CNPJ'].Visivel = False
Formulario['CSC_CPF'].Visivel = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - JURIDICA_FISICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.JURIDICA_FISICA]
**JURIDICA_FISICA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CNPJ'].Visivel = True
    Formulario['CNPJ'].Habilitado = True

if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Física":
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CNPJ'].Visivel = False
    Formulario['CNPJ'].Habilitado = False
```
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
  - RAZAO_SOCIAL_CLIENTE "Razão Social" [TextBox String → CPE_NEGOCIOS.RAZAO_SOCIAL_CLIENTE]
  - COMBOBOX1 "Fornecedor ou Cliente?" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO]
  - DescricaoDetalhada (nativo) "Motivo do cadastro"
  - NOME_DAS "Numero OS PAI" [TextBox String → CP_ORDEM_SERVICO.NOME_DAS]
- Associação de subprocesso: AssociacaoId=1273; Nome=DIEGO ALVES DA SILVA; FraseAssociacao=Assinatura de Novos Contratos e Aditivos ATA -> Solicitar reserva de DGCO

### [348480] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
cnpjfornecedor = OrdemServico.GetCustom('CNPJ_FORNECEDOR')
OrdemServico.SetCustom('CNPJ',  cnpjfornecedor)

fisicajudirica = OrdemServico.GetCustom('FISICA_JUDIRICA')
OrdemServico.SetCustom('JURIDICA_FISICA',  fisicajudirica)
```
- Operação PR0001 Preencher Campos
  - FISICA_JUDIRICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.FISICA_JUDIRICA]
  - JURIDICA_FISICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.JURIDICA_FISICA] obrigatório
  - CNPJ_FORNECEDOR "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR] — Configuracao={"Mascara":"00\\.000\\.000\\/0000\\-00"}
**CNPJ_FORNECEDOR.ScriptModificado**
```python
sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
lista = DB.ExecuteDataTable(sql)
if lista.Rows.Count == 0:
    Formulario.ExibeMensagem("Este CNPJ não está cadastrado no Gescon, preencha os campos para o cadastro.")
    Formulario["NOME_FORNECEDOR"].Habilitado = True
else:
    for linha in lista.Rows:
        Formulario["NOME_FORNECEDOR"].Valor = linha["NOME_FORNECEDOR"]
        Formulario["NOME_FORNECEDOR"].Habilitado = False
```
  - NOME_FORNECEDOR "Razão Social" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR]
  - DescricaoDetalhada (nativo)
- Associação de subprocesso: AssociacaoId=964; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Cadastros Correspondente Bancário -> Solicitar Reserva de DGCO

### [348481] Tarefa "Verificar Solicitação"
Responsável: Fila CSC - Contratos (papel 688)
Config: Codigo=ANALISAR2; ConfirmaResponsabilidade=true; PermiteCancelamentoAA=true
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import clr
import System

from System.Threading import Thread  # Import necessário para o delay
clr.AddReference("System.Net.Http")
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import MediaTypeWithQualityHeaderValue, AuthenticationHeaderValue
from System import TimeSpan
from System.Text import Encoding
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JObject
import unicodedata

# Função para normalizar strings (remove acentos e caracteres especiais)
def normaliza_string(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')

OrdemServico.ModificaCampoFormularioHabilitado('CSC_DGCO',False)       
OrdemServico.ModificaCampoFormularioHabilitado('CSC_CPF',False)
OrdemServico.ModificaCampoFormularioHabilitado('CNPJ',False) 
OrdemServico.ModificaCampoFormularioHabilitado('JURIDICA_FISICA',False) 
OrdemServico.ModificaCampoFormularioHabilitado('RAZAO_SOCIAL_CLIENTE', False)
OrdemServico.ModificaCampoFormularioHabilitado('DescricaoDetalhada', False)

numero_completo = str(OrdemServico.Numero)  # Converte para string
numero_extraido = numero_completo.split('.')[0]

numerodaOSpai = OrdemServico.GetCustom('NOME_DAS').ToString()


lista = Utils.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, ORDEM_SERVICO.ID_OCORRENCIA, OCORRENCIA.NUMERO From OCORRENCIA Inner Join ORDEM_SERVICO On ORDEM_SERVICO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Where OCORRENCIA.NUMERO ='" + numerodaOSpai + "'")

idOcorrencia = 0
for linha in lista.Rows:
    idOcorrencia = linha["ID_OCORRENCIA"]


# Token de autenticação
token = '***MASCARADO***'
url = ''

sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

# URL da API

if dom == 'PRODUÇÃO':    
    url= 'https://sisccon.bbts.com.br/supravizio/supra/gerar-dgco'

else:    
    url= 'https://sisccon-lab.bbts.com.br/supravizio/supra/gerar-dgco'



tipo = str(OrdemServico.GetCustom('COMBOBOX1'))    

# Obtenha o ID do solicitante
idDoSolicitante = OrdemServico.Cliente.Id
matriculaSolicitante = ''
result_table3 = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA From CP_PESSOA Where CP_PESSOA.ID_PESSOA = '" + str(idDoSolicitante) + "'")

for row in result_table3.Rows:
    matriculaSolicitante = str(row['MATRICULA'])

cpf_cnpj = OrdemServico.GetCustom('CSC_CPF').ToString() if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Física' else OrdemServico.GetCustom('CNPJ').ToString()


if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Física' or OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Fisica':
    OrdemServico.SetCustom('JURIDICA_FISICA', 'PESSOA_FISICA')
    OrdemServico.SetCustom('CNPJ', '00000000000000')
    
if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Jurídica' or OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Juridica':
    OrdemServico.SetCustom('JURIDICA_FISICA', 'PESSOA_JURIDICA')
    OrdemServico.SetCustom('CSC_CPF', '00000000000')



# Normalizando strings para evitar problemas de codificação
razao_social = normaliza_string(OrdemServico.GetCustom('RAZAO_SOCIAL_CLIENTE').ToString())
fisica_juridica = normaliza_string(OrdemServico.GetCustom('JURIDICA_FISICA').ToString())

# Definição do objeto JSON
data = {
    "matricula_solicitante": matriculaSolicitante,
    "nr_os": str(OrdemServico.Numero),
    "motivo": OrdemServico.DescricaoDetalhada.ToString(),
    "cnpj_cpf": str(cpf_cnpj),
    "tipo": str(tipo),
    "razao_social": razao_social,
    "fisica_juridica": fisica_juridica 
}

# Log para verificar os dados que estão sendo enviados
#OrdemServico.AdicionaComentario(str(data), True)

# Serialização do JSON
dados = StringContent(JsonConvert.SerializeObject(data), Encoding.UTF8, "application/json")

# Inicializa o HttpClient e configura os cabeçalhos
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Clear()
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)



# Envia a requisição POST
response = client.PostAsync(url, dados)
response.Wait()

# Verifica o código de status da resposta
if response.Result.IsSuccessStatusCode:
    # Lê o conteúdo da resposta
    resultAsync = response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result

    try:
        # Verifica se o JSON é uma string encapsulada e tenta deserializar
        if result.startswith("\"") and result.endswith("\""):
            # Remove as aspas extras
            result = JsonConvert.DeserializeObject(result)

        # Tenta deserializar o JSON como um objeto
        jsonObject = JObject.Parse(result)
        #OrdemServico.AdicionaComentario(result.ToString(), True)

        OrdemServico.SetCustom('CSC_DGCO', jsonObject.dgco.ToString())
        
        
        
        
        pai = OrdemServico.Carrega(Convert.ToInt32(idOcorrencia))
        pai.SetCustom('CSC_DGCO', jsonObject.dgco.ToString())
        pai.Salva()
        
                                    
                            

        
        OrdemServico.ModificaCampoFormularioHabilitado('CSC_DGCO', False)
        OrdemServico.ModificaCampoFormularioHabilitado('CSC_DGCO', False)
        OrdemServico.ModificaCampoFormularioHabilitado('CSC_CPF', False)
        OrdemServico.ModificaCampoFormularioHabilitado('CNPJ', False)
        OrdemServico.ModificaCampoFormularioHabilitado('JURIDICA_FISICA', False)
        OrdemServico.ModificaCampoFormularioHabilitado('RAZAO_SOCIAL_CLIENTE', False)
        OrdemServico.ModificaCampoFormularioHabilitado('DescricaoDetalhada', False)
        
        OrdemServico.ModificaCampoFormularioVisivel('CSC_DGCO', True)
        OrdemServico.ModificaCampoFormularioVisivel('CSC_DGCO', True)
        OrdemServico.ModificaCampoFormularioVisivel('CSC_CPF', True)
        OrdemServico.ModificaCampoFormularioVisivel('CNPJ', True)
        OrdemServico.ModificaCampoFormularioVisivel('JURIDICA_FISICA', True)
        OrdemServico.ModificaCampoFormularioVisivel('RAZAO_SOCIAL_CLIENTE', True)
        OrdemServico.ModificaCampoFormularioVisivel('DescricaoDetalhada', True)
        #pass

    except Exception as e:
        #OrdemServico.AdicionaComentario("Erro de extração: {0}".format(str(e)), False)
        pass

else:
    #OrdemServico.AdicionaComentario(response.Result.StatusCode.ToString(), False)
    pass

AvancaProximaAtividade = True
```
**ScriptFim**
```python
numero_completo = str(OrdemServico.Numero)  # Converte para string
numero_extraido = numero_completo.split('.')[0]

numerodaOSpai = OrdemServico.GetCustom('NOME_DAS').ToString()


lista = Utils.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, ORDEM_SERVICO.ID_OCORRENCIA, OCORRENCIA.NUMERO From OCORRENCIA Inner Join ORDEM_SERVICO On ORDEM_SERVICO.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA Where OCORRENCIA.NUMERO ='" + numerodaOSpai + "'")

idOcorrencia = 0
for linha in lista.Rows:
    idOcorrencia = linha["ID_OCORRENCIA"]
    
    
    
    
pai = OrdemServico.Carrega(Convert.ToInt32(idOcorrencia))
pai.SetCustom('CSC_DGCO', OrdemServico.GetCustom('CSC_DGCO').ToString())
pai.Salva()
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario['COMBOBOX1'].Itens = 'Fornecedor;Cliente'
Formulario['JURIDICA_FISICA'].Valor = 'Pessoa Jurídica'
```

### [348482] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
OrdemServico.SetCustom('NOME_DAS', OrdemServico.Numero.ToString())
OrdemServico.ModificaCampoFormularioHabilitado('NOME_DAS', False)
OrdemServico.ModificaCampoFormularioVisivel('NOME_DAS', False)
OrdemServico.SetCustom('JURIDICA_FISICA', 'Pessoa Jurídica')

AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario['CNPJ'].Visivel = False
Formulario['CSC_CPF'].Visivel = False

Formulario['JURIDICA_FISICA'].Valor = 'Pessoa Jurídica'
Formulario['COMBOBOX1'].Valor = 'Cliente'

Formulario['FORNECEDOR1'].Visivel = False



if OrdemServico.Servico.Sigla == 'ASSINACOMODATO' or OrdemServico.Servico.Sigla == 'ASSINACONSIG' or OrdemServico.Servico.Sigla == 'ASSINACONSIGN':
    Formulario['RAZAO_SOCIAL_CLIENTE'].Valor = Formulario['FORNECEDOR1'].Valor
```
- Operação PR0001 Preencher Campos
  - FORNECEDOR1 "Razão Social" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1]
  - JURIDICA_FISICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.JURIDICA_FISICA]
**JURIDICA_FISICA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CNPJ'].Visivel = True
    Formulario['CNPJ'].Habilitado = True

if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Física":
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CNPJ'].Visivel = False
    Formulario['CNPJ'].Habilitado = False
```
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
  - RAZAO_SOCIAL_CLIENTE "Razão Social" [TextBox String → CPE_NEGOCIOS.RAZAO_SOCIAL_CLIENTE]
  - COMBOBOX1 "Fornecedor ou Cliente?" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO]
  - DescricaoDetalhada (nativo) "Motivo do cadastro"
  - NOME_DAS "Numero OS PAI" [TextBox String → CP_ORDEM_SERVICO.NOME_DAS]
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Associação de subprocesso: AssociacaoId=1644; Nome=RICARDO ALVES COSTA; FraseAssociacao=Comodato -> Solicitar DGCO
- Associação de subprocesso: AssociacaoId=1645; Nome=RICARDO ALVES COSTA; FraseAssociacao=Consignante -> Solicitar DGCO
- Associação de subprocesso: AssociacaoId=1646; Nome=RICARDO ALVES COSTA; FraseAssociacao=Consignatários -> Solicitar DGCO

### [348483] Tarefa "Verificar Solicitação"
Responsável: Fila CSC - Contratos (papel 688)
Config: Codigo=ANALISAR; ConfirmaResponsabilidade=true; PermiteCancelamentoAA=true
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import clr
import System

from System.Threading import Thread  # Import necessário para o delay
clr.AddReference("System.Net.Http")
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import MediaTypeWithQualityHeaderValue, AuthenticationHeaderValue
from System import TimeSpan
from System.Text import Encoding
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JObject
import unicodedata


def normaliza_string(s):
    # --- INÍCIO DA ALTERAÇÃO ---
    # O IronPython (baseado em Python 2.7) diferencia 'str' (bytes) de 'unicode'
    # Vamos garantir que estamos trabalhando com uma string unicode antes de normalizar.
    if isinstance(s, str) and not isinstance(s, unicode):
        try:
            # Tenta decodificar usando 'cp1252', o mais comum para Windows em português
            s = s.decode('cp1252')
        except UnicodeDecodeError:
            # Se falhar, tenta com 'latin-1', que é mais robusto e não deve dar erro
            s = s.decode('latin-1')
    # --- FIM DA ALTERAÇÃO ---
            
    # O resto da sua função continua igual
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')

OrdemServico.ModificaCampoFormularioHabilitado('CSC_DGCO',False)
OrdemServico.ModificaCampoFormularioHabilitado('CSC_CPF',False)
OrdemServico.ModificaCampoFormularioHabilitado('CNPJ',False) 
OrdemServico.ModificaCampoFormularioHabilitado('JURIDICA_FISICA',False) 
OrdemServico.ModificaCampoFormularioHabilitado('RAZAO_SOCIAL_CLIENTE', False)
OrdemServico.ModificaCampoFormularioHabilitado('DescricaoDetalhada', False)

# Token de autenticação
token = '***MASCARADO***'
url = ''

sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

# URL da API

if dom == 'PRODUÇÃO':    
    url= 'https://sisccon.bbts.com.br/supravizio/supra/gerar-dgco'

else:    
    url= 'https://sisccon-lab.bbts.com.br/supravizio/supra/gerar-dgco'



tipo = str(OrdemServico.GetCustom('COMBOBOX1'))    

# Obtenha o ID do solicitante
idDoSolicitante = OrdemServico.Cliente.Id
matriculaSolicitante = ''
result_table3 = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA From CP_PESSOA Where CP_PESSOA.ID_PESSOA = '" + str(idDoSolicitante) + "'")

for row in result_table3.Rows:
    matriculaSolicitante = str(row['MATRICULA'])

cpf_cnpj = OrdemServico.GetCustom('CSC_CPF').ToString() if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Física' else OrdemServico.GetCustom('CNPJ').ToString()


if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Física' or OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Fisica':
    OrdemServico.SetCustom('JURIDICA_FISICA', 'PESSOA_FISICA')
    OrdemServico.SetCustom('CNPJ', '00000000000000')
    
if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Jurídica' or OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Juridica':
    OrdemServico.SetCustom('JURIDICA_FISICA', 'PESSOA_JURIDICA')
    OrdemServico.SetCustom('CSC_CPF', '00000000000')



# Normalizando strings para evitar problemas de codificação
razao_social = normaliza_string(OrdemServico.GetCustom('RAZAO_SOCIAL_CLIENTE').ToString())
fisica_juridica = normaliza_string(OrdemServico.GetCustom('JURIDICA_FISICA').ToString())

# Definição do objeto JSON
data = {
    "matricula_solicitante": matriculaSolicitante,
    "nr_os": str(OrdemServico.Numero),
    "motivo": OrdemServico.DescricaoDetalhada.ToString(),
    "cnpj_cpf": str(cpf_cnpj),
    "tipo": str(tipo),
    "razao_social": razao_social,
    "fisica_juridica": fisica_juridica 
}

# Log para verificar os dados que estão sendo enviados
#OrdemServico.AdicionaComentario(str(data), True)

# Serialização do JSON
dados = StringContent(JsonConvert.SerializeObject(data), Encoding.UTF8, "application/json")

# Inicializa o HttpClient e configura os cabeçalhos
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Clear()
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)



# Envia a requisição POST
response = client.PostAsync(url, dados)
response.Wait()

# Verifica o código de status da resposta
if response.Result.IsSuccessStatusCode:
    # Lê o conteúdo da resposta
    resultAsync = response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result

    try:
        # Verifica se o JSON é uma string encapsulada e tenta deserializar
        if result.startswith("\"") and result.endswith("\""):
            # Remove as aspas extras
            result = JsonConvert.DeserializeObject(result)

        # Tenta deserializar o JSON como um objeto
        jsonObject = JObject.Parse(result)
        #OrdemServico.AdicionaComentario(result.ToString(), True)

        OrdemServico.SetCustom('CSC_DGCO', jsonObject.dgco.ToString())
        OrdemServico.ModificaCampoFormularioHabilitado('CSC_DGCO', False)
        OrdemServico.ModificaCampoFormularioHabilitado('CSC_DGCO', False)
        OrdemServico.ModificaCampoFormularioHabilitado('CSC_CPF', False)
        OrdemServico.ModificaCampoFormularioHabilitado('CNPJ', False)
        OrdemServico.ModificaCampoFormularioHabilitado('JURIDICA_FISICA', False)
        OrdemServico.ModificaCampoFormularioHabilitado('RAZAO_SOCIAL_CLIENTE', False)
        OrdemServico.ModificaCampoFormularioHabilitado('DescricaoDetalhada', False)
        
        OrdemServico.ModificaCampoFormularioVisivel('CSC_DGCO', True)
        OrdemServico.ModificaCampoFormularioVisivel('CSC_DGCO', True)
        OrdemServico.ModificaCampoFormularioVisivel('CSC_CPF', True)
        OrdemServico.ModificaCampoFormularioVisivel('CNPJ', True)
        OrdemServico.ModificaCampoFormularioVisivel('JURIDICA_FISICA', True)
        OrdemServico.ModificaCampoFormularioVisivel('RAZAO_SOCIAL_CLIENTE', True)
        OrdemServico.ModificaCampoFormularioVisivel('DescricaoDetalhada', True)
        #pass

    except Exception as e:
        #OrdemServico.AdicionaComentario("Erro de extração: {0}".format(str(e)), False)
        pass

else:
    #OrdemServico.AdicionaComentario(response.Result.StatusCode.ToString(), False)
    pass

AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
Formulario['COMBOBOX1'].Itens = 'Fornecedor;Cliente;Demais Intervenientes'
```
- Operação PR0001 Preencher Campos
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
**CSC_CPF.ScriptModificado**
```python
#sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
#
#lista = DB.ExecuteDataTable(sql)
#if lista.Rows.Count == 0:
#    Formulario.ExibeMensagem("Este CPF não está cadastrado no Gescon, preencha os campos para o cadastro.")
#    Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = True
#else:
#    for linha in lista.Rows:
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Valor = linha["NOME_RAZAO_SOCIAL"]
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = False
```
  - JURIDICA_FISICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.JURIDICA_FISICA] obrigatório
**JURIDICA_FISICA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CNPJ'].Visivel = True
    Formulario['CNPJ'].Habilitado = True

if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Física":
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CNPJ'].Visivel = False
    Formulario['CNPJ'].Habilitado = False
```
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
**CNPJ.ScriptModificado**
```python
#sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
#lista = DB.ExecuteDataTable(sql)
#if lista.Rows.Count == 0:
#    Formulario.ExibeMensagem("Este CNPJ não está cadastrado no Gescon, preencha os campos para o cadastro.")
#    Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = True
#else:
#    for linha in lista.Rows:
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Valor = linha["NOME_RAZAO_SOCIAL"]
#        Formulario["RAZAO_SOCIAL_CLIENTE"].Habilitado = False
```
  - RAZAO_SOCIAL_CLIENTE "Razão Social" [TextBox String → CPE_NEGOCIOS.RAZAO_SOCIAL_CLIENTE] obrigatório
  - COMBOBOX1 "Fornecedor ou Cliente?" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - DescricaoDetalhada (nativo) obrigatório
  - OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO]

### [348484] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
**ScriptInicio**
```python
import clr
import System
clr.AddReference("System.Net.Http")
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import MediaTypeWithQualityHeaderValue, AuthenticationHeaderValue
from System import TimeSpan
from System.Text import Encoding
clr.AddReference("Newtonsoft.Json")
from Newtonsoft.Json import JsonConvert
from Newtonsoft.Json.Linq import JObject



# Token de autenticação
token = '***MASCARADO***'
url = ''

url2 = ''

sql = "select name from sv_domain where enabled = 'Sim'"

dom = DB.ExecuteScalar(sql)

# URL da API
if dom == 'HOMOLOGAÇÃO':
    url2 = 'https://sisccon-lab.bbts.com.br/supravizio/supra/atualizar-dgco-processo-dilic?dgco=' + OrdemServico.GetCustom('CSC_DGCO').ToString() + '&os=' + OrdemServico.Numero.ToString()

if dom == 'PRODUÇÃO':
    url2 = 'https://sisccon.bbts.com.br/supravizio/supra/atualizar-dgco-processo-dilic?dgco=' + OrdemServico.GetCustom('CSC_DGCO').ToString() + '&os=' + OrdemServico.Numero.ToString()

    
    
#OrdemServico.AdicionaComentario(url2.ToString(), True)
# Inicializa o HttpClient e configura os cabeçalhos
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Clear()
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

# Envia a requisição GET
response2 = client.GetAsync(url2)
response2.Wait()

# Verifica o código de status da resposta
if response2.Result.IsSuccessStatusCode:
    # Lê o conteúdo da resposta
    resultAsync2 = response2.Result.Content.ReadAsStringAsync()
    resultAsync2.Wait()
    result2 = resultAsync2.Result
    
    #OrdemServico.AdicionaComentario(result2.ToString(), True)
    
    AvancaProximaAtividade = True
else:
    # Em caso de erro, adiciona o comentário com o código de erro
    #OrdemServico.AdicionaComentario(response2.Result.StatusCode.ToString(), False)
    pass
```

### [348485] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if OrdemServico.GetCustom('JURIDICA_FISICA') == "Pessoa Jurídica":
    sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+OrdemServico.GetCustom("CNPJ").ToString()+"','.',''),'/',''),'-','')"
    lista = DB.ExecuteDataTable(sql)
    if lista.Rows.Count == 0:
        DB.ExecuteNonQuery("call xxbbtsgate.pr_insere_fornecedor_sv('"+OrdemServico.GetCustom("RAZAO_SOCIAL_CLIENTE")+"',replace(replace(replace('"+OrdemServico.GetCustom("CNPJ").ToString()+"','.',''),'/',''),'-',''),'PESSOA_JURIDICA')")

if OrdemServico.GetCustom('JURIDICA_FISICA') == "Pessoa Física":
    sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+OrdemServico.GetCustom("CSC_CPF").ToString()+"','.',''),'/',''),'-','')"
    lista = DB.ExecuteDataTable(sql)
    if lista.Rows.Count == 0:
        DB.ExecuteNonQuery("call xxbbtsgate.pr_insere_fornecedor_sv('"+OrdemServico.GetCustom("RAZAO_SOCIAL_CLIENTE")+"',replace(replace(replace('"+OrdemServico.GetCustom("CSC_CPF").ToString()+"','.',''),'/',''),'-',''),'PESSOA_FISICA')")
```
**ScriptValidacao**
```python
sql = "select count(1) from bbts_gescon_funcionario P where p.matricula = '"+OrdemServico.Cliente["MATRICULA"].ToString()+"'"
resultado = DB.ExecuteScalar(sql)
if resultado.ToString() == '0':
    Criticas.AdicionaPendencia('O Solicitante não está devidamente cadastrado no Gescon!')
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CNPJ'].Visivel = True
    Formulario['CNPJ'].Habilitado = True

if Formulario['JURIDICA_FISICA'].Valor == "Pessoa Física":
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CNPJ'].Visivel = False
    Formulario['CNPJ'].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Associação de subprocesso: AssociacaoId=540; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Novas parcerias - Clube de Desconto Gepes -> Solicitar reserva de DGCO

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos

## Campos customizados usados (definição global)

### JURIDICA_FISICA — Pessoa Jurídica ou Pessoa Física
DropDownList String → CPE_CSC.JURIDICA_FISICA
Itens: 
Pessoa Física;Pessoa Jurídica

### CNPJ — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ

### CSC_CPF — CPF
TextBox String(300) → CPE_CSC.CSC_CPF

### RAZAO_SOCIAL_CLIENTE — Razão Social do Cliente
TextBox String → CPE_NEGOCIOS.RAZAO_SOCIAL_CLIENTE

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### OBJETO_CONTRATACAO — Objeto da Contratação
Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO

### NOME_DAS — Nome
TextBox String → CP_ORDEM_SERVICO.NOME_DAS

### LABEL12 — LABEL12
Label String(700) → CPE_PDCI2019.LABEL12

### CSC_DGCO — DGCO
TextBox String → CPE_CSC.CSC_DGCO

### FISICA_JUDIRICA — Pessoa Jurídica ou Pessoa Física
DropDownList String → CPE_CSC.FISICA_JUDIRICA
Itens: Pessoa Jurídica;Pessoa Física

### CNPJ_FORNECEDOR — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### FORNECEDOR1 — Fornecedor
TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
