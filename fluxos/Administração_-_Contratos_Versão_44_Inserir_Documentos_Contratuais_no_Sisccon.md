# Fluxo: Inserir Documentos Contratuais no Sisccon (INSERIRDOCSGESCON) — versão 44
Caminho: Fluxos > Administração - Contratos Versão 44 Inserir Documentos Contratuais no Sisccon
XML: `XMLs para teste/Administração_-_Contratos_Versão_44_Inserir_Documentos_Contratuais_no_Sisccon.xml` | Supravizio 19.1.1 | SubProcessoId 21681 | DesenhoProcessoId 3001 | ProcessoId 127
Órgão dono: 3000003410 - DIVISAO DE PLANEJAMENTO E IMPORTACAO | Responsável: GRUWER IURI MACIEL NASCIMENTO
Classe do subprocesso: Objetivo=Inserir Documentos Contratuais no Sisccon; DescricaoCliente=Inserir Documentos Contratuais no Sisccon; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Inserir Contrato de Comodato no Sisccon (INSERIRCOMODATO); Inserir Termo de Confidencialidade no Sisccon (INSERIRCONFIDENCIALIDADE); Inserir Contrato de Convênio no Sisccon (INSERIRCONVENIO); Inserir Participação em Contrato com Fornecedor BB no Sisccon (INSERIRPARTICIPACAOBB); Inserir Termo de Doação no Sisccon (INSERIRDOACAO); Inserir Contrato com Fornecedores no Sisccon (INSERIRCONTRATO); Inserir Aditivo no Sisccon (INSERIRADITIVO); Inserir Ata de Registro de Preço no Sisccon (INSERIRATA); Inserir Apostilamento no Sisccon (INSERIRAPOSTILAMENTO); Inserir Contrato de Parceria no Sisccon (INSERIRPARCERIA); Inserir Acordo de Cooperação Técnica no Sisccon (INSERIRCOOPERACAO); Inserir Termo de Concessão de Uso no Sisccon (INSERIRCONCESSAO); Inserir Aditivo/Contrato de Correspondente Bancário no Sisccon (INSERIRCOBAN)

## Grafo do fluxo
- [344468] EventoFinal "" {Responsável atual} → (fim)
- [344469] FimCancelamento "" → (fim)
- [344470] SubProcesso "Criar OC" {Responsavel Processo} → [G77952] Inserir Contrato/Ata?
- [344445] Tarefa "Informar a Pendência" {Responsável atual} → [344465] Aviso de Pendência e Ajustes
- [344446] EventoIntermediarioMensagem "Contratos fornecedores com vinculação direta ou indireta com contratos clientes" → [G77956] Anonimizar Contrato?
- [344447] SubProcesso "Análise de Garantia Contratual" {Responsável atual} → [344468] 
- [344448] SubProcesso "Publicar no site da BBTS" {Fila CSC - Contratos} → [G77958] Publicar Extrato do DOU no site da BBTS?
- [344449] Tarefa "Verificar OC
" {Responsável atual} → [344463] 5 dias | [G77965] OC em conformidade?
- [344450] LinkInicial "" → [G77962] Solicitar publicação no DOU?
- [344451] Tarefa "Verificar Solicitação
" {Fila CSC - Contratos} → [G77957] Dados OK?
- [344452] EventoIntermediarioTimer "5 dias" → [344461] Reprovação por falta de ajustes
- [344453] SubProcesso "OnBoard" {Fila CSC - Contratos} → [G77955] Atividade fim?
- [344454] SubProcesso "Publicar no Dou" {Fila CSC - Contratos} → [344451] Verificar Solicitação

- [344455] SubProcesso "Anonimizar" {Fila CSC - Contratos} → [G77966] Contrato/Aditivo do Coban?
- [344456] Tarefa "Inserir dados da Contrapartida

" {Responsável atual} → [344446] Contratos fornecedores com vinculação direta ou in
- [344458] Tarefa "Aguardar Retorno do cliente
" {Cliente} → [344452] 5 dias | [344451] Verificar Solicitação

- [344459] SubProcesso "Consulta Fisco Tributária" {Fila CSC - Contratos} → [G77959] OnBoard?
- [344457] EventoInicial "Inserir Documentos Contratuais no Sisccon" {Cliente} → [G77962] Solicitar publicação no DOU?
- [344460] Tarefa "Automática" {Responsável atual} → [344470] Criar OC
- [344461] EventoIntermediarioMensagem "Reprovação por falta de ajustes" → [344469] 
- [344462] SubProcesso "Publicar no site da BBTS" {Fila CSC - Contratos} → [G77958] Publicar Extrato do DOU no site da BBTS?
- [344463] EventoIntermediarioTimer "5 dias" → [G77967] Publicar no SIASG?

- [344464] EventoIntermediarioMensagem "Verificar" → [344449] Verificar OC

- [344465] EventoIntermediarioMensagem "Aviso de Pendência e Ajustes" → [344458] Aguardar Retorno do cliente

- [344466] SubProcesso "Publicar Extrato do DOU no site da BBTS" {Fila CSC - Contratos} → [G77954] Confeccionar OC?
- [344467] SubProcesso "Publicar no Siasg" {Responsável atual} → [G77960] Possui Garantia?
- [G77954] Gateway "Confeccionar OC?" → «Sim» [344470] Criar OC | «Não» [G77967] Publicar no SIASG?

- [G77952] Gateway "Inserir Contrato/Ata?" → «Sim» [344464] Verificar | «Não» [G77967] Publicar no SIASG?

- [G77953] Gateway "Coban?" → «Não» [344456] Inserir dados da Contrapartida

 | «Sim» [G77956] Anonimizar Contrato?
- [G77955] Gateway "Atividade fim?" → «Não» [G77956] Anonimizar Contrato? | «Sim» [G77953] Coban?
- [G77956] Gateway "Anonimizar Contrato?" → «Não» [G77961] Publicar no site da BBTS? | «Sim» [344455] Anonimizar
- [G77957] Gateway "Dados OK?" → «Sim» [G77963] Acionar Ditri?
 | «Não» [344445] Informar a Pendência
- [G77958] Gateway "Publicar Extrato do DOU no site da BBTS?" → «Sim» [344466] Publicar Extrato do DOU no site da BBTS | «Não» [G77954] Confeccionar OC?
- [G77959] Gateway "OnBoard?" → «Sim» [344453] OnBoard | «Não» [G77955] Atividade fim?
- [G77960] Gateway "Possui Garantia?" → «Sim» [344447] Análise de Garantia Contratual | «Não» [344468] 
- [G77961] Gateway "Publicar no site da BBTS?" → «Não» [G77958] Publicar Extrato do DOU no site da BBTS? | «Sim» [344462] Publicar no site da BBTS
- [G77962] Gateway "Solicitar publicação no DOU?" → «Sim» [344454] Publicar no Dou | «Não» [344451] Verificar Solicitação

- [G77963] Gateway "Acionar Ditri?
" → «Não» [G77955] Atividade fim? | «Sim» [344459] Consulta Fisco Tributária
- [G77964] Gateway "Publicar no site da BBTS?" → «Sim» [344448] Publicar no site da BBTS | «Não» [G77958] Publicar Extrato do DOU no site da BBTS?
- [G77965] Gateway "OC em conformidade?" → «Não» [344460] Automática | «Sim» [G77967] Publicar no SIASG?

- [G77966] Gateway "Contrato/Aditivo do Coban?" → «Sim» [G77954] Confeccionar OC? | «Não» [G77964] Publicar no site da BBTS?
- [G77967] Gateway "Publicar no SIASG?
" → «Sim» [344467] Publicar no Siasg | «Não» [G77960] Possui Garantia?

## Gateways
### [G77954] Confeccionar OC? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO6"] == "Sim"
```
- alternativa → [344470] Criar OC: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G77967] Publicar no SIASG?
: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77952] Inserir Contrato/Ata? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "INSERIRCONTRATO" or OrdemServico.Servico.Sigla == "INSERIRATA"
```
- alternativa → [344464] Verificar: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G77967] Publicar no SIASG?
: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77953] Coban? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "INSERIRCOBAN"
```
- alternativa → [344456] Inserir dados da Contrapartida

: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G77956] Anonimizar Contrato?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
### [G77955] Atividade fim? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
from Venki.Supravizio.Processo.Custom import Atividade
OrdemServico["TIPO_ATIVIDADE"] == "Atividade Fim"
```
- alternativa → [G77956] Anonimizar Contrato?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G77953] Coban?: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
### [G77956] Anonimizar Contrato? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "INSERIRADITIVO" or OrdemServico.Servico.Sigla == "INSERIRCONTRATO" or OrdemServico.Servico.Sigla == "INSERIRAPOSTILAMENTO"
```
- alternativa → [G77961] Publicar no site da BBTS?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
True
```
- alternativa → [344455] Anonimizar: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
False
```
### [G77957] Dados OK? (EventBasedExclusiveDecision)
Codigo=DADOS
- alternativa → [G77963] Acionar Ditri?
: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
- alternativa → [344445] Informar a Pendência: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
### [G77958] Publicar Extrato do DOU no site da BBTS? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO1"] == "Sim"
```
- alternativa → [344466] Publicar Extrato do DOU no site da BBTS: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G77954] Confeccionar OC?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77959] OnBoard? (DataBasedExclusiveDecision)
Codigo=ONBOARD2
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == 'INSERIRATA' or OrdemServico.Servico.Sigla == 'INSERIRCOMODATO' or OrdemServico.Servico.Sigla == 'INSERIRCONTRATO'
```
- alternativa → [344453] OnBoard: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G77955] Atividade fim?: SequenciaAvaliacao=2; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77960] Possui Garantia? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO"] == "Sim"
```
- alternativa → [344447] Análise de Garantia Contratual: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [344468] : SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77961] Publicar no site da BBTS? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO_INFRA"] == "Sim"
```
- alternativa → [G77958] Publicar Extrato do DOU no site da BBTS?: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [344462] Publicar no site da BBTS: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
### [G77962] Solicitar publicação no DOU? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO_PROC"] == "Sim"
```
- alternativa → [344454] Publicar no Dou: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [344451] Verificar Solicitação
: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77963] Acionar Ditri?
 (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == 'INSERIRATA' or OrdemServico.Servico.Sigla == 'INSERIRCOMODATO' or OrdemServico.Servico.Sigla == 'INSERIRCONTRATO'
```
- alternativa → [G77955] Atividade fim?: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [344459] Consulta Fisco Tributária: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
### [G77964] Publicar no site da BBTS? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO1"] == "Sim"
```
- alternativa → [344448] Publicar no site da BBTS: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G77958] Publicar Extrato do DOU no site da BBTS?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77965] OC em conformidade? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("VERIFICAROC")
```
- alternativa → [344460] Automática: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G77967] Publicar no SIASG?
: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
### [G77966] Contrato/Aditivo do Coban? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "INSERIRCOBAN"
```
- alternativa → [G77954] Confeccionar OC?: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G77964] Publicar no site da BBTS?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G77967] Publicar no SIASG?
 (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO7"] == "Sim"
```
- alternativa → [344467] Publicar no Siasg: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G77960] Possui Garantia?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [344468] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [344469] FimCancelamento ""

### [344470] SubProcesso "Criar OC"
Responsável: Responsavel Processo (papel 1378)
Config: AssociacaoId=325; PassaTodosItens=true; Configuracao={"ValidacaoFinalizacao":"Finaliza\u00e7\u00e3o da ocorr\u00eancia"}
MotivoInterrupcaoSLA: Aguardando Fim Subprocesso associado
**ScriptInicio**
```python
sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
sub.Cliente = OrdemServico.Cliente
sub.Favorecido = OrdemServico.Cliente  
sub.Salva()
sub.AvancaAtividade()
```
- ValoresInputs:
  - CustomPropertyId=1539; CustomProperty=OBS4
  - CustomPropertyId=1942; CustomProperty=NUMERO_RC
  - CustomPropertyId=2327; CustomProperty=FISICA_JUDIRICA
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=775; CustomProperty=CNPJ_FORNECEDOR
  - CustomPropertyId=1810; CustomProperty=CSC_CPF
  - CustomPropertyId=2085; CustomProperty=TIPO_SOLICITACAO_OC
  - CustomPropertyId=2086; CustomProperty=TIPO_OC_CSC
  - CustomPropertyId=1955; CustomProperty=FUNDAMENTACAO
  - CustomPropertyId=1540; CustomProperty=OBS5
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=1961; CustomProperty=URL3
  - CustomPropertyId=1953; CustomProperty=MODALIDADE_DE_CONTRATACAO
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CSCCRIAOC")
```
  - CustomPropertyId=807; CustomProperty=NUMERO_OC
  - CustomPropertyId=4959; CustomProperty=SIM_NAO200
  - CustomPropertyId=4960; CustomProperty=SIM_NAO201
  - CustomPropertyId=4962; CustomProperty=SIM_NAO203
  - CustomPropertyId=4963; CustomProperty=SIM_NAO204
  - CustomPropertyId=4810; CustomProperty=SIM_NAO_100
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Ordem de Compras; FraseInversaAssociacao=Ordem de Compras -> Inserir Documentos Contratuais no Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=INSERIRDOCUMENTOSOC; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Ordem de Compras

### [344445] Tarefa "Informar a Pendência"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - Justificativa (nativo) "Pendência (Será enviado ao solicitante)" obrigatório

### [344446] EventoIntermediarioMensagem "Contratos fornecedores com vinculação direta ou indireta com contratos clientes"
Config: ListaDestinatarios=dicoc@bbts.com.br
ModeloComunicado: Contrato com Fornecedor vinculado ao Negócio - Dicoc
Corpo do comunicado: Prezado(a),
Informamos que o Contrato DGCO OrdemServico.Customizado.DGCO_BB possui relação direta ou indireta com contratos com CLIENTE, conforme dados da(s) contrapartida(s) listado(s) abaixo: 
OrdemServico.Customizado.DADOS_CONTRATOS_C Atenciosamente,Central de Serviços
Atenciosamente,
Central de Serviços

### [344447] SubProcesso "Análise de Garantia Contratual"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=242
- ValoresInputs:
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2800; ClasseConfiguracao=Instrumento contratual com certificado de assinaturas
  - SuperClasse=Artefato; ClasseConfiguracaoId=2405; ClasseConfiguracao=Instrumento Contratual Assinado
- Associação: Ativo=true; FraseAssociacao=inserir documentos contratuais no gescon -> Análise de Garantia Contratual; FraseInversaAssociacao=Análise de Garantia Contratual -> Inserir documentos contratuais no gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=GARANTIACONTRATUAL; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Análise de Garantia Contratual

### [344448] SubProcesso "Publicar no site da BBTS"
Responsável: Fila CSC - Contratos (papel 688)
Config: ChamadaAssincrona=true; AssociacaoId=1139; Configuracao={"ExibirBotaoNovaSubprocessos":true}
- ValoresInputs:
  - CustomPropertyId=1537; CustomProperty=OBS2
  - CustomPropertyId=1087; CustomProperty=URL1
  - CustomPropertyId=1274; CustomProperty=SIM_NAO_INFRA
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "DOCUMENTOSPUBLICOS")
```
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=1962; CustomProperty=RESPONSAVEL_INFORMACAO
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2404; ClasseConfiguracao=Documento Anonimizado
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2440; ClasseConfiguracao=Matéria não certificada
  - SuperClasse=Artefato; ClasseConfiguracaoId=2398; ClasseConfiguracao=Extrato da Publicação no DOU
  - SuperClasse=Artefato; ClasseConfiguracaoId=2399; ClasseConfiguracao=Matéria Certificada
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Licitações e Contratos - Publicação site BBTS; FraseInversaAssociacao=Licitações e Contratos - Publicação site BBTS -> Inserir Documentos Contratuais no Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=PUBLICAR EXTRATO DOU; SeparadorSequencial=.; IncluirSubniveisSeparador=true | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Licitações e Contratos - Publicação BBTS

### [344449] Tarefa "Verificar OC
"
Responsável: Responsável atual (papel 36)
Config: Codigo=VERIFICAROC
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptFormCarregado**
```python
Formulario['SIM_NAO200'].Itens = 'Sim;Não'
Formulario['SIM_NAO201'].Itens = 'Sim;Não'
Formulario['SIM_NAO203'].Itens = 'Sim;Não'
Formulario['SIM_NAO204'].Itens = 'Sim;Não'
Formulario['SIM_NAO_100'].Itens = 'Sim;Não'

Formulario['SIM_NAO200'].Habilitado = True
Formulario['SIM_NAO201'].Habilitado = True
Formulario['SIM_NAO203'].Habilitado = True
Formulario['SIM_NAO204'].Habilitado = True
Formulario['SIM_NAO_100'].Habilitado = True
```
- Operação PR0002 Aprovar
  - (aprovação) SCR_TODOS_RH "Área do Contrato" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH]
  - (aprovação) FAVORECIDO_TODOS "Solicitante (Área demandante)" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - (aprovação) OBS21 "Objeto do Contrato" [Memo String(4000) → CPE_CSC.OBS21]
  - (aprovação) NUMERO_OC "Número da OC" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC]
  - (aprovação) DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
  - (aprovação) OBJETO_CONTRATO "Objeto da Contratação" [Memo String(1999) → CPE_CSC.OBJETO_CONTRATO]
  - (aprovação) NOME_FORNECEDOR "Nome do Fornecedor" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR]
  - (aprovação) SIM_NAO200 "Valores unitários e totais;" [DropDownList String → CPE_CSC.SIM_NAO200] — Obrigatoriedade=Aprovacao
  - (aprovação) SIM_NAO201 "DGCO de acordo com a contratação?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO201] — Obrigatoriedade=Aprovacao
  - (aprovação) SIM_NAO203 "Modalidade de acordo com a contratação?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO203] — Obrigatoriedade=Aprovacao
  - (aprovação) SIM_NAO204 "Tipo da ordem de compra de acordo?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO204] — Obrigatoriedade=Aprovacao
  - (aprovação) SIM_NAO_100 "Modalidade de acordo com a contratação?" [DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100] — Obrigatoriedade=Aprovacao
  - aprovador: Responsavel Processo (Unico)
- Operação PR0001 Preencher Campos
  - SIM_NAO200 "Valores unitários e totais;" [DropDownList String → CPE_CSC.SIM_NAO200] obrigatório
  - SIM_NAO201 "DGCO de acordo com a contratação?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO201] obrigatório
  - SIM_NAO203 "Modalidade de acordo com a contratação?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO203] obrigatório
  - SIM_NAO204 "Tipo da ordem de compra de acordo?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO204] obrigatório
  - SIM_NAO_100 "Condição de pagamento" [DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100] obrigatório

### [344450] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
nomefornecedor = OrdemServico.GetCustom('NOME_NOME')
OrdemServico.SetCustom('NOME_FORNECEDOR',  nomefornecedor)

dgco = OrdemServico.GetCustom('CSC_DGCO')
OrdemServico.SetCustom('DGCO_BB',  dgco)
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Solicitante (Área demandante)" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_TODOS"].Valor != "" and Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
```
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] — Configuracao={"Mascara":"00000/0000"}
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO]
  - CONTRATO_ADITIVO "Contrato ou Aditivo?" [DropDownList String → CPE_CONTRATOS.CONTRATO_ADITIVO]
  - TIPO_ATIVIDADE "Tipo de Atividade - informe" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE]
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
#if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
#    Formulario['INFORMATIVO_CESEC'].Habilitado = True
#    Formulario['INFORMATIVO_CESEC'].Visivel = True
#    Formulario['DADOS_CONTRATOS_C'].Habilitado = True
#    Formulario['DADOS_CONTRATOS_C'].Visivel = True
#
#if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
#    Formulario['INFORMATIVO_CESEC'].Habilitado = False
#    Formulario['INFORMATIVO_CESEC'].Visivel = False
#    Formulario['DADOS_CONTRATOS_C'].Habilitado = False
#    Formulario['DADOS_CONTRATOS_C'].Visivel = False
```
  - CATEGORIA_DE_COMPRA "Categoria de Compra" [DropDownList String → CPE_CSC.CATEGORIA_DE_COMPRA]
  - MODALIDADE_DE_CONTRATACAO "Modalidade de Contratação" [DropDownList String → CPE_CONTRATOS.MODALIDADE_DE_CONTRATACAO]
  - FUNDAMENTACAO "Fundamentação Legal" [DropDownList String → CPE_CSC.FUNDAMENTACAO]
  - DIRETORIA_GERENCIA "Diretoria/Gerência - Inserir no formato Xxxxx/Xxxxx - Ex: Diafi/Gesap" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO]
  - RESPONSAVEL_PROCESSO "Responsável pela Condução do Processo" [DropDownList String → CPE_CSC.RESPONSAVEL_PROCESSO]
  - DataInicioPrevisto (nativo) "Data da Assinatura do Documento Contratual"
  - DescricaoDetalhada (nativo)
    - coluna CONDICAO_USO obrigatório
    - coluna NUMERO_PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
  - NOME_FORNECEDOR "Nome do Fornecedor" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR]
    - coluna CNPJ obrigatório
**NOME_FORNECEDOR.CNPJ.ScriptModificado**
```python
#FormularioRegistro["CNPJ"].Itens = "42.318.949/0069-72;42.318.949/0063-87;42.318.949/0015-80;42.318.949/0006-99;42.318.949/0016-60;42.318.949/0013-18;42.318.949/0017-41;42.318.949/0069-72;42.318.949/0037-95;42.318.949/0044-14;42.318.949/0005-08;42.318.949/0009-31;42.318.949/0019-03;42.318.949/0020-47;42.318.949/0061-15;42.318.949/0064-68;42.318.949/0012-37;42.318.949/0051-43;42.318.949/0027-13;42.318.949/0030-19;42.318.949/0023-90;42.318.949/0011-56;42.318.949/0071-97;42.318.949/0013-18;42.318.949/0068-91;42.318.949/0004-27;42.318.949/0008-50;42.318.949/0001-84;42.318.949/0010-75;42.318.949/0007-70;42.318.949/0054-96;42.318.949/0004-27;42.318.949/0033-61;42.318.949/0029-85;42.318.949/0031-08;42.318.949/0005-08;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0008-50;42.318.949/0069-72;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0069-72;42.318.949/0004-27"
```
    - coluna BBTS obrigatório
**NOME_FORNECEDOR.BBTS.ScriptModificado**
```python
if FormularioRegistro["BBTS"].Valor == "BB TECNOLOGIA E SERVIÇOS S.A":
    FormularioRegistro["CNPJ"].Itens = "42.318.949/0069-72;42.318.949/0063-87;42.318.949/0015-80;42.318.949/0006-99;42.318.949/0016-60;42.318.949/0013-18;42.318.949/0017-41;42.318.949/0069-72;42.318.949/0037-95;42.318.949/0044-14;42.318.949/0005-08;42.318.949/0009-31;42.318.949/0019-03;42.318.949/0020-47;42.318.949/0061-15;42.318.949/0064-68;42.318.949/0012-37;42.318.949/0051-43;42.318.949/0027-13;42.318.949/0030-19;42.318.949/0023-90;42.318.949/0011-56;42.318.949/0071-97;42.318.949/0013-18;42.318.949/0068-91;42.318.949/0004-27;42.318.949/0008-50;42.318.949/0001-84;42.318.949/0010-75;42.318.949/0007-70;42.318.949/0054-96;42.318.949/0004-27;42.318.949/0033-61;42.318.949/0029-85;42.318.949/0031-08;42.318.949/0005-08;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0008-50;42.318.949/0069-72;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0069-72;42.318.949/0004-27"
```
    - coluna DESCRICAO obrigatório
  - NOME_NOME "Nome do Fornecedor" [TextBox String(100) → CPE_PESSOAS.NOME_NOME] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=ANEXOS_GESCON
  - anexo "Instrumento Contratual Assinado" classes: Instrumento Contratual Assinado — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Associação de subprocesso: AssociacaoId=965; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Cadastros Correspondente Bancário -> Inserir Documentos Contratuais no Gescon

### [344451] Tarefa "Verificar Solicitação
"
Responsável: Fila CSC - Contratos (papel 688)
Config: Codigo=ANALISAR; ConfirmaResponsabilidade=true; PermiteCancelamentoAA=true
**ScriptFormCarregado**
```python
Formulario['SIM_NAO'].Habilitado = False
Formulario['SIM_NAO'].Visivel = False
Formulario['TOMADOR'].Habilitado = False
Formulario['TOMADOR'].Visivel = False
Formulario['PORCENTAGEM_AMOSTRA'].Habilitado = False
Formulario['PORCENTAGEM_AMOSTRA'].Visivel = False
Formulario['RETORNO_HORA'].Habilitado = False
Formulario['RETORNO_HORA'].Visivel = False
Formulario['VALOR_CONTRATADO'].Habilitado = False
Formulario['VALOR_CONTRATADO'].Visivel = False
Formulario['CNPJ_FORNECEDOR'].Habilitado = False
Formulario['CNPJ_FORNECEDOR'].Visivel = False
Formulario['COMBOBOX2'].Habilitado = False
Formulario['COMBOBOX2'].Visivel = False
Formulario['SIM_NAO_INFRA'].Habilitado = False
Formulario['SIM_NAO_INFRA'].Visivel = False


if (OrdemServico.Servico.Sigla == "INSERIRCONTRATO"):
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['TOMADOR'].Habilitado = True
    Formulario['TOMADOR'].Visivel = True
    Formulario['CNPJ_FORNECEDOR'].Habilitado = True
    Formulario['CNPJ_FORNECEDOR'].Visivel = True
    Formulario['COMBOBOX2'].Habilitado = True
    Formulario['COMBOBOX2'].Visivel = True
    Formulario['COMBOBOX2'].Itens = "Contratação de Serviço;Aquisição de Bem/Produto"
    if Formulario["SIM_NAO"].Valor == "Sim":
        Formulario['PORCENTAGEM_AMOSTRA'].Habilitado = True
        Formulario['PORCENTAGEM_AMOSTRA'].Visivel = True
        Formulario['RETORNO_HORA'].Habilitado = True
        Formulario['RETORNO_HORA'].Visivel = True
        Formulario['VALOR_CONTRATADO'].Habilitado = True
        Formulario['VALOR_CONTRATADO'].Visivel = True



    
if (OrdemServico.Servico.Sigla == "INSERIRATA"):
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['TOMADOR'].Habilitado = True
    Formulario['TOMADOR'].Visivel = True
    Formulario['CNPJ_FORNECEDOR'].Habilitado = True
    Formulario['CNPJ_FORNECEDOR'].Visivel = True
    Formulario['COMBOBOX2'].Habilitado = True
    Formulario['COMBOBOX2'].Visivel = True
    Formulario['COMBOBOX2'].Itens = "Contratação de Serviço;Aquisição de Bem/Produto"
    if Formulario["SIM_NAO"].Valor == "Sim":
        Formulario['PORCENTAGEM_AMOSTRA'].Habilitado = True
        Formulario['PORCENTAGEM_AMOSTRA'].Visivel = True
        Formulario['RETORNO_HORA'].Habilitado = True
        Formulario['RETORNO_HORA'].Visivel = True
        Formulario['VALOR_CONTRATADO'].Habilitado = True
        Formulario['VALOR_CONTRATADO'].Visivel = True


    

if (OrdemServico.Servico.Sigla == "INSERIRADITIVO"):
    #Formulario['SIM_NAO_INFRA'].Habilitado = True
    #Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['TOMADOR'].Habilitado = True
    Formulario['TOMADOR'].Visivel = True
    Formulario['CNPJ_FORNECEDOR'].Habilitado = True
    Formulario['CNPJ_FORNECEDOR'].Visivel = True
    Formulario['COMBOBOX2'].Habilitado = True
    Formulario['COMBOBOX2'].Visivel = True
    Formulario['COMBOBOX2'].Itens = "Contratação de Serviço;Aquisição de Bem/Produto"
    if Formulario["SIM_NAO"].Valor == "Sim":
        Formulario['PORCENTAGEM_AMOSTRA'].Habilitado = True
        Formulario['PORCENTAGEM_AMOSTRA'].Visivel = True
        Formulario['RETORNO_HORA'].Habilitado = True
        Formulario['RETORNO_HORA'].Visivel = True
        Formulario['VALOR_CONTRATADO'].Habilitado = True
        Formulario['VALOR_CONTRATADO'].Visivel = True
```
- Operação PR0001 Preencher Campos
  - RETORNO_HORA "Prazo da Garantia (Ex: 20 Dias)" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] obrigatório — Configuracao={"Mascara":""}
  - PORCENTAGEM_AMOSTRA "Percentual da Garantia" [TextBox String → CPE_NEGOCIOS.PORCENTAGEM_AMOSTRA] obrigatório — Configuracao={"Mascara":"00%"}
  - CNPJ_FORNECEDOR "CNPJ do Fornecedor" [TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR] obrigatório — Configuracao={"Mascara":"00,000,000/0000-00"}
  - TOMADOR "TOMADOR" [DataGrid RecordList → Z_00143_TOMADOR.TOMADOR] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna FATURA_CNPJ obrigatório
**TOMADOR.FATURA_CNPJ.ScriptModificado**
```python
if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0069-72":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA ANDARAÍ"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0063-87":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA BARUERI"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0015-80":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA BAURU"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0006-99":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA BELO HORIZONTE"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0016-60":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA BELÉM"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA BRASÍLIA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0017-41":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA CAMPINAS"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0069-72":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA CARIOCA - RJ"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0037-95":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA CAMPO GRANDE"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0044-14":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA CUIABÁ"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0005-08":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA CURITIBA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0009-31":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA FLORIANÓPOLIS"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0019-03":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA FORTALEZA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0020-47":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA GOIÂNIA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0061-15":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA JOINVILLE"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0064-68":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA JOÃO PESSOA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0012-37":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA LONDRINA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0051-43":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA MACEIÓ"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0027-13":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA MANAUS"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0030-19":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA NATAL"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0023-90":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA PASSO FUNDO"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0011-56":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA PORTO ALEGRE"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0071-97":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA PALMAS"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA PLANO PILOTO"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0068-91":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA PORTO VELHO"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0004-27":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA PAULISTA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0008-50":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA RECIFE"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0001-84":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA RIO DE JANEIRO"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0010-75":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA RIBEIRÃO PRETO"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0007-70":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA SALVADOR"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0054-96":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA SÃO LUIZ"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0004-27":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA SÃO PAULO"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0033-61":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA TERESINA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0029-85":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA UBERLÂNDIA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0031-08":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA VITÓRIA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0005-08":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE MONITORAMENTO DE AUTOATENDIMENTO - CURITIBA"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0004-27":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE MONITORAMENTO DE AUTOATENDIMENTO - SÃO PAULO"

#if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
#    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE SUSTENTAÇÃO DE INFRAESTRUTURA DE DATA CENTER"
#
#if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
#    FormularioRegistro['DESC_CNPJ'].Valor = "COORDENAÇÃO DE MONITORAMENTO"
#
#if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
#    FormularioRegistro['DESC_CNPJ'].Valor = "DIVISÃO DE ORGANIZAÇÃO E APOIO À REDE DE SERVIÇOS"
#
#if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
#    FormularioRegistro['DESC_CNPJ'].Valor = "DIVISÃO DE SERVIÇOS DE ASSISTÊNCIA TÉCNICA E OUTSOURCING"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0008-50":
    FormularioRegistro['DESC_CNPJ'].Valor = "GERÊNCIA DE REDE DE SERVIÇOS"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0069-72":
    FormularioRegistro['DESC_CNPJ'].Valor = "GERENCIA REGIONAL NORDESTE"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0004-27":
    FormularioRegistro['DESC_CNPJ'].Valor = "GERENCIA REGIONAL NORTE"

#if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
#    FormularioRegistro['DESC_CNPJ'].Valor = "GERENCIA REGIONAL SÃO PAULO"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0069-72":
    FormularioRegistro['DESC_CNPJ'].Valor = "SUPERINTENDÊNCIA CENTRO NORTE"

if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0004-27":
    FormularioRegistro['DESC_CNPJ'].Valor = "SUPERINTENDÊNCIA NORDESTE"
    
if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0018-22":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA CASCAVEL"
    
if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0075-10":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ATENDIMENTO SALVADOR"
    
if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0073-59":
    FormularioRegistro['DESC_CNPJ'].Valor = "ESTOQUE CENTRAL"
    
if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0074-30":
    FormularioRegistro['DESC_CNPJ'].Valor = "CENTRO DE ASSISTÊNCIA TÉCNICA BARUERI"
    
if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0036-04":
    FormularioRegistro['DESC_CNPJ'].Valor = "CEDOC PIRAI/RJ"

#if FormularioRegistro['FATURA_CNPJ'].Valor == "42.318.949/0013-18":
#    FormularioRegistro['DESC_CNPJ'].Valor = "SUPERINTENDÊNCIA SÃO PAULO"
```
    - coluna CNPJ obrigatório
    - coluna DESC_CNPJ obrigatório
    - coluna BBTS obrigatório
**TOMADOR.BBTS.ScriptModificado**
```python
if FormularioRegistro["BBTS"].Valor == "BB TECNOLOGIA E SERVIÇOS S.A.":
    FormularioRegistro["CNPJ"].Itens = "42.318.949/0069-72;42.318.949/0063-87;42.318.949/0015-80;42.318.949/0006-99;42.318.949/0016-60;42.318.949/0013-18;42.318.949/0017-41;42.318.949/0069-72;42.318.949/0037-95;42.318.949/0044-14;42.318.949/0005-08;42.318.949/0009-31;42.318.949/0019-03;42.318.949/0020-47;42.318.949/0061-15;42.318.949/0064-68;42.318.949/0012-37;42.318.949/0051-43;42.318.949/0027-13;42.318.949/0030-19;42.318.949/0023-90;42.318.949/0011-56;42.318.949/0071-97;42.318.949/0013-18;42.318.949/0068-91;42.318.949/0004-27;42.318.949/0008-50;42.318.949/0001-84;42.318.949/0010-75;42.318.949/0007-70;42.318.949/0054-96;42.318.949/0004-27;42.318.949/0033-61;42.318.949/0029-85;42.318.949/0031-08;42.318.949/0005-08;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0008-50;42.318.949/0069-72;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0069-72;42.318.949/0004-27"
    FormularioRegistro["FATURA_CNPJ"].Itens = "42.318.949/0069-72;42.318.949/0063-87;42.318.949/0015-80;42.318.949/0006-99;42.318.949/0016-60;42.318.949/0013-18;42.318.949/0017-41;42.318.949/0069-72;42.318.949/0037-95;42.318.949/0044-14;42.318.949/0005-08;42.318.949/0009-31;42.318.949/0019-03;42.318.949/0020-47;42.318.949/0061-15;42.318.949/0064-68;42.318.949/0012-37;42.318.949/0051-43;42.318.949/0027-13;42.318.949/0030-19;42.318.949/0023-90;42.318.949/0011-56;42.318.949/0071-97;42.318.949/0013-18;42.318.949/0068-91;42.318.949/0004-27;42.318.949/0008-50;42.318.949/0001-84;42.318.949/0010-75;42.318.949/0007-70;42.318.949/0054-96;42.318.949/0004-27;42.318.949/0033-61;42.318.949/0029-85;42.318.949/0031-08;42.318.949/0005-08;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0008-50;42.318.949/0069-72;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0069-72;42.318.949/0004-27;42.318.949/0018-22;42.318.949/0075-10;42.318.949/0073-59;42.318.949/0074-30;42.318.949/0036-04"
    FormularioRegistro["DESC_CNPJ"].Itens = "CENTRO DE ASSISTÊNCIA TÉCNICA ANDARAÍ;CENTRO DE ASSISTÊNCIA TÉCNICA BARUERI;CENTRO DE ASSISTÊNCIA TÉCNICA BAURU;CENTRO DE ASSISTÊNCIA TÉCNICA BELO HORIZONTE;CENTRO DE ASSISTÊNCIA TÉCNICA BELÉM;CENTRO DE ASSISTÊNCIA TÉCNICA BRASÍLIA;CENTRO DE ASSISTÊNCIA TÉCNICA CAMPINAS;CENTRO DE ASSISTÊNCIA TÉCNICA CARIOCA - RJ;CENTRO DE ASSISTÊNCIA TÉCNICA CAMPO GRANDE;CENTRO DE ASSISTÊNCIA TÉCNICA CUIABÁ;CENTRO DE ASSISTÊNCIA TÉCNICA CURITIBA;CENTRO DE ASSISTÊNCIA TÉCNICA FLORIANÓPOLIS;CENTRO DE ASSISTÊNCIA TÉCNICA FORTALEZA;CENTRO DE ASSISTÊNCIA TÉCNICA GOIÂNIA;CENTRO DE ASSISTÊNCIA TÉCNICA JOINVILLE;CENTRO DE ASSISTÊNCIA TÉCNICA JOÃO PESSOA;CENTRO DE ASSISTÊNCIA TÉCNICA LONDRINA;CENTRO DE ASSISTÊNCIA TÉCNICA MACEIÓ;CENTRO DE ASSISTÊNCIA TÉCNICA MANAUS;CENTRO DE ASSISTÊNCIA TÉCNICA NATAL;CENTRO DE ASSISTÊNCIA TÉCNICA PASSO FUNDO;CENTRO DE ASSISTÊNCIA TÉCNICA PORTO ALEGRE;CENTRO DE ASSISTÊNCIA TÉCNICA PALMAS;CENTRO DE ASSISTÊNCIA TÉCNICA PLANO PILOTO;CENTRO DE ASSISTÊNCIA TÉCNICA PORTO VELHO;CENTRO DE ASSISTÊNCIA TÉCNICA PAULISTA;CENTRO DE ASSISTÊNCIA TÉCNICA RECIFE;CENTRO DE ASSISTÊNCIA TÉCNICA RIO DE JANEIRO;CENTRO DE ASSISTÊNCIA TÉCNICA RIBEIRÃO PRETO;CENTRO DE ASSISTÊNCIA TÉCNICA SALVADOR;CENTRO DE ASSISTÊNCIA TÉCNICA SÃO LUIZ;CENTRO DE ASSISTÊNCIA TÉCNICA SÃO PAULO;CENTRO DE ASSISTÊNCIA TÉCNICA TERESINA;CENTRO DE ASSISTÊNCIA TÉCNICA UBERLÂNDIA;CENTRO DE ASSISTÊNCIA TÉCNICA VITÓRIA;CENTRO DE MONITORAMENTO DE AUTOATENDIMENTO - CURITIBA;CENTRO DE MONITORAMENTO DE AUTOATENDIMENTO - SÃO PAULO;CENTRO DE SUSTENTAÇÃO DE INFRAESTRUTURA DE DATA CENTER;COORDENAÇÃO DE MONITORAMENTO;DIVISÃO DE ORGANIZAÇÃO E APOIO À REDE DE SERVIÇOS;DIVISÃO DE SERVIÇOS DE ASSISTÊNCIA TÉCNICA E OUTSOURCING;GERÊNCIA DE REDE DE SERVIÇOS;GERENCIA REGIONAL CENTRO OESTE;GERENCIA REGIONAL NORDESTE;GERENCIA REGIONAL NORTE;GERENCIA REGIONAL SUDESTE;GERENCIA REGIONAL SÃO PAULO;GERENCIA REGIONAL SUL;SUPERINTENDÊNCIA CENTRO NORTE;SUPERINTENDÊNCIA NORDESTE;SUPERINTENDÊNCIA SUDESTE;SUPERINTENDÊNCIA SÃO PAULO;SUPERINTENDÊNCIA SUL;CENTRO DE ASSISTÊNCIA TÉCNICA CASCAVEL;CENTRO DE ATENDIMENTO SALVADOR;ESTOQUE CENTRAL;CENTRO DE ASSISTÊNCIA TÉCNICA BARUERI;CEDOC PIRAI/RJ"
```
  - VALOR_CONTRATADO "Valor da Garantia (Ex: 1.000.000,00)" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_CONTRATADO] obrigatório — Configuracao={"Mascara":""}
  - COMBOBOX2 "A solicitação é para Contratação de Serviço ou Aquisição de Bem/Produto?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2] obrigatório
  - SIM_NAO_INFRA "Publicar Instrumento Contratual no site da BBTS?" [DropDownList String → CPE_ORDEM_SERVICO.SIM_NAO_INFRA] obrigatório
  - SIM_NAO "Contrato Possui Garantia?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório

### [344452] EventoIntermediarioTimer "5 dias"
Config: Codigo=CINCO_DIAS; TempoIntervalo=7200; MaximoExecucao=1
**ScriptEvento**
```python
OrdemServico.AvancaAtividade()
```

### [344453] SubProcesso "OnBoard"
Responsável: Fila CSC - Contratos (papel 688)
Config: ChamadaAssincrona=true; AssociacaoId=1200; Configuracao={"ExibirBotaoNovaSubprocessos":true}
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - CustomPropertyId=1075; CustomProperty=DATA1
  - CustomPropertyId=510; CustomProperty=FAVORECIDO_TODOS
  - CustomPropertyId=2768; CustomProperty=CONTRATO_ADITIVO
  - CustomPropertyId=1969; CustomProperty=TIPO_ATIVIDADE
  - CustomPropertyId=1972; CustomProperty=FISCAL_SER
  - CustomPropertyId=1974; CustomProperty=FISCAL_MASTER
  - CustomPropertyId=1975; CustomProperty=GESTOR_CONTRATO
  - CustomPropertyId=2290; CustomProperty=SIM_NAO5
  - CustomPropertyId=1976; CustomProperty=CATEGORIA_DE_COMPRA
  - CustomPropertyId=1953; CustomProperty=MODALIDADE_DE_CONTRATACAO
  - CustomPropertyId=1955; CustomProperty=FUNDAMENTACAO
  - CustomPropertyId=1042; CustomProperty=TIPO_DOCUMENTO
  - CustomPropertyId=810; CustomProperty=VALOR_REF_CONT
  - CustomPropertyId=709; CustomProperty=VALOR
  - CustomPropertyId=1272; CustomProperty=SIM_NAO_PROC
  - CustomPropertyId=2385; CustomProperty=SIM_NAO7
  - CustomPropertyId=1274; CustomProperty=SIM_NAO_INFRA
  - CustomPropertyId=1537; CustomProperty=OBS2
  - CustomPropertyId=1087; CustomProperty=URL1
  - CustomPropertyId=1977; CustomProperty=SIM_NAO1
  - CustomPropertyId=1536; CustomProperty=OBS1
  - CustomPropertyId=1959; CustomProperty=URL2
  - CustomPropertyId=1962; CustomProperty=RESPONSAVEL_INFORMACAO
  - CustomPropertyId=1963; CustomProperty=DIRETORIA_GERENCIA
  - CustomPropertyId=610; CustomProperty=PPGEREX_NEGOCIO
  - CustomPropertyId=1958; CustomProperty=RESPONSAVEL_PROCESSO
  - PropertyId=1268; Property=DataHoraInicioPrevisto
  - CustomPropertyId=2289; CustomProperty=SIM_NAO4
  - CustomPropertyId=1961; CustomProperty=URL3
  - PropertyId=1223; Property=DescricaoDetalhada
  - CustomPropertyId=1061; CustomProperty=LABEL1
  - CustomPropertyId=2163; CustomProperty=OBJETO_CONTRATO
  - CustomPropertyId=755; CustomProperty=RESUMO
  - CustomPropertyId=768; CustomProperty=DATA_ENCERRA
  - CustomPropertyId=1357; CustomProperty=CSC_DATA_INICIO
  - CustomPropertyId=1358; CustomProperty=CSC_DATA_FIM
  - CustomPropertyId=1965; CustomProperty=SIM_NAO3
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=2581; CustomProperty=OBS21
  - CustomPropertyId=775; CustomProperty=CNPJ_FORNECEDOR
  - CustomPropertyId=578; CustomProperty=SCR_TODOS_RH
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2800; ClasseConfiguracao=Instrumento contratual com certificado de assinaturas
  - SuperClasse=Artefato; ClasseConfiguracaoId=2405; ClasseConfiguracao=Instrumento Contratual Assinado
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos --> Onboard; FraseInversaAssociacao=Onboard --> Inserir Documentos; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ONBOARDGESC; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: OnBoard

### [344454] SubProcesso "Publicar no Dou"
Responsável: Fila CSC - Contratos (papel 688)
Config: ChamadaAssincrona=true; AssociacaoId=386; Codigo=PUBLICAR_DOU; RetornaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":false}
MotivoInterrupcaoSLA: Aguardando Fim Subprocesso associado
- ValoresInputs:
  - CustomPropertyId=1075; CustomProperty=DATA1
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "PUBLIDOU")
```
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=1061; CustomProperty=LABEL1
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2318; ClasseConfiguracao=RTF
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2440; ClasseConfiguracao=Matéria não certificada
  - SuperClasse=Artefato; ClasseConfiguracaoId=2398; ClasseConfiguracao=Extrato da Publicação no DOU
  - SuperClasse=Artefato; ClasseConfiguracaoId=2399; ClasseConfiguracao=Matéria Certificada
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Publicação no DOU; FraseInversaAssociacao=Publicação no DOU -> Inserir Documentos Contratuais no Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=INSERIRDOU; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Publicação no DOU

### [344455] SubProcesso "Anonimizar"
Responsável: Fila CSC - Contratos (papel 688)
Config: ChamadaAssincrona=true; AssociacaoId=362
- ValoresInputs:
  - CustomPropertyId=1042; CustomProperty=TIPO_DOCUMENTO
  - CustomPropertyId=2290; CustomProperty=SIM_NAO5
  - CustomPropertyId=1274; CustomProperty=SIM_NAO_INFRA
  - CustomPropertyId=1087; CustomProperty=URL1
  - CustomPropertyId=1537; CustomProperty=OBS2
  - CustomPropertyId=1962; CustomProperty=RESPONSAVEL_INFORMACAO
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "SRVANONIMIZACAODDPSSAIS")
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2405; ClasseConfiguracao=Instrumento Contratual Assinado
  - SuperClasse=Artefato; ClasseConfiguracaoId=2399; ClasseConfiguracao=Matéria Certificada
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2404; ClasseConfiguracao=Documento Anonimizado
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Anonimização de Dados Pessoais; FraseInversaAssociacao=Anonimização de Dados Pessoais -> Inserir Documentos Contratuais no Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ANONIMIZACAOGESCON; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Anonimização de Dados Pessoais

### [344456] Tarefa "Inserir dados da Contrapartida

"
Responsável: Responsável atual (papel 36)
**ScriptFim**
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

# Token de autenticação
token = '***MASCARADO***'

# URL da API
url = 'https://sisccon.bbts.com.br/supravizio/supra/relaciona-fornecedor'

os = OrdemServico.Numero

# Executa a query
query = DB.ExecuteDataTable(
    "Select OCORRENCIA.NUMERO As OS, OCORRENCIA.ASSUNTO As ASSUNTO, CPE_FINANCEIRO.DGCO_BB As DGFORNECEDOR, "
    "Z_00143_DADOS_CONTRATOS_C.NOME_CLIENTE, Z_00143_DADOS_CONTRATOS_C.DGCO, Z_00143_DADOS_CONTRATOS_C.VALOR, "
    "Z_00143_DADOS_CONTRATOS_C.RUBRICA From CPE_FINANCEIRO Inner Join OCORRENCIA On OCORRENCIA.ID_OCORRENCIA = "
    "CPE_FINANCEIRO.ID_OCORRENCIA Inner Join Z_00143_DADOS_CONTRATOS_C On OCORRENCIA.ID_OCORRENCIA = "
    "Z_00143_DADOS_CONTRATOS_C.ID_OCORRENCIA WHERE OCORRENCIA.NUMERO = '" + os + "'"
)

# Cria uma lista para armazenar os dados combinados
data = []

# Itera sobre os resultados da consulta
for row in query.Rows:
    cliente = {
        'dgco_bb': row["DGFORNECEDOR"],
        'nome_cliente': row["NOME_CLIENTE"],
        'dgco': row["DGCO"],
        'valor': row["VALOR"],
        'rubrica': row["RUBRICA"]
    }
    data.append(cliente)

# Serializa os dados para JSON
dados_json = JsonConvert.SerializeObject(data)

# Cria o StringContent com o JSON serializado       
dados = StringContent(dados_json, Encoding.UTF8, "application/json")

# Inicializa o HttpClient e configura os cabeçalhos
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Clear()
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

# Envia a requisição POST com os dados
response = client.PostAsync(url, dados)
response.Wait()

# Verifica o código de status da resposta
if response.Result.IsSuccessStatusCode:
    resultAsync = response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    OrdemServico.AdicionaComentario(result, True)
else:
    error_message = response.Result.Content.ReadAsStringAsync().Result
    OrdemServico.AdicionaComentario("Erro: " + str(response.Result.StatusCode) + " - " + error_message, True)
```
- Operação PR0001 Preencher Campos
  - INFORMATIVO_CESEC "DADOS DA CONTRAPARTIDA: A presente contratação possui relação direta ou indireta com contratos com CLIENTE, relacione abaixo os DGCOs de contrapartida conforme informados no Projeto Básico." [Label String(1500) → CPE_CSC.INFORMATIVO_CESEC]
  - DADOS_CONTRATOS_C "Contrato Clientes" [DataGrid RecordList → Z_00143_DADOS_CONTRATOS_C.DADOS_CONTRATOS_C] obrigatório
    - coluna VALOR obrigatório
    - coluna NOME_CLIENTE obrigatório
    - coluna RUBRICA obrigatório
    - coluna DGCO obrigatório

### [344458] Tarefa "Aguardar Retorno do cliente
"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Atividade
Formulario['TIPO_ATIVIDADE'].Visivel = False
Formulario['DGCO_BB'].Visivel = False
##Formulario['INFORMATIVO_CESEC'].Visivel = False
##Formulario['DADOS_CONTRATOS_C'].Visivel = False
Formulario['FISCAL_SER'].Visivel = False
Formulario['FISCAL_MASTER'].Visivel = False
Formulario['GESTOR_CONTRATO'].Visivel = False
Formulario['SIM_NAO'].Visivel = False
Formulario['SIM_NAO_INFRA'].Visivel = False
Formulario['SIM_NAO_PROC'].Visivel = False
Formulario['RESPONSAVEL_PROCESSO'].Visivel = False
Formulario['PPGEREX_NEGOCIO'].Visivel = False
Formulario['DIRETORIA_GERENCIA'].Visivel = False
Formulario['OBS2'].Visivel = False
Formulario['RESPONSAVEL_INFORMACAO'].Visivel = False
Formulario['SIM_NAO1'].Visivel = False
Formulario['LABEL1'].Visivel = False
Formulario['URL1'].Visivel = False
Formulario['URL2'].Visivel = False
Formulario['OBS1'].Visivel = False
#Formulario['URL3'].Visivel = False
#Formulario['SIM_NAO2'].Visivel = False
Formulario['SIM_NAO3'].Visivel = False
Formulario['CATEGORIA_DE_COMPRA'].Visivel = False
Formulario['SIM_NAO4'].Visivel = False
Formulario['FUNDAMENTACAO'].Visivel = False
Formulario['SIM_NAO5'].Visivel = False
Formulario['DATA1'].Visivel = False
Formulario['FUNDAMENTACAO'].Visivel = False
Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = False
Formulario['NOME_FORNECEDOR'].Visivel = False
Formulario['OBJETO_CONTRATO'].Visivel = False
Formulario['NUMERO_OC'].Visivel = False
Formulario['CSC_DATA_INICIO'].Visivel = False
Formulario['CSC_DATA_FIM'].Visivel = False
Formulario['VALOR'].Visivel = False
Formulario['SIM_NAO6'].Visivel = False
Formulario['SIM_NAO7'].Visivel = False
Formulario['CONTRATO_ADITIVO'].Visivel = False
Formulario['CONTRATO_ADITIVO'].Habilitado = False
Formulario['URL3'].Habilitado = False
Formulario['URL3'].Visivel = False
##Formulario['MODALIDADE_LICITACAO'].Habilitado = False
##Formulario['MODALIDADE_LICITACAO'].Visivel = False
Formulario['FUNDAMENTACAO'].Habilitado = False
Formulario['FUNDAMENTACAO'].Visivel = False


Formulario['NUMERO_OC'].Visivel = False
Formulario['NUMERO_RC'].Visivel = False    
Formulario['NOME_FORNECEDOR'].Visivel = False
Formulario['CNPJ_FORNECEDOR'].Visivel = False
Formulario['CSC_CPF'].Visivel = False    
Formulario['TIPO_SOLICITACAO_OC'].Visivel = False
Formulario['TIPO_OC_CSC'].Visivel = False
##Formulario['MODALIDADE_LICITACAO'].Visivel = False
Formulario['FISICA_JUDIRICA'].Visivel = False
Formulario['OBS5'].Visivel = False
Formulario["TIPO_DOCUMENTO"].Habilitado = False



##Campos obrigatórios para Inserir aditivos de fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRADITIVO"):
#Formulario['INFORMAR_DOCUMENTO'].Valor == "Aditivo":
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = False
    Formulario['FISCAL_SER'].Visivel = False
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = False
    Formulario['GESTOR_CONTRATO'].Visivel = False
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True   
    Formulario['DIRETORIA_GERENCIA'].Habilitado = False
    Formulario['DIRETORIA_GERENCIA'].Visivel = False
    Formulario['PPGEREX_NEGOCIO'].Habilitado = False
    Formulario['PPGEREX_NEGOCIO'].Visivel = False
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = False
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = False
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False  
    Formulario['SIM_NAO3'].Visivel = False
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = False
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = True
    Formulario['SIM_NAO7'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Aditivo"
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False

    
    
##Campos obrigatórios para Inserir atas de registros de preços com fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRATA"):    
#if Formulario['INFORMAR_DOCUMENTO'].Valor == "Ata de Registro de Preço":
    Formulario['TIPO_ATIVIDADE'].Habilitado = True
    Formulario['TIPO_ATIVIDADE'].Visivel = True
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = True
    Formulario['FISCAL_MASTER'].Visivel = True
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True  
##    Formulario['SIM_NAO2'].Visivel = True
##    Formulario['SIM_NAO2'].Habilitado = True 
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = True
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = True
    Formulario["CATEGORIA_DE_COMPRA"].Itens = "ATA DE REGISTRO DE PREÇOS/FORNECIMENTO DE BENS/EQUIPAMENTOS/PEÇAS;ATA DE REGISTRO DE PREÇOS/SERVIÇOS"
    Formulario['SIM_NAO4'].Visivel = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = False
    Formulario['SIM_NAO7'].Habilitado = False
    Formulario["TIPO_DOCUMENTO"].Valor = "Ata de Registro de Preço"
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Valor = "LEI N° 13.303/2016, ART. 28 C/C ART. 32, INCISO IV"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "LICITAÇÃO ELETRÔNICA"
    
    
##Campos obrigatórios para Inserir apostilamento de fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRAPOSTILAMENTO"):
#if Formulario['INFORMAR_DOCUMENTO'].Valor == 'Apostilamento':
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = False
    Formulario['FISCAL_SER'].Visivel = False
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = False
    Formulario['GESTOR_CONTRATO'].Visivel = False
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['DIRETORIA_GERENCIA'].Habilitado = False
    Formulario['DIRETORIA_GERENCIA'].Visivel = False
    Formulario['PPGEREX_NEGOCIO'].Habilitado = False
    Formulario['PPGEREX_NEGOCIO'].Visivel = False
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = False
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True   
##    Formulario['SIM_NAO2'].Visivel = True
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = False
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = False
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False 
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = True
    Formulario['SIM_NAO7'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Apostilamento"
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    
##Campos obrigatórios para Inserir contratos de fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONTRATO"):
#if Formulario['INFORMAR_DOCUMENTO'].Valor == "Contrato":
    Formulario['TIPO_ATIVIDADE'].Habilitado = True
    Formulario['TIPO_ATIVIDADE'].Visivel = True
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = True
    Formulario['FISCAL_MASTER'].Visivel = True
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = True
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = True
    Formulario["CATEGORIA_DE_COMPRA"].Itens = "CREDENCIAMENTO/ENRIQUECIMENTO DE BASE;CREDENCIAMENTO/FORNECIMENTO DE BENS/EQUIPAMENTOS/PEÇAS;CREDENCIAMENTO/REPARO DE PARTES E PEÇAS;CREDENCIAMENTO/SERVIÇOS;CREDENCIAMENTO/TRANSPORTE;CREDENCIAMENTO/TELEFONIA;CREDENCIAMENTO/OUTROS;FORNECIMENTO DE BENS/AQUISIÇÃO DE MOBILIÁRIO;FORNECIMENTO DE BENS/INFORMÁTICA;FORNECIMENTO DE BENS/INFRAESTRUTURA;FORNECIMENTO DE BENS/MATERIAL ADMINISTRATIVO;FORNECIMENTO DE BENS/PARTES E PEÇAS (AUTOMAÇÃO BANCÁRIA);FORNECIMENTO DE BENS/PARTES E PEÇAS (PGDM);FORNECIMENTO DE BENS/TECNOLOGIA DA INFORMAÇÃO;FORNECIMENTO DE BENS/OUTROS;SERVIÇOS COMUNS/ADVOCACIA;SERVIÇOS COMUNS/APOIO À GESTÃO DE PESSOAS;SERVIÇOS COMUNS/ASSESSORIA/CONSULTORIA;SERVIÇOS COMUNS/CARTÓRIO;SERVIÇOS COMUNS/CONTABILIDADE;SERVIÇOS COMUNS/DOSI/DOSA/DODR;SERVIÇOS COMUNS/TELECOMUNICAÇÃO;SERVIÇOS COMUNS/DESPACHANTE;SERVIÇOS COMUNS/DESPACHO ADUANEIRO;SERVIÇOS COMUNS/ENGENHARIA;SERVIÇOS COMUNS/MANUTENÇÃO DE TAA;SERVIÇOS COMUNS/MANUTENÇÃO DE PGDM;SERVIÇOS COMUNS/OBRA/REFORMA;SERVIÇOS COMUNS/PCMSO;SERVIÇOS COMUNS/PPRA;SERVIÇOS COMUNS/REMANEJAMENTO;SERVIÇOS COMUNS/REPARO DE COFRE;SERVIÇOS COMUNS/REPARO DE PEÇAS;SERVIÇOS COMUNS/SAÚDE;SERVIÇOS COMUNS/SEGURO;SERVIÇOS COMUNS/TECNOLOGIA DA INFORMAÇÃO;SERVIÇOS COMUNS/TEMPORÁRIO;SERVIÇOS COMUNS/TRANSPORTE ;SERVIÇOS COMUNS/TREINAMENTO;SERVIÇOS COMUNS/OUTROS;FORNECIMENTO DE BENS E SERVIÇOS COMUNS/PARTES E PEÇAS, MANUTENÇÃO DE TAA E REPARO DE PEÇAS;FORNECIMENTO DE BENS E SERVIÇOS COMUNS/PARTES E PEÇAS (PGDM), MANUTENÇÃO E REPARO DE PEÇAS ;FORNECIMENTO DE BENS E SERVIÇOS COMUNS/OUTROS;SERVIÇOS TERCEIRIZADOS/AJUDANTE DE ARMAZÉM;SERVIÇOS TERCEIRIZADOS/ESTAGIÁRIO;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - FÁBRICA DE SOFTWARE;SERVIÇOS TERCEIRIZADOS/JOVEM APRENDIZ;SERVIÇOS TERCEIRIZADOS/LIMPEZA;SERVIÇOS TERCEIRIZADOS/MANUTENÇÃO PREDIAL;SERVIÇOS TERCEIRIZADOS/MOTOBOY;SERVIÇOS TERCEIRIZADOS/RECEPÇÃO;SERVIÇOS TERCEIRIZADOS/SECRETARIA EXECUTIVA;SERVIÇOS TERCEIRIZADOS/VIGILÂNCIA;SERVIÇOS TERCEIRIZADOS/LIMPEZA E VIGILÂNCIA;SERVIÇOS TERCEIRIZADOS/LIMPEZA E MANUTENÇÃO PREDIAL;SERVIÇOS TERCEIRIZADOS/LIMPEZA E RECEPÇÃO;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - TELEATENDIMENTO;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - TEMPORÁRIOS;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - MICROFILMAGEM;SERVIÇOS TERCEIRIZADOS/OUTROS;LOCAÇÃO/EQUIPAMENTOS;LOCAÇÃO/EQUIPAMENTOS/PROGRAMAS DE TI;LOCAÇÃO/IMÓVEIS;LOCAÇÃO/PROGRAMAS DE TI;LOCAÇÃO/SOB MEDIDA;LOCAÇÃO/OUTROS"
    Formulario['SIM_NAO4'].Visivel = True
    Formulario['SIM_NAO4'].Habilitado = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = True
    Formulario['SIM_NAO7'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Contrato" 
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = True
    Formulario['FUNDAMENTACAO'].Habilitado = True
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario["FUNDAMENTACAO"].Itens = "ART. 22 DO DECRETO 7.892/2013;CÓDIGO CIVIL;CÓDIGO CIVIL, ART. 884;COMPRA/CONTRATAÇÃO INERENTE A ATIVIDADE FIM - ACORDÃO TCU PLENÁRIO 1705/2007;DESOBRIGADO;LEI N° 13.303/2016, ART. 27, §§ 2º E 3°;LEI N° 13.303/2016, ART. 27, § 3°;LEI N° 13.303/2016, ART. 28;LEI N° 13.303/2016, ART. 28, § 3°, INCISO I;LEI N° 13.303/2016, ART. 28, § 3°, INCISO II;LEI N° 13.303/2016, ART. 28 C/C ART. 32, INCISO IV;LEI N° 13.303/2016, ART. 28 C/C ART. 32, INCISO IV E ART. 63, INCISO I;LEI N° 13.303/2016, ART. 28 C/C ART. 63, INCISO I;LEI N° 13.303/2016, ART. 28 C/C ART. 63, INCISO III E DECRETO N° 7.892/2013;LEI N° 13.303/2016, ART. 28 C/C DECRETO N° 7.892/2013, ART. 22;LEI N° 13.303/2016, ART. 28, INCISO I;LEI N° 13.303/2016, ART. 29, § 1Â°;LEI N° 13.303/2016, ART. 29, INCISO I;LEI N° 13.303/2016, ART. 29, INCISO II;LEI N° 13.303/2016, ART. 29, INCISO III;LEI N° 13.303/2016, ART. 29, INCISO IV;LEI N° 13.303/2016, ART. 29, INCISO IX;LEI N° 13.303/2016, ART. 29, INCISO V;LEI N° 13.303/2016, ART. 29, INCISO VI;LEI N° 13.303/2016, ART. 29, INCISO VII;LEI N° 13.303/2016, ART. 29, INCISO VIII;LEI N° 13.303/2016, ART. 29, INCISO X;LEI N° 13.303/2016, ART. 29, INCISO XI;LEI N° 13.303/2016, ART. 29, INCISO XII;LEI N° 13.303/2016, ART. 29, INCISO XIII;LEI N° 13.303/2016, ART. 29, INCISO XIV;LEI N° 13.303/2016, ART. 29, INCISO XV;LEI N° 13.303/2016, ART. 29, INCISO XVI;LEI N° 13.303/2016, ART. 29, INCISO XVII;LEI N° 13.303/2016, ART. 29, INCISO XVIII;LEI N° 13.303/2016, ART. 30, CAPUT;LEI N° 13.303/2016, ART. 30, INCISO I;LEI N° 13.303/2016, ART. 30, INCISO II;LEI N° 13.303/2016, ART. 30, INCISO II, A;LEI N° 13.303/2016, ART. 30, INCISO II, B;LEI N° 13.303/2016, ART. 30, INCISO II, C;LEI N° 13.303/2016, ART. 30, INCISO II, D;LEI N° 13.303/2016, ART. 30, INCISO II, E;LEI N° 13.303/2016, ART. 30, INCISO II, F;LEI N° 13.303/2016, ART. 30, INCISO II, G;LEI 10.520 - DECRETO 5.450/2005 - DECRETO 7.892/2013;LEI 10.520/2002 DECRETO 3.555/2000;LEI 10.520/2002 DECRETO 5.450/2005;LEI N° 13.303/2016, ART. 28, INCISO ILEI N° 13.303/2016, ART. 28, INCISO II"

    

##Campos obrigatórios para Inserir contratos de parceria no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRPARCERIA"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "CONTRATO DE PARCERIA"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True


##Campos obrigatórios para Inserir TERMO DE CONFIDENCIALIDADE no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONFIDENCIALIDADE"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "TERMO DE CONFIDENCIALIDADE"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
##Campos obrigatórios para Inserir Acordo de Cooperação Técnica no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCOOPERACAO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "ACORDO DE COOPERAÇÃO TÉCNICA"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
##Campos obrigatórios para Inserir Termo de Concessão de Uso no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONCESSAO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "TERMO DE CONCESSÃO DE USO"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
##Campos obrigatórios para Inserir Comodato no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCOMODATO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "COMODATO"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
    
##Campos obrigatórios para Inserir Convênio no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONVENIO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['OBS2'].Visivel = True
    Formulario['OBS2'].Habilitado = True
    Formulario['URL1'].Visivel = True
    Formulario['URL1'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True 
    Formulario['OBS1'].Visivel = True
    Formulario['OBS1'].Habilitado = True 
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
    Formulario['URL2'].Visivel = True
    Formulario['URL2'].Habilitado = True
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = True
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "CONVENIO"
    Formulario['DATA1'].Visivel = False
    Formulario['DATA1'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Convênio"
    

##Campos obrigatórios para Inserir Participação em Contrato Fornecedor BB no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRPARTICIPACAOBB"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##   Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ PARTICIPAÇÃO EM CONTRATO FORNECEDOR BB"
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "PARTICIPAÇÃO EM CONTRATO FORNECEDOR BB"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    Formulario['SIM_NAO5'].Visivel = False
    
    
    
##Campos obrigatórios para Inserir Termo de Doação no Gescon Gescon
if (OrdemServico.Servico.Sigla == "INSERIRDOACAO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "TERMO DE DOAÇÃO"
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = True
    Formulario['DATA1'].Visivel = False
    Formulario['DATA1'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['OBS2'].Visivel = True
    Formulario['OBS2'].Habilitado = True
    Formulario['URL1'].Visivel = True
    Formulario['URL1'].Habilitado = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True 
    Formulario['OBS1'].Visivel = True
    Formulario['OBS1'].Habilitado = True 
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
    Formulario['URL2'].Visivel = True
    Formulario['URL2'].Habilitado = True
    
    
 ##Campos obrigatórios para Inserir Contrato de Correspondente Bancário no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCOBAN"): 
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = True
    Formulario['TIPO_ATIVIDADE'].Valor = "Atividade Fim"
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = False
    Formulario['FISCAL_SER'].Visivel = False
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = False
    Formulario['GESTOR_CONTRATO'].Visivel = False
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = False
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/SUBSTABELECIMENTO/COBAN"
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"    
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "SUBSTABELECIMENTO/COBAN"    
    Formulario['DATA1'].Visivel = False
    Formulario['DATA1'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO5'].Habilitado = False
    Formulario['NOME_FORNECEDOR'].Visivel = False
    Formulario['NOME_FORNECEDOR'].Habilitado = False
    Formulario['OBJETO_CONTRATO'].Visivel = False
    Formulario['OBJETO_CONTRATO'].Habilitado = False
    Formulario['NUMERO_OC'].Visivel = False
    Formulario['NUMERO_OC'].Habilitado = False
    Formulario['CSC_DATA_INICIO'].Visivel = False
    Formulario['CSC_DATA_INICIO'].Habilitado = False
    Formulario['CSC_DATA_FIM'].Visivel = False
    Formulario['CSC_DATA_FIM'].Habilitado = False
    Formulario['VALOR'].Visivel = False
    Formulario['VALOR'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['OBS2'].Visivel = False
    Formulario['OBS2'].Habilitado = False
    Formulario['URL1'].Visivel = False
    Formulario['URL1'].Habilitado = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False 
    Formulario['OBS1'].Visivel = False
    Formulario['OBS1'].Habilitado = False 
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
    Formulario['URL2'].Visivel = False
    Formulario['URL2'].Habilitado = False
    Formulario['TIPO_DOCUMENTO'].Visivel = False
    Formulario['TIPO_DOCUMENTO'].Habilitado - False
    Formulario['CONTRATO_ADITIVO'].Visivel = True
    Formulario['CONTRATO_ADITIVO'].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - FISICA_JUDIRICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.FISICA_JUDIRICA] obrigatório
**FISICA_JUDIRICA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['FISICA_JUDIRICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CNPJ'].Habilitado = True
    Formulario['CNPJ'].Visivel = True

if Formulario['FISICA_JUDIRICA'].Valor != "Pessoa Jurídica":
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CNPJ'].Habilitado = False
    Formulario['CNPJ'].Visivel = False
```
  - NOME_FORNECEDOR "Fornecedor" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - CNPJ_FORNECEDOR "CNPJ do Fornecedor" [TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
  - TIPO_SOLICITACAO_OC "Tipo de Solicitação" [DropDownList String → CPE_CSC.TIPO_SOLICITACAO_OC] obrigatório
  - TIPO_OC_CSC "Tipo de OC" [DropDownList String → CPE_CSC.TIPO_OC_CSC] obrigatório
  - OBS5 "Descrição Detalhada" [Memo String(2000) → CPE_CONTRATOS.OBS5]
  - NUMERO_OC "Número da OC (Inserir 0 caso não haja)" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC]
  - SIM_NAO6 "Aprovar/Revisar OC?" [DropDownList String → CPE_CSC.SIM_NAO6] obrigatório
**SIM_NAO6.ScriptModificado**
```python
if Formulario['SIM_NAO6'].Valor == "Sim":
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_RC'].Habilitado = True
    Formulario['NUMERO_RC'].Visivel = True    
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['TIPO_SOLICITACAO_OC'].Habilitado = True
    Formulario['TIPO_SOLICITACAO_OC'].Visivel = True
    Formulario['TIPO_OC_CSC'].Habilitado = True
    Formulario['TIPO_OC_CSC'].Visivel = True
   ## Formulario['MODALIDADE_LICITACAO'].Habilitado = True
   ## Formulario['MODALIDADE_LICITACAO'].Visivel = True
    Formulario['FISICA_JUDIRICA'].Habilitado = True
    Formulario['FISICA_JUDIRICA'].Visivel = True
    Formulario['OBS5'].Habilitado = True
    Formulario['OBS5'].Visivel = True   
    
if Formulario['SIM_NAO6'].Valor != "Sim":
    Formulario['NUMERO_OC'].Habilitado = False
    Formulario['NUMERO_OC'].Visivel = False
    Formulario['NUMERO_RC'].Habilitado = False
    Formulario['NUMERO_RC'].Visivel = False    
    Formulario['NOME_FORNECEDOR'].Habilitado = False
    Formulario['NOME_FORNECEDOR'].Visivel = False
    Formulario['CNPJ'].Habilitado = False
    Formulario['CNPJ'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CSC_CPF'].Visivel = False    
    Formulario['TIPO_SOLICITACAO_OC'].Habilitado = False
    Formulario['TIPO_SOLICITACAO_OC'].Visivel = False
    Formulario['TIPO_OC_CSC'].Habilitado = False
    Formulario['TIPO_OC_CSC'].Visivel = False
   ## Formulario['MODALIDADE_LICITACAO'].Habilitado = False
   ## Formulario['MODALIDADE_LICITACAO'].Visivel = False
    Formulario['FISICA_JUDIRICA'].Habilitado = False
    Formulario['FISICA_JUDIRICA'].Visivel = False
    Formulario['OBS5'].Habilitado = False
    Formulario['OBS5'].Visivel = False
```
  - NUMERO_RC "Número da RC (se houver)" [TextBox String → CPE_CSC.NUMERO_RC]
- Operação PR0001 Preencher Campos
  - MODALIDADE_DE_CONTRATACAO "Modalidade de Contratação" [DropDownList String → CPE_CONTRATOS.MODALIDADE_DE_CONTRATACAO] obrigatório
  - FUNDAMENTACAO "Fundamentação Legal" [DropDownList String → CPE_CSC.FUNDAMENTACAO] obrigatório
  - SIM_NAO "Contrato Possui Garantia?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - SIM_NAO_PROC "Publicar Instrumento Contratual  no DOU?" [DropDownList String → CPE_ORDEM_SERVICO.SIM_NAO_PROC] obrigatório
  - SIM_NAO5 "Minha Gerência Executiva é a Gesuc?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
**SIM_NAO5.ScriptModificado**
```python
if Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRPARCERIA":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "CONTRATO DE PARCERIA"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRPARCERIA":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/CONTRATO DE PARCERIA"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONFIDENCIALIDADE":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "TERMO DE CONFIDENCIALIDADE"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONFIDENCIALIDADE":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/TERMO DE CONFIDENCIALIDADE"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOOPERACAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "ACORDO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOOPERACAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ACORDO"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONCESSAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "TERMO DE CONCESSÃO DE USO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONCESSAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ TERMO DE CONCESSÃO DE USO"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOMODATO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "COMODATO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOMODATO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ COMODATO"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONVENIO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "CONVÊNIO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONVENIO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ CONVÊNIO"
```
  - CSC_DATA_INICIO "Início da Vigência" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO] obrigatório
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório — Configuracao={"Mascara":"00000/0000"}
  - DATA1 "Data de Publicação no DOU" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA1] obrigatório
  - CONTRATO_ADITIVO "Contrato ou Aditivo?" [DropDownList String → CPE_CONTRATOS.CONTRATO_ADITIVO] obrigatório
  - OBS2 "Descrição Detalhada - Relacionada a publicação do Instrumento Contratual no site da BBTS (Será enviado a equipe de Comunicação)" [Memo String(2000) → CPE_CONTRATOS.OBS2] obrigatório
  - URL1 "Informe a URL da página para publicação do Instrumento Contratual no site da BBTS." [TextBox String → CP_ORDEM_SERVICO.URL1] obrigatório
  - CSC_DATA_FIM "Fim da Vigência" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
  - URL2 "Informe o URL da página para publicação do extrato no DOU do Instrumento Contratual no site da BBTS." [TextBox String → CPE_CSC.URL2] obrigatório
  - RESPONSAVEL_INFORMACAO "Responsável pela Informação - Será enviado a equipe de Comunicação" [DropDownList String → CPE_CSC.RESPONSAVEL_INFORMACAO] obrigatório
  - DIRETORIA_GERENCIA "Diretoria/Gerência - Inserir no formato Xxxxx/Xxxxx - Ex: Diafi/Gesap" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA] obrigatório
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO] obrigatório
  - RESPONSAVEL_PROCESSO "Responsável pela Condução do Processo" [DropDownList String → CPE_CSC.RESPONSAVEL_PROCESSO] obrigatório
  - DataInicioPrevisto (nativo) "Data da Assinatura do Documento Contratual" obrigatório
  - SIM_NAO3 "Serviço Fiscalizado por Comissão?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
  - TIPO_DOCUMENTO "Tipo de documento" [DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO]
  - SIM_NAO4 "Possui Mapa de Gerenciamento de Riscos?" [DropDownList String → CPE_CSC.SIM_NAO4] obrigatório
  - URL3 "Link da pasta/dossiê digital" [TextBox String → CPE_CSC.URL3] obrigatório
  - SIM_NAO1 "Publicar o extrato no DOU do Instrumento Contratual no site da BBTS?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario['SIM_NAO1'].Valor == "Sim":
    Formulario['URL2'].Visivel = True
    Formulario['URL2'].Habilitado = True
    Formulario['OBS1'].Visivel = True
    Formulario['OBS1'].Habilitado = True
    Formulario['RESPONSAVEL_INFORMACAO'].Visivel = True
    Formulario['RESPONSAVEL_INFORMACAO'].Habilitado = True
   
if Formulario['SIM_NAO1'].Valor != "Sim":
    Formulario['URL2'].Visivel = False
    Formulario['URL2'].Habilitado = False 
    Formulario['OBS1'].Visivel = False
    Formulario['OBS1'].Habilitado = False
```
  - OBS1 "Descrição Detalhada - Relacionada a publicação do Extrato do DOU do Instrumento Contratual no site da BBTS (Será enviado a equipe de comunicação)" [Memo String(2000) → CPE_CONTRATOS.OBS1] obrigatório
  - DescricaoDetalhada (nativo)
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna NUMERO_PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna CONDICAO_USO obrigatório
  - LABEL1 "Solicito por gentileza, publicação da RTF no Diário Oficial da União. Ao finalizar o procedimento, peço por gentileza anexar no chamado o Extrato do DOU. " [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - SIM_NAO7 "Publicar Instrumento Contratual no Siasg?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
  - SIM_NAO_INFRA "Publicar Instrumento Contratual no site da BBTS?" [DropDownList String → CPE_ORDEM_SERVICO.SIM_NAO_INFRA] obrigatório
**SIM_NAO_INFRA.ScriptModificado**
```python
if Formulario['SIM_NAO_INFRA'].Valor == "Sim":
    Formulario['OBS2'].Habilitado = True
    Formulario['OBS2'].Visivel = True
    Formulario['RESPONSAVEL_INFORMACAO'].Habilitado = True
    Formulario['RESPONSAVEL_INFORMACAO'].Visivel = True    
    Formulario['URL1'].Habilitado = True
    Formulario['URL1'].Visivel = True
    

if Formulario['SIM_NAO_INFRA'].Valor != "Sim":
    Formulario['OBS2'].Habilitado = False
    Formulario['OBS2'].Visivel = False
    Formulario['URL1'].Habilitado = False
    Formulario['URL1'].Visivel = False
```
  - OBJETO_CONTRATO "Objeto da Contratação" [Memo String(1999) → CPE_CSC.OBJETO_CONTRATO] obrigatório
  - VALOR "Valor Contratado" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - TIPO_ATIVIDADE "Tipo de Atividade - informe" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
#if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
#    Formulario['INFORMATIVO_CESEC'].Habilitado = True
#    Formulario['INFORMATIVO_CESEC'].Visivel = True
#    Formulario['DADOS_CONTRATOS_C'].Habilitado = True
#    Formulario['DADOS_CONTRATOS_C'].Visivel = True
#
#if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
#    Formulario['INFORMATIVO_CESEC'].Habilitado = False
#    Formulario['INFORMATIVO_CESEC'].Visivel = False
#    Formulario['DADOS_CONTRATOS_C'].Habilitado = False
#    Formulario['DADOS_CONTRATOS_C'].Visivel = False
```
  - FISCAL_SER "Fiscal do Serviço" [DataGrid RecordList → Z_00143_FISCAL_SER.FISCAL_SER] obrigatório
    - coluna FISCAL_SERVICO obrigatório
**FISCAL_SER.FISCAL_SERVICO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_SERVICO"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_FISCAL_SERVICO"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_FISCAL_SERVICO"].Habilitado = False
```
    - coluna FISCAL_SUPLENTE obrigatório
**FISCAL_SER.FISCAL_SUPLENTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_SUPLENTE"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_FISCAL_SUPLENTE"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_FISCAL_SUPLENTE"].Habilitado = False
```
    - coluna MATRICULA_FISCAL_SERVICO obrigatório
    - coluna MATRICULA_FISCAL_SUPLENTE obrigatório
  - FISCAL_MASTER "Fiscal do Serviço Master" [DataGrid RecordList → Z_00143_FISCAL_MASTER.FISCAL_MASTER]
    - coluna FISCAL_MASTER
**FISCAL_MASTER.FISCAL_MASTER.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_MASTER"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_FISCAL_MASTER"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_FISCAL_MASTER"].Habilitado = False
```
    - coluna FISCAL_MASTER_SUPLENTE
**FISCAL_MASTER.FISCAL_MASTER_SUPLENTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_MASTER_SUPLENTE"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_SUPLENTE"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_SUPLENTE"].Habilitado = False
```
    - coluna MATRICULA_FISCAL_MASTER obrigatório
    - coluna MATRICULA_SUPLENTE obrigatório
  - GESTOR_CONTRATO "Gestor do Contrato" [DataGrid RecordList → Z_00143_GESTOR_CONTRATO.GESTOR_CONTRATO] obrigatório
    - coluna GESTOR_CONTRATO_SUPLENTE obrigatório
**GESTOR_CONTRATO.GESTOR_CONTRATO_SUPLENTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["GESTOR_CONTRATO_SUPLENTE"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_GESTOR_SUPLENTE"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_GESTOR_SUPLENTE"].Habilitado = False
```
    - coluna MATRICULA_GESTOR obrigatório
    - coluna MATRICULA_GESTOR_SUPLENTE obrigatório
    - coluna GESTOR_CONTRATO obrigatório
**GESTOR_CONTRATO.GESTOR_CONTRATO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["GESTOR_CONTRATO"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_GESTOR"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_GESTOR"].Habilitado = False
```
  - CATEGORIA_DE_COMPRA "Categoria de Compra" [DropDownList String → CPE_CSC.CATEGORIA_DE_COMPRA] obrigatório

### [344459] SubProcesso "Consulta Fisco Tributária"
Responsável: Fila CSC - Contratos (papel 688)
Config: ChamadaAssincrona=true; AssociacaoId=944; Configuracao={"ExibirBotaoNovaSubprocessos":true}
- ValoresInputs:
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=3679; CustomProperty=TOMADOR
  - CustomPropertyId=2581; CustomProperty=OBS21
  - CustomPropertyId=775; CustomProperty=CNPJ_FORNECEDOR
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2800; ClasseConfiguracao=Instrumento contratual com certificado de assinaturas
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2178; ClasseConfiguracao=Parecer Tributário
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais Gescon -> Consulta Fisco Tributaria; FraseInversaAssociacao=Consulta Fisco Tributaria -> Inserir Documentos Contratuais Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=CONSULTA FISCO TRIBUTARIA; SeparadorSequencial=.; IncluirSubniveisSeparador=true | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Consulta Fisco - Tributária (Estadual, Municipal ou Federal)

### [344457] EventoInicial "Inserir Documentos Contratuais no Sisccon"
Responsável: Cliente (papel 18)
Config: Codigo=INSERIRSISCCON; PermitirRascunho=true; Configuracao={"ServicoIniciador":"<Nenhum>"}
TipoSolicitacao: 05.04. Suprimentos Corporativos, Licitações e Contratos - Contratos
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Processo.Custom import Atividade
#cont = 0
#if OrdemServico.GetCustom("SIM_NAO_INFRA")=="Sim":
#    for itemOcorrencia in OrdemServico.ItensAnexados:
#        if itemOcorrencia.ToString().find("Contrato ou Aditivo Assinado - Tarjado:")==0:
#            cont=1
#else:
#    cont=1
#if cont==0:
#    Criticas.AdicionaPendencia('Não foi anexado o contrato com as informações tarjadas.')

if ((OrdemServico.PossuiItem("MAPAGERISCOS") == False) and (OrdemServico.GetCustom("SIM_NAO4") == 'Sim')):
    Criticas.AdicionaPendencia ('Não foi anexado o mapa de Gerenciamento de Riscos')
    
    
if ((OrdemServico.PossuiItem("RTF") == False) and (OrdemServico.GetCustom("SIM_NAO_PROC") == 'Sim')):
    Criticas.AdicionaPendencia ('Não foi anexado o RTF para realizar a publicação no Diário Oficial da União - DOU')
    

    
#if ((OrdemServico.PossuiItem("PROJETOBAS") == False) and (OrdemServico.GetCustom("TIPO_ATIVIDADE") == 'Atividade Fim')and (OrdemServico.Servico.Sigla != "INSERIRCOBAN")):  
#    Criticas.AdicionaPendencia ('Não foi anexado o projeto básico. Em casos de instrumento contratual com fornecedor vinculado a atividade fim da empresa, é necessário anexar o projeto básico.')
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Atividade
Formulario['TIPO_ATIVIDADE'].Visivel = False
Formulario['DGCO_BB'].Visivel = False
##Formulario['INFORMATIVO_CESEC'].Visivel = False
##Formulario['DADOS_CONTRATOS_C'].Visivel = False
Formulario['FISCAL_SER'].Visivel = False
Formulario['FISCAL_MASTER'].Visivel = False
Formulario['GESTOR_CONTRATO'].Visivel = False
Formulario['SIM_NAO'].Visivel = False
Formulario['SIM_NAO_INFRA'].Visivel = False
Formulario['SIM_NAO_PROC'].Visivel = False
Formulario['RESPONSAVEL_PROCESSO'].Visivel = False
Formulario['PPGEREX_NEGOCIO'].Visivel = False
Formulario['DIRETORIA_GERENCIA'].Visivel = False
Formulario['OBS2'].Visivel = False
Formulario['RESPONSAVEL_INFORMACAO'].Visivel = False
Formulario['SIM_NAO1'].Visivel = False
Formulario['LABEL1'].Visivel = False
Formulario['URL1'].Visivel = False
Formulario['URL2'].Visivel = False
Formulario['OBS1'].Visivel = False
#Formulario['URL3'].Visivel = False
#Formulario['SIM_NAO2'].Visivel = False
Formulario['SIM_NAO3'].Visivel = False
Formulario['CATEGORIA_DE_COMPRA'].Visivel = False
Formulario['SIM_NAO4'].Visivel = False
Formulario['FUNDAMENTACAO'].Visivel = False
Formulario['SIM_NAO5'].Visivel = False
Formulario['DATA1'].Visivel = False
Formulario['FUNDAMENTACAO'].Visivel = False
Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = False
Formulario['OBJETO_CONTRATO'].Visivel = False
Formulario['NUMERO_OC'].Visivel = False
Formulario['CSC_DATA_INICIO'].Visivel = False
Formulario['CSC_DATA_FIM'].Visivel = False
Formulario['VALOR'].Visivel = False
Formulario['SIM_NAO6'].Visivel = False
Formulario['SIM_NAO7'].Visivel = False
Formulario['CONTRATO_ADITIVO'].Visivel = False
Formulario['CONTRATO_ADITIVO'].Habilitado = False
Formulario['URL3'].Habilitado = False
Formulario['URL3'].Visivel = False
##Formulario['MODALIDADE_LICITACAO'].Habilitado = False
##Formulario['MODALIDADE_LICITACAO'].Visivel = False
Formulario['FUNDAMENTACAO'].Habilitado = False
Formulario['FUNDAMENTACAO'].Visivel = False
#Formulario['NOME_FORNECEDOR'].Visivel = False
#Formulario['NOME_FORNECEDOR'].Habilitado = False
#Formulario['TOMADOR'].Visivel = False
#Formulario['TOMADOR'].Habilitado = False
Formulario['OBS21'].Habilitado = False
Formulario['OBS21'].Visivel = False
Formulario['VALOR_REF_CONT'].Habilitado = False
Formulario['VALOR_REF_CONT'].Visivel = False
Formulario['RESUMO'].Habilitado = False
Formulario['RESUMO'].Visivel = False
Formulario['DATA_ENCERRA'].Habilitado = False
Formulario['DATA_ENCERRA'].Visivel = False
Formulario['NUMERO_OC'].Visivel = False
Formulario['NUMERO_RC'].Visivel = False    
Formulario['CNPJ_FORNECEDOR'].Visivel = False
Formulario['CSC_CPF'].Visivel = False    
Formulario['TIPO_SOLICITACAO_OC'].Visivel = False
Formulario['TIPO_OC_CSC'].Visivel = False
##Formulario['MODALIDADE_LICITACAO'].Visivel = False
Formulario['FISICA_JUDIRICA'].Visivel = False
Formulario['OBS5'].Visivel = False
Formulario["TIPO_DOCUMENTO"].Habilitado = False

##Campos obrigatórios para Inserir aditivos de fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRADITIVO"):
#Formulario['INFORMAR_DOCUMENTO'].Valor == "Aditivo":
    Formulario['TIPO_ATIVIDADE'].Habilitado = True
    Formulario['TIPO_ATIVIDADE'].Visivel = True
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = False
    Formulario['FISCAL_SER'].Visivel = False
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = False
    Formulario['GESTOR_CONTRATO'].Visivel = False
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True   
    Formulario['DIRETORIA_GERENCIA'].Habilitado = False
    Formulario['DIRETORIA_GERENCIA'].Visivel = False
    Formulario['PPGEREX_NEGOCIO'].Habilitado = False
    Formulario['PPGEREX_NEGOCIO'].Visivel = False
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = False
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = False
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False  
    Formulario['SIM_NAO3'].Visivel = False
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = False
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = True
    Formulario['SIM_NAO7'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Aditivo"
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    #Formulario['TOMADOR'].Visivel = True
    #Formulario['TOMADOR'].Habilitado = True
    Formulario['OBS21'].Habilitado = True
    Formulario['OBS21'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['VALOR_REF_CONT'].Habilitado = True
    Formulario['VALOR_REF_CONT'].Visivel = True
    
##Campos obrigatórios para Inserir atas de registros de preços com fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRATA"):    
#if Formulario['INFORMAR_DOCUMENTO'].Valor == "Ata de Registro de Preço":
    Formulario['TIPO_ATIVIDADE'].Habilitado = True
    Formulario['TIPO_ATIVIDADE'].Visivel = True
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = True
    Formulario['FISCAL_MASTER'].Visivel = True
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True  
##    Formulario['SIM_NAO2'].Visivel = True
##    Formulario['SIM_NAO2'].Habilitado = True 
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = True
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = True
    Formulario["CATEGORIA_DE_COMPRA"].Itens = "ATA DE REGISTRO DE PREÇOS/FORNECIMENTO DE BENS/EQUIPAMENTOS/PEÇAS;ATA DE REGISTRO DE PREÇOS/SERVIÇOS"
    Formulario['SIM_NAO4'].Visivel = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = False
    Formulario['SIM_NAO7'].Habilitado = False
    Formulario["TIPO_DOCUMENTO"].Valor = "Ata de Registro de Preço"
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Valor = "LEI N° 13.303/2016, ART. 28 C/C ART. 32, INCISO IV"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "LICITAÇÃO ELETRÔNICA"
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
#    Formulario['TE_NOME_FORNECEDOR'].Visivel = True
#    Formulario['TE_NOME_FORNECEDOR'].Habilitado = True
    #Formulario['TOMADOR'].Visivel = True
    #Formulario['TOMADOR'].Habilitado = True
    Formulario['OBS21'].Habilitado = True
    Formulario['OBS21'].Visivel = True
    
    
    
##Campos obrigatórios para Inserir apostilamento de fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRAPOSTILAMENTO"):
#if Formulario['INFORMAR_DOCUMENTO'].Valor == 'Apostilamento':
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = False
    Formulario['FISCAL_SER'].Visivel = False
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = False
    Formulario['GESTOR_CONTRATO'].Visivel = False
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['DIRETORIA_GERENCIA'].Habilitado = False
    Formulario['DIRETORIA_GERENCIA'].Visivel = False
    Formulario['PPGEREX_NEGOCIO'].Habilitado = False
    Formulario['PPGEREX_NEGOCIO'].Visivel = False
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = False
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True   
##    Formulario['SIM_NAO2'].Visivel = True
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = False
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = False
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False 
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = True
    Formulario['SIM_NAO7'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Apostilamento"
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    
##Campos obrigatórios para Inserir contratos de fornecedores no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONTRATO"):
#if Formulario['INFORMAR_DOCUMENTO'].Valor == "Contrato":
    Formulario['TIPO_ATIVIDADE'].Habilitado = True
    Formulario['TIPO_ATIVIDADE'].Visivel = True
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
 ##   Formulario['INFORMATIVO_CESEC'].Habilitado = False
 ##   Formulario['INFORMATIVO_CESEC'].Visivel = False
 ##   Formulario['DADOS_CONTRATOS_C'].Habilitado = False
 ##   Formulario['DADOS_CONTRATOS_C'].Visivel = False
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = True
    Formulario['FISCAL_MASTER'].Visivel = True
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = True
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = True
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = True
    Formulario["CATEGORIA_DE_COMPRA"].Itens = "CREDENCIAMENTO/ENRIQUECIMENTO DE BASE;CREDENCIAMENTO/FORNECIMENTO DE BENS/EQUIPAMENTOS/PEÇAS;CREDENCIAMENTO/REPARO DE PARTES E PEÇAS;CREDENCIAMENTO/SERVIÇOS;CREDENCIAMENTO/TRANSPORTE;CREDENCIAMENTO/TELEFONIA;CREDENCIAMENTO/OUTROS;FORNECIMENTO DE BENS/AQUISIÇÃO DE MOBILIÁRIO;FORNECIMENTO DE BENS/INFORMÁTICA;FORNECIMENTO DE BENS/INFRAESTRUTURA;FORNECIMENTO DE BENS/MATERIAL ADMINISTRATIVO;FORNECIMENTO DE BENS/PARTES E PEÇAS (AUTOMAÇÃO BANCÁRIA);FORNECIMENTO DE BENS/PARTES E PEÇAS (PGDM);FORNECIMENTO DE BENS/TECNOLOGIA DA INFORMAÇÃO;FORNECIMENTO DE BENS/OUTROS;SERVIÇOS COMUNS/ADVOCACIA;SERVIÇOS COMUNS/APOIO À GESTÃO DE PESSOAS;SERVIÇOS COMUNS/ASSESSORIA/CONSULTORIA;SERVIÇOS COMUNS/CARTÓRIO;SERVIÇOS COMUNS/CONTABILIDADE;SERVIÇOS COMUNS/DOSI/DOSA/DODR;SERVIÇOS COMUNS/TELECOMUNICAÇÃO;SERVIÇOS COMUNS/DESPACHANTE;SERVIÇOS COMUNS/DESPACHO ADUANEIRO;SERVIÇOS COMUNS/ENGENHARIA;SERVIÇOS COMUNS/MANUTENÇÃO DE TAA;SERVIÇOS COMUNS/MANUTENÇÃO DE PGDM;SERVIÇOS COMUNS/OBRA/REFORMA;SERVIÇOS COMUNS/PCMSO;SERVIÇOS COMUNS/PPRA;SERVIÇOS COMUNS/REMANEJAMENTO;SERVIÇOS COMUNS/REPARO DE COFRE;SERVIÇOS COMUNS/REPARO DE PEÇAS;SERVIÇOS COMUNS/SAÚDE;SERVIÇOS COMUNS/SEGURO;SERVIÇOS COMUNS/TECNOLOGIA DA INFORMAÇÃO;SERVIÇOS COMUNS/TEMPORÁRIO;SERVIÇOS COMUNS/TRANSPORTE ;SERVIÇOS COMUNS/TREINAMENTO;SERVIÇOS COMUNS/OUTROS;FORNECIMENTO DE BENS E SERVIÇOS COMUNS/PARTES E PEÇAS, MANUTENÇÃO DE TAA E REPARO DE PEÇAS;FORNECIMENTO DE BENS E SERVIÇOS COMUNS/PARTES E PEÇAS (PGDM), MANUTENÇÃO E REPARO DE PEÇAS ;FORNECIMENTO DE BENS E SERVIÇOS COMUNS/OUTROS;SERVIÇOS TERCEIRIZADOS/AJUDANTE DE ARMAZÉM;SERVIÇOS TERCEIRIZADOS/ESTAGIÁRIO;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - FÁBRICA DE SOFTWARE;SERVIÇOS TERCEIRIZADOS/JOVEM APRENDIZ;SERVIÇOS TERCEIRIZADOS/LIMPEZA;SERVIÇOS TERCEIRIZADOS/MANUTENÇÃO PREDIAL;SERVIÇOS TERCEIRIZADOS/MOTOBOY;SERVIÇOS TERCEIRIZADOS/RECEPÇÃO;SERVIÇOS TERCEIRIZADOS/SECRETARIA EXECUTIVA;SERVIÇOS TERCEIRIZADOS/VIGILÂNCIA;SERVIÇOS TERCEIRIZADOS/LIMPEZA E VIGILÂNCIA;SERVIÇOS TERCEIRIZADOS/LIMPEZA E MANUTENÇÃO PREDIAL;SERVIÇOS TERCEIRIZADOS/LIMPEZA E RECEPÇÃO;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - TELEATENDIMENTO;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - TEMPORÁRIOS;SERVIÇOS TERCEIRIZADOS/POSTOS DE SERVIÇOS - MICROFILMAGEM;SERVIÇOS TERCEIRIZADOS/OUTROS;LOCAÇÃO/EQUIPAMENTOS;LOCAÇÃO/EQUIPAMENTOS/PROGRAMAS DE TI;LOCAÇÃO/IMÓVEIS;LOCAÇÃO/PROGRAMAS DE TI;LOCAÇÃO/SOB MEDIDA;LOCAÇÃO/OUTROS"
    Formulario['SIM_NAO4'].Visivel = True
    Formulario['SIM_NAO4'].Habilitado = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO6'].Visivel = True
    Formulario['SIM_NAO6'].Habilitado = True
    Formulario['SIM_NAO7'].Visivel = True
    Formulario['SIM_NAO7'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Contrato" 
    Formulario['URL3'].Habilitado = True
    Formulario['URL3'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = True
    Formulario['FUNDAMENTACAO'].Habilitado = True
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario["FUNDAMENTACAO"].Itens = "ART. 22 DO DECRETO 7.892/2013;CÓDIGO CIVIL;CÓDIGO CIVIL, ART. 884;COMPRA/CONTRATAÇÃO INERENTE A ATIVIDADE FIM - ACORDÃO TCU PLENÁRIO 1705/2007;DESOBRIGADO;LEI N° 13.303/2016, ART. 27, §§ 2º E 3°;LEI N° 13.303/2016, ART. 27, § 3°;LEI N° 13.303/2016, ART. 28;LEI N° 13.303/2016, ART. 28, § 3°, INCISO I;LEI N° 13.303/2016, ART. 28, § 3°, INCISO II;LEI N° 13.303/2016, ART. 28 C/C ART. 32, INCISO IV;LEI N° 13.303/2016, ART. 28 C/C ART. 32, INCISO IV E ART. 63, INCISO I;LEI N° 13.303/2016, ART. 28 C/C ART. 63, INCISO I;LEI N° 13.303/2016, ART. 28 C/C ART. 63, INCISO III E DECRETO N° 7.892/2013;LEI N° 13.303/2016, ART. 28 C/C DECRETO N° 7.892/2013, ART. 22;LEI N° 13.303/2016, ART. 28, INCISO I;LEI N° 13.303/2016, ART. 29, § 1Â°;LEI N° 13.303/2016, ART. 29, INCISO I;LEI N° 13.303/2016, ART. 29, INCISO II;LEI N° 13.303/2016, ART. 29, INCISO III;LEI N° 13.303/2016, ART. 29, INCISO IV;LEI N° 13.303/2016, ART. 29, INCISO IX;LEI N° 13.303/2016, ART. 29, INCISO V;LEI N° 13.303/2016, ART. 29, INCISO VI;LEI N° 13.303/2016, ART. 29, INCISO VII;LEI N° 13.303/2016, ART. 29, INCISO VIII;LEI N° 13.303/2016, ART. 29, INCISO X;LEI N° 13.303/2016, ART. 29, INCISO XI;LEI N° 13.303/2016, ART. 29, INCISO XII;LEI N° 13.303/2016, ART. 29, INCISO XIII;LEI N° 13.303/2016, ART. 29, INCISO XIV;LEI N° 13.303/2016, ART. 29, INCISO XV;LEI N° 13.303/2016, ART. 29, INCISO XVI;LEI N° 13.303/2016, ART. 29, INCISO XVII;LEI N° 13.303/2016, ART. 29, INCISO XVIII;LEI N° 13.303/2016, ART. 30, CAPUT;LEI N° 13.303/2016, ART. 30, INCISO I;LEI N° 13.303/2016, ART. 30, INCISO II;LEI N° 13.303/2016, ART. 30, INCISO II, A;LEI N° 13.303/2016, ART. 30, INCISO II, B;LEI N° 13.303/2016, ART. 30, INCISO II, C;LEI N° 13.303/2016, ART. 30, INCISO II, D;LEI N° 13.303/2016, ART. 30, INCISO II, E;LEI N° 13.303/2016, ART. 30, INCISO II, F;LEI N° 13.303/2016, ART. 30, INCISO II, G;LEI 10.520 - DECRETO 5.450/2005 - DECRETO 7.892/2013;LEI 10.520/2002 DECRETO 3.555/2000;LEI 10.520/2002 DECRETO 5.450/2005;LEI N° 13.303/2016, ART. 28, INCISO ILEI N° 13.303/2016, ART. 28, INCISO II;ADESÃO A LICITAÇÃO"
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    #Formulario['TE_NOME_FORNECEDOR'].Visivel = True
    #Formulario['TE_NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBS21'].Habilitado = True
    Formulario['OBS21'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = False
    Formulario['FISCAL_SER'].Visivel = False
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = False
    Formulario['GESTOR_CONTRATO'].Visivel = False
    Formulario['RESPONSAVEL_INFORMACAO'].Habilitado = False
    Formulario['RESPONSAVEL_INFORMACAO'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['URL3'].Habilitado = False
    Formulario['URL3'].Visivel = False
    Formulario["DescricaoDetalhada"].Habilitado = False
    Formulario["DescricaoDetalhada"].Visivel = False
    Formulario['PROJETOBASIC'].Habilitado = False
    Formulario['PROJETOBASIC'].Visivel = False
    Formulario['MAPAGERISCOS'].Habilitado = False
    Formulario['MAPAGERISCOS'].Visivel = False
    Formulario['VALOR_REF_CONT'].Habilitado = True
    Formulario['VALOR_REF_CONT'].Visivel = True
    Formulario['RESUMO'].Habilitado = True
    Formulario['RESUMO'].Visivel = True
    Formulario['DATA_ENCERRA'].Habilitado = True
    Formulario['DATA_ENCERRA'].Visivel = True

    

##Campos obrigatórios para Inserir contratos de parceria no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRPARCERIA"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "CONTRATO DE PARCERIA"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True


##Campos obrigatórios para Inserir TERMO DE CONFIDENCIALIDADE no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONFIDENCIALIDADE"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "TERMO DE CONFIDENCIALIDADE"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
##Campos obrigatórios para Inserir Acordo de Cooperação Técnica no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCOOPERACAO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "ACORDO DE COOPERAÇÃO TÉCNICA"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
##Campos obrigatórios para Inserir Termo de Concessão de Uso no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONCESSAO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "TERMO DE CONCESSÃO DE USO"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
##Campos obrigatórios para Inserir Comodato no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCOMODATO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "COMODATO"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    
    
    
##Campos obrigatórios para Inserir Convênio no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCONVENIO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['OBS2'].Visivel = True
    Formulario['OBS2'].Habilitado = True
    Formulario['URL1'].Visivel = True
    Formulario['URL1'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True 
    Formulario['OBS1'].Visivel = True
    Formulario['OBS1'].Habilitado = True 
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
    Formulario['URL2'].Visivel = True
    Formulario['URL2'].Habilitado = True
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = True
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "CONVENIO"
    Formulario['DATA1'].Visivel = False
    Formulario['DATA1'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    Formulario["TIPO_DOCUMENTO"].Valor = "Convênio"
    

##Campos obrigatórios para Inserir Participação em Contrato Fornecedor BB no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRPARTICIPACAOBB"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##   Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ PARTICIPAÇÃO EM CONTRATO FORNECEDOR BB"
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "PARTICIPAÇÃO EM CONTRATO FORNECEDOR BB"
    Formulario['DATA1'].Visivel = True
    Formulario['DATA1'].Habilitado = False
    Formulario['DATA1'].Valor = "01/01/1000"
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    Formulario['SIM_NAO5'].Visivel = False
    
    
    
##Campos obrigatórios para Inserir Termo de Doação no Gescon Gescon
if (OrdemServico.Servico.Sigla == "INSERIRDOACAO"):
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = False
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = True
    Formulario['FISCAL_SER'].Visivel = True
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = True
    Formulario['GESTOR_CONTRATO'].Visivel = True
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = True
    Formulario['SIM_NAO'].Valor = "Não"
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = True
    Formulario['SIM_NAO_PROC'].Visivel = True
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = True
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['SIM_NAO3'].Valor = "Não"
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "TERMO DE DOAÇÃO"
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = True
    Formulario['DATA1'].Visivel = False
    Formulario['DATA1'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = True
    Formulario['SIM_NAO5'].Habilitado = True
    #Formulario['NOME_FORNECEDOR'].Visivel = True
    #Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['OBJETO_CONTRATO'].Visivel = True
    Formulario['OBJETO_CONTRATO'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['CSC_DATA_INICIO'].Visivel = True
    Formulario['CSC_DATA_INICIO'].Habilitado = True
    Formulario['CSC_DATA_FIM'].Visivel = True
    Formulario['CSC_DATA_FIM'].Habilitado = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = True
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = True
    Formulario['SIM_NAO_INFRA'].Visivel = True
    Formulario['OBS2'].Visivel = True
    Formulario['OBS2'].Habilitado = True
    Formulario['URL1'].Visivel = True
    Formulario['URL1'].Habilitado = True
    Formulario['SIM_NAO1'].Habilitado = True
    Formulario['SIM_NAO1'].Visivel = True 
    Formulario['OBS1'].Visivel = True
    Formulario['OBS1'].Habilitado = True 
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
    Formulario['URL2'].Visivel = True
    Formulario['URL2'].Habilitado = True
    
    
 ##Campos obrigatórios para Inserir Contrato de Correspondente Bancário no Gescon
if (OrdemServico.Servico.Sigla == "INSERIRCOBAN"): 
    Formulario['TIPO_ATIVIDADE'].Habilitado = False
    Formulario['TIPO_ATIVIDADE'].Visivel = True
    Formulario['TIPO_ATIVIDADE'].Valor = "Atividade Fim"
    Formulario['DGCO_BB'].Habilitado = True
    Formulario['DGCO_BB'].Visivel = True
    Formulario['FISCAL_SER'].Habilitado = False
    Formulario['FISCAL_SER'].Visivel = False
    Formulario['FISCAL_MASTER'].Habilitado = False
    Formulario['FISCAL_MASTER'].Visivel = False
    Formulario['GESTOR_CONTRATO'].Habilitado = False
    Formulario['GESTOR_CONTRATO'].Visivel = False
    Formulario['SIM_NAO'].Habilitado = False
    Formulario['SIM_NAO'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['SIM_NAO_PROC'].Habilitado = False
    Formulario['SIM_NAO_PROC'].Visivel = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False    
    Formulario['DIRETORIA_GERENCIA'].Habilitado = True
    Formulario['DIRETORIA_GERENCIA'].Visivel = True
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
##    Formulario['SIM_NAO2'].Visivel = False
##    Formulario['SIM_NAO2'].Habilitado = False
##    Formulario['URL3'].Visivel = False
##    Formulario['URL3'].Habilitado = False   
    Formulario['SIM_NAO3'].Visivel = False
    Formulario['SIM_NAO3'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Visivel = True
    Formulario['CATEGORIA_DE_COMPRA'].Habilitado = False
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/SUBSTABELECIMENTO/COBAN"
    Formulario['SIM_NAO4'].Visivel = False
    Formulario['SIM_NAO4'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Visivel = True
    Formulario['FUNDAMENTACAO'].Habilitado = False
    Formulario['FUNDAMENTACAO'].Valor = "DESOBRIGADO"    
    Formulario['MODALIDADE_DE_CONTRATACAO'].Visivel = True
    Formulario['MODALIDADE_DE_CONTRATACAO'].Habilitado = False
    Formulario['MODALIDADE_DE_CONTRATACAO'].Valor = "SUBSTABELECIMENTO/COBAN"    
    Formulario['DATA1'].Visivel = False
    Formulario['DATA1'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO5'].Habilitado = False
    #Formulario['NOME_FORNECEDOR'].Visivel = False
    #Formulario['NOME_FORNECEDOR'].Habilitado = False
    Formulario['OBJETO_CONTRATO'].Visivel = False
    Formulario['OBJETO_CONTRATO'].Habilitado = False
    Formulario['NUMERO_OC'].Visivel = False
    Formulario['NUMERO_OC'].Habilitado = False
    Formulario['CSC_DATA_INICIO'].Visivel = False
    Formulario['CSC_DATA_INICIO'].Habilitado = False
    Formulario['CSC_DATA_FIM'].Visivel = False
    Formulario['CSC_DATA_FIM'].Habilitado = False
    Formulario['VALOR'].Visivel = False
    Formulario['VALOR'].Habilitado = False
    Formulario['SIM_NAO5'].Visivel = False
    Formulario['SIM_NAO_INFRA'].Habilitado = False
    Formulario['SIM_NAO_INFRA'].Visivel = False
    Formulario['OBS2'].Visivel = False
    Formulario['OBS2'].Habilitado = False
    Formulario['URL1'].Visivel = False
    Formulario['URL1'].Habilitado = False
    Formulario['SIM_NAO1'].Habilitado = False
    Formulario['SIM_NAO1'].Visivel = False 
    Formulario['OBS1'].Visivel = False
    Formulario['OBS1'].Habilitado = False 
    Formulario['RESPONSAVEL_PROCESSO'].Habilitado = True
    Formulario['RESPONSAVEL_PROCESSO'].Visivel = True
    Formulario['URL2'].Visivel = False
    Formulario['URL2'].Habilitado = False
    Formulario['TIPO_DOCUMENTO'].Visivel = False
    Formulario['TIPO_DOCUMENTO'].Habilitado - False
    Formulario['CONTRATO_ADITIVO'].Visivel = True
    Formulario['CONTRATO_ADITIVO'].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - SIM_NAO_INFRA "Publicar Instrumento Contratual no site da BBTS?" [DropDownList String → CPE_ORDEM_SERVICO.SIM_NAO_INFRA] obrigatório
**SIM_NAO_INFRA.ScriptModificado**
```python
if Formulario['SIM_NAO_INFRA'].Valor == "Sim":
    Formulario['OBS2'].Habilitado = True
    Formulario['OBS2'].Visivel = True
    Formulario['RESPONSAVEL_INFORMACAO'].Habilitado = True
    Formulario['RESPONSAVEL_INFORMACAO'].Visivel = True    
    Formulario['URL1'].Habilitado = True
    Formulario['URL1'].Visivel = True
    

if Formulario['SIM_NAO_INFRA'].Valor != "Sim":
    Formulario['OBS2'].Habilitado = False
    Formulario['OBS2'].Visivel = False
    Formulario['URL1'].Habilitado = False
    Formulario['URL1'].Visivel = False
```
  - OBS2 "Descrição Detalhada - Relacionada a publicação do Instrumento Contratual no site da BBTS (Será enviado a equipe de Comunicação)" [Memo String(2000) → CPE_CONTRATOS.OBS2] obrigatório
  - URL1 "Informe a URL da página para publicação do Instrumento Contratual no site da BBTS." [TextBox String → CP_ORDEM_SERVICO.URL1] obrigatório
  - SIM_NAO "Contrato Possui Garantia?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - SIM_NAO_PROC "Publicar Instrumento Contratual  no DOU?" [DropDownList String → CPE_ORDEM_SERVICO.SIM_NAO_PROC] obrigatório
  - SIM_NAO7 "Publicar Instrumento Contratual no Siasg?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
  - GESTOR_CONTRATO "Gestor do Contrato" [DataGrid RecordList → Z_00143_GESTOR_CONTRATO.GESTOR_CONTRATO] obrigatório
    - coluna GESTOR_CONTRATO_SUPLENTE obrigatório
**GESTOR_CONTRATO.GESTOR_CONTRATO_SUPLENTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["GESTOR_CONTRATO_SUPLENTE"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_GESTOR_SUPLENTE"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_GESTOR_SUPLENTE"].Habilitado = False
```
    - coluna GESTOR_CONTRATO obrigatório
**GESTOR_CONTRATO.GESTOR_CONTRATO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["GESTOR_CONTRATO"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_GESTOR"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_GESTOR"].Habilitado = False
```
    - coluna MATRICULA_GESTOR_SUPLENTE obrigatório
    - coluna MATRICULA_GESTOR obrigatório
  - SIM_NAO5 "Minha Gerência Executiva é a Gesuc?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
**SIM_NAO5.ScriptModificado**
```python
if Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRPARCERIA":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "CONTRATO DE PARCERIA"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRPARCERIA":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/CONTRATO DE PARCERIA"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONFIDENCIALIDADE":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "TERMO DE CONFIDENCIALIDADE"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONFIDENCIALIDADE":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/TERMO DE CONFIDENCIALIDADE"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOOPERACAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "ACORDO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOOPERACAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ACORDO"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONCESSAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "TERMO DE CONCESSÃO DE USO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONCESSAO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ TERMO DE CONCESSÃO DE USO"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOMODATO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "COMODATO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCOMODATO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ COMODATO"
    
elif Formulario['SIM_NAO5'].Valor == "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONVENIO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "CONVÊNIO"
elif Formulario['SIM_NAO5'].Valor != "Sim" and OrdemServico.Servico.Sigla == "INSERIRCONVENIO":
    Formulario['CATEGORIA_DE_COMPRA'].Valor = "OUTROS/ CONVÊNIO"
```
  - CATEGORIA_DE_COMPRA "Categoria de Compra" [DropDownList String → CPE_CSC.CATEGORIA_DE_COMPRA] obrigatório
  - MODALIDADE_DE_CONTRATACAO "Modalidade de Contratação" [DropDownList String → CPE_CONTRATOS.MODALIDADE_DE_CONTRATACAO] obrigatório
  - FUNDAMENTACAO "Fundamentação Legal" [DropDownList String → CPE_CSC.FUNDAMENTACAO] obrigatório
  - TIPO_DOCUMENTO "Tipo de documento" [DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO]
  - VALOR_REF_CONT "Valor do documento contratual (Caso o documento contratual não possua valor, prencher o campo com "0")" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REF_CONT] obrigatório
  - VALOR "Valor do documento contratual (Caso o documento contratual não possua valor, prencher o campo com "0")" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - OBS1 "Descrição Detalhada - Relacionada a publicação do Extrato do DOU do Instrumento Contratual no site da BBTS (Será enviado a equipe de comunicação)" [Memo String(2000) → CPE_CONTRATOS.OBS1] obrigatório
  - FISCAL_MASTER "Fiscal do Serviço Master" [DataGrid RecordList → Z_00143_FISCAL_MASTER.FISCAL_MASTER]
    - coluna FISCAL_MASTER_SUPLENTE
**FISCAL_MASTER.FISCAL_MASTER_SUPLENTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_MASTER_SUPLENTE"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_SUPLENTE"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_SUPLENTE"].Habilitado = False
```
    - coluna MATRICULA_SUPLENTE obrigatório
    - coluna MATRICULA_FISCAL_MASTER obrigatório
    - coluna FISCAL_MASTER
**FISCAL_MASTER.FISCAL_MASTER.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_MASTER"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_FISCAL_MASTER"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_FISCAL_MASTER"].Habilitado = False
```
  - DIRETORIA_GERENCIA "Diretoria/Gerência (Área Cliente):" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA] obrigatório
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO] obrigatório
  - RESPONSAVEL_PROCESSO "Responsável pela Condução do Processo na Dilic" [DropDownList String → CPE_CSC.RESPONSAVEL_PROCESSO] obrigatório
  - DataInicioPrevisto (nativo) "Data da Assinatura do Documento Contratual" obrigatório
  - SIM_NAO3 "Serviço Fiscalizado por mais de um Fiscal (Comissão): " [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
  - SIM_NAO4 "Possui Mapa de Gerenciamento de Riscos?" [DropDownList String → CPE_CSC.SIM_NAO4] obrigatório
  - TIPO_ATIVIDADE "Tipo de Atividade - informe" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
#if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
#    Formulario['INFORMATIVO_CESEC'].Habilitado = True
#    Formulario['INFORMATIVO_CESEC'].Visivel = True
#    Formulario['DADOS_CONTRATOS_C'].Habilitado = True
#    Formulario['DADOS_CONTRATOS_C'].Visivel = True
#
#if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
#    Formulario['INFORMATIVO_CESEC'].Habilitado = False
#    Formulario['INFORMATIVO_CESEC'].Visivel = False
#    Formulario['DADOS_CONTRATOS_C'].Habilitado = False
#    Formulario['DADOS_CONTRATOS_C'].Visivel = False
```
  - FISCAL_SER "Fiscal do Serviço" [DataGrid RecordList → Z_00143_FISCAL_SER.FISCAL_SER] obrigatório
    - coluna MATRICULA_FISCAL_SUPLENTE obrigatório
    - coluna FISCAL_SERVICO obrigatório
**FISCAL_SER.FISCAL_SERVICO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_SERVICO"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_FISCAL_SERVICO"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_FISCAL_SERVICO"].Habilitado = False
```
    - coluna FISCAL_SUPLENTE obrigatório
**FISCAL_SER.FISCAL_SUPLENTE.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(FormularioRegistro["FISCAL_SUPLENTE"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

FormularioRegistro["MATRICULA_FISCAL_SUPLENTE"].Valor = pessoa["MATRICULA"]

FormularioRegistro["MATRICULA_FISCAL_SUPLENTE"].Habilitado = False
```
    - coluna MATRICULA_FISCAL_SERVICO obrigatório
  - URL3 "Link da pasta/dossiê digital" [TextBox String → CPE_CSC.URL3] obrigatório
  - DescricaoDetalhada (nativo)
    - coluna CONDICAO_USO obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna NUMERO_PATRIMONIO obrigatório
  - SIM_NAO1 "Publicar o extrato no DOU do Instrumento Contratual no site da BBTS?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario['SIM_NAO1'].Valor == "Sim":
    Formulario['URL2'].Visivel = True
    Formulario['URL2'].Habilitado = True
    Formulario['OBS1'].Visivel = True
    Formulario['OBS1'].Habilitado = True
    Formulario['RESPONSAVEL_INFORMACAO'].Visivel = True
    Formulario['RESPONSAVEL_INFORMACAO'].Habilitado = True
   
if Formulario['SIM_NAO1'].Valor != "Sim":
    Formulario['URL2'].Visivel = False
    Formulario['URL2'].Habilitado = False 
    Formulario['OBS1'].Visivel = False
    Formulario['OBS1'].Habilitado = False
    Formulario['RESPONSAVEL_INFORMACAO'].Visivel = False
    Formulario['RESPONSAVEL_INFORMACAO'].Habilitado = False
```
  - LABEL1 "Solicito por gentileza, publicação da RTF no Diário Oficial da União. Ao finalizar o procedimento, peço por gentileza anexar no chamado o Extrato do DOU. " [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - URL2 "Informe o URL da página para publicação do extrato no DOU do Instrumento Contratual no site da BBTS." [TextBox String → CPE_CSC.URL2] obrigatório
  - RESPONSAVEL_INFORMACAO "Responsável pela Informação - Será enviado a equipe de Comunicação" [DropDownList String → CPE_CSC.RESPONSAVEL_INFORMACAO] obrigatório
  - OBJETO_CONTRATO "Objeto da Contratação" [Memo String(1999) → CPE_CSC.OBJETO_CONTRATO] obrigatório
  - RESUMO "Resumo do Objeto do Contrato" [Memo String(2000) → CP_ORDEM_SERVICO.RESUMO] obrigatório
  - DATA_ENCERRA "Vigência (Data final do contrato) " [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENCERRA] obrigatório
  - CSC_DATA_INICIO "Início da Vigência" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO] obrigatório
  - CSC_DATA_FIM "Fim da Vigência" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
  - NOME_FORNECEDOR "Nome do Fornecedor" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
    - coluna BBTS obrigatório
**NOME_FORNECEDOR.BBTS.ScriptModificado**
```python
if FormularioRegistro["BBTS"].Valor == "BB TECNOLOGIA E SERVIÇOS S.A":
    FormularioRegistro["CNPJ"].Itens = "42.318.949/0069-72;42.318.949/0063-87;42.318.949/0015-80;42.318.949/0006-99;42.318.949/0016-60;42.318.949/0013-18;42.318.949/0017-41;42.318.949/0069-72;42.318.949/0037-95;42.318.949/0044-14;42.318.949/0005-08;42.318.949/0009-31;42.318.949/0019-03;42.318.949/0020-47;42.318.949/0061-15;42.318.949/0064-68;42.318.949/0012-37;42.318.949/0051-43;42.318.949/0027-13;42.318.949/0030-19;42.318.949/0023-90;42.318.949/0011-56;42.318.949/0071-97;42.318.949/0013-18;42.318.949/0068-91;42.318.949/0004-27;42.318.949/0008-50;42.318.949/0001-84;42.318.949/0010-75;42.318.949/0007-70;42.318.949/0054-96;42.318.949/0004-27;42.318.949/0033-61;42.318.949/0029-85;42.318.949/0031-08;42.318.949/0005-08;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0008-50;42.318.949/0069-72;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0069-72;42.318.949/0004-27"
```
    - coluna DESCRICAO obrigatório
    - coluna CNPJ obrigatório
**NOME_FORNECEDOR.CNPJ.ScriptModificado**
```python
#FormularioRegistro["CNPJ"].Itens = "42.318.949/0069-72;42.318.949/0063-87;42.318.949/0015-80;42.318.949/0006-99;42.318.949/0016-60;42.318.949/0013-18;42.318.949/0017-41;42.318.949/0069-72;42.318.949/0037-95;42.318.949/0044-14;42.318.949/0005-08;42.318.949/0009-31;42.318.949/0019-03;42.318.949/0020-47;42.318.949/0061-15;42.318.949/0064-68;42.318.949/0012-37;42.318.949/0051-43;42.318.949/0027-13;42.318.949/0030-19;42.318.949/0023-90;42.318.949/0011-56;42.318.949/0071-97;42.318.949/0013-18;42.318.949/0068-91;42.318.949/0004-27;42.318.949/0008-50;42.318.949/0001-84;42.318.949/0010-75;42.318.949/0007-70;42.318.949/0054-96;42.318.949/0004-27;42.318.949/0033-61;42.318.949/0029-85;42.318.949/0031-08;42.318.949/0005-08;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0013-18;42.318.949/0008-50;42.318.949/0069-72;42.318.949/0004-27;42.318.949/0013-18;42.318.949/0069-72;42.318.949/0004-27"
```
  - OBS21 "Objeto do Contrato" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - FAVORECIDO_TODOS "Solicitante da área contratante (Cliente)" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_TODOS"].Valor != "" and Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    

#########################################################################################################################################    
    result_table = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, PESSOA.ID_PESSOA, PESSOA.NOME, ORGAO.DESCRICAO, ORGAO.SIGLA, ORGAO.ID_ORGAO From PESSOA Inner Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Where PESSOA.ID_PESSOA = '"+ str(idFavorecidoCustom) +"'")
                            
    divisao = ''
    idOrgao = 0

    for row in result_table .Rows:
        divisao = str(row['DESCRICAO'])
        idOrgao = str(row['SIGLA'])
        
    Formulario['SCR_TODOS_RH'].Valor = idOrgao
    Formulario['SCR_TODOS_RH'].Habilitado = False
    
else:
    Formulario['SCR_TODOS_RH'].Habilitado = True
```
  - SCR_TODOS_RH "Área contratante (Cliente)" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório — Configuracao={"Mascara":"00000/0000"}
  - DATA1 "Data de Publicação no DOU" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA1] obrigatório
  - CONTRATO_ADITIVO "Contrato ou Aditivo?" [DropDownList String → CPE_CONTRATOS.CONTRATO_ADITIVO] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Instrumento Contratual Assinado" classes: Instrumento Contratual Assinado — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=RTF
  - anexo "RTF - Extrato do Contrato" classes: RTF — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=MAPAGERISCOS
  - anexo "Mapa de Gerenciamento de Riscos" classes: Mapa de Gerenciamento de Riscos — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - TIPO_SOLICITACAO_OC "Tipo de Solicitação" [DropDownList String → CPE_CSC.TIPO_SOLICITACAO_OC] obrigatório
  - TIPO_OC_CSC "Tipo de OC" [DropDownList String → CPE_CSC.TIPO_OC_CSC] obrigatório
  - OBS5 "Descrição Detalhada" [Memo String(2000) → CPE_CONTRATOS.OBS5]
  - FISICA_JUDIRICA "Pessoa Jurídica ou Pessoa Física" [DropDownList String → CPE_CSC.FISICA_JUDIRICA] obrigatório
**FISICA_JUDIRICA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['FISICA_JUDIRICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CNPJ_FORNECEDOR'].Habilitado = True
    Formulario['CNPJ_FORNECEDOR'].Visivel = True

if Formulario['FISICA_JUDIRICA'].Valor != "Pessoa Jurídica":
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CNPJ_FORNECEDOR'].Habilitado = False
    Formulario['CNPJ_FORNECEDOR'].Visivel = False
```
  - CNPJ_FORNECEDOR "CNPJ do Fornecedor" [TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - CSC_CPF "CPF" [TextBox String(300) → CPE_CSC.CSC_CPF] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"000\\.000\\.000\\-00"}
  - SIM_NAO6 "Aprovar/Revisar OC?" [DropDownList String → CPE_CSC.SIM_NAO6] obrigatório
**SIM_NAO6.ScriptModificado**
```python
if Formulario['SIM_NAO6'].Valor == "Sim":
    Formulario['NUMERO_OC'].Habilitado = True
    Formulario['NUMERO_OC'].Visivel = True
    Formulario['NUMERO_RC'].Habilitado = True
    Formulario['NUMERO_RC'].Visivel = True    
    Formulario['NOME_FORNECEDOR'].Habilitado = True
    Formulario['NOME_FORNECEDOR'].Visivel = True
    Formulario['TIPO_SOLICITACAO_OC'].Habilitado = True
    Formulario['TIPO_SOLICITACAO_OC'].Visivel = True
    Formulario['TIPO_OC_CSC'].Habilitado = True
    Formulario['TIPO_OC_CSC'].Visivel = True
   ## Formulario['MODALIDADE_LICITACAO'].Habilitado = True
   ## Formulario['MODALIDADE_LICITACAO'].Visivel = True
    Formulario['FISICA_JUDIRICA'].Habilitado = True
    Formulario['FISICA_JUDIRICA'].Visivel = True
    Formulario['OBS5'].Habilitado = True
    Formulario['OBS5'].Visivel = True   
    
if Formulario['SIM_NAO6'].Valor != "Sim":
    Formulario['NUMERO_OC'].Habilitado = False
    Formulario['NUMERO_OC'].Visivel = False
    Formulario['NUMERO_RC'].Habilitado = False
    Formulario['NUMERO_RC'].Visivel = False    
    Formulario['NOME_FORNECEDOR'].Habilitado = False
    Formulario['NOME_FORNECEDOR'].Visivel = False
    Formulario['CNPJ_FORNECEDOR'].Habilitado = False
    Formulario['CNPJ_FORNECEDOR'].Visivel = False
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CSC_CPF'].Visivel = False    
    Formulario['TIPO_SOLICITACAO_OC'].Habilitado = False
    Formulario['TIPO_SOLICITACAO_OC'].Visivel = False
    Formulario['TIPO_OC_CSC'].Habilitado = False
    Formulario['TIPO_OC_CSC'].Visivel = False
   ## Formulario['MODALIDADE_LICITACAO'].Habilitado = False
   ## Formulario['MODALIDADE_LICITACAO'].Visivel = False
    Formulario['FISICA_JUDIRICA'].Habilitado = False
    Formulario['FISICA_JUDIRICA'].Visivel = False
    Formulario['OBS5'].Habilitado = False
    Formulario['OBS5'].Visivel = False
```
  - NUMERO_OC "Número da OC (Inserir 0 caso não haja)" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC]
  - NUMERO_RC "Número da RC (se houver)" [TextBox String → CPE_CSC.NUMERO_RC]
- Operação PR0004 Associar Itens Configuração: Nome=INSTRUMENTOCONTRATUAL
  - anexo "Instrumento contratual com certificado de assinaturas" classes: Instrumento contratual com certificado de assinaturas — RequeridoInicial=true; IncluirPaginaAssinatura=true
  - anexo "Instrumento contratual sem certificado de assinaturas" classes: Instrumento contratual sem certificado de assinaturas — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=DBCROC
  - anexo "DADOS BÁSICOS PARA CRIAÇÃO DE REQUISIÇÃO E ORDEM DE COMPRA" classes: FQ415-075 - DADOS BÁSICOS PARA CRIAÇÃO DE REQUISIÇÃO DE COMPRAS — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração: Nome=PROJETOBASIC
  - anexo "Projeto Básico" classes: Projeto Básico — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Demais Documentos" classes: Arquivo — RequeridoInicial=true; PermiteMultiplosItens=true; IncluirPaginaAssinatura=true

### [344460] Tarefa "Automática"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
correcoes = OrdemServico.ObtemMotivoReprovacao('VERIFICAROC').ToString()
OrdemServico.SetCustom('OBS4', correcoes)
AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
Formulario['SIM_NAO200'].Itens = 'Sim;Não'
Formulario['SIM_NAO201'].Itens = 'Sim;Não'
Formulario['SIM_NAO203'].Itens = 'Sim;Não'
Formulario['SIM_NAO204'].Itens = 'Sim;Não'
Formulario['SIM_NAO_100'].Itens = 'Sim;Não'


Formulario['SIM_NAO200'].Habilitado = False
Formulario['SIM_NAO201'].Habilitado = False
Formulario['SIM_NAO203'].Habilitado = False
Formulario['SIM_NAO204'].Habilitado = False
Formulario['SIM_NAO_100'].Habilitado = False
Formulario['OBS4'].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - SIM_NAO204 "Tipo da ordem de compra de acordo?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO204]
  - SIM_NAO_100 "Condição de pagamento" [DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100]
  - OBS4 "Apontamentos" [Memo String(2000) → CPE_CONTRATOS.OBS4]
  - SIM_NAO200 "Valores unitários e totais;" [DropDownList String → CPE_CSC.SIM_NAO200]
  - SIM_NAO201 "DGCO de acordo com a contratação?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO201]
  - SIM_NAO203 "Modalidade de acordo com a contratação?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO203]

### [344461] EventoIntermediarioMensagem "Reprovação por falta de ajustes"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação por falta de ajustes
Corpo do comunicado: Prezado(a),
A Ordem de Serviço OrdemServico.Numero foi cancelado automaticamente por falta de ajustes.
Para realizar este serviço abra uma nova solicitação.
Para maiores informações Link.Consulta.
Atenciosamente,
Central de Serviços

### [344462] SubProcesso "Publicar no site da BBTS"
Responsável: Fila CSC - Contratos (papel 688)
Config: ChamadaAssincrona=true; AssociacaoId=1220; Configuracao={"ExibirBotaoNovaSubprocessos":true}
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "DOCUMENTOSPUBLICOS")
```
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=1962; CustomProperty=RESPONSAVEL_INFORMACAO
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=1537; CustomProperty=OBS2
  - CustomPropertyId=1087; CustomProperty=URL1
  - CustomPropertyId=1274; CustomProperty=SIM_NAO_INFRA
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2799; ClasseConfiguracao=Instrumento contratual sem certificado de assinaturas
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2440; ClasseConfiguracao=Matéria não certificada
  - SuperClasse=Artefato; ClasseConfiguracaoId=2398; ClasseConfiguracao=Extrato da Publicação no DOU
  - SuperClasse=Artefato; ClasseConfiguracaoId=2399; ClasseConfiguracao=Matéria Certificada
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Licitações e Contratos - Publicação Site da BBTS; FraseInversaAssociacao=Licitações e Contratos - Publicação Site da BBTS -> Inserir Documentos Contratuais no Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PUBLICACAO_SITE_DA_BBTS; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Licitações e Contratos - Publicação BBTS

### [344463] EventoIntermediarioTimer "5 dias"
Config: TempoIntervalo=7200

### [344464] EventoIntermediarioMensagem "Verificar"
Destinatário: Favorecido Todos (papel 385)
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
# Função utilitária para conversão segura
def safe_str(x):
    return '' if x is None else x.ToString()

linkChamado = ''

# Campos vindos da OS (proteção para None)
dgco = safe_str(OrdemServico.GetCustom('DGCO_BB'))
idOs = safe_str(OrdemServico.Id)

objetoContrato = safe_str(OrdemServico.GetCustom('OBS21'))
idCondutor = OrdemServico.GetCustom('FAVORECIDO_TODOS')  # pode ser None
numeroOc = safe_str(OrdemServico.GetCustom('NUMERO_OC'))

# >>> ATENÇÃO: estes dois estavam faltando <<<
numeroContrato = safe_str(OrdemServico.GetCustom('NUMERO_CONTRATO'))    # ajuste o nome do campo conforme seu ambiente
clienteContrato = safe_str(OrdemServico.GetCustom('CLIENTE_CONTRATO'))  # ajuste se o nome for diferente

# Descobrir domínio (pode retornar None)
sql = "select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)
dom = safe_str(dom).upper()  # normalizamos para comparar

fornecedor = safe_str(OrdemServico.GetCustom('NOME_FORNECEDOR'))

# Montar link conforme domínio
if dom == 'HOMOLOGAÇÃO' or dom == 'HOMOLOGACAO':
    linkChamado = 'https://santacruz1.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&amp;TID=43'
elif dom == 'PRODUÇÃO' or dom == 'PRODUCAO':
    linkChamado = 'https://santacruz.bbts.com.br/Supravizio/Forms/Processo/Workspace/PainelOrdemServico/OSDadosPrincipais.aspx?OSID=' + idOs + '&amp;TID=43'
else:
    # fallback seguro (evita None no href)
    linkChamado = '#'

# Buscar dados do condutor (id pode ser None)
matriculaCondutor = ''
nomeCondutor = ''

if idCondutor is not None and safe_str(idCondutor) != '':
    result_table7 = DB.ExecuteDataTable(
        "Select CP_PESSOA.MATRICULA, PESSOA.ID_PESSOA, PESSOA.NOME "
        "From PESSOA Inner Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA "
        "Where PESSOA.ID_PESSOA = '" + safe_str(idCondutor) + "' AND PESSOA.ATIVO = 'Sim'"
    )
    for row in result_table7.Rows:
        matriculaCondutor = safe_str(row["MATRICULA"])
        nomeCondutor = safe_str(row["NOME"])

# Assunto
Mensagem.Assunto = "Verificação de OC"





Mensagem.Corpo = '<html><head><style>body{margin:0;padding:40px;font-family:Arial,sans-serif;color:#0033a0;background-color:#f5f5f5;} .container{background-color:#ffffff;border-radius:10px;padding:30px;box-shadow:0 4px 8px rgba(0,0,0,0.1);} h1{color:#0033a0;} p{margin-bottom:15px;line-height:1.6;} .button{display:inline-block;padding:12px 20px;font-size:16px;border-radius:5px;background-color:#0033a0;color:#ffffff;text-align:center;text-decoration:none;font-weight:bold;transition:background-color 0.3s ease;} .button:hover{background-color:#002080;} ul{margin-top:10px;margin-bottom:20px;padding-left:20px;} li{margin-bottom:8px;}</style></head><body><div class="container"><h1>Ordem de Compra Criada</h1><p>Prezado(a) <strong>' + safe_str(nomeCondutor) + '</strong> (<strong>' + safe_str(matriculaCondutor) + '</strong>),</p><p>Informamos que a Ordem de Compra <strong>' + numeroOc + '</strong> foi criada e está disponível para sua verificação de conformidade.</p><p><strong>Dados do Contrato:</strong></p><ul><li><strong>Número do Contrato:</strong> ' + safe_str(numeroContrato) + '</li><li><strong>Cliente:</strong> ' + safe_str(clienteContrato) + '</li><li><strong>Objeto:</strong> ' + objetoContrato.ToString() + '</li><li><strong>DGCO:</strong> ' + safe_str(dgco) + '</li><li><strong>Fornecedor:</strong> ' + safe_str(fornecedor) + '</li></ul><p>Para acessar a OS e realizar a verificação, clique no botão abaixo:</p><p><a href="' + safe_str(linkChamado) + '" class="button">Acessar OS</a></p><p>Atenciosamente,<br><strong>Central de Serviços</strong></p></div></body></html>'
```

### [344465] EventoIntermediarioMensagem "Aviso de Pendência e Ajustes"
Destinatário: Cliente e Responsavel Atual (papel 544)
Config: Codigo=AVISO
ModeloComunicado: Comunicado para Ajustes - 5 dias
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
A ordem de serviço número OrdemServico.Numero necessita de ajustes e informações. 
Pedimos por gentileza, efetuar os ajuste em até 5 (cinco) dias para não impactar no atendimento da sua solicitação. 
Ajustes necessários:
OrdemServico.Justificativa 
Após finalizar as correções clique na opção "Avançar".
Para maiores informações Link.Edicao .
Atenciosamente,
Central de Serviços

### [344466] SubProcesso "Publicar Extrato do DOU no site da BBTS"
Responsável: Fila CSC - Contratos (papel 688)
Config: ChamadaAssincrona=true; AssociacaoId=1084; Configuracao={"ExibirBotaoNovaSubprocessos":false}
- ValoresInputs:
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=1536; CustomProperty=OBS1
  - CustomPropertyId=1959; CustomProperty=URL2
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "DOCUMENTOSPUBLICOS")
```
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=1977; CustomProperty=SIM_NAO1
  - CustomPropertyId=1962; CustomProperty=RESPONSAVEL_INFORMACAO
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2398; ClasseConfiguracao=Extrato da Publicação no DOU
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Licitações e Contratos - Publicação Extrato DOU no site BBTS; FraseInversaAssociacao=Licitações e Contratos - Publicação Extrato DOU no site BBTS -> Inserir Documentos Contratuais no Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PUBLICACAO_EXTRATO_DOU; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Licitações e Contratos - Publicação Extrato DOU no site BBTS

### [344467] SubProcesso "Publicar no Siasg"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=330; Codigo=SIASG; Configuracao={"ExibirBotaoNovaSubprocessos":false}
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "SIASG")
```
  - PropertyId=1268; Property=DataHoraInicioPrevisto
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2223; ClasseConfiguracao=Anexo
  - SuperClasse=Artefato; ClasseConfiguracaoId=2799; ClasseConfiguracao=Instrumento contratual sem certificado de assinaturas
  - SuperClasse=Artefato; ClasseConfiguracaoId=2405; ClasseConfiguracao=Instrumento Contratual Assinado
- Associação: Ativo=true; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Publicar Documentos no SIASG; FraseInversaAssociacao=Publicar Documentos no SIASG -> Inserir Documentos Contratuais no Gescon; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=INSERIRGESCONSIASG; SeparadorSequencial=. | fonte: Inserir Documentos Contratuais no Sisccon → alvo: Publicar Documentos no SIASG - Sistema Integrado de Administração de Serviços Gerais

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
### papel 1378: Responsavel Processo
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("RESPONSAVEL_PROCESSO"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("RESPONSAVEL_PROCESSO")))

    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 385: Favorecido Todos
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_TODOS"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))

    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```
### papel 544: Cliente e Responsavel Atual
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Responsável atual (PessoaOrdemServico)

## Campos customizados usados (definição global)

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### OBS21 — Observação21
Memo String(4000) → CPE_CSC.OBS21

### NUMERO_OC — Número da OC
TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC

### DGCO_BB — DGCO
TextBox String(300) → CPE_FINANCEIRO.DGCO_BB

### OBJETO_CONTRATO — Objeto do contrato
Memo String(1999) → CPE_CSC.OBJETO_CONTRATO

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### SIM_NAO200 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO200
Itens: Sim;Não

### SIM_NAO201 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO201
Itens: Sim;Não

### SIM_NAO203 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO203
Itens: Sim;Não

### SIM_NAO204 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO204
Itens: Sim;Não

### SIM_NAO_100 — Sim ou Não
DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100
Itens: Sim;Não

### CSC_DGCO — DGCO
TextBox String → CPE_CSC.CSC_DGCO

### CONTRATO_ADITIVO — Contrato ou Aditivo?
DropDownList String → CPE_CONTRATOS.CONTRATO_ADITIVO
Itens: Contrato;Aditivo

### TIPO_ATIVIDADE — Tipo de Atividade - informe
DropDownList String → CPE_CSC.TIPO_ATIVIDADE
Descrição: Tipo de Atividade - Informe
Itens: Atividade Meio; Atividade Fim

### CATEGORIA_DE_COMPRA — Categoria de Compra
DropDownList String → CPE_CSC.CATEGORIA_DE_COMPRA

### MODALIDADE_DE_CONTRATACAO — Modalidade de Contratação
DropDownList String → CPE_CONTRATOS.MODALIDADE_DE_CONTRATACAO
Itens: CARONA EM ATA DE REGISTRO DE PREÇOS;CREDENCIAMENTO;CONCORRÊNCIA;CONTRATO DE PATROCÍNIO;CONVÊNIO;CONVITE;DISPENSA DE LICITAÇÃO;INAPLICABILIDADE DE LICITAÇÃO;INEXIGIBILIDADE DE LICITAÇÃO;LICITAÇÃO;LICITAÇÃO COM PRÉ-QUALIFICAÇÃO;LICITAÇÃO ELETRÔNICA;LICITAÇÃO ELETRÔNICA COM PRÉ-QUALIFICAÇÃO;PREGÃO ELETRÔNICO;RECONHECIMENTO DA OBRIGAÇÃO DE INDENIZAR;RESSARCIMENTO SEM AMPARO CONTRATUAL;SISTEMA DE REGISTRO DE PREÇOS;TOMADA DE PREÇOS

### FUNDAMENTACAO — Fundamentação Legal
DropDownList String → CPE_CSC.FUNDAMENTACAO

### DIRETORIA_GERENCIA — Diretoria/Gerência
TextBox String → CPE_CSC.DIRETORIA_GERENCIA

### PPGEREX_NEGOCIO — Gerente Executivo do Negócio
DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO
**LookupScript**
```python
#Itens = DB.ExecuteDataTable("Select Distinct to_char(PESSOA.ID_PESSOA) as id_pessoa,PESSOA.NOME_ABREVIADO From ORGAO Inner Join PESSOA On ORGAO.ID_GESTOR = PESSOA.ID_PESSOA Where ORGAO.ATIVO = 'Sim' And ORGAO.DESCRICAO Like '%GERE%' And PESSOA.ATIVO = 'Sim' Order By PESSOA.NOME_ABREVIADO")

Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(pessoa.id_pessoa) AS id_pessoa, pessoa.nome_abreviado FROM orgao INNER JOIN pessoa ON orgao.id_gestor = pessoa.id_pessoa INNER JOIN cp_pessoa ON cp_pessoa.id_pessoa = pessoa.id_pessoa WHERE (orgao.ativo = 'Sim' AND cp_pessoa.cargo_funcional LIKE '%EXECUTIVO%' AND pessoa.ativo = 'Sim') or pessoa.id_pessoa in (SELECT p.id_substituto_aprovacao FROM pessoa p INNER JOIN cp_pessoa   cp ON ( p.id_pessoa = cp.id_pessoa ) WHERE cp.cargo_funcional LIKE '%EXECUTIVO%' AND p.ativo = 'Sim' AND sysdate BETWEEN dt_inicio_substit_aprov AND dt_fim_substit_aprov) ORDER BY pessoa.nome_abreviado")
```

### RESPONSAVEL_PROCESSO — Responsável pela Condução do Processo
DropDownList String → CPE_CSC.RESPONSAVEL_PROCESSO
**LookupScript**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#seleção de funcionários BBTS
#Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(p.id_pessoa) AS id_pessoa, p.nome || ' (' || p.usuario_rede || ')' AS nomemat FROM CAD_FUNCIONARIO_V F, PESSOA P, cp_pessoa cpp WHERE p.id_pessoa = Cpp.Id_Pessoa AND F.Matricula = Cpp.Matricula AND F.DESC_COLABORADOR IN ('FUNCIONARIOS CCLP', 'CEDIDO BANCO DO BRASIL', 'ESTAGIARIO', 'FUNCIONARIOS CONCURSADOS', 'FUNCIONARIO CLT', 'DIRETOR EMPREGADO') AND f.status_matricula  = 'Ativo' AND p.ativo = 'Sim' ORDER BY nomemat ")

Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(p.id_pessoa) AS id_pessoa, p.nome || ' (' || p.usuario_rede || ')' AS nomemat FROM PESSOA P where p.ativo = 'Sim' ORDER BY nomemat ")
```

### NOME_NOME — Campo para Nome
TextBox String(100) → CPE_PESSOAS.NOME_NOME

### RETORNO_HORA — Horário do Retorno
TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA

### PORCENTAGEM_AMOSTRA — Porcentagem(%) da amostra verificada
TextBox String → CPE_NEGOCIOS.PORCENTAGEM_AMOSTRA

### CNPJ_FORNECEDOR — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR

### TOMADOR — TOMADOR
DataGrid RecordList → Z_00143_TOMADOR.TOMADOR
Colunas do registro:
- DESC_CNPJ "Descrição da Unidade BBTS" [DropDownList String] itens: [(Nenhum)];
- FATURA_CNPJ "Local Tomador/Faturamento" [DropDownList String] itens: [(Nenhum)];
- BBTS "BBTS" [DropDownList String] itens: BB TECNOLOGIA E SERVIÇOS S.A.
- CNPJ "CNPJ" [DropDownList String] itens: [(Nenhum)];

### VALOR_CONTRATADO — Valor Contratado
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_CONTRATADO

### COMBOBOX2 — COMBOBOX2
DropDownList String → CPE_BOOTCAMP.COMBOBOX2

### SIM_NAO_INFRA — Confirma envolvimento de sua área?
DropDownList String → CPE_ORDEM_SERVICO.SIM_NAO_INFRA
Itens: Sim;Não

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### INFORMATIVO_CESEC — Informativo
Label String(1500) → CPE_CSC.INFORMATIVO_CESEC

### DADOS_CONTRATOS_C — Contrato Clientes
DataGrid RecordList → Z_00143_DADOS_CONTRATOS_C.DADOS_CONTRATOS_C
Colunas do registro:
- NOME_CLIENTE "Nome do Cliente" [TextBox String]
- DGCO "N° DGCO" [TextBox String]
- VALOR "Valor do(s) contrato(s)" [TextBox Decimal]
- RUBRICA "Rubrica(s) do Contrato com  Cliente" [Memo String]

### FISICA_JUDIRICA — Pessoa Jurídica ou Pessoa Física
DropDownList String → CPE_CSC.FISICA_JUDIRICA
Itens: Pessoa Jurídica;Pessoa Física

### CSC_CPF — CPF
TextBox String(300) → CPE_CSC.CSC_CPF

### TIPO_SOLICITACAO_OC — Tipo de Solicitação
DropDownList String → CPE_CSC.TIPO_SOLICITACAO_OC
Itens: 
Contratos Existentes;
Novas compras e Contratações;
Liberação de OC Master;Taxa de Condomínio;Outro

### TIPO_OC_CSC — Tipo de OC
DropDownList String → CPE_CSC.TIPO_OC_CSC
Itens: OC Padrão;Liberação do Contrato Guarda-Chuva/Cobertura;OC vinculada à OC Acordo de Compra do Contrato;Acordo de Compra do Contrato;Acordo de Compra em Aberto; Outras Modalidades


### OBS5 — Observação5
Memo String(2000) → CPE_CONTRATOS.OBS5

### SIM_NAO6 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO6
Itens: Sim;Não

### NUMERO_RC — Número da RC
TextBox String → CPE_CSC.NUMERO_RC

### SIM_NAO_PROC — Confirma envolvimento de sua área?
DropDownList String → CPE_ORDEM_SERVICO.SIM_NAO_PROC
Itens: Sim;Não

### SIM_NAO5 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO5
Itens: Sim;Não

### CSC_DATA_INICIO — Data Início
DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO

### DATA1 — Data
DatePicker DateTime → CP_ORDEM_SERVICO.DATA1

### OBS2 — Observação2
Memo String(2000) → CPE_CONTRATOS.OBS2
Descrição: Informe

### URL1 — Endereço da Página WEB
TextBox String → CP_ORDEM_SERVICO.URL1

### CSC_DATA_FIM — Data Fim
DatePicker DateTime → CPE_CSC.CSC_DATA_FIM

### URL2 — URL2
TextBox String → CPE_CSC.URL2

### RESPONSAVEL_INFORMACAO — Responsável pela Informação
DropDownList String → CPE_CSC.RESPONSAVEL_INFORMACAO
**LookupScript**
```python
Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(p.id_pessoa) AS id_pessoa, p.nome || ' (' || p.usuario_rede || ')' AS nomemat FROM PESSOA P where p.ativo = 'Sim' ORDER BY nomemat ")
```

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

### TIPO_DOCUMENTO — Tipo de documento
DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO
Itens: Contrato;Aditivo;Ata de Registro de Preço; Apostilamento; Convênio

### SIM_NAO4 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO4
Itens: Sim;Não

### URL3 — Endereço da Página WEB
TextBox String → CPE_CSC.URL3

### SIM_NAO1 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO1
Itens: Sim;Não

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### SIM_NAO7 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO7
Itens: Sim;Não

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### FISCAL_SER — Fiscal do Serviço
DataGrid RecordList → Z_00143_FISCAL_SER.FISCAL_SER
Colunas do registro:
- FISCAL_SERVICO "Fiscal do Serviço" [DropDownList String]
**FISCAL_SERVICO.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- FISCAL_SUPLENTE "Fiscal do Serviço - Suplente" [DropDownList String]
**FISCAL_SUPLENTE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- MATRICULA_FISCAL_SERVICO "Matrícula" [TextBox String]
- MATRICULA_FISCAL_SUPLENTE "Matrícula" [TextBox String]

### FISCAL_MASTER — Fiscal do Serviço Master
DataGrid RecordList → Z_00143_FISCAL_MASTER.FISCAL_MASTER
Descrição: Preposto Contrato Cliente
Colunas do registro:
- FISCAL_MASTER "Fiscal do Serviço Master" [DropDownList String]
**FISCAL_MASTER.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- FISCAL_MASTER_SUPLENTE "Fiscal do Serviço Master - Suplente" [DropDownList String]
**FISCAL_MASTER_SUPLENTE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- MATRICULA_FISCAL_MASTER "Matrícula" [TextBox String]
- MATRICULA_SUPLENTE "Matrícula" [TextBox String]

### GESTOR_CONTRATO — Gestor do Contrato
DataGrid RecordList → Z_00143_GESTOR_CONTRATO.GESTOR_CONTRATO
Colunas do registro:
- GESTOR_CONTRATO "Gestor Demandante do Contrato" [DropDownList String]
**GESTOR_CONTRATO.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- GESTOR_CONTRATO_SUPLENTE "Gestor Demandante do Contrato - Suplente" [DropDownList String]
**GESTOR_CONTRATO_SUPLENTE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```
- MATRICULA_GESTOR "Matrícula" [TextBox String]
- MATRICULA_GESTOR_SUPLENTE "Matrícula" [TextBox String]

### VALOR_REF_CONT — Valor Referencial da Contratação
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_REF_CONT

### RESUMO — Recomendação
Memo String(2000) → CP_ORDEM_SERVICO.RESUMO
Descrição: Inteiro teor do texto da recomendação.

### DATA_ENCERRA — Data do encerramento
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENCERRA

### OBS4 — Observação4
Memo String(2000) → CPE_CONTRATOS.OBS4
Descrição: Informe

## Biblioteca de scripts referenciada
dicoc, teste
(fonte em catalogo/biblioteca/<Nome>.py)
