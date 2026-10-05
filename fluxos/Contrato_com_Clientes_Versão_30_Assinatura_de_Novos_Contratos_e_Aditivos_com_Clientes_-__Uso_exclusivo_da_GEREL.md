# Fluxo: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" (ASSINATURACONTRATOSADITIVOS) — versão 30
Caminho: Fluxos > Contrato com Clientes Versão 30 Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)''
XML: `XMLs para teste/Contrato_com_Clientes_Versão_30_Assinatura_de_Novos_Contratos_e_Aditivos_com_Clientes -_(Uso_exclusivo_da_GEREL)''.xml` | Supravizio 19.1.1 | SubProcessoId 20590 | DesenhoProcessoId 2897 | ProcessoId 101
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: TIAGO MARTINS GUEDES
Classe do subprocesso: Objetivo=Fluxo de assinatura de contratos e aditivos já finalizados.; DescricaoCliente=Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)"; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Fluxo de assinatura de contratos e aditivos já finalizados.; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Assinatura de Novos Contratos e Aditivos (ASSINATURACONTRATOSADITIVOS)

## Grafo do fluxo
- [328316] EventoIntermediarioMensagem "Aviso de retorno para correção" → [328335] Inserir Informações Contratos Fornecedores
- [328317] EventoIntermediarioMensagem "Aviso de Chamado Encaminhado" → [328335] Inserir Informações Contratos Fornecedores
- [328318] EventoIntermediarioMensagem "Aviso sobre Abertura de Chamado" → [328336] Anexar Minuta
- [328319] Tarefa "Aguardando Parecer de conformidade" {DICOC} → [328344] Anexar Contrato / Aditivo assinado
- [328320] SubProcesso "CONTRATAÇÃO: Parecer de Conformidade" {Responsável atual} → [G74733] Conformidade OK?
- [328321] SubProcesso "CONTRATAÇÃO: Criar DGCO" {Responsável atual} → [328327] Indicar Condutores do Contrato
- [328322] SubProcesso "CONTRATAÇÃO: Criar transação no ERP" {Responsável atual} → [328343] CONTRATAÇÃO: Solicitar Cadastro do Contrato no OKS
- [328323] SubProcesso "CONTRATAÇÃO: Solicitar conta contabil" {Responsável atual} → [328322] CONTRATAÇÃO: Criar transação no ERP
- [328324] Tarefa "Retornar DGCO
" {Responsável atual} → [328335] Inserir Informações Contratos Fornecedores
- [328325] Tarefa "Informar Dados
" {Responsável atual} → [328321] CONTRATAÇÃO: Criar DGCO
- [328326] SubProcesso "Designar Condutores" {Responsável atual} → [328342] 
- [328327] Tarefa "Indicar Condutores do Contrato" {Responsável atual} → [328326] Designar Condutores
- [328328] Tarefa "Aprovação Responsável do Chamado" {DICOC} → [G74734] Aprova chamado?
- [328329] EventoIntermediarioMensagem "Aviso de complemento de informação" → [328325] Informar Dados

- [328330] EventoIntermediarioMensagem "Aviso de Parecer Conformidade" → [328319] Aguardando Parecer de conformidade
- [328331] EventoInicial "Assinatura de Contratos e Aditivos com Clientes" {Novos Negócios} → [328318] Aviso sobre Abertura de Chamado
- [328332] SubProcesso "Analisar Minuta de contrato ou aditivo" {DICOC} → [328337] Aguardar Análise Minuta

- [328333] Tarefa "Aguardar Minuta Corrigida" {DICOC} → [328336] Anexar Minuta
- [328334] LinkInicial "" → [328340] Analisar Enxoval
- [328335] Tarefa "Inserir Informações Contratos Fornecedores" {Gestor de Contrato} → [328345] Analisar Pedido
- [328336] Tarefa "Anexar Minuta" {Cliente} → [328341] Analisar Minuta
- [328337] Tarefa "Aguardar Análise Minuta
" {DICOC} → [G74732] É aditivo
- [328338] SubProcesso "CONTRATAÇÃO: Solicitar Cadastro de Item no ERP" {Responsável atual} → [328323] CONTRATAÇÃO: Solicitar conta contabil
- [328339] Tarefa "Inserir Enxoval" {Cliente} → [328340] Analisar Enxoval
- [328340] Tarefa "Analisar Enxoval" {DICOC} → [G74729] Enxoval Está Ok?
- [328341] Tarefa "Analisar Minuta" {DICOC} → [G74731] Precisa de Ajustes?
- [328342] SubProcesso "" {Responsável atual} → [328338] CONTRATAÇÃO: Solicitar Cadastro de Item no ERP
- [328343] SubProcesso "CONTRATAÇÃO: Solicitar Cadastro do Contrato no OKS" {Responsável atual} → [328324] Retornar DGCO

- [328344] Tarefa "Anexar Contrato / Aditivo assinado" {DICOC} → [328329] Aviso de complemento de informação
- [328345] Tarefa "Analisar Pedido" {DICOC} → [G74730] Precisa de Ajustes?
- [328346] EventoIntermediarioMensagem "Aviso de Encerramento de Chamado" → [328351] 
- [328347] EventoIntermediarioMensagem "Aviso de ajustes na Minuta" → [328333] Aguardar Minuta Corrigida
- [328348] EventoFinal "" {DICOC} → (fim)
- [328349] EventoIntermediarioMensagem "Aviso de Encerramento de Chamado" → [328348] 
- [328350] Tarefa "Gerel: Verificação Documentação Conformidade" {Cliente} → [328320] CONTRATAÇÃO: Parecer de Conformidade
- [328351] EventoFinal "" {DICOC} → (fim)
- [328352] LinkInicial "" → [328318] Aviso sobre Abertura de Chamado
- [G74729] Gateway "Enxoval Está Ok?" → «Não» [328339] Inserir Enxoval | «Sim» [328336] Anexar Minuta
- [G74730] Gateway "Precisa de Ajustes?" → «Sim» [328316] Aviso de retorno para correção | «Não» [328328] Aprovação Responsável do Chamado
- [G74731] Gateway "Precisa de Ajustes?" → «Não» [328332] Analisar Minuta de contrato ou aditivo | «Sim» [328347] Aviso de ajustes na Minuta
- [G74732] Gateway "É aditivo" → «Não» [328320] CONTRATAÇÃO: Parecer de Conformidade | «Sim» [328349] Aviso de Encerramento de Chamado
- [G74733] Gateway "Conformidade OK?" → «Sim» [328330] Aviso de Parecer Conformidade | «Não» [328350] Gerel: Verificação Documentação Conformidade
- [G74734] Gateway "Aprova chamado?" → «Sim» [328346] Aviso de Encerramento de Chamado | «Não» [328317] Aviso de Chamado Encaminhado

## Gateways
### [G74729] Enxoval Está Ok? (EventBasedExclusiveDecision)
Codigo=VERIFICAR_ENXOVAL
- alternativa → [328339] Inserir Enxoval: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; RotuloMotivo=Não
- alternativa → [328336] Anexar Minuta: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=2; RotuloMotivo=Sim
### [G74730] Precisa de Ajustes? (EventBasedExclusiveDecision)
Codigo=VERIFICAR_AJUSTES_INF_FORN
- alternativa → [328316] Aviso de retorno para correção: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1; MotivoObrigatorio=true; PublicarRespostaAA=true
- alternativa → [328328] Aprovação Responsável do Chamado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=2
### [G74731] Precisa de Ajustes? (EventBasedExclusiveDecision)
Codigo=VERIFICAR_AJUSTES
- alternativa → [328332] Analisar Minuta de contrato ou aditivo: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0; PublicarRespostaAA=true
- alternativa → [328347] Aviso de ajustes na Minuta: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1; PublicarRespostaAA=true
### [G74732] É aditivo (EventBasedExclusiveDecision)
- alternativa → [328320] CONTRATAÇÃO: Parecer de Conformidade: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [328349] Aviso de Encerramento de Chamado: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
### [G74733] Conformidade OK? (EventBasedExclusiveDecision)
- alternativa → [328330] Aviso de Parecer Conformidade: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [328350] Gerel: Verificação Documentação Conformidade: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
### [G74734] Aprova chamado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV_GESTOR_CONTR")
```
- alternativa → [328346] Aviso de Encerramento de Chamado: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [328317] Aviso de Chamado Encaminhado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [328316] EventoIntermediarioMensagem "Aviso de retorno para correção"
Destinatário: Cliente (papel 18)
Config: EmailRemetente=dicoc@bbts.com.br
ClasseAnexoResposta: Minuta do Contrato ou Aditivo
**ScriptEvento**
```python
Mensagem.Assunto = "Comunicado de devolução para ajustes"
Mensagem.Corpo = "Prezado(a). </br>A solicitação de número "+OrdemServico.NumeroSistema.ToString()+" - "+OrdemServico.Servico.ToString()+" foi devolvida para sua caixa para a efetivação de ajuste(s) na(s) informação(ões) conforme lista abaixo.</br></br>Ajustes: "+OrdemServico.ObtemMotivoGateway("VERIFICAR_AJUSTES_INF_FORN")+".</br>Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.</br> <a href='http://santacruz.cobra.com.br/Supravizio'> http://santacruz.cobra.com.br/Supravizio/</a></br></br>Atenciosamente,</br>Gesuc/Dicoc"
```

### [328317] EventoIntermediarioMensagem "Aviso de Chamado Encaminhado"
Config: ListaDestinatarios=dicoc@bbts.com.br
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços

### [328318] EventoIntermediarioMensagem "Aviso sobre Abertura de Chamado"
Config: ListaDestinatarios=dicoc@bbts.com.br
ModeloComunicado: Aviso sobre Abertura de Chamado
Corpo do comunicado: Prezados(as),
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada:
OrdemServico.DescricaoDetalhada 
 OrdemServico.Customizado.DESCRICAO_OBRIG 
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços

### [328319] Tarefa "Aguardando Parecer de conformidade"
Responsável: DICOC (papel 616)
Config: PermissaoRestritaPapel=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Parecer de Conformidade" classes: Parecer de Conformidade — RequeridoInicial=true

### [328320] SubProcesso "CONTRATAÇÃO: Parecer de Conformidade"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1022; Codigo=PARECE_CONFO; PassaTodosItens=true; RetornaTodosItens=true
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos e Aditivos -> Parecer Conformidade; FraseInversaAssociacao=Parecer Conformidade -> Assinatura de Novos Contratos e Aditivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=PARECERCONFORMEASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Parecer Conformidade

### [328321] SubProcesso "CONTRATAÇÃO: Criar DGCO"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1018; Codigo=DGCO; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "DGCO")
```
  - CustomPropertyId=516; CustomProperty=NOME_DAS
  - CustomPropertyId=2153; CustomProperty=JURIDICA_FISICA
  - CustomPropertyId=240; CustomProperty=CNPJ
  - CustomPropertyId=1810; CustomProperty=CSC_CPF
  - CustomPropertyId=1951; CustomProperty=RAZAO_SOCIAL_CLIENTE
  - CustomPropertyId=1074; CustomProperty=COMBOBOX1
  - CustomPropertyId=1059; CustomProperty=OBJETO_CONTRATACAO
  - PropertyId=1223; Property=DescricaoDetalhada
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos e Aditivos -> Solicitar reserva de DGCO; FraseInversaAssociacao=Solicitar reserva de DGCO -> Assinatura de Novos Contratos e Aditivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=DGCOASSINATURAADITIVO; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Solicitar reserva de DGCO

### [328322] SubProcesso "CONTRATAÇÃO: Criar transação no ERP"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1246; Codigo=TRANSACAO; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CNTFATERPAR")
```
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos e Aditivos ---> Criar transação no ERP; FraseInversaAssociacao=Criar transação no ERP ---> Assinatura de Novos Contratos e Aditivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=CRIARCADASTROITEMERP; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Consulta Fisco - Tributária (Estadual, Municipal ou Federal)

### [328323] SubProcesso "CONTRATAÇÃO: Solicitar conta contabil"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1010; Codigo=SOLICITAR_CONTA_CONTABIL; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CONTACONTABIL")
```
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2178; ClasseConfiguracao=Parecer Tributário
  - SuperClasse=Artefato; ClasseConfiguracaoId=2311; ClasseConfiguracao=Contrato ou Aditivo Assinado
  - SuperClasse=Artefato; ClasseConfiguracaoId=2228; ClasseConfiguracao=Nota Técnica
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos e Aditivos -> Solicitar Conta Contábil; FraseInversaAssociacao=Solicitar Conta Contábil -> Assinatura de Novos Contratos e Aditivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=SOLICITCONTACONTABIL; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Solicitar Conta Contábil

### [328324] Tarefa "Retornar DGCO
"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO]

### [328325] Tarefa "Informar Dados
"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.SetCustom('NOME_DAS', OrdemServico.Numero.ToString())
OrdemServico.ModificaCampoFormularioHabilitado('NOME_DAS', False)
OrdemServico.ModificaCampoFormularioVisivel('NOME_DAS', False)
```
**ScriptFim**
```python
OrdemServico.ModificaCampoFormularioHabilitado('RAZAO_SOCIAL_CLIENTE', False)
OrdemServico.ModificaCampoFormularioHabilitado('JURIDICA_FISICA', False)
OrdemServico.ModificaCampoFormularioHabilitado('CSC_CPF', False)
OrdemServico.ModificaCampoFormularioHabilitado('CNPJ', False)
```
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Itens = 'Cliente'
Formulario['COMBOBOX1'].Valor = 'Cliente'
Formulario['COMBOBOX1'].Habilitado = False

Formulario['CNPJ'].Visivel = False
Formulario['CSC_CPF'].Visivel = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados para criação de DGCO
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
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
  - RAZAO_SOCIAL_CLIENTE "Razão Social" [TextBox String → CPE_NEGOCIOS.RAZAO_SOCIAL_CLIENTE] obrigatório
  - COMBOBOX1 "Fornecedor ou Cliente?" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO] obrigatório
  - DescricaoDetalhada (nativo) "Motivo do cadastro" obrigatório
  - NOME_DAS "OS" [TextBox String → CP_ORDEM_SERVICO.NOME_DAS]

### [328326] SubProcesso "Designar Condutores"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1259; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=610; CustomProperty=PPGEREX_NEGOCIO
  - CustomPropertyId=1805; CustomProperty=CSC_NUMERO
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=1059; CustomProperty=OBJETO_CONTRATACAO
  - CustomPropertyId=4698; CustomProperty=CONDUT_CONTRAT_TITU
  - CustomPropertyId=4700; CustomProperty=MATRICULA_CONDUT_TITU
  - CustomPropertyId=4699; CustomProperty=CONDUT_CONTRAT_SUP
  - CustomPropertyId=4701; CustomProperty=MATRICULA_CONDUT_SUP
  - CustomPropertyId=578; CustomProperty=SCR_TODOS_RH
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2178; ClasseConfiguracao=Parecer Tributário
  - SuperClasse=Artefato; ClasseConfiguracaoId=2209; ClasseConfiguracao=Aditivo de Contrato Assinado
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos --> Designar Condutores; FraseInversaAssociacao=Designar Condutores- > Assinatura de Novos Contratos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ASSINATURAASSESORES; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Designar Contrato Cliente

### [328327] Tarefa "Indicar Condutores do Contrato"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.SetCustom('CSC_NUMERO', OrdemServico.GetCustom('NUM_CONTRATO'))
#OrdemServico.SetCustom('OBJETO_CONTRATACAO', 'PRJ_OBJETO')
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Pessoa
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

import clr
import re
from System import Convert
from Newtonsoft.Json.Linq import JValue, JArray
from Newtonsoft.Json import JsonConvert
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System import TimeSpan
from System.Text import Encoding
import unicodedata

# Variáveis necessárias
dgco = OrdemServico.GetCustom("CSC_DGCO").ToString()
nomeContrato = OrdemServico.GetCustom("NOME_FORNECEDOR").ToString()
nomeCliente = OrdemServico.GetCustom("RAZAO_SOCIAL_CLIENTE").ToString()

obj = OrdemServico.GetCustom("OBJETO_CONTRATACAO").ToString()
nmContrato = OrdemServico.GetCustom("CSC_NUMERO").ToString()
tipoPessoa = ""

cpf_cnpj = OrdemServico.GetCustom('CSC_CPF').ToString() if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Física' else OrdemServico.GetCustom('CNPJ').ToString()

def normaliza_string(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')


if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Física' or OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Fisica':
    tipoPessoa = 'PESSOA_FISICA'

    
if OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Jurídica' or OrdemServico.GetCustom('JURIDICA_FISICA').ToString() == 'Pessoa Juridica':
    tipoPessoa = 'PESSOA_JURIDICA'


# Normalizando strings para evitar problemas de codificação
razao_social = normaliza_string(OrdemServico.GetCustom('RAZAO_SOCIAL_CLIENTE').ToString())
fisica_juridica = normaliza_string(OrdemServico.GetCustom('JURIDICA_FISICA').ToString())




def aplicar_mascara(cpf_cnpj, tipoPessoa):
    if tipoPessoa == "PESSOA_FISICA":  # Pessoa Física
        return re.sub(r"(\d{3})(\d{3})(\d{3})(\d{2})", r"\1.\2.\3-\4", cpf_cnpj)
    elif tipoPessoa == "PESSOA_JURIDICA":  # Pessoa Jurídica
        return re.sub(r"(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})", r"\1.\2.\3/\4-\5", cpf_cnpj)
    return cpf_cnpj  # Retorna o documento original se o tipo não for reconhecido



# Aplica a máscara ao documento
cpf_cnpj_mascara = aplicar_mascara(cpf_cnpj, tipoPessoa)


OrdemServico.AdicionaComentario(dgco.ToString(), True)
OrdemServico.AdicionaComentario(nomeContrato.ToString(), True)
OrdemServico.AdicionaComentario(nomeCliente.ToString(), True)
OrdemServico.AdicionaComentario(obj.ToString(), True)
OrdemServico.AdicionaComentario(nmContrato.ToString(), True)
OrdemServico.AdicionaComentario(tipoPessoa.ToString(), True)
OrdemServico.AdicionaComentario(cpf_cnpj.ToString(), True)
OrdemServico.AdicionaComentario(cpf_cnpj_mascara.ToString(), True)



# Token de autenticação
token = '***MASCARADO***'
url_buscar = ''
url_inserir = ''

# Determina o ambiente e define as URLs
sql = "select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)

if dom == 'HOMOLOGAÇÃO':    
    url_buscar = 'https://sisccon-lab.bbts.com.br/supravizio/supra/buscar-contratos-dicoc?dgco=' + dgco
    url_inserir = 'https://sisccon-lab.bbts.com.br/supravizio/supra/inserir-contrato-dicoc'

if dom == 'PRODUÇÃO':    
    url_buscar = 'https://sisccon.bbts.com.br/supravizio/supra/buscar-contratos-dicoc?dgco=' + dgco
    url_inserir = 'https://sisccon.bbts.com.br/supravizio/supra/inserir-contrato-dicoc'

# Primeira requisição: buscar contratos
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(15)
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
client.DefaultRequestHeaders.Accept.Clear()
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))

response_buscar = client.GetAsync(url_buscar).Result
if not response_buscar.IsSuccessStatusCode:
    OrdemServico.AdicionaComentario("Erro ao buscar contratos: " + response_buscar.StatusCode.ToString(), True)
    

result_buscar = response_buscar.Content.ReadAsStringAsync().Result
dados_buscar = JsonConvert.DeserializeObject(result_buscar)

# Verifica se já existe um contrato
if len(dados_buscar) > 0:
    OrdemServico.AdicionaComentario("Contrato já cadastrado no sistema.", True)
    

# Segunda requisição: inserir contrato
contrato = {
    "numero": nmContrato,
    "dgco": dgco,
    "objeto": obj,
    "nomeCliente": nomeCliente,
    "nomeContrato": nomeContrato,
    "tipo_pessoa": tipoPessoa.ToString(),
    "cpf_cnpj": cpf_cnpj_mascara.ToString()
}


OrdemServico.AdicionaComentario(contrato.ToString(), True)

json_contrato = JsonConvert.SerializeObject(contrato)
content = StringContent(json_contrato, Encoding.UTF8, "application/json")
response_inserir = client.PostAsync(url_inserir, content).Result

if not response_inserir.IsSuccessStatusCode:
    OrdemServico.AdicionaComentario("Erro ao inserir contrato: " + response_inserir.StatusCode.ToString(), True)
    
else:
    OrdemServico.AdicionaComentario("Contrato inserido com sucesso.", True)




OrdemServico.ModificaCampoFormularioHabilitado('CSC_DGCO', False)
OrdemServico.ModificaCampoFormularioHabilitado('CSC_NUMERO', False)
OrdemServico.ModificaCampoFormularioHabilitado('CONDUT_CONTRAT_TITU', False)
OrdemServico.ModificaCampoFormularioHabilitado('CONDUT_CONTRAT_SUP', False)
OrdemServico.ModificaCampoFormularioHabilitado('MATRICULA_CONDUT_TITU', False)
OrdemServico.ModificaCampoFormularioHabilitado('MATRICULA_CONDUT_SUP', False)
OrdemServico.ModificaCampoFormularioHabilitado('NOME_FORNECEDOR', False)
OrdemServico.ModificaCampoFormularioHabilitado('NUM_CONTRATO', False)
OrdemServico.ModificaCampoFormularioHabilitado('OBJETO_CONTRATACAO', False)
```
**ScriptValidacao**
```python
matriculaCondTitu = str(OrdemServico.GetCustom("MATRICULA_CONDUT_TITU"))
matriculaCondSup = str(OrdemServico.GetCustom("MATRICULA_CONDUT_SUP"))

if matriculaCondTitu == matriculaCondSup:
    Criticas.AdicionaPendencia('O assessor escolhido não pode assumir dois papeis no contrato!')
    
elif (matriculaCondTitu == '0' or matriculaCondTitu == 0) or (matriculaCondSup == '0' or matriculaCondSup == 0):
    Criticas.AdicionaPendencia('O assessor escolhido não pode assumir dois papeis no contrato!')
```
**ScriptFormCarregado**
```python
Formulario["MATRICULA_CONDUT_TITU"].Habilitado = False
Formulario["MATRICULA_CONDUT_SUP"].Habilitado = False


Formulario['CSC_NUMERO'].Valor = Formulario['NUM_CONTRATO'].Valor
#Formulario['OBJETO_CONTRATACAO'].Valor = Formulario['PRJ_OBJETO'].Valor
Formulario['NUM_CONTRATO'].Visivel = False
```
- Operação PR0001 Preencher Campos
  - NUM_CONTRATO "Número do Contrato" [TextBox String(20) → CP_ORDEM_SERVICO.NUM_CONTRATO]
  - NOME_FORNECEDOR "Nome Empresa" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - OBJETO_CONTRATACAO "Objeto da Contratação" [Memo String(1999) → CP_ORDEM_SERVICO.OBJETO_CONTRATACAO] obrigatório
  - CONDUT_CONTRAT_TITU "Condutor do Contrato" [DropDownList String → CPE_CONTRATOS02.CONDUT_CONTRAT_TITU] obrigatório
**CONDUT_CONTRAT_TITU.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
matriculaCondSup = Formulario['MATRICULA_CONDUT_SUP'].Valor

if Formulario["CONDUT_CONTRAT_TITU"].Valor != "" or Formulario["CONDUT_CONTRAT_TITU"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["CONDUT_CONTRAT_TITU"].Valor)
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

    matriculaCondSup = Formulario['MATRICULA_CONDUT_SUP'].Valor
    
    matricula = ''
    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()



    if (str(matricula) == str(matriculaCondSup)):
        Formulario["CONDUT_CONTRAT_TITU"].Valor = 'O nome já se encontra designado em outro papel no mesmo DGCO!'
        Formulario["MATRICULA_CONDUT_TITU"].Valor = 0 #Necessário para validacão
        OrdemServico.SetCustom('MATRICULA_CONDUT_TITU', 0)
    else:
        Formulario["MATRICULA_CONDUT_TITU"].Valor = matricula.ToString()
       
 
    if Formulario["CONDUT_CONTRAT_TITU"].Valor == None or Formulario["CONDUT_CONTRAT_TITU"].Valor == '':
        Formulario["MATRICULA_CONDUT_TITU"].Valor = None
```
  - MATRICULA_CONDUT_TITU "Matrícula Condutor" [TextBox String → CPE_CONTRATOS02.MATRICULA_CONDUT_TITU] obrigatório — Coluna=2
  - CONDUT_CONTRAT_SUP "Condutor Suplente" [DropDownList String → CPE_CONTRATOS02.CONDUT_CONTRAT_SUP]
**CONDUT_CONTRAT_SUP.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
matriculaCondTitu = Formulario['MATRICULA_CONDUT_TITU'].Valor

if Formulario["CONDUT_CONTRAT_SUP"].Valor != "" or Formulario["CONDUT_CONTRAT_SUP"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["CONDUT_CONTRAT_SUP"].Valor)
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

    
    matriculaCondTitu = Formulario['MATRICULA_CONDUT_TITU'].Valor
    
    matricula = ''
    for linha in lista.Rows:
        matricula = linha["MATRICULA"].ToString()



    if (str(matricula) == str(matriculaCondTitu)):
        Formulario["CONDUT_CONTRAT_SUP"].Valor = 'O nome já se encontra designado em outro papel no mesmo DGCO!'
        Formulario["MATRICULA_CONDUT_SUP"].Valor = 0 #Necessário para validacão
        OrdemServico.SetCustom('MATRICULA_CONDUT_SUP', 0)
    else:
        Formulario["MATRICULA_CONDUT_SUP"].Valor = matricula.ToString()
       
 
    if Formulario["CONDUT_CONTRAT_SUP"].Valor == None or Formulario["CONDUT_CONTRAT_SUP"].Valor == '':
        Formulario["MATRICULA_CONDUT_SUP"].Valor = None
```
  - MATRICULA_CONDUT_SUP "Matrícula Condutor Suplente" [TextBox String → CPE_CONTRATOS02.MATRICULA_CONDUT_SUP] — Coluna=2
  - SCR_TODOS_RH "UOR da gestão do contrato" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
  - PPGEREX_NEGOCIO "Gerente Executivo" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO] obrigatório
  - CSC_DGCO "Nº DGCO" [TextBox String → CPE_CSC.CSC_DGCO] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}
**CSC_DGCO.ScriptModificado**
```python
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

dgco = Formulario["CSC_DGCO"].Valor

# Token de autenticação
token = '***MASCARADO***'
url = ''

# URL da API
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)
if dom == 'HOMOLOGAÇÃO':    
    url = 'https://sisccon-lab.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco-dicoc?dgco=' + str(dgco)

if dom == 'PRODUÇÃO':    
    url = 'https://sisccon.bbts.com.br/supravizio/supra/buscar-intervenientes-por-dgco-dicoc?dgco=' + str(dgco)


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
            
            # jsonArray length deve ser maior q 0; caso seja, já contratos a designar. caso não, apenas continuar com a transferência
            if len(jsonArray) > 0:
                for i, item in enumerate(jsonArray):
                
                    
                    Formulario['NOME_FORNECEDOR'].Valor = item['fornecedor'].ToString() if item['fornecedor'].ToString() != '' else 'N/A'
                    Formulario['OBJETO_CONTRATACAO'].Valor = item['objeto'].ToString() if item['objeto'].ToString() != '' else 'N/A'
                    
                    Formulario["CSC_NUMERO"].Valor = '00000'
                    
                    Formulario['NOME_FORNECEDOR'].Habilitado = False
                    Formulario['OBJETO_CONTRATACAO'].Habilitado = False
                    
                    
                
                    matriculaCondTitular = str(item['matricula_condutor_titular'])
                    matriculaCondSup = str(item['matricula_condutor_suplente'])
                    
                    idCondTitular = 0
                    idCondSup = 0
                

                    result_table1 = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, PESSOA.ID_PESSOA, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA = '" + str(matriculaCondTitular) + "'")
                            
                    for row in result_table1.Rows:
                        idCondTitular = row["ID_PESSOA"]
                        
                        
   
                            
                    result_table2 = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, PESSOA.ID_PESSOA, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA = '" + str(matriculaCondSup) + "'")
                            
                    for row in result_table2.Rows:
                        idCondSup = row["ID_PESSOA"]
                    
                    
                        
                    Formulario["CONDUT_CONTRAT_TITU"].Valor = str(idCondTitular)
                    Formulario["MATRICULA_CONDUT_TITU"].Valor = str(matriculaCondTitular)
                    
                    Formulario["CONDUT_CONTRAT_SUP"].Valor = str(idCondSup)
                    Formulario["MATRICULA_CONDUT_SUP"].Valor = str(matriculaCondSup)
                        
                    
                    
        except Exception as e:
            pass
        
except Exception as e:
    pass
```
  - CSC_NUMERO "Número do Contrato" [TextBox String(100) → CPE_CSC.CSC_NUMERO] obrigatório

### [328328] Tarefa "Aprovação Responsável do Chamado"
Responsável: DICOC (papel 616)
Config: Codigo=APROV_GESTOR_CONTR
**ScriptFormCarregado**
```python
Formulario["FAVORECIDO_TODOS"].Habilitado = False
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação Responsável do Chamado; MinimoAprovadores=1
  - (aprovação) INF_CONTRATOS_FORNEC "Informações Referente aos Contratos Fornecedores" [DataGrid RecordList → Z_00143_INF_CONTRATOS_FORNEC.INF_CONTRATOS_FORNEC] — PermiteModificarAprovado=true
  - aprovador: DICOC (Unico)
- Operação PR0001 Preencher Campos
  - LABEL1 "<font color="red">*Citar <b> todos</b> os contratos de Fornecedores no qual o serviço a ser contratado detém uma vinculação direta e indireta indicando qual rubrica da MPOG do contrato Cliente poderá ser impactada.<br> *Em caso de dúvidas consultar à Divisão de Contratos com Clientes - Dicoc.</font>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - FAVORECIDO_TODOS "Gestor do Contrato" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - INF_CONTRATOS_FORNEC "Informações Referente aos Contratos Fornecedores" [DataGrid RecordList → Z_00143_INF_CONTRATOS_FORNEC.INF_CONTRATOS_FORNEC] obrigatório — FormaEdicaoWeb=JanelaPopup; QtdColunasFormulario=1; LarguraJanelaPopup=1000
    - coluna RAZAO_SOCIAL obrigatório
    - coluna RUBRICA obrigatório
    - coluna DGCO obrigatório
    - coluna RUBRICAS obrigatório

### [328329] EventoIntermediarioMensagem "Aviso de complemento de informação"
Destinatário: Cliente (papel 18)
Config: EmailRemetente=dicoc@bbts.com.br
ClasseAnexoResposta: Minuta do Contrato ou Aditivo
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Recurso.Custom import Contrato
Mensagem.Assunto = "Comunicado Inserir Informações Contratos Fornecedores"
Mensagem.Corpo = "Prezado(a). </br>A solicitação de número "+OrdemServico.NumeroSistema.ToString()+" - "+OrdemServico.Servico.ToString()+" foi encaminhada para sua caixa, para inserir as informações de contratos de fornecedores.</br></br>Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.</br> <a href='http://santacruz.cobra.com.br/Supravizio'> http://santacruz.cobra.com.br/Supravizio/</a></br></br>Atenciosamente,</br>Gesuc/Dicoc"
```

### [328330] EventoIntermediarioMensagem "Aviso de Parecer Conformidade"
Destinatário: Cliente e Responsavel Atual (papel 544)
ModeloComunicado: Aviso de Parecer Conformidade
ClasseAnexoResposta: Parecer de Conformidade
Corpo do comunicado: Prezado(a) , OrdemServico.Cliente.Nome 
Para darmos continuidade ao chamado interno OrdemServico.Numero - OrdemServico.Servico , é necessário responder esse email anexando o parecer de conformidade.
Em caso de dúvidas encaminhar email para DICOC@bbts.com.br
Para mais detalhes sobre esta solicitação Link.Consulta 
Atenciosamente,
Central de Serviços

### [328331] EventoInicial "Assinatura de Contratos e Aditivos com Clientes"
Responsável: Novos Negócios (papel 399)
Config: Codigo=ASSINATURAS_CONTRATOS_ADITIVOS
TipoSolicitacao: Assinatura de Contratos e Aditivos com Clientes
- Operação PR0001 Preencher Campos
  - DescricaoDetalhada (nativo) obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=DOCS
  - anexo "" classes: Nota Técnica — RequeridoInicial=true
  - anexo "Documentos Obrigatórios" classes: Consolidação Técnica — RequeridoInicial=true
  - anexo "" classes: Parecer Tributário — RequeridoInicial=true
  - anexo "" classes: Analise de Risco Legal — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS
  - anexo "" classes: DRE Tela Azul — RequeridoInicial=true
  - anexo "Demais Documentos" classes: Planilha de Precificação — RequeridoInicial=true
  - anexo "" classes: Proposta Comercial — RequeridoInicial=true

### [328332] SubProcesso "Analisar Minuta de contrato ou aditivo"
Referência: Abrir chamado para parecer COJUR (Analisar Minuta)
Responsável: DICOC (papel 616)
Config: AssociacaoId=169; Codigo=MINUTAJURIDICO; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1223; Property=DescricaoDetalhada
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2292; ClasseConfiguracao=Minuta
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos contratos e Aditivos -> Consultas Jurídicas; FraseInversaAssociacao=Consultas Jurídicas -> Assinatura de Novos contratos e Aditivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ASSINATURA_CONSULTA_JURIDICA; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Consultas Jurídicas

### [328333] Tarefa "Aguardar Minuta Corrigida"
Responsável: DICOC (papel 616)
Config: Codigo=DEVOLVER_AJUSTES

### [328334] LinkInicial ""
Config: Codigo=MINUTA; TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=204; Nome=MARCELO CAVALCANTE DE OLIVEIRA LIMA; FraseAssociacao=Portal de Estruturação de Negócios -> Assinatura de Novos Contratos e Aditivos

### [328335] Tarefa "Inserir Informações Contratos Fornecedores"
Referência: Inserir as informações referente aos contratos fornecedores
Responsável: Gestor de Contrato (papel 976)
**ScriptFormCarregado**
```python
Formulario["FAVORECIDO_TODOS"].Habilitado = True


#OrdemServico.SetCustom('FAVORECIDO_COBRA', JEFFERSON)
```
- Operação PR0001 Preencher Campos
  - LABEL1 "<font color="red">*Citar <b> todos</b> os contratos de Fornecedores no qual o serviço a ser contratado detém uma vinculação direta e indireta indicando qual rubrica da MPOG do contrato Cliente poderá ser impactada.<br> *Em caso de dúvidas consultar à Divisão de Contratos com Clientes - Dicoc.</font>" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - FAVORECIDO_TODOS "Gestor do Contrato" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - INF_CONTRATOS_FORNEC "Informações Referente aos Contratos Fornecedores" [DataGrid RecordList → Z_00143_INF_CONTRATOS_FORNEC.INF_CONTRATOS_FORNEC] obrigatório — FormaEdicaoWeb=JanelaPopup; QtdColunasFormulario=1; LarguraJanelaPopup=1000
    - coluna DGCO obrigatório
    - coluna RUBRICAS obrigatório
    - coluna RAZAO_SOCIAL obrigatório
    - coluna RUBRICA obrigatório
  - FAVORECIDO_COBRA "Gerente de Serviço" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório

### [328336] Tarefa "Anexar Minuta"
Responsável: Cliente (papel 18)
- Operação PR0004 Associar Itens Configuração: Nome=MINUTA_GEREL
  - anexo "Minuta Contratual" classes: Minuta — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - PPGEREX_NEGOCIO "Gerente Executivo do Negócio" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO] obrigatório
  - SCR_TODOS_RH "UOR da gestão do contrato" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório

### [328337] Tarefa "Aguardar Análise Minuta
"
Responsável: DICOC (papel 616)
- Operação PR0004 Associar Itens Configuração
  - anexo "Contrato ou aditivo de contrato Chancelado" classes: Minuta do Contrato ou Aditivo — ProduzidoTermino=true
  - anexo "Parecer Jurídico" classes: Gejur - Parecer — RequeridoInicial=true
  - anexo "Outros Documentos" classes: Arquivo — ProduzidoTermino=true

### [328338] SubProcesso "CONTRATAÇÃO: Solicitar Cadastro de Item no ERP"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1021; Codigo=ITEM; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "SERVICOSPRESTADOSBBTS")
```
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2178; ClasseConfiguracao=Parecer Tributário
  - SuperClasse=Artefato; ClasseConfiguracaoId=2311; ClasseConfiguracao=Contrato ou Aditivo Assinado
  - SuperClasse=Artefato; ClasseConfiguracaoId=2292; ClasseConfiguracao=Minuta
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos e Aditiivos -> Cadastro de Itens; FraseInversaAssociacao=Cadastro de Itens -> Assinatura de Novos Contratos e Aditiivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=CADASTROASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Cadastro de Itens

### [328339] Tarefa "Inserir Enxoval"
Responsável: Cliente (papel 18)
Config: Codigo=INSERIR_ENXOVAL; ConfirmaResponsabilidade=true

### [328340] Tarefa "Analisar Enxoval"
Responsável: DICOC (papel 616)
Config: Codigo=ANALISAR_ENXOVAL; ConfirmaResponsabilidade=true

### [328341] Tarefa "Analisar Minuta"
Responsável: DICOC (papel 616)
Config: Codigo=ANALISAR_PEDIDO; ConfirmaResponsabilidade=true

### [328342] SubProcesso ""
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1013; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=610; CustomProperty=PPGEREX_NEGOCIO
  - CustomPropertyId=1805; CustomProperty=CSC_NUMERO
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=4698; CustomProperty=CONDUT_CONTRAT_TITU
  - CustomPropertyId=4700; CustomProperty=MATRICULA_CONDUT_TITU
  - CustomPropertyId=4699; CustomProperty=CONDUT_CONTRAT_SUP
  - CustomPropertyId=4701; CustomProperty=MATRICULA_CONDUT_SUP
  - CustomPropertyId=578; CustomProperty=SCR_TODOS_RH
  - CustomPropertyId=1059; CustomProperty=OBJETO_CONTRATACAO
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2178; ClasseConfiguracao=Parecer Tributário
  - SuperClasse=Artefato; ClasseConfiguracaoId=2209; ClasseConfiguracao=Aditivo de Contrato Assinado
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos e Aditivos -> Designaçao Contrato Cliente; FraseInversaAssociacao=Designação Contrato Cliente -> Assinatura de Novos Contratos e Aditivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=DESIGNACONTRATCLIENTEASSINA; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Designar Contrato Cliente

### [328343] SubProcesso "CONTRATAÇÃO: Solicitar Cadastro do Contrato no OKS"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1025; Codigo=SOLICITAR_OKS; PassaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CADCONTRATO")
```
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=1805; CustomProperty=CSC_NUMERO
  - CustomPropertyId=1916; CustomProperty=NOME_CONTRATO
- Associação: Ativo=true; FraseAssociacao=Assinatura de Novos Contratos e Aditivos -> Cadastrar Contrato no OKS; FraseInversaAssociacao=Cadastrar Contrato no OKS -> Assinatura de Novos Contratos e Aditivos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=CADASTROOKSASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)" → alvo: Cadastrar contratos no OKS

### [328344] Tarefa "Anexar Contrato / Aditivo assinado"
Responsável: DICOC (papel 616)
- Operação PR0001 Preencher Campos
  - PRJ_OBJETO "Objeto do Instrumento" [Memo String → CPE_PRJ_BB.PRJ_OBJETO] obrigatório
  - NUM_CONTRATO "Número do Contrato Cliente" [TextBox String(20) → CP_ORDEM_SERVICO.NUM_CONTRATO] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Contrato ou Aditivo Assinado" classes: Contrato ou Aditivo Assinado — ProduzidoTermino=true

### [328345] Tarefa "Analisar Pedido"
Responsável: DICOC (papel 616)
Config: Codigo=ANALISAR_PEDIDO2; ConfirmaResponsabilidade=true

### [328346] EventoIntermediarioMensagem "Aviso de Encerramento de Chamado"
Destinatário: Cliente e Responsavel Atual (papel 544)
ModeloComunicado: Email de fechamento do chamado
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero referente ao assunto OrdemServico.Assunto foi encerrada com sucesso!
Atebciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2131; ClasseConfiguracao=Proposta Comercial
  - ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
  - ClasseConfiguracaoId=2159; ClasseConfiguracao=Parecer de Conformidade
  - ClasseConfiguracaoId=2167; ClasseConfiguracao=Contrato
  - ClasseConfiguracaoId=2210; ClasseConfiguracao=Minuta do Aditivo

### [328347] EventoIntermediarioMensagem "Aviso de ajustes na Minuta"
Destinatário: Cliente e Responsavel Atual (papel 544)
Config: EmailRemetente=dicoc@bbts.com.br
ModeloComunicado: Aviso de ajustes na Minuta
ClasseAnexoResposta: Minuta do Contrato ou Aditivo
Corpo do comunicado: Prezado(a), OrdemServico.Cliente.Nome 
Para que o chamado interno OrdemServico.Numero - OrdemServico.Servico tenha continuidade é necessário verificar os ajustes na Minuta enviada.
Favor responder a este e-mail, anexando a minuta corrigida.
Em caso de dúvidas encaminhar email para DICOC@bbts.com.br
Para mais detalhes sobre esta solicitação Link.Consulta.
Atenciosamente,
Central de Serviços

### [328348] EventoFinal ""
Responsável: DICOC (papel 616)

### [328349] EventoIntermediarioMensagem "Aviso de Encerramento de Chamado"
Destinatário: Cliente e Responsavel Atual (papel 544)
ModeloComunicado: Email de fechamento do chamado
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero referente ao assunto OrdemServico.Assunto foi encerrada com sucesso!
Atebciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2131; ClasseConfiguracao=Proposta Comercial
  - ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
  - ClasseConfiguracaoId=2159; ClasseConfiguracao=Parecer de Conformidade
  - ClasseConfiguracaoId=2167; ClasseConfiguracao=Contrato
  - ClasseConfiguracaoId=2210; ClasseConfiguracao=Minuta do Aditivo

### [328350] Tarefa "Gerel: Verificação Documentação Conformidade"
Responsável: Cliente (papel 18)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexos" classes: Arquivos 2 — RequeridoInicial=true

### [328351] EventoFinal ""
Responsável: DICOC (papel 616)

### [328352] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=1584; Nome=DANIELA BERNARDO PROVAZI PESCI; FraseAssociacao=Alvo: Assinatura de Novos Contratos

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 616: DICOC
Tipo=RelacaoGrupos
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 544: Cliente e Responsavel Atual
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Responsável atual (PessoaOrdemServico)
### papel 399: Novos Negócios
Tipo=RelacaoGrupos
### papel 976: Gestor de Contrato
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
idPessoa = OrdemServico["FAVORECIDO_TODOS"]

if idPessoa!= None:
    p = Pessoa.Carrega("Id",idPessoa )
    Atores.Adiciona(p);
```

## Campos customizados usados (definição global)

### CSC_DGCO — DGCO
TextBox String → CPE_CSC.CSC_DGCO

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

### NUM_CONTRATO — Número do Contrato
TextBox String(20) → CP_ORDEM_SERVICO.NUM_CONTRATO

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### CONDUT_CONTRAT_TITU — Condutor Responsável do Contrato
DropDownList String → CPE_CONTRATOS02.CONDUT_CONTRAT_TITU
**LookupScript**
```python
Itens = DB.ExecuteDataTable("Select Distinct To_Char(PESSOA.ID_PESSOA) As ID_PESSOA, PESSOA.NOME, ORGAO.SIGLA From CP_PESSOA CP Inner Join PESSOA On CP.ID_PESSOA = PESSOA.ID_PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Where ORGAO.SIGLA = '3000003430' And PESSOA.ATIVO = 'Sim' Order By PESSOA.NOME")
```

### MATRICULA_CONDUT_TITU — Matrícula condutor do contrato titular
TextBox String → CPE_CONTRATOS02.MATRICULA_CONDUT_TITU

### CONDUT_CONTRAT_SUP — Condutor Responsável do Contrato - Suplente
DropDownList String → CPE_CONTRATOS02.CONDUT_CONTRAT_SUP
**LookupScript**
```python
Itens = DB.ExecuteDataTable("Select Distinct To_Char(PESSOA.ID_PESSOA) As ID_PESSOA, PESSOA.NOME, ORGAO.SIGLA From CP_PESSOA CP Inner Join PESSOA On CP.ID_PESSOA = PESSOA.ID_PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Where ORGAO.SIGLA = '3000003430' And PESSOA.ATIVO = 'Sim' Order By PESSOA.NOME")
```

### MATRICULA_CONDUT_SUP — Matrícula condutor do contrato suplente
TextBox String → CPE_CONTRATOS02.MATRICULA_CONDUT_SUP

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### PPGEREX_NEGOCIO — Gerente Executivo do Negócio
DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO
**LookupScript**
```python
#Itens = DB.ExecuteDataTable("Select Distinct to_char(PESSOA.ID_PESSOA) as id_pessoa,PESSOA.NOME_ABREVIADO From ORGAO Inner Join PESSOA On ORGAO.ID_GESTOR = PESSOA.ID_PESSOA Where ORGAO.ATIVO = 'Sim' And ORGAO.DESCRICAO Like '%GERE%' And PESSOA.ATIVO = 'Sim' Order By PESSOA.NOME_ABREVIADO")

Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(pessoa.id_pessoa) AS id_pessoa, pessoa.nome_abreviado FROM orgao INNER JOIN pessoa ON orgao.id_gestor = pessoa.id_pessoa INNER JOIN cp_pessoa ON cp_pessoa.id_pessoa = pessoa.id_pessoa WHERE (orgao.ativo = 'Sim' AND cp_pessoa.cargo_funcional LIKE '%EXECUTIVO%' AND pessoa.ativo = 'Sim') or pessoa.id_pessoa in (SELECT p.id_substituto_aprovacao FROM pessoa p INNER JOIN cp_pessoa   cp ON ( p.id_pessoa = cp.id_pessoa ) WHERE cp.cargo_funcional LIKE '%EXECUTIVO%' AND p.ativo = 'Sim' AND sysdate BETWEEN dt_inicio_substit_aprov AND dt_fim_substit_aprov) ORDER BY pessoa.nome_abreviado")
```

### CSC_NUMERO — Número
TextBox String(100) → CPE_CSC.CSC_NUMERO

### INF_CONTRATOS_FORNEC — Informações Referente aos Contratos Fornecedores
DataGrid RecordList → Z_00143_INF_CONTRATOS_FORNEC.INF_CONTRATOS_FORNEC
Colunas do registro:
- DGCO "DGCOs do(s) Contrato(s) de contrapartida com o FORNECEDOR" [TextBox String]
- RAZAO_SOCIAL "Razão Social do Fornecedor" [TextBox String]
- RUBRICA "Rubrica(s) conforme MPOG Contrato Cliente*" [TextBox String]

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Não') order by nomemat")
```

### PRJ_OBJETO — Objeto
Memo String → CPE_PRJ_BB.PRJ_OBJETO

## Biblioteca de scripts referenciada
dicoc, teste
(fonte em catalogo/biblioteca/<Nome>.py)
