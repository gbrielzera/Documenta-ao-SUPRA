# Fluxo: Termo de Designação de Interveniente  (TERMODEDESIGNACAO) — versão 4
Caminho: Fluxos > Designações Versão 4 Termo de Designação de Interveniente 
XML: `XMLs para teste/Designações_Versão_4_Termo_de_Designação_de_Interveniente_.xml` | Supravizio 19.1.1 | SubProcessoId 21106 | DesenhoProcessoId 2949 | ProcessoId 496
Órgão dono: 3000003140 - DIVISAO DE GESTAO DE CONTRATOS COM FORNECEDORES | Responsável: DIEGO ALVES DA SILVA
Classe do subprocesso: DescricaoCliente=Termo de Designação de Interveniente; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true

## Grafo do fluxo
- [342500] EventoFinal "" {Responsável atual} → (fim)
- [342501] EventoIntermediarioMensagem "Aviso Aprovação" → [342509] Atualizar Sisccon
- [342502] EventoIntermediarioMensagem "Aviso Designação" → [342505] Aprovar Termo de Designação
- [342503] EventoIntermediarioMensagem "Aviso Aprovação" → [342509] Atualizar Sisccon
- [342505] Tarefa "Aprovar Termo de Designação" {Fila CSC - Contratos} → [342511]  | [342510]  | [G77513] Designação Aceita?
- [342506] LinkInicial "Abertura Manual Designação" → [342505] Aprovar Termo de Designação
- [342504] LinkInicial "Movimentação" → [342505] Aprovar Termo de Designação
- [342507] LinkInicial "Comissão" → [342505] Aprovar Termo de Designação
- [342508] LinkInicial "OnBoard" → [342505] Aprovar Termo de Designação
- [342509] Tarefa "Atualizar Sisccon" {Responsável atual} → [342500] 
- [342510] EventoIntermediarioTimer "" → [342502] Aviso Designação
- [342511] EventoIntermediarioTimer "" → [342502] Aviso Designação
- [G77513] Gateway "Designação Aceita?" → «Reprovado» [342501] Aviso Aprovação | «Aprovado» [342503] Aviso Aprovação

## Gateways
### [G77513] Designação Aceita? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("FISCALADM")
```
- alternativa → [342501] Aviso Aprovação: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=3
**ValorComparacaoDecision**
```python
False
```
- alternativa → [342503] Aviso Aprovação: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=2
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [342500] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [342501] EventoIntermediarioMensagem "Aviso Aprovação"
Destinatário: Favorecido All (papel 1119)
ModeloComunicado: Termo de Designação Aceite
Corpo do comunicado: Pelo presente termo, fica designado(a) o(a) 
Colaborador(a) :OrdemServico.Customizado.FAVORECIDO_ALL 
Matricula nº OrdemServico.Customizado.CSC_MATRICULA, para exercer as funções de OrdemServico.Customizado.TIPO_DESIGNACAO_INTERV 
OrdemServico.Customizado.DESIGNA_TITU_OR_SUPDGCO: OrdemServico.Customizado.DGCO_BB , conforme dispõe o PRO412-017 Designação dos Intervenientes Envolvidos na Fiscalização Contratual.
ATRIBUIÇÕES DO FISCAL DE SERVIÇO:Acompanhar e fiscalizar a execução do contrato, garantindo que todos os serviços sejam prestados conforme os termos acordados; Verificar a conformidade dos serviços executados com as especificações técnicas e demais condições estabelecidas no contrato; …
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
correcoes = OrdemServico.ObtemMotivoReprovacao('FISCALADM').ToString()



linkChamado = ''
nomeFiscal = ''
matriculaDesignado = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
tipoDesignacao = OrdemServico.GetCustom('TIPO_DESIGNACAO_INTERV').ToString()
titular_suplente = OrdemServico.GetCustom('DESIGNA_TITU_OR_SUP').ToString()
dgco = OrdemServico.GetCustom('DGCO_BB').ToString()
idOs = OrdemServico.Id.ToString()
obs = OrdemServico.GetCustom('OBS7').ToString()


idGerente = OrdemServico.Cliente.Id.ToString()

sql = "select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'HOMOLOGAÇÃO':
    linkChamado = 'https://santacruz1.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&TID=43'

if dom == 'PRODUÇÃO':
    linkChamado = 'https://santacruz.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&TID=43'



def formatar_tipo_designacao(tipo, titular_suplente):
    mapa = {
        'FISCALIZACAO_ADMINISTRATIVA': 'Fiscal Administrativo',
        'GESTAO_CONTRATO': 'Gestão do Contrato',
        'FISCALIZACAO_SERVICO': 'Fiscal de Serviço'
    }
    tipo_formatado = mapa.get(tipo.upper(), tipo.replace("_", " ").title())

    if titular_suplente:
        titular_suplente = titular_suplente.strip().capitalize()
        tipo_formatado += ' ' + titular_suplente

    return tipo_formatado

tipoFormatado = formatar_tipo_designacao(tipoDesignacao, titular_suplente)




if not String.IsNullOrEmpty(str(matriculaDesignado)):
    fiscal = Utils.ExecuteDataTable("SELECT CP_PESSOA.MATRICULA, PESSOA.NOME FROM PESSOA INNER JOIN CP_PESSOA ON CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA WHERE CP_PESSOA.MATRICULA = '" + matriculaDesignado + "'")
    for linha in fiscal.Rows:
        nomeFiscal = linha["NOME"]


emailGestor = ''  
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.ID_PESSOA ='" + idGerente + "'")
#Adiciona o e-mail ao dicionário
for linha2 in lista.Rows:
    emailGestor = linha2["EMAIL"].ToString()

if emailGestor:
    Mensagem.Destinatarios.Add(emailGestor)
Mensagem.Assunto = "Designação aprovada pelo Fiscal - Acompanhamento"

Mensagem.Corpo = '<html><head><style>body{margin:0;padding:40px;font-family:Arial,sans-serif;color:#0033a0;background-color:#f5f5f5;} .container{background-color:#ffffff;border-radius:10px;padding:30px;box-shadow:0 4px 8px rgba(0,0,0,0.1);} h1,h2{color:#0033a0;} a{color:#fff;text-decoration:none;font-weight:bold;} a:hover{text-decoration:none;} p{margin-bottom:15px;line-height:1.6;} .button{display:inline-block;padding:12px 20px;font-size:16px;border-radius:5px;background-color:#0033a0;color:#ffffff;text-align:center;transition:background-color 0.3s ease;} .button:hover{background-color:#002080;} ul{margin-top:10px;margin-bottom:20px;padding-left:20px;} li{margin-bottom:8px;}</style></head><body><div class="container"><h1>Designação de Fiscal Contratual</h1><p>Prezado(a) <strong>' + nomeFiscal + '</strong> (<strong>' + matriculaDesignado + '</strong>),</p><p>Informamos que, apesar das considerações registradas no momento da sua ciência:</p><p><em><strong>' + correcoes + '</strong></em></p><p>Sua designação foi efetivada como <strong>' + tipoFormatado + '</strong> para atuar na fiscalização do contrato relacionado ao <strong>DGCO:</strong> ' + dgco + ', conforme dispõe o <strong>PRO412-017 - Designação dos Intervenientes Envolvidos na Fiscalização Contratual</strong>.</p><p>Para mais detalhes ou acompanhamento da Ordem de Serviço (OS), clique no botão abaixo:</p><p><a href="' + str(linkChamado) + '" class="button">Acessar OS</a></p><h2>Atribuições do Fiscal</h2><ul><li>Acompanhar e fiscalizar a execução do contrato, garantindo que todos os serviços sejam prestados conforme os termos acordados;</li><li>Verificar a conformidade dos serviços executados com as especificações técnicas e demais condições estabelecidas no contrato;</li><li>Registrar e reportar quaisquer irregularidades, falhas ou desvios identificados durante a execução dos serviços;</li><li>Elaborar relatórios periódicos de acompanhamento da execução do contrato;</li><li>Propor medidas corretivas e preventivas para assegurar o cumprimento integral do contrato;</li><li>Atuar em conformidade com as normas e diretrizes estabelecidas pela BB TECNOLOGIA E SERVIÇOS e pela legislação vigente.</li></ul><p>Atenciosamente,</p><p><strong>Divisão de Contratos com Fornecedores</strong></p></div></body></html>'
```

### [342502] EventoIntermediarioMensagem "Aviso Designação"
Destinatário: Favorecido All (papel 1119)
ModeloComunicado: Aprovação de Termo Designação Pendente
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_ALL.
Você foi indicado para: 
OrdemServico.Customizado.TIPO_DESIGNACAO_INTERV 
OrdemServico.Customizado.DESIGNA_TITU_OR_SUPComunicado: O Gestor Contratante indicou os intervenientes deste contrato, que consta disponibilizado no sistema Sisccon, conforme NI412, PRO412-015 e PRO412-017. 
DGCO: OrdemServico.Customizado.DGCO_BB 
NOME DO FORNECEDOR:OrdemServico.Customizado.NOME_FORNECEDOR ,
Gestor Contratante: OrdemServico.Customizado.FAVORECIDO_NOME,
OBJETO: OrdemServico.Customizado.OBJETO_CONTRATO.
Clique aqui para aprovar a designação Link.Aprovacao.
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
linkChamado = ''
nomeFiscal = ''
matriculaDesignado = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
tipoDesignacao = OrdemServico.GetCustom('TIPO_DESIGNACAO_INTERV').ToString()
titular_suplente = OrdemServico.GetCustom('DESIGNA_TITU_OR_SUP').ToString()
dgco = OrdemServico.GetCustom('DGCO_BB').ToString()
idOs = OrdemServico.Id.ToString()


idGerente = OrdemServico.Cliente.Id.ToString()

sql = "select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'HOMOLOGAÇÃO':
    linkChamado = 'https://santacruz1.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&TID=43'

if dom == 'PRODUÇÃO':
    linkChamado = 'https://santacruz.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&TID=43'


def formatar_tipo_designacao(tipo, titular_suplente):
    mapa = {
        'FISCALIZACAO_ADMINISTRATIVA': 'Fiscal Administrativo',
        'GESTAO_CONTRATO': 'Gestão do Contrato',
        'FISCALIZACAO_SERVICO': 'Fiscal de Serviço'
    }
    tipo_formatado = mapa.get(tipo.upper(), tipo.replace("_", " ").title())

    if titular_suplente:
        titular_suplente = titular_suplente.strip().capitalize()
        tipo_formatado += ' ' + titular_suplente

    return tipo_formatado

tipoFormatado = formatar_tipo_designacao(tipoDesignacao, titular_suplente)


if not String.IsNullOrEmpty(str(matriculaDesignado)):
    fiscal = Utils.ExecuteDataTable("SELECT CP_PESSOA.MATRICULA, PESSOA.NOME FROM PESSOA INNER JOIN CP_PESSOA ON CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA WHERE CP_PESSOA.MATRICULA = '" + matriculaDesignado + "'")
    for linha in fiscal.Rows:
        nomeFiscal = linha["NOME"]


emailGestor = ''
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.ID_PESSOA ='" + idGerente + "'")
#Adiciona o e-mail ao dicionário
for linha2 in lista.Rows:
    emailGestor = linha2["EMAIL"].ToString()

    
if tipoDesignacao.ToString() == 'FISCALIZACAO_ADMINISTRATIVA':
    emailGestor = 'andrea.rezende@bbts.com.br'
    Mensagem.Destinatarios.Add(emailGestor)
    
else:
    if emailGestor:
        Mensagem.Destinatarios.Add(emailGestor)



Mensagem.Assunto = "Termo de ciência de designação encaminhado para o Fiscal - Acompanhamento"

Mensagem.Corpo = '<html><head><style>body{margin:0;padding:40px;font-family:Arial,sans-serif;color:#0033a0;background-color:#f5f5f5;} .container{background-color:#ffffff;border-radius:10px;padding:30px;box-shadow:0 4px 8px rgba(0,0,0,0.1);} h1,h2{color:#0033a0;} a{color:#fff;text-decoration:none;font-weight:bold;} a:hover{text-decoration:none;} p{margin-bottom:15px;line-height:1.6;} .button{display:inline-block;padding:12px 20px;font-size:16px;border-radius:5px;background-color:#0033a0;color:#ffffff;text-align:center;transition:background-color 0.3s ease;} .button:hover{background-color:#002080;} ul{margin-top:10px;margin-bottom:20px;padding-left:20px;} li{margin-bottom:8px;}</style></head><body><div class="container"><h1>Designação de Fiscal Contratual</h1><p>Prezado(a) <strong>' + nomeFiscal + '</strong> (<strong>' + matriculaDesignado + '</strong>),</p><p>Informamos que você foi designado(a) como <strong>' + tipoFormatado + '</strong> para atuar na fiscalização do contrato relacionado ao <strong>DGCO:</strong> ' + dgco + ', conforme estabelece o <strong>PRO412-017 - Designação dos Intervenientes Envolvidos na Fiscalização Contratual</strong>.</p><p>Ressaltamos que o chamado de designação encontra-se <strong>pendente de sua ciência e aprovação</strong>. É imprescindível que acesse o chamado, analise as informações e registre sua manifestação para conclusão do processo de designação.</p><p>Para acessar o chamado e registrar sua ciência, clique no botão abaixo:</p><p><a href="' + str(linkChamado) + '" class="button">Acessar OS</a></p><h2>Atribuições do Fiscal</h2><ul><li>Acompanhar e fiscalizar a execução do contrato, garantindo que todos os serviços sejam prestados conforme os termos acordados;</li><li>Verificar a conformidade dos serviços executados com as especificações técnicas e demais condições estabelecidas no contrato;</li><li>Registrar e reportar quaisquer irregularidades, falhas ou desvios identificados durante a execução dos serviços;</li><li>Elaborar relatórios periódicos de acompanhamento da execução do contrato;</li><li>Propor medidas corretivas e preventivas para assegurar o cumprimento integral do contrato;</li><li>Atuar em conformidade com as normas e diretrizes estabelecidas pela BB TECNOLOGIA E SERVIÇOS e pela legislação vigente.</li></ul><p>Atenciosamente,</p><p><strong>Divisão de Contratos com Fornecedores</strong></p></div></body></html>'
```

### [342503] EventoIntermediarioMensagem "Aviso Aprovação"
Destinatário: Favorecido All (papel 1119)
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
linkChamado = ''
nomeFiscal = ''
matriculaDesignado = OrdemServico.GetCustom('CSC_MATRICULA').ToString()
tipoDesignacao = OrdemServico.GetCustom('TIPO_DESIGNACAO_INTERV').ToString()
titular_suplente = OrdemServico.GetCustom('DESIGNA_TITU_OR_SUP').ToString()
dgco = OrdemServico.GetCustom('DGCO_BB').ToString()
idOs = OrdemServico.Id.ToString()



idGerente = OrdemServico.Cliente.Id.ToString()

sql = "select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'HOMOLOGAÇÃO':
    linkChamado = 'https://santacruz1.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&TID=43'

if dom == 'PRODUÇÃO':
    linkChamado = 'https://santacruz.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&TID=43'



def formatar_tipo_designacao(tipo, titular_suplente):
    mapa = {
        'FISCALIZACAO_ADMINISTRATIVA': 'Fiscal Administrativo',
        'GESTAO_CONTRATO': 'Gestão do Contrato',
        'FISCALIZACAO_SERVICO': 'Fiscal de Serviço'
    }
    tipo_formatado = mapa.get(tipo.upper(), tipo.replace("_", " ").title())

    if titular_suplente:
        titular_suplente = titular_suplente.strip().capitalize()
        tipo_formatado += ' ' + titular_suplente

    return tipo_formatado

tipoFormatado = formatar_tipo_designacao(tipoDesignacao, titular_suplente)




if not String.IsNullOrEmpty(str(matriculaDesignado)):
    fiscal = Utils.ExecuteDataTable("SELECT CP_PESSOA.MATRICULA, PESSOA.NOME FROM PESSOA INNER JOIN CP_PESSOA ON CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA WHERE CP_PESSOA.MATRICULA = '" + matriculaDesignado + "'")
    for linha in fiscal.Rows:
        nomeFiscal = linha["NOME"]


emailGestor = ''  
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.ID_PESSOA ='" + idGerente + "'")
#Adiciona o e-mail ao dicionário
for linha2 in lista.Rows:
    emailGestor = linha2["EMAIL"].ToString()

if emailGestor:
    Mensagem.Destinatarios.Add(emailGestor)
    
Mensagem.Assunto = "Designação aprovada pelo Fiscal - Acompanhamento"

Mensagem.Corpo = '<html><head><style>body{margin:0;padding:40px;font-family:Arial,sans-serif;color:#0033a0;background-color:#f5f5f5;} .container{background-color:#ffffff;border-radius:10px;padding:30px;box-shadow:0 4px 8px rgba(0,0,0,0.1);} h1,h2{color:#0033a0;} a{color:#fff;text-decoration:none;font-weight:bold;} a:hover{text-decoration:none;} p{margin-bottom:15px;line-height:1.6;} .button{display:inline-block;padding:12px 20px;font-size:16px;border-radius:5px;background-color:#0033a0;color:#ffffff;text-align:center;transition:background-color 0.3s ease;} .button:hover{background-color:#002080;} ul{margin-top:10px;margin-bottom:20px;padding-left:20px;} li{margin-bottom:8px;}</style></head><body><div class="container"><h1>Designação de Fiscal Contratual</h1><p>Prezado(a) <strong>' + nomeFiscal + '</strong> (<strong>' + matriculaDesignado + '</strong>),</p><p>Informamos que você foi designado(a) como <strong>' + tipoFormatado + '</strong> para atuar na fiscalização do contrato relacionado ao <strong>DGCO:</strong> ' + dgco + ', conforme dispõe o <strong>PRO412-017 - Designação dos Intervenientes Envolvidos na Fiscalização Contratual</strong>.</p><p>Para mais detalhes ou acompanhamento da Ordem de Serviço (OS), clique no botão abaixo:</p><p><a href="' + str(linkChamado) + '" class="button">Acessar OS</a></p><h2>Atribuições do Fiscal</h2><ul><li>Acompanhar e fiscalizar a execução do contrato, garantindo que todos os serviços sejam prestados conforme os termos acordados;</li><li>Verificar a conformidade dos serviços executados com as especificações técnicas e demais condições estabelecidas no contrato;</li><li>Registrar e reportar quaisquer irregularidades, falhas ou desvios identificados durante a execução dos serviços;</li><li>Elaborar relatórios periódicos de acompanhamento da execução do contrato;</li><li>Propor medidas corretivas e preventivas para assegurar o cumprimento integral do contrato;</li><li>Atuar em conformidade com as normas e diretrizes estabelecidas pela BB TECNOLOGIA E SERVIÇOS e pela legislação vigente.</li></ul><p>Atenciosamente,</p><p><strong>Divisão de Contratos com Fornecedores</strong></p></div></body></html>'
```

### [342505] Tarefa "Aprovar Termo de Designação"
Responsável: Fila CSC - Contratos (papel 688)
Config: Codigo=FISCALADM
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioHabilitado("FAVORECIDO_ALL", False)
OrdemServico.ModificaCampoFormularioHabilitado("FAVORECIDO_ALL", False)
OrdemServico.ModificaCampoFormularioHabilitado("TIPO_DESIGNACAO_INTERV", False)
OrdemServico.ModificaCampoFormularioHabilitado("DESIGNA_TITU_OR_SUP", False)
OrdemServico.ModificaCampoFormularioHabilitado("DGCO_BB", False)
OrdemServico.ModificaCampoFormularioHabilitado("NOME_FORNECEDOR", False)
OrdemServico.ModificaCampoFormularioHabilitado("OBJETO_CONTRATO", False)
OrdemServico.ModificaCampoFormularioHabilitado("CSC_MATRICULA", False)
OrdemServico.ModificaCampoFormularioHabilitado("TE_MATRICULA", False)
OrdemServico.ModificaCampoFormularioHabilitado("TE_NOME_EMPREGADO", False)
OrdemServico.ModificaCampoFormularioHabilitado("ID_DESIGNACAO", False)
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario['FAVORECIDO_NOME'].Habilitado = False


clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

import clr
import re
from System import Convert
from Newtonsoft.Json.Linq import JValue, JArray
from Newtonsoft.Json import JsonConvert
from System.Net.Http import HttpClient
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System import TimeSpan
from System.Collections.Generic import List


dgco = str(OrdemServico.GetCustom("DGCO_BB"))
token = '***MASCARADO***'
token2 = '***MASCARADO***'


# URL da API
url = ''
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)
if dom == 'HOMOLOGAÇÃO' or dom == 'DESENVOLVIMENTO':    
    url= 'https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=' + dgco

if dom == 'PRODUÇÃO':    
    url= 'https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco?dgco=' + dgco
    
    
    


# Inicializa o HttpClient e configura os cabeçalhos
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Clear()
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

# Envia a requisição GET
response = client.GetAsync(url)
response.Wait()

try:
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
            
                
            # Tenta deserializar o JSON como um array
            jsonArray = JArray.Parse(result)
            for i, item in enumerate(jsonArray):

                Formulario['FAVORECIDO_NOME'].Valor = str(item['gestor_titular'])
                
                if item['matricula_gestor_titular']:
                    matriculaGestor = str(item['matricula_gestor_titular'])
                    idGestor = 0
                    
                    lista = Utils.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + matriculaGestor + "'")
                    for linha2 in lista.Rows:
                        idGestor = linha2["ID_PESSOA"]

                    OrdemServico.Favorecido = Pessoa.Carrega(Convert.ToInt32(idGestor))
                    OrdemServico.Cliente = Pessoa.Carrega(Convert.ToInt32(idGestor))
                    
                else:
                    matriculaDesignado = str(Formulario['CSC_MATRICULA'].Valor)
                    idDesignado = 0
                    
                    lista2 = Utils.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + matriculaDesignado + "'")
                    for linha23 in lista2.Rows:
                        idDesignado = linha23["ID_PESSOA"]

                    OrdemServico.Favorecido = Pessoa.Carrega(Convert.ToInt32(idDesignado))
                    OrdemServico.Cliente = Pessoa.Carrega(Convert.ToInt32(idDesignado))
                    
                

        except Exception as e:
            # Adiciona um comentário com o erro de extração
            pass
            
    else:
        # Em caso de erro, adiciona o comentário com o código de erro
        pass
        
except Exception as e:
    # Adiciona um comentário com o erro genérico
    pass
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Designação; MinimoAprovadores=1; ReutilizaAprovacaoAnterior=true; ReenvioEmailAprovacao=48; RotuloBotaoAprovar=Declaro que estou ciente da designação e das responsabilidades a mim atribuídas.; RotuloBotaoReprovar=Declaro que estou ciente, porém desejo adicionar observações a respeito.; ObrigatoriedadeMotivo=Todas
  - (aprovação) FAVORECIDO_COBRA "Gerente do Cesec (Responsável por Aprovar o Termo de Designação)" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] — PermiteModificarAprovado=true
  - (aprovação) TIPO_DESIGNACAO_INTERV "Tipo Designação" [TextBox String(1500) → CPE_CONTRATOS02.TIPO_DESIGNACAO_INTERV]
  - (aprovação) DESIGNA_TITU_OR_SUP "Designação Titular ou Suplente?" [TextBox String(1500) → CPE_CONTRATOS02.DESIGNA_TITU_OR_SUP] — PermiteModificarAprovado=true
  - (aprovação) FAVORECIDO_ALL "Nome Colaborador Designado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_ALL]
  - (aprovação) COMBOBOX2 "Titular ou Suplente?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - (aprovação) OBJETO_CONTRATO "Objeto" [Memo String(1999) → CPE_CSC.OBJETO_CONTRATO]
  - (aprovação) FAVORECIDO_NOME "Gestor Contratante:" [TextBox String → CP_ORDEM_SERVICO.FAVORECIDO_NOME]
  - (aprovação) NOME_FORNECEDOR "Nome do Fornecedor/Favorecido" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] — PermiteModificarAprovado=true
  - (aprovação) FISCAL_ADMINISTRATIVO "Fiscal Administrativo" [DataGrid RecordList → Z_00143_FISCAL_ADMINISTRATIVO.FISCAL_ADMINISTRATIVO] — PermiteModificarAprovado=true
  - (aprovação) NOME_MAE "Matrícula Colaborador Transferido" [TextBox String → CP_ORDEM_SERVICO.NOME_MAE]
  - (aprovação) FAVORECIDO_MONITOR "Nome Colaborador Transferido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_MONITOR]
  - (aprovação) MODELO_TIPO "Tipo de Designação" [TextBox String → CPE_HOMOLOGACAO.MODELO_TIPO]
  - (aprovação) CSC_MATRICULA "Matricula Colaborador Designado" [TextBox String → CPE_CSC.CSC_MATRICULA]
  - (aprovação) LABEL5 "Comunicado:" [Label String(1024) → CPE_ORDEM_SERVICO.LABEL5]
  - (aprovação) ACEITE_DESIGNA_SISCCON2 "Declaro que estou ciente da designação e das responsabilidades a mim atribuídas." [CheckBox Boolean → CPE_CONTRATOS02.ACEITE_DESIGNA_SISCCON2] — Obrigatoriedade=Aprovacao
  - aprovador: Favorecido All (Unico)
- Operação PR0001 Preencher Campos
  - FAVORECIDO_NOME "Gestor Contratante" [TextBox String → CP_ORDEM_SERVICO.FAVORECIDO_NOME]
  - LABEL5 "O Gestor Contratante indicou os intervenientes deste contrato, que consta disponibilizado no sistema Sisccon, conforme NI412, PRO412-015 e  PRO412-017." [Label String(1024) → CPE_ORDEM_SERVICO.LABEL5]

### [342506] LinkInicial "Abertura Manual Designação"
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioHabilitado("DESIGNA_TITU_OR_SUP", False)
OrdemServico.ModificaCampoFormularioHabilitado("TIPO_DESIGNACAO_INTERV", False)
OrdemServico.ModificaCampoFormularioHabilitado("ID_DESIGNACAO", False)
```
- Operação PR0001 Preencher Campos
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório — Configuracao={"Mascara":"00000/0000"}
**DGCO_BB.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Servico
#Formulario.ExibeMensagem(OrdemServico.Cliente['MATRICULA'].ToString())
#sql="SELECT gf.nome_razao_social FROM bbts_gescon_fornecedor GF INNER JOIN BBTS_GESCON_CONTRATO GC ON gc.id_fornecedor = GF.ID WHERE replace(replace(replace(gc.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
#
#Formulario.ExibeMensagem(DB.ExecuteNonQuery("call xxbbtsgate.pr_insere_fornecedor_sv('teste leonam', '10405322763','PESSOA_FISICA132')").ToString() + " Result")
#lista = DB.ExecuteDataTable(sql)
#if lista.Rows.Count == 0:
#    Formulario.ExibeMensagem("Este DGCO não está cadastrado no Gescon.")
#    Formulario["NOME_FORNECEDOR"].Habilitado = True
#    Formulario["NOME_FORNECEDOR"].Valor = None
#else:
#    for linha in lista.Rows:
#        Formulario["NOME_FORNECEDOR"].Valor = linha["NOME_RAZAO_SOCIAL"]
#        Formulario["NOME_FORNECEDOR"].Habilitado = False
#        
##Fiscal Administrativo
#if (OrdemServico.Servico.Sigla == "FISCALADM"):
#    sql_adm="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_ADMINISTRATIVA'"
#    fiscais = DB.ExecuteDataTable(sql_adm)
#    if fiscais.Rows.Count != 0 :
#        for fiscal in fiscais.Rows:
#            OrdemServico.AdicionaLinhaRegistro('FISCAL_ADMINISTRATIVO', ['FISCAL_ADM','MATRICULA_FISCAL','FISCAL_ADM_SUPLENTE','MATRICULA_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
#            if not fiscal['MATRICULA_TITULAR']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#            if not fiscal['MATRICULA_SUPLENTE']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#
##Fiscal Servico e Fiscal Master
#sql_fs="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_SERVICO'"
#
#if (OrdemServico.Servico.Sigla == "FISCALSERVICO"): 
#    fiscais = DB.ExecuteDataTable(sql_fs)
#    if fiscais.Rows.Count != 0 :
#        for fiscal in fiscais.Rows:
#            OrdemServico.AdicionaLinhaRegistro('FISCAL_SER', ['FISCAL_SERVICO','MATRICULA_FISCAL_SERVICO','FISCAL_SUPLENTE','MATRICULA_FISCAL_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
#            if not fiscal['MATRICULA_TITULAR']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#            if not fiscal['MATRICULA_SUPLENTE']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#
#if (OrdemServico.Servico.Sigla == "FISCALMASTER"):
#    fiscais = DB.ExecuteDataTable(sql_fs)        
#    if fiscais.Rows.Count != 0 :
#        for fiscal in fiscais.Rows:
#            OrdemServico.AdicionaLinhaRegistro('FISCAL_SER', ['FISCAL_SERVICO','MATRICULA_FISCAL_SERVICO','FISCAL_SUPLENTE','MATRICULA_FISCAL_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
#            if not fiscal['MATRICULA_TITULAR']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#            if not fiscal['MATRICULA_SUPLENTE']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#            
##Gestor do contrato
#if (OrdemServico.Servico.Sigla == "FISCALSERVICO" or OrdemServico.Servico.Sigla == "FISCALMASTER"):
#    sql_ges="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'GESTAO_CONTRATO'"
#    fiscais = DB.ExecuteDataTable(sql_ges)
#    if fiscais.Rows.Count != 0 :
#        for fiscal in fiscais.Rows:
#            OrdemServico.AdicionaLinhaRegistro('GESTOR_CONTRATO', ['GESTOR_CONTRATO','MATRICULA_GESTOR','GESTOR_CONTRATO_SUPLENTE','MATRICULA_GESTOR_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
#            if not fiscal['MATRICULA_TITULAR']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#            if not fiscal['MATRICULA_SUPLENTE']:
#                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
#
##Gerente executivo do contrato
#
#sql_exec = "select cpp3.id_pessoa as ID_EXEC,f3.nome as NOME_EXEC,f3.matricula AS MATRICULA_EXEC from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO inner join bbts_gescon_funcionario f3 on f3.id = c.ID_GER_EXEC_CON inner join cp_pessoa cpp3 on TO_CHAR(cpp3.matricula) = TO_CHAR(f3.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
#ger_exec = DB.ExecuteDataTable(sql_exec)
#if ger_exec.Rows.Count != 0 :
#    for linha_exec in ger_exec.Rows:
#        Formulario['PPGEREX_NEGOCIO'].Valor = linha_exec['ID_EXEC'].ToString()
#        OrdemServico.AdicionaLinhaRegistro('GESTOR_CONTRATO', ['GESTOR_CONTRATO','MATRICULA_GESTOR','GESTOR_CONTRATO_SUPLENTE','MATRICULA_GESTOR_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
```
  - OBJETO_CONTRATO "Objeto" [Memo String(1999) → CPE_CSC.OBJETO_CONTRATO] obrigatório
  - NOME_FORNECEDOR "Razão Social" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - CSC_MATRICULA "Matricula Colaborador Designado" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - TIPO_DESIGNACAO_INTERV "Tipo Designação" [TextBox String(1500) → CPE_CONTRATOS02.TIPO_DESIGNACAO_INTERV] obrigatório
  - DESIGNA_TITU_OR_SUP "Designação Titular ou Suplente?" [TextBox String(1500) → CPE_CONTRATOS02.DESIGNA_TITU_OR_SUP] obrigatório
  - FAVORECIDO_ALL "Nome Colaborador Designado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_ALL] obrigatório
**FAVORECIDO_ALL.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_ALL"].Valor != "" or Formulario["FAVORECIDO_ALL"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_ALL"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()
       


    Formulario["CSC_MATRICULA"].Valor = matricula.ToString()
```
  - ID_DESIGNACAO "ID Designação" [TextBox String(1500) → CPE_CONTRATOS02.ID_DESIGNACAO] obrigatório
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
- Associação de subprocesso: AssociacaoId=1209; FraseAssociacao=Designação dos Intervenientes (Manual) -> Termo de Aceite; Nome=MANUALDESIGNACAO
- Associação de subprocesso: AssociacaoId=1210; FraseAssociacao=Designação de Intervenientes Administrativo -> Termo de Aceite Designção; Nome=TERMOADMSISCCONACEITE
- Associação de subprocesso: AssociacaoId=1211; FraseAssociacao=Designação Movimentação Fiscal Administrativo -> Termo Aceite Designação; Nome=TERMODEDESIGNACAOMOVADM

### [342504] LinkInicial "Movimentação"
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioHabilitado("DGCO_BB", False)
OrdemServico.ModificaCampoFormularioHabilitado("FAVORECIDO_COBRA", False)
OrdemServico.ModificaCampoFormularioHabilitado("FAVORECIDO_MONITOR", False)
OrdemServico.ModificaCampoFormularioHabilitado("FAVORECIDO_ALL", False)
OrdemServico.ModificaCampoFormularioHabilitado("NOME_FORNECEDOR", False)
OrdemServico.ModificaCampoFormularioHabilitado("NOME_MAE", False)
OrdemServico.ModificaCampoFormularioHabilitado("OBJETO_CONTRATO", False)
OrdemServico.ModificaCampoFormularioHabilitado("CSC_MATRICULA", False)
OrdemServico.ModificaCampoFormularioHabilitado("DESIGNA_TITU_OR_SUP", False)
OrdemServico.ModificaCampoFormularioHabilitado("TIPO_DESIGNACAO_INTERV", False)
OrdemServico.ModificaCampoFormularioHabilitado("ID_DESIGNACAO", False)
```
- Operação PR0001 Preencher Campos
  - TE_MATRICULA "Matrícula do Colaborador Transferido" [TextBox String → CPE_CSC.TE_MATRICULA]
  - GRID_DESIGNACAO "Designações" [DataGrid RecordList → Z_00143_GRID_DESIGNACAO.GRID_DESIGNACAO] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna ANALISTA_CONTRAT_TITU
**GRID_DESIGNACAO.ANALISTA_CONTRAT_TITU.ScriptModificado**
```python
if (str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) == str(FormularioRegistro['GESTOR_CONTRAT_SUP'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) == str(FormularioRegistro['FISCAL_SERV_TITU'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) == str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) == str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) ==str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) == str(FormularioRegistro['FISCAL_SERV_SUP'].Valor)):
    OrdemServico.AdicionaComentario("O interveniente informado já se encontra designado no mesmo contratio!", True)
```
    - coluna MATRICULA_FMASTER_TITU
    - coluna MATRICULA_FSERV_SUP obrigatório
    - coluna MATRICULA_FSERV_TITU obrigatório
    - coluna DGCO
    - coluna TITULAR_OU_SUPLENTE
    - coluna FISCAL_MASTER_SUP
**GRID_DESIGNACAO.FISCAL_MASTER_SUP.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro["FISCAL_MASTER_SUP"].Valor != "" or FormularioRegistro["FISCAL_MASTER_SUP"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(FormularioRegistro["FISCAL_MASTER_SUP"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    matricula = ''
    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()
       


    matriculaGestor = FormularioRegistro["MATRICULA_GESTOR_SUP"].Valor
    matriculaFServTitu = FormularioRegistro["MATRICULA_FSERV_TITU"].Valor
    matriculaFServSup = FormularioRegistro["MATRICULA_FSERV_SUP"].Valor
    matriculaFMasterTitu = FormularioRegistro["MATRICULA_FMASTER_TITU"].Valor

        
    if matricula in [matriculaGestor, matriculaFMasterTitu, matriculaFServTitu, matriculaFServSup]:
        FormularioRegistro["FISCAL_MASTER_SUP"].Valor = 'O nome já se encontra designado em outro papel no mesmo DGCO!'
        FormularioRegistro["MATRICULA_FMASTER_SUP"].Valor = 0 #Necessário para validacão
    else:
        FormularioRegistro["MATRICULA_FMASTER_SUP"].Valor = matricula.ToString()
        
    if FormularioRegistro["FISCAL_MASTER_SUP"].Valor == None or FormularioRegistro["FISCAL_MASTER_SUP"].Valor == '':
        FormularioRegistro["MATRICULA_FMASTER_SUP"].Valor = None
```
    - coluna TIPO
    - coluna FISCAL_SERV_SUP obrigatório
**GRID_DESIGNACAO.FISCAL_SERV_SUP.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro["FISCAL_SERV_SUP"].Valor != "" or FormularioRegistro["FISCAL_SERV_SUP"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(FormularioRegistro["FISCAL_SERV_SUP"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    matricula = ''
    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()
       


    matriculaGestor = FormularioRegistro["MATRICULA_GESTOR_SUP"].Valor
    matriculaFMasterTitu = FormularioRegistro["MATRICULA_FMASTER_TITU"].Valor
    matriculaFMasterSup = FormularioRegistro["MATRICULA_FMASTER_SUP"].Valor
    matriculaFServTitu = FormularioRegistro["MATRICULA_FSERV_TITU"].Valor
    
    if matricula in [matriculaGestor, matriculaFMasterTitu, matriculaFMasterSup, matriculaFServTitu]:
        FormularioRegistro["FISCAL_SERV_SUP"].Valor = 'O nome já se encontra designado em outro papel no mesmo DGCO!'
        FormularioRegistro["MATRICULA_FSERV_SUP"].Valor = 0 #Necessário para validacão
    else:
        FormularioRegistro["MATRICULA_FSERV_SUP"].Valor = matricula.ToString()
```
    - coluna ANALISTA_CONTRAT_SUP
**GRID_DESIGNACAO.ANALISTA_CONTRAT_SUP.ScriptModificado**
```python
if (str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) == str(FormularioRegistro['GESTOR_CONTRAT_SUP'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) == str(FormularioRegistro['FISCAL_SERV_TITU'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) == str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) == str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) == str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) or str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) == str(FormularioRegistro['FISCAL_SERV_SUP'].Valor)):
    OrdemServico.AdicionaComentario("O interveniente informado já se encontra designado no mesmo contratio!", True)
```
    - coluna MATRICULA_GESTOR_SUP obrigatório
    - coluna FISCAL_ADM_SUP
**GRID_DESIGNACAO.FISCAL_ADM_SUP.ScriptModificado**
```python
if (str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) == str(FormularioRegistro['GESTOR_CONTRAT_SUP'].Valor) or str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) == str(FormularioRegistro['FISCAL_SERV_TITU'].Valor) or str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) == str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) or str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) == str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) or str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) == str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) or str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) == str(FormularioRegistro['FISCAL_SERV_SUP'].Valor)):
    OrdemServico.AdicionaComentario("O interveniente informado já se encontra designado no mesmo contratio!", True)
```
    - coluna FISCAL_ADM_TITU
**GRID_DESIGNACAO.FISCAL_ADM_TITU.ScriptModificado**
```python
if (str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) == str(FormularioRegistro['GESTOR_CONTRAT_SUP'].Valor) or str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) == str(FormularioRegistro['FISCAL_SERV_TITU'].Valor) or str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) == str(FormularioRegistro['FISCAL_ADM_SUP'].Valor) or str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) == str(FormularioRegistro['ANALISTA_CONTRAT_TITU'].Valor) or str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) == str(FormularioRegistro['ANALISTA_CONTRAT_SUP'].Valor) or str(FormularioRegistro['FISCAL_ADM_TITU'].Valor) == str(FormularioRegistro['FISCAL_SERV_SUP'].Valor)):
    OrdemServico.AdicionaComentario("O interveniente informado já se encontra designado no mesmo contratio!", True)
```
    - coluna MATRICULA_FMASTER_SUP
    - coluna FISCAL_MASTER_TITU
**GRID_DESIGNACAO.FISCAL_MASTER_TITU.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro["FISCAL_MASTER_TITU"].Valor != "" or FormularioRegistro["FISCAL_MASTER_TITU"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(FormularioRegistro["FISCAL_MASTER_TITU"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    matricula = ''
    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()
       
  
        
    matriculaGestor = FormularioRegistro["MATRICULA_GESTOR_SUP"].Valor
    matriculaFServTitu = FormularioRegistro["MATRICULA_FSERV_TITU"].Valor
    matriculaFServSup = FormularioRegistro["MATRICULA_FSERV_SUP"].Valor
    matriculaFMasterSup = FormularioRegistro["MATRICULA_FMASTER_SUP"].Valor

    if matricula in [matriculaGestor, matriculaFServTitu, matriculaFMasterSup, matriculaFServSup]:
        FormularioRegistro["FISCAL_MASTER_TITU"].Valor = 'O nome já se encontra designado em outro papel no mesmo DGCO!'
        FormularioRegistro["MATRICULA_FMASTER_TITU"].Valor = 0 #Necessário para validacão
    else:
        FormularioRegistro["MATRICULA_FMASTER_TITU"].Valor = matricula.ToString()
        
        
        
        
        
    if FormularioRegistro["FISCAL_MASTER_TITU"].Valor == None or FormularioRegistro["FISCAL_MASTER_TITU"].Valor == '':
        FormularioRegistro["MATRICULA_FMASTER_TITU"].Valor = None
```
    - coluna GESTOR_CONTRAT_SUP obrigatório
**GRID_DESIGNACAO.GESTOR_CONTRAT_SUP.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro["GESTOR_CONTRAT_SUP"].Valor != "" or FormularioRegistro["GESTOR_CONTRAT_SUP"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(FormularioRegistro["GESTOR_CONTRAT_SUP"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    matricula = ''
    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()
       


    matriculaFServTitu = FormularioRegistro["MATRICULA_FSERV_TITU"].Valor
    matriculaFMasterTitu = FormularioRegistro["MATRICULA_FMASTER_TITU"].Valor
    matriculaFMasterSup = FormularioRegistro["MATRICULA_FMASTER_SUP"].Valor
    matriculaFServSup = FormularioRegistro["MATRICULA_FSERV_SUP"].Valor

    # Verifique se a nova matrícula já existe em uma das posições de fiscais ou gestor
    if matricula in [matriculaFServTitu, matriculaFMasterTitu, matriculaFMasterSup, matriculaFServSup]:
        #Exibir uma mensagem de erro ou tomar a ação necessária
        #OrdemServico.AdicionaComentario("A matrícula escolhida já está atribuída a outro papel nesta linha.", True)
        FormularioRegistro["GESTOR_CONTRAT_SUP"].Valor = 'O nome já se encontra designado em outro papel no mesmo DGCO!'
        FormularioRegistro["MATRICULA_GESTOR_SUP"].Valor = 0
    else:
        #Atribua a matrícula ao campo correspondente
        FormularioRegistro["MATRICULA_GESTOR_SUP"].Valor = matricula.ToString()
```
    - coluna RAZAO_SOCIAL obrigatório
    - coluna ID_DESIGNACAO obrigatório
    - coluna OBJ obrigatório
    - coluna FISCAL_SERV_TITU obrigatório
**GRID_DESIGNACAO.FISCAL_SERV_TITU.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if FormularioRegistro["FISCAL_SERV_TITU"].Valor != "" or FormularioRegistro["FISCAL_SERV_TITU"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(FormularioRegistro["FISCAL_SERV_TITU"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    
    matricula = ''
    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()

    #Obtenha as matrículas existentes na linha atual
    matriculaGestor = FormularioRegistro["MATRICULA_GESTOR_SUP"].Valor
    matriculaFMasterTitu = FormularioRegistro["MATRICULA_FMASTER_TITU"].Valor
    matriculaFMasterSup = FormularioRegistro["MATRICULA_FMASTER_SUP"].Valor
    matriculaFServSup = FormularioRegistro["MATRICULA_FSERV_SUP"].Valor

    # Verifique se a nova matrícula já existe em uma das posições de fiscais ou gestor
    if matricula in [matriculaGestor, matriculaFMasterTitu, matriculaFMasterSup, matriculaFServSup]:
        #Exibir uma mensagem de erro ou tomar a ação necessária
        #OrdemServico.AdicionaComentario("A matrícula escolhida já está atribuída a outro papel nesta linha.", True)
        FormularioRegistro["FISCAL_SERV_TITU"].Valor = 'O nome já se encontra designado em outro papel no mesmo DGCO!'
        FormularioRegistro["MATRICULA_FSERV_TITU"].Valor = 0
    else:
        #Atribua a matrícula ao campo correspondente
        FormularioRegistro["MATRICULA_FSERV_TITU"].Valor = matricula.ToString()
```
  - CSC_MATRICULA "Matricula Colaborador Designado" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - FAVORECIDO_ALL "Nome Designado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_ALL] obrigatório
  - ID_DESIGNACAO "ID Designação" [TextBox String(1500) → CPE_CONTRATOS02.ID_DESIGNACAO] obrigatório
  - TIPO_DESIGNACAO_INTERV "Tipo Designação" [TextBox String(1500) → CPE_CONTRATOS02.TIPO_DESIGNACAO_INTERV]
  - DESIGNA_TITU_OR_SUP "Designação Titular ou Suplente?" [TextBox String(1500) → CPE_CONTRATOS02.DESIGNA_TITU_OR_SUP]
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório
  - TE_NOME_EMPREGADO "Nome Colaborador Transferido" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
- Associação de subprocesso: AssociacaoId=1212; FraseAssociacao=Designação de Interveniente Movimentado -> Termo de Aceite Designação; Nome=DESIGNAMOVIMENTACAOSISCCON

### [342507] LinkInicial "Comissão"
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioHabilitado("DESIGNA_TITU_OR_SUP", False)
OrdemServico.ModificaCampoFormularioHabilitado("TIPO_DESIGNACAO_INTERV", False)
OrdemServico.ModificaCampoFormularioHabilitado("ID_DESIGNACAO", False)
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_ALL "Nome Colaborador Designado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_ALL] obrigatório
**FAVORECIDO_ALL.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_ALL"].Valor != "" or Formulario["FAVORECIDO_ALL"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_ALL"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()
       


    Formulario["CSC_MATRICULA"].Valor = matricula.ToString()
```
  - CSC_MATRICULA "Matricula Colaborador Designado" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - TIPO_DESIGNACAO_INTERV "Tipo Designação" [TextBox String(1500) → CPE_CONTRATOS02.TIPO_DESIGNACAO_INTERV] obrigatório
  - DESIGNA_TITU_OR_SUP "Designação Titular ou Suplente?" [TextBox String(1500) → CPE_CONTRATOS02.DESIGNA_TITU_OR_SUP] obrigatório
  - ID_DESIGNACAO "ID Designação" [TextBox String(1500) → CPE_CONTRATOS02.ID_DESIGNACAO] obrigatório
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - OBJETO_CONTRATO "Objeto" [Memo String(1999) → CPE_CSC.OBJETO_CONTRATO] obrigatório
  - NOME_FORNECEDOR "Razão Social" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório — Configuracao={"Mascara":"00000/0000"}
**DGCO_BB.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Servico
#Formulario.ExibeMensagem(OrdemServico.Cliente['MATRICULA'].ToString())
sql="SELECT gf.nome_razao_social FROM bbts_gescon_fornecedor GF INNER JOIN BBTS_GESCON_CONTRATO GC ON gc.id_fornecedor = GF.ID WHERE replace(replace(replace(gc.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"

#Formulario.ExibeMensagem(DB.ExecuteNonQuery("call xxbbtsgate.pr_insere_fornecedor_sv('teste leonam', '10405322763','PESSOA_FISICA132')").ToString() + " Result")
lista = DB.ExecuteDataTable(sql)
if lista.Rows.Count == 0:
    Formulario.ExibeMensagem("Este DGCO não está cadastrado no Gescon.")
    Formulario["NOME_FORNECEDOR"].Habilitado = True
    Formulario["NOME_FORNECEDOR"].Valor = None
else:
    for linha in lista.Rows:
        Formulario["NOME_FORNECEDOR"].Valor = linha["NOME_RAZAO_SOCIAL"]
        Formulario["NOME_FORNECEDOR"].Habilitado = False
        
##Fiscal Administrativo
if (OrdemServico.Servico.Sigla == "FISCALADM"):
    sql_adm="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_ADMINISTRATIVA'"
    fiscais = DB.ExecuteDataTable(sql_adm)
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('FISCAL_ADMINISTRATIVO', ['FISCAL_ADM','MATRICULA_FISCAL','FISCAL_ADM_SUPLENTE','MATRICULA_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')

##Fiscal Servico e Fiscal Master
sql_fs="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_SERVICO'"

if (OrdemServico.Servico.Sigla == "FISCALSERVICO"): 
    fiscais = DB.ExecuteDataTable(sql_fs)
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('FISCAL_SER', ['FISCAL_SERVICO','MATRICULA_FISCAL_SERVICO','FISCAL_SUPLENTE','MATRICULA_FISCAL_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')

if (OrdemServico.Servico.Sigla == "FISCALMASTER"):
    fiscais = DB.ExecuteDataTable(sql_fs)        
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('FISCAL_SER', ['FISCAL_SERVICO','MATRICULA_FISCAL_SERVICO','FISCAL_SUPLENTE','MATRICULA_FISCAL_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            
##Gestor do contrato
if (OrdemServico.Servico.Sigla == "FISCALSERVICO" or OrdemServico.Servico.Sigla == "FISCALMASTER"):
    sql_ges="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'GESTAO_CONTRATO'"
    fiscais = DB.ExecuteDataTable(sql_ges)
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('GESTOR_CONTRATO', ['GESTOR_CONTRATO','MATRICULA_GESTOR','GESTOR_CONTRATO_SUPLENTE','MATRICULA_GESTOR_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')

##Gerente executivo do contrato

sql_exec = "select cpp3.id_pessoa as ID_EXEC,f3.nome as NOME_EXEC,f3.matricula AS MATRICULA_EXEC from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO inner join bbts_gescon_funcionario f3 on f3.id = c.ID_GER_EXEC_CON inner join cp_pessoa cpp3 on TO_CHAR(cpp3.matricula) = TO_CHAR(f3.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
ger_exec = DB.ExecuteDataTable(sql_exec)
if ger_exec.Rows.Count != 0 :
    for linha_exec in ger_exec.Rows:
        Formulario['PPGEREX_NEGOCIO'].Valor = linha_exec['ID_EXEC'].ToString()
        #OrdemServico.AdicionaLinhaRegistro('GESTOR_CONTRATO', ['GESTOR_CONTRATO','MATRICULA_GESTOR','GESTOR_CONTRATO_SUPLENTE','MATRICULA_GESTOR_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
```
- Associação de subprocesso: AssociacaoId=1213; FraseAssociacao=Designação de Interveniente Movimentado (Comissão) -> Termo de Aceite Designação; Nome=TERMOCOMISSAOMOVIMENTADOSISCCON

### [342508] LinkInicial "OnBoard"
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioHabilitado("DESIGNA_TITU_OR_SUP", False)
OrdemServico.ModificaCampoFormularioHabilitado("TIPO_DESIGNACAO_INTERV", False)
OrdemServico.ModificaCampoFormularioHabilitado("ID_DESIGNACAO", False)
```
- Operação PR0001 Preencher Campos
  - TIPO_DESIGNACAO_INTERV "Tipo Designação" [TextBox String(1500) → CPE_CONTRATOS02.TIPO_DESIGNACAO_INTERV] obrigatório
  - DESIGNA_TITU_OR_SUP "Designação Titular ou Suplente?" [TextBox String(1500) → CPE_CONTRATOS02.DESIGNA_TITU_OR_SUP] obrigatório
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório — Configuracao={"Mascara":"00000/0000"}
**DGCO_BB.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Servico
#Formulario.ExibeMensagem(OrdemServico.Cliente['MATRICULA'].ToString())
sql="SELECT gf.nome_razao_social FROM bbts_gescon_fornecedor GF INNER JOIN BBTS_GESCON_CONTRATO GC ON gc.id_fornecedor = GF.ID WHERE replace(replace(replace(gc.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"

#Formulario.ExibeMensagem(DB.ExecuteNonQuery("call xxbbtsgate.pr_insere_fornecedor_sv('teste leonam', '10405322763','PESSOA_FISICA132')").ToString() + " Result")
lista = DB.ExecuteDataTable(sql)
if lista.Rows.Count == 0:
    Formulario.ExibeMensagem("Este DGCO não está cadastrado no Gescon.")
    Formulario["NOME_FORNECEDOR"].Habilitado = True
    Formulario["NOME_FORNECEDOR"].Valor = None
else:
    for linha in lista.Rows:
        Formulario["NOME_FORNECEDOR"].Valor = linha["NOME_RAZAO_SOCIAL"]
        Formulario["NOME_FORNECEDOR"].Habilitado = False
        
##Fiscal Administrativo
if (OrdemServico.Servico.Sigla == "FISCALADM"):
    sql_adm="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_ADMINISTRATIVA'"
    fiscais = DB.ExecuteDataTable(sql_adm)
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('FISCAL_ADMINISTRATIVO', ['FISCAL_ADM','MATRICULA_FISCAL','FISCAL_ADM_SUPLENTE','MATRICULA_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')

##Fiscal Servico e Fiscal Master
sql_fs="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_SERVICO'"

if (OrdemServico.Servico.Sigla == "FISCALSERVICO"): 
    fiscais = DB.ExecuteDataTable(sql_fs)
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('FISCAL_SER', ['FISCAL_SERVICO','MATRICULA_FISCAL_SERVICO','FISCAL_SUPLENTE','MATRICULA_FISCAL_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')

if (OrdemServico.Servico.Sigla == "FISCALMASTER"):
    fiscais = DB.ExecuteDataTable(sql_fs)        
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('FISCAL_SER', ['FISCAL_SERVICO','MATRICULA_FISCAL_SERVICO','FISCAL_SUPLENTE','MATRICULA_FISCAL_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            
##Gestor do contrato
if (OrdemServico.Servico.Sigla == "FISCALSERVICO" or OrdemServico.Servico.Sigla == "FISCALMASTER"):
    sql_ges="select cpp.id_pessoa as ID_TITULAR,f.nome as NOME_TITULAR,f.matricula AS MATRICULA_TITULAR,cpp2.id_pessoa as ID_SUPELNTE,f2.nome as NOME_SUPLENTE,f2.matricula AS MATRICULA_SUPLENTE from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular LEFT OUTER join bbts_gescon_funcionario f2 on f2.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on TO_CHAR(cpp.matricula) = TO_CHAR(f.matricula) LEFT OUTER join cp_pessoa cpp2 on TO_CHAR(cpp2.matricula) = TO_CHAR(f2.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'GESTAO_CONTRATO'"
    fiscais = DB.ExecuteDataTable(sql_ges)
    if fiscais.Rows.Count != 0 :
        for fiscal in fiscais.Rows:
            OrdemServico.AdicionaLinhaRegistro('GESTOR_CONTRATO', ['GESTOR_CONTRATO','MATRICULA_GESTOR','GESTOR_CONTRATO_SUPLENTE','MATRICULA_GESTOR_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
            if not fiscal['MATRICULA_TITULAR']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_TITULAR']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')
            if not fiscal['MATRICULA_SUPLENTE']:
                Formulario.ExibeMensagem('O cadastro no Gescon do funcionário '+fiscal['NOME_SUPLENTE']+' está faltando a matrícula, favor atualizar o cadastro antes de abrir o chamado.')

##Gerente executivo do contrato

sql_exec = "select cpp3.id_pessoa as ID_EXEC,f3.nome as NOME_EXEC,f3.matricula AS MATRICULA_EXEC from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO inner join bbts_gescon_funcionario f3 on f3.id = c.ID_GER_EXEC_CON inner join cp_pessoa cpp3 on TO_CHAR(cpp3.matricula) = TO_CHAR(f3.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','')"
ger_exec = DB.ExecuteDataTable(sql_exec)
if ger_exec.Rows.Count != 0 :
    for linha_exec in ger_exec.Rows:
        Formulario['PPGEREX_NEGOCIO'].Valor = linha_exec['ID_EXEC'].ToString()
        #OrdemServico.AdicionaLinhaRegistro('GESTOR_CONTRATO', ['GESTOR_CONTRATO','MATRICULA_GESTOR','GESTOR_CONTRATO_SUPLENTE','MATRICULA_GESTOR_SUPLENTE'], [fiscal['ID_TITULAR'],fiscal['MATRICULA_TITULAR'],fiscal['ID_SUPELNTE'],fiscal['MATRICULA_SUPLENTE']])
```
  - OBJETO_CONTRATO "Objeto" [Memo String(1999) → CPE_CSC.OBJETO_CONTRATO] obrigatório
  - FAVORECIDO_ALL "Nome Colaborador Designado" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_ALL] obrigatório
**FAVORECIDO_ALL.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_ALL"].Valor != "" or Formulario["FAVORECIDO_ALL"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_ALL"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()
       


    Formulario["CSC_MATRICULA"].Valor = matricula.ToString()
```
  - NOME_FORNECEDOR "Razão Social" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - CSC_MATRICULA "Matricula Colaborador Designado" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - ID_DESIGNACAO "ID Designação" [TextBox String(1500) → CPE_CONTRATOS02.ID_DESIGNACAO] obrigatório
- Associação de subprocesso: AssociacaoId=1208; FraseAssociacao=Designação (Onboard) -> Termo Designação; Nome=TERMOONBOARDDESIGNA

### [342509] Tarefa "Atualizar Sisccon"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

import clr
import re
from System import Convert
from Newtonsoft.Json.Linq import JValue, JArray
from Newtonsoft.Json import JsonConvert
from System.Net.Http import HttpClient
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System import TimeSpan

# Garimpar variáveis preenchidas na abertura;
titular_ou_suplente = str(OrdemServico.GetCustom('DESIGNA_TITU_OR_SUP')) # Titular ou Suplente
tipo_designacao = str(OrdemServico.GetCustom('TIPO_DESIGNACAO_INTERV')) # Tipo Designação


matricula_transferido = '0'
if str(OrdemServico.GetCustom('TE_MATRICULA')) != '' and str(OrdemServico.GetCustom('TE_MATRICULA')) != None:
    matricula_transferido = str(OrdemServico.GetCustom('TE_MATRICULA'))
else:
    matricula_transferido = '0'

    

        
    
    

#matricula_transferido = str(OrdemServico.GetCustom('TE_MATRICULA')) # Matricula Transferido OK


matricula_designado = str(OrdemServico.GetCustom('CSC_MATRICULA')) # Matricula Designado OK

dgco_contrato = str(OrdemServico.GetCustom('DGCO_BB')) # DGCO Contrato

# Realizar a requisição HTTP;
# Token de autenticação
token = '***MASCARADO***'
token2 = '***MASCARADO***'

#URL DA API
sql="select name from sv_domain where enabled = 'Sim'"
url = ''
dom = DB.ExecuteScalar(sql)





if dom == 'HOMOLOGAÇÃO' or dom == 'DESENVOLVIMENTO':   
    url = ('https://sisccon.bbts.com.br/supravizio/supra/atualizar-designacao?dgco=' + dgco_contrato +
       '&matriculaTransferido=' + matricula_transferido + '&matriculaDesignado=' + matricula_designado +
       '&tipoDesignacao=' + tipo_designacao + '&titularSuplente=' + titular_ou_suplente + '&numeroOs=' + str(OrdemServico.Numero))

if dom == 'PRODUÇÃO':    
    url = ('https://sisccon.bbts.com.br/supravizio/supra/atualizar-designacao?dgco=' + dgco_contrato +
       '&matriculaTransferido=' + matricula_transferido + '&matriculaDesignado=' + matricula_designado +
       '&tipoDesignacao=' + tipo_designacao + '&titularSuplente=' + titular_ou_suplente + '&numeroOs=' + str(OrdemServico.Numero))
    
    

#OrdemServico.AdicionaComentario(url.ToString(), True)#####


# Inicializa o HttpClient e configura os cabeçalhos
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Clear()
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

# Envia a requisição GET
response = client.GetAsync(url)
response.Wait()

try:
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
                #OrdemServico.AdicionaComentario(result.ToString(), True)
                
            if result.ToString() == '"deu boa"':
                #OrdemServico.AdicionaComentario(result.ToString(), True)
                OrdemServico.Salva()
                AvancaProximaAtividade = True

        except Exception as e:
            # Adiciona um comentário com o erro de extração
            #OrdemServico.AdicionaComentario("Erro de extração: {0}".format(str(e)), True)
            pass
    else:
        # Em caso de erro, adiciona o comentário com o código de erro
        #OrdemServico.AdicionaComentario("Erro: {0}".format(response.Result.StatusCode), True)
        #OrdemServico.AdicionaComentario("{0}".format(url), True)
        pass
except Exception as e:
    # Adiciona um comentário com o erro genérico
    #OrdemServico.AdicionaComentario("Erro de execução: {0}".format(str(e)), True)
    pass

# Constatar sucesso ou erro.
AvancaProximaAtividade = True
```

### [342510] EventoIntermediarioTimer ""
Config: TempoIntervalo=1440

### [342511] EventoIntermediarioTimer ""
Config: TempoIntervalo=4; MaximoExecucao=1

## Papéis usados
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 1119: Favorecido All
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_ALL"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_ALL")))

    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos

## Campos customizados usados (definição global)

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### DGCO_BB — DGCO
TextBox String(300) → CPE_FINANCEIRO.DGCO_BB

### TIPO_DESIGNACAO_INTERV — Tipo Designação
TextBox String(1500) → CPE_CONTRATOS02.TIPO_DESIGNACAO_INTERV

### DESIGNA_TITU_OR_SUP — Designação Titular ou Suplente?
TextBox String(1500) → CPE_CONTRATOS02.DESIGNA_TITU_OR_SUP

### FAVORECIDO_ALL — Colaborador
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_ALL
Descrição: Para pesquisa rápida faça:
1 - Clique na seta à direita do campo para abrir a relação de nomes;
2 - Com a lista ABERTA, pressione as teclas Ctrl + F (no IE aparece uma caixa de texto na parte superior esquerda e no Chrome na parte superior direita);
3 -  Digite o nome (ou parte dele) a ser pesquisado (serão marcados todas ocorrências que correspondam ao texto digitado);
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")

#Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE f.status_matricula = 'Ativo' AND p.ativo = 'Sim' order by nomemat")

#sqlValor = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat, f.status_matricula, p.ATIVO FROM CAD_FUNCIONARIO_V F, PESSOA P WHERE F.NOME = P.NOME AND f.status_matricula = 'Ativo' AND p.ativo = 'Sim' AND P.ID_PESSOA = "+ValorCorrente

#sqlEntrada = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat, f.status_matricula, p.ATIVO FROM CAD_FUNCIONARIO_V F, PESSOA P WHERE F.NOME = P.NOME AND f.status_matricula = 'Ativo' AND p.ativo = 'Sim' AND UPPER(P.NOME) like UPPER('%"+EntradaUsuario+"%')"


#sqlOrder = " order by nomemat asc"
# 
#if not String.IsNullOrEmpty(ValorCorrente) and not String.IsNullOrEmpty(EntradaUsuario):
#
#   Itens = DB.ExecuteDataTable("(" + sqlValor + ") UNION (" + sqlEntrada + " ) " + sqlOrder)
# 
#elif String.IsNullOrEmpty(EntradaUsuario) and String.IsNullOrEmpty(ValorCorrente):
# 
#   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
#   #None
# 
#elif String.IsNullOrEmpty(EntradaUsuario):
#   
 #  Itens = DB.ExecuteDataTable( sqlValor + sqlOrder)
# 
#else:
#   
#   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
```

### COMBOBOX2 — COMBOBOX2
DropDownList String → CPE_BOOTCAMP.COMBOBOX2

### OBJETO_CONTRATO — Objeto do contrato
Memo String(1999) → CPE_CSC.OBJETO_CONTRATO

### FAVORECIDO_NOME — Nome do favorecido
TextBox String → CP_ORDEM_SERVICO.FAVORECIDO_NOME

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### FISCAL_ADMINISTRATIVO — Fiscal Administrativo
DataGrid RecordList → Z_00143_FISCAL_ADMINISTRATIVO.FISCAL_ADMINISTRATIVO
Colunas do registro:
- FISCAL_ADM "Fiscal Administrativo" [DropDownList String]
**FISCAL_ADM.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- MATRICULA_FISCAL "Matrícula - Fiscal Administrativo" [TextBox String]
- MATRICULA_SUPLENTE "Matrícula -  Suplente" [TextBox String]
- FISCAL_ADM_SUPLENTE "Fiscal Administrativo - Suplente" [DropDownList String]
**FISCAL_ADM_SUPLENTE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### NOME_MAE — Nome da mãe do beneficiário titular
TextBox String → CP_ORDEM_SERVICO.NOME_MAE

### FAVORECIDO_MONITOR — Monitor
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_MONITOR
Descrição: Para pesquisa rápida faça:
1 - Clique na seta à direita do campo para abrir a relação de nomes;
2 - Com a lista ABERTA, pressione as teclas Ctrl + F (no IE aparece uma caixa de texto na parte superior esquerda e no Chrome na parte superior direita);
3 -  Digite o nome (ou parte dele) a ser pesquisado (serão marcados todas ocorrências que correspondam ao texto digitado);
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as id_pessoa, p.nome FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cpp on cpp.matricula = f.matricula inner join pessoa p on p.id_pessoa = cpp.id_pessoa WHERE upper(f.status_matricula) = 'ATIVO' AND p.ativo = 'Sim' order by p.nome")
```

### MODELO_TIPO — Modelo/Tipo
TextBox String → CPE_HOMOLOGACAO.MODELO_TIPO

### CSC_MATRICULA — Matrícula
TextBox String → CPE_CSC.CSC_MATRICULA

### LABEL5 — Texto Informativo
Label String(1024) → CPE_ORDEM_SERVICO.LABEL5

### ACEITE_DESIGNA_SISCCON2 — Aceite Designação
CheckBox Boolean → CPE_CONTRATOS02.ACEITE_DESIGNA_SISCCON2

### ID_DESIGNACAO — ID Designação
TextBox String(1500) → CPE_CONTRATOS02.ID_DESIGNACAO

### TE_NOME_EMPREGADO — Nome do empregado
DropDownList String → CPE_CSC.TE_NOME_EMPREGADO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### GRID_DESIGNACAO — Designações
DataGrid RecordList → Z_00143_GRID_DESIGNACAO.GRID_DESIGNACAO
Colunas do registro:
- MATRICULA_GESTOR_SUP "Matrícula Gestor Suplente" [TextBox String]
- MATRICULA_FMASTER_SUP "Matrícula Fiscal Master Suplente" [TextBox String]
- MATRICULA_FSERV_TITU "Matrícula Fiscal Serviço Titular" [TextBox String]
- MATRICULA_FSERV_SUP "Matrícula Fiscal Serviço Suplente" [TextBox String]
- ID_DESIGNACAO "ID Designação" [TextBox String]
- FISCAL_MASTER_TITU "Fiscal mASTER Titular" [DropDownList String]
**FISCAL_MASTER_TITU.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- FISCAL_MASTER_SUP "Fiscal Master Suplente" [DropDownList String]
**FISCAL_MASTER_SUP.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- MATRICULA_FMASTER_TITU "Matrícula Fiscal Master Titular" [TextBox String]
- DGCO "DGCO" [DropDownList String]
**DGCO.LookupScript**
```python
itens = ["00071/2020"]
```
- FISCAL_SERV_TITU "Fiscal de Serviço Titular" [DropDownList String]
**FISCAL_SERV_TITU.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- FISCAL_SERV_SUP "Fiscal de Serviço Suplente" [DropDownList String]
**FISCAL_SERV_SUP.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- GESTOR_CONTRAT_SUP "Gestor do Contrato Suplente" [DropDownList String]
**GESTOR_CONTRAT_SUP.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- RAZAO_SOCIAL "Razão Social" [TextBox String]
- OBJ "Objeto" [Memo String]

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
