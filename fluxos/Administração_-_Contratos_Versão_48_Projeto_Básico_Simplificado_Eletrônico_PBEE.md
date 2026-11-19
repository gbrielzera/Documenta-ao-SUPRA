# Fluxo: Projeto Básico Simplificado Eletrônico PBEE (PBEE) — versão 48
Caminho: Fluxos > Administração - Contratos Versão 48 Projeto Básico Simplificado Eletrônico PBEE
XML: `XMLs para teste/Administração_-_Contratos_Versão_48_Projeto_Básico_Simplificado_Eletrônico_PBEE.xml` | Supravizio 19.1.1 | SubProcessoId 22970 | DesenhoProcessoId 3088 | ProcessoId 127
Órgão dono: 3000003410 - DIVISAO DE PLANEJAMENTO E IMPORTACAO | Responsável: RAPHAEL GRUPILO NASCIMENTO
Classe do subprocesso: Objetivo=Projeto Básico Simplificado Eletrônico PBEE; DescricaoCliente=Projeto Básico Simplificado Eletrônico PBEE (Jefferson); CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadoresGrupoEnvolvido; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Projeto Básico Eletrônico (PBEE)

## Grafo do fluxo
- [366247] Tarefa "Efetuar correções (Insumos)
" {Cliente} → [366309]  | [366310]  | [366228] Preencher informações de Faturamento para relatóri
- [366248] SubProcesso "Cadastro de Itens" {Responsável atual} → [366303] Preencher dados (cadastro de Código de Item conclu
- [366302] Tarefa "Cancela aprovação gerentes" {Responsável atual} → [366241] Recolhe aprovações e outras informações para preen
- [366303] Tarefa "Preencher dados (cadastro de Código de Item concluído)" {Fila CSC - Prestação de Serviços} → [G82061] Pesquisa Prévia anexada?
- [366304] SubProcesso "Pesquisa de Mercado" {Responsável atual} → [366237] Aviso para preenchimento de formulário
- [366305] EventoFinal "Cancelado" → (fim)
- [366306] EventoFinal "Cancelado" → (fim)
- [366307] Tarefa "Preencher dados para pesquisa de mercado" {Responsável atual} → [366304] Pesquisa de Mercado
- [366308] EventoIntermediarioMensagem "Aviso sobre cancelamento de Ordem de Serviço" → [366314] Cancelado
- [366309] EventoIntermediarioTimer "" → [366289] Ausência de informações
- [366310] EventoIntermediarioTimer "" → [366277] Aviso de cancelamento de chamado por falta de ajus
- [366249] Tarefa "Verificar Reprovação
 Cliente" {Fila CSC - Prestação de Serviços} → [G82067] Submeter novamente para aprovação?
- [366250] EventoIntermediarioMensagem "Aviso de cancelamento por reprovação gerencial" → [366253] Cancelamento por reprovação
- [366251] Tarefa "Solicitar aprovação do Cliente" {Responsável atual} → [G82065] Cliente Aprovou?
- [366252] EventoIntermediarioMensagem "PBe - Conta Contábil" → [366266] Informar Conta Contábil
- [366253] FimCancelamento "Cancelamento por reprovação" → (fim)
- [366311] EventoIntermediarioMensagem "Aviso de cancelamento de chamado por falta de resposta de cliente para complemento do PBe" → [366305] Cancelado
- [366312] SubProcesso "Remanejamento Orçamentário" {Responsável atual} → [366318] Retorno de devolução ao cliente para nova solicita
- [366313] EventoIntermediarioMensagem "Cobrança de Ajustes" → [366275] Verificar Reprovação
 Gerencial (Cliente)
- [366314] EventoFinal "Cancelado" → (fim)
- [366315] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório." {Responsável atual} → [366251] Solicitar aprovação do Cliente
- [366316] Tarefa "Informar número da OS criada para Cadastro de Fornecedor" {Fila CSC - Prestação de Serviços} → [366260] Recolhe aprovações e outras informações para preen
- [366254] Tarefa "Solicitar aprovação conforme NI006" {Responsável atual} → [G82064] Gerentes Aprovaram?
- [366255] Tarefa "Preencher informações para solicitações de parecer" {Fila CSC - Prestação de Serviços} → [G82080] Tem orçamento para conta/UOR informada?
- [366256] EventoIntermediarioMensagem "Reiteração" → [366317] Unificar Projeto Básico
- [366317] Tarefa "Unificar Projeto Básico" {Fila CSC - Prestação de Serviços} → [366229]  | [366257] Preencher dados para confecção de OC
- [366257] Tarefa "Preencher dados para confecção de OC" {Responsável atual} → [G82063] Direcionamento Interno
- [366258] EventoIntermediarioMensagem "Aviso de aprovação ao Gestor" → [366227] Aguardar aprovação Gesap-Diage
- [366259] EventoIntermediarioMensagem "Aviso de utilização de Conta Contábil e UOR referente a Marketing" → [366290] Aguardar aprovação Gemac
- [366318] Tarefa "Retorno de devolução ao cliente para nova solicitação de parecer (CESEC)
" {Fila CSC - Prestação de Serviços} → [G82080] Tem orçamento para conta/UOR informada?
- [366319] Tarefa "Solicitar aprovação do Gerente Executivo da Contratação" {Responsável atual} → [G82076] Gerente Executivo aprovou?
- [366260] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório." {Fila CSC - Prestação de Serviços} → [366255] Preencher informações para solicitações de parecer
- [366261] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório." {Responsável atual} → [366254] Solicitar aprovação conforme NI006
- [366262] Tarefa "Responder Questionário Pesquisa de Mercado e Mitigação de Fracionamento de Demanda" {Cliente} → [366232]  | [366233]  | [366263] Aviso de retorno da Ordem de Serviço
- [366263] EventoIntermediarioMensagem "Aviso de retorno da Ordem de Serviço" → [366265] Cadastrar pesquisa de mercado e Valor referencial
- [366264] FimCancelamento "Cancelamento por reprovação" → (fim)
- [366265] Tarefa "Cadastrar pesquisa de mercado e Valor referencial" {Fila CSC - Prestação de Serviços} → [366293] Verificar se o fornecedor está cadastrado

- [366266] Tarefa "Informar Conta Contábil" {Fila Contabilidade} → [366231]  | [366296] PBe - Consulta conta orçamentária
- [366267] EventoIntermediarioMensagem "Reprovação Cliente" → [366249] Verificar Reprovação
 Cliente
- [366268] EventoIntermediarioTimer "" → [366245] Aviso de cancelamento de chamado por falta de ajus
- [366269] EventoIntermediarioTimer "" → [366238] Conferir Parecer
- [366270] EventoIntermediarioTimer "" → [366313] Cobrança de Ajustes
- [366271] EventoIntermediarioTimer "" → [366294] Reprovação Gemac
- [366272] EventoInicial "" {Cliente} → [G82069] Itens da Gesap?
- [366273] EventoIntermediarioMensagem "Aviso de cancelamento por reprovação da Diage" → [366264] Cancelamento por reprovação
- [366274] EventoIntermediarioMensagem "Conferir PBe para envio de aprovação" → [366240] Conferir itens, Pareceres e Aprovadores
- [366275] Tarefa "Verificar Reprovação
 Gerencial (Cliente)" {Cliente} → [366270]  | [366234] Conferencia de Ajuste do Cliente da Reprovação Ger
- [366276] Tarefa "Ajustar reprovação Gemac (Cliente)" {Cliente} → [366271]  | [366318] Retorno de devolução ao cliente para nova solicita
- [366277] EventoIntermediarioMensagem "Aviso de cancelamento de chamado por falta de ajustes" → [366282] Cancelado
- [366278] Tarefa "Cancela aprovação cliente" {Responsável atual} → [366315] Recolhe aprovações e outras informações para preen
- [366279] Tarefa "Aguardar aprovação Gesap" {Responsável atual} → [G82070] Aprovado?
- [366280] EventoIntermediarioMensagem "Aprovação" → [366317] Unificar Projeto Básico
- [366281] Tarefa "Preencher dados para cadastro de itens" {Responsável atual} → [366248] Cadastro de Itens
- [366282] EventoFinal "Cancelado" → (fim)
- [366283] SubProcesso "Compras Diretas" {Responsável atual} → [366246] Término de Serviço
- [366284] SubProcesso "Cadastro de Fornecedor" {Responsável atual} → [366316] Informar número da OS criada para Cadastro de Forn
- [366225] Tarefa "Verificar Insumos" {Fila CSC - Prestação de Serviços} → [G82062] Informações são suficiente?
- [366226] EventoIntermediarioMensagem "PBe - Informar Conta Contábil" → [366266] Informar Conta Contábil
- [366227] Tarefa "Aguardar aprovação Gesap-Diage" {Fila Pendencia de Aprovação} → [G82071] Aprovado?
- [366228] Tarefa "Preencher informações de Faturamento para relatório" {Fila CSC - Prestação de Serviços} → [366225] Verificar Insumos
- [366229] EventoIntermediarioTimer "" → [366256] Reiteração
- [366230] EventoIntermediarioTimer "" → [366298] Ausência de informações
- [366231] EventoIntermediarioTimer "" → [366252] PBe - Conta Contábil
- [366232] EventoIntermediarioTimer "" → [366311] Aviso de cancelamento de chamado por falta de resp
- [366233] EventoIntermediarioTimer "" → [366237] Aviso para preenchimento de formulário
- [366285] EventoIntermediarioMensagem "Reprovação Gerente Executivo" → [366275] Verificar Reprovação
 Gerencial (Cliente)
- [366286] Tarefa "Efetuar correções (Orçamento)
" {Cliente} → [366230]  | [366268]  | [366244] Aviso de retorno da Ordem de Serviço
- [366234] Tarefa "Conferencia de Ajuste do Cliente da Reprovação Gerencial" {Fila CSC - Prestação de Serviços} → [G82079] Submeter novamente para aprovação?
- [366235] FimCancelamento "Cancelamento por reprovação" → (fim)
- [366236] Tarefa "Informar código do item" {Responsável atual} → [G82073] O item desejado encontra-se cadastrado?
- [366237] EventoIntermediarioMensagem "Aviso para preenchimento de formulário" → [366262] Responder Questionário Pesquisa de Mercado e Mitig
- [366238] EventoIntermediarioMensagem "Conferir Parecer" → [366240] Conferir itens, Pareceres e Aprovadores
- [366287] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório." {Responsável atual} → [366251] Solicitar aprovação do Cliente
- [366288] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório." {Responsável atual} → [366319] Solicitar aprovação do Gerente Executivo da Contra
- [366289] EventoIntermediarioMensagem "Ausência de informações" → [366247] Efetuar correções (Insumos)

- [366290] Tarefa "Aguardar aprovação Gemac" {Responsável atual} → [G82078] Aprovador pelo Gestor?
- [366291] SubProcesso "Cadastro de Fornecedor" {Responsável atual} → [366292] Informar número da OS criada para Cadastro de Forn
- [366239] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório." {Responsável atual} → [366280] Aprovação
- [366240] Tarefa "Conferir itens, Pareceres e Aprovadores" {Fila CSC - Prestação de Serviços} → [366269]  | [366243] Avaliar se a conta contábil e a uor utilizadas são
- [366241] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório." {Responsável atual} → [366254] Solicitar aprovação conforme NI006
- [366292] Tarefa "Informar número da OS criada para Cadastro de Fornecedor" {Fila CSC - Prestação de Serviços} → [366260] Recolhe aprovações e outras informações para preen
- [366293] Tarefa "Verificar se o fornecedor está cadastrado
" {Responsável atual} → [G82074] Fornecedor Cadastrado?
- [366294] EventoIntermediarioMensagem "Reprovação Gemac" → [366276] Ajustar reprovação Gemac (Cliente)
- [366295] EventoIntermediarioMensagem "PBe - Aviso sobre abertura de chamado" → [366228] Preencher informações de Faturamento para relatóri
- [366296] EventoIntermediarioMensagem "PBe - Consulta conta orçamentária" → [366300] Verificar Dados Orçamentários
- [366242] EventoIntermediarioMensagem "Reprovação Gerente da Contratação" → [366275] Verificar Reprovação
 Gerencial (Cliente)
- [366243] Tarefa "Avaliar se a conta contábil e a uor utilizadas são da Gemac e se rubrica são da Gesap" {Responsável atual} → [G82072] Enviar para aprovação?
- [366244] EventoIntermediarioMensagem "Aviso de retorno da Ordem de Serviço" → [366318] Retorno de devolução ao cliente para nova solicita
- [366245] EventoIntermediarioMensagem "Aviso de cancelamento de chamado por falta de ajustes" → [366306] Cancelado
- [366246] EventoIntermediarioMensagem "Término de Serviço" → [366297] 
- [366297] EventoFinal "" {Responsável atual} → (fim)
- [366298] EventoIntermediarioMensagem "Ausência de informações" → [366286] Efetuar correções (Orçamento)

- [366299] EventoIntermediarioMensagem "Aviso de aprovação ao Gestor" → [366279] Aguardar aprovação Gesap
- [366300] SubProcesso "Verificar Dados Orçamentários" {Fila CSC - Prestação de Serviços} → [366301] Avançar tarefa
- [366301] Tarefa "Avançar tarefa" {Fila CSC - Prestação de Serviços} → [G82066] A conta orçamentária possui saldo?
- [G82061] Gateway "Pesquisa Prévia anexada?" → «Sim» [G82068] Necessita de Pesquisa de Mercado Complementar? | «Não» [366307] Preencher dados para pesquisa de mercado
- [G82062] Gateway "Informações são suficiente?" → «Sim» [366236] Informar código do item | «Não» [366289] Ausência de informações
- [G82063] Gateway "Direcionamento Interno" → «Enviar para "Compras Diretas" - Avançar» [366283] Compras Diretas | «Retorno ao inicio do processo "Verificar Insumos"» [366225] Verificar Insumos | «Retorno á Controladoria para reavaliação do parecer» [366300] Verificar Dados Orçamentários | «Retorno á Contabilidade para reavaliação do parecer» [366266] Informar Conta Contábil
- [G82064] Gateway "Gerentes Aprovaram?" → «Aprovado» [G82077] Solicitar aprovação do Gerente Executivo? | «Reprovado» [366242] Reprovação Gerente da Contratação
- [G82065] Gateway "Cliente Aprovou?" → «Aprovado» [366261] Recolhe aprovações e outras informações para preen | «Reprovado» [366267] Reprovação Cliente
- [G82066] Gateway "A conta orçamentária possui saldo?" → «Sim» [366274] Conferir PBe para envio de aprovação | «Não» [366298] Ausência de informações
- [G82067] Gateway "Submeter novamente para aprovação?" → «Sim» [366278] Cancela aprovação cliente | «Não (Cancelar Chamado)» [366235] Cancelamento por reprovação
- [G82068] Gateway "Necessita de Pesquisa de Mercado Complementar?" → «Não» [366265] Cadastrar pesquisa de mercado e Valor referencial | «Sim» [366307] Preencher dados para pesquisa de mercado
- [G82069] Gateway "Itens da Gesap?" → «Sim» [366258] Aviso de aprovação ao Gestor | «Não» [366295] PBe - Aviso sobre abertura de chamado
- [G82070] Gateway "Aprovado?" → «Aprovado» [366287] Recolhe aprovações e outras informações para preen | «Reprovado» [366250] Aviso de cancelamento por reprovação gerencial
- [G82071] Gateway "Aprovado?" → «Reprovado» [366273] Aviso de cancelamento por reprovação da Diage | «Aprovado» [366295] PBe - Aviso sobre abertura de chamado
- [G82072] Gateway "Enviar para aprovação?" → «Sim - Prosseguir com a demanda ou rubrica Gesap-Diage já aprovada» [366287] Recolhe aprovações e outras informações para preen | «Sim - No caso de se tratar de utilização de Conta Contábil e UOR da Gemac» [366259] Aviso de utilização de Conta Contábil e UOR refere | «Sim - Se for Conta Orçamentária da Gesap-Diage e não houver aprovação anterior» [366299] Aviso de aprovação ao Gestor | «Não - Retornar ao inicio do processo "Verificar Insumos"» [366225] Verificar Insumos
- [G82073] Gateway "O item desejado encontra-se cadastrado?" → «Não» [366281] Preencher dados para cadastro de itens | «Sim» [G82061] Pesquisa Prévia anexada?
- [G82074] Gateway "Fornecedor Cadastrado?" → «Sim, já cadastrado» [366260] Recolhe aprovações e outras informações para preen | «Não, cadastrar fornecedor» [366291] Cadastro de Fornecedor | «Sim, atualizar cadastro» [366284] Cadastro de Fornecedor
- [G82075] Gateway "Será realizado Remanejamento Orçamentário?" → «Sim» [366312] Remanejamento Orçamentário | «Não» [366308] Aviso sobre cancelamento de Ordem de Serviço
- [G82076] Gateway "Gerente Executivo aprovou?" → «Aprovado» [366239] Recolhe aprovações e outras informações para preen | «Reprovado» [366285] Reprovação Gerente Executivo
- [G82077] Gateway "Solicitar aprovação do Gerente Executivo?" → «Não» [366239] Recolhe aprovações e outras informações para preen | «Sim» [366288] Recolhe aprovações e outras informações para preen
- [G82078] Gateway "Aprovador pelo Gestor?" → «Aprovado» [366287] Recolhe aprovações e outras informações para preen | «Reprovado» [366294] Reprovação Gemac
- [G82079] Gateway "Submeter novamente para aprovação?" → «Sim» [366302] Cancela aprovação gerentes | «Não (Cancelar Chamado)» [366235] Cancelamento por reprovação
- [G82080] Gateway "Tem orçamento para conta/UOR informada?" → «Sim» [366226] PBe - Informar Conta Contábil | «Não» [G82075] Será realizado Remanejamento Orçamentário?

## Gateways
### [G82061] Pesquisa Prévia anexada? (DataBasedExclusiveDecision)
Codigo=PESQPREVIA
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO6"] == "Sim"
```
- alternativa → [G82068] Necessita de Pesquisa de Mercado Complementar?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366307] Preencher dados para pesquisa de mercado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82062] Informações são suficiente? (EventBasedExclusiveDecision)
Codigo=INSFALT
- alternativa → [366236] Informar código do item: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
- alternativa → [366289] Ausência de informações: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; RotuloMotivo=Informar Pendência(s); MotivoObrigatorio=true; PublicarRespostaAA=true
### [G82063] Direcionamento Interno (EventBasedExclusiveDecision)
- alternativa → [366283] Compras Diretas: OperadorDecision=Equal; ReferenciaDecision=Enviar para "Compras Diretas" - Avançar; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
Não
```
- alternativa → [366225] Verificar Insumos: OperadorDecision=Equal; ReferenciaDecision=Retorno ao inicio do processo "Verificar Insumos"; SequenciaAvaliacao=1
- alternativa → [366300] Verificar Dados Orçamentários: OperadorDecision=Equal; ReferenciaDecision=Retorno á Controladoria para reavaliação do parecer; SequenciaAvaliacao=2
- alternativa → [366266] Informar Conta Contábil: OperadorDecision=Equal; ReferenciaDecision=Retorno á Contabilidade para reavaliação do parecer; SequenciaAvaliacao=3
### [G82064] Gerentes Aprovaram? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVACAO_GERENTES")
```
- alternativa → [G82077] Solicitar aprovação do Gerente Executivo?: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366242] Reprovação Gerente da Contratação: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82065] Cliente Aprovou? (DataBasedExclusiveDecision)
Codigo=APROVAÇÃOCLIENTE
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAÇÃOCLIENTE")
```
- alternativa → [366261] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366267] Reprovação Cliente: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82066] A conta orçamentária possui saldo? (DataBasedExclusiveDecision)
Codigo=INSFALTNOVO
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO14"] == "Sim"
```
- alternativa → [366274] Conferir PBe para envio de aprovação: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366298] Ausência de informações: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82067] Submeter novamente para aprovação? (EventBasedExclusiveDecision)
- alternativa → [366278] Cancela aprovação cliente: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0; PublicarRespostaAA=true
- alternativa → [366235] Cancelamento por reprovação: OperadorDecision=Equal; ReferenciaDecision=Não (Cancelar Chamado); SequenciaAvaliacao=1; PublicarRespostaAA=true
### [G82068] Necessita de Pesquisa de Mercado Complementar? (EventBasedExclusiveDecision)
Codigo=PESQCOMPLEMENTAR
- alternativa → [366265] Cadastrar pesquisa de mercado e Valor referencial: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
- alternativa → [366307] Preencher dados para pesquisa de mercado: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1; RotuloMotivo=Informar quais pendências para finalizar cotação (ex. falta 1 proposta, falta item, necessita de ajustes, etç).; MotivoObrigatorio=true; PublicarRespostaAA=true
### [G82069] Itens da Gesap? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO20"] == "Sim"
```
- alternativa → [366258] Aviso de aprovação ao Gestor: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366295] PBe - Aviso sobre abertura de chamado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82070] Aprovado? (DataBasedExclusiveDecision)
Codigo=APROVACAOGESTORGESAP
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVACAO_GESTORGESAP")
```
- alternativa → [366287] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366250] Aviso de cancelamento por reprovação gerencial: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
Reprovado
```
### [G82071] Aprovado? (DataBasedExclusiveDecision)
Codigo=APROVACAOGESTORGESAP1
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVACAO_GESTORGESAP1")
```
- alternativa → [366273] Aviso de cancelamento por reprovação da Diage: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
Reprovado
```
- alternativa → [366295] PBe - Aviso sobre abertura de chamado: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G82072] Enviar para aprovação? (EventBasedExclusiveDecision)
- alternativa → [366287] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Sim - Prosseguir com a demanda ou rubrica Gesap-Diage já aprovada; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [366259] Aviso de utilização de Conta Contábil e UOR refere: OperadorDecision=Equal; ReferenciaDecision=Sim - No caso de se tratar de utilização de Conta Contábil e UOR da Gemac; SequenciaAvaliacao=1
- alternativa → [366299] Aviso de aprovação ao Gestor: OperadorDecision=Equal; ReferenciaDecision=Sim - Se for Conta Orçamentária da Gesap-Diage e não houver aprovação anterior; SequenciaAvaliacao=2
- alternativa → [366225] Verificar Insumos: OperadorDecision=Equal; ReferenciaDecision=Não - Retornar ao inicio do processo "Verificar Insumos"; SequenciaAvaliacao=3
**ValorComparacaoDecision**
```python
Não
```
### [G82073] O item desejado encontra-se cadastrado? (EventBasedExclusiveDecision)
- alternativa → [366281] Preencher dados para cadastro de itens: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G82061] Pesquisa Prévia anexada?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
### [G82074] Fornecedor Cadastrado? (EventBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
#OrdemServico["FORNECEDOR_CADASTRADO"] == "Atualizar"
```
- alternativa → [366260] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Sim, já cadastrado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
3
```
- alternativa → [366291] Cadastro de Fornecedor: OperadorDecision=Equal; ReferenciaDecision=Não, cadastrar fornecedor; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
1
```
- alternativa → [366284] Cadastro de Fornecedor: OperadorDecision=Equal; ReferenciaDecision=Sim, atualizar cadastro; SequenciaAvaliacao=2
**ValorComparacaoDecision**
```python
2
```
### [G82075] Será realizado Remanejamento Orçamentário? (EventBasedExclusiveDecision)
Referencia=Crie na próxima etapa o chamado de Remanejamento Orçamentário caso tenha os dados pelo cliente para registro ou informe que não irá ter remanejamento para o can…; Codigo=SERAFEITOREM
- alternativa → [366312] Remanejamento Orçamentário: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
- alternativa → [366308] Aviso sobre cancelamento de Ordem de Serviço: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=2; RotuloMotivo=Informe o motivo para cancelamento do chamado; MotivoObrigatorio=true; PublicarRespostaAA=true
### [G82076] Gerente Executivo aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR_GEREX")
```
- alternativa → [366239] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366285] Reprovação Gerente Executivo: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82077] Solicitar aprovação do Gerente Executivo? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO7"] == "Sim"
```
- alternativa → [366239] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [366288] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G82078] Aprovador pelo Gestor? (DataBasedExclusiveDecision)
Codigo=APROVACAOGESTORDIMAC
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVACAO_GESTORDIMAC")
```
- alternativa → [366287] Recolhe aprovações e outras informações para preen: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [366294] Reprovação Gemac: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82079] Submeter novamente para aprovação? (EventBasedExclusiveDecision)
- alternativa → [366302] Cancela aprovação gerentes: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0; PublicarRespostaAA=true
- alternativa → [366235] Cancelamento por reprovação: OperadorDecision=Equal; ReferenciaDecision=Não (Cancelar Chamado); SequenciaAvaliacao=1; PublicarRespostaAA=true
### [G82080] Tem orçamento para conta/UOR informada? (DataBasedExclusiveDecision)
Codigo=UORTEMORÇAM
**ExpressaoComparacaoDecision**
```python
OrdemServico["SIM_NAO3"] == "Sim"
```
- alternativa → [366226] PBe - Informar Conta Contábil: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G82075] Será realizado Remanejamento Orçamentário?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [366247] Tarefa "Efetuar correções (Insumos)
"
Responsável: Cliente (papel 18)
Config: PermiteCancelamentoAA=true; RotuloBotaoAvancar=Avançar (Enviar para Cesec)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.ModificaCampoFormularioVisivel('SIM_NAO6', True)

OrdemServico.Salva()

import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Efetuar Correções (Insumos)'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Efetuar correções (Insumos)'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptValidacao**
```python
#--- Validação de subcampos conforme marcação

uor = OrdemServico.GetCustom("UOR")
gerex = OrdemServico.GetCustom('PPGEREX_NEGOCIO')

if OrdemServico.GetCustom("SIM_NAO6") == 'Sim': 
    if OrdemServico.GetCustom("SIM_NAO7") == 'Sim':
        if String.IsNullOrEmpty(gerex):
            Criticas.AdicionaPendencia("Informe o(a) Gerente Executivo(a) que efetuará a aprovação.")
         
    if OrdemServico.GetCustom("TIPO_DE_VALOR_DE_REFERENCIA") == 'Outros:':
        if String.IsNullOrEmpty(OrdemServico.GetCustom('JUSTIFICATIVA_IMPACTO')): 
            Criticas.AdicionaPendencia("Preencha o campo 'Informe detalhadamente o método estatístico utilizado (Valor Referencial)'.")
         
    if OrdemServico.GetCustom("SIM_NAO1") == 'Não':
        if String.IsNullOrEmpty(OrdemServico.GetCustom('OBS6')): 
            Criticas.AdicionaPendencia("Preencha o campo 'JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002'.")
```
**ScriptFormCarregado**
```python
Formulario["SIM_NAO6"].Valor = '[Nenhum(a)]'
Formulario["VALOR_DOD"].Visivel = False
Formulario["VALOR"].Visivel = False
Formulario["CSC_ESCOLARIDADE"].Visivel = False
Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = False
Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = False
Formulario["OBS6"].Visivel = False
Formulario["CODIGO_ITEM"].Visivel = False
Formulario["VALOR_REFERENCIAL"].Visivel = False
Formulario["SIM_NAO1"].Visivel = False
Formulario["QTD_PESQUISA"].Visivel = False
Formulario["QTD_PESQUISA"].Habilitado = False

Formulario["OBS5"].Visivel = False
Formulario["OBS5"].Habilitado = False

Formulario["OBS50"].Visivel = False
Formulario["OBS50"].Habilitado = False

Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Visivel = False
Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais para a Pesquisa de Mercado
  - SIM_NAO6 "Há pesquisa de mercado prévia? Se sim, favor anexar. Caso selecione 'Não', automaticamente será criado um subprocesso 'Pesquisa de Mercado' para cotação." [DropDownList String → CPE_CSC.SIM_NAO6] obrigatório
**SIM_NAO6.ScriptModificado**
```python
if Formulario['SIM_NAO6'].Valor == "Sim":
   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = True
   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = True
   Formulario['JUSTIFICATIVA_IMAGEM'].Habilitado = True
   Formulario['JUSTIFICATIVA_IMAGEM'].Visivel = True
   Formulario['JUSTIFICATIVA_TENDENCIA'].Habilitado = True
   Formulario['JUSTIFICATIVA_TENDENCIA'].Visivel = True
   Formulario['FQ415_066_ITEM31'].Habilitado = True
   Formulario['FQ415_066_ITEM31'].Visivel = True
   Formulario['FQ415_066_ITEM32'].Habilitado = True
   Formulario['FQ415_066_ITEM32'].Visivel = True
   Formulario['FQ415_066_ITEM321'].Habilitado = True
   Formulario['FQ415_066_ITEM321'].Visivel = True
   Formulario['FQ415_066_ITEM322'].Habilitado = True
   Formulario['FQ415_066_ITEM322'].Visivel = True
   Formulario['FQ415_066_ITEM33'].Habilitado = True
   Formulario['FQ415_066_ITEM33'].Visivel = True
   Formulario['FQ415_066_ITEM331'].Habilitado = True
   Formulario['FQ415_066_ITEM331'].Visivel = True
   Formulario['SIM_NAO1'].Habilitado = True
   Formulario['SIM_NAO1'].Visivel = True
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Habilitado = True
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Visivel = True
   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = False
   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = False
   Formulario['OBS6'].Habilitado = False
   Formulario['OBS6'].Visivel = False   

if Formulario['SIM_NAO6'].Valor != "Sim":
   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = False
   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = False
   Formulario['JUSTIFICATIVA_IMAGEM'].Habilitado = False
   Formulario['JUSTIFICATIVA_IMAGEM'].Visivel = False
   Formulario['JUSTIFICATIVA_TENDENCIA'].Habilitado = False
   Formulario['JUSTIFICATIVA_TENDENCIA'].Visivel = False
   Formulario['FQ415_066_ITEM31'].Habilitado = False
   Formulario['FQ415_066_ITEM31'].Visivel = False
   Formulario['FQ415_066_ITEM32'].Habilitado = False
   Formulario['FQ415_066_ITEM32'].Visivel = False
   Formulario['FQ415_066_ITEM321'].Habilitado = False
   Formulario['FQ415_066_ITEM321'].Visivel = False
   Formulario['FQ415_066_ITEM322'].Habilitado = False
   Formulario['FQ415_066_ITEM322'].Visivel = False
   Formulario['FQ415_066_ITEM33'].Habilitado = False
   Formulario['FQ415_066_ITEM33'].Visivel = False
   Formulario['FQ415_066_ITEM331'].Habilitado = False
   Formulario['FQ415_066_ITEM331'].Visivel = False
   Formulario['SIM_NAO1'].Habilitado = False
   Formulario['SIM_NAO1'].Visivel = False
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Habilitado = False
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Visivel = False
   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = False
   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = False
   Formulario['OBS6'].Habilitado = False
   Formulario['OBS6'].Visivel = False
```
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - JUSTIFICATIVA_IMPACTO "Informe detalhadamente o método estatístico utilizado (Valor Referencial)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. Caso tenha o mínimo de três propostas validas informe `Não se aplica¿." [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario['SIM_NAO1'].Valor == "Não":
   Formulario['OBS6'].Habilitado = True
   Formulario['OBS6'].Visivel = True
else:
   Formulario['OBS6'].Habilitado = False
   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184 Mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar 'Não se aplica'. (Sugere-se, preferencialmente, utilizar o método estatístico de média ou mediana)" [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
**TIPO_DE_VALOR_DE_REFERENCIA.ScriptModificado**
```python
if Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Valor == 'Outros:':
   Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = True
   Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True
    
if Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Valor != 'Outros:':
   Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = False
#   Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True

#Lembrete de referencial escolhido

if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Maior Preço":
    Formulario.ExibeMensagem("Lembrete: \n\nMétodo estatístico de 'Maior Preço' prejudicial á BBTS. Somente aceito com Nota Técnica anexa com 'de acordo' da Gesuc, com fundamentação da necessidade.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Não se aplica":
    Formulario.ExibeMensagem("Lembrete: \n\nMétodo estatístico 'Não se aplica' informado somente em Inexigibilidade de Licitação (inviabilidade de competição); com todos os insumos da TAB415-001 anexados.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Outros:":
    Formulario.ExibeMensagem("Lembrete: \n\nSe ultilizado método estatístico diferente dos convencionais (Média, Mediana ou Menor Valor) é obrigatório informar detalhadamente abaixo o 'Método estatístico utilizado (Valor Referencial)', com critérios fundamentados.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Menor Preço":
    Formulario.ExibeMensagem("Lembrete: \n\nSugere-se, preferencialmente, utilizar o método estatístico de Média ou Mediana. Este item estipula o valor referencial para a aprovação do orçamento (até quanto poderá ser gasto); não o critério de escolha do fornecedor, informado no item abaixo 'Justificativa da escolha do(s) fornecedor(es)' de padrão como 'Melhor/Menor Preço.'.")
```
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79 mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
  - CSC_DGCO "Informar para quantas regiões é esta demanda:" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório
  - PENF_EMAIL "E-mails que serão notificados sobre o andamento da ordem de serviço (separados por ponto e vírgula)" [TextBox String(2000) → CPE_PENF.PENF_EMAIL] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Projeto Básico
  - SIM_NAO "É contratação de TIC? " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
#if Formulario['SIM_NAO'].Valor == "Sim":
#   Formulario['SIM_NAO5'].Habilitado = True
#   Formulario['SIM_NAO5'].Visivel = True
#
#if Formulario['SIM_NAO'].Valor != "Sim":
#    Formulario['SIM_NAO5'].Habilitado = False
#    Formulario['SIM_NAO5'].Visivel = False
```
  - SIM_NAO5 "Aplica-se os artefatos da NI642?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
  - COMBOBOX10 "Natureza Contábil" [DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10] obrigatório
  - CONTA_CONTABIL1 "Conta Contábil (Não obrigatório) - A informação será validada pela Gefic" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1]
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica"." [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]
  - VALOR_DOD "Preço Global Referencial: R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]
  - VALOR "DOTAÇÃO ORÇAMENTÁRIA (VALOR GLOBAL OU VALOR GLOBAL ESTIMADO): R$ " [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - SIM_NAO10 "Possui itens que utilizaram logo e/ou marca BBTS?" [DropDownList String → CPE_CSC.SIM_NAO10] obrigatório
**SIM_NAO10.ScriptModificado**
```python
if Formulario['SIM_NAO10'].Valor == "Sim":
    Formulario.ExibeMensagem("Lembrete: \n\nPara solicitações que utilizaram logo e/ou marca BBTS, é obrigatório informar o número da O.S. do Remanejamento Orçamentário, considerando que somente a GEMAC possui rúbrica orçamentária de MARKETING.")
    Formulario["TEXT"].Visivel = True
    Formulario["TEXT"].Habilitado = True

if Formulario['SIM_NAO10'].Valor == "Não":
    Formulario["TEXT"].Visivel = False
    Formulario["TEXT"].Habilitado = False
```
  - TEXT "Número O.S. (Remanejamento Orçamentário) - Informe N/A se for a própria Gemac a Área Cliente." [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
  - SIM_NAO_100 "De acordo com o objeto da contratação se trata de:" [DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100] obrigatório
  - SIM_NAO7 "Solicitar aprovação do Gerente Executivo?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
**SIM_NAO7.ScriptModificado**
```python
if Formulario['SIM_NAO7'].Valor == "Não":
   Formulario['PPGEREX_NEGOCIO'].Habilitado = False
   Formulario['PPGEREX_NEGOCIO'].Visivel = False

if Formulario['SIM_NAO7'].Valor != "Sim":
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
```
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO]
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX

if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - DIRETORIA_GERENCIA "Área Técnica (quando couber)" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
  - LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV]
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna CODIGO obrigatório
    - coluna PROD_PRODUTO obrigatório
    - coluna ITEM obrigatório
    - coluna ITEM_OBSOLETO obrigatório
    - coluna PROD_NCM
    - coluna PROD_DATA_REC obrigatório
    - coluna NECESSIDADE obrigatório
  - PB_OBJETO_CONTRATACAO "1. Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
    - coluna NOTA_FISCAL obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna PATRIMONIO obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
  - TIPO_ATIVIDADE "Classificação da Atividade" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
#if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
#   Formulario['LABEL6'].Habilitado = True
#   Formulario['LABEL6'].Visivel = True
#   
#
#if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
#    Formulario['LABEL6'].Habilitado = False
#    Formulario['LABEL6'].Visivel = False
```
  - UOR "Informe a(s) UOR(s) de alocação de despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] — PosicaoRotulo=Topo
    - coluna UOR
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
  - SIM_NAO4 "Deseja que o Cesec faça a pesquisa de mercado para o objeto?" [DropDownList String → CPE_CSC.SIM_NAO4] obrigatório
**SIM_NAO4.ScriptModificado**
```python
if Formulario['SIM_NAO4'].Valor == "Não":
 #  Formulario['UNITARIO_OU_LOTE'].Habilitado = True
 #  Formulario['UNITARIO_OU_LOTE'].Visivel = True
   Formulario['QTD_PESQUISA'].Habilitado = True
   Formulario['QTD_PESQUISA'].Visivel = True
   Formulario['VALOR_DOD'].Habilitado = True
   Formulario['VALOR_DOD'].Visivel = True
   Formulario['VALOR_DOD'].Habilitado = True
   Formulario['VALOR_DOD'].Visivel = True
   Formulario['VALOR_REFERENCIAL'].Visivel = True
   Formulario['VALOR_REFERENCIAL'].Habilitado = True   
   Formulario['SIM_NAO1'].Visivel = True
   Formulario['SIM_NAO1'].Habilitado = True
   Formulario['APROVADOR_PB'].Visivel = True
   Formulario['APROVADOR_PB'].Habilitado = True
   Formulario['LABEL13'].Visivel = False
   Formulario['LABEL12'].Visivel = False
   Formulario['LABEL10'].Visivel = False
   Formulario['LABEL11'].Visivel = False
   Formulario['LISTA_ITENS_PESQ_MERC'].Visivel = False
   Formulario['OBS2'].Visivel = False
   Formulario['QUANTIDADE_ESTIMADA'].Visivel = False
   Formulario['POSSUI_DGCO'].Visivel = False
   Formulario['TIPO_DA_DEMANDA'].Visivel = False
   Formulario['CSC_DGCO'].Visivel = False
   Formulario['SERV_ART_29_LEI_13303'].Visivel = False
   Formulario['LABEL57'].Visivel = False
   Formulario['LABEL55'].Visivel = False
   Formulario['LABEL56'].Visivel = False
   Formulario['DESCRICAO_DETALHADA'].Visivel = False
   
if Formulario['SIM_NAO4'].Valor != "Não":
 #  Formulario['UNITARIO_OU_LOTE'].Habilitado = False
 #  Formulario['UNITARIO_OU_LOTE'].Visivel = False
   Formulario['QTD_PESQUISA'].Habilitado = False
   Formulario['QTD_PESQUISA'].Visivel = False
   Formulario['VALOR_DOD'].Habilitado = False
   Formulario['VALOR_DOD'].Visivel = False
   Formulario['VALOR_REFERENCIAL'].Visivel = False
   Formulario['VALOR_REFERENCIAL'].Habilitado = False   
   Formulario['SIM_NAO1'].Visivel = False
   Formulario['SIM_NAO1'].Habilitado = False
   Formulario['APROVADOR_PB'].Visivel = True
   Formulario['APROVADOR_PB'].Habilitado = True
   Formulario['LABEL13'].Visivel = True
   Formulario['LABEL12'].Visivel = True
   Formulario['LABEL10'].Visivel = True
   Formulario['LABEL11'].Visivel = True
   Formulario['LISTA_ITENS_PESQ_MERC'].Visivel = True
   Formulario['OBS2'].Visivel = True
   Formulario['QUANTIDADE_ESTIMADA'].Visivel = True
   Formulario['POSSUI_DGCO'].Visivel = True
   Formulario['TIPO_DA_DEMANDA'].Visivel = True
   Formulario['CSC_DGCO'].Visivel = True
   Formulario['SERV_ART_29_LEI_13303'].Visivel = True
   Formulario['LABEL57'].Visivel = True
   Formulario['LABEL55'].Visivel = True
   Formulario['LABEL56'].Visivel = True
   Formulario['DESCRICAO_DETALHADA'].Visivel = True
```
  - QTD_PESQUISA "Quantidade de Pesquisas" [DropDownList String → CPE_CSC.QTD_PESQUISA] obrigatório
**QTD_PESQUISA.ScriptModificado**
```python
#if Formulario["QTD_PESQUISA"].Valor == "6":
#    Formulario["FORNECEDOR01"].Visivel = True
#    Formulario["FORNECEDOR01"].Habilitado = True
#    Formulario["PESQUISA_MERCADO1"].Visivel = True
#    Formulario["PESQUISA_MERCADO1"].Habilitado = True
#    Formulario["FORNECEDOR2"].Visivel = True
#    Formulario["FORNECEDOR2"].Habilitado = True
#    Formulario["PESQUISA_MERCADO2"].Visivel = True
#    Formulario["PESQUISA_MERCADO2"].Habilitado = True
#    Formulario["FORNECEDOR3"].Visivel = True
#    Formulario["FORNECEDOR3"].Habilitado = True
#    Formulario["PESQUISA_MERCADO3"].Visivel = True
#    Formulario["PESQUISA_MERCADO3"].Habilitado = True
#    Formulario["FORNECEDOR4"].Visivel = True
#    Formulario["FORNECEDOR4"].Habilitado = True
#    Formulario["PESQUISA_MERCADO4"].Visivel = True
#    Formulario["PESQUISA_MERCADO4"].Habilitado = True
#    Formulario["FORNECEDOR5"].Visivel = True
#    Formulario["FORNECEDOR5"].Habilitado = True
#    Formulario["PESQUISA_MERCADO_5"].Visivel = True
#    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
#    Formulario["FORNECEDOR6"].Visivel = True
#    Formulario["FORNECEDOR6"].Habilitado = True
#    Formulario["PESQUISA_MERCADO6"].Visivel = True
#    Formulario["PESQUISA_MERCADO6"].Habilitado = True
#
#
#if Formulario["QTD_PESQUISA"].Valor == "5":
#    Formulario["FORNECEDOR01"].Visivel = True
#    Formulario["FORNECEDOR01"].Habilitado = True
#    Formulario["PESQUISA_MERCADO1"].Visivel = True
#    Formulario["PESQUISA_MERCADO1"].Habilitado = True
#    Formulario["FORNECEDOR2"].Visivel = True
#    Formulario["FORNECEDOR2"].Habilitado = True
#    Formulario["PESQUISA_MERCADO2"].Visivel = True
#    Formulario["PESQUISA_MERCADO2"].Habilitado = True
#    Formulario["FORNECEDOR3"].Visivel = True
#    Formulario["FORNECEDOR3"].Habilitado = True
#    Formulario["PESQUISA_MERCADO3"].Visivel = True
#    Formulario["PESQUISA_MERCADO3"].Habilitado = True
#    Formulario["FORNECEDOR4"].Visivel = True
#    Formulario["FORNECEDOR4"].Habilitado = True
#    Formulario["PESQUISA_MERCADO4"].Visivel = True
#    Formulario["PESQUISA_MERCADO4"].Habilitado = True
#    Formulario["FORNECEDOR5"].Visivel = True
#    Formulario["FORNECEDOR5"].Habilitado = True
#    Formulario["PESQUISA_MERCADO_5"].Visivel = True
#    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
#    Formulario["FORNECEDOR6"].Visivel = False
#    Formulario["FORNECEDOR6"].Habilitado = False
#    Formulario["PESQUISA_MERCADO6"].Visivel = False
#    Formulario["PESQUISA_MERCADO6"].Habilitado = False
#    
#if Formulario["QTD_PESQUISA"].Valor == "4":
#    Formulario["FORNECEDOR01"].Visivel = True
#    Formulario["FORNECEDOR01"].Habilitado = True
#    Formulario["PESQUISA_MERCADO1"].Visivel = True
#    Formulario["PESQUISA_MERCADO1"].Habilitado = True
#    Formulario["FORNECEDOR2"].Visivel = True
#    Formulario["FORNECEDOR2"].Habilitado = True
#    Formulario["PESQUISA_MERCADO2"].Visivel = True
#    Formulario["PESQUISA_MERCADO2"].Habilitado = True
#    Formulario["FORNECEDOR3"].Visivel = True
#    Formulario["FORNECEDOR3"].Habilitado = True
#    Formulario["PESQUISA_MERCADO3"].Visivel = True
#    Formulario["PESQUISA_MERCADO3"].Habilitado = True
#    Formulario["FORNECEDOR4"].Visivel = True
#    Formulario["FORNECEDOR4"].Habilitado = True
#    Formulario["PESQUISA_MERCADO4"].Visivel = True
#    Formulario["PESQUISA_MERCADO4"].Habilitado = True
#    Formulario["FORNECEDOR5"].Visivel = False
#    Formulario["FORNECEDOR5"].Habilitado = False
#    Formulario["PESQUISA_MERCADO_5"].Visivel = False
#    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
#    Formulario["FORNECEDOR6"].Visivel = False
#    Formulario["FORNECEDOR6"].Habilitado = False
#    Formulario["PESQUISA_MERCADO6"].Visivel = False
#    Formulario["PESQUISA_MERCADO6"].Habilitado = False
#
#if Formulario["QTD_PESQUISA"].Valor == "3":
#    Formulario["FORNECEDOR01"].Visivel = True
#    Formulario["FORNECEDOR01"].Habilitado = True
#    Formulario["PESQUISA_MERCADO1"].Visivel = True
#    Formulario["PESQUISA_MERCADO1"].Habilitado = True
#    Formulario["FORNECEDOR2"].Visivel = True
#    Formulario["FORNECEDOR2"].Habilitado = True
#    Formulario["PESQUISA_MERCADO2"].Visivel = True
#    Formulario["PESQUISA_MERCADO2"].Habilitado = True
#    Formulario["FORNECEDOR3"].Visivel = True
#    Formulario["FORNECEDOR3"].Habilitado = True
#    Formulario["PESQUISA_MERCADO3"].Visivel = True
#    Formulario["PESQUISA_MERCADO3"].Habilitado = True
#    Formulario["FORNECEDOR4"].Visivel = False
#    Formulario["FORNECEDOR4"].Habilitado = False
#    Formulario["PESQUISA_MERCADO4"].Visivel = False
#    Formulario["PESQUISA_MERCADO4"].Habilitado = False
#    Formulario["FORNECEDOR5"].Visivel = False
#    Formulario["FORNECEDOR5"].Habilitado = False
#    Formulario["PESQUISA_MERCADO_5"].Visivel = False
#    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
#    Formulario["FORNECEDOR6"].Visivel = False
#    Formulario["FORNECEDOR6"].Habilitado = False
#    Formulario["PESQUISA_MERCADO6"].Visivel = False
#    Formulario["PESQUISA_MERCADO6"].Habilitado = False
#    
#if Formulario["QTD_PESQUISA"].Valor == "2":
#    Formulario["FORNECEDOR01"].Visivel = True
#    Formulario["FORNECEDOR01"].Habilitado = True
#    Formulario["PESQUISA_MERCADO1"].Visivel = True
#    Formulario["PESQUISA_MERCADO1"].Habilitado = True
#    Formulario["FORNECEDOR2"].Visivel = True
#    Formulario["FORNECEDOR2"].Habilitado = True
#    Formulario["PESQUISA_MERCADO2"].Visivel = True
#    Formulario["PESQUISA_MERCADO2"].Habilitado = True
#    Formulario["FORNECEDOR3"].Visivel = False
#    Formulario["FORNECEDOR3"].Habilitado = False
#    Formulario["PESQUISA_MERCADO3"].Visivel = False
#    Formulario["PESQUISA_MERCADO3"].Habilitado = True
#    Formulario["FORNECEDOR4"].Visivel = False
#    Formulario["FORNECEDOR4"].Habilitado = False
#    Formulario["PESQUISA_MERCADO4"].Visivel = False
#    Formulario["PESQUISA_MERCADO4"].Habilitado = False
#    Formulario["FORNECEDOR5"].Visivel = False
#    Formulario["FORNECEDOR5"].Habilitado = False
#    Formulario["PESQUISA_MERCADO_5"].Visivel = False
#    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
#    Formulario["FORNECEDOR6"].Visivel = False
#    Formulario["FORNECEDOR6"].Habilitado = False
#    Formulario["PESQUISA_MERCADO6"].Visivel = False
#    Formulario["PESQUISA_MERCADO6"].Habilitado = False
#    
#if Formulario["QTD_PESQUISA"].Valor == "1":
#    Formulario["FORNECEDOR01"].Visivel = True
#    Formulario["FORNECEDOR01"].Habilitado = True
#    Formulario["PESQUISA_MERCADO1"].Visivel = True
#    Formulario["PESQUISA_MERCADO1"].Habilitado = True
#    Formulario["FORNECEDOR2"].Visivel = False
#    Formulario["FORNECEDOR2"].Habilitado = False
#    Formulario["PESQUISA_MERCADO2"].Visivel = False
#    Formulario["PESQUISA_MERCADO2"].Habilitado = False
#    Formulario["FORNECEDOR3"].Visivel = False
#    Formulario["FORNECEDOR3"].Habilitado = False
#    Formulario["PESQUISA_MERCADO3"].Visivel = False
#    Formulario["PESQUISA_MERCADO3"].Habilitado = False
#    Formulario["FORNECEDOR4"].Visivel = False
#    Formulario["FORNECEDOR4"].Habilitado = False
#    Formulario["PESQUISA_MERCADO4"].Visivel = False
#    Formulario["PESQUISA_MERCADO4"].Habilitado = False
#    Formulario["FORNECEDOR5"].Visivel = False
#    Formulario["FORNECEDOR5"].Habilitado = False
#    Formulario["PESQUISA_MERCADO_5"].Visivel = False
#    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
#    Formulario["FORNECEDOR6"].Visivel = False
#    Formulario["FORNECEDOR6"].Habilitado = False
#    Formulario["PESQUISA_MERCADO6"].Visivel = False
#    Formulario["PESQUISA_MERCADO6"].Habilitado = False
```
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna VALOR_REFERENCIAL
**VALOR_REFERENCIAL.VALOR_REFERENCIAL.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_TOTAL obrigatório
    - coluna VALOR_UNITARIO
    - coluna ITEM1 obrigatório
    - coluna ITEM
- Operação PR0004 Associar Itens Configuração: Nome=DOCS3
  - anexo "Pesquisa de Mercado Prévia (Propostas conforme PRO417-002 e FQ415-068; Exemplo: Devem ser em formato PDF com CNPJ, descrição completa, preço unitário, subtotal e total, condição de pagamento pós-pago com no mínimo 10 dias após emissão de NF (faturado 10 DDL), prazo de entrega com frete (CIF) - não destacado por conta do fornecedor, impostos (inclusos), garantia, validade e telefone/e-mail de contato do fornecedor.) " classes: Pesquisa de Mercado — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - APROVADOR_PB "Aprovadores da contratação - Gerente de Divisão, Coordenador e/ou Superintendente" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório — PosicaoRotulo=Topo
    - coluna APROVADORES obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo Complementar as Especificações Técnicas" classes: Especificação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS DE INEXIGIBILIDADE2
  - anexo "" classes: Nota Técnica — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Parecer Jurídico Específico — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Rateio Localidades — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Consulta Consolidada TCU — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: CND FGTS — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Comprovante de exclusividade — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Cartão CNPJ — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Apólice de Seguro – Serviço de Transporte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: CND Federal — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Certidão CNJ — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Comprovação de razoabilidade de preço — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "Demais Documentos (conforme TAB 415-001)" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: QSA - Quadro de Sócios e Administradores — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Anexo I -  Espeficiações Técnicas
  - OBS21 "2. Especificações Técnicas" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - LABEL1 "ATENÇÃO: O campo "2. Especificações Técnicas" tem o limite de 4000 caracteres. Caso o limite de caracteres não seja o suficiente, utilize os campos abaixo para complementar a informação." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - OBS22 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS22]
  - OBS23 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS23]
  - OBS10 "3. Qualificação Técnica" [Memo String(2000) → CPE_CSC.OBS10] obrigatório
  - OBS4 "4. Condições de Entrega" [Memo String(2000) → CPE_CONTRATOS.OBS4] obrigatório
  - OBS7 "Condições de Entrega - Continuação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS7]
  - INFORMACAO_FATURAMENTO "5. Informações para Faturamento: (Incluir os dados da BBTS para o qual será faturado o objeto da contratação - Endereço completo com CEP)" [DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; PosicaoRotulo=Topo
    - coluna CNPJ_BBTS
    - coluna ENDERECO obrigatório
    - coluna ENDERECO_COM_CEP obrigatório
    - coluna INSCRICAO_MUNICIIPAL
    - coluna INSCRICAO_ESTADUAL
  - OBS3 "6. Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico:" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - OBS5 "8. Multa" [Memo String(2000) → CPE_CONTRATOS.OBS5] obrigatório
  - OBS50 "9. Privacidade , Proteção e Tratamento de Dados Pessoais" [Memo String(2000) → CPE_CONTRATOS.OBS50] obrigatório
  - NN_CONDICAO_PAGAMENTO "7. Condições de Pagamento:" [Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO] obrigatório

### [366248] SubProcesso "Cadastro de Itens"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1329; Configuracao={"UtilizaMesmaVersaoProc":false, "ExibirBotaoNovaSubprocessos":true}
MotivoInterrupcaoSLA: Aguardando Fim Subprocesso associado
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Cadastro de Itens'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None

# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": 'Fila CSC',
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Cadastro de Itens'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                pass
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
            else:
                pass
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message), True)
        except Exception as exJson:
            pass
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
finally:
    client.Dispose()
```
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=1145; CustomProperty=PRJ_SRC_USUARIO
  - CustomPropertyId=1146; CustomProperty=PRJ_TIPO_SOLICITACAO
  - CustomPropertyId=1153; CustomProperty=PRJ_UNI_MEDIDA
  - CustomPropertyId=4614; CustomProperty=SERVICO_ITENS_CADASTRADOS
  - PropertyId=1250; Property=Justificativa
  - CustomPropertyId=1061; CustomProperty=LABEL1
  - CustomPropertyId=1158; CustomProperty=PRJ_CATEGORIA_NCM
  - CustomPropertyId=1147; CustomProperty=PRJ_CODIGO_ITEM
  - CustomPropertyId=1148; CustomProperty=PRJ_CODIGO_ITENS
  - CustomPropertyId=1152; CustomProperty=PRJ_DESC_ITEM
  - CustomPropertyId=1163; CustomProperty=PRJ_OBS
  - CustomPropertyId=1157; CustomProperty=PRJ_ORIGEM_ITEM
  - CustomPropertyId=1156; CustomProperty=PRJ_PATRIMONIADO
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2223; ClasseConfiguracao=Anexo
- Relatorios:
  - FormatoExportacao=PDF
- Associação: Ativo=true; FraseAssociacao=Projeto Básico Eletrônico -> Cadastro de Itens; FraseInversaAssociacao=Cadastro de Itens -> Projeto Básico Eletrônico; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=CADPRO; SeparadorSequencial=. | fonte: Projeto Básico Simplificado Eletrônico PBEE → alvo: Cadastro de Itens

### [366302] Tarefa "Cancela aprovação gerentes"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.CancelaAprovacao("APROVACAO_GERENTES")

import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Cancela aprovação gerentes'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Cancela aprovação gerentes'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```

### [366303] Tarefa "Preencher dados (cadastro de Código de Item concluído)"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Preencher dados (cadastro de Código de Item concluído)'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Preencher dados (cadastro de Código de Item concluído)'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0001 Preencher Campos
  - CODIGO_ITEM "Código do Item" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=500
    - coluna ITEM_OBSOLETO obrigatório
    - coluna ITEM
    - coluna NECESSIDADE obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366304] SubProcesso "Pesquisa de Mercado"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=392; PassaTodosItens=true; RetornaTodosItens=true; SincronizaCancelamento=true; Configuracao={"ExibirBotaoNovaSubprocessos":true}
MotivoInterrupcaoSLA: Aguardando Fim Subprocesso associado
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Pesquisa
from Venki.Supravizio.Processo.Custom import Processo
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Pesquisa de Mercado'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None

# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": 'Fila CSC',
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Pesquisa
from Venki.Supravizio.Processo.Custom import Processo
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Pesquisa de Mercado'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- ValoresInputs:
  - CustomPropertyId=2840; CustomProperty=FORNECEDOR01
  - CustomPropertyId=2828; CustomProperty=PESQUISA_MERCADO1
  - CustomPropertyId=2299; CustomProperty=FORNECEDOR2
  - CustomPropertyId=2829; CustomProperty=PESQUISA_MERCADO2
  - CustomPropertyId=2838; CustomProperty=FORNECEDOR3
  - CustomPropertyId=2830; CustomProperty=PESQUISA_MERCADO3
  - CustomPropertyId=2835; CustomProperty=FORNECEDOR4
  - CustomPropertyId=5232; CustomProperty=SIM_NAO20
  - CustomPropertyId=1536; CustomProperty=OBS1
  - CustomPropertyId=2930; CustomProperty=CODIGO_ITEM
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=1540; CustomProperty=OBS5
  - CustomPropertyId=4585; CustomProperty=OBS50
  - CustomPropertyId=580; CustomProperty=DESCRICAO_OBRIG
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "PESQMERCSIM")
```
  - CustomPropertyId=2359; CustomProperty=TIPO_DA_DEMANDA
  - CustomPropertyId=2379; CustomProperty=OBS8
  - CustomPropertyId=2360; CustomProperty=SERV_ART_29_LEI_13303
  - CustomPropertyId=2164; CustomProperty=DESCRICAO_DETALHADA
  - CustomPropertyId=2381; CustomProperty=OBS10
  - CustomPropertyId=1539; CustomProperty=OBS4
  - CustomPropertyId=2447; CustomProperty=INFORMACAO_FATURAMENTO
  - CustomPropertyId=1538; CustomProperty=OBS3
  - CustomPropertyId=946; CustomProperty=NN_CONDICAO_PAGAMENTO
  - CustomPropertyId=1540; CustomProperty=OBS5
  - CustomPropertyId=2583; CustomProperty=OBS23
  - CustomPropertyId=2348; CustomProperty=LISTA_ITENS_PESQ_MERC
  - CustomPropertyId=1400; CustomProperty=CSC_VALOR1_A
  - CustomPropertyId=1537; CustomProperty=OBS2
  - CustomPropertyId=2466; CustomProperty=QUANTIDADE_ESTIMADA
  - CustomPropertyId=2355; CustomProperty=POSSUI_DGCO
  - CustomPropertyId=2841; CustomProperty=QTD_PESQUISA
  - CustomPropertyId=2831; CustomProperty=PESQUISA_MERCADO4
  - CustomPropertyId=5073; CustomProperty=PESQUISA_MERCADO_5
  - CustomPropertyId=2839; CustomProperty=FORNECEDOR5
  - CustomPropertyId=2855; CustomProperty=FORNECEDOR6
  - CustomPropertyId=2856; CustomProperty=PESQUISA_MERCADO6
  - CustomPropertyId=2476; CustomProperty=PB_OBJETO_CONTRATACAO
  - CustomPropertyId=2581; CustomProperty=OBS21
  - CustomPropertyId=2582; CustomProperty=OBS22
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2412; ClasseConfiguracao=Solicitação atendida
- Relatorios:
  - FormatoExportacao=PDF
- Associação: FraseAssociacao=Projeto Básico Eletrônico -> Pesquisa de Mercado; FraseInversaAssociacao=Pesquisa de Mercado -> Projeto Básico Eletrônico; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=PBEPESQUISA; SeparadorSequencial=. | fonte: Projeto Básico Simplificado Eletrônico PBEE → alvo: Pesquisa de Mercado

### [366305] EventoFinal "Cancelado"
Config: TipoFinalizacao=NaoRealizado
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Cancelado"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        pass
        #log("Falha ao obter comprador_padrao: " + str(ex))

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```

### [366306] EventoFinal "Cancelado"
Config: TipoFinalizacao=NaoRealizado
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Cancelado"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        log("Falha ao obter comprador_padrao: " + str(ex))

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```

### [366307] Tarefa "Preencher dados para pesquisa de mercado"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico["SERV_ART_29_LEI_13303"] = "Sim"
OrdemServico["OBS1"] = OrdemServico.ObtemMotivoGateway('PESQCOMPLEMENTAR')


import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Preencher dados para pesquisa de mercado'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Preencher dados para pesquisa de mercado'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais para a Pesquisa de Mercado
  - LABEL12 "Exemplos: material administrativo, licenças de software, mobiliário, equipamentos de uso geral." [Label String(700) → CPE_PDCI2019.LABEL12]
  - LABEL10 "OBJETO COMPLEXO: Produtos ou serviços com especificações e aplicações definidas para uso exclusivo da BBTS, ou seja, itens que são personalizados e exigem maior detalhamento técnico." [Label String(700) → CPE_PDCI2019.LABEL10]
  - LABEL56 "II - para outros serviços e compras de valor até R$ 50.000,00 (cinquenta mil reais) e para alienações, nos casos previstos nesta Lei, desde que não se refiram a parcelas de um mesmo serviço, compra ou alienação de maior vulto que possa ser realizado de uma só vez;" [Label String(500) → CPE_CSC.LABEL56]
  - LABEL11 " Exemplos: serviços especializados, serviços com dedicação de mão de obra, softwares customizados, peças de equipamentos de automação bancária." [Label String(700) → CPE_PDCI2019.LABEL11]
  - OBS1 "Se pesquisa de mercado complementar: informar quais pendências para finalizar cotação (ex. falta 1 proposta, falta item, necessita de ajustes, etç)." [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - LISTA_ITENS_PESQ_MERC "Lista de itens - Tipo de Objeto:" [DropDownList String → CPE_CSC.LISTA_ITENS_PESQ_MERC]
**LISTA_ITENS_PESQ_MERC.ScriptModificado**
```python
#if Formulario['LISTA_ITENS_PESQ_MERC'].Valor == "Outros (especificar detalhadamente)":
#    Formulario['DESCRICAO_OBRIG'].Visivel = True
#    Formulario['DESCRICAO_OBRIG'].Habilitado = True
#
#    
#    
#if Formulario['LISTA_ITENS_PESQ_MERC'].Valor != "Outros (especificar detalhadamente)":
#    Formulario['DESCRICAO_OBRIG'].Visivel = False  
#    Formulario['DESCRICAO_OBRIG'].Habilitado = False
#
#    
#
#if Formulario['LISTA_ITENS_PESQ_MERC'].Valor == "Aluguel":
#    Formulario['CSC_VALOR1_A'].Visivel = True
#    Formulario['CSC_VALOR1_A'].Habilitado = True
#
#    
#    
#if Formulario['LISTA_ITENS_PESQ_MERC'].Valor != "Aluguel":
#    Formulario['CSC_VALOR1_A'].Visivel = False  
#    Formulario['CSC_VALOR1_A'].Habilitado = False
#    
#    
#    
#if Formulario['LISTA_ITENS_PESQ_MERC'].Valor == "Ata de Registro de Preço":
#    Formulario['OBS2'].Visivel = True
#    Formulario['OBS2'].Habilitado = True
#
#    
#    
#if Formulario['LISTA_ITENS_PESQ_MERC'].Valor != "Ata de Registro de Preço":
#    Formulario['OBS2'].Visivel = False  
#    Formulario['OBS2'].Habilitado = False
```
  - DESCRICAO_OBRIG "Se Outros, especificar o tipo de objeto detalhadamente:" [TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG]
  - SERV_ART_29_LEI_13303 "Serviços do art. 29, Incisos I e II, da Lei 13.303/2016?" [DropDownList String → CPE_CSC.SERV_ART_29_LEI_13303]
  - LABEL57 "Art. 29. É dispensável a realização de licitação por empresas públicas e sociedades de economia mista:" [Label String(1500) → CPE_CSC.LABEL57]
  - LABEL13 " OBJETO SIMPLES: Produtos ou serviços comuns, cujas especificações são definidas pelo fabricante ou fornecedor, também conhecidos como itens de prateleira." [Label String(700) → CPE_PDCI2019.LABEL13]
  - LABEL55 "I - para obras e serviços de engenharia de valor até R$ 100.000,00 (cem mil reais), desde que não se refiram a parcelas de uma mesma obra ou serviço ou ainda a obras e serviços de mesma natureza e no mesmo local que possam ser realizadas conjunta e concomitantemente;" [Label String(500) → CPE_CSC.LABEL55]
- Operação PR0001 Preencher Campos
  - CODIGO_ITEM "Código do Item" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=500
    - coluna ITEM
    - coluna NECESSIDADE obrigatório
    - coluna ITEM_OBSOLETO obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366308] EventoIntermediarioMensagem "Aviso sobre cancelamento de Ordem de Serviço"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento2 = OrdemServico.ObtemMotivoGateway("SERAFEITOREM")

if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Chamado cancelado"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Gerente Posição"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    pass
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366309] EventoIntermediarioTimer ""
Config: TempoIntervalo=720

### [366310] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200; MaximoExecucao=1

### [366249] Tarefa "Verificar Reprovação
 Cliente"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Verificar Reprovação Cliente'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Verificar Reprovação Cliente'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptValidacao**
```python
#--- Validação de subcampos conforme marcação

uor = OrdemServico.GetCustom("UOR")
gerex = OrdemServico.GetCustom('PPGEREX_NEGOCIO')

if OrdemServico.GetCustom("SIM_NAO7") == 'Sim':
    if String.IsNullOrEmpty(gerex):
        Criticas.AdicionaPendencia("Informe o(a) Gerente Executivo(a) que efetuará a aprovação.")
         
if OrdemServico.GetCustom("TIPO_DE_VALOR_DE_REFERENCIA") == 'Outros:':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('JUSTIFICATIVA_IMPACTO')): 
        Criticas.AdicionaPendencia("Preencha o campo 'Informe detalhadamente o método estatístico utilizado (Valor Referencial)'.")
         
if OrdemServico.GetCustom("SIM_NAO1") == 'Não':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('OBS6')):
        Criticas.AdicionaPendencia("Preencha o campo 'JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002'.")
```
**ScriptFormCarregado**
```python
Formulario["OBS5"].Habilitado = False

Formulario["SIM_NAO1"].Visivel = True
Formulario["SIM_NAO1"].Habilitado = True

Formulario["UOR"].Visivel = True
Formulario["UOR"].Habilitado = True

Formulario["PB_OBJETO_CONTRATACAO"].Visivel = True
Formulario["PB_OBJETO_CONTRATACAO"].Habilitado = True

Formulario["PARECER_QUALIF"].Visivel = True
Formulario["PARECER_QUALIF"].Habilitado = True

Formulario["QTD_PESQUISA"].Itens = "1;2;3;4;5;6"

OrdemServico.Salva()
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Pesquisa de Mercado Prévia" classes: Pesquisa de Mercado — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS INEXIGIBILIDADE1
  - anexo "Demais Documentos" classes: Anexo — RequeridoInicial=true
  - anexo "Comprovante de exclusividade" classes: Comprovante de exclusividade — RequeridoInicial=true
  - anexo "Carta de Exclusividade" classes: Carta de Exclusividade — RequeridoInicial=true
  - anexo "Comprovação de razoabilidade de preço" classes: Comprovação de razoabilidade de preço — RequeridoInicial=true
  - anexo "Remanejamento Orçamentário" classes: Remanejamento Orçamentário — RequeridoInicial=true
  - anexo "Parecer Jurídico Específico" classes: Parecer Jurídico Específico — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Anexo I -  Espeficiações Técnicas
  - OBS23 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS23]
  - OBS50 "9. Privacidade , Proteção e Tratamento de Dados Pessoais" [Memo String(2000) → CPE_CONTRATOS.OBS50] obrigatório
  - OBS21 "2. Especificações Técnicas" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - NN_CONDICAO_PAGAMENTO "7. Condições de Pagamento:" [Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO] obrigatório
  - OBS5 "8. Multa" [Memo String(2000) → CPE_CONTRATOS.OBS5] obrigatório
  - LABEL1 "ATENÇÃO: O campo "2. Especificações Técnicas" tem o limite de 4000 caracteres. Caso o limite de caracteres não seja o suficiente, utilize os campos abaixo para complementar a informação." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - OBS22 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS22]
  - OBS10 "3. Qualificação Técnica" [Memo String(2000) → CPE_CSC.OBS10] obrigatório
  - OBS4 "4. Condições de Entrega" [Memo String(2000) → CPE_CONTRATOS.OBS4] obrigatório
  - OBS7 "Condições de Entrega - Continuação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS7]
  - INFORMACAO_FATURAMENTO "5. Informações para Faturamento: (Incluir os dados da BBTS para o qual será faturado o objeto da contratação)" [DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; PosicaoRotulo=Topo
    - coluna ENDERECO_COM_CEP obrigatório
    - coluna ENDERECO obrigatório
    - coluna CNPJ_BBTS
    - coluna INSCRICAO_ESTADUAL
    - coluna INSCRICAO_MUNICIIPAL
  - OBS3 "6. Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico:" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=DEMAISDOCAJUSTE1
  - anexo "" classes: Comprovação de razoabilidade de preço — RequeridoInicial=true
  - anexo "" classes: CND FGTS — RequeridoInicial=true
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Parecer Jurídico Específico — RequeridoInicial=true
  - anexo "" classes: Comprovante de exclusividade — RequeridoInicial=true
  - anexo "" classes: Rateio Localidades — RequeridoInicial=true
  - anexo "" classes: QSA - Quadro de Sócios e Administradores — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true
  - anexo "" classes: Apólice de Seguro – Serviço de Transporte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Nota Técnica — RequeridoInicial=true
  - anexo "" classes: Certidão CNJ — RequeridoInicial=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true
  - anexo "" classes: CND Federal — RequeridoInicial=true
  - anexo "Demais Documentos (conforme TAB 415-001)" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Projeto Básico
  - SIM_NAO "É contratação de Tic? " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
#if Formulario['SIM_NAO'].Valor == "Sim":
#   Formulario['SIM_NAO5'].Habilitado = True
#   Formulario['SIM_NAO5'].Visivel = True

#if Formulario['SIM_NAO'].Valor != "Sim":
#    Formulario['SIM_NAO5'].Habilitado = False
#    Formulario['SIM_NAO5'].Visivel = False
```
  - PESQUISA_MERCADO4 "PESQUISA_MERCADO4" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO4.PESQUISA_MERCADO4]
**PESQUISA_MERCADO4.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO4.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM
    - coluna FORNECEDOR obrigatório
    - coluna VALOR obrigatório
    - coluna UDM
    - coluna DESCRICAO_ITEM
    - coluna QUANTIDADE obrigatório
    - coluna ITEM1 obrigatório
    - coluna VALOR_UNITARIO obrigatório
  - FORNECEDOR5 "Fornecedor 5" [TextBox String → CPE_CSC.FORNECEDOR5]
  - PESQUISA_MERCADO_5 "PESQUISA_MERCADO5" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO_5.PESQUISA_MERCADO_5]
**PESQUISA_MERCADO_5.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna ITEM
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO_5.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna DESCRICAO_ITEM
    - coluna VALOR obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO_5.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna UDM obrigatório
    - coluna QUANTIDADE obrigatório
  - FORNECEDOR6 "Fornecedor 6" [TextBox String → CPE_CSC.FORNECEDOR6]
  - PESQUISA_MERCADO6 "PESQUISA DE MERCADO 6" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO6.PESQUISA_MERCADO6]
**PESQUISA_MERCADO6.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO6.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''

contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0

    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO6.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna QUANTIDADE obrigatório
    - coluna UDM obrigatório
    - coluna ITEM1 obrigatório
    - coluna ITEM
    - coluna DESCRICAO_ITEM
    - coluna VALOR obrigatório
    - coluna VALOR_UNITARIO obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna VALOR_TOTAL
    - coluna VALOR_REFERENCIAL obrigatório
**VALOR_REFERENCIAL.VALOR_REFERENCIAL.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna ITEM
  - PESQUISA_MERCADO1 "PESQUISA_MERCADO1" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO1.PESQUISA_MERCADO1] obrigatório
**PESQUISA_MERCADO1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna DESCRICAO_ITEM
**PESQUISA_MERCADO1.DESCRICAO_ITEM.ScriptModificado**
```python
#FormularioRegistro["ITEM"].Visivel = True
#FormularioRegistro["ITEM"].Habilitado = True
#dt = OrdemServico.GetCustom("CODIGO_ITEM")
#itensCODIGO=''
#
#
#contCODIGO=0
#
##if (itensCNPJ.Rows.Count==0):
#for dr in dt.Rows:
#    igualCODIGO=0
#    regdr2=0
#    
#    #for dr2 in dt.Rows:
#    #    if (dr["ITEM"]== dr2["ITEM"]):
#    #        if (regdr<=regdr2 and igualCODIGO==0):
#    #            igualCODIGO=0
#    #        else:
#    #            igualCODIGO=1
#        
#    #if (igualCODIGO<=0):
#    if (contCODIGO==0):
#        itensCODIGO=dr["ITEM"]
#        contCODIGO=1
#    else:
#        itensCODIGO = itensCODIGO+';'+dr["ITEM"]
#
##regdr=regdr+1
#FormularioRegistro["ITEM"].Itens = itensCODIGO
#
```
    - coluna VALOR
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO1.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO
    - coluna FORNECEDOR
    - coluna ITEM
**PESQUISA_MERCADO1.ITEM.ScriptModificado**
```python
#dt = OrdemServico.GetCustom("CODIGO_ITEM")
#
#itensCODIGO = ''
#cont=0
#
#for dr in dt.Rows:
#    if (FormularioRegistro["ITEM"].Valor == dr["CODIGO_ITEM"]):
#        if (cont==0):
#            itensCODIGO=dr["ITEM"]
#        else:
#            itensCNPJ = itensCODIGO+';'+dr["ITEM"]
#
#        cont=1
#FormularioRegistro["ITEM"].Itens = itensCODIGO
#
```
    - coluna QUANTIDADE
    - coluna PESQUISA1
**PESQUISA_MERCADO1.PESQUISA1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna ITEM1 obrigatório
  - FORNECEDOR2 "Fornecedor 2" [TextBox String → CPE_CSC.FORNECEDOR2]
  - FORNECEDOR4 "Fornecedor 4" [TextBox String → CPE_CSC.FORNECEDOR4]
  - PESQUISA_MERCADO2 "PESQUISA_MERCADO2" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO2.PESQUISA_MERCADO2]
**PESQUISA_MERCADO2.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna VALOR obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO2.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna ITEM
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
  - FORNECEDOR3 "Fornecedor 3" [TextBox String → CPE_CSC.FORNECEDOR3]
  - PESQUISA_MERCADO3 "PESQUISA_MERCADO3" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO3.PESQUISA_MERCADO3]
**PESQUISA_MERCADO3.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna FORNECEDOR obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO3.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0


for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
    - coluna ITEM
    - coluna ITEM1 obrigatório
  - PB_OBJETO_CONTRATACAO "1. Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna PATRIMONIO obrigatório
    - coluna NOTA_FISCAL obrigatório
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna CODIGO obrigatório
    - coluna ITEM
    - coluna PROD_PRODUTO obrigatório
    - coluna ITEM_OBSOLETO obrigatório
    - coluna PROD_DATA_REC obrigatório
    - coluna NECESSIDADE obrigatório
    - coluna PROD_NCM
  - QTD_PESQUISA "Quantidade de Pesquisas" [DropDownList String → CPE_CSC.QTD_PESQUISA] obrigatório
**QTD_PESQUISA.ScriptModificado**
```python
if Formulario["QTD_PESQUISA"].Valor == "6":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = True
    Formulario["FORNECEDOR6"].Habilitado = True
    Formulario["PESQUISA_MERCADO6"].Visivel = True
    Formulario["PESQUISA_MERCADO6"].Habilitado = True


if Formulario["QTD_PESQUISA"].Valor == "5":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "4":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False

if Formulario["QTD_PESQUISA"].Valor == "3":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "2":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "1":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = False
    Formulario["FORNECEDOR2"].Habilitado = False
    Formulario["PESQUISA_MERCADO2"].Visivel = False
    Formulario["PESQUISA_MERCADO2"].Habilitado = False
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = False
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
```
  - FORNECEDOR01 "Fornecedor 1" [TextBox String → CPE_CSC.FORNECEDOR01] obrigatório
  - TIPO_ATIVIDADE "Classificação da Atividade" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
   Formulario['LABEL6'].Habilitado = True
   Formulario['LABEL6'].Visivel = True
   

if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
    Formulario['LABEL6'].Habilitado = False
    Formulario['LABEL6'].Visivel = False
```
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica"." [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]
  - LABEL6 "(Preencher se for contrato com FORNECEDOR para ATIVIDADE FIM) Citar todos os contratos de clientes no qual o serviço a ser contratado detém uma vinculação direta e indireta." [Label String(1500) → CPE_PDCI2019.LABEL6]
  - SIM_NAO5 "Aplica-se os artefatos da NI642?" [DropDownList String → CPE_CSC.SIM_NAO5]
  - VALOR "DOTAÇÃO ORÇAMENTÁRIA (VALOR GLOBAL OU VALOR GLOBAL ESTIMADO): R$ " [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - VALOR_DOD "Preço Global Referencial: R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]
  - COMBOBOX10 "Natureza Contábil" [DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10] obrigatório
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX

if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - DIRETORIA_GERENCIA "Área Técnica (quando couber)" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
  - LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Pareceres
  - UOR "UOR(s) de alocação de Despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório
    - coluna UOR obrigatório
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - CONTA_CONTABIL1 "Conta Contábil (Parecer Contabilidade)" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - PARECER_QUALIF "Parecer Controladoria" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais da Pesquisa de Mercado
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184 Mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar ''Não se aplica''." [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
  - JUSTIFICATIVA_IMPACTO "Justificativa 1 (Metodologia aplicada em caso de valor referencial escolhido "Outros")" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. " [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79 mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
#if Formulario['SIM_NAO1'].Valor == "Não":
#   Formulario['OBS6'].Habilitado = True
#   Formulario['OBS6'].Visivel = True
   
#if Formulario['SIM_NAO1'].Valor != "Sim":
#   Formulario['OBS6'].Habilitado = False
#   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo Complementar as Especificações Técnicas" classes: Especificação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - SIM_NAO7 "Solicitar aprovação do Gerente Executivo?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
  - LABEL150 "<b style="color:red">Somente avance para a etapa seguinte caso o usuário seja Solucionador ou Gerente Cesec.</b>" [Label String(1500) → CPE_PDCI2019.LABEL150] obrigatório
  - FAVORECIDO_TODOS_2 "Assessor/Analista que assinará como elaborador(a) do Projeto Básico" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_2] obrigatório
  - APROVADOR_PB "Aprovadores da contratação conforme NI006 (Somente Funções Gerenciais)" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório
    - coluna APROVADORES obrigatório
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO]
- Relatorios:
  - FormatoExportacao=PDF

### [366250] EventoIntermediarioMensagem "Aviso de cancelamento por reprovação gerencial"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Aviso de reprovação de chamados"  # ajuste conforme a etapa do seu evento


idCliente = 0
nomeCliente = ''

try:
    idCliente = OrdemServico.Cliente.Id.ToString()
    dt = Utils.ExecuteDataTable("SELECT P.NOME FROM PESSOA P INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA WHERE CP.ID_PESSOA = '" + idResp + "'")
    nomeCliente = None
    for r in dt.Rows:
        nomeCliente = r["NOME"]
        break
except:
    nomeCliente = None

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = nomeCliente  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366251] Tarefa "Solicitar aprovação do Cliente"
Responsável: Responsável atual (papel 36)
Config: Codigo=APROVAÇÃOCLIENTE; PermiteCancelamentoAA=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()



etapa = 'Solicitar aprovação do Cliente'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
    else:
        #Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
finally:
    client.Dispose()


OrdemServico.Salva()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Solicitar aprovação do Cliente'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Projeto Básico; ReenvioEmailAprovacao=12
  - item para aprovação ""
  - item para aprovação ""
  - aprovador: Favorecido Todos 2 (Unico)
  - relatório: FormatoExportacao=PDF; RotuloLink=Para acessar o PROJETO BÁSICO preenchido, CLIQUE AQUI.
- Relatorios:
  - FormatoExportacao=PDF

### [366252] EventoIntermediarioMensagem "PBe - Conta Contábil"
Config: ListaDestinatarios=contabilidade@bbts.com.br
ModeloComunicado: PBe - Conta Contábil
Corpo do comunicado: Prezados(as),
Aguardamos a informação da conta contábil para prosseguir com a confecção do projeto básico solicitado na Ordem de Serviço nº OrdemServico.Numero .
Segue o objeto da contratação:
 OrdemServico.Customizado.PB_OBJETO_CONTRATACAO 
Para maiores informações Link.Edicao .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Informar Conta Contábil"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "contabilidade@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366253] FimCancelamento "Cancelamento por reprovação"
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Cancelado"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        log("Falha ao obter comprador_padrao: " + str(ex))

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```

### [366311] EventoIntermediarioMensagem "Aviso de cancelamento de chamado por falta de resposta de cliente para complemento do PBe"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Reprovação por falta de ajustes
Corpo do comunicado: Prezado(a),
A Ordem de Serviço OrdemServico.Numero foi cancelado automaticamente por falta de ajustes.
Para realizar este serviço abra uma nova solicitação.
Para maiores informações Link.Consulta.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Reprovação por falta de ajustes"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Gerente Posição"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366312] SubProcesso "Remanejamento Orçamentário"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=1047; PermiteCancelamentoAA=true
MotivoInterrupcaoSLA: Aguardando Fim Subprocesso associado
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Remanejamento Orçamentário'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None

# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": 'Fila CSC',
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Remanejamento Orçamentário'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Associação: Ativo=true; FraseAssociacao=Projeto Básico --> Remanejamento Orçamentário; FraseInversaAssociacao=Remanejamento Orçamentário --> Projeto Básico; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=REMAPB; SeparadorSequencial=. | fonte: Projeto Básico → alvo: Remanejamento Orçamentário

### [366313] EventoIntermediarioMensagem "Cobrança de Ajustes"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Projeto Básico Reprovado - Ajustes
Corpo do comunicado: Prezado(a),
O projeto básico foi reprovado e necessita de ajustes.
Para ajustar o projeto básico, Link.Workspace .
Ajustes Necessários:
 Complemento1 
Dados do Projeto:
Objeto:
 OrdemServico.Customizado.PB_OBJETO_CONTRATACAO 
Itens da Contratação:
 OrdemServico.Customizado.CODIGO_ITEM 
Após ajustar as informações, clique em "Avançar" para submeter novamente para aprovação.
Qualquer dúvida, entre em contato com Cesec - Centro de Serviços Compartilhados.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROVAR_GEREX") or OrdemServico.ObtemMotivoReprovacao("APROVACAO_GERENTES")
 
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Verificar Reprovação Gerencial (Cliente)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Gerente Posição"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366314] EventoFinal "Cancelado"
Config: TipoFinalizacao=NaoRealizado
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Cancelada"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        log("Falha ao obter comprador_padrao: " + str(ex))

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```

### [366315] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório."
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico

#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR'].ToString()+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Tabela de Aprovações    
consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'

for dados in consultaAprovacoes.Rows:

    cargo = ''
    
    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
        cargo = dados['FUNCAO_GRATIFICADA']
    else:
        cargo = dados['CARGO']

    tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
    
OrdemServico["APROVACOES"] = tabelaAprovacoes.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')  

#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos









import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório.'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()




AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório.'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0001 Preencher Campos
  - LISTA_VALOR_REF_UNIT "Valor referencial do Projeto Basico" [Memo String(2000) → CPE_CSC.LISTA_VALOR_REF_UNIT]
  - TABELA_DADOS_CONTRATOS_C "Tabela de Dados Contratuais" [Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C]
  - APROVACOES "Campo para preenchimento das aprovações." [Memo String(2000) → CPE_CSC.APROVACOES]
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366316] Tarefa "Informar número da OS criada para Cadastro de Fornecedor"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Services.Custom import Query
num_associada = OrdemServico.ObtemAssociadasComoAlvo('PBECADFOR')
associadas = ''

if not len(num_associada) > 1:
    for i in num_associada:
        OrdemServico['CSC_LOGRADOURO'] += i.ToString().split(' - ')[0]
        
else:
    for i in num_associada:
        OrdemServico['CSC_LOGRADOURO'] += i.ToString().split(' - ')[0] + ', '

        
        
        
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Informar número da OS criada para Cadastro de Fornecedor'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
        
OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Informar número da OS criada para Cadastro de Fornecedor'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
#Formulario["CSC_CPF"].Visivel = True
#Formulario["CSC_CPF"].Habilitado = True

#num_associada = OrdemServico.ObtemAssociadasComoAlvo('PBECADFOR')
#associadas = ''
#
#if not len(num_associada) > 1:
#    for i in num_associada:
#        Formulario['CSC_CPF'].Valor += i.ToString().split(' - ')[0]
#        
#else:
#    for i in num_associada:
#        Formulario['CSC_CPF'].Valor += i.ToString().split(' - ')[0] + ', '
```
- Operação PR0001 Preencher Campos
  - CSC_LOGRADOURO "Número da OS subprocesso Cadastro de Fornecedor" [TextBox String(500) → CPE_CSC.CSC_LOGRADOURO]

### [366254] Tarefa "Solicitar aprovação conforme NI006"
Responsável: Responsável atual (papel 36)
Config: Codigo=APROVACAO_GERENTES
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
from Venki.Services.Custom import Query
#OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.Salva()





import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Solicitar aprovação conforme NI006'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Solicitar aprovação conforme NI006'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar projeto básico eletrônico simplificado; ReprovarImediato=true; ReenvioEmailAprovacao=24; ObrigatoriedadeMotivo=Todas
  - item para aprovação ""
  - item para aprovação ""
  - aprovador: Aprovadores Projeto Básico (Unico)
  - relatório: FormatoExportacao=PDF
- Relatorios:
  - FormatoExportacao=PDF

### [366255] Tarefa "Preencher informações para solicitações de parecer"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico["SIM_NAO3"] = "Sim"



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Preencher informações para solicitações de parecer'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Preencher informações para solicitações de parecer'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
#---------Replace

OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()
#
#Formulario["VALOR_REFERENCIAL"].Visivel = True
#Formulario["VALOR_REFERENCIAL"].Habilitado = True
#Formulario['CSC_ESCOLARIDADE'].Visivel = True
#Formulario['CSC_ESCOLARIDADE'].Habilitado = True
#Formulario['UOR'].Visivel = True
#Formulario['UOR'].Habilitado = True
#
#Formulario["SIM_NAO3"] = "Sim"
#
#OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Importante!
  - LABEL150 "<b style="color:red">Somente avance para a etapa seguinte caso o usuário seja Solucionador ou Gerente Cesec.</b>" [Label String(1500) → CPE_PDCI2019.LABEL150] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados para enviar para parecer
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica".)" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]
  - OBS24 "Ações tomadas do cliente sobre a reprovação da Gemac, se houver." [Memo String(2000) → CPE_CSC.OBS24]
  - SIM_NAO3 "Há orçamento para conta/UOR informada?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
  - UOR "UOR" [DataGrid RecordList → Z_00143_UOR.UOR]
    - coluna UOR obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL]
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna VALOR_TOTAL
    - coluna VALOR_REFERENCIAL obrigatório
    - coluna ITEM
  - CONTA_CONTABIL1 "Conta Contábil" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1]
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
- Relatorios:
  - FormatoExportacao=PDF

### [366256] EventoIntermediarioMensagem "Reiteração"
Config: ListaDestinatarios=cesec.comp@bbts.com.br;rony.baldoino@bbts.com.br
ModeloComunicado: Projeto Básico - Aprovação
Corpo do comunicado: Prezado(a) Cesec,
O projeto básico foi aprovado.
Acesse a ordem de serviço e unifique os documentos.
Para maiores informações, Link.Edicao .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = u"Unificar Projeto Básico"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "cesec.comp@bbts.com.br;rony.baldoino@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366317] Tarefa "Unificar Projeto Básico"
Referência: .
Prezado(a) Solucionador(a),
Se houver a aprovação "Aprovar utilização de Conta de Marketing" por gentileza excluir do documento unificado o(a) aprovador da GEMAC (Gerente de Divisão) da lista de aprovadores do PBe. A aprovação é exclusiva para a ultilização da rúbrica orçamentária de Marketing.
Se houver a aprovação "Aprovar utilização de rubrica da Gesap-Diage" por gentileza excluir do documento unificado o(a) aprovador da DIAGE (Gerente de Divisão) da lista de aprovadores do PBe. A aprovação é exclusiva para a ultilização da rúbrica orçamentária da Gestão de Estabelecimentos.
Se houver dua
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()

#OrdemServico["DESCRICAO_DETALHADA"].Visivel = False
#OrdemServico["DESCRICAO_DETALHADA"].Habilitado = False
#OrdemServico["FAVORECIDO_COBRA"].Visivel = False
#OrdemServico["FAVORECIDO_COBRA"].Habilitado = False
#OrdemServico["MODALIDADE_LICITACAO"].Visivel = False
#OrdemServico["MODALIDADE_LICITACAO"].Habilitado = False
#OrdemServico["NUMERO_OC"].Visivel = False
#OrdemServico["NUMERO_OC"].Habilitado = False
#OrdemServico["NUMERO_RC"].Visivel = False
#OrdemServico["NUMERO_RC"].Habilitado = False


OrdemServico.ModificaCampoFormularioVisivel('UOR', True)

import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Unificar Projeto Básico'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

OrdemServico.Salva()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Unificar Projeto Básico'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()

Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = True
Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True
Formulario['UOR'].Visivel = True
Formulario['UOR'].Habilitado = True
Formulario["SIM_NAO1"].Visivel = True
Formulario["SIM_NAO1"].Habilitado = True
Formulario["PARECER_QUALIF"].Visivel = True
Formulario["PARECER_QUALIF"].Habilitado = True

Formulario["DESCRICAO_DETALHADA"].Visivel = False
Formulario["DESCRICAO_DETALHADA"].Habilitado = False
Formulario["FAVORECIDO_COBRA"].Visivel = False
Formulario["FAVORECIDO_COBRA"].Habilitado = False
Formulario["MODALIDADE_LICITACAO"].Visivel = False
Formulario["MODALIDADE_LICITACAO"].Habilitado = False
Formulario["NUMERO_OC"].Visivel = False
Formulario["NUMERO_OC"].Habilitado = False
Formulario["NUMERO_RC"].Visivel = False
Formulario["NUMERO_RC"].Habilitado = False

Formulario["PB_OBJETO_CONTRATACAO"].Visivel = True
Formulario["PB_OBJETO_CONTRATACAO"].Habilitado = True

Formulario["QTD_PESQUISA"].Itens = "1;2;3;4;5;6"

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais da Pesquisa de Mercado
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. " [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar ''Não se aplica''." [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
#if Formulario['SIM_NAO1'].Valor == "Não":
#   Formulario['OBS6'].Habilitado = True
#   Formulario['OBS6'].Visivel = True
   
#if Formulario['SIM_NAO1'].Valor != "Sim":
#   Formulario['OBS6'].Habilitado = False
#   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184 Mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79 mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
  - JUSTIFICATIVA_IMPACTO "Justificativa 1 (Metodologia aplicada em caso de valor referencial escolhido "Outros")" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=UOR(s) de alocação de despesa/Custo
  - DESCRICAO_DETALHADA "Descrição da Solicitação" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - FAVORECIDO_COBRA "Solicitante" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - NUMERO_OC "Número da OC (Se houver)" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC]
  - MODALIDADE_LICITACAO "Modalidade de Contratação - Inserir Modalidade, Artigo e Inciso (Ex: Dispensa de Licitação, Art. 29, Inciso II, Lei 13.303/16) " [TextBox String → CP_ORDEM_SERVICO.MODALIDADE_LICITACAO] obrigatório
  - UOR "UOR(s) de alocação de despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório
    - coluna UOR obrigatório
  - NUMERO_RC "Número da RC (Se houver)" [TextBox String → CPE_CSC.NUMERO_RC]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Projeto Básico
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX

if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - DIRETORIA_GERENCIA "Área Técnica (quando couber)" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
  - LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] obrigatório
  - PB_OBJETO_CONTRATACAO "1. Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna PATRIMONIO obrigatório
    - coluna NOTA_FISCAL obrigatório
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna ITEM_OBSOLETO obrigatório
    - coluna PROD_DATA_REC obrigatório
    - coluna NECESSIDADE obrigatório
    - coluna PROD_PRODUTO obrigatório
    - coluna PROD_NCM
    - coluna CODIGO obrigatório
    - coluna ITEM
  - QTD_PESQUISA "Quantidade de Pesquisas" [DropDownList String → CPE_CSC.QTD_PESQUISA] obrigatório
**QTD_PESQUISA.ScriptModificado**
```python
if Formulario["QTD_PESQUISA"].Valor == "6":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = True
    Formulario["FORNECEDOR6"].Habilitado = True
    Formulario["PESQUISA_MERCADO6"].Visivel = True
    Formulario["PESQUISA_MERCADO6"].Habilitado = True


if Formulario["QTD_PESQUISA"].Valor == "5":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "4":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False

if Formulario["QTD_PESQUISA"].Valor == "3":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "2":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "1":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = False
    Formulario["FORNECEDOR2"].Habilitado = False
    Formulario["PESQUISA_MERCADO2"].Visivel = False
    Formulario["PESQUISA_MERCADO2"].Habilitado = False
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = False
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
```
  - FORNECEDOR01 "Fornecedor 1" [TextBox String → CPE_CSC.FORNECEDOR01] obrigatório
  - PESQUISA_MERCADO1 "PESQUISA_MERCADO1" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO1.PESQUISA_MERCADO1] obrigatório
**PESQUISA_MERCADO1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna DESCRICAO_ITEM
    - coluna PESQUISA1
**PESQUISA_MERCADO1.PESQUISA1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna QUANTIDADE
    - coluna ITEM1 obrigatório
    - coluna VALOR
    - coluna FORNECEDOR
    - coluna VALOR_UNITARIO
    - coluna ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO1.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
  - FORNECEDOR2 "Fornecedor 2" [TextBox String → CPE_CSC.FORNECEDOR2]
  - VALOR "DOTAÇÃO ORÇAMENTÁRIA (VALOR GLOBAL OU VALOR GLOBAL ESTIMADO): R$ " [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - VALOR_DOD "Preço Global Referencial: R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]
  - FORNECEDOR4 "Fornecedor 4" [TextBox String → CPE_CSC.FORNECEDOR4]
  - COMBOBOX10 "Natureza Contábil" [DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10] obrigatório
  - PESQUISA_MERCADO2 "PESQUISA_MERCADO2" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO2.PESQUISA_MERCADO2]
**PESQUISA_MERCADO2.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna DESCRICAO_ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO2.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna VALOR obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
  - FORNECEDOR3 "Fornecedor 3" [TextBox String → CPE_CSC.FORNECEDOR3]
  - PESQUISA_MERCADO3 "PESQUISA_MERCADO3" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO3.PESQUISA_MERCADO3]
**PESQUISA_MERCADO3.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna DESCRICAO_ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO3.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna ITEM1 obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
    - coluna ITEM
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna VALOR_REFERENCIAL obrigatório
**VALOR_REFERENCIAL.VALOR_REFERENCIAL.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_TOTAL
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna ITEM
  - FORNECEDOR5 "Fornecedor 5" [TextBox String → CPE_CSC.FORNECEDOR5]
  - PESQUISA_MERCADO_5 "PESQUISA_MERCADO5" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO_5.PESQUISA_MERCADO_5]
**PESQUISA_MERCADO_5.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna ITEM
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO_5.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna DESCRICAO_ITEM
    - coluna UDM obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna VALOR obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO_5.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
  - FORNECEDOR6 "Fornecedor 6" [TextBox String → CPE_CSC.FORNECEDOR6]
  - PESQUISA_MERCADO6 "PESQUISA DE MERCADO 6" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO6.PESQUISA_MERCADO6]
**PESQUISA_MERCADO6.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO6.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna ITEM
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna VALOR obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO6.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna QUANTIDADE obrigatório
  - TIPO_ATIVIDADE "Classificação da Atividade" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
   Formulario['LABEL6'].Habilitado = True
   Formulario['LABEL6'].Visivel = True
   

if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
    Formulario['LABEL6'].Habilitado = False
    Formulario['LABEL6'].Visivel = False
```
  - LABEL6 "(Preencher se for contrato com FORNECEDOR para ATIVIDADE FIM) Citar todos os contratos de clientes no qual o serviço a ser contratado detém uma vinculação direta e indireta." [Label String(1500) → CPE_PDCI2019.LABEL6]
  - SIM_NAO "É contratação de Tic? " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
#if Formulario['SIM_NAO'].Valor == "Sim":
#   Formulario['SIM_NAO5'].Habilitado = True
#   Formulario['SIM_NAO5'].Visivel = True

#if Formulario['SIM_NAO'].Valor != "Sim":
#    Formulario['SIM_NAO5'].Habilitado = False
#    Formulario['SIM_NAO5'].Visivel = False
```
  - SIM_NAO5 "Aplica-se os artefatos da NI642?" [DropDownList String → CPE_CSC.SIM_NAO5]
  - PESQUISA_MERCADO4 "PESQUISA_MERCADO4" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO4.PESQUISA_MERCADO4]
**PESQUISA_MERCADO4.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO4.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM
    - coluna DESCRICAO_ITEM
    - coluna VALOR_UNITARIO obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
    - coluna VALOR obrigatório
    - coluna ITEM1 obrigatório
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica"." [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Pesquisa de Mercado — RequeridoInicial=true
  - anexo "Itens para unificação" classes: Especificação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Projeto Básico — ProduzidoTermino=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Anexo I -  Espeficiações Técnicas
  - OBS21 "2. Especificações Técnicas" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - LABEL1 "ATENÇÃO: O campo "2. Especificações Técnicas" tem o limite de 4000 caracteres. Caso o limite de caracteres não seja o suficiente, utilize os campos abaixo para complementar a informação." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - OBS22 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS22]
  - OBS23 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS23]
  - OBS10 "3. Qualificação Técnica" [Memo String(2000) → CPE_CSC.OBS10] obrigatório
  - OBS4 "4. Condições de Entrega" [Memo String(2000) → CPE_CONTRATOS.OBS4] obrigatório
  - OBS7 "Condições de Entrega - Continuação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS7]
  - INFORMACAO_FATURAMENTO "5. Informações para Faturamento: (Incluir os dados da BBTS para o qual será faturado o objeto da contratação)" [DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; PosicaoRotulo=Topo
    - coluna INSCRICAO_MUNICIIPAL
    - coluna ENDERECO_COM_CEP obrigatório
    - coluna ENDERECO obrigatório
    - coluna CNPJ_BBTS
    - coluna INSCRICAO_ESTADUAL
  - OBS3 "6. Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico:" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - NN_CONDICAO_PAGAMENTO "7. Condições de Pagamento:" [Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO] obrigatório
  - OBS5 "8. Multa" [Memo String(2000) → CPE_CONTRATOS.OBS5] obrigatório
  - OBS50 "9. Privacidade , Proteção e Tratamento de Dados Pessoais" [Memo String(2000) → CPE_CONTRATOS.OBS50] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=DEMAISDOCAJUSTE2
  - anexo "" classes: Parecer Jurídico Específico — RequeridoInicial=true
  - anexo "" classes: Certidão CNJ — RequeridoInicial=true
  - anexo "" classes: CND Federal — RequeridoInicial=true
  - anexo "" classes: Apólice de Seguro – Serviço de Transporte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: CND FGTS — RequeridoInicial=true
  - anexo "" classes: Comprovante de exclusividade — RequeridoInicial=true
  - anexo "" classes: Justificativa — RequeridoInicial=true
  - anexo "" classes: Nota Técnica — RequeridoInicial=true
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: QSA - Quadro de Sócios e Administradores — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Rateio Localidades — RequeridoInicial=true
  - anexo "" classes: Comprovação de razoabilidade de preço — RequeridoInicial=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true
  - anexo "Demais Documentos (conforme TAB 415-001)" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Pareceres
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - CONTA_CONTABIL1 "Conta Contábil (Parecer Contabilidade)" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - PARECER_QUALIF "Parecer Controladoria" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366257] Tarefa "Preencher dados para confecção de OC"
Referência: Se necessário, clique em "Voltar" para etapa de "Unificar Projeto Básico" para efetuar ajustes ou em "Avançar" para direcionamentos internos.
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico['FAVORECIDO_COBRA'] = OrdemServico.ClienteId



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Preencher dados para confecção de OC'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


OrdemServico.Salva()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Preencher dados para confecção de OC'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
#Formulario['LABEL10'].Visivel = True
#Formulario['LABEL11'].Visivel = True
#Formulario['LABEL2'].Visivel = True
Formulario['UOR'].Visivel = True

Formulario["DESCRICAO_DETALHADA"].Visivel = True
Formulario["DESCRICAO_DETALHADA"].Habilitado = True
Formulario["FAVORECIDO_COBRA"].Visivel = True
Formulario["FAVORECIDO_COBRA"].Habilitado = True
Formulario["MODALIDADE_LICITACAO"].Visivel = True
Formulario["MODALIDADE_LICITACAO"].Habilitado = True
Formulario["NUMERO_OC"].Visivel = True
Formulario["NUMERO_OC"].Habilitado = True
Formulario["NUMERO_RC"].Visivel = True
Formulario["NUMERO_RC"].Habilitado = True
Formulario['DESCRICAO_DETALHADA'].Valor = OrdemServico['PB_OBJETO_CONTRATACAO']
Formulario['MODALIDADE_LICITACAO'].Valor = 'Dispensa de Licitação, Art. 29, Inciso II, Lei 13.303/16'
```
- Operação PR0004 Associar Itens Configuração: Nome=DOCS5
  - anexo "Anexo Complementar as Especificações Técnicas" classes: Especificação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Pesquisa de Mercado" classes: Pesquisa de Mercado — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "FQ415-075" classes: FQ415-075 - DADOS BÁSICOS PARA CRIAÇÃO DE REQUISIÇÃO DE COMPRAS — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=DEMAISDOCAJUSTE5
  - anexo "" classes: QSA - Quadro de Sócios e Administradores — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Justificativa — RequeridoInicial=true
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Rateio Localidades — RequeridoInicial=true
  - anexo "" classes: Apólice de Seguro – Serviço de Transporte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Parecer Jurídico Específico — RequeridoInicial=true
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true
  - anexo "Demais Documentos (conforme TAB 415-001)" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Comprovante de exclusividade — RequeridoInicial=true
  - anexo "" classes: Certidão CNJ — RequeridoInicial=true
  - anexo "" classes: CND FGTS — RequeridoInicial=true
  - anexo "" classes: Nota Técnica — RequeridoInicial=true
  - anexo "" classes: Comprovação de razoabilidade de preço — RequeridoInicial=true
  - anexo "" classes: CND Federal — RequeridoInicial=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Técnica" classes: Nota Técnica — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - NUMERO_OC "Número da OC (Se houver)" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC]
  - NUMERO_RC "Número da RC (Se houver)" [TextBox String → CPE_CSC.NUMERO_RC]
  - DESCRICAO_DETALHADA "Descrição da Solicitação" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - MODALIDADE_LICITACAO "Modalidade de Contratação - Inserir Modalidade, Artigo e Inciso (Ex: Dispensa de Licitação, Art. 29, Inciso II, Lei 13.303/16) " [TextBox String → CP_ORDEM_SERVICO.MODALIDADE_LICITACAO] obrigatório
  - UOR "UOR(s) de alocação de Despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório
    - coluna UOR obrigatório
  - FAVORECIDO_TODOS_03 "Solucionador responável pelo PBe" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_03] obrigatório
  - FAVORECIDO_COBRA "Solicitante" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Projeto Básico — RequeridoInicial=true
- Relatorios:
  - FormatoExportacao=PDF

### [366258] EventoIntermediarioMensagem "Aviso de aprovação ao Gestor"
Destinatário: Gerente Divisão Gesap (papel 1359)
Config: ListaDestinatarios=marcus.pereira@bbts.com.br
ModeloComunicado: Aviso para aprovação
Corpo do comunicado: Prezado(a),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto segue para sua aprovação.
Para mais detalhes sobre esta solicitação : Link.Consulta .
Atenciosamente
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Aguardar aprovação Gesap-Diage"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "marcus.pereira@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366259] EventoIntermediarioMensagem "Aviso de utilização de Conta Contábil e UOR referente a Marketing"
Config: ListaDestinatarios=comunicacao@bbts.com.br
ModeloComunicado: Aviso sobre Abertura de Chamado
Corpo do comunicado: Prezados(as),
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada:
OrdemServico.DescricaoDetalhada 
 OrdemServico.Customizado.DESCRICAO_OBRIG 
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Aguardar aprovação Gemac"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "comunicacao@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366318] Tarefa "Retorno de devolução ao cliente para nova solicitação de parecer (CESEC)
"
Referência: Caro(a) Solucionador(a), favor verificar o motivo da devolução ao cliente e confirmar se as pendências foram resolvidas para que uma nova solicitação de parecer possa ser emitida. Caso o Parecer Contábil permaneça o mesmo, pule a próxima etapa e avance diretamente para a fase de Controladoria.
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Retorno de devolução ao cliente para nova solicitação de parecer'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Retorno de devolução ao cliente para nova solicitação de parecer'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
#---------Replace

OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()

Formulario["VALOR_REFERENCIAL"].Visivel = True
Formulario["VALOR_REFERENCIAL"].Habilitado = True
Formulario['CSC_ESCOLARIDADE'].Visivel = True
Formulario['CSC_ESCOLARIDADE'].Habilitado = True
Formulario['UOR'].Visivel = True
Formulario['UOR'].Habilitado = True
Formulario['CONTA_CONTABIL1'].Visivel = True
Formulario['CONTA_CONTABIL1'].Habilitado = True
Formulario['PARECER_QUALIF'].Visivel = True
Formulario['PARECER_QUALIF'].Habilitado = True
Formulario['CONTA_ORCAMENTARIA'].Visivel = True
Formulario['CONTA_ORCAMENTARIA'].Habilitado = True
Formulario['CODIGO_ITEM'].Visivel = True
Formulario['CODIGO_ITEM'].Habilitado = True


OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Importante!
  - LABEL150 "<b style="color:red">Somente avance para a etapa seguinte caso o usuário seja Solucionador ou Gerente Cesec.</b>" [Label String(1500) → CPE_PDCI2019.LABEL150] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados para enviar para parecer
  - SIM_NAO3 "Há orçamento para conta/UOR informada?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM]
    - coluna ITEM_OBSOLETO obrigatório
    - coluna ITEM obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL]
    - coluna ITEM1 obrigatório
    - coluna VALOR_TOTAL
    - coluna VALOR_REFERENCIAL obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM
  - UOR "UOR(s) de alocação de despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR]
    - coluna UOR obrigatório
  - CONTA_CONTABIL1 "Conta Contábil" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1]
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - PARECER_QUALIF "Parecer Controladoria" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF]
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica".)" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]
  - OBS24 "Ações tomadas do cliente sobre a reprovação da Gemac, se houver." [Memo String(2000) → CPE_CSC.OBS24]
- Relatorios:
  - FormatoExportacao=PDF

### [366319] Tarefa "Solicitar aprovação do Gerente Executivo da Contratação"
Responsável: Responsável atual (papel 36)
Config: Codigo=APROVAR_GEREX
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
from Venki.Services.Custom import Query
#OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.Salva()


import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Solicitar aprovação do Gerente Executivo da Contratação'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Solicitar aprovação do Gerente Executivo da Contratação'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar projeto básico eletrônico simplificado - Gerente Executivo; ReprovarImediato=true; ReenvioEmailAprovacao=24; ObrigatoriedadeMotivo=Todas
  - item para aprovação ""
  - item para aprovação ""
  - aprovador: Gerente - PPGEREX_NEGOCIO (Unico)
  - relatório: FormatoExportacao=PDF; RotuloLink=Para acessar o PROJETO BÁSICO preenchido, CLIQUE AQUI.
- Relatorios:
  - FormatoExportacao=PDF

### [366260] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório."
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico

#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR'].ToString()+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Tabela de Aprovações    
#consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'
#
#for dados in consultaAprovacoes.Rows:
#
#    cargo = ''
#    
#    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
#        cargo = dados['FUNCAO_GRATIFICADA']
#    else:
#        cargo = dados['CARGO']
#
#    tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
#    
#OrdemServico["APROVACOES"] = tabelaAprovacoes
#
#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')  

#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos




import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Recolhimento de aprovações e outras informações para preenchimento do relatório'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Recolhimento de aprovações e outras informações para preenchimento do relatório'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos
  - TABELA_DADOS_CONTRATOS_C "Tabela de Dados Contratuais" [Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C]
  - APROVACOES "Campo para preenchimento das aprovações." [Memo String(2000) → CPE_CSC.APROVACOES]
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366261] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório."
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico

#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR'].ToString()+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Tabela de Aprovações    
consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'

for dados in consultaAprovacoes.Rows:

    cargo = ''
    
    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
        cargo = dados['FUNCAO_GRATIFICADA']
    else:
        cargo = dados['CARGO']

    tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
    
OrdemServico["APROVACOES"] = tabelaAprovacoes.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')  

#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos














import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()




AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos
  - TABELA_DADOS_CONTRATOS_C "Tabela de Dados Contratuais" [Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C]
  - APROVACOES "Campo para preenchimento das aprovações." [Memo String(2000) → CPE_CSC.APROVACOES]
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366262] Tarefa "Responder Questionário Pesquisa de Mercado e Mitigação de Fracionamento de Demanda"
Responsável: Cliente (papel 18)
Config: RotuloBotaoAvancar=Avançar (Enviar para Cesec)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Pesquisa
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)



etapa = 'Questionário Pesquisa de Mercado e Mitigação de Fracionamento de Demanda'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Pesquisa
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Questionário Pesquisa de Mercado e Mitigação de Fracionamento de Demanda'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptValidacao**
```python
#--- Validação de subcampos conforme marcação

if OrdemServico.GetCustom("TIPO_DE_VALOR_DE_REFERENCIA") == 'Outros:':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('JUSTIFICATIVA_IMPACTO')): 
        Criticas.AdicionaPendencia("Preencha o campo 'Informe detalhadamente o método estatístico utilizado (Valor Referencial)'.")
         
if OrdemServico.GetCustom("SIM_NAO1") == 'Não':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('OBS6')): 
     Criticas.AdicionaPendencia("Preencha o campo 'JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002'.")
```
**ScriptFormCarregado**
```python
Formulario["SIM_NAO6"].Visivel = False
Formulario["FQ415_066_ITEM31"].Habilitado = True
Formulario["FQ415_066_ITEM31"].Visivel = True
Formulario["FQ415_066_ITEM32"].Habilitado = True
Formulario["FQ415_066_ITEM32"].Visivel = True
Formulario["FQ415_066_ITEM321"].Habilitado = True
Formulario["FQ415_066_ITEM321"].Visivel = True
Formulario["FQ415_066_ITEM322"].Habilitado = True
Formulario["FQ415_066_ITEM322"].Visivel = True
Formulario["FQ415_066_ITEM33"].Habilitado = True
Formulario["FQ415_066_ITEM33"].Visivel = True
Formulario["FQ415_066_ITEM331"].Habilitado = True
Formulario["FQ415_066_ITEM331"].Visivel = True
Formulario["JUSTIFICATIVA_IMAGEM"].Habilitado = True
Formulario["JUSTIFICATIVA_IMAGEM"].Visivel = True

Formulario["SIM_NAO1"].Habilitado = True
Formulario["SIM_NAO1"].Visivel = True
Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True
Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = False

Formulario["JUSTIFICATIVA_TENDENCIA"].Habilitado = True
Formulario["JUSTIFICATIVA_TENDENCIA"].Visivel = True
Formulario["LABEL107"].Habilitado = True
Formulario["LABEL107"].Visivel = True
Formulario["LABEL108"].Habilitado = True
Formulario["LABEL108"].Visivel = True

Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Habilitado = True
Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Visivel = True
Formulario["OBS6"].Habilitado = True
Formulario["OBS6"].Visivel = False

Formulario["QTD_PESQUISA"].Visivel = False
Formulario["FORNECEDOR01"].Visivel = False
Formulario["PESQUISA_MERCADO1"].Visivel = False
Formulario["FORNECEDOR2"].Visivel = False
Formulario["PESQUISA_MERCADO2"].Visivel = False
Formulario["FORNECEDOR3"].Visivel = False
Formulario["PESQUISA_MERCADO3"].Visivel = False
Formulario["FORNECEDOR4"].Visivel = False
Formulario["PESQUISA_MERCADO4"].Visivel = False
Formulario["FORNECEDOR5"].Visivel = False
Formulario["PESQUISA_MERCADO_5"].Visivel = False
Formulario["FORNECEDOR6"].Visivel = False
Formulario["PESQUISA_MERCADO6"].Visivel = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Acionamento (E-mails)" classes: Anexo de  Evidência — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "MCC (Mapa Comparativo de Compras)" classes: FQ415 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Certidões" classes: Certidões — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Declínios (Se houver)" classes: Arquivo 08 — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - FORNECEDOR01 "Fornecedor 1" [TextBox String → CPE_CSC.FORNECEDOR01]
  - PESQUISA_MERCADO1 "PESQUISA DE MERCADO 1" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO1.PESQUISA_MERCADO1] — FormaEdicaoWeb=JanelaPopup
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO1.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
    - coluna DESCRICAO_ITEM
    - coluna ITEM
    - coluna UDM obrigatório
    - coluna QUANTIDADE obrigatório
**PESQUISA_MERCADO1.QUANTIDADE.ScriptModificado**
```python
Convert.ToDecimal(FormularioRegistro["QUANTIDADE"].Valor)
```
    - coluna ITEM1 obrigatório
  - FORNECEDOR2 "Fornecedor 2" [TextBox String → CPE_CSC.FORNECEDOR2]
  - PESQUISA_MERCADO2 "PESQUISA DE MERCADO 2" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO2.PESQUISA_MERCADO2] — FormaEdicaoWeb=JanelaPopup
    - coluna DESCRICAO_ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO2.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM
    - coluna QUANTIDADE obrigatório
    - coluna UDM obrigatório
    - coluna VALOR obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
  - FORNECEDOR3 "Fornecedor 3" [TextBox String → CPE_CSC.FORNECEDOR3]
  - PESQUISA_MERCADO3 "PESQUISA DE MERCADO 3" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO3.PESQUISA_MERCADO3] — FormaEdicaoWeb=JanelaPopup
    - coluna ITEM
    - coluna DESCRICAO_ITEM
    - coluna UDM obrigatório
    - coluna ITEM1 obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO3.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
  - FORNECEDOR4 "Fornecedor 4" [TextBox String → CPE_CSC.FORNECEDOR4]
  - PESQUISA_MERCADO4 "PESQUISA DE MERCADO 4" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO4.PESQUISA_MERCADO4] — FormaEdicaoWeb=JanelaPopup
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO4.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna ITEM
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
  - FORNECEDOR5 "Fornecedor 5" [TextBox String → CPE_CSC.FORNECEDOR5]
  - PESQUISA_MERCADO_5 "PESQUISA DE MERCADO 5" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO_5.PESQUISA_MERCADO_5] — FormaEdicaoWeb=JanelaPopup
    - coluna UDM obrigatório
    - coluna VALOR obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO_5.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna ITEM
    - coluna DESCRICAO_ITEM
    - coluna QUANTIDADE obrigatório
  - FORNECEDOR6 "Fornecedor 6" [TextBox String → CPE_CSC.FORNECEDOR6]
  - PESQUISA_MERCADO6 "PESQUISA DE MERCADO 6" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO6.PESQUISA_MERCADO6] — FormaEdicaoWeb=JanelaPopup
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO6.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna DESCRICAO_ITEM
    - coluna UDM obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
    - coluna ITEM1 obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais para a Pesquisa de Mercado
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. " [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184 Mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario['SIM_NAO1'].Valor == "Não":
   Formulario['OBS6'].Habilitado = True
   Formulario['OBS6'].Visivel = True
else:
   Formulario['OBS6'].Habilitado = False
   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
  - SIM_NAO6 "Há pesquisa de mercado prévia? Se sim, favor anexar." [DropDownList String → CPE_CSC.SIM_NAO6] obrigatório
**SIM_NAO6.ScriptModificado**
```python
#if Formulario['SIM_NAO6'].Valor == "Sim":
#   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = True
#   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = True
#   Formulario['JUSTIFICATIVA_IMAGEM'].Habilitado = True
#   Formulario['JUSTIFICATIVA_IMAGEM'].Visivel = True
#   Formulario['JUSTIFICATIVA_TENDENCIA'].Habilitado = True
#   Formulario['JUSTIFICATIVA_TENDENCIA'].Visivel = True
#   Formulario['FQ415_066_ITEM31'].Habilitado = True
#   Formulario['FQ415_066_ITEM31'].Visivel = True
#   Formulario['FQ415_066_ITEM32'].Habilitado = True
#   Formulario['FQ415_066_ITEM32'].Visivel = True
#   Formulario['FQ415_066_ITEM321'].Habilitado = True
#   Formulario['FQ415_066_ITEM321'].Visivel = True
#   Formulario['FQ415_066_ITEM322'].Habilitado = True
#   Formulario['FQ415_066_ITEM322'].Visivel = True
#   Formulario['FQ415_066_ITEM33'].Habilitado = True
#   Formulario['FQ415_066_ITEM33'].Visivel = True
#   Formulario['FQ415_066_ITEM331'].Habilitado = True
#   Formulario['FQ415_066_ITEM331'].Visivel = True
#   Formulario['SIM_NAO1'].Habilitado = True
#   Formulario['SIM_NAO1'].Visivel = True   
#   
#
#if Formulario['SIM_NAO6'].Valor != "Sim":
#   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = False
#   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = False
#   Formulario['JUSTIFICATIVA_IMAGEM'].Habilitado = False
#   Formulario['JUSTIFICATIVA_IMAGEM'].Visivel = False
#   Formulario['JUSTIFICATIVA_TENDENCIA'].Habilitado = False
#   Formulario['JUSTIFICATIVA_TENDENCIA'].Visivel = False
#   Formulario['FQ415_066_ITEM31'].Habilitado = False
#   Formulario['FQ415_066_ITEM31'].Visivel = False
#   Formulario['FQ415_066_ITEM32'].Habilitado = False
#   Formulario['FQ415_066_ITEM32'].Visivel = False
#   Formulario['FQ415_066_ITEM321'].Habilitado = False
#   Formulario['FQ415_066_ITEM321'].Visivel = False
#   Formulario['FQ415_066_ITEM322'].Habilitado = False
#   Formulario['FQ415_066_ITEM322'].Visivel = False
#   Formulario['FQ415_066_ITEM33'].Habilitado = False
#   Formulario['FQ415_066_ITEM33'].Visivel = False
#   Formulario['FQ415_066_ITEM331'].Habilitado = False
#   Formulario['FQ415_066_ITEM331'].Visivel = False
#   Formulario['SIM_NAO1'].Habilitado = False
#   Formulario['SIM_NAO1'].Visivel = False
```
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar 'Não se aplica'. (Sugere-se, preferencialmente, utilizar o método estatístico de média ou mediana)" [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
**TIPO_DE_VALOR_DE_REFERENCIA.ScriptModificado**
```python
if Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Valor == 'Outros:':
    Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = True
    Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True
    
if Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Valor != 'Outros:':
    Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = False
#   Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = False
    
#Lembrete de referencial escolhido

if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Maior Preço":
    Formulario.ExibeMensagem("Lembrete: \n\nMétodo estatístico de 'Maior Preço' prejudicial á BBTS. Somente aceito com Nota Técnica anexa com 'de acordo' da Gesuc, com fundamentação da necessidade.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Não se aplica":
    Formulario.ExibeMensagem("Lembrete: \n\nMétodo estatístico 'Não se aplica' informado somente em Inexigibilidade de Licitação (inviabilidade de competição); com todos os insumos da TAB415-001 anexados.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Outros:":
    Formulario.ExibeMensagem("Lembrete: \n\nSe ultilizado método estatístico diferente dos convencionais (Média, Mediana ou Menor Valor) é obrigatório informar detalhadamente abaixo o 'Método estatístico utilizado (Valor Referencial)', com critérios fundamentados.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Menor Preço":
    Formulario.ExibeMensagem("Lembrete: \n\nSugere-se, preferencialmente, utilizar o método estatístico de Média ou Mediana. Este item estipula o valor referencial para a aprovação do orçamento (até quanto poderá ser gasto); não o critério de escolha do fornecedor, informado no item abaixo 'Justificativa da escolha do(s) fornecedor(es)' de padrão como 'Melhor/Menor Preço.'.")
```
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - JUSTIFICATIVA_IMPACTO "Informe detalhadamente o método estatístico utilizado (Valor Referencial)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - QTD_PESQUISA "Quantidade de Pesquisas" [DropDownList String → CPE_CSC.QTD_PESQUISA]
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79 mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informação importante!
  - LABEL108 "FQ415-019 MAPA COMPARATIVO DE COMPRAS ARTIGO 29, INCISOS I E II: <a href="
https://intranet.bbts.com.br/images/misc/normas/serie4/FQ415-019_V_02.xlsx" target="_blank">
clique aqui. </a>" [Label String(500) → CPE_CONTRATOS.LABEL108] obrigatório
  - LABEL100 "<b style="color:red">Para o comparativo de preços, utilizar a FQ415-019 (Vide anexos).</b>" [Label String(1000) → CPE_CONTRATOS.LABEL100] obrigatório
  - LABEL107 "PRO417-002 PESQUISA DE PREÇOS DE MERCADO: <a href="https://bbts.docnix.com.br/bbts/corporate/index.html#/maxdoc/link/documento/35057821" target="_blank">
clique aqui. </a>" [Label String(1000) → CPE_CONTRATOS.LABEL107] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=PROPOSTAREC
  - anexo "Proposta(s) Recebida(s)" classes: Pesquisa de Mercado — RequeridoInicial=true
- Relatorios:
  - FormatoExportacao=PDF

### [366263] EventoIntermediarioMensagem "Aviso de retorno da Ordem de Serviço"
Config: ListaDestinatarios=cesec.comp@bbts.com.br
ModeloComunicado: Aviso de retorno de chamado
Corpo do comunicado: Prezado(a),
Foi recebido na respectiva fila o chamado: OrdemServico - OrdemServico.Assunto .
Para mais informações Link.Edicao .
Atenciosamente,
Central de Serivços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Cadastrar pesquisa de mercado e Valor referencial"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "cesec.comp@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366264] FimCancelamento "Cancelamento por reprovação"
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Cancelada"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        log("Falha ao obter comprador_padrao: " + str(ex))

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```

### [366265] Tarefa "Cadastrar pesquisa de mercado e Valor referencial"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()




etapa = 'Cadastrar pesquisa de mercado e Valor referencial'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Cadastrar pesquisa de mercado e Valor referencial'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
    

    
    
    
URL_ITENS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-itens-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass    


    
    
nomeDoResponsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    nomeDoResponsavel = row["NOME"].ToString()
    
# ===== 2) Monta lista de itens a partir da grid LISTA_ECOM =====
from System import DBNull

def to_text(val):
    from System import DBNull

    if val is None or val == DBNull.Value:
        return None

    try:
        s = val.ToString()
    except:
        try:
            s = str(val)
        except:
            return None

    s = s.strip()
    return s if s != "" else None


def to_decimal(val, default_str="0.00"):
    txt = to_text(val)

    if txt is None:
        txt = default_str

    norm = txt.replace(".", "").replace(",", ".")

    try:
        return round(float(norm), 2)
    except:
        return round(float(default_str.replace(",", ".")), 2)


def calcular_quantidade(valor_total, valor_unitario):
    total = to_decimal(valor_total, "0.00")
    unitario = to_decimal(valor_unitario, "0.00")

    # Evita divisão por zero
    if unitario <= 0:
        return 0

    quantidade = total / unitario

    # Se o resultado for inteiro, retorna sem casas decimais
    if quantidade.is_integer():
        return int(quantidade)

    return round(quantidade, 2)


def extrair_nome_item(codigo):
    codigo_texto = to_text(codigo)

    if codigo_texto is None:
        return ""

    # Divide somente nos dois primeiros " - "
    partes = codigo_texto.split(" - ", 2)

    if len(partes) >= 3:
        return partes[2].strip()

    # Se não encontrar dois hífens, retorna vazio
    return ""

# ... obtém 

lista = OrdemServico.GetCustom("VALOR_REFERENCIAL")

colnames = [c.ColumnName for c in lista.Columns]
itens = []

for i in range(getattr(lista.Rows, "Count", 0)):
    r = lista.Rows[i]

    try:
        codigo = to_text(r["ITEM1"]) if "ITEM1" in colnames else None
        descricao = "N/A"

        preco_unitario = 0.00
        if "VALOR_UNITARIO" in colnames:
            preco_unitario = to_decimal(r["VALOR_UNITARIO"], "0.00")

        valor_total = 0.00
        if "VALOR_TOTAL" in colnames:
            valor_total = to_decimal(r["VALOR_TOTAL"], "0.00")

        qtd = calcular_quantidade(r["VALOR_TOTAL"], r["VALOR_UNITARIO"])
        nome = extrair_nome_item(codigo)

        fornecedor = "Não informado"
        necessidade = "Outros"

        itens.append({
            "codigo_item": codigo,
            "descricao_item": descricao,
            "quantidade": qtd,
            "preco_unitario": preco_unitario,
            "comprador_nome": nomeDoResponsavel,
            "fornecedor_nome": fornecedor,
            "nome": nome,
            "necessidade": necessidade
        })

    except Exception as ex:
        # log("Linha {} ignorada por erro: {}".format(i + 1, str(ex)))
        pass

# ===== 3) Envia itens (se houver) =====
if len(itens) == 0:
    pass
    #log("Nenhum item válido encontrado em VALOR_REFERENCIAL; nada a enviar.")
else:
    payload_itens = {
        "os": os_numero,
        "itens": itens
    }
    ok, status_code, body = http_post_json(URL_ITENS_SALVAR, payload_itens)
    #log("Payload Itens: " + JsonConvert.SerializeObject(payload_itens))
    if not ok:
        pass
        #log("Falha ao salvar itens (HTTP {}): {}".format(status_code, body))
    else:
        try:
            obj = JsonConvert.DeserializeObject(body)
            st = obj["status"] if "status" in obj else "?"
            msg = obj["message"] if "message" in obj else ""
            ins = obj["inseridos"] if "inseridos" in obj else "?"
            #log("Salvar Itens -> {} (inseridos={}): {}".format(st, ins, msg))
        except:
            pass
```
**ScriptFormCarregado**
```python
Formulario["CODIGO_ITEM"].Visivel = True
Formulario["FORNECEDOR01"].Visivel = True
Formulario["FORNECEDOR2"].Visivel = True
Formulario["FORNECEDOR3"].Visivel = True
Formulario["FORNECEDOR4"].Visivel = True
Formulario["FORNECEDOR5"].Visivel = True
Formulario["FORNECEDOR6"].Visivel = True
Formulario["PESQUISA_MERCADO1"].Visivel = True
Formulario["PESQUISA_MERCADO2"].Visivel = True
Formulario["PESQUISA_MERCADO3"].Visivel = True
Formulario["PESQUISA_MERCADO4"].Visivel = True
Formulario["PESQUISA_MERCADO_5"].Visivel = True
Formulario["PESQUISA_MERCADO6"].Visivel = True
Formulario["QTD_PESQUISA"].Visivel = True
Formulario["QTD_PESQUISA"].Habilitado = True
Formulario["VALOR"].Visivel = False
Formulario["VALOR"].Habilitado = False
Formulario["VALOR_DOD"].Visivel = False
Formulario["VALOR_DOD"].Habilitado = False
Formulario["VALOR_REFERENCIAL"].Visivel = True
Formulario["VALOR_REFERENCIAL"].Habilitado = True
Formulario["CODIGO_ITEM"].Habilitado = True
Formulario["FORNECEDOR01"].Habilitado = True
Formulario["FORNECEDOR2"].Habilitado = True
Formulario["FORNECEDOR3"].Habilitado = True
Formulario["FORNECEDOR4"].Habilitado = True
Formulario["FORNECEDOR5"].Habilitado = True
Formulario["FORNECEDOR6"].Habilitado = True
Formulario["PESQUISA_MERCADO1"].Habilitado = True
Formulario["PESQUISA_MERCADO2"].Habilitado = True
Formulario["PESQUISA_MERCADO3"].Habilitado = True
Formulario["PESQUISA_MERCADO4"].Habilitado = True
Formulario["PESQUISA_MERCADO_5"].Habilitado = True
Formulario["PESQUISA_MERCADO6"].Habilitado = True


Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Visivel = True
Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Habilitado = True
Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = True
Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True


Formulario["QTD_PESQUISA"].Itens = "1;2;3;4;5;6"
```
- Operação PR0001 Preencher Campos
  - CODIGO_ITEM "Código do Item" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna ITEM obrigatório
    - coluna ITEM_OBSOLETO obrigatório
    - coluna NECESSIDADE obrigatório
  - QTD_PESQUISA "Quantidade de Pesquisas" [DropDownList String → CPE_CSC.QTD_PESQUISA] obrigatório
**QTD_PESQUISA.ScriptModificado**
```python
if Formulario["QTD_PESQUISA"].Valor == "6":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = True
    Formulario["FORNECEDOR6"].Habilitado = True
    Formulario["PESQUISA_MERCADO6"].Visivel = True
    Formulario["PESQUISA_MERCADO6"].Habilitado = True


if Formulario["QTD_PESQUISA"].Valor == "5":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "4":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False

if Formulario["QTD_PESQUISA"].Valor == "3":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
    
if Formulario["QTD_PESQUISA"].Valor == "2":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = False
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "1":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = False
    Formulario["FORNECEDOR2"].Habilitado = False
    Formulario["PESQUISA_MERCADO2"].Visivel = False
    Formulario["PESQUISA_MERCADO2"].Habilitado = False
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = False
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
```
  - CHECKBOX8 "Clique aqui para desativar o cálculo automatico do campo VALOR TOTAL da grid abaixo:" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX8]
  - FORNECEDOR01 "Fornecedor 1" [TextBox String → CPE_CSC.FORNECEDOR01] obrigatório
  - PESQUISA_MERCADO1 "PESQUISA DE MERCADO 1" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO1.PESQUISA_MERCADO1] obrigatório — FormaEdicaoWeb=JanelaPopup
**PESQUISA_MERCADO1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''

contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna ITEM
    - coluna DESCRICAO_ITEM
    - coluna VALOR obrigatório
**PESQUISA_MERCADO1.VALOR.ScriptModificado**
```python
if Formulario['CHECKBOX8'].Valor == False:
    FormularioRegistro["VALOR"].Habilitado = True
    (FormularioRegistro["VALOR"].Valor) = (FormularioRegistro["QUANTIDADE"].Valor) * (FormularioRegistro["VALOR_UNITARIO"].Valor)
```
    - coluna ITEM1 obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna UDM obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO1.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
  - FORNECEDOR2 "Fornecedor 2" [TextBox String → CPE_CSC.FORNECEDOR2]
  - PESQUISA_MERCADO2 "PESQUISA DE MERCADO 2" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO2.PESQUISA_MERCADO2] — FormaEdicaoWeb=JanelaPopup
**PESQUISA_MERCADO2.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''

contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna VALOR obrigatório
**PESQUISA_MERCADO2.VALOR.ScriptModificado**
```python
if Formulario['CHECKBOX8'].Valor == False:
    FormularioRegistro["VALOR"].Habilitado = True
    (FormularioRegistro["VALOR"].Valor) = (FormularioRegistro["QUANTIDADE"].Valor) * (FormularioRegistro["VALOR_UNITARIO"].Valor)
```
    - coluna DESCRICAO_ITEM
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO2.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna UDM obrigatório
    - coluna VALOR_UNITARIO obrigatório
  - FORNECEDOR3 "Fornecedor 3" [TextBox String → CPE_CSC.FORNECEDOR3]
  - PESQUISA_MERCADO_5 "PESQUISA DE MERCADO 5" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO_5.PESQUISA_MERCADO_5] — FormaEdicaoWeb=JanelaPopup
**PESQUISA_MERCADO_5.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''

contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna VALOR obrigatório
**PESQUISA_MERCADO_5.VALOR.ScriptModificado**
```python
if Formulario['CHECKBOX8'].Valor == False:
    FormularioRegistro["VALOR"].Habilitado = True
    (FormularioRegistro["VALOR"].Valor) = (FormularioRegistro["QUANTIDADE"].Valor) * (FormularioRegistro["VALOR_UNITARIO"].Valor)
```
    - coluna ITEM1 obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO_5.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    

    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna DESCRICAO_ITEM
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO_5.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
  - FORNECEDOR6 "Fornecedor 6" [TextBox String → CPE_CSC.FORNECEDOR6]
  - PESQUISA_MERCADO6 "PESQUISA DE MERCADO 6" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO6.PESQUISA_MERCADO6] — FormaEdicaoWeb=JanelaPopup
**PESQUISA_MERCADO6.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''

contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna DESCRICAO_ITEM
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO6.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO6.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna QUANTIDADE obrigatório
    - coluna VALOR obrigatório
**PESQUISA_MERCADO6.VALOR.ScriptModificado**
```python
if Formulario['CHECKBOX8'].Valor == False:
    FormularioRegistro["VALOR"].Habilitado = True
    (FormularioRegistro["VALOR"].Valor) = (FormularioRegistro["QUANTIDADE"].Valor) * (FormularioRegistro["VALOR_UNITARIO"].Valor)
```
    - coluna UDM obrigatório
    - coluna ITEM
  - VALOR_REFERENCIAL "Valor Referencial (para referencial menor preço ou mediana com 3 propostas arrendonde para cima, se necessário, para valor total bater com total da(s) proposta(s))" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL] obrigatório
    - coluna VALOR_REFERENCIAL obrigatório
**VALOR_REFERENCIAL.VALOR_REFERENCIAL.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM
    - coluna VALOR_TOTAL obrigatório
    - coluna ITEM1 obrigatório
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1 (Valor referencial escolhido pelo cliente) - Incongruências ajustar ou devolver ao cliente" [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
  - JUSTIFICATIVA_IMPACTO "Justificativa 1 (Metodologia aplicada em caso de valor referencial escolhido "Outros")" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - VALOR "DOTAÇÃO ORÇAMENTÁRIA (VALOR GLOBAL OU VALOR GLOBAL ESTIMADO): R$ " [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - FORNECEDOR4 "Fornecedor 4" [TextBox String → CPE_CSC.FORNECEDOR4]
  - PESQUISA_MERCADO4 "PESQUISA DE MERCADO 4" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO4.PESQUISA_MERCADO4] — FormaEdicaoWeb=JanelaPopup
**PESQUISA_MERCADO4.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''

contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO4.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM
    - coluna ITEM1 obrigatório
    - coluna DESCRICAO_ITEM
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
**PESQUISA_MERCADO4.VALOR.ScriptModificado**
```python
if Formulario['CHECKBOX8'].Valor == False:
    FormularioRegistro["VALOR"].Habilitado = True
    (FormularioRegistro["VALOR"].Valor) = (FormularioRegistro["QUANTIDADE"].Valor) * (FormularioRegistro["VALOR_UNITARIO"].Valor)
```
    - coluna UDM obrigatório
    - coluna QUANTIDADE obrigatório
  - FORNECEDOR5 "Fornecedor 5" [TextBox String → CPE_CSC.FORNECEDOR5]
  - VALOR_DOD "Preço Global Referencial: R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]
  - PESQUISA_MERCADO3 "PESQUISA DE MERCADO 3" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO3.PESQUISA_MERCADO3] — FormaEdicaoWeb=JanelaPopup
**PESQUISA_MERCADO3.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''

contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna ITEM
    - coluna ITEM1 obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna DESCRICAO_ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO3.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR obrigatório
**PESQUISA_MERCADO3.VALOR.ScriptModificado**
```python
if Formulario['CHECKBOX8'].Valor == False:
    FormularioRegistro["VALOR"].Habilitado = True
    (FormularioRegistro["VALOR"].Valor) = (FormularioRegistro["QUANTIDADE"].Valor) * (FormularioRegistro["VALOR_UNITARIO"].Valor)
```
    - coluna UDM obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informação!
  - LABEL21 "Salve e atualize antes de Avançar!" [Label String(700) → CPE_PDCI2019.LABEL21] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366266] Tarefa "Informar Conta Contábil"
Responsável: Fila Contabilidade (papel 254)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.ModificaCampoFormularioVisivel('UOR', True)


import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Informar Conta Contábil'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


OrdemServico.Salva()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Informar Conta Contábil'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
#OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
#
#Formulario['UOR'].Visivel = True
#Formulario['UOR'].Habilitado = True
#
#OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informação!
  - LABEL21 "Salve e atualize antes de Avançar!" [Label String(700) → CPE_PDCI2019.LABEL21] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM]
    - coluna ITEM obrigatório
    - coluna NECESSIDADE obrigatório
    - coluna ITEM_OBSOLETO obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL]
    - coluna VALOR_TOTAL
    - coluna ITEM1 obrigatório
    - coluna ITEM
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR_REFERENCIAL obrigatório
  - UOR "UOR(s) de alocação de despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR]
    - coluna UOR obrigatório
  - CONTA_CONTABIL1 "Parecer Contabilidade (Avaliar conta indicada pelo cliente, se estiver preenchido)" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366267] EventoIntermediarioMensagem "Reprovação Cliente"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Projeto Básico Reprovado - Ajustes
Corpo do comunicado: Prezado(a),
O projeto básico foi reprovado e necessita de ajustes.
Para ajustar o projeto básico, Link.Workspace .
Ajustes Necessários:
 Complemento1 
Dados do Projeto:
Objeto:
 OrdemServico.Customizado.PB_OBJETO_CONTRATACAO 
Itens da Contratação:
 OrdemServico.Customizado.CODIGO_ITEM 
Após ajustar as informações, clique em "Avançar" para submeter novamente para aprovação.
Qualquer dúvida, entre em contato com Cesec - Centro de Serviços Compartilhados.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROVACAOCLIENTE")

if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Verificar Reprovação Cliente"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Responsável atual"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366268] EventoIntermediarioTimer ""
Config: TempoIntervalo=14400; MaximoExecucao=1

### [366269] EventoIntermediarioTimer ""
Config: TempoIntervalo=200

### [366270] EventoIntermediarioTimer ""
Config: TempoIntervalo=720

### [366271] EventoIntermediarioTimer ""
Config: TempoIntervalo=720

### [366272] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Codigo=PROJETOB; PermitirRascunho=true
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
TipoSolicitacao: 05.04. Suprimentos Corporativos, Licitações e Contratos - Contratos
**ScriptFim**
```python
OrdemServico.AdicionaComentario("Conta Contábil indicada pelo cliente na abertura do chamado (informação será validada pela Contabilidade): " + OrdemServico["CONTA_CONTABIL1"],False)

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


URL_OS_SALVAR    = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao  = "Aberta"

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""

try:
    recebedor = OrdemServico.ClienteId.ToString()
    if recebedor is not None:
        
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
        
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        #log("Falha ao obter comprador_padrao: " + str(ex))
        pass

# Garante que não vai nulo (sua action exige não nulo)
if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== 1) Garante a OS (upsert) =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "OS criada/atualizada via integração"
}
ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))
if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
    #durante o teste, não levantar exceção; comente o raise
    #raise Exception("Erro ao salvar OS")
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        #log("Salvar OS (resposta cru): " + body)
        pass
```
**ScriptValidacao**
```python
from Venki.Supravizio.Recurso.Custom import Local
from Venki.Supravizio.Processo.Custom import Pesquisa
from Venki.Supravizio.Processo.Custom import Servico
campo1 = OrdemServico.GetCustom('SIM_NAO201').ToString()
campo2 = OrdemServico.GetCustom('SIM_NAO202').ToString()
campo3 = OrdemServico.GetCustom('SIM_NAO203').ToString()
uor = OrdemServico.GetCustom("UOR")
gerex = OrdemServico.GetCustom('PPGEREX_NEGOCIO')


campos = [campo1, campo2, campo3]


if 'Sim' in campos:
    Criticas.AdicionaPendencia('Identificamos que a sua contratação não se enquadra em PBe. Gentileza abrir chamado no: SISCCON <https://sisccon.bbts.com.br>.')
    
#--- Checkbox
if OrdemServico.GetCustom("CHECKBOX9") == False:
   Criticas.AdicionaPendencia("Confirme a revisão de preenchimento dos campos obrigatórios.")
       
#--- Validação de anexo quando a realizado Pesquisa de Mercado prévia pelo cliente
if OrdemServico.GetCustom("SIM_NAO6") == 'Sim':
    if OrdemServico.PossuiItem('PESQUISA') == False: 
         Criticas.AdicionaPendencia("Pesquisa(s) de Mercado/Proposta(s) não foi(foram) anexada(s).")
    if OrdemServico.PossuiItem('CNDFEDER') == False: 
         Criticas.AdicionaPendencia("CND Federal ou Sicaf não foi anexado.")
    if OrdemServico.PossuiItem('CNDFGTS') == False: 
         Criticas.AdicionaPendencia("CND FGTS (CRF) ou Sicaf não foi anexado.")
    if OrdemServico.PossuiItem('CONSULTATCU') == False: 
         Criticas.AdicionaPendencia("Consulta Consolidada TCU não foi anexado.")
    if OrdemServico.PossuiItem('CARTAOCNPJ') == False: 
         Criticas.AdicionaPendencia("Cartão CNPJ <https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/> não foi anexado. O CNAE dos fornecedores devem ser obrigatóriamente compativeis com o objeto; exemplo: se a compra/contratação for Serviços de Engenharia, o Cartão CNPJ deve conter Serviços de Engenharia ou similar.")      
         

#--- Validação de anexo Remanejamento Orçamentário quando informado que o item orçamentário é centralizado
#if OrdemServico.GetCustom("AREA_GESTORA_ITEM") == 'Não (Item Orçamentário Centralizado)':
#    if OrdemServico.PossuiItem('REMANEJORCAM') == False: 
#         Criticas.AdicionaPendencia("Evidência do Remanejamento Orçamentário não foi anexado no campo 'Demais documentos'.")
     

if uor.Rows.Count > 1:
    if OrdemServico.PossuiItem("RATEIOLOCALIDADES") == False:
        Criticas.AdicionaPendencia("Para solicitações com mais de uma UOR, é obrigatória o anexo do 'Rateio de Localidades'.")
        

if OrdemServico.GetCustom("SIM_NAO10") == 'Sim':
   if OrdemServico.PossuiItem("ARTE") == False:
        Criticas.AdicionaPendencia("Necessário anexar a 'Arte' para o(s) produto(s) a ser(em) adquirido(s) conforme catálogo ou especificações enviadas pela Gemac.")

#--- Validação de subcampos conforme marcação

if OrdemServico.GetCustom("SIM_NAO7") == 'Sim':
    if String.IsNullOrEmpty(gerex):
        Criticas.AdicionaPendencia("Informe o(a) Gerente Executivo(a) que efetuará a aprovação.")
         
if OrdemServico.GetCustom("TIPO_DE_VALOR_DE_REFERENCIA") == 'Outros:':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('JUSTIFICATIVA_IMPACTO')): 
        Criticas.AdicionaPendencia("Preencha o campo 'Informe detalhadamente o método estatístico utilizado (Valor Referencial)'.")
         
if OrdemServico.GetCustom("SIM_NAO1") == 'Não':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('OBS6')): 
     Criticas.AdicionaPendencia("Preencha o campo 'JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002'.")
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Empresa
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Pesquisa
from Venki.Supravizio.Configuracao.Custom import Software
Formulario['DOTACAO1'].Habilitado = True
Formulario['COMBOBOX10'].Itens = 'Custo;Investimento;Despesa;Inventário'
Formulario['COMBOBOX10'].Visivel = True
Formulario['SIM_NAO4'].Visivel = False
Formulario['CSC_CPF'].Visivel = False
Formulario['CONTA_CONTABIL1'].Visivel = True
Formulario['CONTA_CONTABIL1'].Habilitado = True
Formulario['SIM_NAO7'].Visivel = True
Formulario['SIM_NAO7'].Habilitado = True
Formulario['JUSTIFICATIVA_IMAGEM'].Habilitado = False
Formulario['JUSTIFICATIVA_IMAGEM'].Visivel = False
Formulario['JUSTIFICATIVA_TENDENCIA'].Habilitado = False
Formulario['JUSTIFICATIVA_TENDENCIA'].Visivel = False
Formulario['OBS6'].Habilitado = True
Formulario['OBS6'].Visivel = False
Formulario['FQ415_066_ITEM31'].Habilitado = False
Formulario['FQ415_066_ITEM31'].Visivel = False
Formulario['FQ415_066_ITEM32'].Habilitado = False
Formulario['FQ415_066_ITEM32'].Visivel = False
Formulario['FQ415_066_ITEM321'].Habilitado = False
Formulario['FQ415_066_ITEM321'].Visivel = False
Formulario['FQ415_066_ITEM322'].Habilitado = False
Formulario['FQ415_066_ITEM322'].Visivel = False
Formulario['FQ415_066_ITEM33'].Habilitado = False
Formulario['FQ415_066_ITEM33'].Visivel = False
Formulario['FQ415_066_ITEM331'].Habilitado = False
Formulario['FQ415_066_ITEM331'].Visivel = False
Formulario['LABEL101'].Habilitado = False
Formulario['LABEL101'].Visivel = False
Formulario['SIM_NAO1'].Habilitado = False
Formulario['SIM_NAO1'].Visivel = False
Formulario['PPGEREX_NEGOCIO'].Habilitado = False
Formulario['PPGEREX_NEGOCIO'].Visivel = False
Formulario['TEXT'].Habilitado = False
Formulario['TEXT'].Visivel = False
Formulario['CHECKBOX9'].Habilitado = False
Formulario['CHECKBOX9'].Visivel = False

    

    
Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Visivel = False
Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = False
Formulario['SIM_NAO20'].Habilitado = False


Formulario['SIM_NAO_100'].Itens = 'Aquisição de bens (mercadoria); Prestação de Serviços; Aquisição de Industria (com IPI incluso)'

Formulario['LABEL30'].Valor = "<a target='_blank' href= https://sisccon.bbts.com.br/sisccon-controle-certidoes>Clique aqui para consulta das certidões do fornecedor - Sicaf</a>"


Formulario['LABEL31'].Valor = "<a target='_blank' href= https://sisccon.bbts.com.br/sisccon-controle-certidao-tcu>Clique aqui para consulta consolidada de Pessoa Jurídica - TCU</a>"

#Especificações técnicas


#Formulario['COMBOBOX1'].Itens = 'Contratações que envolvam tratamento de dados pessoais predominantemente da BBTS/clientes da BBTS em estabelecimentos ou ambientes de TI do fornecedor.;Contratações que envolvam tratamento de dados pessoais predominantemente da BBTS/clientes da BBTS em estabelecimentos ou ambientes da BBTS e prestação de serviço de mão de obra terceira.;Contratos sem tratamento direto de dados pessoais declarados pelas partes.'

#Formulario['COMBOBOX2'].Itens = 'Sim;Não;Não se aplica'


if String.IsNullOrEmpty(Formulario['OBS21'].Valor):
    Formulario['OBS21'].Valor = "NOTA EXPLICATIVA: \nDescrever todos os requisitos técnicos, funcionais e não funcionais, obrigatórios ou não, além de outros requisitos necessários à contratação, como desenhos técnicos, qualidade dos materiais, padrão ABNT, normas internacionais, cores, dimensões, padrões de qualidade, idioma, voltagem, etc. \nPara cada item do objeto, defina as quantidades, unidade padrão adotada (ex.: unidade, metro, km/mês, h, dentre outros), bem como demais dados necessários à composição do preço.\nNas especificações do objeto para aquisição de bens é permitido indicar marca ou modelo, nas seguintes hipóteses (conforme Art. 47, Inciso I da Lei 13.303/16):\na) em decorrência da necessidade de padronização do objeto;\nb) quando determinada marca ou modelo comercializado por mais de um fornecedor constituir o único capaz de atender o objeto da contratação; e\nc) quando for necessário, para compreensão do objeto, a identificação de determinada marca ou modelo apto a servir como referência, situação em que será obrigatório o acréscimo da expressão ou similar ou de melhor qualidade.\n"

#Qualificação Técnica

if String.IsNullOrEmpty(Formulario['OBS10'].Valor):
    Formulario['OBS10'].Valor = "3.1. A qualificação técnica DA CONTRATADA será avaliada de acordo com os seguintes critérios:\n3.1.1 Registro ou inscrição DA CONTRATADA na entidade profissional xxxx (indicar a entidade profissional) se houver;\n3.1.2 No mínimo 01(um) atestado de capacidade técnica comprovando que executa/executou, serviço compatível em características, quantidades e prazos ao indicado no projeto básico.\n3.1.3 A CONTRATADA deve disponibilizar, se solicitadas, todas as informações necessárias à comprovação da legitimidade dos atestados solicitados.\nNOTA EXPLICATIVA:  \nA depender da especificidade do objeto a ser contratado, os requisitos de qualificação técnica poderão ser adaptados, suprimidos ou acrescidos de outros considerados importantes para a contratação, mediante a devida justificativa técnica. Caso a Qualificação Técnica e/ou Qualificação Econômico-Financeira for dispensada informar 'Não se aplica'.\nInclua neste campo a exigência de HOMOLOGAÇÃO de amostra do fornecedor, se houver. Se for pesquisa de mercado realizada previamente pela área cliente o fornecedor deve está ciente de atendimento desta qualificação para ser selecionado.\nA de solicitação da documentação pertinente á Qualificação Técnica ou envio/aprovação da Amostra (Homologação) é realizada pelo comprador via e-mail na fase de confecção de Ordem de Compra no fim do processo.\n"
    

#Condições de Entrega
if String.IsNullOrEmpty(Formulario['OBS4'].Valor):
    Formulario['OBS4'].Valor = "NOTA EXPLICATIVA: \nFornecer as informações relativas à logística de entrega a ser adotada quanto ao prazo, local de entrega com CEP, horários, tipos de embalagens, orientações para a recepção do produto na dependência e outros relacionados à entrega dos bens.\n"

#Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico
if String.IsNullOrEmpty(Formulario['OBS3'].Valor):
    Formulario['OBS3'].Valor = "NOTA EXPLICATIVA: \nDescrever todas as condições de garantia e assistência técnica, manutenção e suporte técnico, tais como tipo de garantia, prazos, condições de atendimento, fornecimento de novas versões, correções de erros, etc.\nFavor informar o tempo de garantia em dias (Ex: 90 (noventa) dias)."

#Condições de Pagamento
if String.IsNullOrEmpty(Formulario['NN_CONDICAO_PAGAMENTO'].Valor):
    Formulario['NN_CONDICAO_PAGAMENTO'].Valor = "7.1 O pagamento será creditado, (em parcela única OU definir outra condição em caso específico) em conta corrente mantida preferencialmente no Banco do Brasil S.A., em nome da CONTRATADA, em xx dias corridos, a contar da emissão da Nota fiscal, acompanhada do Documento Auxiliar da Nota Fiscal Eletrônica, relativo aos municípios em que o documento é exigido.\n7.2 A nota fiscal deverá ser entregue à CONTRATANTE, em até 5 (cinco) dias úteis subsequentes a data de sua emissão, sendo entregue até o dia 21 (vinte e um) do mês de sua emissão, acompanhada do Documento Auxiliar da Nota Fiscal Eletrônica, relativo a prestação de serviços nos municípios em que o documento é exigido. (Utilizar esse subitem apenas no caso de contratação de serviços).\nNOTA EXPLICATIVA 1: Especificar caso utilize outra condição de pagamento.\nNOTA EXPLICATIVA 2: Deverá ser informado em quantos dias ocorrerá o pagamento e/ou se haverá parcelamento no pagamento.\nNOTA EXPLICATIVA 3: Para pagamento em parcela única, de forma antecipada à execução dos serviços/entrega, deverá ser justificado no documento de aprovação da contratação a escolha dessa opção, pois por regra, os pagamentos devem acompanhar e serem proporcionais as parcelas do objeto entregues/executadas."

#Multa
if String.IsNullOrEmpty(Formulario['OBS5'].Valor):
    Formulario['OBS5'].Valor = "8.1 Em caso de inexecução total ou parcial, será aplicada multa de 20% sobre o valor contratado."
    
    
#Privacidade, Proteção e Trtamento de Dados Pessoais
if String.IsNullOrEmpty(Formulario['OBS50'].Valor):
    Formulario['OBS50'].Valor = "9.1  As partes declaram conhecer e cumprir as leis vigentes envolvendo proteção de dados pessoais, em especial a Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais - LGPD), comprometendo-se a limitar eventual uso de dados pessoais, inclusive de seus representantes, somente para execução do objeto e/ou cumprimento de obrigações acessórias desta contratação, abstendo-se de utilizá-los em proveito próprio ou alheio, para fins comerciais ou quaisquer outros, ressalvadas as hipóteses em que o tratamento seja necessário para o cumprimento legal e regulatório ou exercício regular de direitos."
    
    
#Justificativa da Contratação
#if String.IsNullOrEmpty(Formulario['Descrição detalhada'].Valor):
#    Formulario['Descrição detalhada'].Valor = "Nota explicativa: a justificativa há de ser clara, precisa e suficiente, sendo vedadas justificativas genéricas, incapazes de demonstrar de forma cabal a necessidade da BB Tecnologia e Serviços (BBTS). A justificativa deverá incluir: a) a necessidade da contratação; b) o quantitativo a ser contratado, que deve se pautar no histórico de utilização ou em dados demonstrativos da perspectiva futura da demanda. c) Para Licitação e Dispensa de Licitação por limite de valor (Art. 29, Inc. I e II da Lei 13.303/2016) ¿ Indicação de Pareceres Jurídico de caráter geral ou legislação aplicável relacionados ao tema."

    
#Pesquisa de Mercado
#Formulario['LABEL13'].Visivel = False
#Formulario['LABEL12'].Visivel = False
#Formulario['LABEL10'].Visivel = False
#Formulario['LABEL11'].Visivel = False
#Formulario['LISTA_ITENS_PESQ_MERC'].Visivel = False
#Formulario['DESCRICAO_OBRIG'].Visivel = False
#Formulario['CSC_VALOR1_A'].Visivel = False
#Formulario['OBS2'].Visivel = False
#Formulario['QUANTIDADE_ESTIMADA'].Visivel = False
#Formulario['POSSUI_DGCO'].Visivel = False
#Formulario['DESCRICAO_QUALIF'].Visivel = False
#Formulario['TIPO_DA_DEMANDA'].Visivel = False
#Formulario['OBS8'].Visivel = False
#Formulario['PAHL_VOUCHER_CARRO'].Visivel = False
#Formulario['ADITIVOS'].Visivel = False
#Formulario['CSC_DGCO'].Visivel = False
#Formulario['SERV_ART_29_LEI_13303'].Visivel = False
#Formulario['LABEL57'].Visivel = False
#Formulario['LABEL55'].Visivel = False
#Formulario['LABEL56'].Visivel = False
#Formulario['DESCRICAO_DETALHADA'].Visivel = False
#Formulario['OBSERVACAO'].Habilitado = False
#
#
#Formulario["QTD_PESQUISA"].Visivel = False
#Formulario["QTD_PESQUISA"].Habilitado = False
#Formulario["FORNECEDOR01"].Visivel = False
#Formulario["FORNECEDOR01"].Habilitado = False
#Formulario["PESQUISA_MERCADO1"].Visivel = False
#Formulario["PESQUISA_MERCADO1"].Habilitado = False
#Formulario["FORNECEDOR2"].Visivel = False
#Formulario["FORNECEDOR2"].Habilitado = False
#Formulario["PESQUISA_MERCADO2"].Visivel = False
#Formulario["PESQUISA_MERCADO2"].Habilitado = False
#Formulario["FORNECEDOR3"].Visivel = False
#Formulario["FORNECEDOR3"].Habilitado = False
#Formulario["PESQUISA_MERCADO3"].Visivel = False
#Formulario["PESQUISA_MERCADO3"].Habilitado = False
#Formulario["FORNECEDOR4"].Visivel = False
#Formulario["FORNECEDOR4"].Habilitado = False
#Formulario["PESQUISA_MERCADO4"].Visivel = False
#Formulario["PESQUISA_MERCADO4"].Habilitado = False
#Formulario["FORNECEDOR5"].Visivel = False
#Formulario["FORNECEDOR5"].Habilitado = False
#Formulario["PESQUISA_MERCADO_5"].Visivel = False
#Formulario["PESQUISA_MERCADO_5"].Habilitado = False
#Formulario["FORNECEDOR6"].Visivel = False
#Formulario["FORNECEDOR6"].Habilitado = False
#Formulario["PESQUISA_MERCADO6"].Visivel = False
#Formulario["PESQUISA_MERCADO6"].Habilitado = False
#
#Verifica a pergunta "Deseja que o Cesec faça a pesquisa de Mercado para o objeto"?
#if Formulario['SIM_NAO4'].Valor == "Não":
#   Formulario['PESQUISA_MERCADO'].Habilitado = True
#   Formulario['PESQUISA_MERCADO'].Visivel = True
#   Formulario['VALOR_DOD'].Habilitado = True
#   Formulario['VALOR_DOD'].Visivel = True
#   Formulario['VALOR_REFERENCIAL'].Visivel = True
#   Formulario['VALOR_REFERENCIAL'].Habilitado = True  
#   Formulario['SIM_NAO1'].Visivel = True
#   Formulario['SIM_NAO1'].Habilitado = True  
#   Formulario['APROVADOR_PB'].Visivel = True
#   Formulario['APROVADOR_PB'].Habilitado = True
#   Formulario['LABEL13'].Visivel = False
#   Formulario['LABEL12'].Visivel = False
#   Formulario['LABEL10'].Visivel = False
#   Formulario['LABEL11'].Visivel = False
#   Formulario['LISTA_ITENS_PESQ_MERC'].Visivel = False
#   Formulario['OBS2'].Visivel = False
#   Formulario['QUANTIDADE_ESTIMADA'].Visivel = False
#   Formulario['POSSUI_DGCO'].Visivel = False
#   Formulario['TIPO_DA_DEMANDA'].Visivel = False
#   Formulario['CSC_DGCO'].Visivel = False
#   Formulario['SERV_ART_29_LEI_13303'].Visivel = False
#   Formulario['LABEL57'].Visivel = False
#   Formulario['LABEL55'].Visivel = False
#   Formulario['LABEL56'].Visivel = False
#   Formulario['DESCRICAO_DETALHADA'].Visivel = False
#   
#if Formulario['SIM_NAO4'].Valor != "Não":
#   Formulario['PESQUISA_MERCADO'].Habilitado = False
#   Formulario['PESQUISA_MERCADO'].Visivel = False
#   Formulario['VALOR_DOD'].Habilitado = False
#   Formulario['VALOR_DOD'].Visivel = False
#   Formulario['VALOR_REFERENCIAL'].Visivel = False
#   Formulario['VALOR_REFERENCIAL'].Habilitado = False   
#   Formulario['SIM_NAO1'].Visivel = False
#   Formulario['SIM_NAO1'].Habilitado = False
#   Formulario['APROVADOR_PB'].Visivel = True
#   Formulario['APROVADOR_PB'].Habilitado = True
#   Formulario['LABEL13'].Visivel = True
#   Formulario['LABEL12'].Visivel = True
#   Formulario['LABEL10'].Visivel = True
#   Formulario['LABEL11'].Visivel = True
#   Formulario['LISTA_ITENS_PESQ_MERC'].Visivel = True
#   Formulario['OBS2'].Visivel = True
#   Formulario['QUANTIDADE_ESTIMADA'].Visivel = True
#   Formulario['POSSUI_DGCO'].Visivel = True
#   Formulario['TIPO_DA_DEMANDA'].Visivel = True
#   Formulario['CSC_DGCO'].Visivel = True
#   Formulario['SERV_ART_29_LEI_13303'].Visivel = True
#   Formulario['LABEL57'].Visivel = True
#   Formulario['LABEL55'].Visivel = True
#   Formulario['LABEL56'].Visivel = True
#   Formulario['DESCRICAO_DETALHADA'].Visivel = True
   
   
   

#Lista Gestor de itens
#Formulario["COMBOBOX"].Itens = "Insumos p/Operações;Marketing;Crédito Rotativo Peq. Gastos;Serv. Especializados - Gestão Financeira;Serv. Especializados - Gestão Jurídica;Treinamento;Serv. Especializados - Gestão de Pessoas;Uniformes;Manutenção Especializada;Imp.s/Apl.peças;Aplicação de Peças;Fretes;Serv. Especializados - Gestão de Negócios;Obsolescência de Estoques;Estoque (manutenção);Novos Negócios;Seguro Empresarial;Vigilância;Manut. e Conservação;Mat. Expediente;Copa/Periódicos;Equipamentos/Móveis/Utensílios;Serv. Especializados - Gestão de Apoio Administrativo;Benfeitorias;Instalações;Móveis e Utensílios;Máquinas e Equipamentos*;Anúncios e Editais;Serv. Telecom - Infra;Licenças de Software - Uso Infra TI;Licenças de Software - Uso Exclusivo Área;Serv. Telecom - Mensageria;Revenda de Software/Equip. De Ti;Serv. Especializados - Gestão de TI;Equip. Proc. Dados;Sist. Aplic. Software;Softwares desenvolvidos"



Formulario['DIRETORES'].Habilitado = False
Formulario['DIRETORES'].Visivel = False

Formulario['GEREX'].Habilitado = False
Formulario['GEREX'].Visivel = False

Formulario['DIRETORIA_GERENCIA'].Habilitado = False
Formulario['DIRETORIA_GERENCIA'].Visivel = False

Formulario['LOCALIDADE_MOV'].Habilitado = False
Formulario['LOCALIDADE_MOV'].Visivel = False

Formulario['PB_OBJETO_CONTRATACAO'].Habilitado = False
Formulario['PB_OBJETO_CONTRATACAO'].Visivel = False

Formulario['LABEL112'].Habilitado = False
Formulario['LABEL112'].Visivel = False

Formulario['LABEL113'].Habilitado = False
Formulario['LABEL113'].Visivel = False

Formulario['DescricaoDetalhada'].Habilitado = False
Formulario['DescricaoDetalhada'].Visivel = False

Formulario['UOR'].Habilitado = False
Formulario['UOR'].Visivel = False

Formulario['AREA_GESTORA_ITEM'].Habilitado = False
Formulario['AREA_GESTORA_ITEM'].Visivel = False

Formulario['DOTACAO1'].Habilitado = False
Formulario['DOTACAO1'].Visivel = False

Formulario['COMBOBOX10'].Habilitado = False
Formulario['COMBOBOX10'].Visivel = False

Formulario['CONTA_CONTABIL1'].Habilitado = False
Formulario['CONTA_CONTABIL1'].Visivel = False

Formulario['SIM_NAO'].Habilitado = False
Formulario['SIM_NAO'].Visivel = False

Formulario['SIM_NAO5'].Habilitado = False
Formulario['SIM_NAO5'].Visivel = False

Formulario['SIM_NAO7'].Habilitado = False
Formulario['SIM_NAO7'].Visivel = False

Formulario['APROVADOR_PB'].Habilitado = False
Formulario['APROVADOR_PB'].Visivel = False

Formulario['OBS21'].Habilitado = False
Formulario['OBS21'].Visivel = False

Formulario['LABEL1'].Habilitado = False
Formulario['LABEL1'].Visivel = False

Formulario['OBS22'].Habilitado = False
Formulario['OBS22'].Visivel = False

Formulario['OBS23'].Habilitado = False
Formulario['OBS23'].Visivel = False

Formulario['OBS10'].Habilitado = False
Formulario['OBS10'].Visivel = False

Formulario['OBS22'].Habilitado = False
Formulario['OBS22'].Visivel = False

Formulario['OBS7'].Habilitado = False
Formulario['OBS7'].Visivel = False

Formulario['INFORMACAO_FATURAMENTO'].Habilitado = False
Formulario['INFORMACAO_FATURAMENTO'].Visivel = False

Formulario['OBS3'].Habilitado = False
Formulario['OBS3'].Visivel = False

Formulario['NN_CONDICAO_PAGAMENTO'].Habilitado = False
Formulario['NN_CONDICAO_PAGAMENTO'].Visivel = False

Formulario['OBS5'].Habilitado = False
Formulario['OBS5'].Visivel = False

Formulario['OBS50'].Habilitado = False
Formulario['OBS50'].Visivel = False

Formulario['OBS4'].Habilitado = False
Formulario['OBS4'].Visivel = False

Formulario['SIM_NAO6'].Habilitado = False
Formulario['SIM_NAO6'].Visivel = False

Formulario['CSC_DGCO'].Habilitado = False
Formulario['CSC_DGCO'].Visivel = False

Formulario['PENF_EMAIL'].Habilitado = False
Formulario['PENF_EMAIL'].Visivel = False


Formulario['DOCUMENTOS DE INEXIGIBILIDADE'].Visivel = False
Formulario['DOCS1'].Visivel = False
Formulario['DOCS2'].Visivel = False

Formulario['LABEL2'].Visivel = False
Formulario["LABEL2"].Valor = "<h4 style='color: red;'><strong>Atenção!</strong> Identificamos que a sua contratação não se enquadra em PBe. Gentileza abrir chamado no: SISCCON <a target='_blank' href= https://sisccon.bbts.com.br>sisccon.bbts.com.br</a> ."

campos_formulario = ['DIRETORES', 'GEREX', 'DIRETORIA_GERENCIA', 'LOCALIDADE_MOV', 'PB_OBJETO_CONTRATACAO', 'LABEL112', 'LABEL113','DescricaoDetalhada', 'UOR', 'AREA_GESTORA_ITEM', 'DOTACAO1', 'COMBOBOX10', 'CONTA_CONTABIL1', 'SIM_NAO', 'SIM_NAO5', 'SIM_NAO7', 'APROVADOR_PB','OBS21', 'LABEL1', 'OBS22', 'OBS23', 'OBS10', 'OBS7', 'INFORMACAO_FATURAMENTO', 'OBS3', 'NN_CONDICAO_PAGAMENTO', 'OBS4',  'SIM_NAO6', 'CSC_DGCO', 'PENF_EMAIL', 'DOCUMENTOS DE INEXIGIBILIDADE', 'DOCS1', 'DOCS2', 'CHECKBOX9']

# Aplicando a visibilidade e habilitação nos campos

for campo in campos_formulario:
    Formulario[campo].Habilitado = True
    Formulario[campo].Visivel = True

    
Formulario['AREA_GESTORA_ITEM'].Habilitado = False
Formulario['AREA_GESTORA_ITEM'].Visivel = False
Formulario['LABEL101'].Habilitado = False
Formulario['LABEL101'].Visivel = False
Formulario['CSC_DGCO'].Habilitado = False
Formulario['CSC_DGCO'].Visivel = False

Formulario['TEXT'].Habilitado = False
Formulario['TEXT'].Visivel = False

Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = False


if Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Benfeitorias" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Equipamentos/Móveis/Utensílios" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Instalações" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Manut. e Conservação" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Máq. Equipamentos" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Mat. Expediente" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Móveis e utensílios":
    
    Formulario['SIM_NAO20'].Valor = "Sim"

else:
    Formulario['SIM_NAO20'].Valor = "Não"
```
- Operação PR0001 Preencher Campos
  - APROVADOR_PB "Aprovadores da contratação conforme NI006 (Comitê da Superintendência ou Gerência Executiva. Informe o Gerente Executivo no campo acima, se houver)." [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório — PosicaoRotulo=Topo
    - coluna APROVADORES obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Anexo I -  Espeficiações Técnicas
  - OBS21 "2. Especificações Técnicas (para aquisição de produtos eletrônicos, informar a voltgem desejada)." [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - LABEL1 "ATENÇÃO: O campo "2. Especificações Técnicas" tem o limite de 4000 caracteres. Caso o limite de caracteres não seja o suficiente, utilize os campos abaixo para complementar a informação." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - OBS22 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS22]
  - OBS23 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS23]
  - OBS10 "3. Qualificação Técnica " [Memo String(2000) → CPE_CSC.OBS10] obrigatório
  - OBS4 "4. Condições de Entrega" [Memo String(2000) → CPE_CONTRATOS.OBS4] obrigatório
  - OBS7 "Condições de Entrega - Continuação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS7]
  - INFORMACAO_FATURAMENTO "5. Informações para Faturamento: (Incluir os dados da BBTS para o qual será faturado o objeto da contratação - Endereço completo com CEP)" [DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; PosicaoRotulo=Topo
    - coluna ENDERECO_COM_CEP obrigatório
    - coluna ENDERECO obrigatório
    - coluna CNPJ_BBTS obrigatório
    - coluna INSCRICAO_ESTADUAL obrigatório
    - coluna INSCRICAO_MUNICIIPAL obrigatório
  - OBS3 "6. Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico:" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - NN_CONDICAO_PAGAMENTO "7. Condições de Pagamento:" [Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO] obrigatório
  - OBS5 "8. Multa:" [Memo String(2000) → CPE_CONTRATOS.OBS5] obrigatório
  - OBS50 "9. Privacidade , Proteção e Tratamento de Dados Pessoais:" [Memo String(2000) → CPE_CONTRATOS.OBS50] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=DOCS1
  - anexo "Anexo Complementar as Especificações Técnicas" classes: Especificação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais para a Pesquisa de Mercado
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar 'Não se aplica'. (Sugere-se, preferencialmente, utilizar o método estatístico de média ou mediana)" [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
**TIPO_DE_VALOR_DE_REFERENCIA.ScriptModificado**
```python
if Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Valor == 'Outros:':
    Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = True
    Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True
    
if Formulario["TIPO_DE_VALOR_DE_REFERENCIA"].Valor != 'Outros:':
    Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = False
#   Formulario["JUSTIFICATIVA_IMPACTO"].Habilitado = True

#Lembrete de referencial escolhido

if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Maior Preço":
    Formulario.ExibeMensagem("Lembrete: \n\nMétodo estatístico de 'Maior Preço' prejudicial á BBTS. Somente aceito com Nota Técnica anexa com 'de acordo' da Gesuc, com fundamentação da necessidade.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Não se aplica":
    Formulario.ExibeMensagem("Lembrete: \n\nMétodo estatístico 'Não se aplica' informado somente em Inexigibilidade de Licitação (inviabilidade de competição); com todos os insumos da TAB415-001 anexados.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Outros:":
    Formulario.ExibeMensagem("Lembrete: \n\nSe ultilizado método estatístico diferente dos convencionais (Média, Mediana ou Menor Valor) é obrigatório informar detalhadamente abaixo o 'Método estatístico utilizado (Valor Referencial)', com critérios fundamentados.")
    
if Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Valor == "Menor Preço":
    Formulario.ExibeMensagem("Lembrete: \n\nSugere-se, preferencialmente, utilizar o método estatístico de Média ou Mediana. Este item estipula o valor referencial para a aprovação do orçamento (até quanto poderá ser gasto); não o critério de escolha do fornecedor, informado no item abaixo 'Justificativa da escolha do(s) fornecedor(es)' de padrão como 'Melhor/Menor Preço.'.")
```
  - JUSTIFICATIVA_IMPACTO "Informe detalhadamente o método estatístico utilizado (Valor Referencial)." [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario['SIM_NAO1'].Valor == "Não":
   Formulario['OBS6'].Habilitado = True
   Formulario['OBS6'].Visivel = True
else:
   Formulario['OBS6'].Habilitado = False
   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184.000,00?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79.000,00?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
  - CSC_DGCO "Informar para quantas regiões é esta demanda:" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório
  - PENF_EMAIL "E-mails que serão notificados sobre o andamento da ordem de serviço (separados por ponto e vírgula)" [TextBox String(2000) → CPE_PENF.PENF_EMAIL] obrigatório
  - CHECKBOX9 "Confirmo que revisei os campos do "Anexo I - Especificações Técnicas", editando os textos pré-preenchidos e retirando as NOTAS EXPLICATIVAS de orientação. Tais campos têm classificação de informação #pública, pois são as orientações e condições repassadas para o fornecedor quando em cotação e na contratação no final do processo. Os demais campos, apesar de serem classificação #interna, devem ser preenchidos adequadamente, pois refletem no documento final de PBe." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX9] obrigatório
  - LABEL30 "LABEL30" [Label String(700) → CPE_PDCI2019.LABEL30] obrigatório
  - LABEL31 "LABEL31" [Label String → CPE_PDCI2019.LABEL31] obrigatório
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. Caso tenha o mínimo de três propostas validas informe `Não se aplica¿." [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - SIM_NAO6 "Há pesquisa de mercado prévia? Se sim, favor anexar. Caso selecione 'Não', automaticamente será criado um subprocesso 'Pesquisa de Mercado' para cotação." [DropDownList String → CPE_CSC.SIM_NAO6] obrigatório
**SIM_NAO6.ScriptModificado**
```python
if Formulario['SIM_NAO6'].Valor == "Sim":
   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = False
   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = False
   Formulario['JUSTIFICATIVA_IMAGEM'].Habilitado = True
   Formulario['JUSTIFICATIVA_IMAGEM'].Visivel = True
   Formulario['JUSTIFICATIVA_TENDENCIA'].Habilitado = True
   Formulario['JUSTIFICATIVA_TENDENCIA'].Visivel = True
   Formulario['FQ415_066_ITEM31'].Habilitado = True
   Formulario['FQ415_066_ITEM31'].Visivel = True
   Formulario['FQ415_066_ITEM32'].Habilitado = True
   Formulario['FQ415_066_ITEM32'].Visivel = True
   Formulario['FQ415_066_ITEM321'].Habilitado = True
   Formulario['FQ415_066_ITEM321'].Visivel = True
   Formulario['FQ415_066_ITEM322'].Habilitado = True
   Formulario['FQ415_066_ITEM322'].Visivel = True
   Formulario['FQ415_066_ITEM33'].Habilitado = True
   Formulario['FQ415_066_ITEM33'].Visivel = True
   Formulario['FQ415_066_ITEM331'].Habilitado = True
   Formulario['FQ415_066_ITEM331'].Visivel = True
   Formulario['SIM_NAO1'].Habilitado = True
   Formulario['SIM_NAO1'].Visivel = True
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Habilitado = True
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Visivel = True
   

if Formulario['SIM_NAO6'].Valor != "Sim":
   Formulario['JUSTIFICATIVA_IMPACTO'].Habilitado = False
   Formulario['JUSTIFICATIVA_IMPACTO'].Visivel = False
   Formulario['JUSTIFICATIVA_IMAGEM'].Habilitado = False
   Formulario['JUSTIFICATIVA_IMAGEM'].Visivel = False
   Formulario['JUSTIFICATIVA_TENDENCIA'].Habilitado = False
   Formulario['JUSTIFICATIVA_TENDENCIA'].Visivel = False
   Formulario['FQ415_066_ITEM31'].Habilitado = False
   Formulario['FQ415_066_ITEM31'].Visivel = False
   Formulario['FQ415_066_ITEM32'].Habilitado = False
   Formulario['FQ415_066_ITEM32'].Visivel = False
   Formulario['FQ415_066_ITEM321'].Habilitado = False
   Formulario['FQ415_066_ITEM321'].Visivel = False
   Formulario['FQ415_066_ITEM322'].Habilitado = False
   Formulario['FQ415_066_ITEM322'].Visivel = False
   Formulario['FQ415_066_ITEM33'].Habilitado = False
   Formulario['FQ415_066_ITEM33'].Visivel = False
   Formulario['FQ415_066_ITEM331'].Habilitado = False
   Formulario['FQ415_066_ITEM331'].Visivel = False
   Formulario['SIM_NAO1'].Habilitado = False
   Formulario['SIM_NAO1'].Visivel = False
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Habilitado = False
   Formulario['TIPO_DE_VALOR_DE_REFERENCIA'].Visivel = False
```
- Operação PR0004 Associar Itens Configuração: Nome=DOCS2
  - anexo "Pesquisa de Mercado Prévia (Propostas conforme PRO417-002 e FQ415-068; Exemplo: Devem ser em formato PDF com CNPJ, descrição completa, preço unitário, subtotal e total, condição de pagamento pós-pago com no mínimo 10 dias após emissão de NF (faturado 10 DDL), prazo de entrega com frete (CIF) - não destacado por conta do fornecedor, impostos (inclusos), garantia, validade e telefone/e-mail de contato do fornecedor.) " classes: Pesquisa de Mercado — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS DE INEXIGIBILIDADE
  - anexo "" classes: Cartão CNPJ — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Apólice de Seguro – Serviço de Transporte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: QSA - Quadro de Sócios e Administradores — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Comprovação de razoabilidade de preço — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Certidão CNJ — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: CND Federal — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Consulta Consolidada TCU — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Comprovante de exclusividade — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: CND FGTS — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Parecer Jurídico Específico — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "Demais Documentos (conforme TAB 415-001)" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Nota Técnica — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Rateio Localidades — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Projeto Básico
  - SIM_NAO201 "Trata-se de Compra/Contratação de bens e serviços de valor superior ao limite da dispensa, (Art. 29,
Inc I e II da Lei 13.303/2016)?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO201] obrigatório
**SIM_NAO201.ScriptModificado**
```python
# VERIFICA SE ALGUM DOS CAMPOS FOI MARCADO COM ¿SIM¿. CASO VERDADEIRO, HABILITA O CAMPO `LABEL2¿, QUE EXPLICA QUE A DEMANDA NÃO ATENDE AO FLUXO. E ENCAMINHA O CLIENTE PARA O FLUXO CORRETO.

campo1 = Formulario['SIM_NAO201'].Valor.ToString() if Formulario['SIM_NAO201'].Valor is not None else None
campo2 = Formulario['SIM_NAO202'].Valor.ToString() if Formulario['SIM_NAO202'].Valor is not None else None
campo3 = Formulario['SIM_NAO203'].Valor.ToString() if Formulario['SIM_NAO203'].Valor is not None else None


if campo1 is not None and campo2 is not None and campo3 is not None:
    campos = [campo1, campo2, campo3]

    if any(campo == 'Sim' for campo in campos):   # Se todos forem 'Não'
        Formulario.ExibeMensagem("ATENÇÃO:\n\nIdentificamos que a sua contratação não se enquadra em PBe. \nGentileza abrir chamado no: SISCCON <https://sisccon.bbts.com.br>.")
        Formulario['LABEL2'].Visivel = True
```
  - SIM_NAO202 "Trata-se de Compra/Contratação de bens e serviços com obrigação futura e contratação de serviços de natureza contínua?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO202] obrigatório
**SIM_NAO202.ScriptModificado**
```python
# VERIFICA SE ALGUM DOS CAMPOS FOI MARCADO COM ¿SIM¿. CASO VERDADEIRO, HABILITA O CAMPO `LABEL2¿, QUE EXPLICA QUE A DEMANDA NÃO ATENDE AO FLUXO. E ENCAMINHA O CLIENTE PARA O FLUXO CORRETO.

campo1 = Formulario['SIM_NAO201'].Valor.ToString() if Formulario['SIM_NAO201'].Valor is not None else None
campo2 = Formulario['SIM_NAO202'].Valor.ToString() if Formulario['SIM_NAO202'].Valor is not None else None
campo3 = Formulario['SIM_NAO203'].Valor.ToString() if Formulario['SIM_NAO203'].Valor is not None else None


if campo1 is not None and campo2 is not None and campo3 is not None:
    campos = [campo1, campo2, campo3]

    if any(campo == 'Sim' for campo in campos):   # Se todos forem 'Não'
        Formulario.ExibeMensagem("ATENÇÃO:\n\nIdentificamos que a sua contratação não se enquadra em PBe. \nGentileza abrir chamado no: SISCCON <https://sisccon.bbts.com.br>")
        Formulario['LABEL2'].Visivel = True
```
  - SIM_NAO203 "Trata-se de Contratação de obras e serviços de engenharia de valor superior a R$ 184.000,00?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO203] obrigatório
**SIM_NAO203.ScriptModificado**
```python
#  VERIFICA SE ALGUM DOS CAMPOS FOI MARCADO COM ¿SIM¿. CASO VERDADEIRO, HABILITA O CAMPO `LABEL2¿, QUE EXPLICA QUE A DEMANDA NÃO ATENDE AO FLUXO. E ENCAMINHA O CLIENTE PARA O FLUXO CORRETO.

campo1 = Formulario['SIM_NAO201'].Valor.ToString() if Formulario['SIM_NAO201'].Valor is not None else None
campo2 = Formulario['SIM_NAO202'].Valor.ToString() if Formulario['SIM_NAO202'].Valor is not None else None
campo3 = Formulario['SIM_NAO203'].Valor.ToString() if Formulario['SIM_NAO203'].Valor is not None else None


if campo1 is not None and campo2 is not None and campo3 is not None:
    campos = [campo1, campo2, campo3]

    if any(campo == 'Sim' for campo in campos):   # Se todos forem 'Não'
        Formulario.ExibeMensagem("ATENÇÃO:\n\nIdentificamos que a sua contratação não se enquadra em PBe. \nGentileza abrir chamado no: SISCCON <https://sisccon.bbts.com.br>")
        Formulario['LABEL2'].Visivel = True
```
  - LABEL2 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2]
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX
if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None




#----- Consulta GEREX

#if Formulario["DIRETORES"].Valor != None:
#    if Formulario["DIRETORES"].Valor != "933":
#        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#    else:
#        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - DIRETORIA_GERENCIA "Área Técnica (quando couber)" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
  - LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] obrigatório
  - PB_OBJETO_CONTRATACAO "1. Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
    - coluna NOTA_FISCAL obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna PATRIMONIO obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
  - LABEL112 "<b style="color: red">Orientações para preenchimento do Campo Justificativa da Contratação: Nota explicativa: a justificativa há de ser clara, precisa e suficiente, sendo vedadas justificativas genéricas, incapazes de demonstrar de forma cabal a necessidade da BB Tecnologia e Serviços (BBTS).</b>" [Label String(500) → CPE_CONTRATOS.LABEL112] obrigatório
  - LABEL113 "<b style="color: red">A justificativa deverá incluir: a) a necessidade da contratação; b) o quantitativo a ser contratado, que deve se pautar no histórico de utilização ou em dados demonstrativos da perspectiva futura da demanda. c) Para Licitação e Dispensa de Licitação por limite de valor (Art. 29, Inc. I e II da Lei 13.303/2016) ¿ Indicação de Pareceres Jurídico de caráter geral ou legislação aplicável relacionados ao tema.</b>" [Label String(1000) → CPE_CONTRATOS02.LABEL113] obrigatório
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
  - UOR "Informe a(s) UOR(s) de alocação de Despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório — PosicaoRotulo=Topo
    - coluna UOR
  - AREA_GESTORA_ITEM "A área demandante é a área gestora do item? (Conforme TAB208-001)" [DropDownList String → CPE_CONTRATOS.AREA_GESTORA_ITEM] obrigatório
**AREA_GESTORA_ITEM.ScriptModificado**
```python
if Formulario["AREA_GESTORA_ITEM"].Valor == "Sim":
    #OrdemServico.PossuiItem('COMPROVANTE').Visivel = False
    Formulario["LABEL101"].Visivel = False
    Formulario["LABEL101"].Habilitado = False

if Formulario["AREA_GESTORA_ITEM"].Valor == "Não (Item Orçamentário Descentralizado)":
    #OrdemServico.PossuiItem('COMPROVANTE').Visivel = False
    Formulario["LABEL101"].Visivel = False
    Formulario["LABEL101"].Habilitado = False    

if Formulario["AREA_GESTORA_ITEM"].Valor == "Não (Item Orçamentário Centralizado)":
    #Formulario['COMPROVANTE'].Visivel = True
    Formulario["LABEL101"].Visivel = True
    Formulario["LABEL101"].Habilitado = False
```
  - LABEL101 "<b style="color: red">Obrigatório anexar o documento Remanejamento Orçamentário (Ex: Ordem de Serviço, E-mail ou "De acordo" do Gestor da UOR a ser debitada).</b>" [Label String(1300) → CPE_HOMOLOGACAO.LABEL101]
  - DOTACAO1 "Dotação Orçamentária (opcional)" [TextBox String → CPE_CONTRATOS.DOTACAO1]
  - COMBOBOX10 "Natureza Contábil" [DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10] obrigatório
  - GESTOR_DE_ITENS_GESAP "Informe o item orçamentário (TAB208-001). No caso de itens centralizados, é necessário consultar previamente a área gestora, pois poderá haver encaminhamento para aprovação neste chamado." [DropDownList String(2000) → CPE_CONTRATOS02.GESTOR_DE_ITENS_GESAP] obrigatório
**GESTOR_DE_ITENS_GESAP.ScriptModificado**
```python
if Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Benfeitorias" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Equipamentos/Móveis/Utensílios" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Instalações" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Manut. e Conservação" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Máq. Equipamentos" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Mat. Expediente" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Móveis e utensílios":
    
    Formulario['SIM_NAO20'].Valor = "Sim"

else:
    Formulario['SIM_NAO20'].Valor = "Não"
```
  - SIM_NAO20 "Aprovação Gesap" [DropDownList String → CPE_CONTRATOS02.SIM_NAO20]
**SIM_NAO20.ScriptModificado**
```python
if Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Benfeitorias" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Equipamentos/Móveis/Utensílios" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Instalações" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Manut. e Conservação" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Máq. Equipamentos" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Mat. Expediente" or \
   Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Móveis e utensílios":
    
    Formulario['SIM_NAO20'].Valor = "Sim"

else:
    Formulario['SIM_NAO20'].Valor = "Não"
```
  - CONTA_CONTABIL1 "Conta Contábil (Não obrigatório) - A informação será validada pela Contabilidade" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1]
  - TIPO_ATIVIDADE "Classificação da atividade" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
  - DATA_ENTREGA "Data da necessidade" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENTREGA] obrigatório
  - CSC_CPF "Caso haja contrato com cliente decorrente de atividade fim, informar o DGCO do cliente" [TextBox String(300) → CPE_CSC.CSC_CPF]
  - SIM_NAO "É contratação de TIC? " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
#if Formulario['SIM_NAO'].Valor == "Sim":
#   Formulario['SIM_NAO5'].Habilitado = True
#   Formulario['SIM_NAO5'].Visivel = True
#
#if Formulario['SIM_NAO'].Valor != "Sim":
#    Formulario['SIM_NAO5'].Habilitado = False
#    Formulario['SIM_NAO5'].Visivel = False
```
  - SIM_NAO5 "Aplica-se os artefatos da NI642?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
  - SIM_NAO10 "Possui itens que utilizaram logo e/ou marca BBTS?" [DropDownList String → CPE_CSC.SIM_NAO10] obrigatório
**SIM_NAO10.ScriptModificado**
```python
if Formulario['SIM_NAO10'].Valor == "Sim":
    Formulario.ExibeMensagem("Lembrete: \n\nNecessário anexar a 'Arte' para o(s) produto(s) a ser(em) adquirido(s) conforme catálogo ou especificações enviadas pela Gemac.")
#    Formulario["TEXT"].Visivel = True
#    Formulario["TEXT"].Habilitado = True
#
#if Formulario['SIM_NAO10'].Valor == "Não":
#    Formulario["TEXT"].Visivel = False
#    Formulario["TEXT"].Habilitado = False
```
  - TEXT "Número O.S. (Remanejamento Orçamentário) - Informe N/A se for a própria Gemac a Área Cliente." [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
  - SIM_NAO_100 "De acordo com o objeto da contratação se trata de:
 " [DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100] obrigatório
  - SIM_NAO7 "Solicitar aprovação do Gerente Executivo?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
**SIM_NAO7.ScriptModificado**
```python
if Formulario['SIM_NAO7'].Valor == "Não":
   Formulario['PPGEREX_NEGOCIO'].Habilitado = False
   Formulario['PPGEREX_NEGOCIO'].Visivel = False

if Formulario['SIM_NAO7'].Valor != "Não":
    Formulario['PPGEREX_NEGOCIO'].Habilitado = True
    Formulario['PPGEREX_NEGOCIO'].Visivel = True
```
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO]
  - SIM_NAO4 "Trata-se de demanda para atender atividade fim?" [DropDownList String → CPE_CSC.SIM_NAO4] obrigatório
    - coluna NOME_CLIENTE obrigatório
    - coluna RUBRICA
    - coluna VALOR obrigatório
    - coluna DGCO obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366273] EventoIntermediarioMensagem "Aviso de cancelamento por reprovação da Diage"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Aviso de cancelamento por reprovação da Diage"  # ajuste conforme a etapa do seu evento


idCliente = 0
nomeCliente = ''

try:
    idCliente = OrdemServico.Cliente.Id.ToString()
    dt = Utils.ExecuteDataTable("SELECT P.NOME FROM PESSOA P INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA WHERE CP.ID_PESSOA = '" + idResp + "'")
    nomeCliente = None
    for r in dt.Rows:
        nomeCliente = r["NOME"]
        break
except:
    nomeCliente = None

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = nomeCliente  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}




ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366274] EventoIntermediarioMensagem "Conferir PBe para envio de aprovação"
Config: ListaDestinatarios=cesec.comp@bbts.com.br
ModeloComunicado: Projeto Básico - Informações Gefic
Corpo do comunicado: Prezado(a),
Foram inseridas no projeto básico as informações de conta contábil e conta orçamentária.
Verifique o código do item e envie a Ordem de Serviço para aprovação do projeto básico.
Para maiores informações, Link.Edicao .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from Venki.Supravizio.Processo.Custom import Aprovador
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = OrdemServico.Numero.ToString()

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = u"Conferir itens, Pareceres e Aprovadores"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "cesec.comp@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": destinatario
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    pass
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366275] Tarefa "Verificar Reprovação
 Gerencial (Cliente)"
Responsável: Cliente (papel 18)
Config: PermiteCancelamentoAA=true; RotuloBotaoAvancar=Avançar (submeter aprovação Gerencial novamente)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.ModificaCampoFormularioVisivel('UOR', True)



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Verificar Reprovação Gerencial (Cliente)'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

OrdemServico.Salva()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Verificar Reprovação Gerencial (Cliente)'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
Formulario["SIM_NAO1"].Visivel = True
Formulario["SIM_NAO1"].Habilitado = True
Formulario["OBS6"].Visivel = True
Formulario["OBS6"].Habilitado = True
Formulario["PB_OBJETO_CONTRATACAO"].Visivel = True
Formulario["PB_OBJETO_CONTRATACAO"].Habilitado = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Projeto Básico
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX

if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - DIRETORIA_GERENCIA "Área Técnica (quando couber)" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
  - LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] obrigatório
  - PB_OBJETO_CONTRATACAO "1. Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna PATRIMONIO obrigatório
    - coluna NOTA_FISCAL obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
  - TIPO_ATIVIDADE "Classificação da Atividade" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
   Formulario['LABEL6'].Habilitado = True
   Formulario['LABEL6'].Visivel = True
   

if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
    Formulario['LABEL6'].Habilitado = False
    Formulario['LABEL6'].Visivel = False
```
  - LABEL6 "(Preencher se for contrato com FORNECEDOR para ATIVIDADE FIM) Citar todos os contratos de clientes no qual o serviço a ser contratado detém uma vinculação direta e indireta." [Label String(1500) → CPE_PDCI2019.LABEL6]
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
  - SIM_NAO "É contratação de Tic? " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
#if Formulario['SIM_NAO'].Valor == "Sim":
#   Formulario['SIM_NAO5'].Habilitado = True
#   Formulario['SIM_NAO5'].Visivel = True

#if Formulario['SIM_NAO'].Valor != "Sim":
#    Formulario['SIM_NAO5'].Habilitado = False
#    Formulario['SIM_NAO5'].Visivel = False
```
  - SIM_NAO5 "Aplica-se os artefatos da NI642?" [DropDownList String → CPE_CSC.SIM_NAO5]
  - COMBOBOX10 "Natureza Contábil" [DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentos adicionais para aprovação (opcional)" classes: Justificativa — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Anexo I -  Espeficiações Técnicas
  - OBS21 "2. Especificações Técnicas" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - LABEL1 "ATENÇÃO: O campo "2. Especificações Técnicas" tem o limite de 4000 caracteres. Caso o limite de caracteres não seja o suficiente, utilize os campos abaixo para complementar a informação." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - OBS50 "9. Privacidade , Proteção e Tratamento de Dados Pessoais" [Memo String(2000) → CPE_CONTRATOS.OBS50] obrigatório
  - OBS4 "4. Condições de Entrega" [Memo String(2000) → CPE_CONTRATOS.OBS4] obrigatório
  - OBS7 "Condições de Entrega - Continuação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS7]
  - OBS22 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS22]
  - OBS23 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS23]
  - OBS10 "3. Qualificação Técnica" [Memo String(2000) → CPE_CSC.OBS10] obrigatório
  - OBS5 "8. Multa" [Memo String(2000) → CPE_CONTRATOS.OBS5] obrigatório
  - INFORMACAO_FATURAMENTO "5. Informações para Faturamento: (Incluir os dados da BBTS para o qual será faturado o objeto da contratação)" [DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; PosicaoRotulo=Topo
    - coluna CNPJ_BBTS
    - coluna INSCRICAO_ESTADUAL
    - coluna INSCRICAO_MUNICIIPAL
    - coluna ENDERECO_COM_CEP obrigatório
    - coluna ENDERECO obrigatório
  - OBS3 "6. Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico:" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - NN_CONDICAO_PAGAMENTO "7. Condições de Pagamento:" [Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO] obrigatório
- Operação PR0001 Preencher Campos
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO]
  - APROVADOR_PB "Aprovadores da contratação conforme NI006 (Somente Funções Gerenciais)" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório
    - coluna APROVADORES obrigatório
  - SIM_NAO7 "Solicitar aprovação do Gerente Executivo?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informação!
  - LABEL25 "Caso o comitê gerencial decida não seguir com a aquisição ou contratação nesta etapa, o próprio solicitante pode cancelar o chamado. Acesse a Central de Serviços (https://santacruz.bbts.com.br/Supravizio/Portal/Classico/Inicial.aspx), entre na aba "Consulta", selecione e entre no chamado desejado e clique no botão "Cancelar"; informe o motivo e clique em "Confirmar"." [Label String(1000) → CPE_PDCI2019.LABEL25] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais da Pesquisa de Mercado
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184 Mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar ''Não se aplica''." [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
  - JUSTIFICATIVA_IMPACTO "Justificativa 1 (Metodologia aplicada em caso de valor referencial escolhido "Outros")" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79 mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. " [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
#if Formulario['SIM_NAO1'].Valor == "Não":
#   Formulario['OBS6'].Habilitado = True
#   Formulario['OBS6'].Visivel = True
   
#if Formulario['SIM_NAO1'].Valor != "Sim":
#   Formulario['OBS6'].Habilitado = False
#   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informe os ajustes realizados para nova aprovação
  - TEXT2 "Ajustes realizados pela área cliente:" [TextBox String → CPE_CSC.TEXT2] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366276] Tarefa "Ajustar reprovação Gemac (Cliente)"
Responsável: Cliente (papel 18)
Config: PermiteCancelamentoAA=true; RotuloBotaoAvancar=Avançar (Enviar para Cesec)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Ajustar reprovação Gemac (Cliente)'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
resp = DB.ExecuteDataTable(
    "SELECT PESSOA.NOME, OCORRENCIA.ASSUNTO, OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO "
    "FROM PESSOA "
    "INNER JOIN OCORRENCIA ON OCORRENCIA.ID_RESPONSAVEL = PESSOA.ID_PESSOA "
    "WHERE OCORRENCIA.NUMERO = '" + OrdemServico.Numero + "' "
    "FETCH FIRST 1 ROWS ONLY"
)

responsavel = ""
for row in resp.Rows:
    responsavel = (row["NOME"] or "").ToString().Trim()
    break



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
        OrdemServico.AdicionaComentario(
            "Resposta da API (Erro HTTP {}): {}".format(int(response.Result.StatusCode), errText),
            True
        )
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Ajustar reprovação Gemac (Cliente)'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
Formulario["VALOR_REFERENCIAL"].Habilitado = False
Formulario["CODIGO_ITEM"].Habilitado = False
Formulario['CSC_ESCOLARIDADE'].Visivel = True
```
- Operação PR0001 Preencher Campos
  - PB_OBJETO_CONTRATACAO "Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
- Operação PR0001 Preencher Campos
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM]
    - coluna NECESSIDADE obrigatório
    - coluna ITEM_OBSOLETO obrigatório
    - coluna ITEM obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL]
    - coluna ITEM1 obrigatório
    - coluna VALOR_TOTAL
    - coluna VALOR_REFERENCIAL obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM
  - UOR "Informe a(s) UOR(s) de alocação de despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR]
    - coluna UOR obrigatório
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário (informar Ordem de Serviço) e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica".)" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE] obrigatório
**CSC_ESCOLARIDADE.ScriptModificado**
```python
OrdemServico.Salva()
```
  - OBS24 "Ações tomadas sobre a reprovação da Gemac" [Memo String(2000) → CPE_CSC.OBS24] obrigatório
  - PB_OBJETO_CONTRATACAO "Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS GEMAC2
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true

### [366277] EventoIntermediarioMensagem "Aviso de cancelamento de chamado por falta de ajustes"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Reprovação por falta de ajustes
Corpo do comunicado: Prezado(a),
A Ordem de Serviço OrdemServico.Numero foi cancelado automaticamente por falta de ajustes.
Para realizar este serviço abra uma nova solicitação.
Para maiores informações Link.Consulta.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Efetuar correções (Insumos)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Gerente Posição"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366278] Tarefa "Cancela aprovação cliente"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.CancelaAprovacao("APROVACAO_CLIENTE")


import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Cancela aprovação cliente'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Cancela aprovação cliente'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```

### [366279] Tarefa "Aguardar aprovação Gesap"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Aguardar aprovação Gesap'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'


url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Aguardar aprovação Gesap'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar utilização de rubrica da Gesap (Diage)
  - (aprovação) GESTOR_DE_ITENS_GESAP "Gestor de Itens Gesap" [DropDownList String(2000) → CPE_CONTRATOS02.GESTOR_DE_ITENS_GESAP] — PermiteModificarAprovado=true
  - (aprovação) PB_OBJETO_CONTRATACAO "Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] — PermiteModificarAprovado=true
  - (aprovação) DescricaoDetalhada (nativo) "Justificativa da Contratação" — PermiteModificarAprovado=true
  - (aprovação) LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] — PermiteModificarAprovado=true
  - aprovador: Gerente Divisão Gesap (Unico)

### [366280] EventoIntermediarioMensagem "Aprovação"
Destinatário: Cliente e Responsavel Atual (papel 544)
Config: ListaDestinatarios=cesec.comp@bbts.com.br;rony.baldoino@bbts.com.br
ModeloComunicado: Projeto Básico - Aprovação
Corpo do comunicado: Prezado(a) Cesec,
O projeto básico foi aprovado.
Acesse a ordem de serviço e unifique os documentos.
Para maiores informações, Link.Edicao .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12))
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = OrdemServico.Numero.ToString()

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = u"Recolhe aprovações e outras informações para preenchimento do relatório"  # ajuste conforme a etapa do seu evento

destinatario = u"Cliente e Responsável Atual"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": destinatario
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366281] Tarefa "Preencher dados para cadastro de itens"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Preencher dados para cadastro de itens'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Preencher dados para cadastro de itens'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
#Formulario['PRJ_CODIGO_ITENS'].Visivel = False
#Formulario['PRJ_CODIGO_ITEM'].Visivel = False
#Formulario['PRJ_DESC_ITEM'].Visivel = False
#Formulario['PRJ_UNI_MEDIDA'].Visivel = False
#Formulario['PRJ_CATEGORIA_NCM'].Visivel = False
#Formulario['Justificativa'].Visivel = False
#Formulario['PRJ_OBS'].Visivel = False
#Formulario['PRJ_ALIQUOTA'].Visivel = False
#Formulario['LABEL1'].Visivel = False

#Formulario["Assunto"].Valor = OrdemServico.Servico.Descricao
#Formulario["Assunto"].Habilitado = False
#
cliente = OrdemServico.Cliente.UsuarioRede
area= OrdemServico.Cliente.Orgao.Descricao
local = "RJ"
#Formulario["PRJ_SRC_USUARIO"].Valor = cliente + "/" + area + "/"+local
Formulario["PRJ_SRC_USUARIO"].Valor = area + "/"+local
Formulario["PRJ_SRC_USUARIO"].Habilitado = False

#Formulario["PRJ_TIPO_ITEM"].Visivel = False
#Formulario["PRJ_ALIQUOTA"].Visivel = False
#Formulario["PRJ_CLASSE"].Visivel = False
#Formulario["PRJ_CONF_BEM"].Visivel = False
#Formulario["PRJ_DESC_CURTA"].Visivel = False
#Formulario["PRJ_FABRICANTE"].Visivel = False
#Formulario["PRJ_COD_EQUI_PERIF"].Visivel = False
#Formulario["PRJ_FAM_REPARO"].Visivel = False
#Formulario["PRJ_ITENS_ALT"].Visivel = False
#Formulario["PRJ_PLANEJADOR"].Visivel = False
Formulario["PRJ_PATRIMONIADO"].Visivel = False
Formulario["Justificativa"].Visivel = False
#Formulario["PRJ_AVISO"].Visivel = False
Formulario["PRJ_CODIGO_ITEM"].Visivel = False
Formulario["PRJ_CODIGO_ITENS"].Visivel = False
Formulario["PRJ_DESC_ITEM"].Visivel = False
#Formulario["PRJ_DESC_LONGA"].Visivel = False
Formulario["PRJ_UNI_MEDIDA"].Visivel = False
Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
Formulario["PRJ_CATEGORIA_NCM"].Visivel = False 
Formulario["LABEL1"].Visivel = False
#
#
#Formulario["PRJ_AVISO"].Valor = "Caso possua foto ou documentação do item, favor anexar." 
#
#
#Formulario["PRJ_AVISO"].Valor = "<span style=\"color: Red; font-weight: bold\"><br><br>*Caso possua foto ou documentação do item, favor anexar.</span>"
#
#Formulario["LABEL1"].Valor = "<span style=\"color: Black; font-weight: bold\"><br><br>Preencher apenas os campos que devem ser alterados.</span>"


#if Formulario["SERVICO_ITENS_CADASTRADOS"].Valor == "Serviços Contratados pela BBTS":
#    Formulario["PRJ_PATRIMONIADO"].Visivel = False
#    Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Exporte o Relatório de Apoio (Anexo I) e anexe em PDF as especificações técnicas para cadastro do código do item." classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - SERVICO_ITENS_CADASTRADOS "Escolha a opção" [DropDownList String → CPE_CONTRATOS02.SERVICO_ITENS_CADASTRADOS] obrigatório
**SERVICO_ITENS_CADASTRADOS.ScriptModificado**
```python
if Formulario["SERVICO_ITENS_CADASTRADOS"].Valor == "Itens Administrativos":
    Formulario["PRJ_PATRIMONIADO"].Visivel = True
    Formulario["PRJ_ORIGEM_ITEM"].Visivel = True
    
if Formulario["SERVICO_ITENS_CADASTRADOS"].Valor != "Itens Administrativos":
    Formulario["PRJ_PATRIMONIADO"].Visivel = False
    Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
```
  - PRJ_SRC_USUARIO "SRC/Descrição/Localidade" [TextBox String → CPE_PRJ_BB.PRJ_SRC_USUARIO] obrigatório
  - PRJ_CODIGO_ITEM "Código do Item" [TextBox String → CPE_PRJ_BB.PRJ_CODIGO_ITEM]
  - PRJ_TIPO_SOLICITACAO "Tipo de solicitação" [DropDownList String → CPE_PRJ_BB.PRJ_TIPO_SOLICITACAO] obrigatório
**PRJ_TIPO_SOLICITACAO.ScriptModificado**
```python
if Formulario["PRJ_TIPO_SOLICITACAO"].Valor == "Cadastrar":
    Formulario["PRJ_DESC_ITEM"].Visivel = True
    Formulario["PRJ_DESC_ITEM"].Habilitado = True
    Formulario["PRJ_UNI_MEDIDA"].Visivel = True
    Formulario["PRJ_UNI_MEDIDA"].Habilitado = True
    Formulario["PRJ_PATRIMONIADO"].Visivel = True
    Formulario["PRJ_PATRIMONIADO"].Habilitado = True
    Formulario["PRJ_ORIGEM_ITEM"].Visivel = True
    Formulario["PRJ_ORIGEM_ITEM"].Habilitado = True
    Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
    Formulario["PRJ_CATEGORIA_NCM"].Habilitado = True

    
if Formulario["PRJ_TIPO_SOLICITACAO"].Valor == "Alterar":
    Formulario["PRJ_CODIGO_ITEM"].Visivel = True
    Formulario["PRJ_CODIGO_ITEM"].Habilitado = True
    Formulario["PRJ_DESC_ITEM"].Visivel = True
    Formulario["PRJ_DESC_ITEM"].Habilitado = True
    Formulario["PRJ_ORIGEM_ITEM"].Visivel = True
    Formulario["PRJ_ORIGEM_ITEM"].Habilitado = True
    Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
    Formulario["PRJ_CATEGORIA_NCM"].Habilitado = True

if Formulario["PRJ_TIPO_SOLICITACAO"].Valor == "Inativar":
    Formulario["PRJ_CODIGO_ITENS"].Visivel = True
    Formulario["PRJ_CODIGO_ITENS"].Habilitado = True
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Habilitado = True

if Formulario["PRJ_TIPO_SOLICITACAO"].Valor == "Reativar":
    Formulario["PRJ_CODIGO_ITENS"].Visivel = True
    Formulario["PRJ_CODIGO_ITENS"].Habilitado = True
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Habilitado = True
```
  - PRJ_CODIGO_ITENS "Código dos Itens" [DataGrid RecordList → Z_00186_PRJ_CODIGO_ITENS.PRJ_CODIGO_ITENS] — PosicaoRotulo=Topo
    - coluna COD_ITEM obrigatório
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - PRJ_DESC_ITEM "Descrição do Item" [TextBox String → CPE_PRJ_BB.PRJ_DESC_ITEM]
  - PRJ_UNI_MEDIDA "Unidade de Medida" [DropDownList String → CPE_PRJ_BB.PRJ_UNI_MEDIDA]
  - PRJ_PATRIMONIADO "Patrimoniado?" [DropDownList String → CPE_PRJ_BB.PRJ_PATRIMONIADO]
  - PRJ_ORIGEM_ITEM "Origem do Item" [DropDownList String → CPE_PRJ_BB.PRJ_ORIGEM_ITEM]
  - PRJ_CATEGORIA_NCM "Categoria NCM" [DropDownList String → CPE_PRJ_BB.PRJ_CATEGORIA_NCM]
  - Justificativa (nativo)
  - PRJ_OBS "Observação" [Memo String → CPE_PRJ_BB.PRJ_OBS]
- Relatorios:
  - FormatoExportacao=PDF

### [366282] EventoFinal "Cancelado"
Config: TipoFinalizacao=NaoRealizado
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token = '***MASCARADO***'
URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Cancelada"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        log("Falha ao obter comprador_padrao: " + str(ex))

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```

### [366283] SubProcesso "Compras Diretas"
Referência: Se necessário, volte para a etapa anterior (e depois avance para a pergunta de direcionamento interno) para retorno à Controladoria ou ao início do processo para ajustes na montagem do documento unificado, ortografia ou adequações de incompatibilidade dos dados contábeis na elaboração da Ordem de Compra (OC), submetendo a nova aprovação se necessário. Atividade exclusiva do(a) Solucionador(a) ou Gerente do Cesec Compras para casos atípicos ao fluxo do processo.
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1459; PassaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":false}
MotivoInterrupcaoSLA: Aguardando Fim Subprocesso associado
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Processo
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Compras Diretas'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None

# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": 'Fila CSC',
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


OrdemServico.Salva()
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Compras Diretas'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- ValoresInputs:
  - CustomPropertyId=1942; CustomProperty=NUMERO_RC
  - CustomPropertyId=1060; CustomProperty=MODALIDADE_LICITACAO
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=2164; CustomProperty=DESCRICAO_DETALHADA
  - CustomPropertyId=807; CustomProperty=NUMERO_OC
  - CustomPropertyId=4810; CustomProperty=SIM_NAO_100
  - CustomPropertyId=1804; CustomProperty=CSC_LOGRADOURO
  - CustomPropertyId=4341; CustomProperty=FAVORECIDO_TODOS_03
  - CustomPropertyId=747; CustomProperty=DATA_ENTREGA
  - CustomPropertyId=1558; CustomProperty=PENF_EMAIL
- Relatorios:
  - FormatoExportacao=PDF
- Associação: Ativo=true; FraseAssociacao=PBE --> COMPRA DIRETA; FraseInversaAssociacao=COMPRA DIRETA --> PBE; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PBECOMPRASDIRETA; SeparadorSequencial=. | fonte: Projeto Básico Simplificado Eletrônico PBEE → alvo: Compras Diretas

### [366284] SubProcesso "Cadastro de Fornecedor"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=471; Codigo=CADFORNPBE1; Configuracao={"UtilizaMesmaVersaoProc":false}
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Cadastro de Fornecedor'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None

# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": 'Fila CSC',
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Cadastro de Fornecedor'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CADFORNATU")
```
  - CustomPropertyId=2476; CustomProperty=PB_OBJETO_CONTRATACAO
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=5331; CustomProperty=FORNECEDOR_CADASTRADO
- Associação: Ativo=true; FraseAssociacao=Projeto Básico Eletrônico Simplificado PBEE -> Cadastro de Fornecedor; FraseInversaAssociacao=Cadastro de Fornecedor -> Projeto Básico Eletrônico Simplificado PBEE; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=PBECADFOR; SeparadorSequencial=. | fonte: Projeto Básico Simplificado Eletrônico PBEE → alvo: Cadastro de Fornecedor

### [366225] Tarefa "Verificar Insumos"
Referência: PRO415-011 - Compras Diretas pelo Cesec: clique aqui
POP415-008 - Projeto Básico Eletrônico: clique aqui
Caro(a) Solucionador(a), o campo abaixo (Há pesquisa de mercado prévia?) é informado pelo cliente na abertura do chamado. Caso informado "Sim", e o cliente deseja a pesquisa de mercado pelo Cesec, altere para "Não" e avance para as próximas etapas. Se equivocadamente informou "Não" com a(s) proposta(s) anexa(s), devolva ao cliente informando que a resposta deve ser obrigatoriamente preenchida com "Sim".
Responsável: Fila CSC - Prestação de Serviços (papel 539)
Config: ConfirmaResponsabilidade=true
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))
 

OrdemServico.Salva()


import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()



etapa = 'Verificar Insumos'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Verificar Insumos'

# 'start' para abrir, 'end' para encerrar
acao = 'end'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))


OrdemServico.SetCustom('ARQUIVOS_ANEXADOS', OrdemServico.GetCustom('ARQUIVOS_ANEXADOS').Replace('\"', ''). Replace('<', '').Replace('>', '').Replace('/br', '').Replace('\\', ''))


Formulario['GESTOR_DE_ITENS_GESAP'].Visivel = False
Formulario['SIM_NAO20'].Visivel = False


if Formulario["SIM_NAO6"].Valor == "Sim":
    Formulario["SIM_NAO11"].Visivel = True
else:
    Formulario["SIM_NAO11"].Visivel = False


OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Importante!
  - LABEL150 "<b style="color:red">Somente avance para a etapa seguinte caso o usuário seja Solucionador ou Gerente Cesec.</b>" [Label String(1500) → CPE_PDCI2019.LABEL150] obrigatório
- Operação PR0001 Preencher Campos
  - LABEL150 "<b style="color:red">Somente avance para a etapa seguinte caso o usuário seja Solucionador ou Gerente Cesec.</b>" [Label String(1500) → CPE_PDCI2019.LABEL150] obrigatório
  - SIM_NAO6 "Há pesquisa de mercado prévia?" [DropDownList String → CPE_CSC.SIM_NAO6] obrigatório
**SIM_NAO6.ScriptModificado**
```python
if Formulario["SIM_NAO6"].Valor == 'Sim':
    Formulario["SIM_NAO11"].Visivel = True

if Formulario["SIM_NAO6"].Valor != 'Sim':
    Formulario["SIM_NAO11"].Visivel = False
```
  - FAVORECIDO_TODOS_03 "Solucionador responsável pelo PBe" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_03] obrigatório
  - SIM_NAO11 "Cartão CNPJ (CNAE), CND Federal, CRF (FGTS) e Consulta TCU (CNJ) do fornecedor de melhor preço, se encontra regular?" [DropDownList String → CPE_CONTRATOS.SIM_NAO11] obrigatório
  - LISTA_ITENS_PESQ_MERC "Lista de itens - Tipo de Objeto:" [DropDownList String → CPE_CSC.LISTA_ITENS_PESQ_MERC] obrigatório
  - DESCRICAO_OBRIG "Se Outros, especificar o tipo de objeto detalhadamente:" [TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG]
  - PAHL_VOUCHER_CARRO "DGCO relacionado, se houver." [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO] — Configuracao={"Mascara":"00000/0000"}
  - CODIGO_DO_SERVICO "Código da Pendência" [TextBox Integer → CPE_CSC.CODIGO_DO_SERVICO] obrigatório
  - GESTOR_DE_ITENS_GESAP "Item Gesap Teste" [DropDownList String(2000) → CPE_CONTRATOS02.GESTOR_DE_ITENS_GESAP] obrigatório
  - SIM_NAO20 "Valor Teste" [DropDownList String → CPE_CONTRATOS02.SIM_NAO20] obrigatório
**SIM_NAO20.ScriptModificado**
```python
#if Formulario['GESTOR_DE_ITENS_GESAP'].Valor == "Benfeitorias" or "Equipamentos/Móveis/Utensílios" or "Instalações" or "Manut. e Conservação" or "Máq. Equipamentos" or "Mat. Expediente" or "Móveis e utensílios":
#    Formulario['SIM_NAO20'].Valor = "Sim"
#    
#if Formulario['GESTOR_DE_ITENS_GESAP'].Valor != "Benfeitorias" or "Equipamentos/Móveis/Utensílios" or "Instalações" or "Manut. e Conservação" or "Máq. Equipamentos" or "Mat. Expediente" or "Móveis e utensílios":
#    Formulario['SIM_NAO20'].Valor = "Não"
```
- Relatorios:
  - FormatoExportacao=PDF

### [366226] EventoIntermediarioMensagem "PBe - Informar Conta Contábil"
Config: ListaDestinatarios=contabilidade@bbts.com.br
ModeloComunicado: Aviso sobre Abertura de Chamado
Corpo do comunicado: Prezados(as),
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada:
OrdemServico.DescricaoDetalhada 
 OrdemServico.Customizado.DESCRICAO_OBRIG 
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Informar Conta Contábil"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "contabilidade@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366227] Tarefa "Aguardar aprovação Gesap-Diage"
Responsável: Fila Pendencia de Aprovação (papel 1143)
Config: Codigo=APROVACAO_GESTORGESAP1
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Aguardar aprovação Gesap-Diage'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
        OrdemServico.AdicionaComentario(
            "Resposta da API (Erro HTTP {}): {}".format(int(response.Result.StatusCode), errText),
            True
        )
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Aguardar aprovação Gesap-Diage'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        OrdemServico.AdicionaComentario(
            "Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body),
            True
        )
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
            else:
                OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar utilização de rubrica da Gesap-Diage; MinimoAprovadores=1
  - (aprovação) DOTACAO1 "Dotação Orçamentária (opcional)" [TextBox String → CPE_CONTRATOS.DOTACAO1]
  - (aprovação) PB_OBJETO_CONTRATACAO "Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] — PermiteModificarAprovado=true
  - (aprovação) UOR "Informe a(s) UOR(s) de alocação de Despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR]
  - (aprovação) LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] — PermiteModificarAprovado=true
  - (aprovação) CONTA_CONTABIL1 "Conta Contábil (Não obrigatório) - A informação será validada pela Contabilidade" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] — PermiteModificarAprovado=true
  - (aprovação) GESTOR_DE_ITENS_GESAP "Item orçamentário (TAB208-001) da Gesap" [DropDownList String(2000) → CPE_CONTRATOS02.GESTOR_DE_ITENS_GESAP] — PermiteModificarAprovado=true
  - (aprovação) DescricaoDetalhada (nativo) "Justificativa da Contratação" — PermiteModificarAprovado=true
  - aprovador: Gerente Divisão Gesap (Unico)

### [366228] Tarefa "Preencher informações de Faturamento para relatório"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico

#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR'].ToString()+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')


#Tabela de Aprovações    
#consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'
#
#for dados in consultaAprovacoes.Rows:
#
#    cargo = ''
#    
#    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
#        cargo = dados['FUNCAO_GRATIFICADA']
#    else:
#        cargo = dados['CARGO']
#
#    tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
#    
#OrdemServico["APROVACOES"] = tabelaAprovacoes
#
#
#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"') 


#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

AvancaProximaAtividade = True





import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Preencher informações de Faturamento para relatório'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
        #OrdemServico.AdicionaComentario("Resposta da API (Erro HTTP {}): {}".format(int(response.Result.StatusCode), errText), True)
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Preencher informações de Faturamento para relatório'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0001 Preencher Campos
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366229] EventoIntermediarioTimer ""
Config: TempoIntervalo=200

### [366230] EventoIntermediarioTimer ""
Config: TempoIntervalo=720

### [366231] EventoIntermediarioTimer ""
Config: TempoIntervalo=480; MaximoExecucao=1

### [366232] EventoIntermediarioTimer ""
Config: TempoIntervalo=14400; MaximoExecucao=1

### [366233] EventoIntermediarioTimer ""
Config: TempoIntervalo=720

### [366285] EventoIntermediarioMensagem "Reprovação Gerente Executivo"
Destinatário: Cliente e Responsavel Atual (papel 544)
ModeloComunicado: Projeto Básico Reprovado - Ajustes
Corpo do comunicado: Prezado(a),
O projeto básico foi reprovado e necessita de ajustes.
Para ajustar o projeto básico, Link.Workspace .
Ajustes Necessários:
 Complemento1 
Dados do Projeto:
Objeto:
 OrdemServico.Customizado.PB_OBJETO_CONTRATACAO 
Itens da Contratação:
 OrdemServico.Customizado.CODIGO_ITEM 
Após ajustar as informações, clique em "Avançar" para submeter novamente para aprovação.
Qualquer dúvida, entre em contato com Cesec - Centro de Serviços Compartilhados.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROVAR_GEREX")

if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Verificar Reprovação Gerencial (Cliente)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Responsável Atual"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366286] Tarefa "Efetuar correções (Orçamento)
"
Responsável: Cliente (papel 18)
Config: PermiteCancelamentoAA=true; RotuloBotaoAvancar=Avançar (Enviar para Cesec)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.AdicionaComentario("Solicitação de ajustes da Controladoria: " + OrdemServico["PARECER_QUALIF"],False)


import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Efetuar correções (Orçamento)'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


OrdemServico.Salva()
```
**ScriptFim**
```python
OrdemServico.AdicionaComentario("Resposta/retorno do cliente da solicitação de ajustes da Controladoria (Campo Informações Orçamentárias): " + OrdemServico["CSC_ESCOLARIDADE"],False)



import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Efetuar correções (Orçamento)'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()



OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
Formulario["VALOR_REFERENCIAL"].Habilitado = False
Formulario["PARECER_QUALIF"].Habilitado = False
Formulario["CONTA_ORCAMENTARIA"].Habilitado = False
Formulario["CODIGO_ITEM"].Habilitado = False
Formulario["SIM_NAO14"].Visivel = False
#Formulario["CODIGO_ITEM"].Visivel = False
#Formulario["VALOR_REFERENCIAL"].Visivel = False
Formulario['CSC_ESCOLARIDADE'].Visivel = True
Formulario['UOR'].Visivel = True
Formulario['UOR'].Habilitado = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informação!
  - LABEL25 "Caso o comitê gerencial decida não seguir com a aquisição ou contratação nesta etapa, o próprio solicitante pode cancelar o chamado. Acesse a Central de Serviços (https://santacruz.bbts.com.br/Supravizio/Portal/Classico/Inicial.aspx), entre na aba "Consulta", selecione e entre no chamado desejado e clique no botão "Cancelar"; informe o motivo e clique em "Confirmar"." [Label String(1000) → CPE_PDCI2019.LABEL25] obrigatório
- Operação PR0001 Preencher Campos
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM]
    - coluna ITEM obrigatório
    - coluna NECESSIDADE obrigatório
    - coluna ITEM_OBSOLETO obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL]
    - coluna VALOR_TOTAL
    - coluna VALOR_REFERENCIAL obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna ITEM
  - PARECER_QUALIF "Parecer Controladoria" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] obrigatório
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - SIM_NAO14 "A Conta Orçamentária possui saldo?" [DropDownList String → CPE_CONTRATOS.SIM_NAO14] obrigatório
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário (informar Ordem de Serviço) e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica".)" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE] obrigatório
**CSC_ESCOLARIDADE.ScriptModificado**
```python
OrdemServico.Salva()
```
  - UOR "Informe a(s) UOR(s) de alocação de Despesa/Custo. (A alteração da UOR para outra área só deve ser realizada mediante ciência e concordância da área envolvida ¿ por exemplo, no caso de remanejamento orçamentário de itens de Marketing já providenciados via chamado, podendo ser utilizada a conta contabil e orçamentária da Gemac.)" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório
    - coluna UOR obrigatório
  - PB_OBJETO_CONTRATACAO "Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório

### [366234] Tarefa "Conferencia de Ajuste do Cliente da Reprovação Gerencial"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
Config: RotuloBotaoAvancar=Avançar (submeter aprovação Gerencial novamente)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Conferencia de Ajuste do Cliente da Reprovação Gerencial'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Conferencia de Ajuste do Cliente da Reprovação Gerencial'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptValidacao**
```python
#--- Validação de subcampos conforme marcação

uor = OrdemServico.GetCustom("UOR")
gerex = OrdemServico.GetCustom('PPGEREX_NEGOCIO')

if OrdemServico.GetCustom("SIM_NAO7") == 'Sim':
    if String.IsNullOrEmpty(gerex):
        Criticas.AdicionaPendencia("Informe o(a) Gerente Executivo(a) que efetuará a aprovação.")
         
if OrdemServico.GetCustom("TIPO_DE_VALOR_DE_REFERENCIA") == 'Outros:':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('JUSTIFICATIVA_IMPACTO')): 
        Criticas.AdicionaPendencia("Preencha o campo 'Informe detalhadamente o método estatístico utilizado (Valor Referencial)'.")
         
if OrdemServico.GetCustom("SIM_NAO1") == 'Não':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('OBS6')):
        Criticas.AdicionaPendencia("Preencha o campo 'JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002'.")
```
**ScriptFormCarregado**
```python
Formulario["SIM_NAO1"].Visivel = True
Formulario["SIM_NAO1"].Habilitado = True

Formulario["UOR"].Visivel = True
Formulario["UOR"].Habilitado = True

Formulario["PB_OBJETO_CONTRATACAO"].Visivel = True
Formulario["PB_OBJETO_CONTRATACAO"].Habilitado = True

Formulario["PARECER_QUALIF"].Visivel = True
Formulario["PARECER_QUALIF"].Habilitado = True

Formulario["QTD_PESQUISA"].Itens = "1;2;3;4;5;6"

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Pareceres
  - UOR "UOR(s) de alocação de Despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório
    - coluna UOR obrigatório
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - CONTA_CONTABIL1 "Conta Contábil (Parecer Contabilidade)" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - PARECER_QUALIF "Parecer Controladoria" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Pesquisa de Mercado Prévia" classes: Pesquisa de Mercado — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Anexo I -  Espeficiações Técnicas
  - OBS21 "2. Especificações Técnicas" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - LABEL1 "ATENÇÃO: O campo "2. Especificações Técnicas" tem o limite de 4000 caracteres. Caso o limite de caracteres não seja o suficiente, utilize os campos abaixo para complementar a informação." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - OBS22 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS22]
  - OBS23 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS23]
  - OBS10 "3. Qualificação Técnica" [Memo String(2000) → CPE_CSC.OBS10] obrigatório
  - OBS4 "4. Condições de Entrega" [Memo String(2000) → CPE_CONTRATOS.OBS4] obrigatório
  - OBS7 "Condições de Entrega - Continuação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS7]
  - INFORMACAO_FATURAMENTO "5. Informações para Faturamento: (Incluir os dados da BBTS para o qual será faturado o objeto da contratação)" [DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; PosicaoRotulo=Topo
    - coluna ENDERECO_COM_CEP obrigatório
    - coluna INSCRICAO_ESTADUAL
    - coluna ENDERECO obrigatório
    - coluna CNPJ_BBTS
    - coluna INSCRICAO_MUNICIIPAL
  - OBS3 "6. Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico:" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - NN_CONDICAO_PAGAMENTO "7. Condições de Pagamento:" [Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO] obrigatório
  - OBS5 "8. Multa" [Memo String(2000) → CPE_CONTRATOS.OBS5] obrigatório
  - OBS50 "9. Privacidade , Proteção e Tratamento de Dados Pessoais" [Memo String(2000) → CPE_CONTRATOS.OBS50] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais da Pesquisa de Mercado
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
#if Formulario['SIM_NAO1'].Valor == "Não":
#   Formulario['OBS6'].Habilitado = True
#   Formulario['OBS6'].Visivel = True
   
#if Formulario['SIM_NAO1'].Valor != "Sim":
#   Formulario['OBS6'].Habilitado = False
#   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184 Mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79 mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
  - JUSTIFICATIVA_IMPACTO "Justificativa 1 (Metodologia aplicada em caso de valor referencial escolhido "Outros")" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. " [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar ''Não se aplica''." [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Aprovadores
  - APROVADOR_PB "Aprovadores da contratação conforme NI006 (Somente Funções Gerenciais)" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório
    - coluna APROVADORES obrigatório
  - SIM_NAO7 "Solicitar aprovação do Gerente Executivo?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO]
- Operação PR0004 Associar Itens Configuração: Nome=DEMAISDOCAJUSTE
  - anexo "" classes: Comprovante de exclusividade — RequeridoInicial=true
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true
  - anexo "" classes: CND FGTS — RequeridoInicial=true
  - anexo "" classes: Parecer Jurídico Específico — RequeridoInicial=true
  - anexo "Demais Documentos (conforme TAB 415-001)" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Comprovação de razoabilidade de preço — RequeridoInicial=true
  - anexo "" classes: Nota Técnica — RequeridoInicial=true
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Apólice de Seguro – Serviço de Transporte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Rateio Localidades — RequeridoInicial=true
  - anexo "" classes: CND Federal — RequeridoInicial=true
  - anexo "" classes: QSA - Quadro de Sócios e Administradores — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Certidão CNJ — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Documentos adicionais para aprovação (opcional)" classes: Justificativa — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Importante!
  - LABEL150 "<b style="color:red">Somente avance para a etapa seguinte caso o usuário seja Solucionador ou Gerente Cesec.</b>" [Label String(1500) → CPE_PDCI2019.LABEL150] obrigatório
  - TEXT2 "Ajustes realizados pelo cliente para submeter a nova aprovação" [TextBox String → CPE_CSC.TEXT2]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Projeto Básico
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX

if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - DIRETORIA_GERENCIA "Área Técnica (quando couber)" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
  - PB_OBJETO_CONTRATACAO "1. Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
    - coluna PATRIMONIO obrigatório
    - coluna NOTA_FISCAL obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna PROD_NCM
    - coluna CODIGO obrigatório
    - coluna ITEM
    - coluna ITEM_OBSOLETO obrigatório
    - coluna PROD_DATA_REC obrigatório
    - coluna NECESSIDADE obrigatório
    - coluna PROD_PRODUTO obrigatório
  - QTD_PESQUISA "Quantidade de Pesquisas" [DropDownList String → CPE_CSC.QTD_PESQUISA] obrigatório
**QTD_PESQUISA.ScriptModificado**
```python
if Formulario["QTD_PESQUISA"].Valor == "6":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = True
    Formulario["FORNECEDOR6"].Habilitado = True
    Formulario["PESQUISA_MERCADO6"].Visivel = True
    Formulario["PESQUISA_MERCADO6"].Habilitado = True


if Formulario["QTD_PESQUISA"].Valor == "5":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "4":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False

if Formulario["QTD_PESQUISA"].Valor == "3":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "2":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "1":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = False
    Formulario["FORNECEDOR2"].Habilitado = False
    Formulario["PESQUISA_MERCADO2"].Visivel = False
    Formulario["PESQUISA_MERCADO2"].Habilitado = False
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = False
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
```
  - LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] obrigatório
  - FORNECEDOR01 "Fornecedor 1" [TextBox String → CPE_CSC.FORNECEDOR01] obrigatório
  - PESQUISA_MERCADO1 "PESQUISA_MERCADO1" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO1.PESQUISA_MERCADO1] obrigatório
**PESQUISA_MERCADO1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO
    - coluna PESQUISA1
**PESQUISA_MERCADO1.PESQUISA1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna ITEM1 obrigatório
    - coluna VALOR
    - coluna FORNECEDOR
    - coluna ITEM
    - coluna QUANTIDADE
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO1.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna DESCRICAO_ITEM
**PESQUISA_MERCADO1.DESCRICAO_ITEM.ScriptModificado**
```python
#FormularioRegistro["ITEM"].Visivel = True
#FormularioRegistro["ITEM"].Habilitado = True
#dt = OrdemServico.GetCustom("CODIGO_ITEM")
#itensCODIGO=''
#
#
#contCODIGO=0
#
##if (itensCNPJ.Rows.Count==0):
#for dr in dt.Rows:
#    igualCODIGO=0
#    regdr2=0
#    
#    #for dr2 in dt.Rows:
#    #    if (dr["ITEM"]== dr2["ITEM"]):
#    #        if (regdr<=regdr2 and igualCODIGO==0):
#    #            igualCODIGO=0
#    #        else:
#    #            igualCODIGO=1
#        
#    #if (igualCODIGO<=0):
#    if (contCODIGO==0):
#        itensCODIGO=dr["ITEM"]
#        contCODIGO=1
#    else:
#        itensCODIGO = itensCODIGO+';'+dr["ITEM"]
#
##regdr=regdr+1
#FormularioRegistro["ITEM"].Itens = itensCODIGO
#
```
  - FORNECEDOR2 "Fornecedor 2" [TextBox String → CPE_CSC.FORNECEDOR2]
  - FORNECEDOR4 "Fornecedor 4" [TextBox String → CPE_CSC.FORNECEDOR4]
  - PESQUISA_MERCADO2 "PESQUISA_MERCADO2" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO2.PESQUISA_MERCADO2]
**PESQUISA_MERCADO2.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO2.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna VALOR obrigatório
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
  - FORNECEDOR3 "Fornecedor 3" [TextBox String → CPE_CSC.FORNECEDOR3]
  - PESQUISA_MERCADO3 "PESQUISA_MERCADO3" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO3.PESQUISA_MERCADO3]
**PESQUISA_MERCADO3.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna DESCRICAO_ITEM
    - coluna ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO3.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna ITEM1 obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
  - PESQUISA_MERCADO4 "PESQUISA_MERCADO4" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO4.PESQUISA_MERCADO4]
**PESQUISA_MERCADO4.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO4.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM
    - coluna VALOR obrigatório
    - coluna ITEM1 obrigatório
    - coluna DESCRICAO_ITEM
    - coluna UDM
    - coluna QUANTIDADE obrigatório
    - coluna FORNECEDOR obrigatório
  - FORNECEDOR5 "Fornecedor 5" [TextBox String → CPE_CSC.FORNECEDOR5]
  - PESQUISA_MERCADO_5 "PESQUISA_MERCADO5" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO_5.PESQUISA_MERCADO_5]
**PESQUISA_MERCADO_5.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO_5.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO_5.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM1 obrigatório
    - coluna UDM obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
    - coluna VALOR obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna DESCRICAO_ITEM
  - FORNECEDOR6 "Fornecedor 6" [TextBox String → CPE_CSC.FORNECEDOR6]
  - PESQUISA_MERCADO6 "PESQUISA DE MERCADO 6" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO6.PESQUISA_MERCADO6]
**PESQUISA_MERCADO6.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna QUANTIDADE obrigatório
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna VALOR obrigatório
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO6.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM
    - coluna ITEM1 obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO6.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna VALOR_TOTAL
    - coluna ITEM
    - coluna VALOR_REFERENCIAL obrigatório
**VALOR_REFERENCIAL.VALOR_REFERENCIAL.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna VALOR_UNITARIO obrigatório
  - TIPO_ATIVIDADE "Classificação da Atividade" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
   Formulario['LABEL6'].Habilitado = True
   Formulario['LABEL6'].Visivel = True
   

if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
    Formulario['LABEL6'].Habilitado = False
    Formulario['LABEL6'].Visivel = False
```
  - LABEL6 "(Preencher se for contrato com FORNECEDOR para ATIVIDADE FIM) Citar todos os contratos de clientes no qual o serviço a ser contratado detém uma vinculação direta e indireta." [Label String(1500) → CPE_PDCI2019.LABEL6]
  - SIM_NAO "É contratação de Tic? " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
#if Formulario['SIM_NAO'].Valor == "Sim":
#   Formulario['SIM_NAO5'].Habilitado = True
#   Formulario['SIM_NAO5'].Visivel = True

#if Formulario['SIM_NAO'].Valor != "Sim":
#    Formulario['SIM_NAO5'].Habilitado = False
#    Formulario['SIM_NAO5'].Visivel = False
```
  - SIM_NAO5 "Aplica-se os artefatos da NI642?" [DropDownList String → CPE_CSC.SIM_NAO5]
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica"." [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]
  - VALOR "DOTAÇÃO ORÇAMENTÁRIA (VALOR GLOBAL OU VALOR GLOBAL ESTIMADO): R$ " [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - VALOR_DOD "Preço Global Referencial: R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]
  - COMBOBOX10 "Natureza Contábil" [DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo Complementar as Especificações Técnicas" classes: Especificação Técnica — RequeridoInicial=true; PermiteMultiplosItens=true

### [366235] FimCancelamento "Cancelamento por reprovação"
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Cancelada"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor
        )
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable(
            "SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente
        )
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
    except Exception as ex:
        log("Falha ao obter comprador_padrao: " + str(ex))

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```

### [366236] Tarefa "Informar código do item"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Informar código do item'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Informar código do item'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
Formulario["CODIGO_ITEM"].Visivel = True
Formulario["CODIGO_ITEM"].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - CODIGO_ITEM "Código do Item" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=500
    - coluna NECESSIDADE obrigatório
    - coluna ITEM_OBSOLETO obrigatório
    - coluna ITEM
- Relatorios:
  - FormatoExportacao=PDF

### [366237] EventoIntermediarioMensagem "Aviso para preenchimento de formulário"
Destinatário: Cliente e Gerente Posição (papel 631)
Config: EmailRemetente=csc@bbts.com.br
ModeloComunicado: Aviso para preenchimento de formulário
Corpo do comunicado: Prezado(a) OrdemServico.Cliente ,
Segue para preenchimento o formulário "Informações Adicionais para Pesquisa de Mercado" referente a Ordem de Serviço OrdemServico.Numero - OrdemServico.Assunto . 
Com a recente finalização da Ordem de Serviço de Pesquisa de Mercado, associada ao PBe, é necessário complementar o documento do Projeto Básico com os dados da pesquisa, tais como referencial, justificativas se houver, entre outros. 
 Link.Workspace para preencher o formulário com as informações necessárias.
O prazo para atendimento à solicitação contida neste e-mail é de 10 (dez) dias úteis. Após este prazo, o chamado será cancelado.
Após ajustar as informações, clique em "Avançar".
Qualquer dúvid…
**ScriptEvento**
```python
from Venki.Supravizio.Processo.Custom import Pesquisa
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Questionário Pesquisa de Mercado e Mitigação de Fracionamento de Demanda"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "csc@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366238] EventoIntermediarioMensagem "Conferir Parecer"
Config: ListaDestinatarios=cesec.comp@bbts.com.br
ModeloComunicado: Projeto Básico - Informações Gefic
Corpo do comunicado: Prezado(a),
Foram inseridas no projeto básico as informações de conta contábil e conta orçamentária.
Verifique o código do item e envie a Ordem de Serviço para aprovação do projeto básico.
Para maiores informações, Link.Edicao .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from Venki.Supravizio.Processo.Custom import Aprovador
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Conferir itens, Pareceres e Aprovadores"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "cesec.comp@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    pass
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366287] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório."
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico

#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR'].ToString()+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Tabela de Aprovações    
#consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'
#
#for dados in consultaAprovacoes.Rows:
#
#    cargo = ''
#    
#    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
#        cargo = dados['FUNCAO_GRATIFICADA']
#    else:
#        cargo = dados['CARGO']
#
#    tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
#    
#OrdemServico["APROVACOES"] = tabelaAprovacoes
#
#
#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"') 

#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos

#OrdemServico['FAVORECIDO_TODOS_2'] = OrdemServico.Cliente



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()


OrdemServico.Salva()

AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()

#Formulario['FAVORECIDO_TODOS_2'].Valor = OrdemServico.ClienteId
Formulario['FAVORECIDO_TODOS_2'].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
  - FAVORECIDO_TODOS_2 "Eladorador(a) do Projeto Básico" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_2] obrigatório
  - TABELA_DADOS_CONTRATOS_C "Tabela de Dados Contratuais" [Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C]
  - APROVACOES "Campo para preenchimento das aprovações." [Memo String(2000) → CPE_CSC.APROVACOES]
- Relatorios:
  - FormatoExportacao=PDF

### [366288] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório."
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico
#
#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR']+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Tabela de Aprovações    
consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"' ORDER BY VERSAO DESC")

tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'
listaAprovadores = []

for dados in consultaAprovacoes.Rows:
    cargo = ''
    
    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
        cargo = dados['FUNCAO_GRATIFICADA']
    else:
        cargo = dados['CARGO']

    if listaAprovadores.count(dados['NOME']) == 0:
        tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
        
    listaAprovadores.append(dados['NOME'])
    
OrdemServico["APROVACOES"] = tabelaAprovacoes.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')
#
#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')  

#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos




import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos
  - LISTA_VALOR_REF_UNIT "Valor referencial do Projeto Basico" [Memo String(2000) → CPE_CSC.LISTA_VALOR_REF_UNIT]
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
  - TABELA_DADOS_CONTRATOS_C "Tabela de Dados Contratuais" [Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C]
  - APROVACOES "Campo para preenchimento das aprovações." [Memo String(2000) → CPE_CSC.APROVACOES]
- Relatorios:
  - FormatoExportacao=PDF

### [366289] EventoIntermediarioMensagem "Ausência de informações"
Destinatário: Cliente e Gerente Posição (papel 631)
Config: EmailRemetente=csc@bbts.com.br
ModeloComunicado: Aviso sobre a falta de documentos ou informações 3
Corpo do comunicado: Prezado(a),
Solicitamos a inclusão da documentação/informação faltante para que possamos dar continuidade ao tratamento da Ordem de Serviço nº OrdemServico .
O prazo para atendimento à solicitação contida neste e-mail é de 5 (cinco) dias úteis. Após este prazo, o chamado será cancelado.
Pendências: 
 Complemento1 
Para ajustar o Projeto Básico, Link.Edicao Worklist .
Após ajustar as informações, clique em "Avançar".
Qualquer dúvida, entre em contato com Cesec - Centro de Serviços Compartilhados.
Atenciosamente,
 Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("INSFALT")

if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Efetuar correções (Insumos)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "csc@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    pass
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo

### [366290] Tarefa "Aguardar aprovação Gemac"
Responsável: Responsável atual (papel 36)
Config: Codigo=APROVACAO_GESTORDIMAC
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()



etapa = 'Aguardar aprovação Gemac'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'


url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Aguardar aprovação Gemac'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar utilização de Conta de Marketing; ReenvioEmailAprovacao=24
  - (aprovação) UOR "UOR" [DataGrid RecordList → Z_00143_UOR.UOR] — PermiteModificarAprovado=true
  - (aprovação) GEREX "Gerencia Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX] — PermiteModificarAprovado=true
  - (aprovação) PB_OBJETO_CONTRATACAO "Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] — PermiteModificarAprovado=true
  - (aprovação) DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] — PermiteModificarAprovado=true
  - (aprovação) VALOR_REFERENCIAL "Valor referencial da contratação" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL] — PermiteModificarAprovado=true
  - (aprovação) CONTA_CONTABIL1 "Conta Contábil" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] — PermiteModificarAprovado=true
  - (aprovação) CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA] — PermiteModificarAprovado=true
  - (aprovação) PARECER_QUALIF "Parecer Controladoria" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] — PermiteModificarAprovado=true
  - aprovador: Gerente Gemac (Unico)

### [366291] SubProcesso "Cadastro de Fornecedor"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=471; Codigo=CADFORNPBE; Configuracao={"UtilizaMesmaVersaoProc":false}
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Cadastro de Fornecedor'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None

# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": 'Fila CSC',
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Processo.Custom import Processo
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Cadastro de Fornecedor'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=5331; CustomProperty=FORNECEDOR_CADASTRADO
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CADFORNEC")
```
  - CustomPropertyId=2476; CustomProperty=PB_OBJETO_CONTRATACAO
- Associação: Ativo=true; FraseAssociacao=Projeto Básico Eletrônico Simplificado PBEE -> Cadastro de Fornecedor; FraseInversaAssociacao=Cadastro de Fornecedor -> Projeto Básico Eletrônico Simplificado PBEE; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=PBECADFOR; SeparadorSequencial=. | fonte: Projeto Básico Simplificado Eletrônico PBEE → alvo: Cadastro de Fornecedor

### [366239] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório."
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico
#
#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR']+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Tabela de Aprovações    
consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"' ORDER BY VERSAO DESC")

tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'
listaAprovadores = []

for dados in consultaAprovacoes.Rows:
    cargo = ''
    
    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
        cargo = dados['FUNCAO_GRATIFICADA']
    else:
        cargo = dados['CARGO']

    if listaAprovadores.count(dados['NOME']) == 0:
        tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
        
    listaAprovadores.append(dados['NOME'])
    
OrdemServico["APROVACOES"] = tabelaAprovacoes.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')
#
#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')  

#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos
  - LISTA_VALOR_REF_UNIT "Valor referencial do Projeto Basico" [Memo String(2000) → CPE_CSC.LISTA_VALOR_REF_UNIT]
  - TABELA_DADOS_CONTRATOS_C "Tabela de Dados Contratuais" [Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C]
  - APROVACOES "Campo para preenchimento das aprovações." [Memo String(2000) → CPE_CSC.APROVACOES]
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366240] Tarefa "Conferir itens, Pareceres e Aprovadores"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
Config: ConfirmaResponsabilidade=true
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Aprovador
from Venki.Services.Custom import Query
OrdemServico['FAVORECIDO_TODOS_2'] = OrdemServico.ClienteId

OrdemServico.ModificaCampoFormularioVisivel('UOR', True)



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Conferir itens, Pareceres e Aprovadores'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()



OrdemServico.Salva()
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Aprovador
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Conferir itens, Pareceres e Aprovadores'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptValidacao**
```python
#--- Certidões irregulares
if OrdemServico.GetCustom("SIM_NAO11")  == 'Não':
   Criticas.AdicionaPendencia("CND Federal, CRF (FGTS) e Consulta TCU (CNJ) do fornecedor de melhor preço deve obrigatoriamente se encontrar regular!")
  
#--- Validação de subcampos conforme marcação

uor = OrdemServico.GetCustom("UOR")
gerex = OrdemServico.GetCustom('PPGEREX_NEGOCIO')

if OrdemServico.GetCustom("SIM_NAO7") == 'Sim':
    if String.IsNullOrEmpty(gerex):
        Criticas.AdicionaPendencia("Informe o(a) Gerente Executivo(a) que efetuará a aprovação.")
         
if OrdemServico.GetCustom("TIPO_DE_VALOR_DE_REFERENCIA") == 'Outros:':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('JUSTIFICATIVA_IMPACTO')): 
        Criticas.AdicionaPendencia("Preencha o campo 'Informe detalhadamente o método estatístico utilizado (Valor Referencial)'.")
         
if OrdemServico.GetCustom("SIM_NAO1") == 'Não':
    if String.IsNullOrEmpty(OrdemServico.GetCustom('OBS6')):
        Criticas.AdicionaPendencia("Preencha o campo 'JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002'.")
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.Salva()

Formulario["QTD_PESQUISA"].Visivel = True
Formulario["QTD_PESQUISA"].Habilitado = True
Formulario["FORNECEDOR01"].Visivel = True
Formulario["FORNECEDOR01"].Habilitado = True
Formulario["PESQUISA_MERCADO1"].Visivel = True
Formulario["PESQUISA_MERCADO1"].Habilitado = True
Formulario["FORNECEDOR2"].Visivel = True
Formulario["FORNECEDOR2"].Habilitado = True
Formulario["PESQUISA_MERCADO2"].Visivel = True
Formulario["PESQUISA_MERCADO2"].Habilitado = True
Formulario["FORNECEDOR3"].Visivel = True
Formulario["FORNECEDOR3"].Habilitado = True
Formulario["PESQUISA_MERCADO3"].Visivel = True
Formulario["PESQUISA_MERCADO3"].Habilitado = True
Formulario["FORNECEDOR4"].Visivel = True
Formulario["FORNECEDOR4"].Habilitado = True
Formulario["PESQUISA_MERCADO4"].Visivel = True
Formulario["PESQUISA_MERCADO4"].Habilitado = True
Formulario["FORNECEDOR5"].Visivel = True
Formulario["FORNECEDOR5"].Habilitado = True
Formulario["PESQUISA_MERCADO_5"].Visivel = True
Formulario["PESQUISA_MERCADO_5"].Habilitado = True
Formulario["FORNECEDOR6"].Visivel = True
Formulario["FORNECEDOR6"].Habilitado = True
Formulario["PESQUISA_MERCADO6"].Visivel = True
Formulario["PESQUISA_MERCADO6"].Habilitado = True
Formulario["VALOR_DOD"].Visivel = False
Formulario["VALOR"].Visivel = False
Formulario['QTD_PESQUISA'].Itens = '1;2;3;4;5;6'

Formulario["JUSTIFICATIVA_IMPACTO"].Visivel = True
Formulario['UOR'].Visivel = True
Formulario['UOR'].Habilitado = True
Formulario['SIM_NAO11'].Visivel = True
Formulario['SIM_NAO11'].Habilitado = True

Formulario["SIM_NAO7"].Visivel = True
Formulario["SIM_NAO7"].Habilitado = True
Formulario["PPGEREX_NEGOCIO"].Visivel = True
Formulario["PPGEREX_NEGOCIO"].Habilitado = True
Formulario["SIM_NAO5"].Visivel = True
Formulario["SIM_NAO5"].Habilitado = True
Formulario["SIM_NAO1"].Visivel = True
Formulario["SIM_NAO1"].Habilitado = True
Formulario["OBS6"].Visivel = True
Formulario["OBS6"].Habilitado = True

Formulario["QTD_PESQUISA"].Itens = "1;2;3;4;5;6"

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Projeto Básico
  - LOCALIDADE_MOV "Local / UF" [TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV] obrigatório
  - PB_OBJETO_CONTRATACAO "1. Objeto" [Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO] obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna RC_COMPRAS obrigatório
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna PATRIMONIO obrigatório
    - coluna NOTA_FISCAL obrigatório
  - DescricaoDetalhada (nativo) "Justificativa da Contratação" obrigatório
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna ITEM_OBSOLETO obrigatório
    - coluna PROD_DATA_REC obrigatório
    - coluna NECESSIDADE obrigatório
    - coluna PROD_PRODUTO obrigatório
    - coluna PROD_NCM
    - coluna CODIGO obrigatório
    - coluna ITEM
  - QTD_PESQUISA "Quantidade de Pesquisas" [DropDownList String → CPE_CSC.QTD_PESQUISA] obrigatório
**QTD_PESQUISA.ScriptModificado**
```python
if Formulario["QTD_PESQUISA"].Valor == "6":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = True
    Formulario["FORNECEDOR6"].Habilitado = True
    Formulario["PESQUISA_MERCADO6"].Visivel = True
    Formulario["PESQUISA_MERCADO6"].Habilitado = True


if Formulario["QTD_PESQUISA"].Valor == "5":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = True
    Formulario["FORNECEDOR5"].Habilitado = True
    Formulario["PESQUISA_MERCADO_5"].Visivel = True
    Formulario["PESQUISA_MERCADO_5"].Habilitado = True
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "4":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = True
    Formulario["FORNECEDOR4"].Habilitado = True
    Formulario["PESQUISA_MERCADO4"].Visivel = True
    Formulario["PESQUISA_MERCADO4"].Habilitado = True
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False

if Formulario["QTD_PESQUISA"].Valor == "3":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = True
    Formulario["FORNECEDOR3"].Habilitado = True
    Formulario["PESQUISA_MERCADO3"].Visivel = True
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "2":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = True
    Formulario["FORNECEDOR2"].Habilitado = True
    Formulario["PESQUISA_MERCADO2"].Visivel = True
    Formulario["PESQUISA_MERCADO2"].Habilitado = True
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = True
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
    
if Formulario["QTD_PESQUISA"].Valor == "1":
    Formulario["FORNECEDOR01"].Visivel = True
    Formulario["FORNECEDOR01"].Habilitado = True
    Formulario["PESQUISA_MERCADO1"].Visivel = True
    Formulario["PESQUISA_MERCADO1"].Habilitado = True
    Formulario["FORNECEDOR2"].Visivel = False
    Formulario["FORNECEDOR2"].Habilitado = False
    Formulario["PESQUISA_MERCADO2"].Visivel = False
    Formulario["PESQUISA_MERCADO2"].Habilitado = False
    Formulario["FORNECEDOR3"].Visivel = False
    Formulario["FORNECEDOR3"].Habilitado = False
    Formulario["PESQUISA_MERCADO3"].Visivel = False
    Formulario["PESQUISA_MERCADO3"].Habilitado = False
    Formulario["FORNECEDOR4"].Visivel = False
    Formulario["FORNECEDOR4"].Habilitado = False
    Formulario["PESQUISA_MERCADO4"].Visivel = False
    Formulario["PESQUISA_MERCADO4"].Habilitado = False
    Formulario["FORNECEDOR5"].Visivel = False
    Formulario["FORNECEDOR5"].Habilitado = False
    Formulario["PESQUISA_MERCADO_5"].Visivel = False
    Formulario["PESQUISA_MERCADO_5"].Habilitado = False
    Formulario["FORNECEDOR6"].Visivel = False
    Formulario["FORNECEDOR6"].Habilitado = False
    Formulario["PESQUISA_MERCADO6"].Visivel = False
    Formulario["PESQUISA_MERCADO6"].Habilitado = False
```
  - FORNECEDOR01 "Fornecedor 1" [TextBox String → CPE_CSC.FORNECEDOR01] obrigatório
  - PESQUISA_MERCADO1 "PESQUISA_MERCADO1" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO1.PESQUISA_MERCADO1] obrigatório
**PESQUISA_MERCADO1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna ITEM
**PESQUISA_MERCADO1.ITEM.ScriptModificado**
```python
#dt = OrdemServico.GetCustom("CODIGO_ITEM")
#
#itensCODIGO = ''
#cont=0
#
#for dr in dt.Rows:
#    if (FormularioRegistro["ITEM"].Valor == dr["CODIGO_ITEM"]):
#        if (cont==0):
#            itensCODIGO=dr["ITEM"]
#        else:
#            itensCNPJ = itensCODIGO+';'+dr["ITEM"]
#
#        cont=1
#FormularioRegistro["ITEM"].Itens = itensCODIGO
#
```
    - coluna QUANTIDADE
    - coluna ITEM1 obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO1.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO
    - coluna FORNECEDOR
    - coluna DESCRICAO_ITEM
**PESQUISA_MERCADO1.DESCRICAO_ITEM.ScriptModificado**
```python
#FormularioRegistro["ITEM"].Visivel = True
#FormularioRegistro["ITEM"].Habilitado = True
#dt = OrdemServico.GetCustom("CODIGO_ITEM")
#itensCODIGO=''
#
#
#contCODIGO=0
#
##if (itensCNPJ.Rows.Count==0):
#for dr in dt.Rows:
#    igualCODIGO=0
#    regdr2=0
#    
#    #for dr2 in dt.Rows:
#    #    if (dr["ITEM"]== dr2["ITEM"]):
#    #        if (regdr<=regdr2 and igualCODIGO==0):
#    #            igualCODIGO=0
#    #        else:
#    #            igualCODIGO=1
#        
#    #if (igualCODIGO<=0):
#    if (contCODIGO==0):
#        itensCODIGO=dr["ITEM"]
#        contCODIGO=1
#    else:
#        itensCODIGO = itensCODIGO+';'+dr["ITEM"]
#
##regdr=regdr+1
#FormularioRegistro["ITEM"].Itens = itensCODIGO
#
```
    - coluna PESQUISA1
**PESQUISA_MERCADO1.PESQUISA1.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna VALOR
  - FORNECEDOR2 "Fornecedor 2" [TextBox String → CPE_CSC.FORNECEDOR2]
  - PESQUISA_MERCADO2 "PESQUISA_MERCADO2" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO2.PESQUISA_MERCADO2]
**PESQUISA_MERCADO2.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna ITEM
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM1 obrigatório
    - coluna VALOR obrigatório
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO2.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
  - FORNECEDOR3 "Fornecedor 3" [TextBox String → CPE_CSC.FORNECEDOR3]
  - PESQUISA_MERCADO3 "PESQUISA_MERCADO3" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO3.PESQUISA_MERCADO3]
**PESQUISA_MERCADO3.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO3.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM obrigatório
    - coluna DESCRICAO_ITEM
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR obrigatório
    - coluna ITEM
    - coluna ITEM1 obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna QUANTIDADE obrigatório
  - FORNECEDOR4 "Fornecedor 4" [TextBox String → CPE_CSC.FORNECEDOR4]
  - PESQUISA_MERCADO4 "PESQUISA_MERCADO4" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO4.PESQUISA_MERCADO4]
**PESQUISA_MERCADO4.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna ITEM
    - coluna VALOR_UNITARIO obrigatório
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO4.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna UDM
    - coluna DESCRICAO_ITEM
    - coluna QUANTIDADE obrigatório
    - coluna FORNECEDOR obrigatório
    - coluna VALOR obrigatório
  - FORNECEDOR5 "Fornecedor 5" [TextBox String → CPE_CSC.FORNECEDOR5]
  - PESQUISA_MERCADO_5 "PESQUISA_MERCADO5" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO_5.PESQUISA_MERCADO_5]
**PESQUISA_MERCADO_5.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna VALOR obrigatório
    - coluna ITEM1 obrigatório
    - coluna UDM obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna ITEM
    - coluna FORNECEDOR obrigatório
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO_5.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna VALOR_UNITARIO obrigatório
    - coluna DESCRICAO_ITEM
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO_5.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
  - FORNECEDOR6 "Fornecedor 6" [TextBox String → CPE_CSC.FORNECEDOR6]
  - PESQUISA_MERCADO6 "PESQUISA DE MERCADO 6" [DataGrid RecordList → Z_00143_PESQUISA_MERCADO6.PESQUISA_MERCADO6]
**PESQUISA_MERCADO6.ScriptModificado**
```python
FormularioRegistro["ITEM"].Visivel = True
FormularioRegistro["ITEM"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM"].Itens = itensCODIGO
```
    - coluna NUMERO obrigatório
**PESQUISA_MERCADO6.NUMERO.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna QUANTIDADE obrigatório
    - coluna DESCRICAO_ITEM
    - coluna VALOR obrigatório
    - coluna VALOR_UNITARIO obrigatório
    - coluna NUMERO1 obrigatório
**PESQUISA_MERCADO6.NUMERO1.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna ITEM
    - coluna UDM obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna VALOR_TOTAL
    - coluna ITEM
    - coluna VALOR_REFERENCIAL obrigatório
**VALOR_REFERENCIAL.VALOR_REFERENCIAL.ScriptModificado**
```python
FormularioRegistro["ITEM1"].Visivel = True
FormularioRegistro["ITEM1"].Habilitado = True
dt = OrdemServico.GetCustom("CODIGO_ITEM")
itensCODIGO=''


contCODIGO=0

#if (itensCNPJ.Rows.Count==0):
for dr in dt.Rows:
    igualCODIGO=0
    regdr2=0
    
    #for dr2 in dt.Rows:
    #    if (dr["ITEM"]== dr2["ITEM"]):
    #        if (regdr<=regdr2 and igualCODIGO==0):
    #            igualCODIGO=0
    #        else:
    #            igualCODIGO=1
        
    #if (igualCODIGO<=0):
    if (contCODIGO==0):
        itensCODIGO=dr["ITEM"]
        contCODIGO=1
    else:
        itensCODIGO = itensCODIGO+';'+dr["ITEM"]

#regdr=regdr+1
FormularioRegistro["ITEM1"].Itens = itensCODIGO
```
    - coluna ITEM1 obrigatório
    - coluna VALOR_UNITARIO obrigatório
  - TIPO_ATIVIDADE "Classificação da Atividade" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
**TIPO_ATIVIDADE.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Atividade
if Formulario['TIPO_ATIVIDADE'].Valor == "Atividade Fim":
   Formulario['LABEL6'].Habilitado = True
   Formulario['LABEL6'].Visivel = True
   

if Formulario['TIPO_ATIVIDADE'].Valor != "Atividade Fim":
    Formulario['LABEL6'].Habilitado = False
    Formulario['LABEL6'].Visivel = False
```
  - LABEL6 "(Preencher se for contrato com FORNECEDOR para ATIVIDADE FIM) Citar todos os contratos de clientes no qual o serviço a ser contratado detém uma vinculação direta e indireta." [Label String(1500) → CPE_PDCI2019.LABEL6]
  - SIM_NAO "É contratação de Tic? " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
#if Formulario['SIM_NAO'].Valor == "Sim":
#   Formulario['SIM_NAO5'].Habilitado = True
#   Formulario['SIM_NAO5'].Visivel = True

#if Formulario['SIM_NAO'].Valor != "Sim":
#    Formulario['SIM_NAO5'].Habilitado = False
#    Formulario['SIM_NAO5'].Visivel = False
```
  - SIM_NAO5 "Aplica-se os artefatos da NI642?" [DropDownList String → CPE_CSC.SIM_NAO5]
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica"." [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]
  - VALOR "DOTAÇÃO ORÇAMENTÁRIA (VALOR GLOBAL OU VALOR GLOBAL ESTIMADO): R$ " [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - VALOR_DOD "Preço Global Referencial: R$" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]
  - COMBOBOX10 "Natureza Contábil" [DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10] obrigatório
  - DIRETORES "Diretoria" [DropDownList String → CP_ORDEM_SERVICO.DIRETORES] obrigatório
**DIRETORES.ScriptModificado**
```python
#----- Consulta GEREX

if Formulario["DIRETORES"].Valor != None:
    if Formulario["DIRETORES"].Valor != "933":
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao_pai = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
    else:
        Formulario["GEREX"].Itens = Utils.ExecuteDataTable("SELECT O.ID_ORGAO, O.DESCRICAO FROM orgao o WHERE Ativo = 'Sim' AND id_orgao = "+ Formulario["DIRETORES"].Valor.ToString() +" ORDER BY O.DESCRICAO")
#   Formulario["GEREX"].Visivel = True
#else:
#   Formulario["GEREX"].Visivel = False
#Formulario["GEREX"].Valor = None
```
  - GEREX "Gerência Executiva" [DropDownList String → CP_ORDEM_SERVICO.GEREX]
  - DIRETORIA_GERENCIA "Área Técnica (quando couber)" [TextBox String → CPE_CSC.DIRETORIA_GERENCIA]
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Pareceres
  - UOR "UOR(s) de alocação de Despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório
    - coluna UOR obrigatório
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - CONTA_CONTABIL1 "Conta Contábil (Parecer Contabilidade)" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - PARECER_QUALIF "Consulta Orçamentária" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] obrigatório
  - SIM_NAO14 "A Conta Orçamentária possui saldo?" [DropDownList String → CPE_CONTRATOS.SIM_NAO14] obrigatório
  - SIM_NAO20 "Refere-se a Conta de Investimento?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO20] obrigatório
  - DOTACAO1 "Dotação Orçamentária informada pelo Cliente na abertura (opcional)" [TextBox String → CPE_CONTRATOS.DOTACAO1] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações Adicionais da Pesquisa de Mercado
  - TIPO_DE_VALOR_DE_REFERENCIA "Justificativa 1: Informar qual o método estatístico utilizado (média, mediana ou menor valor) e justificar aqueles valores que foram pesquisados, mas deverão ser desconsiderados por serem inexequíveis, inconsistentes ou excessivamente elevados. Deverão ser adotados critérios fundamentados. Em caso de inexigibilidade, informar ''Não se aplica''." [DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA] obrigatório
  - JUSTIFICATIVA_IMPACTO "Justificativa 1 (Metodologia aplicada em caso de valor referencial escolhido "Outros")" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO]
  - JUSTIFICATIVA_IMAGEM "Justificativa 2: Justificar, com fundamentos plausíveis e boa argumentação o motivo de não ter sido possível obter ao menos 03 (três) preços por item contratado. Listar os itens que se aplicam e a justificativa de cada um. " [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM] obrigatório
  - JUSTIFICATIVA_TENDENCIA "Justificativa da escolha do(s) fornecedor(es): (melhor preço, proposta mais econômica, entre outros ¿ não cite nome de fornecedores)" [Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA] obrigatório
  - SIM_NAO1 "Pesquisa de preços realizada conforme parâmetros preferenciais estabelecidos no PRO417-002 (PESQUISA DE PREÇOS DE MERCADO) e na quantidade mínima de 3?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
#if Formulario['SIM_NAO1'].Valor == "Não":
#   Formulario['OBS6'].Habilitado = True
#   Formulario['OBS6'].Visivel = True
   
#if Formulario['SIM_NAO1'].Valor != "Sim":
#   Formulario['OBS6'].Habilitado = False
#   Formulario['OBS6'].Visivel = False
```
  - OBS6 "JUSTIFICATIVA - Justificar quando não utilizar os parâmetros preferenciais do PRO417-002." [Memo String(2000) → CPE_CSC.OBS6]
  - FQ415_066_ITEM31 "Foi conferido pela área demandante que a compra/contratação por Dispensa de valor (art. 29, incisos I e II da lei 13.303/16) não extrapola o limite legal?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31] obrigatório
  - FQ415_066_ITEM32 "Trata-se de obra ou serviço de engenharia de valor até R$ 184 Mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32] obrigatório
  - FQ415_066_ITEM321 "Refere-se a parcela de uma mesma obra ou serviço já contratado anteriormente?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321] obrigatório
  - FQ415_066_ITEM322 "Trata-se de obra ou serviço cuja natureza e local sejam os mesmos de contratação anterior que poderia ter sido planejada para aquisição conjunta e concomitantemente? " [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322] obrigatório
  - FQ415_066_ITEM33 "Trata-se de outros serviços e compras de valor até R$ 79 mil?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33] obrigatório
  - FQ415_066_ITEM331 "Refere-se a parcela de um mesmo serviço ou compra de maior vulto que poderia ter sido realizada de uma só vez?" [DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331] obrigatório
  - SIM_NAO11 "Cartão CNPJ (CNAE), CND Federal, CRF (FGTS) e Consulta CNJ do fornecedor de melhor preço, se encontra regular?" [DropDownList String → CPE_CONTRATOS.SIM_NAO11] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Anexo I -  Espeficiações Técnicas
  - OBS21 "2. Especificações Técnicas" [Memo String(4000) → CPE_CSC.OBS21] obrigatório
  - LABEL1 "ATENÇÃO: O campo "2. Especificações Técnicas" tem o limite de 4000 caracteres. Caso o limite de caracteres não seja o suficiente, utilize os campos abaixo para complementar a informação." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - OBS22 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS22]
  - OBS23 "Especificações Técnicas - Continuação (Não obrigatório)" [Memo String(4000) → CPE_CSC.OBS23]
  - OBS10 "3. Qualificação Técnica" [Memo String(2000) → CPE_CSC.OBS10] obrigatório
  - OBS4 "4. Condições de Entrega" [Memo String(2000) → CPE_CONTRATOS.OBS4] obrigatório
  - OBS7 "Condições de Entrega - Continuação (Não obrigatório)" [Memo String(2000) → CPE_CSC.OBS7]
  - INFORMACAO_FATURAMENTO "5. Informações para Faturamento: (Incluir os dados da BBTS para o qual será faturado o objeto da contratação)" [DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO] obrigatório — FormaEdicaoWeb=JanelaPopup; PosicaoRotulo=Topo
    - coluna INSCRICAO_ESTADUAL
    - coluna ENDERECO obrigatório
    - coluna CNPJ_BBTS
    - coluna INSCRICAO_MUNICIIPAL
    - coluna ENDERECO_COM_CEP obrigatório
  - OBS3 "6. Condições de Garantia e Assistência Técnica, Manutenção e Suporte Técnico:" [Memo String(2000) → CPE_CONTRATOS.OBS3] obrigatório
  - NN_CONDICAO_PAGAMENTO "7. Condições de Pagamento:" [Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO] obrigatório
  - OBS5 "8. Multa" [Memo String(2000) → CPE_CONTRATOS.OBS5] obrigatório
  - OBS50 "9. Privacidade , Proteção e Tratamento de Dados Pessoais" [Memo String(2000) → CPE_CONTRATOS.OBS50] obrigatório
- Operação PR0001 Preencher Campos
  - LABEL150 "<b style="color:red">Somente avance para a etapa seguinte caso o usuário seja Solucionador ou Gerente Cesec.</b>" [Label String(1500) → CPE_PDCI2019.LABEL150] obrigatório
  - FAVORECIDO_TODOS_2 "Assessor/Analista que assinará como elaborador(a) do Projeto Básico" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_2] obrigatório
  - APROVADOR_PB "Aprovadores da contratação conforme NI006 (Somente Funções Gerenciais)" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório
    - coluna APROVADORES obrigatório
  - SIM_NAO7 "Solicitar aprovação do Gerente Executivo?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório
  - PPGEREX_NEGOCIO "Gerente Executivo da Contratação" [DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO]
- Operação PR0004 Associar Itens Configuração
  - anexo "Parecer Jurídico" classes: Parecer Jurídico — RequeridoInicial=true
- Relatorios:
  - FormatoExportacao=PDF

### [366241] Tarefa "Recolhe aprovações e outras informações para preenchimento do relatório."
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Services.Custom import Query
#Tabela de Valor Referencial do Projeto Basico
#consultaValorReferencialDoProjetoBasico = DB.ExecuteDataTable("Select * from Z_00143_VALOR_REF_UNIT WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#
#tabelaValorReferencialDoProjetoBasico = '<table><tr><th>Valor Referencial</th><th>Item</th><th>Valor unitário</th><th>Valor Total</th></tr>'
#
#for dados in consultaValorReferencialDoProjetoBasico.Rows:
#    tabelaValorReferencialDoProjetoBasico = tabelaValorReferencialDoProjetoBasico+'<tr><td>'+dados['VALOR_REFERENCIAL']+'</td><td>'+dados['ITEM']+'</td><td>'+dados['VALOR_UNITARIO']+'</td><td>'+dados['VALOR_TOTAL']+'</td></tr>'
#
#OrdemServico["LISTA_VALOR_REF_UNIT"] = tabelaValorReferencialDoProjetoBasico

#Tabela de Dados do Contrato de Contrapartida do Cliente
consultaDadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaDadosContratoContraPartidaDoCliente.Rows.Count > 0:
    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = 'OK'
    tabelaDadosContratosContraPartidaDoCliente = '<table><tr><th>DGCOs do(s) contrato(s) de contrapartida com o cliente</th><th>Razão Social do Cliente</th><th>Valor do(s) contrato(s)</th></tr>'
    
    dadosContratoContraPartidaDoCliente = DB.ExecuteDataTable("Select * from Z_00143_DADOS_CONTRATOS_C WHERE ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dados in dadosContratoContraPartidaDoCliente.Rows:
        tabelaDadosContratosContraPartidaDoCliente = tabelaDadosContratosContraPartidaDoCliente+'<tr><td>'+dados['DGCO']+'</td><td>'+dados['NOME_CLIENTE']+'</td><td>'+dados['VALOR'].ToString()+'</td></tr>'

    OrdemServico["TABELA_DADOS_CONTRATOS_C"] = tabelaDadosContratosContraPartidaDoCliente.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Tabela de Aprovações    
consultaAprovacoes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, VERSAO_APROVACAO.DATA_HORA_FIM, PESSOA.NOME, PESSOA.CARGO, CP_PESSOA.FUNCAO_GRATIFICADA, CP_PESSOA.CPF, APROVACAO.MOTIVO, APROVACAO.SITUACAO, APROVACAO.DATA_HORA_EVIDENCIA From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA =ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO =VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO =APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA WHERE APROVACAO.SITUACAO = 'Aprovado' and OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

tabelaAprovacoes = '<table><tr><th>Aprovações</th></tr>'

for dados in consultaAprovacoes.Rows:

    cargo = ''
    
    if dados['FUNCAO_GRATIFICADA'] != DBNull.Value:
        cargo = dados['FUNCAO_GRATIFICADA']
    else:
        cargo = dados['CARGO']

    tabelaAprovacoes = tabelaAprovacoes+'<tr><td>'+dados['NOME']+'</br>'+dados['CPF']+'</br>'+cargo+'</br>'+dados['DATA_HORA_EVIDENCIA'].ToString()+'</td></tr>'
    
OrdemServico["APROVACOES"] = tabelaAprovacoes.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')

#Lista HTML INFORMACOES_PAGAMENTO
tabelaInformacoesPagamento = ""

consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaInformacoesPagamento.Rows.Count > 0:

    consultaInformacoesPagamento = DB.ExecuteDataTable("select Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA, Z_00143_INFORMACAO_FATURAMENTO.CNPJ_BBTS, Z_00143_INFORMACAO_FATURAMENTO.ENDERECO, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_MUNICIIPAL, Z_00143_INFORMACAO_FATURAMENTO.INSCRICAO_ESTADUAL from Z_00143_INFORMACAO_FATURAMENTO WHERE Z_00143_INFORMACAO_FATURAMENTO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
    
    for dados in consultaInformacoesPagamento.Rows:
    
        if dados["INSCRICAO_MUNICIIPAL"] != DBNull.Value:
            inscricaoMunicipal = dados["INSCRICAO_MUNICIIPAL"]
        else:
            inscricaoMunicipal = ''
    
        tabelaInformacoesPagamento = tabelaInformacoesPagamento+'<tr><td>CNPJ de Faturamento: '+dados["CNPJ_BBTS"]+'</tr><tr><td>Endereço de Faturamento: '+dados["ENDERECO"]+'</td></tr><tr><td>Inscrição Estadual ou Distrital: '+dados["INSCRICAO_ESTADUAL"]+'</td></tr><tr><td>Inscrição Municipal: '+inscricaoMunicipal+'</td></tr><tr><td></td></tr>'
    
OrdemServico["TABELA_HTML_INFO_FATURAMENTO"] = tabelaInformacoesPagamento.Replace('<', '\\"<\\"').Replace('>', '\\">\\"')  

#Lista de anexos
listaAnexos = ''

consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

if consultaAnexos.Rows.Count > 0:

    consultaAnexos = DB.ExecuteDataTable("select OCORRENCIA.ID_OCORRENCIA, ITEM_OCORRENCIA.DATA_HORA_ANEXADO, ITEM.DESCRICAO FROM OCORRENCIA INNER JOIN ITEM_OCORRENCIA ON OCORRENCIA.ID_OCORRENCIA = ITEM_OCORRENCIA.ID_OCORRENCIA INNER JOIN ITEM ON ITEM_OCORRENCIA.ID_ITEM = ITEM.ID_ITEM WHERE OCORRENCIA.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")

    for dadosAnexos in consultaAnexos.Rows:
        listaAnexos = listaAnexos+dadosAnexos['DESCRICAO']+'</br>'
    
OrdemServico["ARQUIVOS_ANEXADOS"] = listaAnexos




import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório.'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Recolhe aprovações e outras informações para preenchimento do relatório.'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        #OrdemServico.AdicionaComentario("Erro HTTP {} ao encerrar etapa: {}".format(int(response.Result.StatusCode), body), True)
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- Operação PR0001 Preencher Campos
  - TABELA_DADOS_CONTRATOS_C "Tabela de Dados Contratuais" [Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C]
  - APROVACOES "Campo para preenchimento das aprovações." [Memo String(2000) → CPE_CSC.APROVACOES]
  - TABELA_HTML_INFO_FATURAMENTO "Tabela HTML de informações de faturamento" [Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO] obrigatório
  - LISTA_VALOR_REF_UNIT "Valor referencial do Projeto Basico" [Memo String(2000) → CPE_CSC.LISTA_VALOR_REF_UNIT]
- Relatorios:
  - FormatoExportacao=PDF

### [366292] Tarefa "Informar número da OS criada para Cadastro de Fornecedor"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Services.Custom import Query
num_associada = OrdemServico.ObtemAssociadasComoAlvo('PBECADFOR')
associadas = ''

if not len(num_associada) > 1:
    for i in num_associada:
        OrdemServico['CSC_LOGRADOURO'] += i.ToString().split(' - ')[0]
        
else:
    for i in num_associada:
        OrdemServico['CSC_LOGRADOURO'] += i.ToString().split(' - ')[0] + ', '


import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Informar número da OS criada para Cadastro de Fornecedor'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""

except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()

        
OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'
url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Informar número da OS criada para Cadastro de Fornecedor'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
#Formulario["CSC_CPF"].Visivel = True
#Formulario["CSC_CPF"].Habilitado = True

#num_associada = OrdemServico.ObtemAssociadasComoAlvo('PBECADFOR')
#associadas = ''
#
#if not len(num_associada) > 1:
#    for i in num_associada:
#        Formulario['CSC_CPF'].Valor += i.ToString().split(' - ')[0]
#        
#else:
#    for i in num_associada:
#        Formulario['CSC_CPF'].Valor += i.ToString().split(' - ')[0] + ', '
```
- Operação PR0001 Preencher Campos
  - CSC_LOGRADOURO "Número da OS subprocesso Cadastro de Fornecedor" [TextBox String(500) → CPE_CSC.CSC_LOGRADOURO]

### [366293] Tarefa "Verificar se o fornecedor está cadastrado
"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Verificar se o fornecedor está cadastrado'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
resp = DB.ExecuteDataTable(
    "SELECT PESSOA.NOME, OCORRENCIA.ASSUNTO, OCORRENCIA.NUMERO, OCORRENCIA.SITUACAO "
    "FROM PESSOA "
    "INNER JOIN OCORRENCIA ON OCORRENCIA.ID_RESPONSAVEL = PESSOA.ID_PESSOA "
    "WHERE OCORRENCIA.NUMERO = '" + OrdemServico.Numero + "' "
    "FETCH FIRST 1 ROWS ONLY"
)

responsavel = ""
for row in resp.Rows:
    responsavel = (row["NOME"] or "").ToString().Trim()
    break



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
        OrdemServico.AdicionaComentario(
            "Resposta da API (Erro HTTP {}): {}".format(int(response.Result.StatusCode), errText),
            True
        )
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Verificar se o fornecedor está cadastrado'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
Formulario["PENF_FORNECEDOR"].Visivel = True
Formulario["PENF_FORNECEDOR"].Habilitado = True
Formulario['FORNECEDOR_CADASTRADO'].Visivel = False
Formulario['FORNECEDOR_CADASTRADO'].Visivel = False
```
- Operação PR0001 Preencher Campos
  - PENF_FORNECEDOR "Fornecedor" [DropDownList String → CPE_PENF.PENF_FORNECEDOR]
  - FORNECEDOR_CADASTRADO "Fornecedor Cadastrado?" [DropDownList String → CPE_CONTRATOS02.FORNECEDOR_CADASTRADO] obrigatório
- Relatorios:
  - FormatoExportacao=PDF

### [366294] EventoIntermediarioMensagem "Reprovação Gemac"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Projeto Básico Reprovado - Ajustes
Corpo do comunicado: Prezado(a),
O projeto básico foi reprovado e necessita de ajustes.
Para ajustar o projeto básico, Link.Workspace .
Ajustes Necessários:
 Complemento1 
Dados do Projeto:
Objeto:
 OrdemServico.Customizado.PB_OBJETO_CONTRATACAO 
Itens da Contratação:
 OrdemServico.Customizado.CODIGO_ITEM 
Após ajustar as informações, clique em "Avançar" para submeter novamente para aprovação.
Qualquer dúvida, entre em contato com Cesec - Centro de Serviços Compartilhados.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROVACAO_GESTORDIMAC")

if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Ajustar reprovação Gemac (Cliente)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Gerente Posição"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366295] EventoIntermediarioMensagem "PBe - Aviso sobre abertura de chamado"
Config: ListaDestinatarios=cesec.comp@bbts.com.br;tiago.pires@bbts.com.br;rodrigo.figueiredo@bbts.com.br;rony.baldoino@bbts.com.br; MaximoExecucao=1
ModeloComunicado: Aviso sobre Abertura de Chamado
Corpo do comunicado: Prezados(as),
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada:
OrdemServico.DescricaoDetalhada 
 OrdemServico.Customizado.DESCRICAO_OBRIG 
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Preencher informações de Faturamento para relatório"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "cesec.comp@bbts.com.br;tiago.pires@bbts.com.br;rodrigo.figueiredo@bbts.com.br;rony.baldoino@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366296] EventoIntermediarioMensagem "PBe - Consulta conta orçamentária"
Config: ListaDestinatarios=cesec.comp@bbts.com.br
ModeloComunicado: Aviso sobre Abertura de Chamado
Corpo do comunicado: Prezados(as),
Foi aberta a Ordem de Serviço nº OrdemServico.Numero referente ao assunto: OrdemServico.SubProcesso .
Descrição Detalhada:
OrdemServico.DescricaoDetalhada 
 OrdemServico.Customizado.DESCRICAO_OBRIG 
Para maiores informações Link.Workspace .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Aviso sobre Abertura de Chamado - Consulta conta orçamentária"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "cesec.comp@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366242] EventoIntermediarioMensagem "Reprovação Gerente da Contratação"
Destinatário: Cliente e Responsavel Atual (papel 544)
ModeloComunicado: Projeto Básico Reprovado - Ajustes
Corpo do comunicado: Prezado(a),
O projeto básico foi reprovado e necessita de ajustes.
Para ajustar o projeto básico, Link.Workspace .
Ajustes Necessários:
 Complemento1 
Dados do Projeto:
Objeto:
 OrdemServico.Customizado.PB_OBJETO_CONTRATACAO 
Itens da Contratação:
 OrdemServico.Customizado.CODIGO_ITEM 
Após ajustar as informações, clique em "Avançar" para submeter novamente para aprovação.
Qualquer dúvida, entre em contato com Cesec - Centro de Serviços Compartilhados.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoReprovacao("APROVACAO_GERENTES")


if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Verificar Reprovação Gerencial (Cliente)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Responsável Atual"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- Relatorios:
  - FormatoExportacao=PDF

### [366243] Tarefa "Avaliar se a conta contábil e a uor utilizadas são da Gemac e se rubrica são da Gesap"
Referência: .
Rubricas Orçamentárias que requer aprovação da Gesap (Diage):
Despesas:
Equipamentos/Móveis/Utensílios
Mat. Expediente
Manut. e Conservação
Investimento:
Móveis e utensílios
Máq. Equipamentos
Benfeitorias
Instalações
Rubricas Orçamentárias que requer aprovação da Gemac (Marketing):
Mídia/Institucional
Produção/Institucional
Material Promocional/Institucional
Representação
 .
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Avaliar se a conta contábil e a uor utilizadas são da Gemac e se rubrica são da Gesap'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Avaliar se a conta contábil e a uor utilizadas são da Gemac e se rubrica são da Gesap'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
Formulario["SIM_NAO10"].Visivel = True
Formulario["SIM_NAO10"].Habilitado = True
Formulario["UOR"].Visivel = True
Formulario["UOR"].Habilitado = True
```
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS GEMAC
  - anexo "" classes: Arte — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Remanejamento Orçamentário — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Pareceres
  - CONTA_CONTABIL1 "Conta Contábil (Parecer Contabilidade)" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - SIM_NAO10 "Para esta solicitação a UOR utilizada é a 3000004052 (Gemac) com conta orçamentária 93434180 e a conta contábil é 34341801 - Mídia/Institucional, 34341802 - Produção/Institucional, 34341803 - Material Promocional/Institucional ou 34341804 - Representação ?" [DropDownList String → CPE_CSC.SIM_NAO10] obrigatório
  - UOR "UOR(s) de alocação de Despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR] obrigatório
    - coluna UOR obrigatório
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - TEXT "Número O.S. (Remanejamento Orçamentário) - Informe N/A se for a própria Gemac a Área Cliente." [TextBox String(1000) → CPE_CSC.TEXT]
  - PARECER_QUALIF "Parecer Controladoria" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados preenchidos pelo cliente na abertura do chamado (considere a validação dos pareceres)
  - GESTOR_DE_ITENS_GESAP "Item Orçamentário (TAB208-001)" [DropDownList String(2000) → CPE_CONTRATOS02.GESTOR_DE_ITENS_GESAP] obrigatório
  - SIM_NAO20 "Houve aprovação no inicio do chamado pela Gesap-Diage?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO20] obrigatório
  - SIM_NAO10 "Para esta solicitação a UOR utilizada é a 3000004052 (Gemac) com conta orçamentária 93434180 e a conta contábil é 34341801 - Mídia/Institucional, 34341802 - Produção/Institucional, 34341803 - Material Promocional/Institucional ou 34341804 - Representação ?" [DropDownList String → CPE_CSC.SIM_NAO10] obrigatório

### [366244] EventoIntermediarioMensagem "Aviso de retorno da Ordem de Serviço"
Config: ListaDestinatarios=cesec.comp@bbts.com.br
ModeloComunicado: Aviso de retorno de chamado
Corpo do comunicado: Prezado(a),
Foi recebido na respectiva fila o chamado: OrdemServico - OrdemServico.Assunto .
Para mais informações Link.Edicao .
Atenciosamente,
Central de Serivços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Retorno de devolução ao cliente para nova solicitação de parecer"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "cesec.comp@bbts.com.br"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366245] EventoIntermediarioMensagem "Aviso de cancelamento de chamado por falta de ajustes"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Reprovação por falta de ajustes
Corpo do comunicado: Prezado(a),
A Ordem de Serviço OrdemServico.Numero foi cancelado automaticamente por falta de ajustes.
Para realizar este serviço abra uma nova solicitação.
Para maiores informações Link.Consulta.
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Efetuar correções (Orçamento)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Gerente Posição"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366246] EventoIntermediarioMensagem "Término de Serviço"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
 Complemento1 
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Término de Serviço"  # ajuste conforme a etapa do seu evento

idCliente = 0
nomeCliente = ''

try:
    idCliente = OrdemServico.Cliente.Id.ToString()
    dt = Utils.ExecuteDataTable("SELECT P.NOME FROM PESSOA P INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA WHERE CP.ID_PESSOA = '" + idResp + "'")
    nomeCliente = None
    for r in dt.Rows:
        nomeCliente = r["NOME"]
        break
except:
    nomeCliente = None

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = nomeCliente  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1767; ClasseConfiguracao=Projeto Básico

### [366297] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
**ScriptInicio**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 |
        getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'
URL_OS_SALVAR = "https://sisccon.bbts.com.br/supravizio/supra/salvar-os-pbee"

# ===== Helpers =====
def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        respTask = client.PostAsync(url, content); respTask.Wait()
        body = ""
        try:
            body = respTask.Result.Content.ReadAsStringAsync().Result
        except:
            pass
        return (respTask.Result.IsSuccessStatusCode, int(respTask.Result.StatusCode), body)
    finally:
        client.Dispose()

def log(msg):
    try:
        OrdemServico.AdicionaComentario(msg, True)
    except:
        pass

# ===== Dados de OS =====
os_numero = str(OrdemServico.Numero)
situacao = "Finalizada com Sucesso"  # <-- Altere aqui para a nova situação desejada

# Comprador: tenta usar o nome do recebedor; se não houver, usa o nome do ClienteId
comprador_padrao = ""
try:
    recebedor = str(OrdemServico.GetCustom('NOME_RECEBEDOR'))
    if recebedor is not None:
        compr = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + recebedor)
            
        for row in compr.Rows:
            comprador_padrao = row["NOME"].ToString()
except:
    pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    try:
        idCliente = OrdemServico.ClienteId.ToString()
        resp = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idCliente)
        
        for row in resp.Rows:
            comprador_padrao = row["NOME"].ToString()
            
    except Exception as ex:
        #log("Falha ao obter comprador_padrao: " + str(ex))
        pass

if comprador_padrao is None or comprador_padrao.strip() == "":
    comprador_padrao = "Comprador não informado"

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")

# ===== Envia apenas a OS =====
payload_os = {
    "os": os_numero,
    "dt_abertura_os": agora,
    "situacao": situacao,
    "comprador_padrao": comprador_padrao,
    "observacoes": "Situação atualizada via integração"
}

ok, status_code, body = http_post_json(URL_OS_SALVAR, payload_os)
#log("Payload OS: " + JsonConvert.SerializeObject(payload_os))

if not ok:
    pass
    #log("Falha ao salvar OS (HTTP {}): {}".format(status_code, body))
else:
    try:
        obj = JsonConvert.DeserializeObject(body)
        st = obj["status"] if "status" in obj else "?"
        msg = obj["message"] if "message" in obj else ""
        #log("Salvar OS -> {}: {}".format(st, msg))
    except:
        pass
        #log("Salvar OS (resposta cru): " + body)
```
**ScriptFim**
```python
OrdemServico.FinalizadorId = Convert.ToInt32(OrdemServico.ResponsavelId)
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=OC(s) criada(s) no Compras Diretas
  - NUMERO_DE_OC "Número de OC" [TextBox String(50) → CPE_CONTRATOS.NUMERO_DE_OC]
- Relatorios:
  - FormatoExportacao=PDF

### [366298] EventoIntermediarioMensagem "Ausência de informações"
Destinatário: Cliente e Gerente Posição (papel 631)
Config: EmailRemetente=csc@bbts.com.br
ModeloComunicado: Aviso sobre a falta de documentos ou informações 4
Corpo do comunicado: Prezado(a),
Solicitamos a inclusão da documentação/informação faltante para que possamos dar continuidade ao tratamento da ordem de serviço OrdemServico.
O prazo para atendimento à solicitação contida neste e-mail é de 10 (dez) dias úteis. Após este prazo, o chamado será cancelado.
Pendências: 
 OrdemServico.Customizado.PARECER_QUALIF 
Para ajustar o Projeto Básico, Link.Workspace .
Após ajustar as informações, clique em "Avançar".
Qualquer dúvida, entre em contato com Cesec - Centro de Serviços Compartilhados.
Atenciosamente,
 Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("INSFALT")

if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
        
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = OrdemServico.Numero.ToString()

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = u"Efetuar correções (Orçamento)"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Cliente e Gerente Posição"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": destinatario
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo

### [366299] EventoIntermediarioMensagem "Aviso de aprovação ao Gestor"
Destinatário: Gerente Divisão Gesap (papel 1359)
ModeloComunicado: Aviso para aprovação
Corpo do comunicado: Prezado(a),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto segue para sua aprovação.
Para mais detalhes sobre esta solicitação : Link.Consulta .
Atenciosamente
Central de Serviços
**ScriptEvento**
```python
from System import DBNull

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import TimeSpan

# ===== TLS =====
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ===== Config =====
token = '***MASCARADO***'
token2 = '***MASCARADO***'


URL_ALERTA = "https://sisccon.bbts.com.br/supravizio/supra/registrar-alerta-pbee"


def http_post_json(url, payload):
    client = HttpClient()
    try:
        client.Timeout = TimeSpan.FromSeconds(60)
        client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
        client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)
        content = StringContent(JsonConvert.SerializeObject(payload), Encoding.UTF8, "application/json")
        task = client.PostAsync(url, content); task.Wait()
        code = int(task.Result.StatusCode)
        body = ""
        try: body = task.Result.Content.ReadAsStringAsync().Result
        except: pass
        return (task.Result.IsSuccessStatusCode, code, body)
    finally:
        client.Dispose()

# ===== Dados do alerta =====
os_numero = str(OrdemServico.Numero)

# Defina a etapa atual ¿sem erro de digitação¿: use exatamente como cadastrado nas etapas
etapa = "Aguardar aprovação Gesap"  # ajuste conforme a etapa do seu evento

# Quem recebe: pode ser nome, matrícula ou e-mail; escolha um padrão e mantenha
# Exemplos de origem:
# destinatario = str(OrdemServico.GetCustom("NOME_APROVADOR"))
# ou, se estiver na tarefa: destinatario = str(OrdemServico.ResponsavelAtual)
destinatario = "Gerente Divisão Gesap"  # ajuste conforme seu fluxo

payload = {
    "os": os_numero,
    "etapa": etapa,
    "destinatario": str(destinatario)
}

ok, status, body = http_post_json(URL_ALERTA, payload)
#log("Payload Alerta: " + JsonConvert.SerializeObject(payload))
if not ok:
    #log("Falha ao registrar alerta (HTTP {}): {}".format(status, body))
    pass
else:
    try:
        resp = JsonConvert.DeserializeObject(body)
        st = resp["status"] if "status" in resp else "?"
        msg = resp["message"] if "message" in resp else ""
        #log("Registrar alerta -> {}: {}".format(st, msg))
        pass
    except:
        pass
        #log("Registrar alerta (não-JSON): " + body)
```

### [366300] SubProcesso "Verificar Dados Orçamentários"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
Config: AssociacaoId=1684
**ScriptInicio**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = str(OrdemServico.Numero)
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Verificar Dados Orçamentários'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None

# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": 'Fila CSC',
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()
```
**ScriptFim**
```python
from Venki.Supravizio.Processo.Custom import Processo
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = str(OrdemServico.Numero)
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Sub Processo - Verificar Dados Orçamentários'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
- ValoresInputs:
  - CustomPropertyId=2930; CustomProperty=CODIGO_ITEM
  - CustomPropertyId=1938; CustomProperty=CONTA_CONTABIL1
  - CustomPropertyId=2857; CustomProperty=VALOR_REFERENCIAL
  - CustomPropertyId=2574; CustomProperty=UOR
- Associação: Ativo=true; FraseAssociacao=Projeto Básico Simplificado Eletrônico PBEE -> Verificação de Dados Orçamentários; FraseInversaAssociacao=Verificação de Dados Orçamentários -> Projeto Básico Simplificado Eletrônico PBEE; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrMore; Nome=PBECONTAORCAM; SeparadorSequencial=. | fonte: Projeto Básico Simplificado Eletrônico PBEE → alvo: Verificação de Dados Orçamentários

### [366301] Tarefa "Avançar tarefa"
Responsável: Fila CSC - Prestação de Serviços (papel 539)
**ScriptInicio**
```python
from Venki.Services.Custom import Query
OrdemServico.ModificaCampoFormularioVisivel('SIM_NAO14', True)
OrdemServico.ModificaCampoFormularioVisivel('UOR', True)



import clr
# Referências de assemblies necessários
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")  # mscorlib/System para DateTime etc.

from Newtonsoft.Json import JsonConvert

from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue

# "System.Text" é NAMESPACE, não assembly. NÃO fazer AddReference.
from System.Text import Encoding

from System import DateTime, TimeSpan

# (Opcional) Garantir TLS 1.2/1.3 se o host exigir
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    # Se Tls13 não existir, fica só no Tls12
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

# ==== Configurações ====
token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

# ==== Dados da OS ====
os_numero = OrdemServico.Numero.ToString()
situacao = 'Em andamento'

# Pega o nome do responsável do seu banco (mantive sua lógica)
idResponsavel = OrdemServico.ResponsavelId.ToString()






etapa = 'Avançar tarefa'

# 'start' para abrir, 'end' para encerrar
acao = 'start'  # ajuste conforme seu fluxo

# ==== Datas (sempre agora) ====
agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora                  # se preferir, pode usar OrdemServico.DataHoraCriacao.ToString("yyyy-MM-dd HH:mm:ss")
dt_inicio_etapa = agora if acao == 'start' else None
dt_saida_etapa = agora if acao == 'end' else None


# ==== Query (1 linha, nome limpinho) ====
responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()



# ==== Monta payload ====
payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,
    "situacao": situacao,
    "responsavel_enviado": responsavel,  # string limpa
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

# ==== Envia requisição ====
client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

# ==== Trata resposta ====
try:
    if response.Result.IsSuccessStatusCode:
        resultText = response.Result.Content.ReadAsStringAsync().Result
        #OrdemServico.AdicionaComentario("Resposta da API (OK): " + resultText, True)
    else:
        # Tenta ler corpo; se falhar, usa só o status
        try:
            errText = response.Result.Content.ReadAsStringAsync().Result
        except:
            errText = ""
except Exception as e:
    pass
    #OrdemServico.AdicionaComentario("Falha ao processar resposta: " + str(e), True)
finally:
    client.Dispose()




OrdemServico.Salva()







AvancaProximaAtividade = True
```
**ScriptFim**
```python
import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("System")

from Newtonsoft.Json import JsonConvert
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Http import HttpClient, StringContent
from System.Net.Http.Headers import AuthenticationHeaderValue, MediaTypeWithQualityHeaderValue
from System.Text import Encoding
from System import DateTime, TimeSpan

# TLS
try:
    ServicePointManager.SecurityProtocol = (
        SecurityProtocolType.Tls12 | getattr(SecurityProtocolType, "Tls13", SecurityProtocolType.Tls12)
    )
except:
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12

token = '***MASCARADO***'
token2 = '***MASCARADO***'

url = "https://sisccon.bbts.com.br/supravizio/supra/inserir-etapa-pbee"

os_numero = OrdemServico.Numero.ToString()
situacao = 'Concluída'

responsavel = ""    
idResponsavel = OrdemServico.ResponsavelId.ToString()
responsavelSql = DB.ExecuteDataTable("SELECT PESSOA.NOME FROM PESSOA WHERE PESSOA.ID_PESSOA = " + idResponsavel)

for row in responsavelSql.Rows:
    responsavel = row["NOME"].ToString()

etapa = 'Avançar tarefa'
acao = 'end'  # encerramento

agora = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")
dt_abertura_os = agora
dt_inicio_etapa = None
dt_saida_etapa = agora  # sempre agora no end

payload = {
    "acao": acao,
    "os": os_numero,
    "dt_abertura_os": dt_abertura_os,            # não usado no end, mas não atrapalha
    "situacao": 'Concluída',                         # idem
    "responsavel_enviado": responsavel,    # idem
    "etapa": etapa,
    "dt_inicio_etapa": dt_inicio_etapa,
    "dt_saida_etapa": dt_saida_etapa
}

json_data = JsonConvert.SerializeObject(payload)

client = HttpClient()
client.Timeout = TimeSpan.FromSeconds(60)
client.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))
client.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Bearer", token)

content = StringContent(json_data, Encoding.UTF8, "application/json")
response = client.PostAsync(url, content)
response.Wait()

try:
    body = ""
    try:
        body = response.Result.Content.ReadAsStringAsync().Result
    except:
        pass

    # Loga o payload enviado para auditoria
    #OrdemServico.AdicionaComentario("Payload enviado (end): " + json_data, True)

    if not response.Result.IsSuccessStatusCode:
        pass
    else:
        # Tenta interpretar JSON
        try:
            resultObj = JsonConvert.DeserializeObject(body)
            status = resultObj["status"] if "status" in resultObj else "desconhecido"
            message = resultObj["message"] if "message" in resultObj else ""
            if status != "success":
                # Tratar warning/erro do backend como falha funcional
                #OrdemServico.AdicionaComentario("Encerramento NÃO realizado (status={}): {}".format(status, message), True)
                pass
            else:
                #OrdemServico.AdicionaComentario("Encerramento OK: {}".format(message),True)
                pass
        except Exception as exJson:
            # Se não for JSON, loga cru
            #OrdemServico.AdicionaComentario("Resposta (não-JSON): " + body, True)
            pass
finally:
    client.Dispose()
```
**ScriptFormCarregado**
```python
OrdemServico.SetCustom('TABELA_DADOS_CONTRATOS_C', OrdemServico.GetCustom('TABELA_DADOS_CONTRATOS_C').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('APROVACOES', OrdemServico.GetCustom('APROVACOES').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

OrdemServico.SetCustom('TABELA_HTML_INFO_FATURAMENTO', OrdemServico.GetCustom('TABELA_HTML_INFO_FATURAMENTO').Replace('\\"', '').Replace('<', '\\"<\\"').Replace('>', '\\">\\"'))

Formulario["VALOR_REFERENCIAL"].Visivel = True
Formulario["VALOR_REFERENCIAL"].Habilitado = True
Formulario["PARECER_QUALIF"].Habilitado = True
Formulario["SIM_NAO14"].Visivel = True
Formulario["SIM_NAO14"].Habilitado = True
Formulario["CONTA_ORCAMENTARIA"].Habilitado = True
Formulario["CODIGO_ITEM"].Habilitado = True
OrdemServico.ModificaCampoFormularioVisivel('PARECER_RISCO', False)
Formulario['CSC_ESCOLARIDADE'].Visivel = True
Formulario["SIM_NAO20"].Visivel = True
Formulario["SIM_NAO20"].Habilitado = True

#Formulario["SIM_NAO14"].Valor = '[Nenhum(a)]'

Formulario['UOR'].Visivel = True
Formulario['UOR'].Habilitado = True

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informação!
  - LABEL21 "Salve e atualize antes de Avançar!" [Label String(700) → CPE_PDCI2019.LABEL21] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados
  - CODIGO_ITEM "Código do Item a ser contratado" [DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM]
    - coluna ITEM obrigatório
    - coluna ITEM_OBSOLETO obrigatório
    - coluna NECESSIDADE obrigatório
  - VALOR_REFERENCIAL "Valor Referencial" [DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL]
    - coluna ITEM
    - coluna ITEM1 obrigatório
    - coluna VALOR_TOTAL
    - coluna VALOR_UNITARIO obrigatório
    - coluna VALOR_REFERENCIAL obrigatório
  - UOR "UOR(s) de alocação de despesa/Custo" [DataGrid RecordList → Z_00143_UOR.UOR]
    - coluna UOR obrigatório
  - DOTACAO1 "Dotação Orçamentária informada pelo Cliente na abertura (opcional)" [TextBox String → CPE_CONTRATOS.DOTACAO1]
  - CONTA_CONTABIL1 "Parecer Contabilidade" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1] obrigatório
  - PARECER_QUALIF "Consulta Orçamentária" [Memo String → CPE_FINANCEIRO.PARECER_QUALIF] obrigatório
  - CONTA_ORCAMENTARIA "Conta Orçamentária" [TextBox String → CPE_CSC.CONTA_ORCAMENTARIA]
  - SIM_NAO14 "A Conta Orçamentária possui saldo?" [DropDownList String → CPE_CONTRATOS.SIM_NAO14] obrigatório
  - SIM_NAO20 "Refere-se a Conta de Investimento?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO20] obrigatório
  - CSC_ESCOLARIDADE "Informações Orçamentárias (O cliente deve preencher este campo em caso de remanejamento orçamentário e/ou alteração de UOR, com "de acordo" do gestor dela se necessário. Caso não haja remanejamento orçamentário, preencher com "Não se aplica".)" [TextBox String → CPE_CSC.CSC_ESCOLARIDADE]

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
### papel 539: Fila CSC - Prestação de Serviços
Tipo=RelacaoPessoas | pessoas: Fila CSC - Prestação de Serviços
### papel 631: Cliente e Gerente Posição
Tipo=Composto
- composto por: Gerente Posição do Cliente (Script)
- composto por: Cliente (PessoaOrdemServico)
### papel 1379: Favorecido Todos 2
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Aprovador
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_TODOS_2"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS_2")))

    if favorecido != None:
        Atores.Adiciona(favorecido, "Aprovador")
```
### papel 842: Aprovadores Projeto Básico
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
#pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, APROVADORES FROM Z_00143_APROVADOR_PB WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")

tentativa = 0

while tentativa < 5:
    pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, APROVADORES FROM Z_00143_APROVADOR_PB WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
    tentativa = tentativa + 1
    for pessoa in pesquisa01.Rows:    
        aprovadores = Pessoa.Carrega(Convert.ToInt32(pessoa["APROVADORES"]))
        Atores.Adiciona(aprovadores)
```
### papel 1359: Gerente Divisão Gesap
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
query = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL, ORGAO.SIGLA, PESSOA.ID_PESSOA From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Where CP_PESSOA.CARGO_FUNCIONAL Like '%DIVISAO' And ORGAO.SIGLA = '3000003154'")

for i in query.Rows:
    id = Convert.ToInt32(i['ID_PESSOA'])
    pessoa = Pessoa.Carrega(id)
    Atores.Adiciona(pessoa)
```
### papel 730: Gerente - PPGEREX_NEGOCIO
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
ator = DB.ExecuteScalar("SELECT CPO.PPGEREX_NEGOCIO FROM CP_ORDEM_SERVICO CPO WHERE CPO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"' ")

if ator != DBNull.Value:
    if ator != None and ator != '' :
        gerente = Convert.ToInt32(ator)
        #Atores.Adiciona(Pessoa.Carrega("Id", 3))
        Atores.Adiciona(Pessoa.Carrega("Id", gerente))
else:
    Atores.Adiciona(Pessoa.Carrega("Id", 3))

#----------------------------------------

#ator = DB.ExecuteScalar("SELECT CPO.PPGEREX_NEGOCIO FROM CP_ORDEM_SERVICO CPO WHERE CPO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString.()+"' ")
#
#if ator != None:
##for at in ator:
#    gerente = Convert.ToInt32(ator)
#
#    Atores.Adiciona(Pessoa.Carrega("Id", gerente))


#pesquisa = DB.ExecuteDataTable("select ID_OCORRENCIA, PPGEREX_NEGOCIO FROM CP_ORDEM_SERVICO WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
#
#for pessoa in pesquisa:
#    fiscalServico = Pessoa.Carrega(Convert.ToInt32(pessoa["PPGEREX_NEGOCIO"])) 
#
#    Atores.Adiciona(fiscalServico)


#gestor = DB.ExecuteScalar("SELECT CPO.GESTORES_INT_02 FROM CP_ORDEM_SERVICO CPO WHERE CPO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"'")
#if gestor != None:    Atores.Adiciona(Pessoa.Carrega("Id", gestor))
#
```
### papel 254: Fila Contabilidade
Tipo=RelacaoPessoas | pessoas: Fila CONTABILIDADE
### papel 544: Cliente e Responsavel Atual
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Responsável atual (PessoaOrdemServico)
### papel 1143: Fila Pendencia de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação
### papel 1381: Gerente Gemac
Tipo=RelacaoPessoas | pessoas: ALLINE MENDONCA BARRETO

## Campos customizados usados (definição global)

### SIM_NAO6 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO6
Itens: Sim;Não

### JUSTIFICATIVA_TENDENCIA — Justificativa tendência
Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_TENDENCIA

### JUSTIFICATIVA_IMPACTO — Justificativa do retorno financeiro anual estimado 
Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMPACTO
Descrição: Justificativa do retorno financeiro anual estimado

### JUSTIFICATIVA_IMAGEM — Justificativa da promoção da imagem
Memo String → CP_ORDEM_SERVICO.JUSTIFICATIVA_IMAGEM

### SIM_NAO1 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO1
Itens: Sim;Não

### OBS6 — Observação6
Memo String(2000) → CPE_CSC.OBS6

### FQ415_066_ITEM31 — FQ415-066 Item 3.1
DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM31
Itens: Sim;Não;Não se aplica

### FQ415_066_ITEM32 — FQ415-066 Item 3.2
DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM32
Itens: Sim;Não;Não se aplica

### FQ415_066_ITEM321 — FQ415-066 Item 3.2.1
DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM321
Itens: Sim;Não;Não se aplica

### FQ415_066_ITEM322 — FQ415-066 Item 3.2.2
DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM322
Itens: Sim;Não;Não se aplica

### TIPO_DE_VALOR_DE_REFERENCIA — Tipo de Valor de Referência
DropDownList String(50) → CPE_CONTRATOS02.TIPO_DE_VALOR_DE_REFERENCIA
Itens: Média;Mediana;Menor Preço;Não se aplica;Maior Preço;Outros:

### FQ415_066_ITEM33 — FQ415-066 Item 3.3
DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM33
Itens: Sim;Não;Não se aplica

### FQ415_066_ITEM331 — FQ415-066 Item 3.3.1
DropDownList String → CPE_HOMOLOGACAO.FQ415_066_ITEM331
Itens: Sim;Não;Não se aplica

### CSC_DGCO — DGCO
TextBox String → CPE_CSC.CSC_DGCO

### PENF_EMAIL — E-mails que serão notificados sobre o andamento da ordem de serviço (separados por ponto e vírgula)
TextBox String(2000) → CPE_PENF.PENF_EMAIL

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### SIM_NAO5 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO5
Itens: Sim;Não

### COMBOBOX10 — Combo Box
DropDownList String(900) → CPE_HOMOLOGACAO.COMBOBOX10
Itens: Custo;Investimento;Despesa;Inventário

### CONTA_CONTABIL1 — Conta Contábil
TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1

### CSC_ESCOLARIDADE — Escolaridade
TextBox String → CPE_CSC.CSC_ESCOLARIDADE

### VALOR_DOD — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD
Descrição: Valor do orçamento

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### SIM_NAO10 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO10
Itens: Sim;Não

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### SIM_NAO_100 — Sim ou Não
DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100
Itens: Sim;Não

### SIM_NAO7 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO7
Itens: Sim;Não

### PPGEREX_NEGOCIO — Gerente Executivo do Negócio
DropDownList String → CP_ORDEM_SERVICO.PPGEREX_NEGOCIO
**LookupScript**
```python
#Itens = DB.ExecuteDataTable("Select Distinct to_char(PESSOA.ID_PESSOA) as id_pessoa,PESSOA.NOME_ABREVIADO From ORGAO Inner Join PESSOA On ORGAO.ID_GESTOR = PESSOA.ID_PESSOA Where ORGAO.ATIVO = 'Sim' And ORGAO.DESCRICAO Like '%GERE%' And PESSOA.ATIVO = 'Sim' Order By PESSOA.NOME_ABREVIADO")

Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(pessoa.id_pessoa) AS id_pessoa, pessoa.nome_abreviado FROM orgao INNER JOIN pessoa ON orgao.id_gestor = pessoa.id_pessoa INNER JOIN cp_pessoa ON cp_pessoa.id_pessoa = pessoa.id_pessoa WHERE (orgao.ativo = 'Sim' AND cp_pessoa.cargo_funcional LIKE '%EXECUTIVO%' AND pessoa.ativo = 'Sim') or pessoa.id_pessoa in (SELECT p.id_substituto_aprovacao FROM pessoa p INNER JOIN cp_pessoa   cp ON ( p.id_pessoa = cp.id_pessoa ) WHERE cp.cargo_funcional LIKE '%EXECUTIVO%' AND p.ativo = 'Sim' AND sysdate BETWEEN dt_inicio_substit_aprov AND dt_fim_substit_aprov) ORDER BY pessoa.nome_abreviado")
```

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

### DIRETORIA_GERENCIA — Diretoria/Gerência
TextBox String → CPE_CSC.DIRETORIA_GERENCIA

### LOCALIDADE_MOV — Localidade Movimentação
TextBox String(500) → CP_ORDEM_SERVICO.LOCALIDADE_MOV

### CODIGO_ITEM — Código do Item
DataGrid RecordList → Z_00143_CODIGO_ITEM.CODIGO_ITEM
Colunas do registro:
- ITEM_OBSOLETO "Item Obsoleto?" [DropDownList String] itens: Sim;Não
- ITEM "Código do Item" [DropDownList String]
**ITEM.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT segment1 || ' - ' || segment2 || ' - ' || description as produto FROM mtl_system_items_b WHERE organization_id = '88' AND enabled_flag = 'Y'")
```

### PB_OBJETO_CONTRATACAO — Descrever o objeto de forma global, tal como deve constar na ordem de compra. A definição do objeto deve ser feita da forma mais clara e precisa possível, a fim de garantir que a compra ou contratação seja realizada da forma pretendida pelo demandante.
Memo String(2000) → CPE_CONTRATOS.PB_OBJETO_CONTRATACAO

### TIPO_ATIVIDADE — Tipo de Atividade - informe
DropDownList String → CPE_CSC.TIPO_ATIVIDADE
Descrição: Tipo de Atividade - Informe
Itens: Atividade Meio; Atividade Fim; Não se Aplica

### UOR — UOR
DataGrid RecordList → Z_00143_UOR.UOR
Colunas do registro:
- UOR "UOR" [DropDownList String] itens: Itens=DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO")
**UOR.LookupScript**
```python
Itens=DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO")
```

### SIM_NAO4 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO4
Itens: Sim;Não

### QTD_PESQUISA — Quantidade de Pesquisas
DropDownList String → CPE_CSC.QTD_PESQUISA
Itens: 0;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20

### VALOR_REFERENCIAL — Valor Referencial
DataGrid RecordList → Z_00143_VALOR_REFERENCIAL.VALOR_REFERENCIAL
Colunas do registro:
- ITEM "Código do Item" [TextBox String]
- VALOR_REFERENCIAL "Valor Referencial" [DropDownList String] itens: Média;Mediana;Maior Preço;Menor Preço;Não se aplica;Outros
- VALOR_TOTAL "Valor Total" [TextBox Decimal]
- VALOR_UNITARIO "Valor Referencial Unitário" [TextBox String]
- ITEM1 "Código do Item" [DropDownList String]
**ITEM1.LookupScript**
```python
##
```

### APROVADOR_PB — Vistoriador dos Bens (no mínimo 3, sendo um o gestor de patrimônio)
DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB
Colunas do registro:
- APROVADORES "Aprovadores" [DropDownList String]
**APROVADORES.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### OBS21 — Observação21
Memo String(4000) → CPE_CSC.OBS21

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### OBS22 — Observação22
Memo String(4000) → CPE_CSC.OBS22

### OBS23 — Observação23
Memo String(4000) → CPE_CSC.OBS23

### OBS10 — Observação10
Memo String(2000) → CPE_CSC.OBS10

### OBS4 — Observação4
Memo String(2000) → CPE_CONTRATOS.OBS4
Descrição: Informe

### OBS7 — Informe
Memo String(2000) → CPE_CSC.OBS7

### INFORMACAO_FATURAMENTO — Informações para Faturamento
DataGrid RecordList → Z_00143_INFORMACAO_FATURAMENTO.INFORMACAO_FATURAMENTO
Colunas do registro:
- CNPJ_BBTS "CNPJ BBTS" [TextBox String]
- INSCRICAO_ESTADUAL "Inscrição Estadual ou Distrital" [TextBox String]
- INSCRICAO_MUNICIIPAL "Inscrição Municipal" [TextBox String]
- ENDERECO "Endereço" [Memo String]

### OBS3 — Observação3
Memo String(2000) → CPE_CONTRATOS.OBS3
Descrição: Informe

### OBS5 — Observação5
Memo String(2000) → CPE_CONTRATOS.OBS5

### OBS50 — Observação50
Memo String(2000) → CPE_CONTRATOS.OBS50

### NN_CONDICAO_PAGAMENTO — Condição de Pagamento
Memo String(2000) → CP_ORDEM_SERVICO.NN_CONDICAO_PAGAMENTO
Descrição: Condição de Pagamento DA CONTRATAÇÃO

### LABEL12 — LABEL12
Label String(700) → CPE_PDCI2019.LABEL12

### LABEL10 — LABEL10
Label String(700) → CPE_PDCI2019.LABEL10

### LABEL56 — LABEL56
Label String(500) → CPE_CSC.LABEL56

### LABEL11 — LABEL11
Label String(700) → CPE_PDCI2019.LABEL11

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### LISTA_ITENS_PESQ_MERC — Lista de itens
DropDownList String → CPE_CSC.LISTA_ITENS_PESQ_MERC
Descrição: Lista de itens - Pesquisa de Mercado
Itens: Aluguel;Aquisição de acessórios e suprimentos para informática (mouse, teclado, tonner de impressora, etc);Aquisição de Eletrodomésticos (ar condicionado, cafeteira, geladeiras, microondas, etc);Aquisição de peças e sobressalentes;Aquisição de software (aplicativos e programas de computador);Artes Visuais e Eventos;Ata de Registro de Preço;Conservação e limpeza;Insumos para microfilmagem;Locação de equipamentos;Manutenção de elevadores;Manutenção Predial;Material de expediente;Outros (especificar detalhadamente);Postos de serviços - microfilmagem e call center;Segurança do trabalho;Segurança e…

### DESCRICAO_OBRIG — Descrição obrigatória
TextBox String(2000) → CP_ORDEM_SERVICO.DESCRICAO_OBRIG
Descrição: Breve descrição

### SERV_ART_29_LEI_13303 — Serviços do art. 29 da Lei 13.303/2016
DropDownList String → CPE_CSC.SERV_ART_29_LEI_13303
Descrição: Serviços do art. 29 da Lei 13.303/2016, Inc. I e II?
Itens: Sim;Não

### LABEL57 — LABEL57
Label String(1500) → CPE_CSC.LABEL57

### LABEL13 — LABEL13
Label String(700) → CPE_PDCI2019.LABEL13

### LABEL55 — LABEL55
Label String(500) → CPE_CSC.LABEL55

### PESQUISA_MERCADO4 — Pesquisa de Mercado
DataGrid RecordList → Z_00143_PESQUISA_MERCADO4.PESQUISA_MERCADO4
Colunas do registro:
- UDM "Unidade de Medida" [DropDownList String] itens: UN;SRV;ANO;CX;CM;CM3;CT;DIA;GL;G;H;LC;L;M2;ME;M;M3;MI;ML;MM;MM3;MIN;PCT;PC;KG;KM;RA;RL;S
- QUANTIDADE "Quantidade" [TextBox Decimal]
- ITEM "Código do Item" [TextBox String]
- DESCRICAO_ITEM "Descrição do Item" [TextBox String]
- NUMERO "Número do Produto/Serviço" [DropDownList String] itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60
- VALOR_UNITARIO "Valor Unitário" [TextBox Decimal]
- VALOR "Valor Total" [TextBox Decimal]
- ITEM1 "Código do Item" [DropDownList String]
**ITEM1.LookupScript**
```python
##
```

### FORNECEDOR5 — Fornecedor
TextBox String → CPE_CSC.FORNECEDOR5

### PESQUISA_MERCADO_5 — Pesquisa de Mercado
DataGrid RecordList → Z_00143_PESQUISA_MERCADO_5.PESQUISA_MERCADO_5
Colunas do registro:
- NUMERO "Número do Produto/Serviço" [DropDownList String] itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60
- ITEM1 "Código do Item" [DropDownList String]
**ITEM1.LookupScript**
```python
##
```
- ITEM "Código do Item" [TextBox String]
- DESCRICAO_ITEM "Descrição do Item" [TextBox String]
- QUANTIDADE "Quantidade" [TextBox Decimal]
- VALOR_UNITARIO "Valor Unitário" [TextBox Decimal]
- VALOR "Valor Total" [TextBox Decimal]
- UDM "Unidade de Medida" [DropDownList String] itens: UN;SRV;ANO;CX;CM;CM3;CT;DIA;GL;G;H;LC;L;M2;ME;M;M3;MI;ML;MM;MM3;MIN;PCT;PC;KG;KM;RA;RL;S

### FORNECEDOR6 — Fornecedor 6
TextBox String → CPE_CSC.FORNECEDOR6

### PESQUISA_MERCADO6 — Pesquisa de Mercado
DataGrid RecordList → Z_00143_PESQUISA_MERCADO6.PESQUISA_MERCADO6
Colunas do registro:
- UDM "Unidade de Medida" [DropDownList String] itens: UN;SRV;ANO;CX;CM;CM3;CT;DIA;GL;G;H;LC;L;M2;ME;M;M3;MI;ML;MM;MM3;MIN;PCT;PC;KG;KM;RA;RL;S
- QUANTIDADE "Quantidade" [TextBox Decimal]
- ITEM "Código do Item" [TextBox String]
- DESCRICAO_ITEM "Descrição do Item" [TextBox String]
- VALOR_UNITARIO "Valor Unitário" [TextBox Decimal]
- VALOR "Valor Total" [TextBox Decimal]
- ITEM1 "Código do Item" [DropDownList String]
**ITEM1.LookupScript**
```python
##
```
- NUMERO1 "Numero do Produto/Serviço" [DropDownList String] itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60

### PESQUISA_MERCADO1 — Pesquisa de Mercado
DataGrid RecordList → Z_00143_PESQUISA_MERCADO1.PESQUISA_MERCADO1
Colunas do registro:
- QUANTIDADE "Quantidade" [TextBox Decimal]
- VALOR_UNITARIO "Valor Unitário" [TextBox Decimal]
- UDM "Unidade de Medida" [DropDownList String] itens: UN;SRV;ANO;CX;CM;CM3;CT;DIA;GL;G;H;LC;L;M2;ME;M;M3;MI;ML;MM;MM3;MIN;PCT;PC;KG;KM;RA;RL;S
- ITEM "Código do Item" [TextBox String]
- DESCRICAO_ITEM "Descrição do Item" [TextBox String]
- VALOR "Valor Total" [TextBox Decimal]
- ITEM1 "Código do Item" [DropDownList String]
**ITEM1.LookupScript**
```python
##
```
- NUMERO "Número do Produto/Serviço" [DropDownList String] itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60

### FORNECEDOR2 — Fornecedor
TextBox String → CPE_CSC.FORNECEDOR2

### FORNECEDOR4 — Fornecedor
TextBox String → CPE_CSC.FORNECEDOR4

### PESQUISA_MERCADO2 — Pesquisa de Mercado
DataGrid RecordList → Z_00143_PESQUISA_MERCADO2.PESQUISA_MERCADO2
Colunas do registro:
- QUANTIDADE "Quantidade" [TextBox Decimal]
- UDM "Unidade de Medida" [DropDownList String] itens: UN;SRV;ANO;CX;CM;CM3;CT;DIA;GL;G;H;LC;L;M2;ME;M;M3;MI;ML;MM;MM3;MIN;PCT;PC;KG;KM;RA;RL;S
- NUMERO "Número do Produto/Serviço" [DropDownList String] itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60
- ITEM "Código do Item" [TextBox String]
- DESCRICAO_ITEM "Descrição do Item" [TextBox String]
- VALOR_UNITARIO "Valor Unitário" [TextBox Decimal]
- VALOR "Valor Total" [TextBox Decimal]
- ITEM1 "Código do Item" [DropDownList String]
**ITEM1.LookupScript**
```python
##
```

### FORNECEDOR3 — Fornecedor
TextBox String → CPE_CSC.FORNECEDOR3

### PESQUISA_MERCADO3 — Pesquisa de Mercado
DataGrid RecordList → Z_00143_PESQUISA_MERCADO3.PESQUISA_MERCADO3
Colunas do registro:
- QUANTIDADE "Quantidade" [TextBox Decimal]
- UDM "Unidade de Medida" [DropDownList String] itens: UN;SRV;ANO;CX;CM;CM3;CT;DIA;GL;G;H;LC;L;M2;ME;M;M3;MI;ML;MM;MM3;MIN;PCT;PC;KG;KM;RA;RL;S
- NUMERO "Número do Produto/Serviço" [DropDownList String] itens: 1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;51;52;53;54;55;56;57;58;59;60
- ITEM "Código do Item" [TextBox String]
- DESCRICAO_ITEM "Descrição do Item" [TextBox String]
- VALOR_UNITARIO "Valor Unitário" [TextBox Decimal]
- VALOR "Valor Total" [TextBox Decimal]
- ITEM1 "Código do Item" [DropDownList String]
**ITEM1.LookupScript**
```python
###
```

### FORNECEDOR01 — Fornecedor
TextBox String → CPE_CSC.FORNECEDOR01

### LABEL6 — LABEL6
Label String(1500) → CPE_PDCI2019.LABEL6

### CONTA_ORCAMENTARIA — Conta Orçamentária
TextBox String → CPE_CSC.CONTA_ORCAMENTARIA

### PARECER_QUALIF — Parecer - Qualificação Financeira
Memo String → CPE_FINANCEIRO.PARECER_QUALIF

### LABEL150 — LABEL150
Label String(1500) → CPE_PDCI2019.LABEL150

### FAVORECIDO_TODOS_2 — Favorecido
DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_2
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

### LISTA_VALOR_REF_UNIT — Valor referencial do Projeto Basico
Memo String(2000) → CPE_CSC.LISTA_VALOR_REF_UNIT

### TABELA_DADOS_CONTRATOS_C — Tabela de Dados Contratuais
Memo String(2000) → CPE_CSC.TABELA_DADOS_CONTRATOS_C

### APROVACOES — Campo para preenchimento das aprovações.
Memo String(2000) → CPE_CSC.APROVACOES
Descrição: APROVACOES

### TABELA_HTML_INFO_FATURAMENTO — Tabela HTML de informações de faturamento
Memo String(2000) → CPE_CSC.TABELA_HTML_INFO_FATURAMENTO

### CSC_LOGRADOURO — Logradouro
TextBox String(500) → CPE_CSC.CSC_LOGRADOURO

### OBS24 — Observação24
Memo String(2000) → CPE_CSC.OBS24

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### NUMERO_OC — Número da OC
TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC

### MODALIDADE_LICITACAO — Modalidade de Licitação
TextBox String → CP_ORDEM_SERVICO.MODALIDADE_LICITACAO

### NUMERO_RC — Número da RC
TextBox String → CPE_CSC.NUMERO_RC

### FAVORECIDO_TODOS_03 — Favorecido
DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_03
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

### LABEL108 — LABEL108
Label String(500) → CPE_CONTRATOS.LABEL108

### LABEL100 — Label100
Label String(1000) → CPE_CONTRATOS.LABEL100

### LABEL107 — LABEL107
Label String(1000) → CPE_CONTRATOS.LABEL107

### CHECKBOX8 — Checkbox8
CheckBox Boolean → CPE_PESSOAS.CHECKBOX8

### LABEL21 — LABEL21
Label String(700) → CPE_PDCI2019.LABEL21

### CHECKBOX9 — Checkbox9
CheckBox Boolean → CPE_PESSOAS.CHECKBOX9
Descrição: Checkbo9

### LABEL30 — LABEL30
Label String(700) → CPE_PDCI2019.LABEL30

### LABEL31 — LABEL31
Label String → CPE_PDCI2019.LABEL31

### SIM_NAO201 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO201
Itens: Sim;Não

### SIM_NAO202 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO202
Itens: Sim;Não

### SIM_NAO203 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO203
Itens: Sim;Não

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

### LABEL112 — LABEL112
Label String(500) → CPE_CONTRATOS.LABEL112

### LABEL113 — LABEL113
Label String(1000) → CPE_CONTRATOS02.LABEL113

### AREA_GESTORA_ITEM — A área é gestora do item?
DropDownList String → CPE_CONTRATOS.AREA_GESTORA_ITEM
Itens: Sim;Não (Item Orçamentário Centralizado);Não (Item Orçamentário Descentralizado)

### LABEL101 — LABEL101
Label String(1300) → CPE_HOMOLOGACAO.LABEL101

### DOTACAO1 — Dotação
TextBox String → CPE_CONTRATOS.DOTACAO1

### GESTOR_DE_ITENS_GESAP — Gestor de Itens Gesap
DropDownList String(2000) → CPE_CONTRATOS02.GESTOR_DE_ITENS_GESAP
Itens: Aluguel (Bens Imóveis);Aluguel (Bens Móveis);Anúncios e Editais;Aplicação de Peças;Benfeitorias;Deslocamento a Serviço;Despesas Financeiras;Equip. Proc. Dados;Equipamentos/Móveis/Utensílios;Estoque (Impressão);Estoque (Manutenção);Fretes;Horas Extras;Imp.s/Apl.peças;Impostos/Deduções;Instalações;Licenças de Software - Uso Exclusivo Área;Licenças de Software - Uso Infra TI;Manut. e Conservação;Manutenção Especializada;Máq. Equipamentos;Máq. Equipamentos - Atividade fim;Marketing;Mat. Expediente;Móveis e utensílios;Multas Clientes;Multas Fornecedor;Novos Negócios;Pessoal;Plano de Saúde;Revenda d…

### SIM_NAO20 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO20
Itens: Sim;Não

### DATA_ENTREGA — Data de entrega
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENTREGA
Descrição: Data prevista para entrega

### CSC_CPF — CPF
TextBox String(300) → CPE_CSC.CSC_CPF

### LABEL25 — LABEL25
Label String(1000) → CPE_PDCI2019.LABEL25

### TEXT2 — TEXT2
TextBox String → CPE_CSC.TEXT2

### SERVICO_ITENS_CADASTRADOS — Serviço para Itens Cadastrados
DropDownList String → CPE_CONTRATOS02.SERVICO_ITENS_CADASTRADOS
Itens: Itens Administrativos;
Serviços Contratados pela BBTS

### PRJ_SRC_USUARIO — SRC/Descrição/Localidade
TextBox String → CPE_PRJ_BB.PRJ_SRC_USUARIO

### PRJ_CODIGO_ITEM — Código do Item
TextBox String → CPE_PRJ_BB.PRJ_CODIGO_ITEM

### PRJ_TIPO_SOLICITACAO — Tipo de solicitação
DropDownList String → CPE_PRJ_BB.PRJ_TIPO_SOLICITACAO
Itens: Cadastrar;Alterar;Inativar;Reativar

### PRJ_CODIGO_ITENS — Código dos Itens
DataGrid RecordList → Z_00186_PRJ_CODIGO_ITENS.PRJ_CODIGO_ITENS
Colunas do registro:
- COD_ITEM "Código do Item" [TextBox String]

### PRJ_DESC_ITEM — Descrição do Item
TextBox String → CPE_PRJ_BB.PRJ_DESC_ITEM

### PRJ_UNI_MEDIDA — Unidade de Medida
DropDownList String → CPE_PRJ_BB.PRJ_UNI_MEDIDA
**LookupScript**
```python
from Venki.Services.Dictionary.Custom import Class
#select teste
Itens = DB.ExecuteDataTable("SELECT UOM_CODE, UNIT_OF_MEASURE_TL || '-' || UOM_CLASS FROM LISTA_UNIDADE_MEDIDA ORDER BY UNIT_OF_MEASURE_TL")

#select doc item 5.4
#Itens = DB.ExecuteDataTable("SELECT a.unit_of_measure_tl AS 'Unidade de Medida',a.uom_code AS 'Código da UDM',a.uom_class AS 'Classe' FROM mtl_units_of_measure_tl a WHERE LANGUAGE = userenv('LANG') AND disable_date IS NULL AND created_by <> 120 order by 1")
```

### PRJ_PATRIMONIADO — Patrimoniado
DropDownList String → CPE_PRJ_BB.PRJ_PATRIMONIADO
Itens: Sim;Não

### PRJ_ORIGEM_ITEM — Origem do Item
DropDownList String → CPE_PRJ_BB.PRJ_ORIGEM_ITEM
**LookupScript**
```python
#select teste
Itens = DB.ExecuteDataTable("SELECT origem_do_item, origem_do_item || '-' || descricao FROM lista_origem_item order by origem_do_item")

#select lista item 5.5
#Itens = DB.ExecuteDataTable("SELECT lookup_code as origem_do_item,meaning as descricao FROM fnd_lookups WHERE lookup_type = 'JLBR_ITEM_ORIGIN' AND nvl(end_date_active, SYSDATE + 1) > SYSDATE")
```

### PRJ_CATEGORIA_NCM — Categoria NCM
DropDownList String → CPE_PRJ_BB.PRJ_CATEGORIA_NCM
**LookupScript**
```python
#select teste
Itens = DB.ExecuteDataTable("SELECT lookup_code, lookup_code || '-' || description FROM lista_categoria_ncm order by lookup_code")

#Select lista item 5.6
#Itens = DB.ExecuteDataTable("SELECT fl.lookup_code,DESCRIPTION FROM fnd_lookups fl WHERE fl.lookup_type = 'JLZZ_AR_TX_FISCAL_CLASS_CODE' AND nvl(fl.start_date_active, SYSDATE) <= SYSDATE AND nvl(fl.end_date_active SYSDATE) >= SYSDATE AND fl.enabled_flag = 'Y' AND EXISTS (SELECT 1 FROM jl_zz_ar_tx_fsc_cls_all fc WHERE org_id = fnd_profile.value('ORG_ID') AND fc.fiscal_classification_code = fl.lookup_code AND fc.enabled_flag = 'Y')")
```

### PRJ_OBS — Observação
Memo String → CPE_PRJ_BB.PRJ_OBS

### SIM_NAO11 — Sim ou Não
DropDownList String → CPE_CONTRATOS.SIM_NAO11
Itens: Sim;
Não

### PAHL_VOUCHER_CARRO — Voucher de Locação de Carro
TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO

### CODIGO_DO_SERVICO — Código do Serviço
TextBox Integer → CPE_CSC.CODIGO_DO_SERVICO

### SIM_NAO14 — Sim ou Não
DropDownList String → CPE_CONTRATOS.SIM_NAO14
Itens: Sim;
Não

### PENF_FORNECEDOR — Fornecedor
DropDownList String → CPE_PENF.PENF_FORNECEDOR
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT cnpj, cnpj || '/' || trim(nome) fornecedor FROM VW_BBTS_PO_CADASTRO_FORNEC WHERE ATIVO = 'A' and tipo_contribuinte <> 'FUNCIONARIO' order by nome")

#Itens = DB.ExecuteDataTable("Select 'Faltam permissões para VW_BBTS_PO_CADASTRO_FORNEC' teste from dual")
```

### FORNECEDOR_CADASTRADO — Fornecedor Cadastrado
DropDownList String → CPE_CONTRATOS02.FORNECEDOR_CADASTRADO
Itens: Sim, já cadastrado;Não, cadastrar fornecedor;Sim, atualizar cadastro

### NUMERO_DE_OC — Número de OC
TextBox String(50) → CPE_CONTRATOS.NUMERO_DE_OC

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
