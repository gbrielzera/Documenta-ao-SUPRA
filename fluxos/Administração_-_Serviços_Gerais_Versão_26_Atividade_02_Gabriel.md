# Fluxo: Atividade 02 Gabriel (SERVDESPACHANTES) — versão 26
Caminho: Fluxos > Administração - Serviços Gerais Versão 26 Atividade 02 Gabriel
XML: `XMLs para teste/Administração_-_Serviços_Gerais_Versão_26_Atividade_02_Gabriel.xml` | Supravizio 19.1.1 | SubProcessoId 14755 | DesenhoProcessoId 2296 | ProcessoId 97
Órgão dono: 3000003150 - DIVISAO DE ENGENHARIA E GESTAO DE ESTABELECIMENTOS | Responsável: DAIANY NEVES ROSA
Classe do subprocesso: Objetivo=Serviços Despachantes; DescricaoCliente=Serviços Despachantes; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Serviços Despachantes; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Arquivamento de Ata (ARQUIVAMENTOATA); Certidões (CERTIDOES); Abertura de Estabelecimento (ABERESTABELECIMENTO); Alteração de Dados Cadastrais (ALTDADOSCADASTRAIS); Encerramento de Estabelecimento (ENCESTABELECIMENTO); Renovação de Alvará de funcionamento (RENOVALVARAESTAB); Renovação de AVCB (RENOVAVCB); Renovação de Licença Ambiental (RENOVLICENAMBIENTAL); Renovação de Vigilância Sanitária (RENOVVIGILANCIASANITARIA)

## Grafo do fluxo
- [229025] Tarefa "Anexar NF e Abrir RI" {Responsável atual} → [229014] Aguardar Pagamento
- [229003] FimCancelamento "" {Responsável atual} → (fim)
- [229004] EventoIntermediarioRegra "" → [229011] Aguardar Pagamento
- [229005] EventoInicial "Início" {Fila CSC - Serviços Gerais} → [G55825] Qual Serviço?
- [229015] Tarefa "Tarefa Automática Pesq. de mercado" {Fila Diapa} → [G55821] Inicio Pesq. de Mercado - Nota Técnica
- [229016] Tarefa "Analisar Solicitação" {Fila CSC - Serviços Gerais} → [G55817] Atender Solicitação?
- [229017] EventoFinal "" {Responsável atual} → (fim)
- [229018] FimCancelamento "" {Responsável atual} → (fim)
- [229019] Tarefa "Analisar Solicitação" {Fila CSC - Serviços Gerais} → [G55826] Atender Solicitação?
- [229020] Tarefa "Solicitar Aprovação do Superior Imediato" {Fila CSC - Pendente de Aprovação} → [229054] 7200 minutos | [G55811] Aprovado?
- [229021] Tarefa "Aguardar Pagamento" {Fila CSC - Pendente de Aprovação} → [229001]  | [229055] Conclusão de Chamado
- [229022] Tarefa "Elaborar Nota Técnica" {Responsável atual} → [229059] Gerar número - Ato de Diretoria
- [229023] Tarefa "Acionar Despachante e informar Serviços Solicitados" {Responsável atual} → [229024] Incluir documentos comprobatórios dos Serviços Sol
- [229024] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados" {Responsável atual} → [229025] Anexar NF e Abrir RI
- [229026] EventoIntermediarioRegra "" → [229014] Aguardar Pagamento
- [229027] Tarefa "Anexar NF e Abrir RI" {Responsável atual} → [229011] Aguardar Pagamento
- [229028] Tarefa "Acionar Despachante e informar Serviços Solicitados" {Responsável atual} → [229029] Incluir documentos comprobatórios dos Serviços Sol
- [229029] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados" {Responsável atual} → [G55828] Anexar NF e Abrir RI?
- [229030] Tarefa "Solicitar Aprovação do Superior Imediato" {Fila CSC - Pendente de Aprovação} → [229031] 7200 minutos | [G55815] Aprovado?
- [229031] EventoIntermediarioTimer "7200 minutos" → [229041] 
- [229032] Tarefa "Solicitar Aprovação do Superior Imediato" {Fila CSC - Pendente de Aprovação} → [229013] 7200 minutos | [G55818] Aprovado?
- [229034] Tarefa "Solicitar Ato para COJUR" {Responsável atual} → [229035] Requisições de manifestações Jurídicas - Consultas
- [229033] EventoIntermediarioMensagem "Conclusão de Chamado" → [229052] 
- [229035] SubProcesso "Requisições de manifestações Jurídicas - Consultas Matriz/CAT" {Responsável atual} → [G55820] Fim Pesq. de Mercado - Nota Técnica
- [229036] FimCancelamento "" {Responsável atual} → (fim)
- [229037] Tarefa "Acionar Despachante e informar Serviços Solicitados" {Responsável atual} → [229038] Incluir documentos comprobatórios dos Serviços Sol
- [229038] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados" {Responsável atual} → [G55813] Anexar NF e Abrir RI?
- [229039] Tarefa "Analisar Solicitação" {Fila CSC - Serviços Gerais} → [G55814] Atender Solicitação?
- [229040] FimCancelamento "" {Responsável atual} → (fim)
- [229041] FimCancelamento "" {Responsável atual} → (fim)
- [229042] EventoIntermediarioMensagem "Conclusão de Chamado" → [G55829] Tipo de Processo?
- [229047] FimCancelamento "" {Responsável atual} → (fim)
- [229043] Tarefa "Tarefa Automática" {Responsável atual} → [G55824] Inicio Despachante Arquivamento
- [229044] EventoFinal "" {Responsável atual} → (fim)
- [229045] FimCancelamento "" {Responsável atual} → (fim)
- [229046] Tarefa "Anexar NF e Abrir RI" {Responsável atual} → [229007] Aguardar Pagamento
- [229048] FimCancelamento "" {Responsável atual} → (fim)
- [229049] Tarefa "Aguardar Liberação de OC Master e Nota Fiscal do Fornecedor." {Responsável atual} → [229046] Anexar NF e Abrir RI
- [229050] Tarefa "Aguardar Liberação de OC Master e Nota Fiscal do Fornecedor." {Responsável atual} → [229000] Anexar NF e Abrir RI
- [229051] Tarefa "Acionar Despachante e informar Serviços Solicitados" {Responsável atual} → [229063] Incluir documentos comprobatórios dos Serviços Sol
- [229052] EventoFinal "" {Responsável atual} → (fim)
- [229053] EventoIntermediarioRegra "" → [229007] Aguardar Pagamento
- [229054] EventoIntermediarioTimer "7200 minutos" → [229057] 
- [229055] EventoIntermediarioMensagem "Conclusão de Chamado" → [229056] 
- [229056] EventoFinal "" {Responsável atual} → (fim)
- [229057] FimCancelamento "" {Responsável atual} → (fim)
- [229058] Tarefa "Tarefa Automática" {Responsável atual} → [G55816] Fim Despachante Arquivamento
- [229061] Tarefa "Solicitar Validação do Serviço ao Superior Imediato" → [229062] 7200 minutos | [G55812] Aprovado?
- [229062] EventoIntermediarioTimer "7200 minutos" → [229027] Anexar NF e Abrir RI
- [229063] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados" {Responsável atual} → [229061] Solicitar Validação do Serviço ao Superior Imediat
- [229059] Tarefa "Gerar número - Ato de Diretoria" {Fila CSC - Serviços Gerais} → [229060] Numeração para documentos
- [229060] SubProcesso "Numeração para documentos" {Responsável atual} → [229034] Solicitar Ato para COJUR
- [229000] Tarefa "Anexar NF e Abrir RI" {Responsável atual} → [229021] Aguardar Pagamento
- [229001] EventoIntermediarioRegra "" → [229021] Aguardar Pagamento
- [229002] Tarefa "Analisar Solicitação" {Fila Diapa} → [G55819] Atender Solicitação?
- [229014] Tarefa "Aguardar Pagamento" {Fila CSC - Pendente de Aprovação} → [229026]  | [229042] Conclusão de Chamado
- [229009] SubProcesso "Pesquisa de mercado" {Responsável atual} → [G55820] Fim Pesq. de Mercado - Nota Técnica
- [229010] FimCancelamento "" {Responsável atual} → (fim)
- [229008] Tarefa "Informar dados para pesquisa de mercado" {Fila CSC - Serviços Gerais} → [229009] Pesquisa de mercado
- [229006] Tarefa "Informar Dados para Arquivamento Despachante Rio" {Fila Diapa} → [G55817] Atender Solicitação?
- [229012] EventoIntermediarioMensagem "Conclusão de Chamado" → [229044] 
- [229013] EventoIntermediarioTimer "7200 minutos" → [229036] 
- [229007] Tarefa "Aguardar Pagamento" {Fila CSC - Pendente de Aprovação} → [229053]  | [229012] Conclusão de Chamado
- [229011] Tarefa "Aguardar Pagamento" {Fila CSC - Pendente de Aprovação} → [229004]  | [229033] Conclusão de Chamado
- [G55811] Gateway "Aprovado?" → «Não» [229010]  | «Sim» [229019] Analisar Solicitação
- [G55812] Gateway "Aprovado?" → «Sim» [229027] Anexar NF e Abrir RI | «Não» [229051] Acionar Despachante e informar Serviços Solicitado
- [G55813] Gateway "Anexar NF e Abrir RI?" → «Sim» [229049] Aguardar Liberação de OC Master e Nota Fiscal do F | «Não» [229012] Conclusão de Chamado
- [G55814] Gateway "Atender Solicitação?" → «Não» [229048]  | «Sim» [229028] Acionar Despachante e informar Serviços Solicitado
- [G55815] Gateway "Aprovado?" → «Não» [229040]  | «Sim» [229039] Analisar Solicitação
- [G55816] Gateway "Fim Despachante Arquivamento" → «Fim» [229051] Acionar Despachante e informar Serviços Solicitado
- [G55817] Gateway "Atender Solicitação?" → «Não» [229018]  | «Sim» [229023] Acionar Despachante e informar Serviços Solicitado
- [G55818] Gateway "Aprovado?" → «Sim» [229002] Analisar Solicitação | «Não» [229047] 
- [G55819] Gateway "Atender Solicitação?" → «Não» [229003]  | «Sim» [G55822] Qual UF?
- [G55820] Gateway "Fim Pesq. de Mercado - Nota Técnica" → [G55823] Qual UF?
- [G55821] Gateway "Inicio Pesq. de Mercado - Nota Técnica" → «Nota Técnica» [229022] Elaborar Nota Técnica | «Pesquisa de Mercado» [229008] Informar dados para pesquisa de mercado
- [G55822] Gateway "Qual UF?" → «RJ» [229022] Elaborar Nota Técnica | «Outros» [G55827] Deseja iniciar uma pesquisa de mercado?
- [G55823] Gateway "Qual UF?" → «Outros» [229043] Tarefa Automática | «RJ» [229051] Acionar Despachante e informar Serviços Solicitado
- [G55824] Gateway "Inicio Despachante Arquivamento" → «Novo» [229016] Analisar Solicitação | «SubProcesso» [229006] Informar Dados para Arquivamento Despachante Rio
- [G55825] Gateway "Qual Serviço?" → «Certidões» [229020] Solicitar Aprovação do Superior Imediato | «Arquivamento» [229016] Analisar Solicitação | «Estabelecimento» [229032] Solicitar Aprovação do Superior Imediato | «Renovação» [229030] Solicitar Aprovação do Superior Imediato
- [G55826] Gateway "Atender Solicitação?" → «Não» [229045]  | «Sim» [229037] Acionar Despachante e informar Serviços Solicitado
- [G55827] Gateway "Deseja iniciar uma pesquisa de mercado?" → «Sim» [229015] Tarefa Automática Pesq. de mercado | «Não» [229022] Elaborar Nota Técnica
- [G55828] Gateway "Anexar NF e Abrir RI?" → «Sim» [229050] Aguardar Liberação de OC Master e Nota Fiscal do F | «Não» [229055] Conclusão de Chamado
- [G55829] Gateway "Tipo de Processo?" → [G55816] Fim Despachante Arquivamento | «SubProcesso» [229058] Tarefa Automática | «Novo» [229017] 

## Gateways
### [G55811] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVSUPIMEDIATO CERT")
```
- alternativa → [229010] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [229019] Analisar Solicitação: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
### [G55812] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVSUPIMEDIATO")
```
- alternativa → [229027] Anexar NF e Abrir RI: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [229051] Acionar Despachante e informar Serviços Solicitado: SequenciaAvaliacao=2; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G55813] Anexar NF e Abrir RI? (EventBasedExclusiveDecision)
Codigo=RI
- alternativa → [229049] Aguardar Liberação de OC Master e Nota Fiscal do F: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
- alternativa → [229012] Conclusão de Chamado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
### [G55814] Atender Solicitação? (EventBasedExclusiveDecision)
Codigo=ATENDER REN
- alternativa → [229048] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [229028] Acionar Despachante e informar Serviços Solicitado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
### [G55815] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVSUPIMEDIATO RENO")
```
- alternativa → [229040] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [229039] Analisar Solicitação: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
### [G55816] Fim Despachante Arquivamento (DataBasedInclusiveDecision)
- alternativa → [229051] Acionar Despachante e informar Serviços Solicitado: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Fim
### [G55817] Atender Solicitação? (EventBasedExclusiveDecision)
Codigo=ATENDER ATA
- alternativa → [229018] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [229023] Acionar Despachante e informar Serviços Solicitado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
### [G55818] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVSUPIMEDIATO EST")
```
- alternativa → [229002] Analisar Solicitação: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [229047] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```
### [G55819] Atender Solicitação? (EventBasedExclusiveDecision)
Codigo=ATENDER EST
- alternativa → [229003] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G55822] Qual UF?: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
### [G55820] Fim Pesq. de Mercado - Nota Técnica (Parallel)
Codigo=3
- alternativa → [G55823] Qual UF?: SequenciaAvaliacao=1; OperadorDecision=Equal
### [G55821] Inicio Pesq. de Mercado - Nota Técnica (Parallel)
Codigo=2
- alternativa → [229022] Elaborar Nota Técnica: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Nota Técnica
- alternativa → [229008] Informar dados para pesquisa de mercado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Pesquisa de Mercado
### [G55822] Qual UF? (DataBasedExclusiveDecision)
Codigo=ESTAB
**ExpressaoComparacaoDecision**
```python
OrdemServico["CSC_UF"].ToString()
```
- alternativa → [229022] Elaborar Nota Técnica: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=RJ
**ValorComparacaoDecision**
```python
'RJ'
```
- alternativa → [G55827] Deseja iniciar uma pesquisa de mercado?: SequenciaAvaliacao=1; OperadorDecision=NotEqual; ReferenciaDecision=Outros
**ValorComparacaoDecision**
```python
'RJ'
```
### [G55823] Qual UF? (DataBasedExclusiveDecision)
Codigo=ARQU
**ExpressaoComparacaoDecision**
```python
OrdemServico["CSC_UF"].ToString()
```
- alternativa → [229043] Tarefa Automática: SequenciaAvaliacao=1; OperadorDecision=NotEqual; ReferenciaDecision=Outros
**ValorComparacaoDecision**
```python
'RJ'
```
- alternativa → [229051] Acionar Despachante e informar Serviços Solicitado: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=RJ
**ValorComparacaoDecision**
```python
'RJ'
```
### [G55824] Inicio Despachante Arquivamento (DataBasedInclusiveDecision)
- alternativa → [229016] Analisar Solicitação: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Novo
**ValorComparacaoDecision**
```python
1==2
```
- alternativa → [229006] Informar Dados para Arquivamento Despachante Rio: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=SubProcesso
**ValorComparacaoDecision**
```python
1==1
```
### [G55825] Qual Serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.ClasseServico.Sigla.ToString()
```
- alternativa → [229020] Solicitar Aprovação do Superior Imediato: SequenciaAvaliacao=3; OperadorDecision=Equal; ReferenciaDecision=Certidões
**ValorComparacaoDecision**
```python
'DESPCERTIDOES'
```
- alternativa → [229016] Analisar Solicitação: SequenciaAvaliacao=2; OperadorDecision=Equal; ReferenciaDecision=Arquivamento
**ValorComparacaoDecision**
```python
'DESPARQUIVAMENTO'
```
- alternativa → [229032] Solicitar Aprovação do Superior Imediato: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Estabelecimento
**ValorComparacaoDecision**
```python
'DESPESTABELECIMENTO'
```
- alternativa → [229030] Solicitar Aprovação do Superior Imediato: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Renovação
**ValorComparacaoDecision**
```python
'DESPRENOVACAO'
```
### [G55826] Atender Solicitação? (EventBasedExclusiveDecision)
Codigo=ATENDER CERT
- alternativa → [229045] : SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```
- alternativa → [229037] Acionar Despachante e informar Serviços Solicitado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
### [G55827] Deseja iniciar uma pesquisa de mercado? (EventBasedExclusiveDecision)
- alternativa → [229015] Tarefa Automática Pesq. de mercado: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
Sim
```
- alternativa → [229022] Elaborar Nota Técnica: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
Sim
```
### [G55828] Anexar NF e Abrir RI? (EventBasedExclusiveDecision)
Codigo=ANEXARNFRI
- alternativa → [229050] Aguardar Liberação de OC Master e Nota Fiscal do F: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim
- alternativa → [229055] Conclusão de Chamado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não
### [G55829] Tipo de Processo? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.OcorrenciaPrincipalId
```
- alternativa → [G55816] Fim Despachante Arquivamento: SequenciaAvaliacao=2; OperadorDecision=Equal
**ValorComparacaoDecision**
```python
1
```
- alternativa → [229058] Tarefa Automática: SequenciaAvaliacao=1; OperadorDecision=NotNull; ReferenciaDecision=SubProcesso
**ValorComparacaoDecision**
```python
True
```
- alternativa → [229017] : SequenciaAvaliacao=0; OperadorDecision=Null; ReferenciaDecision=Novo
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [229025] Tarefa "Anexar NF e Abrir RI"
Responsável: Responsável atual (papel 36)
**ScriptValidacao**
```python
texto=''

ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

if ri !='' and organizacao!= '':

    sqlRI= DB.ExecuteScalar("select count(a.OPERATION_ID) RI from CLL_F189_ENTRY_OPERATIONS a where 1=1 and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' order by a.OPERATION_ID")


    if sqlRI == 0:
        sqlOrganizacao= DB.ExecuteScalar("SELECT ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS WHERE ORGANIZATION_ID = '"+organizacao.ToString()+"' ORDER BY ORGANIZACAO")
        texto = texto+'RI não encontrado para Organização '+sqlOrganizacao.ToString()+' e Número '+ri.ToString()+' informados.\n'

if texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0001 Preencher Campos
  - CSC_RI "Nº RI" [TextBox String → CPE_CSC.CSC_RI]
  - CSC_ORGANIZACAO "Organização" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL ATA
  - anexo "Nota Fiscal" classes: Nota Fiscal — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_CARGO_FUNCAO "Cargo - Função" [TextBox String → CPE_CSC.CSC_CARGO_FUNCAO] obrigatório
  - CSC_UF "UF do Estabelecimento" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_OBS "Descrição Detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS]
- Operação PR0001 Preencher Campos
  - LISTA_ATIV_DESP_RJ "Lista de Atividades Despachante/RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] — QtdColunasFormulario=1
    - coluna ATIVIDADE obrigatório
**LISTA_ATIV_DESP_RJ.ATIVIDADE.ScriptModificado**
```python
servico = OrdemServico.Servico.Descricao.ToString()
FormularioRegistro["VALOR"].Valor = ''
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento))" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'

if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'
    

    
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'    
    

    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais (Encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    

if (servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária") and (FormularioRegistro["ATIVIDADE"].Valor =="Taxas de Licenças de Estabelecimento"):
    FormularioRegistro["VALOR"].Valor = '100'

    
if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Renovação do AVCB"):
    FormularioRegistro["VALOR"].Valor = '300'

if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Certificado de Aprovação do Corpo de Bombeiros"):
    FormularioRegistro["VALOR"].Valor = '200'

    

if servico == "Arquivamento de Ata" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'


if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviços para Regularização da Certidão Municipal do IPTU"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço de Retirada de Certidão Simplificada na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Municipal - IPTU" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver." or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver)"):
    FormularioRegistro["VALOR"].Valor = '100'    
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel"):
    FormularioRegistro["VALOR"].Valor = '150'
    
    
if servico == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if servico == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if servico == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if servico == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if servico == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if servico == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
    - coluna SERVICO
**LISTA_ATIV_DESP_RJ.SERVICO.ScriptModificado**
```python
FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Taxas de Licenças de Estabelecimento;Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"

FormularioRegistro["ATIVIDADE"].Valor = None
FormularioRegistro["Valor"].Valor = None

if FormularioRegistro["SERVICO"].Valor == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if FormularioRegistro["SERVICO"].Valor == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if FormularioRegistro["SERVICO"].Valor == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if FormularioRegistro["SERVICO"].Valor == "Renovação de Alvara de funcionamento" or FormularioRegistro["SERVICO"].Valor == "Renovação de Licença Ambiental" or FormularioRegistro["SERVICO"].Valor == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if FormularioRegistro["SERVICO"].Valor == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if FormularioRegistro["SERVICO"].Valor == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if FormularioRegistro["SERVICO"].Valor == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
    - coluna VALOR

### [229003] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoGateway("ATENDER")
```

### [229004] EventoIntermediarioRegra ""
**Regra**
```python
1<>2
```

### [229005] EventoInicial "Início"
Responsável: Fila CSC - Serviços Gerais (papel 483)
TipoSolicitacao: 10.03. Administração e Patrimônio - Serviços Gerais
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Servico
OrdemServico.Assunto = OrdemServico.SubProcesso.ToString() +' - ' + OrdemServico.Servico.Descricao
pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
Formulario["CSC_MATRICULA"].Valor = pessoa["MATRICULA"].ToString()
Formulario["CSC_CARGO_FUNCAO"].Valor = OrdemServico.Cliente.Cargo.ToString()

Formulario["CSC_MATRICULA"].Habilitado=False
Formulario["CSC_CARGO_FUNCAO"].Habilitado=False
Formulario["LISTA_ATIV_DESP"].Habilitado=False
Formulario["LISTA_ATIV_DESP_RJ"].Habilitado=False
Formulario["LISTA_ATIV_DESP"].Visivel=False
Formulario["LISTA_ATIV_DESP_RJ"].Visivel=False 


if pessoa["FUNCAO_GRATIFICADA"].ToString() == pessoa["CARGO_FUNCIONAL"].ToString():
    Formulario["CSC_CARGO_FUNCAO"].Valor = OrdemServico.Cliente.Cargo.ToString() +' - '+ pessoa["FUNCAO_GRATIFICADA"].ToString()
    
##TRATA TIPO ESTABELECIMENTO

if OrdemServico.Servico.ClasseServico.Sigla.ToString() == "DESPESTABELECIMENTO":
    Formulario["CSC_NOVO_ESTABELECIMENTO"].Visivel=False
    Formulario["CSC_ESTABELECIMENTO"].Visivel=True
    Formulario["CSC_UF"].Visivel=True
    Formulario["CSC_UF"].Habilitado=False
    Formulario["CSC_ESTABELECIMENTO"].Itens = DB.ExecuteDataTable("SELECT DISTINCT TO_CHAR(E.ESTABID) AS ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE)")

    #Servico.Carrega()
    Formulario["CSC_UF"].Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")


        
    if OrdemServico.Servico.Sigla.ToString() != 'ENCESTABELECIMENTO' and OrdemServico.Servico.Sigla.ToString() != 'ALTDADOSCADASTRAIS':
        Formulario["CSC_ESTABELECIMENTO"].Visivel=False
        Formulario["CSC_UF"].Visivel=False
        Formulario["CSC_UF"].Habilitado=False
        
    if OrdemServico.Servico.Sigla.ToString() == 'ABERESTABELECIMENTO':
        Formulario["CSC_NOVO_ESTABELECIMENTO"].Visivel=True
        Formulario["CSC_UF"].Visivel=True
        Formulario["CSC_UF"].Habilitado=True
    
        
##TRATA TIPO RENOVAÇÃO

if OrdemServico.Servico.ClasseServico.Sigla.ToString() == "DESPRENOVACAO":
    Formulario["CSC_NOVO_ESTABELECIMENTO"].Visivel=False
    Formulario["CSC_ESTABELECIMENTO"].Visivel=True
    Formulario["CSC_UF"].Visivel=True
    Formulario["CSC_ESTABELECIMENTO"].Habilitado=True
    Formulario["CSC_UF"].Habilitado=False
    
    Formulario["CSC_ESTABELECIMENTO"].Itens = DB.ExecuteDataTable("SELECT DISTINCT TO_CHAR(E.ESTABID) AS ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE)")

    #Servico.Carrega()
    Formulario["CSC_UF"].Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")


##TRATA TIPO ARQUIVAMENTO

if OrdemServico.Servico.ClasseServico.Sigla.ToString() == "DESPARQUIVAMENTO":
    Formulario["CSC_NOVO_ESTABELECIMENTO"].Visivel=False
    Formulario["CSC_ESTABELECIMENTO"].Visivel=False
    Formulario["CSC_UF"].Visivel=True
    Formulario["CSC_UF"].Habilitado=False
    
    Formulario["CSC_UF"].Valor = 'RJ'

    
##TRATA TIPO CERTIDÃO

if OrdemServico.Servico.ClasseServico.Sigla.ToString() == "DESPCERTIDOES":
    Formulario["CSC_NOVO_ESTABELECIMENTO"].Visivel=False
    Formulario["CSC_ESTABELECIMENTO"].Visivel=True
    Formulario["CSC_UF"].Visivel=True
    Formulario["CSC_ESTABELECIMENTO"].Habilitado=True
    Formulario["CSC_UF"].Habilitado=False
    Formulario["LISTA_ATIV_DESP"].Visivel=False
    Formulario["LISTA_ATIV_DESP_RJ"].Visivel=False
    
    Formulario["CSC_ESTABELECIMENTO"].Itens = DB.ExecuteDataTable("SELECT DISTINCT TO_CHAR(E.ESTABID) AS ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE)")

    #Servico.Carrega()
    Formulario["CSC_UF"].Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")
```
- Operação PR0001 Preencher Campos
  - CSC_ESTABELECIMENTO "Estabelecimento" [DropDownList String → CPE_CSC.CSC_ESTABELECIMENTO] obrigatório
**CSC_ESTABELECIMENTO.ScriptModificado**
```python
uf = DB.ExecuteScalar("SELECT DISTINCT e.state FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE) AND E.ESTABID = '"+Controle.Valor.ToString()+"'")
Formulario["CSC_UF"].Valor = uf.ToString()

if OrdemServico.Servico.ClasseServico.Sigla.ToString() == "DESPCERTIDOES":    
    if Formulario["CSC_UF"].Valor =='RJ':
        Formulario["LISTA_ATIV_DESP"].Habilitado=False
        Formulario["LISTA_ATIV_DESP_RJ"].Habilitado=True 
        Formulario["LISTA_ATIV_DESP"].Visivel=False
        Formulario["LISTA_ATIV_DESP_RJ"].Visivel=True
    else:
        Formulario["LISTA_ATIV_DESP"].Habilitado=True
        Formulario["LISTA_ATIV_DESP_RJ"].Habilitado=False 
        Formulario["LISTA_ATIV_DESP"].Visivel=True
        Formulario["LISTA_ATIV_DESP_RJ"].Visivel=False
```
  - CSC_NOVO_ESTABELECIMENTO "Novo Estabelecimento" [TextBox String → CPE_CSC.CSC_NOVO_ESTABELECIMENTO] obrigatório
  - CSC_UF "UF do Estabelecimento" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_OBS "Descrição Detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - LISTA_ATIV_DESP "Lista de Atividades Despachante" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP.LISTA_ATIV_DESP] obrigatório
    - coluna SERVICO
    - coluna ATIVIDADE obrigatório
    - coluna VALOR obrigatório
  - LISTA_ATIV_DESP_RJ "Lista de Atividades Despachante/RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] obrigatório
    - coluna VALOR obrigatório
    - coluna SERVICO
**LISTA_ATIV_DESP_RJ.SERVICO.ScriptModificado**
```python
FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Taxas de Licenças de Estabelecimento;Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"

FormularioRegistro["ATIVIDADE"].Valor = None
FormularioRegistro["Valor"].Valor = None

if FormularioRegistro["SERVICO"].Valor == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if FormularioRegistro["SERVICO"].Valor == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if FormularioRegistro["SERVICO"].Valor == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if FormularioRegistro["SERVICO"].Valor == "Renovação de Alvara de funcionamento" or FormularioRegistro["SERVICO"].Valor == "Renovação de Licença Ambiental" or FormularioRegistro["SERVICO"].Valor == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if FormularioRegistro["SERVICO"].Valor == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if FormularioRegistro["SERVICO"].Valor == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if FormularioRegistro["SERVICO"].Valor == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
    - coluna ATIVIDADE obrigatório
**LISTA_ATIV_DESP_RJ.ATIVIDADE.ScriptModificado**
```python
FormularioRegistro["VALOR"].Valor = ''
servico = OrdemServico.Servico.Descricao.ToString()
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento))" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'

if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'
    

    
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'    
    

    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais (Encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    

if (servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária") and (FormularioRegistro["ATIVIDADE"].Valor =="Taxas de Licenças de Estabelecimento"):
    FormularioRegistro["VALOR"].Valor = '100'

    
if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Renovação do AVCB"):
    FormularioRegistro["VALOR"].Valor = '300'

if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Certificado de Aprovação do Corpo de Bombeiros"):
    FormularioRegistro["VALOR"].Valor = '200'

    

if servico == "Arquivamento de Ata" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'


if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviços para Regularização da Certidão Municipal do IPTU"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço de Retirada de Certidão Simplificada na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Municipal - IPTU" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver." or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver)"):
    FormularioRegistro["VALOR"].Valor = '100'    
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel"):
    FormularioRegistro["VALOR"].Valor = '150'
    
    
if servico == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if servico == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if servico == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if servico == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if servico == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if servico == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_CARGO_FUNCAO "Cargo - Função" [TextBox String → CPE_CSC.CSC_CARGO_FUNCAO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTO VENCIDO
  - anexo "Documento Vencido" classes: Arquivo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTO A SER ARQUIVADO
  - anexo "Documento a ser arquivado" classes: Anexo — RequeridoInicial=true

### [229015] Tarefa "Tarefa Automática Pesq. de mercado"
Responsável: Fila Diapa (papel 610)
**ScriptInicio**
```python
AvancaProximaAtividade = True
```

### [229016] Tarefa "Analisar Solicitação"
Responsável: Fila CSC - Serviços Gerais (papel 483)

### [229017] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [229018] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoGateway("ATENDER")
```

### [229019] Tarefa "Analisar Solicitação"
Responsável: Fila CSC - Serviços Gerais (papel 483)

### [229020] Tarefa "Solicitar Aprovação do Superior Imediato"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVSUPIMEDIATO CERT
- Operação PR0002 Aprovar
  - (aprovação) CSC_ESTABELECIMENTO "Estabelecimento" [DropDownList String → CPE_CSC.CSC_ESTABELECIMENTO]
  - (aprovação) CSC_UF "UF" [DropDownList String → CPE_CSC.CSC_UF]
  - aprovador: Gerente da Pessoa (Unico)

### [229021] Tarefa "Aguardar Pagamento"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=AGUARDARPAGAMENTO RENO
**ScriptInicio**
```python
texto=''


ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

sqlRI= DB.ExecuteDataTable("select TO_CHAR(E.AMOUNT_PAID) PAGTO_AP,TO_CHAR(C.CREATION_DATE, 'DD-MON-YYYY HH24:MI') CREATION_DATE,TO_CHAR(C.CHECK_DATE, 'DD-MON-YYYY HH24:MI') DATAPAGAMENTO from  CLL_F189_ENTRY_OPERATIONS A, CLL_F189_INVOICES B , VW_AP_INVOICE_PAYMENT_HISTORY C, ORG_ORGANIZATION_DEFINITIONS D, AP_INVOICES_ALL E, AP_SUPPLIERS F, CLL_F189_INVOICE_TYPES G where 1=1 and a.OPERATION_ID =B.OPERATION_ID and a.ORGANIZATION_ID=B.ORGANIZATION_ID and a.ORGANIZATION_ID=D.ORGANIZATION_ID and B.INVOICE_NUM_AP=E.INVOICE_NUM and E.VENDOR_ID=F.VENDOR_ID and B.INVOICE_TYPE_ID =G.INVOICE_TYPE_ID (+) and E.INVOICE_DATE =B.INVOICE_DATE and E.INVOICE_ID=C.INVOICE_ID and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' and C.CREATION_DATE = (select max(C1.CREATION_DATE)from CLL_F189_INVOICES B1, VW_AP_INVOICE_PAYMENT_HISTORY C1, AP_INVOICES_ALL E1 where 1=1 and B1.INVOICE_NUM_AP = E1.INVOICE_NUM and E1.INVOICE_DATE = B1.INVOICE_DATE and E1.INVOICE_ID = C1.INVOICE_ID and b1.ORGANIZATION_ID = '"+organizacao.ToString()+"' and b1.OPERATION_ID = '"+ri.ToString()+"' ) order by a.OPERATION_ID, B.INVOICE_NUM")

for resultado in sqlRI.Rows:
    OrdemServico["CSC_DATA_RECEBIMENTO"]= resultado['DATAPAGAMENTO']
    #Criticas.AdicionaPendencia(resultado['PAGTO_AP'].ToString()+' | '+resultado['CREATION_DATE'].ToString()+' | '+resultado['DATAPAGAMENTO'].ToString())

AvancaProximaAtividade = True
```
**ScriptValidacao**
```python
contLinha=0
contPag=0
texto = ''
ri= OrdemServico["CSC_RI"]

if OrdemServico["CSC_DATA_RECEBIMENTO"].ToString()!= '':
    contPag=contPag+1
else:
    texto = texto+'Data Pagamento não encontrado para RI Número '+ri.ToString()+' informados.\n'

if contPag == contLinha or texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0001 Preencher Campos
  - CSC_DATA_RECEBIMENTO "Data Pagamento" [DatePicker DateTime → CPE_CSC.CSC_DATA_RECEBIMENTO] obrigatório
  - CSC_RI "CSC_RI" [TextBox String → CPE_CSC.CSC_RI] obrigatório
  - CSC_ORGANIZACAO "CSC_ORGANIZACAO" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório

### [229022] Tarefa "Elaborar Nota Técnica"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração: Nome=NOTA TÉCNICA EST
  - anexo "Nota Técnica" classes: Arquivo — RequeridoInicial=true

### [229023] Tarefa "Acionar Despachante e informar Serviços Solicitados"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario["LISTA_ATIV_DESP_RJ"].Visivel=True
Formulario["LISTA_ATIV_DESP_RJ"].Habilitado=True
```
- Operação PR0001 Preencher Campos
  - LISTA_ATIV_DESP_RJ "Lista de Atividades Despachante/RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] obrigatório — QtdColunasFormulario=1
    - coluna SERVICO
**LISTA_ATIV_DESP_RJ.SERVICO.ScriptModificado**
```python
FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Taxas de Licenças de Estabelecimento;Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"

FormularioRegistro["ATIVIDADE"].Valor = None
FormularioRegistro["Valor"].Valor = None

if FormularioRegistro["SERVICO"].Valor == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if FormularioRegistro["SERVICO"].Valor == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if FormularioRegistro["SERVICO"].Valor == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if FormularioRegistro["SERVICO"].Valor == "Renovação de Alvara de funcionamento" or FormularioRegistro["SERVICO"].Valor == "Renovação de Licença Ambiental" or FormularioRegistro["SERVICO"].Valor == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if FormularioRegistro["SERVICO"].Valor == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if FormularioRegistro["SERVICO"].Valor == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if FormularioRegistro["SERVICO"].Valor == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
    - coluna VALOR
    - coluna ATIVIDADE obrigatório
**LISTA_ATIV_DESP_RJ.ATIVIDADE.ScriptModificado**
```python
servico = OrdemServico.Servico.Descricao.ToString()
FormularioRegistro["VALOR"].Valor = ''
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento))" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'

if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'
    

    
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'    
    

    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais (Encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    

if (servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária") and (FormularioRegistro["ATIVIDADE"].Valor =="Taxas de Licenças de Estabelecimento"):
    FormularioRegistro["VALOR"].Valor = '100'

    
if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Renovação do AVCB"):
    FormularioRegistro["VALOR"].Valor = '300'

if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Certificado de Aprovação do Corpo de Bombeiros"):
    FormularioRegistro["VALOR"].Valor = '200'

    

if servico == "Arquivamento de Ata" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'


if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviços para Regularização da Certidão Municipal do IPTU"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço de Retirada de Certidão Simplificada na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Municipal - IPTU" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver." or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver)"):
    FormularioRegistro["VALOR"].Valor = '100'    
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel"):
    FormularioRegistro["VALOR"].Valor = '150'
    
    
if servico == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if servico == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if servico == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if servico == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if servico == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if servico == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
- Operação PR0001 Preencher Campos
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_CARGO_FUNCAO "Cargo - Função" [TextBox String → CPE_CSC.CSC_CARGO_FUNCAO] obrigatório
  - CSC_UF "UF do Estabelecimento" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_OBS "Descrição Detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS]

### [229024] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - LISTA_ATIV_DESP_RJ "Lista de Atividades Despachante/RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] — QtdColunasFormulario=1
    - coluna VALOR
    - coluna ATIVIDADE obrigatório
**LISTA_ATIV_DESP_RJ.ATIVIDADE.ScriptModificado**
```python
servico = OrdemServico.Servico.Descricao.ToString()
FormularioRegistro["VALOR"].Valor = ''
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento))" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'

if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'
    

    
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'    
    

    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais (Encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    

if (servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária") and (FormularioRegistro["ATIVIDADE"].Valor =="Taxas de Licenças de Estabelecimento"):
    FormularioRegistro["VALOR"].Valor = '100'

    
if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Renovação do AVCB"):
    FormularioRegistro["VALOR"].Valor = '300'

if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Certificado de Aprovação do Corpo de Bombeiros"):
    FormularioRegistro["VALOR"].Valor = '200'

    

if servico == "Arquivamento de Ata" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'


if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviços para Regularização da Certidão Municipal do IPTU"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço de Retirada de Certidão Simplificada na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Municipal - IPTU" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver." or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver)"):
    FormularioRegistro["VALOR"].Valor = '100'    
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel"):
    FormularioRegistro["VALOR"].Valor = '150'
    
    
if servico == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if servico == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if servico == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if servico == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if servico == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if servico == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
    - coluna SERVICO
**LISTA_ATIV_DESP_RJ.SERVICO.ScriptModificado**
```python
FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Taxas de Licenças de Estabelecimento;Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"

FormularioRegistro["ATIVIDADE"].Valor = None
FormularioRegistro["Valor"].Valor = None

if FormularioRegistro["SERVICO"].Valor == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if FormularioRegistro["SERVICO"].Valor == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if FormularioRegistro["SERVICO"].Valor == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if FormularioRegistro["SERVICO"].Valor == "Renovação de Alvara de funcionamento" or FormularioRegistro["SERVICO"].Valor == "Renovação de Licença Ambiental" or FormularioRegistro["SERVICO"].Valor == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if FormularioRegistro["SERVICO"].Valor == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if FormularioRegistro["SERVICO"].Valor == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if FormularioRegistro["SERVICO"].Valor == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS COMPROBATÓRIOS
  - anexo "Documentos Comprobatórios" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_CARGO_FUNCAO "Cargo - Função" [TextBox String → CPE_CSC.CSC_CARGO_FUNCAO] obrigatório
  - CSC_UF "UF do Estabelecimento" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_OBS "Descrição Detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS]

### [229026] EventoIntermediarioRegra ""
**Regra**
```python
1<>2
```

### [229027] Tarefa "Anexar NF e Abrir RI"
Responsável: Responsável atual (papel 36)
**ScriptValidacao**
```python
texto=''

ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

if ri !='' and organizacao!= '':

    sqlRI= DB.ExecuteScalar("select count(a.OPERATION_ID) RI from CLL_F189_ENTRY_OPERATIONS a where 1=1 and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' order by a.OPERATION_ID")


    if sqlRI == 0:
        sqlOrganizacao= DB.ExecuteScalar("SELECT ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS WHERE ORGANIZATION_ID = '"+organizacao.ToString()+"' ORDER BY ORGANIZACAO")
        texto = texto+'RI não encontrado para Organização '+sqlOrganizacao.ToString()+' e Número '+ri.ToString()+' informados.\n'

if texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL EST
  - anexo "Nota Fiscal" classes: Nota Fiscal — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CSC_ORGANIZACAO "Organização" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório
  - CSC_RI "Nº RI" [TextBox String → CPE_CSC.CSC_RI] obrigatório

### [229028] Tarefa "Acionar Despachante e informar Serviços Solicitados"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
if OrdemServico["CSC_UF"].ToString() == 'RJ':
    Formulario["LISTA_ATIV_DESP_RJ"].Visivel = True
    Formulario["LISTA_ATIV_DESP"].Visivel = False
    Formulario["LISTA_ATIV_DESP_RJ"].Habilitado = True
    Formulario["LISTA_ATIV_DESP"].Habilitado = False

if OrdemServico["CSC_UF"].ToString() != 'RJ':
    Formulario["LISTA_ATIV_DESP_RJ"].Visivel = False
    Formulario["LISTA_ATIV_DESP"].Visivel = True
    Formulario["LISTA_ATIV_DESP_RJ"].Habilitado = False
    Formulario["LISTA_ATIV_DESP"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LISTA_ATIV_DESP "LISTA DE ATIV. DESPACHANTE" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP.LISTA_ATIV_DESP] obrigatório
    - coluna VALOR obrigatório
    - coluna SERVICO
    - coluna ATIVIDADE obrigatório
  - LISTA_ATIV_DESP_RJ "LISTA DE ATIV DESPACHANTE RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] obrigatório
    - coluna VALOR obrigatório
    - coluna ATIVIDADE obrigatório
    - coluna SERVICO

### [229029] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS COMPROBATÓRIOS RENO
  - anexo "Documentos Comprobatórios" classes: Anexo — RequeridoInicial=true

### [229030] Tarefa "Solicitar Aprovação do Superior Imediato"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVSUPIMEDIATO RENO
- Operação PR0002 Aprovar
  - item para aprovação ""
  - aprovador: Gerente Superior Imediato Posição (Unico)

### [229031] EventoIntermediarioTimer "7200 minutos"
Config: TempoIntervalo=7200

### [229032] Tarefa "Solicitar Aprovação do Superior Imediato"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVSUPIMEDIATO EST
- Operação PR0002 Aprovar
  - (aprovação) CSC_UF "UF" [DropDownList String → CPE_CSC.CSC_UF]
  - (aprovação) CSC_ESTABELECIMENTO "Estabelecimento" [DropDownList String → CPE_CSC.CSC_ESTABELECIMENTO]
  - (aprovação) CSC_NOVO_ESTABELECIMENTO "Novo Estabelecimento" [TextBox String → CPE_CSC.CSC_NOVO_ESTABELECIMENTO]
  - aprovador: Gerente Superior Imediato Posição (Unico)

### [229034] Tarefa "Solicitar Ato para COJUR"
Responsável: Responsável atual (papel 36)
- Operação PR0001 Preencher Campos
  - OBJETO DA CONSULTA "Objeto da Consulta" [Memo String(2000) → CP_ORDEM_SERVICO.OBJETO_DA_CONSULTA] obrigatório
  - DescricaoDetalhada (nativo) obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=NOTA TÉCNICA COJUR
  - anexo "Nota Técnica" classes: Arquivo — RequeridoInicial=true

### [229033] EventoIntermediarioMensagem "Conclusão de Chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço CESEC
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
Atenciosamente,
Central de Serviços

### [229035] SubProcesso "Requisições de manifestações Jurídicas - Consultas Matriz/CAT"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=142; Configuracao={"ExibirBotaoNovaSubprocessos":true}
- ValoresInputs:
  - PropertyId=1223; Property=DescricaoDetalhada
  - CustomPropertyId=135; CustomProperty=OBJETO DA CONSULTA
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega('Sigla','REQCAT')
```
  - PropertyId=1311; Property=Cliente
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2212; ClasseConfiguracao=Parecer Jurídico
  - SuperClasse=Artefato; ClasseConfiguracaoId=1667; ClasseConfiguracao=Gejur - Parecer
- Associação: Ativo=true; FraseAssociacao=Serv. Desp. Estab. -> Cons. Jur.; FraseInversaAssociacao=Cons. Jur -> Serv. Desp. Estab.; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=SERVDESPESTAB_CONSJUR | fonte: Serviços Despachantes - Estabelecimento 1 → alvo: Consultas Jurídicas

### [229036] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = "Não aprovação no prazo de 5 dias pelo Gestor do Cliente."
```

### [229037] Tarefa "Acionar Despachante e informar Serviços Solicitados"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
if OrdemServico["CSC_UF"].ToString() == 'RJ':
    Formulario["LISTA_ATIV_DESP_RJ"].Visivel = True
    Formulario["LISTA_ATIV_DESP"].Visivel = False
    Formulario["LISTA_ATIV_DESP_RJ"].Habilitado = True
    Formulario["LISTA_ATIV_DESP"].Habilitado = False

if OrdemServico["CSC_UF"].ToString() != 'RJ':
    Formulario["LISTA_ATIV_DESP_RJ"].Visivel = False
    Formulario["LISTA_ATIV_DESP"].Visivel = True
    Formulario["LISTA_ATIV_DESP_RJ"].Habilitado = False
    Formulario["LISTA_ATIV_DESP"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - LISTA_ATIV_DESP "LISTA DE ATIV. DESPACHANTE" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP.LISTA_ATIV_DESP] obrigatório
    - coluna VALOR obrigatório
    - coluna SERVICO obrigatório
    - coluna ATIVIDADE obrigatório
  - LISTA_ATIV_DESP_RJ "LISTA DE ATIV DESPACHANTE RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] obrigatório
    - coluna VALOR obrigatório
    - coluna ATIVIDADE obrigatório
    - coluna SERVICO obrigatório

### [229038] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS COMPROBATÓRIOS CERT
  - anexo "Documentos Comprobatórios" classes: Anexo — RequeridoInicial=true

### [229039] Tarefa "Analisar Solicitação"
Responsável: Fila CSC - Serviços Gerais (papel 483)

### [229040] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoReprovacao("APROVSUPIMEDIATO")
```

### [229041] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = "Não aprovação no prazo de 5 dias pelo Gestor do Cliente."
```

### [229042] EventoIntermediarioMensagem "Conclusão de Chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço CESEC
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
Atenciosamente,
Central de Serviços

### [229047] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoReprovacao("APROVSUPIMEDIATO")
```

### [229043] Tarefa "Tarefa Automática"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
AvancaProximaAtividade = True
```

### [229044] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [229045] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoGateway("ATENDER")
```

### [229046] Tarefa "Anexar NF e Abrir RI"
Responsável: Responsável atual (papel 36)
**ScriptValidacao**
```python
texto=''

ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

if ri !='' and organizacao!= '':

    sqlRI= DB.ExecuteScalar("select count(a.OPERATION_ID) RI from CLL_F189_ENTRY_OPERATIONS a where 1=1 and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' order by a.OPERATION_ID")


    if sqlRI == 0:
        sqlOrganizacao= DB.ExecuteScalar("SELECT ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS WHERE ORGANIZATION_ID = '"+organizacao.ToString()+"' ORDER BY ORGANIZACAO")
        texto = texto+'RI não encontrado para Organização '+sqlOrganizacao.ToString()+' e Número '+ri.ToString()+' informados.\n'

if texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0001 Preencher Campos
  - CSC_ORGANIZACAO "Organização" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO]
  - CSC_RI "Nº RI" [TextBox String → CPE_CSC.CSC_RI]
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL CERT
  - anexo "Nota Fiscal" classes: Nota Fiscal — RequeridoInicial=true

### [229048] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoGateway("ATENDER")
```

### [229049] Tarefa "Aguardar Liberação de OC Master e Nota Fiscal do Fornecedor."
Responsável: Responsável atual (papel 36)

### [229050] Tarefa "Aguardar Liberação de OC Master e Nota Fiscal do Fornecedor."
Responsável: Responsável atual (papel 36)

### [229051] Tarefa "Acionar Despachante e informar Serviços Solicitados"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario["CSC_OBS2"].Visivel = False
Formulario["CSC_OBS2"].Habilitado = False

if OrdemServico["CSC_UF"].ToString() == 'RJ':
    Formulario["LISTA_ATIV_DESP_RJ"].Visivel = True
    Formulario["LISTA_ATIV_DESP"].Visivel = False
    Formulario["LISTA_ATIV_DESP_RJ"].Habilitado = True
else:
    Formulario["LISTA_ATIV_DESP_RJ"].Visivel = False
    Formulario["LISTA_ATIV_DESP"].Visivel = True
    Formulario["LISTA_ATIV_DESP"].Habilitado = True


if OrdemServico.PossuiAprovacao("APROVSUPIMEDIATO2") == False:   
    motivoReprov = OrdemServico.ObtemMotivoReprovacao("APROVSUPIMEDIATO2").ToString()
    Formulario["CSC_OBS2"].Visivel = True
    Formulario["CSC_OBS2"].Valor = motivoReprov
```
- Operação PR0001 Preencher Campos
  - CSC_OBS2 "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS2]
  - LISTA_ATIV_DESP_RJ "Lista de Atividades Despachante/RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] obrigatório — QtdColunasFormulario=1
    - coluna VALOR
    - coluna ATIVIDADE obrigatório
**LISTA_ATIV_DESP_RJ.ATIVIDADE.ScriptModificado**
```python
servico = OrdemServico.Servico.Descricao.ToString()
FormularioRegistro["VALOR"].Valor = ''
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento))" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'

if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'
    

    
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'    
    

    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais (Encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    

if (servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária") and (FormularioRegistro["ATIVIDADE"].Valor =="Taxas de Licenças de Estabelecimento"):
    FormularioRegistro["VALOR"].Valor = '100'

    
if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Renovação do AVCB"):
    FormularioRegistro["VALOR"].Valor = '300'

if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Certificado de Aprovação do Corpo de Bombeiros"):
    FormularioRegistro["VALOR"].Valor = '200'

    

if servico == "Arquivamento de Ata" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'


if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviços para Regularização da Certidão Municipal do IPTU"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço de Retirada de Certidão Simplificada na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Municipal - IPTU" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver." or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver)"):
    FormularioRegistro["VALOR"].Valor = '100'    
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel"):
    FormularioRegistro["VALOR"].Valor = '150'
    
    
if servico == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if servico == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if servico == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if servico == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if servico == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if servico == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
    - coluna SERVICO
**LISTA_ATIV_DESP_RJ.SERVICO.ScriptModificado**
```python
FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Taxas de Licenças de Estabelecimento;Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"

FormularioRegistro["ATIVIDADE"].Valor = None
FormularioRegistro["Valor"].Valor = None

if FormularioRegistro["SERVICO"].Valor == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if FormularioRegistro["SERVICO"].Valor == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if FormularioRegistro["SERVICO"].Valor == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if FormularioRegistro["SERVICO"].Valor == "Renovação de Alvara de funcionamento" or FormularioRegistro["SERVICO"].Valor == "Renovação de Licença Ambiental" or FormularioRegistro["SERVICO"].Valor == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if FormularioRegistro["SERVICO"].Valor == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if FormularioRegistro["SERVICO"].Valor == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if FormularioRegistro["SERVICO"].Valor == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
  - LISTA_ATIV_DESP "Lista de Atividades Despachante" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP.LISTA_ATIV_DESP] obrigatório — QtdColunasFormulario=1
    - coluna SERVICO
    - coluna VALOR obrigatório
    - coluna ATIVIDADE obrigatório

### [229052] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [229053] EventoIntermediarioRegra ""
**Regra**
```python
1<>2
```

### [229054] EventoIntermediarioTimer "7200 minutos"
Config: TempoIntervalo=7200

### [229055] EventoIntermediarioMensagem "Conclusão de Chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço CESEC
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
Atenciosamente,
Central de Serviços

### [229056] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação - CSC

### [229057] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = "Não aprovação no prazo de 5 dias pelo Gestor do Cliente."
```

### [229058] Tarefa "Tarefa Automática"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
AvancaProximaAtividade = True
```

### [229061] Tarefa "Solicitar Validação do Serviço ao Superior Imediato"
Config: Codigo=APROVSUPIMEDIATO
- Operação PR0002 Aprovar
  - item para aprovação "Documentos Comprobatórios"
  - aprovador: Gerente Superior Imediato Posição (Unico)

### [229062] EventoIntermediarioTimer "7200 minutos"
Config: TempoIntervalo=7200

### [229063] Tarefa "Incluir documentos comprobatórios dos Serviços Solicitados"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS COMPROBATÓRIOS EST
  - anexo "Documentos Comprobatórios" classes: Anexo — RequeridoInicial=true

### [229059] Tarefa "Gerar número - Ato de Diretoria"
Responsável: Fila CSC - Serviços Gerais (papel 483)
**ScriptFormCarregado**
```python
Formulario["TIPO_DOCUMENTO_DGOV"].Habilitado = False
Formulario["TIPO_DOCUMENTO_DGOV"].Valor = 'Ato de diretoria'
Formulario["DIRETORES"].Itens = DB.ExecuteDataTable("select distinct to_char(ORGAO.ID_ORGAO) as id_orgao, ORGAO.DESCRICAO AS ORGAO_COMPLETO from ORGAO left outer join PESSOA on ORGAO.ID_GESTOR = PESSOA.ID_PESSOA where ORGAO.ATIVO like 'Sim' and (ORGAO.DESCRICAO like '%DIRETORIA%') order by ORGAO.DESCRICAO")
Formulario["DIRETORES"].Valor = None
```
- Operação PR0001 Preencher Campos
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX

if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT to_char(O.ID_ORGAO) as id_orgao, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT to_char(O.ID_ORGAO) as id_orgao, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - TIPO_DOCUMENTO_DGOV "Tipo de documento" [DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO_DGOV] obrigatório
  - ASSUNTO_DGOV "Assunto" [Memo String(2000) → CP_ORDEM_SERVICO.ASSUNTO_DGOV] obrigatório
  - ALCADA_ESTATUTARIO "Instrumento com a alçada e competência dos representantes estatutários" [CheckBox Boolean → CP_ORDEM_SERVICO.ALCADA_ESTATUTARIO]
  - DOCUMENTO "Nome do documento" [TextBox String → CP_ORDEM_SERVICO.DOCUMENTO]

### [229060] SubProcesso "Numeração para documentos"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=144; Configuracao={"ExibirBotaoNovaSubprocessos":false}
- ValoresInputs:
  - CustomPropertyId=1004; CustomProperty=ALCADA_ESTATUTARIO
  - CustomPropertyId=706; CustomProperty=ASSUNTO_DGOV
  - CustomPropertyId=704; CustomProperty=DOCUMENTO
  - PropertyId=1311; Property=Cliente
  - CustomPropertyId=287; CustomProperty=DIRETORES
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega('Sigla','NUMDOC')
```
  - CustomPropertyId=715; CustomProperty=TIPO_DOCUMENTO_DGOV
  - CustomPropertyId=714; CustomProperty=GEREX
- Associação: Ativo=true; FraseAssociacao=Serv. Desp. Estab. -> Num. Doc.; FraseInversaAssociacao=Num. Doc. -> Serv. Desp. Estab.; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ESTABNUMDOC | fonte: Serviços Despachantes - Estabelecimento 1 → alvo: Numeração para documentos

### [229000] Tarefa "Anexar NF e Abrir RI"
Responsável: Responsável atual (papel 36)
**ScriptValidacao**
```python
texto=''

ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

if ri !='' and organizacao!= '':

    sqlRI= DB.ExecuteScalar("select count(a.OPERATION_ID) RI from CLL_F189_ENTRY_OPERATIONS a where 1=1 and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' order by a.OPERATION_ID")


    if sqlRI == 0:
        sqlOrganizacao= DB.ExecuteScalar("SELECT ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS WHERE ORGANIZATION_ID = '"+organizacao.ToString()+"' ORDER BY ORGANIZACAO")
        texto = texto+'RI não encontrado para Organização '+sqlOrganizacao.ToString()+' e Número '+ri.ToString()+' informados.\n'

if texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0001 Preencher Campos
  - CSC_RI "Nº RI" [TextBox String → CPE_CSC.CSC_RI] obrigatório
  - CSC_ORGANIZACAO "Organização" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL RENO
  - anexo "Nota Fiscal" classes: Nota Fiscal — RequeridoInicial=true

### [229001] EventoIntermediarioRegra ""
**Regra**
```python
1<>2
```

### [229002] Tarefa "Analisar Solicitação"
Responsável: Fila Diapa (papel 610)

### [229014] Tarefa "Aguardar Pagamento"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=AGUARDARPAGAMENTO ATA
**ScriptInicio**
```python
texto=''


ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

sqlRI= DB.ExecuteDataTable("select TO_CHAR(E.AMOUNT_PAID) PAGTO_AP,TO_CHAR(C.CREATION_DATE, 'DD-MON-YYYY HH24:MI') CREATION_DATE,TO_CHAR(C.CHECK_DATE, 'DD-MON-YYYY HH24:MI') DATAPAGAMENTO from  CLL_F189_ENTRY_OPERATIONS A, CLL_F189_INVOICES B , VW_AP_INVOICE_PAYMENT_HISTORY C, ORG_ORGANIZATION_DEFINITIONS D, AP_INVOICES_ALL E, AP_SUPPLIERS F, CLL_F189_INVOICE_TYPES G where 1=1 and a.OPERATION_ID =B.OPERATION_ID and a.ORGANIZATION_ID=B.ORGANIZATION_ID and a.ORGANIZATION_ID=D.ORGANIZATION_ID and B.INVOICE_NUM_AP=E.INVOICE_NUM and E.VENDOR_ID=F.VENDOR_ID and B.INVOICE_TYPE_ID =G.INVOICE_TYPE_ID (+) and E.INVOICE_DATE =B.INVOICE_DATE and E.INVOICE_ID=C.INVOICE_ID and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' and C.CREATION_DATE = (select max(C1.CREATION_DATE)from CLL_F189_INVOICES B1, VW_AP_INVOICE_PAYMENT_HISTORY C1, AP_INVOICES_ALL E1 where 1=1 and B1.INVOICE_NUM_AP = E1.INVOICE_NUM and E1.INVOICE_DATE = B1.INVOICE_DATE and E1.INVOICE_ID = C1.INVOICE_ID and b1.ORGANIZATION_ID = '"+organizacao.ToString()+"' and b1.OPERATION_ID = '"+ri.ToString()+"' ) order by a.OPERATION_ID, B.INVOICE_NUM")

for resultado in sqlRI.Rows:
    OrdemServico["CSC_DATA_RECEBIMENTO"]= resultado['DATAPAGAMENTO']
    Criticas.AdicionaPendencia(resultado['PAGTO_AP'].ToString()+' | '+resultado['CREATION_DATE'].ToString()+' | '+resultado['DATAPAGAMENTO'].ToString())

AvancaProximaAtividade = True
```
**ScriptValidacao**
```python
contLinha=0
contPag=0
texto = ''
ri= OrdemServico["CSC_RI"]

if OrdemServico["CSC_DATA_RECEBIMENTO"].ToString()!= '':
    contPag=contPag+1
else:
    texto = texto+'Data Pagamento não encontrado para RI Número '+ri.ToString()+' informados.\n'

if contPag == contLinha or texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0001 Preencher Campos
  - CSC_CARGO_FUNCAO "Cargo - Função" [TextBox String → CPE_CSC.CSC_CARGO_FUNCAO] obrigatório
  - CSC_UF "UF do Estabelecimento" [DropDownList String → CPE_CSC.CSC_UF] obrigatório
  - CSC_OBS "Descrição Detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
- Operação PR0001 Preencher Campos
  - CSC_DATA_RECEBIMENTO "Data Pagamento" [DatePicker DateTime → CPE_CSC.CSC_DATA_RECEBIMENTO] obrigatório
  - CSC_ORGANIZACAO "CSC_ORGANIZACAO" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório
  - CSC_RI "CSC_RI" [TextBox String → CPE_CSC.CSC_RI] obrigatório
- Operação PR0001 Preencher Campos
  - LISTA_ATIV_DESP_RJ "Lista de Atividades Despachante/RJ" [DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ] — QtdColunasFormulario=1
    - coluna VALOR
    - coluna ATIVIDADE obrigatório
**LISTA_ATIV_DESP_RJ.ATIVIDADE.ScriptModificado**
```python
servico = OrdemServico.Servico.Descricao.ToString()
FormularioRegistro["VALOR"].Valor = ''
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento))" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'

if servico == "Abertura de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'
    

    
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '250'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'

if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais"):
    FormularioRegistro["VALOR"].Valor = '100'
    
if servico == "Alteração de Dados Cadastrais" and (FormularioRegistro["ATIVIDADE"].Valor =="Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros)"):
    FormularioRegistro["VALOR"].Valor = '300'    
    

    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento)" or FormularioRegistro["ATIVIDADE"].Valor =="Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    
if servico == "Encerramento de Estabelecimento" and (FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Alvarás - legalização de Filiais (Encerramento)"):
    FormularioRegistro["VALOR"].Valor = '200'    
    

if (servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária") and (FormularioRegistro["ATIVIDADE"].Valor =="Taxas de Licenças de Estabelecimento"):
    FormularioRegistro["VALOR"].Valor = '100'

    
if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Renovação do AVCB"):
    FormularioRegistro["VALOR"].Valor = '300'

if servico == "Renovação de AVCB" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Certificado de Aprovação do Corpo de Bombeiros"):
    FormularioRegistro["VALOR"].Valor = '200'

    

if servico == "Arquivamento de Ata" and (FormularioRegistro["ATIVIDADE"].Valor =="Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU)"):
    FormularioRegistro["VALOR"].Valor = '250'


if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local)" or FormularioRegistro["ATIVIDADE"].Valor =="Serviços para Regularização da Certidão Municipal do IPTU"):
    FormularioRegistro["VALOR"].Valor = '200'
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Serviço de Retirada de Certidão Simplificada na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Municipal - IPTU" or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver." or FormularioRegistro["ATIVIDADE"].Valor =="Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver)"):
    FormularioRegistro["VALOR"].Valor = '100'    
    
if servico == "Certidões" and (FormularioRegistro["ATIVIDADE"].Valor =="Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel"):
    FormularioRegistro["VALOR"].Valor = '150'
    
    
if servico == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if servico == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if servico == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if servico == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if servico == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if servico == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```
    - coluna SERVICO
**LISTA_ATIV_DESP_RJ.SERVICO.ScriptModificado**
```python
FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Taxas de Licenças de Estabelecimento;Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"

FormularioRegistro["ATIVIDADE"].Valor = None
FormularioRegistro["Valor"].Valor = None

if FormularioRegistro["SERVICO"].Valor == "Abertura de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
if FormularioRegistro["SERVICO"].Valor == "Alteração de Dados Cadastrais":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);"
    
if FormularioRegistro["SERVICO"].Valor == "Encerramento de Estabelecimento":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);"

if FormularioRegistro["SERVICO"].Valor == "Renovação de Alvara de funcionamento" or FormularioRegistro["SERVICO"].Valor == "Renovação de Licença Ambiental" or FormularioRegistro["SERVICO"].Valor == "Renovação de Vigilância Sanitária":
    FormularioRegistro["ATIVIDADE"].Itens = "Taxas de Licenças de Estabelecimento"

if FormularioRegistro["SERVICO"].Valor == "Renovação de AVCB":
    FormularioRegistro["ATIVIDADE"].Itens = "Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;"

if FormularioRegistro["SERVICO"].Valor == "Arquivamento de Ata":
    FormularioRegistro["ATIVIDADE"].Itens = "Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);"


if FormularioRegistro["SERVICO"].Valor == "Certidões":
    FormularioRegistro["ATIVIDADE"].Itens = "Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;"
```

### [229009] SubProcesso "Pesquisa de mercado"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=143; Configuracao={"ExibirBotaoNovaSubprocessos":false}
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla",'SPM')
```
  - PropertyId=1250; Property=Justificativa
  - CustomPropertyId=1039; CustomProperty=TIPO_SOLICITACAO
  - PropertyId=1311; Property=Cliente
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1767; ClasseConfiguracao=Projeto Básico
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2169; ClasseConfiguracao=Orçamento
- Associação: Ativo=true; FraseAssociacao=Serv. Despachante -> Pesq. de Mercado; FraseInversaAssociacao=Pesq. de Mercado -> Serv. Despachante; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=SERV_DESP_PESQ_MERCADO | fonte: Atividade 02 Gabriel → alvo: Pesquisa de Mercado

### [229010] FimCancelamento ""
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
OrdemServico.MotivoCancelamento = OrdemServico.ObtemMotivoReprovacao("APROVSUPIMEDIATO")
```

### [229008] Tarefa "Informar dados para pesquisa de mercado"
Responsável: Fila CSC - Serviços Gerais (papel 483)
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Empresa
Formulario["TIPO_SOLICITACAO"].Itens = "Contração de Serviços Prediais;Seguro Empresarial e Responsabilidade Civil;Aquisição de Mobiliários e Equipamentos Prediais;Serviços de Engenharia;Serviços de Reforma e Construção;Serviço de Transporte Executivo com Motorista;Contratação de Despachante"

Formulario["TIPO_SOLICITACAO"].Valor = "Contratação de Despachante"

Formulario["TIPO_SOLICITACAO"].Habilitado = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Projeto Básico — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - TIPO_SOLICITACAO "Tipo de Pesquisa" [DropDownList String → CP_ORDEM_SERVICO.TIPO_SOLICITACAO] obrigatório
  - Justificativa (nativo) "Observação"

### [229006] Tarefa "Informar Dados para Arquivamento Despachante Rio"
Responsável: Fila Diapa (papel 610)
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Servico
#servico_arquiv=Servico.Carrega("Sigla", 'ARQUIVAMENTOATA')
#atual = OrdemServico.Servico
#atual=servico_arquiv
#OrdemServico.Salva(atual)
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Servico
servico_arquiv=Servico.Carrega("Sigla", 'ARQUIVAMENTOATA')
atual = OrdemServico
atual.Servico=servico_arquiv
OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Processo.Custom import Servico
Formulario["CSC_UF"].Valor = 'RJ'
Formulario["CSC_UF"].Habilitado = False

osPai= OrdemServico.Carrega("Id", OrdemServico.OcorrenciaPrincipalId)
Formulario["CSC_CARGO_FUNCAO"].Valor = osPai["CSC_CARGO_FUNCAO"]
Formulario["CSC_CARGO_FUNCAO"].Habilitado = False
Formulario["CSC_MATRICULA"].Valor = osPai["CSC_MATRICULA"]
Formulario["CSC_MATRICULA"].Habilitado = False
if osPai["CSC_MATRICULA"] == None or osPai["CSC_MATRICULA"]=='':
    Formulario["CSC_MATRICULA"].Habilitado = True
if osPai["CSC_CARGO_FUNCAO"]==None or osPai["CSC_CARGO_FUNCAO"]=='':
    Formulario["CSC_CARGO_FUNCAO"].Habilitado = True

if osPai["CSC_ESTABELECIMENTO"] == None or osPai["CSC_ESTABELECIMENTO"].ToString() == '':
    estabelecimento = osPai["CSC_NOVO_ESTABELECIMENTO"].ToString()
else:
    estabelecimento = osPai["CSC_ESTABELECIMENTO"].ToString()

Formulario["CSC_OBS"].Valor = 'Solicitação aberta através do chamado '+osPai.NumeroSistema.ToString()+' para a UF '+OrdemServico["CSC_UF"].ToString()+' e Estabelecimento '+estabelecimento+'.'
Formulario["CSC_OBS"].Habilitado = False

servico_arquiv=Servico.Carrega("Sigla", 'ARQUIVAMENTOATA')
atual = OrdemServico
atual.Servico=servico_arquiv
OrdemServico.Salva()
```
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTO A SER ARQUIVADO ATA
  - anexo "Documento a ser arquivado" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CSC_OBS "Descrição Detalhada" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_CARGO_FUNCAO "Cargo - Função" [TextBox String → CPE_CSC.CSC_CARGO_FUNCAO] obrigatório
  - CSC_UF "UF do Estabelecimento" [DropDownList String → CPE_CSC.CSC_UF] obrigatório

### [229012] EventoIntermediarioMensagem "Conclusão de Chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço CESEC
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
Atenciosamente,
Central de Serviços

### [229013] EventoIntermediarioTimer "7200 minutos"
Config: TempoIntervalo=7200

### [229007] Tarefa "Aguardar Pagamento"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=AGUARDARPAGAMENTO CERT
**ScriptInicio**
```python
texto=''


ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

sqlRI= DB.ExecuteDataTable("select TO_CHAR(E.AMOUNT_PAID) PAGTO_AP,TO_CHAR(C.CREATION_DATE, 'DD-MON-YYYY HH24:MI') CREATION_DATE,TO_CHAR(C.CHECK_DATE, 'DD-MON-YYYY HH24:MI') DATAPAGAMENTO from  CLL_F189_ENTRY_OPERATIONS A, CLL_F189_INVOICES B , VW_AP_INVOICE_PAYMENT_HISTORY C, ORG_ORGANIZATION_DEFINITIONS D, AP_INVOICES_ALL E, AP_SUPPLIERS F, CLL_F189_INVOICE_TYPES G where 1=1 and a.OPERATION_ID =B.OPERATION_ID and a.ORGANIZATION_ID=B.ORGANIZATION_ID and a.ORGANIZATION_ID=D.ORGANIZATION_ID and B.INVOICE_NUM_AP=E.INVOICE_NUM and E.VENDOR_ID=F.VENDOR_ID and B.INVOICE_TYPE_ID =G.INVOICE_TYPE_ID (+) and E.INVOICE_DATE =B.INVOICE_DATE and E.INVOICE_ID=C.INVOICE_ID and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' and C.CREATION_DATE = (select max(C1.CREATION_DATE)from CLL_F189_INVOICES B1, VW_AP_INVOICE_PAYMENT_HISTORY C1, AP_INVOICES_ALL E1 where 1=1 and B1.INVOICE_NUM_AP = E1.INVOICE_NUM and E1.INVOICE_DATE = B1.INVOICE_DATE and E1.INVOICE_ID = C1.INVOICE_ID and b1.ORGANIZATION_ID = '"+organizacao.ToString()+"' and b1.OPERATION_ID = '"+ri.ToString()+"' ) order by a.OPERATION_ID, B.INVOICE_NUM")

for resultado in sqlRI.Rows:
    OrdemServico["CSC_DATA_RECEBIMENTO"]= resultado['DATAPAGAMENTO']
    #Criticas.AdicionaPendencia(resultado['PAGTO_AP'].ToString()+' | '+resultado['CREATION_DATE'].ToString()+' | '+resultado['DATAPAGAMENTO'].ToString())

AvancaProximaAtividade = True
```
**ScriptValidacao**
```python
contLinha=0
contPag=0
texto = ''
ri= OrdemServico["CSC_RI"]

if OrdemServico["CSC_DATA_RECEBIMENTO"].ToString()!= '':
    contPag=contPag+1
else:
    texto = texto+'Data Pagamento não encontrado para RI Número '+ri.ToString()+' informados.\n'

if contPag == contLinha or texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0001 Preencher Campos
  - CSC_DATA_RECEBIMENTO "Data Pagamento" [DatePicker DateTime → CPE_CSC.CSC_DATA_RECEBIMENTO] obrigatório
  - CSC_ORGANIZACAO "CSC_ORGANIZACAO" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório
  - CSC_RI "CSC_RI" [TextBox String → CPE_CSC.CSC_RI] obrigatório

### [229011] Tarefa "Aguardar Pagamento"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=AGUARDARPAGAMENTO EST
**ScriptInicio**
```python
texto=''


ri= OrdemServico["CSC_RI"].ToString()
organizacao=OrdemServico["CSC_ORGANIZACAO"].ToString()

sqlRI= DB.ExecuteDataTable("select TO_CHAR(E.AMOUNT_PAID) PAGTO_AP,TO_CHAR(C.CREATION_DATE, 'DD-MON-YYYY HH24:MI') CREATION_DATE,TO_CHAR(C.CHECK_DATE, 'DD-MON-YYYY HH24:MI') DATAPAGAMENTO from  CLL_F189_ENTRY_OPERATIONS A, CLL_F189_INVOICES B , VW_AP_INVOICE_PAYMENT_HISTORY C, ORG_ORGANIZATION_DEFINITIONS D, AP_INVOICES_ALL E, AP_SUPPLIERS F, CLL_F189_INVOICE_TYPES G where 1=1 and a.OPERATION_ID =B.OPERATION_ID and a.ORGANIZATION_ID=B.ORGANIZATION_ID and a.ORGANIZATION_ID=D.ORGANIZATION_ID and B.INVOICE_NUM_AP=E.INVOICE_NUM and E.VENDOR_ID=F.VENDOR_ID and B.INVOICE_TYPE_ID =G.INVOICE_TYPE_ID (+) and E.INVOICE_DATE =B.INVOICE_DATE and E.INVOICE_ID=C.INVOICE_ID and a.ORGANIZATION_ID = '"+organizacao.ToString()+"' and a.OPERATION_ID = '"+ri.ToString()+"' and C.CREATION_DATE = (select max(C1.CREATION_DATE)from CLL_F189_INVOICES B1, VW_AP_INVOICE_PAYMENT_HISTORY C1, AP_INVOICES_ALL E1 where 1=1 and B1.INVOICE_NUM_AP = E1.INVOICE_NUM and E1.INVOICE_DATE = B1.INVOICE_DATE and E1.INVOICE_ID = C1.INVOICE_ID and b1.ORGANIZATION_ID = '"+organizacao.ToString()+"' and b1.OPERATION_ID = '"+ri.ToString()+"' ) order by a.OPERATION_ID, B.INVOICE_NUM")

for resultado in sqlRI.Rows:
    OrdemServico["CSC_DATA_RECEBIMENTO"]= resultado['DATAPAGAMENTO']
    #Criticas.AdicionaPendencia(resultado['PAGTO_AP'].ToString()+' | '+resultado['CREATION_DATE'].ToString()+' | '+resultado['DATAPAGAMENTO'].ToString())

AvancaProximaAtividade = True
```
**ScriptValidacao**
```python
contLinha=0
contPag=0
texto = ''
ri= OrdemServico["CSC_RI"]

if OrdemServico["CSC_DATA_RECEBIMENTO"].ToString()!= '':
    contPag=contPag+1
else:
    texto = texto+'Data Pagamento não encontrado para RI Número '+ri.ToString()+' informados.\n'

if contPag == contLinha or texto!='':
    Criticas.AdicionaPendencia(texto)
```
- Operação PR0001 Preencher Campos
  - CSC_DATA_RECEBIMENTO "Data Pagamento" [DatePicker DateTime → CPE_CSC.CSC_DATA_RECEBIMENTO] obrigatório
  - CSC_ORGANIZACAO "CSC_ORGANIZACAO" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório
  - CSC_RI "CSC_RI" [TextBox String → CPE_CSC.CSC_RI] obrigatório

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
### papel 483: Fila CSC - Serviços Gerais
Tipo=RelacaoPessoas | pessoas: Fila CSC - Serviços Gerais
### papel 610: Fila Diapa
Tipo=RelacaoPessoas | pessoas: Fila Diapa
### papel 461: Fila CSC - Pendente de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação
### papel 192: Gerente da Pessoa
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.Servico.Sigla.ToString() == 'LIBERACAORI' or OrdemServico.Servico.Sigla.ToString() == 'REVERSAORI':
    favorecido=Pessoa.Carrega(Convert.ToInt32(OrdemServico["CSC_FAVORECIDO"]))
    gestor = favorecido.ObtemChefia(False)
else:
    gestor = OrdemServico.Cliente.ObtemChefia(False)

if (gestor == OrdemServico.Cliente):
    gestor = OrdemServico.Cliente.Orgao.OrgaoPai.Gestor

# se for um diretor ou presidente (mudar os identificadores e relacionar todos)
if gestor.Id == 3090 or gestor.Id == 4458 or gestor.Id == 5903 or gestor.Id == 13787 or gestor.Id == 17491 or gestor.Id == 22073 or gestor.Id == 4507 or gestor.Id == 23450 or gestor.Id == 23490:
    gestor = OrdemServico.Cliente

Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())
```
### papel 565: Gerente Superior Imediato Posição
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))

# se for um diretor ou presidente (mudar os identificadores e relacionar todos)
if gestor.Id == 4458 or gestor.Id == 4459 or gestor.Id == 4460 or gestor.Id == 4461 or gestor.Id == 3805 or gestor.Id == 5313 or gestor.Id == 5457 or gestor.Id == 5903 or gestor.Id == 23450 or gestor.Id == 23490 or gestor.Id == 23547:
    gestor = OrdemServico.Cliente

Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### CSC_RI — CSC_RI
TextBox String → CPE_CSC.CSC_RI

### CSC_ORGANIZACAO — CSC_ORGANIZACAO
DropDownList String → CPE_CSC.CSC_ORGANIZACAO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT TO_CHAR(ORGANIZATION_ID) ID,ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS ORDER BY ORGANIZACAO")
```

### CSC_MATRICULA — Matrícula
TextBox String → CPE_CSC.CSC_MATRICULA

### CSC_CARGO_FUNCAO — Cargo - Função
TextBox String → CPE_CSC.CSC_CARGO_FUNCAO

### CSC_UF — UF
DropDownList String → CPE_CSC.CSC_UF
**LookupScript**
```python
Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")
```

### CSC_OBS — Observação
Memo String(2000) → CPE_CSC.CSC_OBS

### LISTA_ATIV_DESP_RJ — LISTA DE ATIV DESPACHANTE RJ
DataGrid RecordList → Z_00143_LISTA_ATIV_DESP_RJ.LISTA_ATIV_DESP_RJ
Descrição: LISTA DE ATIVIDADE DESPACHANTE RJ
Colunas do registro:
- VALOR "VALOR" [TextBox String]
- ATIVIDADE "ATIVIDADE" [DropDownList String]
**ATIVIDADE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Taxas de Licenças de Estabelecimento;Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")


servico = OrdemServico.Servico.Descricao.ToString()
if servico == "Abertura de Estabelecimento":
    Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada(Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")
if servico == "Alteração de Dados Cadastrais":
    Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicações DOU);Inscrição municipal - abertura e filiais e alteração (Entrada/alterações/encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais;Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Regularização/atualização/ renovação do AVCB (Auto vistoria do corpo dos Bombeiros);' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")
    
if servico == "Encerramento de Estabelecimento":
    Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Arquivamentos de todas as Atas(Desarquivamento/Reratificação/Publicaçoes DOU);Serviço para regularização via DBEC - Documento básico de Entrada (Entrada/alterações/encerramento);Retirada de Alvarás - legalização de Filiais (Encerramento);Inscrição Estadual - abertura de filiais e alteração. (Entrada/alterações/encerramento);' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")

if servico == "Renovação de Alvará de funcionamento" or servico == "Renovação de Licença Ambiental" or servico == "Renovação de Vigilância Sanitária":
    Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Taxas de Licenças de Estabelecimento;' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")

if servico == "Renovação de AVCB":
    Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Renovação do AVCB;Cópia do Certificado de Aprovação do Corpo de Bombeiros;' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")

if servico == "Arquivamento de Ata":
    Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Arquivamentos de todas as Atas (Desarquivamento/Reratificação/Publicaçoes DOU);' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")


if servico == "Certidões":
    Itens = DB.ExecuteDataTable("SELECT regexp_substr(info, separador, 1, LEVEL) info FROM (SELECT 'Cópia do Habite-se - imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Cópia do último IPTU e da Certidão de Quitação Fiscal da Prefeitura: imóvel BBTS ou terceiros para aluguel (adquirir junto a Prefeitura local);Certidão de Regularidade de edificação em conformidade com a Lie municipal de uso (zoneamento, licença de funcionamento de atividade, etc) imóvel BBTS ou terceiro para aluguel (adquirir junto a Prefeitura local);Serviços para Regularização da Certidão Municipal do IPTU;Serviço de Retirada de Certidão Simplificada na Junta Comercial;Serviço para Retirada de Certidão de Inteiro Teor na Junta Comercial;Retirada de Certidão Municipal - IPTU;Retirada de Certidão Simplificada na Junta Comercial - cumprimento de todas as exigências apontadas, quando houver.;Retirada de Certidão de Inteiro Teor na Junta Comercial (cumprimento de todas as exigências apontadas, quando houver);Cópia da certidão de inteiro Teor do imóvel (contendo informações de matrícula, averbações e registro) imóvel BBTS ou terceiros para aluguel;' info, '[^;]+' separador FROM dual) CONNECT BY regexp_substr(info, separador, 1, LEVEL) IS NOT NULL")
```
- SERVICO "SERVIÇO" [DropDownList String] itens: Certidões

### CSC_ESTABELECIMENTO — Estabelecimento
DropDownList String → CPE_CSC.CSC_ESTABELECIMENTO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT TO_CHAR(E.ESTABID) AS ESTABID, E.DESCR FROM PS_ESTAB_TBL E where E.EFF_STATUS='A' AND E.EFFDT = (SELECT MAX(E_ED.EFFDT) FROM PS_ESTAB_TBL E_ED WHERE E.ESTABID = E_ED.ESTABID AND E_ED.EFFDT <= SYSDATE)")
```

### CSC_NOVO_ESTABELECIMENTO — Novo Estabelecimento
TextBox String → CPE_CSC.CSC_NOVO_ESTABELECIMENTO

### LISTA_ATIV_DESP — LISTA DE ATIV. DESPACHANTE
DataGrid RecordList → Z_00143_LISTA_ATIV_DESP.LISTA_ATIV_DESP
Descrição: LISTA DE ATIVIDADE DESPACHANTE
Colunas do registro:
- VALOR "VALOR" [TextBox String]
- SERVICO "SERVIÇO" [DropDownList String] itens: Certidões
- ATIVIDADE "ATIVIDADE" [TextBox String]

### CSC_DATA_RECEBIMENTO — Data de Recebimento
DatePicker DateTime → CPE_CSC.CSC_DATA_RECEBIMENTO

### OBJETO DA CONSULTA — Objeto da Consulta
Memo String(2000) → CP_ORDEM_SERVICO.OBJETO_DA_CONSULTA

### CSC_OBS2 — Observação
Memo String(2000) → CPE_CSC.CSC_OBS2

### DIRETORES — Diretoria
DropDownList String → CP_ORDEM_SERVICO.DIRETORES
**LookupScript**
```python
#PGESV###
#lista = DB.ExecuteDataTable("select vl1 from sv_param where ch1 = 'DIRETORES'")
#sv_param = None
#for l in lista.Rows:
#    if sv_param == None:
#       sv_param = "(UPPER(ORGAO.DESCRICAO) like '" + l["vl1"] + "'"
#    else:
#       sv_param += " OR UPPER(ORGAO.DESCRICAO) like '" + l["vl1"] + "'"
#if sv_param == None:
#   sv_param += " 1 <> 1 " # faltam dados na tabela sv_param
#else:
#   sv_param += ") "

Itens = DB.ExecuteDataTable("select distinct to_char(ORGAO.ID_ORGAO) as id_orgao, ORGAO.DESCRICAO AS ORGAO_COMPLETO from ORGAO left outer join PESSOA on ORGAO.ID_GESTOR = PESSOA.ID_PESSOA where ORGAO.ATIVO = 'Sim' and SIGLA LIKE '4%' order by ORGAO.DESCRICAO")



# - #Itens = DB.ExecuteDataTable("select distinct to_char(ORGAO.ID_ORGAO) as id_orgao, ORGAO.DESCRICAO AS ORGAO_COMPLETO from ORGAO left outer join PESSOA on ORGAO.ID_GESTOR = PESSOA.ID_PESSOA where ORGAO.ATIVO like 'Sim' and (ORGAO.DESCRICAO like '%DIRE%' or ORGAO.DESCRICAO like '%PRESI%' or ORGAO.DESCRICAO like '%AUDITORIA%') order by ORGAO.DESCRICAO")
```

### GEREX — Gerência Executiva
DropDownList String → CP_ORDEM_SERVICO.GEREX
Descrição: Gerências Executivas de cada diretoria
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(O.ID_ORGAO) as id_orgao, to_char(O.DESCRICAO) as descricao FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = '"+ OrdemServico.GetCustom("DIRETORES").ToString() +"' ORDER BY O.DESCRICAO")
```

### TIPO_DOCUMENTO_DGOV — Tipo de documento
DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO_DGOV
Itens: Ato de diretoria;Ato de nomeação;Comunicação suplementar;Delegação de competência;Expediente;Nota técnica;Ofício;Portaria;VOTO (colegiados)

### ASSUNTO_DGOV — Assunto da deliberação
Memo String(2000) → CP_ORDEM_SERVICO.ASSUNTO_DGOV

### ALCADA_ESTATUTARIO — Instrumento com a alçada e competência dos representantes estatutários
CheckBox Boolean → CP_ORDEM_SERVICO.ALCADA_ESTATUTARIO

### DOCUMENTO — Nome do documento
TextBox String → CP_ORDEM_SERVICO.DOCUMENTO
Descrição: Nome do documento que originou a deliberação

### TIPO_SOLICITACAO — Tipo de solicitação
DropDownList String → CP_ORDEM_SERVICO.TIPO_SOLICITACAO
Itens: Remanejamento; Conversão

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
