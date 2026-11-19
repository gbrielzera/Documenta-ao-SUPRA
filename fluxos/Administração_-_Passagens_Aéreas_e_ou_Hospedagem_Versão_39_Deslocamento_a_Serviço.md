# Fluxo: Deslocamento a Serviço (DESLOCAMENTO0) — versão 39
Caminho: Fluxos > Administração - Passagens Aéreas e ou Hospedagem Versão 39 Deslocamento a Serviço
XML: `XMLs para teste/Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço.xml` | Supravizio 19.1.1 | SubProcessoId 21542 | DesenhoProcessoId 2962 | ProcessoId 103
Órgão dono: 3000009430 - DIVISAO DE GERENCIAMENTO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: Objetivo=Deslocamento a Serviço; DescricaoCliente=Deslocamento a Serviço; MetodoPriorizacaoId=2; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Deslocamento a Serviço; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Deslocamento a Serviço (DESLOCAMENTO)

## Grafo do fluxo
- [369136] LinkInicial "chatbot" {Fila CSC - Passagens Aéreas e Hospedagem} → [369130] Preencher dados
- [369137] FimCancelamento "" → (fim)
- [369138] EventoIntermediarioRegra "" → [369120] Inserir dados no ERP

- [369125] Tarefa "Realizar reserva no sistema


" {Fila CSC - Passagens Aéreas e Hospedagem} → [G82662] Reserva realizada?
- [369128] EventoFinal "" {Responsável atual} → (fim)
- [369129] FimCancelamento "" → (fim)
- [369130] Tarefa "Preencher dados" {Fila CSC - Passagens Aéreas e Hospedagem} → [369123] Aprovar Deslocamento - Gerente Favorecido
- [369120] Tarefa "Inserir dados no ERP
" {Responsavel Processo} → [369135] Realizar Prestação de Contas
- [369121] EventoIntermediarioMensagem "Envio do Voucher" → [G82657] Viagem internacional?
- [369122] EventoInicial "" {Cliente} → [369123] Aprovar Deslocamento - Gerente Favorecido
- [369123] Tarefa "Aprovar Deslocamento - Gerente Favorecido" {Fila CSC - Pendente de Aprovação} → [G82660] Deslocamento aprovado?
- [369124] EventoFinal "" {Responsavel Processo} → (fim)
- [369126] EventoIntermediarioMensagem "Reserva não realizada" → [369128] 
- [369127] Tarefa "Incluir informações da Reserva" {Responsável atual} → [369121] Envio do Voucher
- [369131] Tarefa "Aprovar Deslocamento - Diretor do Favorecido" {Fila CSC - Pendente de Aprovação} → [G82663] Diretor aprovou?
- [369132] SubProcesso "Publicação no DOU" {Responsável atual} → [369120] Inserir dados no ERP

- [369133] Tarefa "Aguardando data valida para pagamento" {Responsavel Processo} → [369138]  | [369120] Inserir dados no ERP

- [369134] Tarefa "Aprovar valor de atencipação de deslocamento maior que R$5000,00" {Fila CSC - Pendente de Aprovação} → [G82664] Gereg/Gediv/Super aprovou?
- [369135] SubProcesso "Realizar Prestação de Contas" {Responsavel Processo} → [369140] Configurar ponto eletrônico
- [369140] EventoIntermediarioMensagem "Configurar ponto eletrônico" → [369124] 
- [G82656] Gateway "Haverá aquisição de passagens e/ou hospedagens e/ou locação de carro?" → «Sim» [G82667] Haverá aquisição de passagens? | «Não» [G82666] Haverá Adiantamento de valores?
- [G82657] Gateway "Viagem internacional?" → «Não» [369133] Aguardando data valida para pagamento | «Sim» [369132] Publicação no DOU
- [G82658] Gateway "Assistência Técnica" → «Não» [G82659] Pedido da reserva menor ou igual a 30 dias da data | «Sim» [369125] Realizar reserva no sistema



- [G82659] Gateway "Pedido da reserva menor ou igual a 30 dias da data da reserva?" → «Sim» [G82668] Presidente, Diretor, Conselheiro, Gerex, Gereg ? | «Não» [369125] Realizar reserva no sistema



- [G82660] Gateway "Deslocamento aprovado?" → «Aprovado» [G82661] Presi, Diretor, Conselheiro, 
Gerex, Super, Gereg, | «Reprovado» [369129] 
- [G82661] Gateway "Presi, Diretor, Conselheiro, 
Gerex, Super, Gereg, Gediv?" → «Sim» [G82656] Haverá aquisição de passagens e/ou hospedagens e/o | «Não» [G82665] Adiantamento superior a R$5000,00?
- [G82662] Gateway "Reserva realizada?" → «Sim» [369127] Incluir informações da Reserva | «Não» [369126] Reserva não realizada
- [G82663] Gateway "Diretor aprovou?" → «Reprovado» [369137]  | «Aprovado» [369125] Realizar reserva no sistema



- [G82664] Gateway "Gereg/Gediv/Super aprovou?" → «Reprovado» [369129]  | «Aprovado» [G82656] Haverá aquisição de passagens e/ou hospedagens e/o
- [G82665] Gateway "Adiantamento superior a R$5000,00?" → «Não» [G82656] Haverá aquisição de passagens e/ou hospedagens e/o | «Sim» [369134] Aprovar valor de atencipação de deslocamento maior
- [G82666] Gateway "Haverá Adiantamento de valores?" → «Sim» [G82657] Viagem internacional? | «Não» [369135] Realizar Prestação de Contas
- [G82667] Gateway "Haverá aquisição de passagens?" → «Sim» [G82658] Assistência Técnica | «Não» [369125] Realizar reserva no sistema



- [G82668] Gateway "Presidente, Diretor, Conselheiro, Gerex, Gereg ?" → «Sim» [369125] Realizar reserva no sistema


 | «Não» [369131] Aprovar Deslocamento - Diretor do Favorecido

## Gateways
### [G82656] Haverá aquisição de passagens e/ou hospedagens e/ou locação de carro? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["PAHL_HOSPEDAGENS"] == True or OrdemServico["PAHL_LOCACOES"] == True or OrdemServico["PAHL_PASSAGENS"] == True
```
- alternativa → [G82667] Haverá aquisição de passagens?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G82666] Haverá Adiantamento de valores?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82657] Viagem internacional? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["TIPO_DESLOCAMENTO"] == "Viagem a Serviço - Internacional"
```
- alternativa → [369133] Aguardando data valida para pagamento: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [369132] Publicação no DOU: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G82658] Assistência Técnica (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['TIPO_DESLOCAMENTO'] == "Viagem - Assistência Técnica" or OrdemServico['TIPO_DESLOCAMENTO'] == "Treinamento - Assistência Técnica"
```
- alternativa → [G82659] Pedido da reserva menor ou igual a 30 dias da data: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [369125] Realizar reserva no sistema


: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G82659] Pedido da reserva menor ou igual a 30 dias da data da reserva? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["SAIDA"].Date.AddDays(-29) <= DateTime.Now.Date
```
- alternativa → [G82668] Presidente, Diretor, Conselheiro, Gerex, Gereg ?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [369125] Realizar reserva no sistema


: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82660] Deslocamento aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR_DESLOCAMENTO")
```
- alternativa → [G82661] Presi, Diretor, Conselheiro, 
Gerex, Super, Gereg,: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [369129] : OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82661] Presi, Diretor, Conselheiro, 
Gerex, Super, Gereg, Gediv? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["CARGO_DESLOCAMENTO"] == "PRESIDENTE" or OrdemServico["CARGO_DESLOCAMENTO"] == "DIRETOR" or OrdemServico["CARGO_DESLOCAMENTO"] == "GERENTE EXECUTIVO" or OrdemServico["CARGO_DESLOCAMENTO"] == "GERENTE DE DIVISAO" or OrdemServico["CARGO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["CARGO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["CARGO_DESLOCAMENTO"] == "CONSELHEIRO FISCAL" or OrdemServico["CARGO_DESLOCAMENTO"] == "SUPERINTENDENTE" or OrdemServico["CARGO_DESLOCAMENTO"] == "GERENTE REGIONAL DE OPERACOES" or OrdemServico["CARGO_DESLOCAMENTO"] == "COORDENADOR" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "PRESIDENTE" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "DIRETOR" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "GERENTE EXECUTIVO" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "GERENTE DE DIVISAO" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "CONSELHEIRO FISCAL" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "SUPERINTENDENTE" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "GERENTE REGIONAL DE OPERACOES" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "COORDENADOR"
```
- alternativa → [G82656] Haverá aquisição de passagens e/ou hospedagens e/o: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G82665] Adiantamento superior a R$5000,00?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82662] Reserva realizada? (EventBasedExclusiveDecision)
Codigo=RESERVANAOREALIZADA
- alternativa → [369127] Incluir informações da Reserva: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0; RotuloMotivo=Sim
- alternativa → [369126] Reserva não realizada: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; RotuloMotivo=Não; MotivoObrigatorio=true
### [G82663] Diretor aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVARDIREX")
```
- alternativa → [369137] : OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [369125] Realizar reserva no sistema


: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G82664] Gereg/Gediv/Super aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR>1000")
```
- alternativa → [369129] : OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G82656] Haverá aquisição de passagens e/ou hospedagens e/o: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G82665] Adiantamento superior a R$5000,00? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("VALOR_TOTAL_ADIANTAMENTO")
```
- alternativa → [G82656] Haverá aquisição de passagens e/ou hospedagens e/o: OperadorDecision=LessThan; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
5000
```
- alternativa → [369134] Aprovar valor de atencipação de deslocamento maior: OperadorDecision=GreaterThanEqual; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
5000
```
### [G82666] Haverá Adiantamento de valores? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("VALOR_TOTAL_ADIANTAMENTO")
```
- alternativa → [G82657] Viagem internacional?: OperadorDecision=GreaterThanEqual; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
1
```
- alternativa → [369135] Realizar Prestação de Contas: OperadorDecision=LessThan; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
1
```
### [G82667] Haverá aquisição de passagens? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["PAHL_PASSAGENS"] == True
```
- alternativa → [G82658] Assistência Técnica: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [369125] Realizar reserva no sistema


: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82668] Presidente, Diretor, Conselheiro, Gerex, Gereg ? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["CARGO_DESLOCAMENTO"] == "PRESIDENTE" or OrdemServico["CARGO_DESLOCAMENTO"] == "DIRETOR" or OrdemServico["CARGO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["CARGO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["CARGO_DESLOCAMENTO"] == "CONSELHEIRO FISCAL" or OrdemServico["CARGO_DESLOCAMENTO"] == "COORDENADOR" or OrdemServico["CARGO_DESLOCAMENTO"] == "COMITE DE AUDITORIA" or OrdemServico["CARGO_DESLOCAMENTO"] == "ASSESSOR EXECUTIVO PRESIDENCIA" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "PRESIDENTE" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "DIRETOR" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "MEMBRO COMITE DE AUDITORIA" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "CONSELHEIRO FISCAL" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "COORDENADOR" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "COMITE DE AUDITORIA" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "ASSESSOR EXECUTIVO PRESIDENCIA" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "GERENTE REGIONAL DE OPERACOES" or OrdemServico["FUNCAO_DESLOCAMENTO"] == "CONSELHEIRO DE ADMINISTRACAO"
```
- alternativa → [369125] Realizar reserva no sistema


: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [369131] Aprovar Deslocamento - Diretor do Favorecido: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [369136] LinkInicial "chatbot"
Responsável: Fila CSC - Passagens Aéreas e Hospedagem (papel 508)
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do Deslocamento
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] obrigatório — Coluna=3
  - TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM] obrigatório
  - QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA] obrigatório
  - QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL] obrigatório
  - MATRICULA "Matrícula do favorecido" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] obrigatório
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] obrigatório
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO] obrigatório
  - OBS43 "Quem fará o deslocamento" [Memo String(900) → CPE_CSC.OBS43] obrigatório
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM] obrigatório
  - OBS41 "Cidade e Estado de ORIGEM" [Memo String(900) → CPE_CSC.OBS41] obrigatório
  - CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] obrigatório
  - OBS42 "Cidade e Estado de DESTINO" [Memo String(900) → CPE_CSC.OBS42] obrigatório
  - OBS44 "A Base TR" [Memo String(900) → CPE_CSC.OBS44]
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM]
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA] obrigatório
- Associação de subprocesso: AssociacaoId=1617; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Chatbot > Deslocamento a Serviço

### [369137] FimCancelamento ""

### [369138] EventoIntermediarioRegra ""
Config: MaximoExecucao=1
**Regra**
```python
DateTime.Now.Date.AddDays(5) >= OrdemServico["SAIDA"]
#DateTime.Now.Date <= OrdemServico["SAIDA"].Date.AddDays(-6)
#DateTime.Now() > OrdemServico.DataHoraSolicitacao.AddDays(27)
```

### [369125] Tarefa "Realizar reserva no sistema


"
Responsável: Fila CSC - Passagens Aéreas e Hospedagem (papel 508)
**ScriptValidacao**
```python
if OrdemServico["FUNCAO_DESLOCAMENTO"] == "GERENTE EXECUTIVO" and OrdemServico["CHECKBOX1"] == False:
    Criticas.AdicionaPendencia("Você precisa confimrar a Reserva/Hospedagem para Executivos")
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CHECKBOX1"].Visivel = False
Formulario["LABEL3"].Visivel = False

if OrdemServico["FUNCAO_DESLOCAMENTO"] == "GERENTE EXECUTIVO":
    Formulario["CHECKBOX1"].Visivel = True
    Formulario["LABEL3"].Visivel = True
    
camposVisiveis = None
camposHabilitados = None
vis = False
hab = False

pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
   # lista de campos a serem alteradas a visibilidade.
   camposVisiveis = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL","CSC_OBS"]
   camposHabilitados = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL","CSC_OBS"]
   if OrdemServico["PAHL_HOSPEDAGENS"] == True:
      vis = True
      hab = False
   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado
       valor = Formulario[controle.Key].Valor
       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = vis
              valor = None
              break
       Formulario[controle.Key].Visivel = visivel

       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = hab
              break
       Formulario[controle.Key].Habilitado = habilitado
       
Formulario["CHECKBOX1"].Habilitado = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Solicitação de Reservas
  - PAH_DATA_ENTRADA "Data de Entrada no Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA]
  - PAH_DATA_SAIDA "Data de Saída do Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA]
**PAH_DATA_SAIDA.ScriptModificado**
```python
if Formulario["PAH_DATA_SAIDA"].Valor <= Formulario["PAH_DATA_ENTRADA"].Valor:
   Formulario.ExibeMensagem("'Data de Saída do Hotel' deve ser maior que 'Data de Entrada no Hotel'!")
   Formulario["PAH_DATA_SAIDA"].Valor = None
```
  - PAH_EVENTO_HOTEL "Evento no Hotel?" [DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL]
**PAH_EVENTO_HOTEL.ScriptModificado**
```python
Formulario["PAH_HOTEL_EVENTO"].Visivel = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
Formulario["PAH_HOTEL_EVENTO"].Habilitado = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
```
  - RESERVA_DE_VOO_INTERNACIONAL "Informações para Reserva de Voo - Internacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL]
    - coluna SEQUENCIA obrigatório
    - coluna TRECHO obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna AEROPORTO_ORIGEM obrigatório
    - coluna CIDADE_DESTINO obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna DATA_VOO obrigatório
    - coluna HORA_ESTIMADA_VOO obrigatório
    - coluna DESPACHO_BAGAGENS obrigatório
    - coluna QUANTIDADE_BAGAGENS obrigatório
  - CSC_OBS "Endereço do Local do Evento/Atendimento e outras observações (Informe até 2 sugestões de hotel, se houver)" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - DATA_INICIO_AUX1 "Data Início da Viagem" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1]
  - PAH_HOTEL_EVENTO "Hotel do Evento" [TextBox String → CPE_CSC.PAH_HOTEL_EVENTO]
  - PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO]
  - PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO]
**PAHL_LOCACOES_CARRO.ScriptConfirmado**
```python
if Registro["DATA_HORA_DEVOLUCAO"] < Registro["DATA_HORA_RETIRADA"]:
   Formulario.ExibeMensagem("ATENÇÃO: Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
```
    - coluna CELULAR_FAVORECIDO obrigatório
    - coluna CARRO4X4 obrigatório
    - coluna DATA_HORA_RETIRADA obrigatório
    - coluna LOCAL_DEVOLUCAO obrigatório
    - coluna DATA_HORA_DEVOLUCAO obrigatório
**PAHL_LOCACOES_CARRO.DATA_HORA_DEVOLUCAO.ScriptModificado**
```python
#if FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor < FormularioRegistro["DATA_HORA_RETIRADA"].Valor:
#   Formulario.ExibeMensagem("Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
#   FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor = None
```
    - coluna CPF_FAVORECIDO obrigatório
    - coluna LOCAL_RETIRADA obrigatório
    - coluna VALOR_LOCACAO
  - PAH_MOTIVO_SOL "Motivo da Solicitação" [DropDownList String → CPE_CSC.PAH_MOTIVO_SOL]
  - PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES]
    - coluna VALOR_TRECHO
    - coluna CIA_AEREA obrigatório
    - coluna LOCALIZADOR obrigatório
    - coluna SEQUENCIA obrigatório
  - PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM]
  - RESERVA_DE_VOO "Informações da Reserva de Voo - Nacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO]
    - coluna DATA_VOO obrigatório
    - coluna ALT_OU_EXC
    - coluna HORA_ESTIMADA_VOO obrigatório
    - coluna QUANTIDADE_BAGAGENS obrigatório
    - coluna SEQUENCIA obrigatório
**RESERVA_DE_VOO.SEQUENCIA.ScriptModificado**
```python
rv = OrdemServico["RESERVA_DE_VOO"]

for seq in rv.Rows:
    if FormularioRegistro["SEQUENCIA"].Valor == seq["SEQUENCIA"]:
       Formulario.ExibeMensagem("A T E N Ç Ã O !!! \n Nº do Trecho já lançado!")
       FormularioRegistro["SEQUENCIA"].Valor = None
```
    - coluna ALT_EXC obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna UF_ORIGEM obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna TRECHO obrigatório
    - coluna DESPACHO_BAGAGENS obrigatório
**RESERVA_DE_VOO.DESPACHO_BAGAGENS.ScriptModificado**
```python
#Sim;Não
FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = None
FormularioRegistro["QUANTIDADE_BAGAGENS"].Habilitado = FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Sim"

if FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Não":
   FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = 0
```
    - coluna AEROPORTO_ORIGEM obrigatório
    - coluna UF_DESTINO obrigatório
    - coluna CIDADE_DESTINO obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do Deslocamento
  - VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR]
**VALOR_DIARIA_DOLAR.ScriptModificado**
```python
if Convert.ToDecimal(Formulario["VALOR_DIARIA_DOLAR"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DOLAR"].Valor):
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["CAMPO_VALIDACAO_DOLAR"].Valor
else:
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["VALOR_DIARIA_DOLAR"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True

valorTotal1 = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor)

valorTotal1 = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal1 


#OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal1
```
  - CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR] — Coluna=2
  - DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL] — Coluna=3
  - VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA]
  - TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR]
  - LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE]
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM]
  - CHECKBOX1 "Confirmo que foi realizado a compra de aéreo com tarifa alternável/reembolsavel, pois favorecido possui função de Gerente Executivo." [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1] obrigatório
  - NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO]
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] — Coluna=2
  - CIDADE_DESTINO_INTERNACIONAL "Cidade/País de Destino" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL] — Coluna=2
  - DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM]
**TIPO_HOSPEDAGEM.ScriptModificado**
```python
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
    Formulario["QUANTIDADE_DIARIA"].Visivel = False
    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0" 
    
if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    
#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = True
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA"].Visivel = True
#    Formulario["VALOR_DIARIA"].Habilitado = True
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False    
    

#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = False
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
```
  - QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA]
**QUANTIDADE_DIARIA.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import OutputSubProcesso
def calculaDiaria():
    ############### SE O FAVORECIDO FOR DO GRUPO C MAS ESTARÁ ACOMPANHANDO O GRUPO B RECEBE O VALOR DO GRUPO B 
    
    if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    elif Formulario["SIM_NAO"].Valor == "Sim" :
          if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 
                 Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                
          elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO E BRASILIA
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
            
          elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
              Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
      
    else:     
            
        ############## SE FOR DO GRUPO A -  PRESIDENTE / DIRETOR / CONSELHEIRO NÃO TEM LIMITE   
        if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
            
            
            
        ############## SE O FAVORECIDO FOR DO GRUPO B  ELE RECEBE REFERENTE A CIDADE     
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "SUPERINTENDENTE":
            if Formulario["CIDADE_DESTINO"].Valor == "3550308 ": # SAO PAULO 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO OutputSubProcesso BRASILIA
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                      Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
            else:
                Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                  
                  
        ############## DEMAIS CARGOS
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor != "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE":
              
              if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 3550308 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550" 
                    
              elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO ou BRASILIA
                        Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                        
              elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                          Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "370" 
                          
              else:
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "350"
                  

              
              
calculaDiaria()
     
############ VALOR FINAL DO ADIANTAMENTO EM DIARIAS      
diasViagem = Convert.ToInt32(Formulario["DIAS_DE_TRA"].Valor)
diasHospedagem = Convert.ToInt32(Formulario["QUANTIDADE_DIARIA"].Valor)



if diasHospedagem > diasViagem:
    mensagem = "Quantidade de Diária Excedida! Máximo Permitido: " + Formulario["DIAS_DE_TRA"].Valor + " Verifique a saída e o retorno"
    Formulario.ExibeMensagem(mensagem)      
    Formulario["VALOR_DIARIA"].Habilitado = True

#Valor parcela complementar    
if Formulario["QUANTIDADE_DIARIA"] != "0":
    Formulario["PARCELA_COMPLEMENTAR"].Valor = "17,90"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    
    pc = Formulario["PARCELA_COMPLEMENTAR"].Valor
    qtd = Formulario["QUANTIDADE_DIARIA"].Valor
    total = 0

    total = pc * qtd

    Formulario["TOTAL_COMPLEMENTAR"].Valor = total
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = True
    
#if (Formulario["TIPO_DESTINO"].Valor == "Interior") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "350"
#    
#if (Formulario["TIPO_DESTINO"].Valor == "Capital") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "500"
#
#import System.Text
#daysOffText = System.Text.StringBuilder()
#
# #RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#   
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            return True
#    return False
#   
#def workingDays(totalDays, firstDate):
#    
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#saida = Formulario["SAIDA"].Valor
#retorno  = Formulario["RETORNO_DIA"].Valor
#
#totalDias = (retorno - saida).TotalDays  
#count = 0
#
#totalDiasUteis = workingDays(totalDias,saida) 
#totalDiasNaoUteis = totalDias - totalDiasUteis
#
############### almoço e janta de ambos os dias
#quantReduzida = totalDiasUteis  
#quantIntegral = (totalDiasNaoUteis * 2) + totalDiasUteis
#
#
#

#Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalDiasUteis 
#Formulario["QTD_REFEICAO_INTEGRAL"].Valor = totalDiasNaoUteis
#
#
#Formulario["VALOR_REF_REDUZIDA"].Valor = totalDiasUteis * 18.39
#Formulario["VALOR_REF_INTEGRAL"].Valor = totalDiasNaoUteis *  64.36
#
#
#OrdemServico.AdicionaComentario("WorkingDays "+totalWorkingDays.ToString(),False)
#OrdemServico.AdicionaComentario(daysOffText.ToString(),False )

#OrdemServico["totalWorkingDays"] = totalWorkingDays
```
  - QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA]
**QTD_REFEICAO_REDUZIDA.ScriptModificado**
```python
import clr 
import datetime
import System.Text

daysOffText = System.Text.StringBuilder()

quantRefeicaoReduzida = Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor)
quantRefeicaoIntegral = Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor)

valorRefIntegral = 64.36
valorRefReduzida = 18.39
Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False

def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
   
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            return True
    return False


    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff


    
firstDate = Formulario["SAIDA"].Valor
lastDate   = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0


saidaHora = Formulario["SAIDA_HORA"].Valor
retornoHora = Formulario["RETORNO_HORA"].Valor

hora = saidaHora.Split(':');
horaRetorno = retornoHora.Split(':');

horarioSaida = saidaHora[0]
minutoSaida = saidaHora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]




totalWorkingDays = workingDays(totalDays,firstDate)

#SAIDA E RETORNO DIAS ÚTEIS

#SAIDA DIAS ÚTEIS
if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) >=13 and Convert.ToInt32(horarioSaida) < 21:
    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
    totalWorkingDays = totalWorkingDays - 1
   
if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
    totalWorkingDays = totalWorkingDays - 1
   
    
#RETORNO DIAS ÚTEIS   
if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    totalWorkingDays = totalWorkingDays - 1
    
if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) > 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
     
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS    
if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    
if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1

    
    
#RETORNO FINAIS DE SEMANA E/OU FERIADOS    
if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 2

if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) != 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1 


totalWorkingDays = totalWorkingDays - 2    
    
if quantRefeicaoReduzida > (totalWorkingDays - 1):
    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
    Formulario.ExibeMensagem(mensagem)    
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
        
else:
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
    refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
    valorTotalRefeicoes = refIntegral + refReduzida
    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    
    


#Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalWorkingDays
#Formulario["QTD_REFEICAO_INTEGRAL"].Valor = saturdays + totalWorkingDays
```
  - MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO]
**MEIO_LOCOMOCAO.ScriptModificado**
```python
if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = True
    Formulario["VALOR_DISTANCIA"].Visivel = True
    Formulario["VALOR_DISTANCIA"].Habilitado = True
else:
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False
    Formulario["VALOR_DISTANCIA"].Visivel = False
    Formulario["VALOR_DISTANCIA"].Habilitado = False
    
    
    
##if Formulario["MEIO_LOCOMOCAO"].Valor == "Avião" or Formulario["MEIO_LOCOMOCAO"] == "Ônibus Interestadual":
##    Formulario["VALOR_PASSAGEM"].Visivel = True
##    Formulario["VALOR_PASSAGEM"].Habilitado = True
##    Formulario["VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = True
##else:
##    Formulario["VALOR_PASSAGEM"].Visivel = False
##    Formulario["VALOR_PASSAGEM"].Habilitado = False
##    Formulario["VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False    
#    
    






##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral
############# calculo dias
import clr 
import datetime
import System.Text
 

##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral

valorRefIntegral = 64.36
valorRefReduzida = 18.39



daysOffText = System.Text.StringBuilder()


##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False


def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate

    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)

    return totalHolidays

    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
   


    
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
    
    return saturdays

    
firstDate = Formulario["SAIDA"].Valor
lastDate   = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0





totalWorkingDays = workingDays(totalDays,firstDate)
holidaysCount = countHolidays(firstDate, lastDate)
saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2

quantRed = totalWorkingDays
quantInt = saturdays + totalWorkingDays 








saidaHora = Formulario["SAIDA_HORA"].Valor
retornoHora = Formulario["RETORNO_HORA"].Valor

hora = saidaHora.Split(':');
horaRetorno = retornoHora.Split(':');

horarioSaida = hora[0]
minutoSaida = hora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]



#SAIDA DIAS ÚTEIS


#1 maior q o 2
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
#    quantRed = quantRed - 1
#   
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
#    quantInt = quantInt - 1
#   
#RETORNO DIAS ÚTEIS
#1 menor q o 2   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRed = quantRed - 1
#    quantInt = quantInt - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantInt = quantInt - 1
#    #teste abaixo
#    quantRed = quantRed - 1





if workingDays(0,firstDate):
    if (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioSaida) > 21):
        quantInt = quantInt - 1
        quantRed = quantRed - 1
    
    if (Convert.ToInt32(horarioRetorno) <= 13):
        quantRed = quantRed - 1
        quantInt = quantInt - 1
    if (Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13):
        quantInt = quantInt - 1
    
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS

if not  workingDays(0,firstDate):
    if Convert.ToInt32(horarioSaida) > 13:
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioSaida) > 21:
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioRetorno) < 13:
        quantInt = quantInt - 2
    if Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) != 13:
        quantInt = quantInt - 1   


##Correção margem de erro do cálculo de refeições:
quantRed = quantRed - 1
quantInt = quantInt + 1
        
        
Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
  
##totalIntegrais = integrais + totalWorkingDays

##Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalWorkingDays
##Formulario["QTD_REFEICAO_INTEGRAL"].Valor = saturdays + totalWorkingDays



############## calculo valor total
 
refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
valorTotalRefeicoes = refIntegral + refReduzida
Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
```
  - TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO]
**TIPO_DESLOCAMENTO.ScriptModificado**
```python
##Viagem internacional

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    

    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False

    
    
    

    
    
else:


    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["COTACAO_DOLAR"].Visivel = False
    Formulario["COTACAO_DOLAR"].Habilitado = False   
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
    Formulario["PAIS"].Visivel = False
    Formulario["PAIS"].Habilitado = False  

    
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["DIARIA_COTACAO_REAL"].Visivel = False
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
```
  - VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA] — Coluna=2
  - VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA]
**VALOR_DIARIA.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
         Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor
    



if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE": 
     Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor


     
     
if Convert.ToDecimal(Formulario["VALOR_DIARIA"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DIARIA"].Valor):
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["CAMPO_VALIDACAO_DIARIA"].Valor
else:
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True

valorTotal = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["VALOR_DIARIA_AUTORIZADO"].Valor)

valorTotal = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal 


OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal
```
  - VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO] — Coluna=2
  - PREVISAO_DISTANCIA_KM "Previsão de distancia em KM" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM]
**PREVISAO_DISTANCIA_KM.ScriptModificado**
```python
import System


Formulario["VALOR_DISTANCIA"].Habilitado = False

valorTotal = 0

distancia = Formulario["PREVISAO_DISTANCIA_KM"].Valor
valorTotal = distancia * 1.30 


Formulario["VALOR_DISTANCIA"].Valor = valorTotal
#OrdemServico["VALOR_DISTANCIA"] = valorTotal
#
```
  - VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO] — Coluna=2
  - VALOR_REF_REDUZIDA "Valor Refeição Reduzida" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA]
  - QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL]
**QTD_REFEICAO_INTEGRAL.ScriptModificado**
```python
import System
import clr 
import datetime
import System.Text
  

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False

#valorTotal = 0
valorRefIntegral = 64.36
valorRefReduzida = 18.39



#valorTotal = quantRefeicaoIntegral + quantRefeicaoReduzida

#Formulario["VALOR_TOTAL_REFEICAO"].Valor = valorTotal 
#OrdemServico["VALOR_TOTAL_REFEICAO"] = valorTotal




quantRefeicaoReduzida = Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor)
quantRefeicaoIntegral = Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor)


daysOffText = System.Text.StringBuilder()


#RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False


def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate

    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)

    return totalHolidays

    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
   


    
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
    
    return saturdays

    
firstDate = Formulario["SAIDA"].Valor
lastDate   = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0



totalWorkingDays = workingDays(totalDays,firstDate)
totalREF = workingDays(totalDays,firstDate)
holidaysCount = countHolidays(firstDate, lastDate)
saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2

refIntPermitidas = totalWorkingDays + saturdays



saidaHora = Formulario["SAIDA_HORA"].Valor
retornoHora = Formulario["RETORNO_HORA"].Valor

hora = saidaHora.Split(':');
horaRetorno = retornoHora.Split(':');

horarioSaida = saidaHora[0]
minutoSaida = saidaHora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]



refeicoesFeriados = totalWorkingDays + saturdays



#SAIDA DIAS ÚTEIS
if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21:
    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
    totalREF = totalREF - 1
   
if workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    refeicoesFeriados = refeicoesFeriados - 1
    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
    totalREF = totalREF - 1
   
#RETORNO DIAS ÚTEIS   
if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
    quantRefeicaoReduzida = quantRefeicaoReduzida - 1
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    totalREF = totalREF - 1
    refeicoesFeriados = refeicoesFeriados - 1
    
if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    refeicoesFeriados = refeicoesFeriados - 1
     
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS    
if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    refeicoesFeriados = refeicoesFeriados - 1
    
if not  workingDays(0,firstDate) and Convert.ToInt32(horarioSaida) > 21:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    refeicoesFeriados = refeicoesFeriados - 1

    
    
#RETORNO FINAIS DE SEMANA E/OU FERIADOS    
if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 2
    refeicoesFeriados = refeicoesFeriados - 2

if not  workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) < 19 and Convert.ToInt32(horarioRetorno) != 13:
    quantRefeicaoIntegral = quantRefeicaoIntegral - 1
    refeicoesFeriados = refeicoesFeriados - 1
    
          

refeicoesFeriados = refeicoesFeriados + 1


calcula = refeicoesFeriados - 1
    

    
if quantRefeicaoIntegral >= (calcula - 1):
    mensagem = ("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + str(calcula) + " Verifique a Saída e o Retorno.")
    Formulario.ExibeMensagem(mensagem)
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False 

else:
    refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
    refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
    valorTotalRefeicoes = refIntegral + refReduzida
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes        

    
#adjusted by: Fernando Cajango Dias
```
  - VALOR_REF_INTEGRAL "Valor Refeição Integral" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL] — Coluna=2
  - PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR]
  - LABEL3 "<b style="color: red">Confirme a compra de aéreo com tarifa alternável/reembolsavel para Executivos</b>" [Label String(1024) → CP_ORDEM_SERVICO.LABEL3] obrigatório
  - VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS] — Coluna=2
**VALOR_DESPESAS.ScriptModificado**
```python
import System
Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    
    valorTotalAdiantamento = 0


    totalDiaria = 0
    ##valorAvicao = 0
    outrasDespesas = 0
    ##valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
    valorTotalAdiantamento = totalDiaria + outrasDespesas + complementar
    
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento

elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento    
else:
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0
    
    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    
    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

    #OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento
```
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR]
**COTACAO_DOLAR.ScriptModificado**
```python
#import System
#
#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)
#
#
#Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor) = valorTotal


valorTotal = 0
vtd = Formulario["VALOR_TOTAL_DIARIA"].Valor
cd = Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)

valorTotal = vtd * cd

Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal




#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * (Formulario["COTACAO_DOLAR"].Valor)
#
#
#Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal
#

#diariaReal = ""
#cotacao = ""
#valorTotal = ""
#
#diariaReal = Convert.ToDouble(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#cotacao = Convert.ToDouble(Formulario["COTACAO_DOLAR"].Valor)
```
  - DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha) " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS]
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True



Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False



Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None



cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()

    
        


if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
```
  - FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A]
**ACOMPANHANDO_GRUPO_A.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
    Formulario["SIM_NAO"].Visivel = False
    Formulario["SIM_NAO"].Habilitado = False 
  

else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False 
    Formulario["SIM_NAO"].Visivel = True
    Formulario["SIM_NAO"].Habilitado = True
     
    
    
#    
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Não":
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
#    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#
#else:
#     Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
```
  - SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
```
  - PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS] — Coluna=3
**PAIS.ScriptModificado**
```python
  
        ################## grupo A
if Formulario["PAIS"].Valor == "AFEGANISTÃO" or Formulario["PAIS"].Valor == "ARMÊNIA" or Formulario["PAIS"].Valor == "BANGLADESH" or Formulario["PAIS"].Valor == "BELARUS" or Formulario["PAIS"].Valor == "BENIN" or Formulario["PAIS"].Valor == "BOLÍVIA" or Formulario["PAIS"].Valor == "BURKINAFASSO" or Formulario["PAIS"].Valor == "BUTÃO"  or Formulario["PAIS"].Valor == "CHILE" or Formulario["PAIS"].Valor == "COMORES" or Formulario["PAIS"].Valor == "REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA" or Formulario["PAIS"].Valor == "COSTA RICA" or Formulario["PAIS"].Valor == "EL SALVADOR" or Formulario["PAIS"].Valor == "EQUADOR" or Formulario["PAIS"].Valor == "ESLOVÊNIA" or Formulario["PAIS"].Valor == "FILIPINAS" or Formulario["PAIS"].Valor == "GÂMBIA" or Formulario["PAIS"].Valor == "GUIANA" or Formulario["PAIS"].Valor == "GUINÉ BISSAU" or Formulario["PAIS"].Valor == "GUINÉ" or Formulario["PAIS"].Valor == "HONDURAS" or Formulario["PAIS"].Valor == "INDONÉSIA" or Formulario["PAIS"].Valor == "IRÃ" or Formulario["PAIS"].Valor == "IRAQUE" or Formulario["PAIS"].Valor == "LAOS" or Formulario["PAIS"].Valor == "LÍBANO" or Formulario["PAIS"].Valor == "MALÁSIA" or Formulario["PAIS"].Valor == "MALDIVAS" or Formulario["PAIS"].Valor == "MARROCOS" or Formulario["PAIS"].Valor == "MONGÓLIA" or Formulario["PAIS"].Valor == "NAMÍBIA" or Formulario["PAIS"].Valor == "MYANMAR" or Formulario["PAIS"].Valor == "NAURU" or Formulario["PAIS"].Valor == "NEPAL"or Formulario["PAIS"].Valor == "NICARÁGUA" or Formulario["PAIS"].Valor == "PANAMÁ" or Formulario["PAIS"].Valor == "PARAGUAI" or Formulario["PAIS"].Valor == " REP. CENTRO AFRICANA" or Formulario["PAIS"].Valor == "REPÚBLICA TOGOLESA" or Formulario["PAIS"].Valor == "SALOMÃO" or Formulario["PAIS"].Valor == "SAMOA" or Formulario["PAIS"].Valor == "SERRA LEOA" or Formulario["PAIS"].Valor == "SÍRIA" or Formulario["PAIS"].Valor == "SOMÁLIA" or Formulario["PAIS"].Valor == "SRI LANKA" or Formulario["PAIS"].Valor == "TURQUIA" or Formulario["PAIS"].Valor == "TADJIQUISTÃO" or Formulario["PAIS"].Valor == "TAILÂNDIA" or Formulario["PAIS"].Valor == "TIMOR LESTE" or Formulario["PAIS"].Valor == "TONGA" or Formulario["PAIS"].Valor == "TUNÍSIA" or Formulario["PAIS"].Valor == "TURCOMENISTÃO" or Formulario["PAIS"].Valor == "TUVALU" or Formulario["PAIS"].Valor == "VIETNÃ" or Formulario["PAIS"].Valor == "ZIMBÁBUE":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "220"
                        
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "200"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "190"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "180"
          
    else:
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "170"
            
        ###################### grupo B    
            
elif Formulario["PAIS"].Valor == "ÁFRICA DO SUL" or Formulario["PAIS"].Valor == "ALBÂNIA" or Formulario["PAIS"].Valor == "ANDORA" or Formulario["PAIS"].Valor == "ARGÉLIA" or Formulario["PAIS"].Valor == "ARGENTINA" or Formulario["PAIS"].Valor == "AUSTRÁLIA" or Formulario["PAIS"].Valor == "BELIZE" or Formulario["PAIS"].Valor == "BÓSNIA-HERZEGÓVINA"  or Formulario["PAIS"].Valor == "BURUNDI" or Formulario["PAIS"].Valor == " CABO VERDE" or Formulario["PAIS"].Valor == "CAMARÕES" or Formulario["PAIS"].Valor == "CAMBOJA" or Formulario["PAIS"].Valor == "CATAR" or Formulario["PAIS"].Valor == "CHADE" or Formulario["PAIS"].Valor == "CHINA" or Formulario["PAIS"].Valor == "CHIPRE" or Formulario["PAIS"].Valor == "COLÔMBIA" or Formulario["PAIS"].Valor == "DOMINICA" or Formulario["PAIS"].Valor == "EGITO" or Formulario["PAIS"].Valor == "ERITRÉIA" or Formulario["PAIS"].Valor == "ESTÔNIA" or Formulario["PAIS"].Valor == "ETIÓPIA" or Formulario["PAIS"].Valor == "GANA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "HUNGRIA" or Formulario["PAIS"].Valor == "IEMEN" or Formulario["PAIS"].Valor == " ILHAS MARSHALL" or Formulario["PAIS"].Valor == "ÍNDIA" or Formulario["PAIS"].Valor == "KIRIBATI" or Formulario["PAIS"].Valor == "LESOTO" or Formulario["PAIS"].Valor == "LÍBIA" or Formulario["PAIS"].Valor == "MACEDÔNIA"or Formulario["PAIS"].Valor == "MADAGASCAR" or Formulario["PAIS"].Valor == "MALAUÍ" or Formulario["PAIS"].Valor == "MICRONÉSIA" or Formulario["PAIS"].Valor == "MOÇAMBIQUE" or Formulario["PAIS"].Valor == "MOLDÁVIA" or Formulario["PAIS"].Valor == "NÍGER" or Formulario["PAIS"].Valor == "NIGÉRIA" or Formulario["PAIS"].Valor == "NOVA ZELÂNDIA" or Formulario["PAIS"].Valor == "PALAU" or Formulario["PAIS"].Valor == "PAPUA NOVA GUINÉ" or Formulario["PAIS"].Valor == "PAQUISTÃO" or Formulario["PAIS"].Valor == "PERU" or Formulario["PAIS"].Valor == "POLÔNIA" or Formulario["PAIS"].Valor == "QUÊNIA" or Formulario["PAIS"].Valor == "REPÚBLICA DOMINICANA" or Formulario["PAIS"].Valor == "ROMÊNIA" or Formulario["PAIS"].Valor == "RUANDA" or Formulario["PAIS"].Valor == " SÃO TOMÉ E PRÍNCIPE" or Formulario["PAIS"].Valor == "SENEGAL" or Formulario["PAIS"].Valor == "TANZÂNIA" or Formulario["PAIS"].Valor == "SUDÃO"  or Formulario["PAIS"].Valor == "URUGUAI" or Formulario["PAIS"].Valor == "UZBEQUISTÃO" or Formulario["PAIS"].Valor == "VENEZUELA":

    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "280"

    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "270"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "260"
        
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "250"
                    
                    

            ################### grupo C

            
elif Formulario["PAIS"].Valor == "ANTÍGUA E BARBUDA" or Formulario["PAIS"].Valor == "ARÁBIA SAUDITA" or Formulario["PAIS"].Valor == "AZERBAIDJÃO" or Formulario["PAIS"].Valor == "BAHAMAS" or Formulario["PAIS"].Valor == "BAREINE" or Formulario["PAIS"].Valor == "BOTSUANA" or Formulario["PAIS"].Valor == "BRUNEI DARUSSALAM" or Formulario["PAIS"].Valor == "BULGÁRIA"  or Formulario["PAIS"].Valor == "CANADÁ" or Formulario["PAIS"].Valor == "CINGAPURA" or Formulario["PAIS"].Valor == "CONGO" or Formulario["PAIS"].Valor == "COSTA DO MARFIM" or Formulario["PAIS"].Valor == "CUBA" or Formulario["PAIS"].Valor == "DJIBUTI" or Formulario["PAIS"].Valor == "EMIRADOS ÁRABES" or Formulario["PAIS"].Valor == "FIJI" or Formulario["PAIS"].Valor == "GABÃO" or Formulario["PAIS"].Valor == "GUATEMALA" or Formulario["PAIS"].Valor == "REPÚBLICA DEMOCRÁTICA DO CONGO" or Formulario["PAIS"].Valor == "JAMAICA" or Formulario["PAIS"].Valor == "JORDÂNIA" or Formulario["PAIS"].Valor == "LETÔNIA" or Formulario["PAIS"].Valor == "LIBÉRIA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "MAURÍCIO" or Formulario["PAIS"].Valor == "MAURITÂNIA" or Formulario["PAIS"].Valor == "MÉXICO" or Formulario["PAIS"].Valor == "MALTA" or Formulario["PAIS"].Valor == " REPÚBLICA TCHECA" or Formulario["PAIS"].Valor == "RÚSSIA" or Formulario["PAIS"].Valor == "SAN MARINO" or Formulario["PAIS"].Valor == "SANTA LÚCIA"or Formulario["PAIS"].Valor == "SÃO CRISTOVÃO E NÉVIS" or Formulario["PAIS"].Valor == "SÃO VICENTE E GRANADINAS" or Formulario["PAIS"].Valor == "TAIWAN" or Formulario["PAIS"].Valor == "TRINIDAD E TOBAGO" or Formulario["PAIS"].Valor == "UCRÂNIA" or Formulario["PAIS"].Valor == "UGANDA" or Formulario["PAIS"].Valor == "ZÂMBIA":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "330"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "320"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "310"
    
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"     
                    
                
            #################### grupo D 
if Formulario["PAIS"].Valor == "ALEMANHA" or Formulario["PAIS"].Valor == "ANGOLA" or Formulario["PAIS"].Valor == "ÁUSTRIA" or Formulario["PAIS"].Valor == "BARBADOS" or Formulario["PAIS"].Valor == "BÉLGICA"or Formulario["PAIS"].Valor == "CAZAQUISTÃO" or Formulario["PAIS"].Valor == "CORÉIA DO SUL" or Formulario["PAIS"].Valor == "CROÁCIA"  or Formulario["PAIS"].Valor == "DINAMARCA" or Formulario["PAIS"].Valor == "ESPANHA" or Formulario["PAIS"].Valor == "ESTADOS UNIDOS DA AMÉRICA" or Formulario["PAIS"].Valor == "FINLÂNDIA" or Formulario["PAIS"].Valor == "FRANÇA" or Formulario["PAIS"].Valor == "GRANADA" or Formulario["PAIS"].Valor == "GRÉCIA HONG KONG" or Formulario["PAIS"].Valor == "IRLANDA" or Formulario["PAIS"].Valor == "ISLÂNDIA" or Formulario["PAIS"].Valor == "ISRAEL" or Formulario["PAIS"].Valor == "ITÁLIA" or Formulario["PAIS"].Valor == "JAPÃO" or Formulario["PAIS"].Valor == "KUAITE" or Formulario["PAIS"].Valor == "LIECHTENSTEIN" or Formulario["PAIS"].Valor == "LUXEMBURGO" or Formulario["PAIS"].Valor == "MÔNACO" or Formulario["PAIS"].Valor == "MONTENEGRO" or Formulario["PAIS"].Valor == "NORUEGA" or Formulario["PAIS"].Valor == "OMÃ" or Formulario["PAIS"].Valor == "PEÍSES BAIXOS" or Formulario["PAIS"].Valor == "PORTUGAL" or Formulario["PAIS"].Valor == "REINO UNIDO" or Formulario["PAIS"].Valor == "REPÚBLICA QUIRGUIZ" or Formulario["PAIS"].Valor == "SEICHELES" or Formulario["PAIS"].Valor == "SÉRVIA SUAZILÂNDIA" or Formulario["PAIS"].Valor == "SUÉCIA" or Formulario["PAIS"].Valor == "SUÍÇA" or Formulario["PAIS"].Valor == "VANUATU":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "460"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "420"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "390"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "370"
                  
                  
    else:
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
```
  - TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO] — Coluna=4
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] — Coluna=3; Configuracao={"Mascara":"00:00"}
**RETORNO_HORA.ScriptModificado**
```python
import clr 
import datetime

data1 = ""
data2 = ""

data1 = Formulario["SAIDA"].Valor
data2 = Formulario["RETORNO_DIA"].Valor
 
delta = data2 - data1
diferenca = delta.Days

Formulario["DIAS_DE_TRA"].Valor = diferenca
Formulario["DIAS_DE_TRA"].Habilitado = False
```
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA]
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] — Coluna=3
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] — Configuracao={"Mascara":"00:00"}
  - CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA]

### [369128] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Pesquisa
idCliente = OrdemServico.ClienteId

listaPesq = DB.ExecuteDataTable("SELECT ID_PESQUISA FROM PESQUISA WHERE OS = '" + OrdemServico.Id.ToString() +"'")

for pesq in listaPesq.Rows:
    pesquisa = Pesquisa.Carrega(pesq["ID_PESQUISA"])

    # modifica a propriedade Avaliador
    pesquisa.Avaliador = Pessoa.Carrega(idCliente);

    # salva modificação da propriedade Avaliador
    Pesquisa.Salva(pesquisa)
```

### [369129] FimCancelamento ""

### [369130] Tarefa "Preencher dados"
Responsável: Fila CSC - Passagens Aéreas e Hospedagem (papel 508)
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Opções de Reserva
  - PAHL_LOCACOES "Locações de Carro" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES] obrigatório
**PAHL_LOCACOES.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
camposVisiveis = None
camposHabilitados = None
vis = False
hab = False

pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
   # lista de campos a serem alteradas a visibilidade.
   camposVisiveis = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
   camposHabilitados = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
   if Formulario["PAHL_LOCACOES"].Valor == True:
      vis = True
      hab = True

   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado
       valor = Formulario[controle.Key].Valor
       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = vis
              valor = None
              break
       Formulario[controle.Key].Visivel = visivel
       
       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = hab
              break
       Formulario[controle.Key].Habilitado = habilitado
       Formulario[controle.Key].Valor = valor
       
   #Formulario["PAH_MOTIVO_SOL"].Visivel = False
   
   #cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]
   
   #if (Formulario["PAHL_PASSAGENS"].Valor == True or Formulario["PAHL_HOSPEDAGENS"].Valor == True or Formulario["PAHL_LOCACOES"].Valor == True) and cargos.Contains(pessoa["CARGO_FUNCIONAL"]):
   Formulario["PAH_MOTIVO_SOL"].Visivel = True
   Formulario["PAH_MOTIVO_SOL"].Habilitado = True
   #else:
   #   Formulario["PAH_MOTIVO_SOL"].Visivel = False
   #   Formulario["PAH_MOTIVO_SOL"].Habilitado = False
```
  - PAHL_PASSAGENS "Reserva de Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS] obrigatório
**PAHL_PASSAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposVisiveis = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   if Formulario["PAHL_PASSAGENS"].Valor == True:
#      vis = True
#      hab = True
#    
#
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
#       
#   cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]

if (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = True
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = True
    Formulario["RESERVA_DE_VOO"].Visivel = False
    Formulario["RESERVA_DE_VOO"].Habilitado = False
    #Formulario["DESCRICAO_OBRIG"].Visivel = True
    #Formulario["DESCRICAO_OBRIG"].Habilitado = True
    Formulario["CSC_OBS"].Visivel = True
    Formulario["CSC_OBS"].Habilitado = True
elif (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
    Formulario["RESERVA_DE_VOO"].Visivel = True
    Formulario["RESERVA_DE_VOO"].Habilitado = True    
    #Formulario["DESCRICAO_OBRIG"].Visivel = True
    #Formulario["DESCRICAO_OBRIG"].Habilitado = True
    Formulario["CSC_OBS"].Visivel = True
    Formulario["CSC_OBS"].Habilitado = True
else:
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
    Formulario["RESERVA_DE_VOO"].Visivel = False
    Formulario["RESERVA_DE_VOO"].Habilitado = False    
   # Formulario["DESCRICAO_OBRIG"].Visivel = False
   # Formulario["DESCRICAO_OBRIG"].Habilitado = False
    Formulario["CSC_OBS"].Visivel = False
    Formulario["CSC_OBS"].Habilitado = False
```
  - PAHL_HOSPEDAGENS "Reserva de Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS] obrigatório
**PAHL_HOSPEDAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
camposVisiveis = None
camposHabilitados = None
vis = False
hab = False

pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
   # lista de campos a serem alteradas a visibilidade.
   camposVisiveis = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL","CSC_OBS"]
   camposHabilitados = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL","CSC_OBS"]
   if Formulario["PAHL_HOSPEDAGENS"].Valor == True:
      vis = True
      hab = True
   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado
       valor = Formulario[controle.Key].Valor
       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = vis
              valor = None
              break
       Formulario[controle.Key].Visivel = visivel
       
       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = hab
              break
       Formulario[controle.Key].Habilitado = habilitado
       Formulario[controle.Key].Valor = valor
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do Deslocamento
  - FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - CELULAR "Celular do Favorecido" [TextBox String → CP_ORDEM_SERVICO.CELULAR] — Configuracao={"Mascara":"00000000000"}
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO] obrigatório
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True



Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False



Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None



cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()
    if desc_colaborador.ToString() != 'FUNCIONARIOS CONCURSADOS' and funcao.ToString()=='':
        Formulario["FUNCAO_DESLOCAMENTO"].Valor = cargo.ToString()
    
        


if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
    
#if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
    #Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
#else:
    #Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    #Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
```
  - MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO] obrigatório
**TIPO_DESLOCAMENTO.ScriptModificado**
```python
if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    Formulario["NUMERO_NT"].Habilitado = True
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False  
    Formulario["SIM_NAO_REFEICAO"].Habilitado = False
    Formulario["SIM_NAO_REFEICAO"].Valor = "Não"
    
else:
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["COTACAO_DOLAR"].Visivel = False
    Formulario["COTACAO_DOLAR"].Habilitado = False   
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
    Formulario["PAIS"].Visivel = False
    Formulario["PAIS"].Habilitado = False  
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = True
    
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["DIARIA_COTACAO_REAL"].Visivel = False
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
    Formulario["SIM_NAO_REFEICAO"].Habilitado = True
    
    
    Formulario["LABEL1"].Visivel =  False
    Formulario["LABEL1"].Habilitado = False
    Formulario["NUMERO_NT"].Visivel =  False
    Formulario["NUMERO_NT"].Habilitado = False
```
  - ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A] obrigatório
**ACOMPANHANDO_GRUPO_A.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#    Formulario["SIM_NAO"].Visivel = False
#    Formulario["SIM_NAO"].Habilitado = False 
  

else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False 
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["SIM_NAO"].Habilitado = True
     
    
    
#    
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Não":
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
#    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#
#else:
#     Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
```
  - SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
```
  - NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO] obrigatório
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] — Coluna=2
**CIDADE_DESTINO.ScriptModificado**
```python
sqlConsultaCidadeDestino = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao ||' - '|| c.id_estado as cidade FROM cidade_v c WHERE id_cidade = '"+Formulario["CIDADE_DESTINO"].Valor.ToString()+"'")

sqlConsultaClassificacao = DB.ExecuteDataTable("select DISTINCT CLASSIFICACAO, CIDADE || ' - ' || UF AS cidadeuf from Z_00143_CIDADES_CLASSIFICACOES where CIDADE || ' - ' || UF = '"+sqlConsultaCidadeDestino.Rows[0]["CIDADE"].ToString()+"'")

for classificacao in sqlConsultaClassificacao.Rows:
    Formulario["CIDADE_CLASSIFICACAO"].Valor = classificacao["CLASSIFICACAO"].ToString()
```
  - CIDADE_CLASSIFICACAO "Cidade Classificação" [TextBox String → CPE_CSC.CIDADE_CLASSIFICACAO]
  - CIDADE_DESTINO_INTERNACIONAL "Cidade de Destino (Internacional)" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL] obrigatório — Coluna=2
  - PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS] obrigatório — Coluna=3
**PAIS.ScriptModificado**
```python
  
        ################## grupo A
if Formulario["PAIS"].Valor == "AFEGANISTÃO" or Formulario["PAIS"].Valor == "ARMÊNIA" or Formulario["PAIS"].Valor == "BANGLADESH" or Formulario["PAIS"].Valor == "BELARUS" or Formulario["PAIS"].Valor == "BENIN" or Formulario["PAIS"].Valor == "BOLÍVIA" or Formulario["PAIS"].Valor == "BURKINAFASSO" or Formulario["PAIS"].Valor == "BUTÃO"  or Formulario["PAIS"].Valor == "CHILE" or Formulario["PAIS"].Valor == "COMORES" or Formulario["PAIS"].Valor == "REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA" or Formulario["PAIS"].Valor == "COSTA RICA" or Formulario["PAIS"].Valor == "EL SALVADOR" or Formulario["PAIS"].Valor == "EQUADOR" or Formulario["PAIS"].Valor == "ESLOVÊNIA" or Formulario["PAIS"].Valor == "FILIPINAS" or Formulario["PAIS"].Valor == "GÂMBIA" or Formulario["PAIS"].Valor == "GUIANA" or Formulario["PAIS"].Valor == "GUINÉ BISSAU" or Formulario["PAIS"].Valor == "GUINÉ" or Formulario["PAIS"].Valor == "HONDURAS" or Formulario["PAIS"].Valor == "INDONÉSIA" or Formulario["PAIS"].Valor == "IRÃ" or Formulario["PAIS"].Valor == "IRAQUE" or Formulario["PAIS"].Valor == "LAOS" or Formulario["PAIS"].Valor == "LÍBANO" or Formulario["PAIS"].Valor == "MALÁSIA" or Formulario["PAIS"].Valor == "MALDIVAS" or Formulario["PAIS"].Valor == "MARROCOS" or Formulario["PAIS"].Valor == "MONGÓLIA" or Formulario["PAIS"].Valor == "NAMÍBIA" or Formulario["PAIS"].Valor == "MYANMAR" or Formulario["PAIS"].Valor == "NAURU" or Formulario["PAIS"].Valor == "NEPAL"or Formulario["PAIS"].Valor == "NICARÁGUA" or Formulario["PAIS"].Valor == "PANAMÁ" or Formulario["PAIS"].Valor == "PARAGUAI" or Formulario["PAIS"].Valor == " REP. CENTRO AFRICANA" or Formulario["PAIS"].Valor == "REPÚBLICA TOGOLESA" or Formulario["PAIS"].Valor == "SALOMÃO" or Formulario["PAIS"].Valor == "SAMOA" or Formulario["PAIS"].Valor == "SERRA LEOA" or Formulario["PAIS"].Valor == "SÍRIA" or Formulario["PAIS"].Valor == "SOMÁLIA" or Formulario["PAIS"].Valor == "SRI LANKA" or Formulario["PAIS"].Valor == "TURQUIA" or Formulario["PAIS"].Valor == "TADJIQUISTÃO" or Formulario["PAIS"].Valor == "TAILÂNDIA" or Formulario["PAIS"].Valor == "TIMOR LESTE" or Formulario["PAIS"].Valor == "TONGA" or Formulario["PAIS"].Valor == "TUNÍSIA" or Formulario["PAIS"].Valor == "TURCOMENISTÃO" or Formulario["PAIS"].Valor == "TUVALU" or Formulario["PAIS"].Valor == "VIETNÃ" or Formulario["PAIS"].Valor == "ZIMBÁBUE":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "220"
                        
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "200"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "190"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "180"
          
    else:
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "170"
            
        ###################### grupo B    
            
elif Formulario["PAIS"].Valor == "ÁFRICA DO SUL" or Formulario["PAIS"].Valor == "ALBÂNIA" or Formulario["PAIS"].Valor == "ANDORA" or Formulario["PAIS"].Valor == "ARGÉLIA" or Formulario["PAIS"].Valor == "ARGENTINA" or Formulario["PAIS"].Valor == "AUSTRÁLIA" or Formulario["PAIS"].Valor == "BELIZE" or Formulario["PAIS"].Valor == "BÓSNIA-HERZEGÓVINA"  or Formulario["PAIS"].Valor == "BURUNDI" or Formulario["PAIS"].Valor == " CABO VERDE" or Formulario["PAIS"].Valor == "CAMARÕES" or Formulario["PAIS"].Valor == "CAMBOJA" or Formulario["PAIS"].Valor == "CATAR" or Formulario["PAIS"].Valor == "CHADE" or Formulario["PAIS"].Valor == "CHINA" or Formulario["PAIS"].Valor == "CHIPRE" or Formulario["PAIS"].Valor == "COLÔMBIA" or Formulario["PAIS"].Valor == "DOMINICA" or Formulario["PAIS"].Valor == "EGITO" or Formulario["PAIS"].Valor == "ERITRÉIA" or Formulario["PAIS"].Valor == "ESTÔNIA" or Formulario["PAIS"].Valor == "ETIÓPIA" or Formulario["PAIS"].Valor == "GANA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "HUNGRIA" or Formulario["PAIS"].Valor == "IEMEN" or Formulario["PAIS"].Valor == " ILHAS MARSHALL" or Formulario["PAIS"].Valor == "ÍNDIA" or Formulario["PAIS"].Valor == "KIRIBATI" or Formulario["PAIS"].Valor == "LESOTO" or Formulario["PAIS"].Valor == "LÍBIA" or Formulario["PAIS"].Valor == "MACEDÔNIA"or Formulario["PAIS"].Valor == "MADAGASCAR" or Formulario["PAIS"].Valor == "MALAUÍ" or Formulario["PAIS"].Valor == "MICRONÉSIA" or Formulario["PAIS"].Valor == "MOÇAMBIQUE" or Formulario["PAIS"].Valor == "MOLDÁVIA" or Formulario["PAIS"].Valor == "NÍGER" or Formulario["PAIS"].Valor == "NIGÉRIA" or Formulario["PAIS"].Valor == "NOVA ZELÂNDIA" or Formulario["PAIS"].Valor == "PALAU" or Formulario["PAIS"].Valor == "PAPUA NOVA GUINÉ" or Formulario["PAIS"].Valor == "PAQUISTÃO" or Formulario["PAIS"].Valor == "PERU" or Formulario["PAIS"].Valor == "POLÔNIA" or Formulario["PAIS"].Valor == "QUÊNIA" or Formulario["PAIS"].Valor == "REPÚBLICA DOMINICANA" or Formulario["PAIS"].Valor == "ROMÊNIA" or Formulario["PAIS"].Valor == "RUANDA" or Formulario["PAIS"].Valor == " SÃO TOMÉ E PRÍNCIPE" or Formulario["PAIS"].Valor == "SENEGAL" or Formulario["PAIS"].Valor == "TANZÂNIA" or Formulario["PAIS"].Valor == "SUDÃO"  or Formulario["PAIS"].Valor == "URUGUAI" or Formulario["PAIS"].Valor == "UZBEQUISTÃO" or Formulario["PAIS"].Valor == "VENEZUELA":

    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "280"

    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "270"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "260"
        
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "250"
                    
                    

            ################### grupo C

            
elif Formulario["PAIS"].Valor == "ANTÍGUA E BARBUDA" or Formulario["PAIS"].Valor == "ARÁBIA SAUDITA" or Formulario["PAIS"].Valor == "AZERBAIDJÃO" or Formulario["PAIS"].Valor == "BAHAMAS" or Formulario["PAIS"].Valor == "BAREINE" or Formulario["PAIS"].Valor == "BOTSUANA" or Formulario["PAIS"].Valor == "BRUNEI DARUSSALAM" or Formulario["PAIS"].Valor == "BULGÁRIA"  or Formulario["PAIS"].Valor == "CANADÁ" or Formulario["PAIS"].Valor == "CINGAPURA" or Formulario["PAIS"].Valor == "CONGO" or Formulario["PAIS"].Valor == "COSTA DO MARFIM" or Formulario["PAIS"].Valor == "CUBA" or Formulario["PAIS"].Valor == "DJIBUTI" or Formulario["PAIS"].Valor == "EMIRADOS ÁRABES" or Formulario["PAIS"].Valor == "FIJI" or Formulario["PAIS"].Valor == "GABÃO" or Formulario["PAIS"].Valor == "GUATEMALA" or Formulario["PAIS"].Valor == "REPÚBLICA DEMOCRÁTICA DO CONGO" or Formulario["PAIS"].Valor == "JAMAICA" or Formulario["PAIS"].Valor == "JORDÂNIA" or Formulario["PAIS"].Valor == "LETÔNIA" or Formulario["PAIS"].Valor == "LIBÉRIA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "MAURÍCIO" or Formulario["PAIS"].Valor == "MAURITÂNIA" or Formulario["PAIS"].Valor == "MÉXICO" or Formulario["PAIS"].Valor == "MALTA" or Formulario["PAIS"].Valor == " REPÚBLICA TCHECA" or Formulario["PAIS"].Valor == "RÚSSIA" or Formulario["PAIS"].Valor == "SAN MARINO" or Formulario["PAIS"].Valor == "SANTA LÚCIA"or Formulario["PAIS"].Valor == "SÃO CRISTOVÃO E NÉVIS" or Formulario["PAIS"].Valor == "SÃO VICENTE E GRANADINAS" or Formulario["PAIS"].Valor == "TAIWAN" or Formulario["PAIS"].Valor == "TRINIDAD E TOBAGO" or Formulario["PAIS"].Valor == "UCRÂNIA" or Formulario["PAIS"].Valor == "UGANDA" or Formulario["PAIS"].Valor == "ZÂMBIA":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "330"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "320"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "310"
    
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"     
                    
                
            #################### grupo D 
if Formulario["PAIS"].Valor == "ALEMANHA" or Formulario["PAIS"].Valor == "ANGOLA" or Formulario["PAIS"].Valor == "ÁUSTRIA" or Formulario["PAIS"].Valor == "BARBADOS" or Formulario["PAIS"].Valor == "BÉLGICA"or Formulario["PAIS"].Valor == "CAZAQUISTÃO" or Formulario["PAIS"].Valor == "CORÉIA DO SUL" or Formulario["PAIS"].Valor == "CROÁCIA"  or Formulario["PAIS"].Valor == "DINAMARCA" or Formulario["PAIS"].Valor == "ESPANHA" or Formulario["PAIS"].Valor == "ESTADOS UNIDOS DA AMÉRICA" or Formulario["PAIS"].Valor == "FINLÂNDIA" or Formulario["PAIS"].Valor == "FRANÇA" or Formulario["PAIS"].Valor == "GRANADA" or Formulario["PAIS"].Valor == "GRÉCIA HONG KONG" or Formulario["PAIS"].Valor == "IRLANDA" or Formulario["PAIS"].Valor == "ISLÂNDIA" or Formulario["PAIS"].Valor == "ISRAEL" or Formulario["PAIS"].Valor == "ITÁLIA" or Formulario["PAIS"].Valor == "JAPÃO" or Formulario["PAIS"].Valor == "KUAITE" or Formulario["PAIS"].Valor == "LIECHTENSTEIN" or Formulario["PAIS"].Valor == "LUXEMBURGO" or Formulario["PAIS"].Valor == "MÔNACO" or Formulario["PAIS"].Valor == "MONTENEGRO" or Formulario["PAIS"].Valor == "NORUEGA" or Formulario["PAIS"].Valor == "OMÃ" or Formulario["PAIS"].Valor == "PEÍSES BAIXOS" or Formulario["PAIS"].Valor == "PORTUGAL" or Formulario["PAIS"].Valor == "REINO UNIDO" or Formulario["PAIS"].Valor == "REPÚBLICA QUIRGUIZ" or Formulario["PAIS"].Valor == "SEICHELES" or Formulario["PAIS"].Valor == "SÉRVIA SUAZILÂNDIA" or Formulario["PAIS"].Valor == "SUÉCIA" or Formulario["PAIS"].Valor == "SUÍÇA" or Formulario["PAIS"].Valor == "VANUATU":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "460"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "420"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "390"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "370"
                  
                  
    else:
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
                    
if (Formulario["PAIS"].Valor != "") or (Formulario["PAIS"].Valor != None):
    Formulario["TIPO_DESTINO"].Valor = "Exterior"
    Formulario["TIPO_DESTINO"].Habilitado = False
```
  - TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO] obrigatório — Coluna=4
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA] obrigatório
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] obrigatório — Coluna=3
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] obrigatório — Configuracao={"Mascara":"00:00"}
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] obrigatório — Coluna=3; Configuracao={"Mascara":"00:00"}
**RETORNO_HORA.ScriptModificado**
```python
import clr 
import datetime

data1 = ""
data2 = ""

data1 = Formulario["SAIDA"].Valor
data2 = Formulario["RETORNO_DIA"].Valor
 
delta = data2 - data1
diferenca = delta.Days

if diferenca == 0 or diferenca == '0':
    diferenca = 1


Formulario["DIAS_DE_TRA"].Valor = diferenca
Formulario["DIAS_DE_TRA"].Habilitado = False
```
  - VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR] obrigatório
**VALOR_DIARIA_DOLAR.ScriptModificado**
```python
if Convert.ToDecimal(Formulario["VALOR_DIARIA_DOLAR"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DOLAR"].Valor):
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["CAMPO_VALIDACAO_DOLAR"].Valor
else:
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["VALOR_DIARIA_DOLAR"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True

valorTotal1 = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor)

valorTotal1 = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal1 


#OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal1
```
  - DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
  - TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM] obrigatório
**TIPO_HOSPEDAGEM.ScriptModificado**
```python
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
    Formulario["QUANTIDADE_DIARIA"].Visivel = False
    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0" 
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = False        

if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa COM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = True
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = True

    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa COM apresentação de NF":
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False
       
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    Formulario["VALOR_DIARIA"].Valor = "" 
    
#Remover quando não houver mais tipo de hospedagens avulsas!!!!!!    
if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = True
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = True
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False
    
 
queryAdesaoDiariaAvulaSemApresentarNF = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA Where OCORRENCIA.ASSUNTO = 'Adesão a diárias avulsas sem comprovação documental' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+Formulario["FAVORECIDO_DESLOCAMENTO"].Valor+"'")

if queryAdesaoDiariaAvulaSemApresentarNF.Rows.Count == 0 and Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF":
    Formulario.ExibeMensagem("Parece que seu aceite, Adesão a diárias avulsas sem comprovação documental, não foi feito. O Aceite é necessário para este tipo de solicitação.")
 
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada":
    Formulario["VALOR_DIARIA"].Valor = 0
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Valor = 0
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 0
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 0
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = 0
    
#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = True
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA"].Visivel = True
#    Formulario["VALOR_DIARIA"].Habilitado = True
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False    
    

#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = False
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
```
  - QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA] obrigatório
**QUANTIDADE_DIARIA.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import OutputSubProcesso
def calculaDiaria():
    ############### SE O FAVORECIDO FOR DO GRUPO C MAS ESTARÁ ACOMPANHANDO O GRUPO B RECEBE O VALOR DO GRUPO B 
    
    if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    elif Formulario["SIM_NAO"].Valor == "Sim" :
          if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 
                 Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                
          elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO E BRASILIA
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
            
          elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
              Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
          else: 
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
      
    else:     
            
        ############## SE FOR DO GRUPO A -  PRESIDENTE / DIRETOR / CONSELHEIRO NÃO TEM LIMITE   
        if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
            
            
            
        ############## SE O FAVORECIDO FOR DO GRUPO B  ELE RECEBE REFERENTE A CIDADE     
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "SUPERINTENDENTE":
            if Formulario["CIDADE_DESTINO"].Valor == "3550308 ": # SAO PAULO 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO OutputSubProcesso BRASILIA
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                      Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
            else:
                Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                  
                  
        ############## DEMAIS CARGOS
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor != "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "SUPERINTENDENTE":
              
              if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 3550308 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550" 
                    
              elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO ou BRASILIA
                        Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                        
              elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                          Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "370" 
                          
              else:
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "350"
                  

              
              
calculaDiaria()
     
############ VALOR FINAL DO ADIANTAMENTO EM DIARIAS      
diasViagem = Convert.ToInt32(Formulario["DIAS_DE_TRA"].Valor)
diasHospedagem = Convert.ToInt32(Formulario["QUANTIDADE_DIARIA"].Valor)



if diasHospedagem > diasViagem:
    mensagem = "Quantidade de Diária Excedida! Máximo Permitido: " + Formulario["DIAS_DE_TRA"].Valor + " Verifique a saída e o retorno"
    Formulario.ExibeMensagem(mensagem)      
    Formulario["VALOR_DIARIA"].Habilitado = False
else:
    Formulario["VALOR_DIARIA"].Habilitado = True   


#Valor parcela complementar    



if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":

    Formulario["PARCELA_COMPLEMENTAR"].Valor = "0"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0"
   
else:    
    Formulario["PARCELA_COMPLEMENTAR"].Valor = "19,74"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    
    pc = Formulario["PARCELA_COMPLEMENTAR"].Valor 
    qtd = Formulario["QUANTIDADE_DIARIA"].Valor
    total = 0

    total = pc * qtd
    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = total
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = True


#Define o valor para hospedagem do tipo avulsa
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "A":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 230.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 230.00
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "B":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 250.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 250.00

if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "C":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 270.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 270.00  
    

#if (Formulario["TIPO_DESTINO"].Valor == "Interior") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "350"
#    
#if (Formulario["TIPO_DESTINO"].Valor == "Capital") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "500"
#
#import System.Text
#daysOffText = System.Text.StringBuilder()
#
# #RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#   
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            return True
#    return False
#   
#def workingDays(totalDays, firstDate):
#    
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#saida = Formulario["SAIDA"].Valor
#retorno  = Formulario["RETORNO_DIA"].Valor
#
#totalDias = (retorno - saida).TotalDays  
#count = 0
#
#totalDiasUteis = workingDays(totalDias,saida) 
#totalDiasNaoUteis = totalDias - totalDiasUteis
#
############### almoço e janta de ambos os dias
#quantReduzida = totalDiasUteis  
#quantIntegral = (totalDiasNaoUteis * 2) + totalDiasUteis
#
#
#

#Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalDiasUteis 
#Formulario["QTD_REFEICAO_INTEGRAL"].Valor = totalDiasNaoUteis
#
#
#Formulario["VALOR_REF_REDUZIDA"].Valor = totalDiasUteis * 18.39
#Formulario["VALOR_REF_INTEGRAL"].Valor = totalDiasNaoUteis *  64.36
#
#
#OrdemServico.AdicionaComentario("WorkingDays "+totalWorkingDays.ToString(),False)
#OrdemServico.AdicionaComentario(daysOffText.ToString(),False )

#OrdemServico["totalWorkingDays"] = totalWorkingDays
```
  - CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR] obrigatório — Coluna=2
  - DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL] obrigatório — Coluna=3
  - VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA] obrigatório
**VALOR_DIARIA.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
         Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor
    



if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE": 
     Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor


     
     
if Convert.ToDecimal(Formulario["VALOR_DIARIA"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DIARIA"].Valor):
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["CAMPO_VALIDACAO_DIARIA"].Valor
else:
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True

valorTotal = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["VALOR_DIARIA_AUTORIZADO"].Valor)

valorTotal = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal 


OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal
```
  - LABEL1 "Cotação do Dólar Americano Conforme Aprovado na NT" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO] obrigatório — Coluna=2
  - CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA] obrigatório
  - VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA] obrigatório
  - COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR] obrigatório
**COTACAO_DOLAR.ScriptModificado**
```python
#import System
#
#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)
#
#
#Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor) = valorTotal


valorTotal = 0
vtd = Formulario["VALOR_TOTAL_DIARIA"].Valor
cd = Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)

valorTotal = vtd * cd

Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal




#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * (Formulario["COTACAO_DOLAR"].Valor)
#
#
#Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal
#

#diariaReal = ""
#cotacao = ""
#valorTotal = ""
#
#diariaReal = Convert.ToDouble(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#cotacao = Convert.ToDouble(Formulario["COTACAO_DOLAR"].Valor)
```
  - DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL] obrigatório — Coluna=2
  - NUMERO_NT "Número da Nota Técnica" [TextBox String → CPE_CONTRATOS.NUMERO_NT] obrigatório — Configuracao={"Mascara":"0000/0000"}
  - PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR] obrigatório
  - TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR] obrigatório
  - LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE] obrigatório
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM] obrigatório
  - MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO] obrigatório
**MEIO_LOCOMOCAO.ScriptModificado**
```python
if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = True
    Formulario["VALOR_DISTANCIA"].Visivel = True
    Formulario["VALOR_DISTANCIA"].Habilitado = True
else:
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False
    Formulario["VALOR_DISTANCIA"].Visivel = False
    Formulario["VALOR_DISTANCIA"].Habilitado = False
    
if (Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Locado" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro da Frota" or Formulario["MEIO_LOCOMOCAO"].Valor == "Barco") and Formulario ["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica":
    Formulario["VIAGEM_LONGA"].Visivel = True
    Formulario["VIAGEM_LONGA"].Habilitado = True
else:
    Formulario["VIAGEM_LONGA"].Visivel = False
    Formulario["VIAGEM_LONGA"].Habilitado = False 
    
    
    
##if Formulario["MEIO_LOCOMOCAO"].Valor == "Avião" or Formulario["MEIO_LOCOMOCAO"] == "Ônibus Interestadual":
##    Formulario["VALOR_PASSAGEM"].Visivel = True
##    Formulario["VALOR_PASSAGEM"].Habilitado = True
##    Formulario["VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = True
##else:
##    Formulario["VALOR_PASSAGEM"].Visivel = False
##    Formulario["VALOR_PASSAGEM"].Habilitado = False
##    Formulario["VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False    
#    
    






##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral
############# calculo dias
#import clr 
#import datetime
#import System.Text
# 
#
#
#zero = 0
#valorRefIntegral = 64.36
#valorRefReduzida = 18.39
#
#
#
#daysOffText = System.Text.StringBuilder()
#
#
###RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#    #feriados = 0
#    
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            #feriados += 2
#            return True
#    return False
#
#
#def countHolidays(firstDate, lastDate):
#    totalHolidays = 0
#    currentDay = firstDate
#
#    while currentDay <= lastDate:
#        if isHoliday(currentDay):
#            totalHolidays += 1
#        currentDay = currentDay.AddDays(1)
#
#    return totalHolidays
#
#    
#def workingDays(totalDays, firstDate):
#
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        
#        
#        
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#
#    
#def countSaturdays(firstDate, lastDate):
#    saturdays = 0
#    currentDay = firstDate
#    
#    while currentDay <= lastDate:
#        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
#            saturdays += 2
#        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
#    
#    return saturdays
#
#    
#firstDate = Formulario["SAIDA"].Valor
#lastDate = Formulario["RETORNO_DIA"].Valor
#
#totalDays = (lastDate - firstDate).TotalDays
#count = 0
#
#
#
#
#
#totalWorkingDays = workingDays(totalDays,firstDate)
#holidaysCount = countHolidays(firstDate, lastDate)
#saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2
#
#
##Quantidade de refeições Reduzias e integrais
#quantRed = totalWorkingDays
#quantInt = saturdays + totalWorkingDays 
#
#
#
#
#
#
##Atribuindo valor a variável
#saidaHora = Formulario["SAIDA_HORA"].Valor 
#retornoHora = Formulario["RETORNO_HORA"].Valor 
#
##Split de horário, separando hora de minuto
#hora = saidaHora.Split(':');     
#horaRetorno = retornoHora.Split(':');
#
##Atribuindo valor de horário e minuto de acordo com o índice da variável
#horarioSaida = hora[0]
#minutoSaida = hora[1]
#
#horarioRetorno = horaRetorno[0] 
#minutoRetorno = horaRetorno[1]
#
#
#
##SAIDA DIAS ÚTEIS
#
#
##1 maior q o 2
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
##    quantRed = quantRed - 1
##   
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
##    quantInt = quantInt - 1
##   
##RETORNO DIAS ÚTEIS
##1 menor q o 2   
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
##    quantRed = quantRed - 1
##    quantInt = quantInt - 1
##    
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
##    quantInt = quantInt - 1
##    #teste abaixo
##    quantRed = quantRed - 1
#
#
#
#
#
##DIAS UTEIS
#
#if workingDays(0,firstDate):
#    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if workingDays(0,lastDate):    
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
##Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
################################################################
#    
##SAÍDA FINAIS DE SEMANA E/OU FERIADOS
#
#if not  workingDays(0,firstDate):
#    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if not  workingDays(0,lastDate):
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1   
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
#  
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#    
#else:
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
#  
#    
#if quantRed > (totalWorkingDays):
#    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
#    Formulario.ExibeMensagem(mensagem)    
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    
#
############## calculo valor total
#
#refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
#refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
#valorTotalRefeicoes = refIntegral + refReduzida
#Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
#Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
#Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
#
#
#
#
#
#
```
  - VIAGEM_LONGA "Distância da Viagem de Carro (Programa Valor)" [DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA] obrigatório
  - PREVISAO_DISTANCIA_KM "Previsão de distancia em KM (Para recebimento de R$1,30 por KM)" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM] obrigatório
**PREVISAO_DISTANCIA_KM.ScriptModificado**
```python
import System


Formulario["VALOR_DISTANCIA"].Habilitado = False

valorTotal = 0

distancia = Formulario["PREVISAO_DISTANCIA_KM"].Valor
valorTotal = distancia * 1.30 


Formulario["VALOR_DISTANCIA"].Valor = valorTotal
#OrdemServico["VALOR_DISTANCIA"] = valorTotal
#
```
  - VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA] obrigatório — Coluna=2
  - SIM_NAO_REFEICAO "O Empregado/Gestor terá direito a refeição complementar?" [DropDownList String → CPE_DESLOCAMENTO.SIM_NAO_REFEICAO] obrigatório
**SIM_NAO_REFEICAO.ScriptModificado**
```python
import clr 
import datetime
import System.Text
 


zero = 0
valorRefIntegral = 71
valorRefReduzida = 20.29



daysOffText = System.Text.StringBuilder()


##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False


def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate

    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)

    return totalHolidays

    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
   


    
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
    
    return saturdays

    
firstDate = Formulario["SAIDA"].Valor
lastDate = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0





totalWorkingDays = workingDays(totalDays,firstDate)
holidaysCount = countHolidays(firstDate, lastDate)
saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2


#Quantidade de refeições Reduzias e integrais
quantRed = totalWorkingDays
quantInt = saturdays + totalWorkingDays 






#Atribuindo valor a variável
saidaHora = Formulario["SAIDA_HORA"].Valor 
retornoHora = Formulario["RETORNO_HORA"].Valor 

#Split de horário, separando hora de minuto
hora = saidaHora.Split(':');     
horaRetorno = retornoHora.Split(':');

#Atribuindo valor de horário e minuto de acordo com o índice da variável
horarioSaida = hora[0]
minutoSaida = hora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]



#SAIDA DIAS ÚTEIS


#1 maior q o 2
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
#    quantRed = quantRed - 1
#   
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
#    quantInt = quantInt - 1
#   
#RETORNO DIAS ÚTEIS
#1 menor q o 2   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRed = quantRed - 1
#    quantInt = quantInt - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantInt = quantInt - 1
#    #teste abaixo
#    quantRed = quantRed - 1





#DIAS UTEIS

if workingDays(0,firstDate):
    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if workingDays(0,lastDate):    
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
#Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS

if not  workingDays(0,firstDate):
    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if not  workingDays(0,lastDate):
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1   


if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Habilitado = False
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Habilitado = True
  
    
if quantRed > (totalWorkingDays):
    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
    Formulario.ExibeMensagem(mensagem)    
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    

############# calculo valor total

refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
valorTotalRefeicoes = refIntegral + refReduzida

if Formulario["SIM_NAO_REFEICAO"].Valor == "Sim":
    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
    Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
    Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Valor = zero
    Formulario["VALOR_REF_INTEGRAL"].Valor = zero
    Formulario["VALOR_TOTAL_REFEICAO"].Valor = zero  
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
```
  - VALOR_REF_REDUZIDA "Valor Refeições Reduzidas" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA] obrigatório
  - VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO] obrigatório — Coluna=2
  - VALOR_REF_INTEGRAL "Valor refeições integrais" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS] obrigatório — Coluna=2
**VALOR_DESPESAS.ScriptModificado**
```python
import System

diariaAvulsa = 0
valorDist = 0 



#valorTotalPrestContas = OrdemServico.GetCustom("VALOR_DESPESAS") + OrdemServico.GetCustom("VALOR_DISTANCIA") + OrdemServico.GetCustom("VALOR_TOTAL_DIARIA")
#valorTotSemPrestContas = refeições, diaria de hotel contratada/sem hospedagem e parcela complementar

if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica") or (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
    
elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False


    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento

########Deslocamento para viagem internacional###############
elif Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    
    valorTotalAdiantamento = 0


    totalDiaria = 0
    ##valorAvicao = 0
    outrasDespesas = 0
    ##valorDistancia = 0
    #complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    #complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
    valorTotalAdiantamento = totalDiaria + outrasDespesas
    
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento
    
else:
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0
    
    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    
    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
    #Esta faltando pegar valor de diaria e da parcela complementar para o valor total
    


 
#Valores a prestar conta 
    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
#    
#    
#    diariaAvulsa = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#    
#    
#else:
#    diariaAvulsa = 0
#
#
#    
#if Formulario["VALOR_DISTANCIA"].Valor != 0:
#    valorDist = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
#
#else:
#    valorDist = 0 
#    
#outrasDespesas2 = Convert.ToDecimal(outrasDespesas)
#
#valorTotalPrestContas = outrasDespesas2 + diariaAvulsa + valorDist
#
#
#
#Formulario["VALOR_TOT_PREST_CONTAS"].Valor = Convert.ToDecimal(valorTotalPrestContas)
#
#
#
##Valores sem necessidade de prestação de contas
#
#refeicoes = 0
#hospeda = 0
#complementar = 0
#
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA":
#
#    refeicoes = 0
#
#else:
#    refeicoes = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
#    
#
#    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada":
#   hospeda = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#   
#elif Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
#   hospeda = 0
#
#   
# 
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
#    complementar = 0
#else:
#    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
#    
#
#    
#totalSemPrestContas = complementar + hospeda + refeicoes
#
#Formulario["VALORTOTSEMCOMPROV"].Valor = Convert.ToDecimal(totalSemPrestContas)
















    #OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento
```
  - QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA] obrigatório
**QTD_REFEICAO_REDUZIDA.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    
qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL] obrigatório
**QTD_REFEICAO_INTEGRAL.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import System
import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False

qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO] obrigatório
  - DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Solicitação de Reservas
  - PAH_MOTIVO_SOL "Motivo da Solicitação" [DropDownList String → CPE_CSC.PAH_MOTIVO_SOL] obrigatório
  - PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES]
    - coluna CIA_AEREA obrigatório
    - coluna LOCALIZADOR obrigatório
    - coluna SEQUENCIA obrigatório
    - coluna VALOR_TRECHO
  - PAH_DATA_ENTRADA "Data de Entrada no Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA] obrigatório
  - PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM]
  - RESERVA_DE_VOO "Informações da Reserva de Voo - Nacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO]
    - coluna ALT_EXC obrigatório
    - coluna CIDADE_DESTINO obrigatório
    - coluna DATA_VOO obrigatório
    - coluna ALT_OU_EXC
    - coluna SEQUENCIA obrigatório
**RESERVA_DE_VOO.SEQUENCIA.ScriptModificado**
```python
rv = OrdemServico["RESERVA_DE_VOO"]

for seq in rv.Rows:
    if FormularioRegistro["SEQUENCIA"].Valor == seq["SEQUENCIA"]:
       Formulario.ExibeMensagem("A T E N Ç Ã O !!! \n Nº do Trecho já lançado!")
       FormularioRegistro["SEQUENCIA"].Valor = None
```
    - coluna QUANTIDADE_BAGAGENS obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna HORA_ESTIMADA_VOO obrigatório
    - coluna UF_ORIGEM obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna TRECHO obrigatório
    - coluna DESPACHO_BAGAGENS obrigatório
**RESERVA_DE_VOO.DESPACHO_BAGAGENS.ScriptModificado**
```python
#Sim;Não
FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = None
FormularioRegistro["QUANTIDADE_BAGAGENS"].Habilitado = FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Sim"

if FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Não":
   FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = 0
```
    - coluna AEROPORTO_ORIGEM obrigatório
    - coluna UF_DESTINO obrigatório
  - RESERVA_DE_VOO_INTERNACIONAL "Informações para Reserva de Voo - Internacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL]
    - coluna SEQUENCIA obrigatório
    - coluna TRECHO obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna AEROPORTO_ORIGEM obrigatório
    - coluna CIDADE_DESTINO obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna DATA_VOO obrigatório
    - coluna HORA_ESTIMADA_VOO obrigatório
    - coluna DESPACHO_BAGAGENS obrigatório
    - coluna QUANTIDADE_BAGAGENS obrigatório
  - PAH_DATA_SAIDA "Data de Saída do Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA] obrigatório
**PAH_DATA_SAIDA.ScriptModificado**
```python
if Formulario["PAH_DATA_SAIDA"].Valor <= Formulario["PAH_DATA_ENTRADA"].Valor:
   Formulario.ExibeMensagem("'Data de Saída do Hotel' deve ser maior que 'Data de Entrada no Hotel'!")
   Formulario["PAH_DATA_SAIDA"].Valor = None
```
  - PAH_EVENTO_HOTEL "Evento no Hotel?" [DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL]
**PAH_EVENTO_HOTEL.ScriptModificado**
```python
Formulario["PAH_HOTEL_EVENTO"].Visivel = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
Formulario["PAH_HOTEL_EVENTO"].Habilitado = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
```
  - PAH_HOTEL_EVENTO "Hotel do Evento" [TextBox String → CPE_CSC.PAH_HOTEL_EVENTO]
  - PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO]
  - PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO]
**PAHL_LOCACOES_CARRO.ScriptConfirmado**
```python
if Registro["DATA_HORA_DEVOLUCAO"] < Registro["DATA_HORA_RETIRADA"]:
   Formulario.ExibeMensagem("ATENÇÃO: Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
```
    - coluna DATA_HORA_DEVOLUCAO obrigatório
**PAHL_LOCACOES_CARRO.DATA_HORA_DEVOLUCAO.ScriptModificado**
```python
#if FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor < FormularioRegistro["DATA_HORA_RETIRADA"].Valor:
#   Formulario.ExibeMensagem("Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
#   FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor = None
```
    - coluna CPF_FAVORECIDO obrigatório
    - coluna LOCAL_RETIRADA obrigatório
    - coluna VALOR_LOCACAO
    - coluna CELULAR_FAVORECIDO obrigatório
    - coluna CARRO4X4 obrigatório
    - coluna DATA_HORA_RETIRADA obrigatório
    - coluna LOCAL_DEVOLUCAO obrigatório
  - CSC_OBS "Endereço do Local do Evento/Atendimento e outras observações (Informe até 2 sugestões de hotel, se houver)" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - DATA_INICIO_AUX1 "Data Início da Viagem" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1]

### [369120] Tarefa "Inserir dados no ERP
"
Responsável: Responsavel Processo (papel 1378)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO"))
favorecido = Pessoa.Carrega(idFavorecido)
nomeFavorecido = favorecido.Nome
orgao = Orgao.Carrega(favorecido.OrgaoId)
#sigla = orgao.Sigla
#OrdemServico.SetCustom("SCR_TODOS_RH",sigla.ToString())
#


matricula = OrdemServico.GetCustom("MATRICULA_DESLOCAMENTO")
sigla=DB.ExecuteScalar("select substr(organizacao,1,10) as uor from cad_funcionario_v where matricula='"+matricula.ToString()+"'")

#if OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString() != None and OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString() != '0' and OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString() != '':
#    valorTotal = Convert.ToDecimal(OrdemServico.GetCustom("VALOR_TOTAL_REEMBOLSO").ToString())
#OrdemServico.AdicionaComentario('teste10', False)    
total_carro_loc = None
valorAdiantamento = None
total_passag_contr = None
total_hosp_contr = None
if OrdemServico.GetCustom('VALOR_TOTAL_ADIANTAMENTO')!= None :
    valorAdiantamento = OrdemServico["VALOR_TOTAL_ADIANTAMENTO"].ToString()
   

valorCusteio = 0
if OrdemServico["VALOR_TOTAL_DIARIA"] != None:
    valorCusteio = valorCusteio+Convert.ToDecimal(OrdemServico["VALOR_TOTAL_DIARIA"])
    

if (not String.IsNullOrEmpty(OrdemServico.GetCustom('VALOR_TOTAL_REFEICAO').ToString())) and OrdemServico.GetCustom("VALOR_TOTAL_REFEICAO").ToString() != None and OrdemServico.GetCustom("VALOR_TOTAL_REFEICAO").ToString() != '0' and OrdemServico.GetCustom("VALOR_TOTAL_REFEICAO").ToString() != '':
    valorCusteio = valorCusteio+Convert.ToDecimal(OrdemServico.GetCustom("VALOR_TOTAL_REFEICAO"))
   

if OrdemServico["VALOR_DESPESAS"] != None :
    valorCusteio = valorCusteio+Convert.ToDecimal(OrdemServico["VALOR_DESPESAS"])
  
if (not String.IsNullOrEmpty(OrdemServico.GetCustom('VALOR_DISTANCIA').ToString())) and OrdemServico["VALOR_DISTANCIA"].ToString() != None and OrdemServico["VALOR_DISTANCIA"].ToString() != '0' and OrdemServico["VALOR_DISTANCIA"].ToString() != '':
    valorCusteio = valorCusteio+Convert.ToDecimal(OrdemServico["VALOR_DISTANCIA"])

  
if str(OrdemServico["TOTAL_COMPLEMENTAR"]) != 'None' and str(OrdemServico["TOTAL_COMPLEMENTAR"]) != '0' and str(OrdemServico["TOTAL_COMPLEMENTAR"]) != '':
        valorCusteio = valorCusteio+Convert.ToDecimal(OrdemServico["TOTAL_COMPLEMENTAR"])

numero = OrdemServico.Numero.ToString()
fornecedor_passivo = '001.110001.3000001000.219399.000000.000.00000'
fornecedor = '001.110001.3000001000.219399.000000.000.00000'


qry = "SELECT MAX(INICIO_DATA_FUNCAO), EMPRESA, SUBSTR('"+sigla.ToString()+"', 1, 1) AS PREFIXO  FROM CAD_FUNCIONARIO_V WHERE DATA_DE_DEMISSAO IS NULL AND MATRICULA = '" + matricula.ToString() + "' GROUP BY EMPRESA"


lista = Utils.ExecuteDataTable(qry)
if (lista != None):
    for linha in lista.Rows:
        if (DBNull.Value.Equals(linha["EMPRESA"]) != True ):
            empresa = linha["EMPRESA"].ToString()
            OrdemServico.SetCustom("NUM_CHAVE",empresa.ToString())
            
        if (DBNull.Value.Equals(linha["PREFIXO"]) != True ):
            scr = linha["PREFIXO"].ToString()
            OrdemServico.SetCustom("NUM_ITEM",scr.ToString())  


filial = OrdemServico["NUM_CHAVE"].ToString()
inicio = OrdemServico["NUM_ITEM"].ToString()
uor = sigla
termo = '00 DDL'
numero = OrdemServico.Numero.ToString()
if filial == '999994' and uor == '3000003204':
    filial ='410013'

#--- Prefixo da conta contábil (337 quando a UOR iniciar com 1 ou 2 e 343 quando iniciar com 3 ou 4)
if inicio == '1' or inicio == '2':
    prefixo = '337'
else:
    prefixo = '343'
OrdemServico.AdicionaComentario("valor adiantamento:"+valorAdiantamento.ToString(), False)
#######Adiantamento    
if valorAdiantamento != None and valorAdiantamento != '0' and valorAdiantamento != '':

    rubrica = '90303'
    nota = 'APV'
    fornecedor = '001.110001.3000001000.114201.000000.000.00000'
    conta = '001.110001.3000001000.219399.000000.000.00000'
    #conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
    OrdemServico.SetCustom("NUM_DOCU", conta)
    valor = DB.ExecuteScalar("select replace('"+ valorAdiantamento.ToString() + "',',','.') as valor from dual")
    valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '999999D99') as valor from dual")
    valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
        
    contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND REFERENCE1 LIKE '%ADIANT_LOC%'")
        
    contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%' AND NAME LIKE '%ADIANT_LOC%'")
    valordecimal = Convert.ToDecimal(valor)
    
    #OrdemServico.AdicionaComentario("valor:"+valordecimal.ToString(), False)
    #OrdemServico.AdicionaComentario("contInterfaceGL:"+contInterfaceGL.ToString(), False)
    #OrdemServico.AdicionaComentario("contGL:"+contGL.ToString(), False)
    
    #----- insert no GL
    #--- débito
    if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0' and valor.ToString() != '.00' and valor.ToString() !='0' and valordecimal > 0:
        
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'ADIANT_LOC"+ numero +"','ADIANT_LOC"+ numero +"') ")
        
        OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'ADIANT_LOC"+ numero +"','ADIANT_LOC"+ numero +"') ", False)
        
        #--- crédito
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'ADIANT_LOC"+ numero +"','ADIANT_LOC"+ numero +"') ")
        
        OrdemServico.AdicionaComentario("Procedure para Credito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'ADIANT_LOC"+ numero +"','ADIANT_LOC"+ numero +"') ", False)


    #--- Conta contábil (001.filial.uor.prefixo+rubrica)
    #conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
    #OrdemServico.SetCustom("NUM_DOCU", conta)
    #OrdemServico.AdicionaComentario('Conta contábil de débito no GL: '+ conta, False)
    #valor = DB.ExecuteScalar("select replace('"+ valorAdiantamento.ToString() + "',',','.') as valor from dual")
    #valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '9999D99') as valor from dual")
    #valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")
    
    contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")

    contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")   
    #----- insert no AP
    if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0' and valor.ToString() !='0' and valordecimal > 0:
        DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero.ToString() + "', SYSDATE+1, '"+ matricula.ToString() +"', "+valor.ToString() +", '"+ conta +"', '"+ termo +"','"+ fornecedor_passivo +"') ")
        
        OrdemServico.AdicionaComentario("Procedure AP: call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero.ToString() + "', SYSDATE+1, '"+ matricula.ToString() +"', "+valor.ToString() +", '"+ conta +"', '"+ termo +"','"+ fornecedor_passivo +"')", False)
########FIM Adiantamento


OrdemServico.Salva()
AvancaProximaAtividade = True
```

### [369121] EventoIntermediarioMensagem "Envio do Voucher"
Destinatário: Cliente e Favorecido Deslocamento (papel 1021)
ModeloComunicado: Envio do Voucher
Corpo do comunicado: Prezados(as),
Segue voucher da locomoção.
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2241; ClasseConfiguracao=Voucher

### [369122] EventoInicial ""
Responsável: Cliente (papel 18)
TipoSolicitacao: 08.03. Administração e Patrimônio - Deslocamento a Serviço
**ScriptValidacao**
```python
import calculos_deslocamento
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import clr 
import datetime
import System.Text


diasViagem = OrdemServico["DIAS_DE_TRA"]
diasHospedagem = OrdemServico["QUANTIDADE_DIARIA"]

if Convert.ToInt32(diasHospedagem) > Convert.ToInt32(diasViagem):
    Criticas.AdicionaPendencia("Quantidade de Diária Excedida! Máximo Permitido: " + diasViagem + " Verifique a saída e o retorno")    

qtdRef = qtdRefeicoes(OrdemServico.GetCustom("SAIDA"), OrdemServico.GetCustom("RETORNO_DIA"), OrdemServico.GetCustom("SAIDA_HORA"), OrdemServico.GetCustom("RETORNO_HORA"))


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(OrdemServico.GetCustom("QTD_REFEICAO_INTEGRAL")):
    Criticas.AdicionaPendencia("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(OrdemServico.GetCustom("QTD_REFEICAO_REDUZIDA")):
    Criticas.AdicionaPendencia("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    

#if OrdemServico.GetCustom["QUANTIDADE_DIARIA"] > OrdemServico.GetCustom["DIAS_DE_TRA"]:
#    Criticas.AdicionaPendencia("Quantidade de diárias excedidas!")    
    
#if OrdemServico["QTD_REFEICAO_INTEGRAL"].Habilitado == False:
#    Criticas.AdicionaPendencia("Quantidade de refeições integrais excedidas!")
#
#if OrdemServico["QTD_REFEICAO_REDUZIDA"].Habilitado == False:
#    Criticas.AdicionaPendencia("Quantidade de refeições reduzidas excedidas!")


#Valida cidades que possuem CAT quanto a solicitação avulsa e que são capitais
listaCidadesCAT = ["ARACAJU - SE", "BELEM - PA", "BELO HORIZONTE - MG", "BOA VISTA - RR", "BRASILIA - DF", "CAMPO GRANDE - MS", "CUIABA - MT", "CURITIBA - PR", "FLORIANOPOLIS - SC", "FORTALEZA - CE", "GOIANIA - GO", "SAO LUIS - MA", "MACAPA - AP", "MACEIO - AL", "NATAL - RN", "PALMAS - TO", "PORTO ALEGRE - RS", "PORTO VELHO - RO", "RECIFE - PE", "RIO BRANCO - AC", "RIO DE JANEIRO - RJ", "SALVADOR - BA", "SAO PAULO - SP", "SERRA - ES", "TERESINA - PI", "VITORIA - ES", "BAURU - SP", "CAMPINAS - SP", "JOINVILLE - SC", "LONDRINA - PR", "PASSO FUNDO - RS", "RIBEIRAO PRETO - SP", "UBERLANDIA - MG"]

cidadeDestinoNome = ""
cidadeDestinoDescricao = DB.ExecuteDataTable("SELECT DISTINCT id_cidade, descricao || ' - ' || id_estado AS cidadeuf FROM cidade_v WHERE id_cidade = '"+ OrdemServico["CIDADE_DESTINO"] + "'")

for cidadeDestino in cidadeDestinoDescricao.Rows:
    cidadeDestinoNome = cidadeDestino['CIDADEUF'].ToString()
    
for cidade in listaCidadesCAT:  
    if cidade.ToString() == cidadeDestinoNome.ToString() and OrdemServico["TIPO_HOSPEDAGEM"].ToString() == "Avulsa SEM apresentação de NF":
        Criticas.AdicionaPendencia("Não é permitido a abertura de solicitaçoes de hospedagens avulsas para capitais e ou cidades que possui CAT.")
        

queryAdesaoDiariaAvulaSemApresentarNF = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA Where OCORRENCIA.ASSUNTO = 'Adesão a diárias avulsas sem comprovação documental' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+OrdemServico["FAVORECIDO_DESLOCAMENTO"]+"'")

if queryAdesaoDiariaAvulaSemApresentarNF.Rows.Count == 0 and OrdemServico["TIPO_HOSPEDAGEM"] == "Avulsa SEM apresentação de NF":
    Criticas.AdicionaPendencia("Parece que seu aceite, Adesão a diárias avulsas sem comprovação documental, não foi feito. O Aceite é necessário para este tipo de solicitação.") 
    
if OrdemServico["TIPO_HOSPEDAGEM"] == "Contratada" and OrdemServico["PAHL_HOSPEDAGENS"] == False and OrdemServico.Numero == "":
    Criticas.AdicionaPendencia("Para hospedagem do tipo Contratada é obrigatório a solicitação de Reserva de Hospedagens!")
    
if OrdemServico["RETORNO_DIA"] < OrdemServico["SAIDA"] and OrdemServico.Numero == "":
    Criticas.AdicionaPendencia("A data de retorno não pode ser inferior a data de saída.")
    
horaSaida = OrdemServico["SAIDA_HORA"].Split(":")
horaRetorno = OrdemServico["RETORNO_HORA"].Split(":")

if Convert.ToInt32(horaSaida[0]) > 23 or Convert.ToInt32(horaSaida[1]) > 59:
    Criticas.AdicionaPendencia("Horário da Saída com formato inválido. Não é permitido valor superior a 23 para horas ou 59 para minutos.")
    
if Convert.ToInt32(horaRetorno[0]) > 23 or Convert.ToInt32(horaRetorno[1]) > 59:
    Criticas.AdicionaPendencia("Horário do Retorno com formato inválido. Não é permitido valor superior a 23 para horas ou 59 para minutos.")

#Trava solicitações para terceiros (Matirculas iniciadas em 99)    
matriculaString = OrdemServico["MATRICULA_DESLOCAMENTO"].ToString()
matriculaInicio = matriculaString[0]+matriculaString[1]

#if OrdemServico.Numero == "" and matriculaInicio == "99":
    #Criticas.AdicionaPendencia("Não é permitido solicitações para terceiros.")
    

teste = DB.ExecuteDataTable("SELECT P.NOME, P.USUARIO_REDE FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA WHERE P.ID_PESSOA = '"+OrdemServico['FAVORECIDO_DESLOCAMENTO'].ToString()+"' AND C.DATA_DE_DEMISSAO IS NULL")

if teste.Rows.Count > 0:
    for i in teste.Rows:
        usuario = i['USUARIO_REDE']

logins = ["ext-acarlos.farias","ext-ataide.fonseca","ext-claudio.azevedo","ext-cynthia.joca","ext-luis.anjos","ext-kenia.bueno","ext-keyla.reis","ext-naisa.amorim","ext-simone.monteiro","ext-tatiele.pereira","ext-wpereira.santos","ext-lsfernandes","ext-fazevedo.santos","ext-amilton.cabral","joao.cassino"]


if OrdemServico.Numero == "" and matriculaInicio == "99" and usuario not in logins:
    Criticas.AdicionaPendencia("Não é permitido solicitações para terceiros.")
```
**ScriptFormCarregado**
```python
Formulario["QUANTIDADE_DIARIA"].Visivel = False
Formulario["QUANTIDADE_DIARIA"].Habilitado = False
Formulario["VALOR_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False

Formulario["DIARIA_COTACAO_REAL"].Visivel = False
Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False


Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False  


Formulario["VALOR_REF_INTEGRAL"].Visivel = False
Formulario["VALOR_REF_INTEGRAL"].Habilitado = False
Formulario["VALOR_REF_REDUZIDA"].Visivel = False
Formulario["VALOR_REF_REDUZIDA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = True
Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False        
Formulario["COTACAO_DOLAR"].Visivel = False
Formulario["COTACAO_DOLAR"].Habilitado = False  


Formulario["VALOR_DISTANCIA"].Valor = "0"
Formulario["VALOR_TOTAL_REFEICAO"].Valor = "0"
Formulario["QTD_REFEICAO_REDUZIDA"].Valor = "0"




Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = "0"
Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "0"
Formulario["VALOR_DIARIA_DOLAR"].Valor = "0"
Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "0"
Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False




Formulario["CARGO_DESLOCAMENTO"].Visivel = False
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = False
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = False
Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False

    

Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False 
Formulario["VALOR_DISTANCIA"].Visivel = False
Formulario["VALOR_DISTANCIA"].Habilitado = False
#Formulario["VALOR_PASSAGEM"].Visivel = False
#Formulario["VALOR_PASSAGEM"].Habilitado = False
#Formulario["VALIDADE_PASSAGEM"].Visivel = False
#Formulario["VALIDADE_PASSAGEM"].Habilitado = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
#Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False


#Formulario["QUANTIDADE_DIARIA"].Visivel = True
#Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#Formulario["VALOR_DIARIA"].Visivel = False
#Formulario["VALOR_DIARIA"].Habilitado = False
#Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False

Formulario["CIDADE_DESTINO"].Visivel = False
Formulario["CIDADE_DESTINO"].Habilitado = False
Formulario["CIDADE_CLASSIFICACAO"].Visivel = False
Formulario["CIDADE_CLASSIFICACAO"].Habilitado = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
Formulario["PAIS"].Visivel = False
Formulario["PAIS"].Habilitado = False

#Dados das Reservas

Formulario["PAH_MOTIVO_SOL"].Visivel = False
Formulario["PAH_MOTIVO_SOL"].Habilitado = False 
Formulario["PAH_LOCALIZADORES"].Visivel = False
Formulario["PAH_LOCALIZADORES"].Habilitado = False
Formulario["PAH_VOUCHER_HOSPEDAGEM"].Visivel = False
Formulario["PAH_VOUCHER_HOSPEDAGEM"].Habilitado = False
Formulario["RESERVA_DE_VOO"].Visivel = False
Formulario["RESERVA_DE_VOO"].Habilitado = False
Formulario["PAH_DATA_ENTRADA"].Visivel = False
Formulario["PAH_DATA_ENTRADA"].Habilitado = False
Formulario["PAH_DATA_SAIDA"].Visivel = False
Formulario["PAH_DATA_SAIDA"].Habilitado = False 
Formulario["PAH_LOCALIZADORES"].Visivel = False
Formulario["PAH_LOCALIZADORES"].Habilitado = False
Formulario["PAH_EVENTO_HOTEL"].Visivel = False
Formulario["PAH_EVENTO_HOTEL"].Habilitado = False
Formulario["PAH_HOTEL_EVENTO"].Visivel = False
Formulario["PAH_HOTEL_EVENTO"].Habilitado = False
Formulario["PAHL_VOUCHER_CARRO"].Visivel = False
Formulario["PAHL_VOUCHER_CARRO"].Habilitado = False
Formulario["PAHL_LOCACOES_CARRO"].Visivel = False
Formulario["PAHL_LOCACOES_CARRO"].Habilitado = False 
##Formulario["DESCRICAO_OBRIG"].Visivel = False
##Formulario["DESCRICAO_OBRIG"].Habilitado = False
Formulario["CSC_OBS"].Visivel = False
Formulario["CSC_OBS"].Habilitado = False
Formulario["RESERVA_DE_VOO"].Visivel = False
Formulario["RESERVA_DE_VOO"].Habilitado = False
Formulario["DATA_INICIO_AUX1"].Visivel = False
Formulario["DATA_INICIO_AUX1"].Habilitado = False
Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False


Formulario["SIM_NAO"].Valor = 'Não'

Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False   
Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False  

Formulario["VIAGEM_LONGA"].Visivel = False
Formulario["VIAGEM_LONGA"].Habilitado = False 

Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False 

Formulario["LABEL1"].Visivel = False
Formulario["LABEL1"].Habilitado = False
Formulario["NUMERO_NT"].Visivel = False
Formulario["NUMERO_NT"].Habilitado = False


#LISTA DE PAÍSES

Formulario["PAIS"].Itens = "AFEGANISTÃO;ARMÊNIA;BANGLADESH;BELARUS;BENIN;BOLÍVIA;BURKINAFASSO;BUTÃO;CHILE; COMORES;REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA;COSTA RICA;EL SALVADOR; EQUADOR;ESLOVÊNIA;FILIPINAS;GÂMBIA;GUIANA;GUINÉ BISSAU;GUINÉ;HONDURAS;INDONÉSIA;IRÃ;IRAQUE;LAOS;LÍBANO;MALÁSIA;MALDIVAS; MARROCOS;MONGÓLIA;MYANMAR;NAMÍBIA;NAURU;NEPAL;NICARÁGUA;PANAMÁ;PARAGUAI; REP. CENTRO AFRICANA;REPÚBLICA TOGOLESA;SALOMÃO;SAMOA;SERRA LEOA;SÍRIA;SOMÁLIA;SRI LANKA;SURINAME;TADJIQUISTÃO;TAILÂNDIA;TIMOR LESTE;TONGA;TUNÍSIA;TURCOMENISTÃO;TURQUIA;TUVALU;VIETNÃ;ZIMBÁBUE;ÁFRICA DO SUL;ALBÂNIA;ANDORA;ARGÉLIA;ARGENTINA;AUSTRÁLIA;BELIZE;BÓSNIA-HERZEGÓVINA;BURUNDI;CABO VERDE;CAMARÕES;CAMBOJA;CATAR;CHADE;CHINA;CHIPRE;COLÔMBIA;DOMINICA;EGITO;ERITRÉIA;ESTÔNIA;ETIÓPIA;GANA;GEÓRGIA;GUINÉ EQUATORIAL;HAITI;HUNGRIA;IEMEN;ILHAS MARSHALL;ÍNDIA;KIRIBATI;LESOTO;LÍBIA;MACEDÔNIA;MADAGASCAR;MALAUÍ;MICRONÉSIA;MOÇAMBIQUE;MOLDÁVIA;NÍGER;NIGÉRIA;NOVA ZELÂNDIA;PALAU;PAPUA NOVAGUINÉ;PAQUISTÃO;PERU;POLÔNIA;QUÊNIA;REPÚBLICA DOMINICANA;ROMÊNIA;RUANDA;SÃO TOMÉ E PRÍNCIPE;SENEGAL; SUDÃO;TANZÂNIA;URUGUAI;UZBEQUISTÃO;VENEZUELA;ANTÍGUA E BARBUDA;ARÁBIA SAUDITA;AZERBAIDJÃO;BAHAMAS;BAREINE;BOTSUANA;BRUNEI DARUSSALAM;BULGÁRIA;CANADÁ;CINGAPURA;CONGO;COSTA DO MARFIM;CUBA;DJIBUTI;EMIRADOS ÁRABES;FIJI;GABÃO;GUATEMALA;JAMAICA;JORDÂNIA;LETÔNIA;LIBÉRIA;LITUÂNIA;MALI;MALTA;MAURÍCIO;MAURITÂNIA;MÉXICO;REPÚBLICA DEMOCRÁTICA DO CONGO;REPÚBLICA TCHECA;RÚSSIA;SAN MARINO;SANTA LÚCIA;SÃO CRISTOVÃO E NÉVIS;SÃO VICENTE EGRANADINAS;TAIWAN;TRINIDAD E TOBAGO;UCRÂNIA;UGANDA;ZÂMBIA;ALEMANHA;ANGOLA;ÁUSTRIA;BARBADOS;BÉLGICA;CAZAQUISTÃO;CORÉIA DOSUL;CROÁCIA;DINAMARCA;ESPANHA;ESTADOS UNIDOS DA AMÉRICA;FINLÂNDIA;FRANÇA;GRANADA;GRÉCIA;HONG KONG;IRLANDA;ISLÂNDIA;ISRAEL;ITÁLIA;JAPÃO;KUAITE;LIECHTENSTEIN;LUXEMBURGO;MÔNACO;MONTENEGRO;NORUEGA;OMÃ;PEÍSES BAIXOS;PORTUGAL;REINO UNIDO;REPÚBLICA QUIRGUIZ;SEICHELES;SÉRVIA SUAZILÂNDIA;SUÉCIA;SUÍÇA;VANUATU"
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Solicitação de Reservas
  - PAH_HOTEL_EVENTO "Hotel do Evento" [TextBox String → CPE_CSC.PAH_HOTEL_EVENTO] obrigatório
  - PAH_DATA_SAIDA "Data de Saída do Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA] obrigatório
**PAH_DATA_SAIDA.ScriptModificado**
```python
if Formulario["PAH_DATA_SAIDA"].Valor <= Formulario["PAH_DATA_ENTRADA"].Valor:
   Formulario.ExibeMensagem("'Data de Saída do Hotel' deve ser maior que 'Data de Entrada no Hotel'!")
   Formulario["PAH_DATA_SAIDA"].Valor = None
```
  - PAH_EVENTO_HOTEL "Evento no Hotel?" [DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL] obrigatório
**PAH_EVENTO_HOTEL.ScriptModificado**
```python
Formulario["PAH_HOTEL_EVENTO"].Visivel = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
Formulario["PAH_HOTEL_EVENTO"].Habilitado = Formulario["PAH_EVENTO_HOTEL"].Valor == "Sim"
```
  - PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO]
  - PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO]
**PAHL_LOCACOES_CARRO.ScriptConfirmado**
```python
if Registro["DATA_HORA_DEVOLUCAO"] < Registro["DATA_HORA_RETIRADA"]:
   Formulario.ExibeMensagem("ATENÇÃO: Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
```
    - coluna DATA_HORA_DEVOLUCAO obrigatório
**PAHL_LOCACOES_CARRO.DATA_HORA_DEVOLUCAO.ScriptModificado**
```python
#if FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor < FormularioRegistro["DATA_HORA_RETIRADA"].Valor:
#   Formulario.ExibeMensagem("Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
#   FormularioRegistro["DATA_HORA_DEVOLUCAO"].Valor = None
```
    - coluna CPF_FAVORECIDO obrigatório
    - coluna LOCAL_RETIRADA obrigatório
    - coluna VALOR_LOCACAO
    - coluna CELULAR_FAVORECIDO obrigatório
    - coluna CARRO4X4 obrigatório
    - coluna DATA_HORA_RETIRADA obrigatório
    - coluna LOCAL_DEVOLUCAO obrigatório
  - CSC_OBS "Endereço do Local do Evento/Atendimento e outras observações (Informe até 2 sugestões de hotel, se houver)" [Memo String(2000) → CPE_CSC.CSC_OBS]
  - DATA_INICIO_AUX1 "Data Início da Viagem" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1]
  - PAH_DATA_ENTRADA "Data de Entrada no Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA] obrigatório
  - PAH_MOTIVO_SOL "Motivo da Solicitação" [DropDownList String → CPE_CSC.PAH_MOTIVO_SOL] obrigatório
  - PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES]
    - coluna VALOR_TRECHO
    - coluna CIA_AEREA obrigatório
    - coluna LOCALIZADOR obrigatório
    - coluna SEQUENCIA obrigatório
  - PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM]
  - RESERVA_DE_VOO "Informações da Reserva de Voo - Nacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO]
    - coluna DESPACHO_BAGAGENS obrigatório
**RESERVA_DE_VOO.DESPACHO_BAGAGENS.ScriptModificado**
```python
#Sim;Não
FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = None
FormularioRegistro["QUANTIDADE_BAGAGENS"].Habilitado = FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Sim"

if FormularioRegistro["DESPACHO_BAGAGENS"].Valor == "Não":
   FormularioRegistro["QUANTIDADE_BAGAGENS"].Valor = 0
```
    - coluna AEROPORTO_ORIGEM obrigatório
    - coluna UF_DESTINO obrigatório
    - coluna DATA_VOO obrigatório
    - coluna CIDADE_DESTINO obrigatório
    - coluna ALT_OU_EXC
    - coluna SEQUENCIA obrigatório
**RESERVA_DE_VOO.SEQUENCIA.ScriptModificado**
```python
rv = OrdemServico["RESERVA_DE_VOO"]

for seq in rv.Rows:
    if FormularioRegistro["SEQUENCIA"].Valor == seq["SEQUENCIA"]:
       Formulario.ExibeMensagem("A T E N Ç Ã O !!! \n Nº do Trecho já lançado!")
       FormularioRegistro["SEQUENCIA"].Valor = None
```
    - coluna ALT_EXC obrigatório
    - coluna QUANTIDADE_BAGAGENS obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna HORA_ESTIMADA_VOO obrigatório
    - coluna UF_ORIGEM obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna TRECHO obrigatório
  - RESERVA_DE_VOO_INTERNACIONAL "Informações para Reserva de Voo - Internacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL]
    - coluna CIDADE_DESTINO obrigatório
    - coluna AEROPORTO_DESTINO obrigatório
    - coluna DATA_VOO obrigatório
    - coluna HORA_ESTIMADA_VOO obrigatório
    - coluna DESPACHO_BAGAGENS obrigatório
    - coluna QUANTIDADE_BAGAGENS obrigatório
    - coluna SEQUENCIA obrigatório
    - coluna TRECHO obrigatório
    - coluna CIDADE_ORIGEM obrigatório
    - coluna AEROPORTO_ORIGEM obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexos" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Opções de Reserva
  - PAHL_PASSAGENS "Reserva de Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS] obrigatório
**PAHL_PASSAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#camposVisiveis = None
#camposHabilitados = None
#vis = False
#hab = False
#
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
#if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
#   # lista de campos a serem alteradas a visibilidade.
#   camposVisiveis = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["RESERVA_DE_VOO", "DESCRICAO_OBRIG", "CSC_OBS"]
#   camposVisiveis = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   camposHabilitados = ["DESCRICAO_OBRIG", "CSC_OBS"]
#   if Formulario["PAHL_PASSAGENS"].Valor == True:
#      vis = True
#      hab = True
#    
#
#   for controle in Formulario.Controles:
#       # preserva a visibilidade atual dos campos
#       visivel = Formulario[controle.Key].Visivel
#       habilitado = Formulario[controle.Key].Habilitado
#       valor = Formulario[controle.Key].Valor
#       for campo in camposVisiveis:
#           if controle.Key == campo:
#              visivel = vis
#              valor = None
#              break
#       Formulario[controle.Key].Visivel = visivel
#       
#       for campo in camposHabilitados:
#           if controle.Key == campo:
#              habilitado = hab
#              break
#       Formulario[controle.Key].Habilitado = habilitado
#       Formulario[controle.Key].Valor = valor
#       
#   cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]

if (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = True
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = True
    Formulario["RESERVA_DE_VOO"].Visivel = False
    Formulario["RESERVA_DE_VOO"].Habilitado = False
    #Formulario["DESCRICAO_OBRIG"].Visivel = True
    #Formulario["DESCRICAO_OBRIG"].Habilitado = True
    Formulario["CSC_OBS"].Visivel = True
    Formulario["CSC_OBS"].Habilitado = True
elif (Formulario["PAHL_PASSAGENS"].Valor == True) and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
    Formulario["RESERVA_DE_VOO"].Visivel = True
    Formulario["RESERVA_DE_VOO"].Habilitado = True    
    #Formulario["DESCRICAO_OBRIG"].Visivel = True
    #Formulario["DESCRICAO_OBRIG"].Habilitado = True
    Formulario["CSC_OBS"].Visivel = True
    Formulario["CSC_OBS"].Habilitado = True
else:
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Visivel = False
    Formulario["RESERVA_DE_VOO_INTERNACIONAL"].Habilitado = False
    Formulario["RESERVA_DE_VOO"].Visivel = False
    Formulario["RESERVA_DE_VOO"].Habilitado = False    
   # Formulario["DESCRICAO_OBRIG"].Visivel = False
   # Formulario["DESCRICAO_OBRIG"].Habilitado = False
    Formulario["CSC_OBS"].Visivel = False
    Formulario["CSC_OBS"].Habilitado = False
```
  - PAHL_HOSPEDAGENS "Reserva de Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS] obrigatório
**PAHL_HOSPEDAGENS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
camposVisiveis = None
camposHabilitados = None
vis = False
hab = False

pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
   # lista de campos a serem alteradas a visibilidade.
   camposVisiveis = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL","CSC_OBS"]
   camposHabilitados = ["PAH_DATA_ENTRADA", "PAH_DATA_SAIDA", "PAH_EVENTO_HOTEL","CSC_OBS"]
   if Formulario["PAHL_HOSPEDAGENS"].Valor == True:
      vis = True
      hab = True
   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado
       valor = Formulario[controle.Key].Valor
       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = vis
              valor = None
              break
       Formulario[controle.Key].Visivel = visivel
       
       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = hab
              break
       Formulario[controle.Key].Habilitado = habilitado
       Formulario[controle.Key].Valor = valor
```
  - PAHL_LOCACOES "Locações de Carro" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES] obrigatório
**PAHL_LOCACOES.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
camposVisiveis = None
camposHabilitados = None
vis = False
hab = False

pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
if OrdemServico.Servico.Sigla == "DESLOCAMENTO":
   # lista de campos a serem alteradas a visibilidade.
   camposVisiveis = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
   camposHabilitados = ["PAHL_LOCACOES_CARRO", "CSC_OBS"]
   if Formulario["PAHL_LOCACOES"].Valor == True:
      vis = True
      hab = True

   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado
       valor = Formulario[controle.Key].Valor
       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = vis
              valor = None
              break
       Formulario[controle.Key].Visivel = visivel
       
       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = hab
              break
       Formulario[controle.Key].Habilitado = habilitado
       Formulario[controle.Key].Valor = valor
       
   #Formulario["PAH_MOTIVO_SOL"].Visivel = False
   
   #cargos = ["TECNICO", "TECNICO DE OPERACOES", "TECNICO ESPECIALISTA"]
   
   #if (Formulario["PAHL_PASSAGENS"].Valor == True or Formulario["PAHL_HOSPEDAGENS"].Valor == True or Formulario["PAHL_LOCACOES"].Valor == True) and cargos.Contains(pessoa["CARGO_FUNCIONAL"]):
   Formulario["PAH_MOTIVO_SOL"].Visivel = True
   Formulario["PAH_MOTIVO_SOL"].Habilitado = True
   #else:
   #   Formulario["PAH_MOTIVO_SOL"].Visivel = False
   #   Formulario["PAH_MOTIVO_SOL"].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Informações do Deslocamento
  - VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR] obrigatório
**VALOR_DIARIA_DOLAR.ScriptModificado**
```python
if Convert.ToDecimal(Formulario["VALOR_DIARIA_DOLAR"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DOLAR"].Valor):
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["CAMPO_VALIDACAO_DOLAR"].Valor
else:
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor = Formulario["VALOR_DIARIA_DOLAR"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True

valorTotal1 = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Valor)

valorTotal1 = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal1 


#OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal1
```
  - CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR] obrigatório — Coluna=2
  - QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA] obrigatório
**QUANTIDADE_DIARIA.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import OutputSubProcesso
def calculaDiaria():
    ############### SE O FAVORECIDO FOR DO GRUPO C MAS ESTARÁ ACOMPANHANDO O GRUPO B RECEBE O VALOR DO GRUPO B 
    
    if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    elif Formulario["SIM_NAO"].Valor == "Sim" :
          if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 
                 Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                
          elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO E BRASILIA
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
            
          elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
              Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
          else: 
            Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
      
    else:     
            
        ############## SE FOR DO GRUPO A -  PRESIDENTE / DIRETOR / CONSELHEIRO NÃO TEM LIMITE   
        if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE":
            Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
            
            
            
        ############## SE O FAVORECIDO FOR DO GRUPO B  ELE RECEBE REFERENTE A CIDADE     
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "SUPERINTENDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "SUPERINTENDENTE":
            if Formulario["CIDADE_DESTINO"].Valor == "3550308 ": # SAO PAULO 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "650"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO OutputSubProcesso BRASILIA
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550"
                    
            elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                      Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450" 
            else:
                Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                  
                  
        ############## DEMAIS CARGOS
        elif Formulario["FUNCAO_DESLOCAMENTO"].Valor != "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE DE PROJETOS I" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor != "SUPERINTENDENTE":
              
              if Formulario["CIDADE_DESTINO"].Valor == "3550308": # SAO PAULO 3550308 
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "550" 
                    
              elif Formulario["CIDADE_DESTINO"].Valor == "5300108" or Formulario["CIDADE_DESTINO"].Valor == "3304557": #RIO DE JANEIRO ou BRASILIA
                        Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "450"
                        
              elif Formulario["CIDADE_DESTINO"].Valor == "1501402" or Formulario["CIDADE_DESTINO"].Valor == "3106200" or Formulario["CIDADE_DESTINO"].Valor == "2303501" or      Formulario["CIDADE_DESTINO"].Valor == "2304400" or Formulario["CIDADE_DESTINO"].Valor == "5208707" or Formulario["CIDADE_DESTINO"].Valor == "3543402":
                          Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "370" 
                          
              else:
                    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = "350"
                  

              
              
calculaDiaria()
     
############ VALOR FINAL DO ADIANTAMENTO EM DIARIAS      
diasViagem = Convert.ToInt32(Formulario["DIAS_DE_TRA"].Valor)
diasHospedagem = Convert.ToInt32(Formulario["QUANTIDADE_DIARIA"].Valor)



if diasHospedagem > diasViagem:
    mensagem = "Quantidade de Diária Excedida! Máximo Permitido: " + Formulario["DIAS_DE_TRA"].Valor + " Verifique a saída e o retorno"
    Formulario.ExibeMensagem(mensagem)      
    Formulario["VALOR_DIARIA"].Habilitado = False
else:
    Formulario["VALOR_DIARIA"].Habilitado = True   


#Valor parcela complementar    



if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":

    Formulario["PARCELA_COMPLEMENTAR"].Valor = "0"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0"
   
else:    
    Formulario["PARCELA_COMPLEMENTAR"].Valor = "19,74"
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = True
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False    
    
    pc = Formulario["PARCELA_COMPLEMENTAR"].Valor 
    qtd = Formulario["QUANTIDADE_DIARIA"].Valor
    total = 0

    total = pc * qtd
    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = total
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = True


#Define o valor para hospedagem do tipo avulsa
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "A":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 230.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 230.00
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "B":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 250.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 250.00

if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" and Formulario["CIDADE_CLASSIFICACAO"].Valor == "C":
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 270.00
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 270.00  
    

#if (Formulario["TIPO_DESTINO"].Valor == "Interior") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "350"
#    
#if (Formulario["TIPO_DESTINO"].Valor == "Capital") and (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa"):
#    Formulario["VALOR_DIARIA"].Valor = "500"
#
#import System.Text
#daysOffText = System.Text.StringBuilder()
#
# #RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C  inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#   
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            return True
#    return False
#   
#def workingDays(totalDays, firstDate):
#    
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#saida = Formulario["SAIDA"].Valor
#retorno  = Formulario["RETORNO_DIA"].Valor
#
#totalDias = (retorno - saida).TotalDays  
#count = 0
#
#totalDiasUteis = workingDays(totalDias,saida) 
#totalDiasNaoUteis = totalDias - totalDiasUteis
#
############### almoço e janta de ambos os dias
#quantReduzida = totalDiasUteis  
#quantIntegral = (totalDiasNaoUteis * 2) + totalDiasUteis
#
#
#

#Formulario["QTD_REFEICAO_REDUZIDA"].Valor = totalDiasUteis 
#Formulario["QTD_REFEICAO_INTEGRAL"].Valor = totalDiasNaoUteis
#
#
#Formulario["VALOR_REF_REDUZIDA"].Valor = totalDiasUteis * 18.39
#Formulario["VALOR_REF_INTEGRAL"].Valor = totalDiasNaoUteis *  64.36
#
#
#OrdemServico.AdicionaComentario("WorkingDays "+totalWorkingDays.ToString(),False)
#OrdemServico.AdicionaComentario(daysOffText.ToString(),False )

#OrdemServico["totalWorkingDays"] = totalWorkingDays
```
  - DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL] — Coluna=3
  - LABEL1 "Cotação do Dólar Americano Conforme Aprovado na NT" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A] obrigatório
**ACOMPANHANDO_GRUPO_A.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#    Formulario["SIM_NAO"].Visivel = False
#    Formulario["SIM_NAO"].Habilitado = False 
  

else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False 
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["SIM_NAO"].Habilitado = True
     
    
    
#    
#if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Não":
#    Formulario["SIM_NAO"].Visivel = True
#    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True 
#    Formulario["NUM_ABERTURA_CHAMADO"].Habilitado = True 
#
#else:
#     Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
#
```
  - CELULAR "Celular do Favorecido" [TextBox String → CP_ORDEM_SERVICO.CELULAR] — Configuracao={"Mascara":"00000000000"}
  - DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO] obrigatório
  - TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO] obrigatório
**TIPO_DESLOCAMENTO.ScriptModificado**
```python
if Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
    Formulario["COTACAO_DOLAR"].Visivel = True
    Formulario["COTACAO_DOLAR"].Habilitado = True  
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = True
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = True
    Formulario["PAIS"].Visivel = True
    Formulario["PAIS"].Habilitado = True       
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["TIPO_HOSPEDAGEM"].Visivel = True
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = False    
    Formulario["TIPO_HOSPEDAGEM"].Valor = "Avulsa"
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True    
    
    Formulario["CIDADE_DESTINO"].Visivel = False
    Formulario["CIDADE_DESTINO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["DIARIA_COTACAO_REAL"].Visivel = True
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL1"].Habilitado = True
    Formulario["NUMERO_NT"].Visivel =  True
    Formulario["NUMERO_NT"].Habilitado = True
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False  
    Formulario["SIM_NAO_REFEICAO"].Habilitado = False
    Formulario["SIM_NAO_REFEICAO"].Valor = "Não"
    
else:
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["COTACAO_DOLAR"].Visivel = False
    Formulario["COTACAO_DOLAR"].Habilitado = False   
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Visivel = False
    Formulario["CIDADE_DESTINO_INTERNACIONAL"].Habilitado = False
    Formulario["PAIS"].Visivel = False
    Formulario["PAIS"].Habilitado = False  
    Formulario["TIPO_HOSPEDAGEM"].Habilitado = True
    
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_DESTINO"].Visivel = True
    Formulario["CIDADE_DESTINO"].Habilitado = True
    Formulario["CIDADE_CLASSIFICACAO"].Visivel = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True
    Formulario["DIARIA_COTACAO_REAL"].Visivel = False
    Formulario["DIARIA_COTACAO_REAL"].Habilitado = False
    Formulario["SIM_NAO_REFEICAO"].Habilitado = True
    
    
    Formulario["LABEL1"].Visivel =  False
    Formulario["LABEL1"].Habilitado = False
    Formulario["NUMERO_NT"].Visivel =  False
    Formulario["NUMERO_NT"].Habilitado = False
```
  - TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR] obrigatório
  - LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE] obrigatório
  - MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO] obrigatório
**MEIO_LOCOMOCAO.ScriptModificado**
```python
if Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio":
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = True
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = True
    Formulario["VALOR_DISTANCIA"].Visivel = True
    Formulario["VALOR_DISTANCIA"].Habilitado = True
else:
    Formulario["PREVISAO_DISTANCIA_KM"].Visivel = False
    Formulario["PREVISAO_DISTANCIA_KM"].Habilitado = False
    Formulario["VALOR_DISTANCIA"].Visivel = False
    Formulario["VALOR_DISTANCIA"].Habilitado = False
    
if (Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Próprio" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro Locado" or Formulario["MEIO_LOCOMOCAO"].Valor == "Carro da Frota" or Formulario["MEIO_LOCOMOCAO"].Valor == "Barco") and Formulario ["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica":
    Formulario["VIAGEM_LONGA"].Visivel = True
    Formulario["VIAGEM_LONGA"].Habilitado = True
else:
    Formulario["VIAGEM_LONGA"].Visivel = False
    Formulario["VIAGEM_LONGA"].Habilitado = False 
    
    
    
##if Formulario["MEIO_LOCOMOCAO"].Valor == "Avião" or Formulario["MEIO_LOCOMOCAO"] == "Ônibus Interestadual":
##    Formulario["VALOR_PASSAGEM"].Visivel = True
##    Formulario["VALOR_PASSAGEM"].Habilitado = True
##    Formulario["VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = True
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = True
##else:
##    Formulario["VALOR_PASSAGEM"].Visivel = False
##    Formulario["VALOR_PASSAGEM"].Habilitado = False
##    Formulario["VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["VALIDADE_PASSAGEM"].Habilitado = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Visivel = False
##    Formulario["HORA_VALIDADE_PASSAGEM"].Habilitado = False    
#    
    






##finais de semana um almoço e janta integral
##dias de semana uma refeição reduzida e uma integral
############# calculo dias
#import clr 
#import datetime
#import System.Text
# 
#
#
#zero = 0
#valorRefIntegral = 64.36
#valorRefReduzida = 18.39
#
#
#
#daysOffText = System.Text.StringBuilder()
#
#
###RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
#def isHoliday(day):
#    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
#    #feriados = 0
#    
#    for holiday in holidays.Rows:
#        if day == holiday["DATA"].Date:
#            #feriados += 2
#            return True
#    return False
#
#
#def countHolidays(firstDate, lastDate):
#    totalHolidays = 0
#    currentDay = firstDate
#
#    while currentDay <= lastDate:
#        if isHoliday(currentDay):
#            totalHolidays += 1
#        currentDay = currentDay.AddDays(1)
#
#    return totalHolidays
#
#    
#def workingDays(totalDays, firstDate):
#
#    totalWorkingDays = 0
#    totalDaysOff = 0
#    count = 0
#
#   
#    while count <= totalDays:
#        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
#        day = firstDate.Date.AddDays(count)
#        
#        
#        
#        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
#            totalDaysOff = totalDaysOff + 1
#            daysOffText.AppendLine(" dayOff: "+str(day))
#        
#        count = count + 1
#        totalWorkingDays = totalWorkingDays + 1
#    return totalWorkingDays - totalDaysOff
#   
#
#
#    
#def countSaturdays(firstDate, lastDate):
#    saturdays = 0
#    currentDay = firstDate
#    
#    while currentDay <= lastDate:
#        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
#            saturdays += 2
#        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
#    
#    return saturdays
#
#    
#firstDate = Formulario["SAIDA"].Valor
#lastDate = Formulario["RETORNO_DIA"].Valor
#
#totalDays = (lastDate - firstDate).TotalDays
#count = 0
#
#
#
#
#
#totalWorkingDays = workingDays(totalDays,firstDate)
#holidaysCount = countHolidays(firstDate, lastDate)
#saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2
#
#
##Quantidade de refeições Reduzias e integrais
#quantRed = totalWorkingDays
#quantInt = saturdays + totalWorkingDays 
#
#
#
#
#
#
##Atribuindo valor a variável
#saidaHora = Formulario["SAIDA_HORA"].Valor 
#retornoHora = Formulario["RETORNO_HORA"].Valor 
#
##Split de horário, separando hora de minuto
#hora = saidaHora.Split(':');     
#horaRetorno = retornoHora.Split(':');
#
##Atribuindo valor de horário e minuto de acordo com o índice da variável
#horarioSaida = hora[0]
#minutoSaida = hora[1]
#
#horarioRetorno = horaRetorno[0] 
#minutoRetorno = horaRetorno[1]
#
#
#
##SAIDA DIAS ÚTEIS
#
#
##1 maior q o 2
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
##    quantRed = quantRed - 1
##   
##if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
##    quantInt = quantInt - 1
##   
##RETORNO DIAS ÚTEIS
##1 menor q o 2   
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
##    quantRed = quantRed - 1
##    quantInt = quantInt - 1
##    
##if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
##    quantInt = quantInt - 1
##    #teste abaixo
##    quantRed = quantRed - 1
#
#
#
#
#
##DIAS UTEIS
#
#if workingDays(0,firstDate):
#    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if workingDays(0,lastDate):    
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantRed = quantRed - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
##Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
################################################################
#    
##SAÍDA FINAIS DE SEMANA E/OU FERIADOS
#
#if not  workingDays(0,firstDate):
#    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
#        quantInt = quantInt - 1
#if not  workingDays(0,lastDate):
#    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1
#    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
#        quantInt = quantInt - 1   
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
#  
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
#    
#else:
#    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
#    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
#    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
#    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
#    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
#    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
#    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
#    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
#  
#    
#if quantRed > (totalWorkingDays):
#    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
#    Formulario.ExibeMensagem(mensagem)    
#    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
#    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
#    
#
############## calculo valor total
#
#refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
#refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
#valorTotalRefeicoes = refIntegral + refReduzida
#Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
#Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
#Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
#
#
#
#
#
#
```
  - VIAGEM_LONGA "Distância da Viagem de Carro (Programa Valor)" [DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA] obrigatório
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS] obrigatório — Coluna=3
**PAIS.ScriptModificado**
```python
  
        ################## grupo A
if Formulario["PAIS"].Valor == "AFEGANISTÃO" or Formulario["PAIS"].Valor == "ARMÊNIA" or Formulario["PAIS"].Valor == "BANGLADESH" or Formulario["PAIS"].Valor == "BELARUS" or Formulario["PAIS"].Valor == "BENIN" or Formulario["PAIS"].Valor == "BOLÍVIA" or Formulario["PAIS"].Valor == "BURKINAFASSO" or Formulario["PAIS"].Valor == "BUTÃO"  or Formulario["PAIS"].Valor == "CHILE" or Formulario["PAIS"].Valor == "COMORES" or Formulario["PAIS"].Valor == "REPÚBLICA POPULAR DEMOCRÁTICA DA CORÉIA" or Formulario["PAIS"].Valor == "COSTA RICA" or Formulario["PAIS"].Valor == "EL SALVADOR" or Formulario["PAIS"].Valor == "EQUADOR" or Formulario["PAIS"].Valor == "ESLOVÊNIA" or Formulario["PAIS"].Valor == "FILIPINAS" or Formulario["PAIS"].Valor == "GÂMBIA" or Formulario["PAIS"].Valor == "GUIANA" or Formulario["PAIS"].Valor == "GUINÉ BISSAU" or Formulario["PAIS"].Valor == "GUINÉ" or Formulario["PAIS"].Valor == "HONDURAS" or Formulario["PAIS"].Valor == "INDONÉSIA" or Formulario["PAIS"].Valor == "IRÃ" or Formulario["PAIS"].Valor == "IRAQUE" or Formulario["PAIS"].Valor == "LAOS" or Formulario["PAIS"].Valor == "LÍBANO" or Formulario["PAIS"].Valor == "MALÁSIA" or Formulario["PAIS"].Valor == "MALDIVAS" or Formulario["PAIS"].Valor == "MARROCOS" or Formulario["PAIS"].Valor == "MONGÓLIA" or Formulario["PAIS"].Valor == "NAMÍBIA" or Formulario["PAIS"].Valor == "MYANMAR" or Formulario["PAIS"].Valor == "NAURU" or Formulario["PAIS"].Valor == "NEPAL"or Formulario["PAIS"].Valor == "NICARÁGUA" or Formulario["PAIS"].Valor == "PANAMÁ" or Formulario["PAIS"].Valor == "PARAGUAI" or Formulario["PAIS"].Valor == " REP. CENTRO AFRICANA" or Formulario["PAIS"].Valor == "REPÚBLICA TOGOLESA" or Formulario["PAIS"].Valor == "SALOMÃO" or Formulario["PAIS"].Valor == "SAMOA" or Formulario["PAIS"].Valor == "SERRA LEOA" or Formulario["PAIS"].Valor == "SÍRIA" or Formulario["PAIS"].Valor == "SOMÁLIA" or Formulario["PAIS"].Valor == "SRI LANKA" or Formulario["PAIS"].Valor == "TURQUIA" or Formulario["PAIS"].Valor == "TADJIQUISTÃO" or Formulario["PAIS"].Valor == "TAILÂNDIA" or Formulario["PAIS"].Valor == "TIMOR LESTE" or Formulario["PAIS"].Valor == "TONGA" or Formulario["PAIS"].Valor == "TUNÍSIA" or Formulario["PAIS"].Valor == "TURCOMENISTÃO" or Formulario["PAIS"].Valor == "TUVALU" or Formulario["PAIS"].Valor == "VIETNÃ" or Formulario["PAIS"].Valor == "ZIMBÁBUE":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "220"
                        
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "200"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "190"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "180"
          
    else:
          Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "170"
            
        ###################### grupo B    
            
elif Formulario["PAIS"].Valor == "ÁFRICA DO SUL" or Formulario["PAIS"].Valor == "ALBÂNIA" or Formulario["PAIS"].Valor == "ANDORA" or Formulario["PAIS"].Valor == "ARGÉLIA" or Formulario["PAIS"].Valor == "ARGENTINA" or Formulario["PAIS"].Valor == "AUSTRÁLIA" or Formulario["PAIS"].Valor == "BELIZE" or Formulario["PAIS"].Valor == "BÓSNIA-HERZEGÓVINA"  or Formulario["PAIS"].Valor == "BURUNDI" or Formulario["PAIS"].Valor == " CABO VERDE" or Formulario["PAIS"].Valor == "CAMARÕES" or Formulario["PAIS"].Valor == "CAMBOJA" or Formulario["PAIS"].Valor == "CATAR" or Formulario["PAIS"].Valor == "CHADE" or Formulario["PAIS"].Valor == "CHINA" or Formulario["PAIS"].Valor == "CHIPRE" or Formulario["PAIS"].Valor == "COLÔMBIA" or Formulario["PAIS"].Valor == "DOMINICA" or Formulario["PAIS"].Valor == "EGITO" or Formulario["PAIS"].Valor == "ERITRÉIA" or Formulario["PAIS"].Valor == "ESTÔNIA" or Formulario["PAIS"].Valor == "ETIÓPIA" or Formulario["PAIS"].Valor == "GANA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "HUNGRIA" or Formulario["PAIS"].Valor == "IEMEN" or Formulario["PAIS"].Valor == " ILHAS MARSHALL" or Formulario["PAIS"].Valor == "ÍNDIA" or Formulario["PAIS"].Valor == "KIRIBATI" or Formulario["PAIS"].Valor == "LESOTO" or Formulario["PAIS"].Valor == "LÍBIA" or Formulario["PAIS"].Valor == "MACEDÔNIA"or Formulario["PAIS"].Valor == "MADAGASCAR" or Formulario["PAIS"].Valor == "MALAUÍ" or Formulario["PAIS"].Valor == "MICRONÉSIA" or Formulario["PAIS"].Valor == "MOÇAMBIQUE" or Formulario["PAIS"].Valor == "MOLDÁVIA" or Formulario["PAIS"].Valor == "NÍGER" or Formulario["PAIS"].Valor == "NIGÉRIA" or Formulario["PAIS"].Valor == "NOVA ZELÂNDIA" or Formulario["PAIS"].Valor == "PALAU" or Formulario["PAIS"].Valor == "PAPUA NOVA GUINÉ" or Formulario["PAIS"].Valor == "PAQUISTÃO" or Formulario["PAIS"].Valor == "PERU" or Formulario["PAIS"].Valor == "POLÔNIA" or Formulario["PAIS"].Valor == "QUÊNIA" or Formulario["PAIS"].Valor == "REPÚBLICA DOMINICANA" or Formulario["PAIS"].Valor == "ROMÊNIA" or Formulario["PAIS"].Valor == "RUANDA" or Formulario["PAIS"].Valor == " SÃO TOMÉ E PRÍNCIPE" or Formulario["PAIS"].Valor == "SENEGAL" or Formulario["PAIS"].Valor == "TANZÂNIA" or Formulario["PAIS"].Valor == "SUDÃO"  or Formulario["PAIS"].Valor == "URUGUAI" or Formulario["PAIS"].Valor == "UZBEQUISTÃO" or Formulario["PAIS"].Valor == "VENEZUELA":

    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "280"

    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "270"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "260"
        
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "250"
                    
                    

            ################### grupo C

            
elif Formulario["PAIS"].Valor == "ANTÍGUA E BARBUDA" or Formulario["PAIS"].Valor == "ARÁBIA SAUDITA" or Formulario["PAIS"].Valor == "AZERBAIDJÃO" or Formulario["PAIS"].Valor == "BAHAMAS" or Formulario["PAIS"].Valor == "BAREINE" or Formulario["PAIS"].Valor == "BOTSUANA" or Formulario["PAIS"].Valor == "BRUNEI DARUSSALAM" or Formulario["PAIS"].Valor == "BULGÁRIA"  or Formulario["PAIS"].Valor == "CANADÁ" or Formulario["PAIS"].Valor == "CINGAPURA" or Formulario["PAIS"].Valor == "CONGO" or Formulario["PAIS"].Valor == "COSTA DO MARFIM" or Formulario["PAIS"].Valor == "CUBA" or Formulario["PAIS"].Valor == "DJIBUTI" or Formulario["PAIS"].Valor == "EMIRADOS ÁRABES" or Formulario["PAIS"].Valor == "FIJI" or Formulario["PAIS"].Valor == "GABÃO" or Formulario["PAIS"].Valor == "GUATEMALA" or Formulario["PAIS"].Valor == "REPÚBLICA DEMOCRÁTICA DO CONGO" or Formulario["PAIS"].Valor == "JAMAICA" or Formulario["PAIS"].Valor == "JORDÂNIA" or Formulario["PAIS"].Valor == "LETÔNIA" or Formulario["PAIS"].Valor == "LIBÉRIA" or Formulario["PAIS"].Valor == "GEÓRGIA" or Formulario["PAIS"].Valor == "GUINÉ EQUATORIAL" or Formulario["PAIS"].Valor == "HAITI" or Formulario["PAIS"].Valor == "MAURÍCIO" or Formulario["PAIS"].Valor == "MAURITÂNIA" or Formulario["PAIS"].Valor == "MÉXICO" or Formulario["PAIS"].Valor == "MALTA" or Formulario["PAIS"].Valor == " REPÚBLICA TCHECA" or Formulario["PAIS"].Valor == "RÚSSIA" or Formulario["PAIS"].Valor == "SAN MARINO" or Formulario["PAIS"].Valor == "SANTA LÚCIA"or Formulario["PAIS"].Valor == "SÃO CRISTOVÃO E NÉVIS" or Formulario["PAIS"].Valor == "SÃO VICENTE E GRANADINAS" or Formulario["PAIS"].Valor == "TAIWAN" or Formulario["PAIS"].Valor == "TRINIDAD E TOBAGO" or Formulario["PAIS"].Valor == "UCRÂNIA" or Formulario["PAIS"].Valor == "UGANDA" or Formulario["PAIS"].Valor == "ZÂMBIA":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "330"
                    
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "320"
                
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "310"
    
    else:
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "300"     
                    
                
            #################### grupo D 
if Formulario["PAIS"].Valor == "ALEMANHA" or Formulario["PAIS"].Valor == "ANGOLA" or Formulario["PAIS"].Valor == "ÁUSTRIA" or Formulario["PAIS"].Valor == "BARBADOS" or Formulario["PAIS"].Valor == "BÉLGICA"or Formulario["PAIS"].Valor == "CAZAQUISTÃO" or Formulario["PAIS"].Valor == "CORÉIA DO SUL" or Formulario["PAIS"].Valor == "CROÁCIA"  or Formulario["PAIS"].Valor == "DINAMARCA" or Formulario["PAIS"].Valor == "ESPANHA" or Formulario["PAIS"].Valor == "ESTADOS UNIDOS DA AMÉRICA" or Formulario["PAIS"].Valor == "FINLÂNDIA" or Formulario["PAIS"].Valor == "FRANÇA" or Formulario["PAIS"].Valor == "GRANADA" or Formulario["PAIS"].Valor == "GRÉCIA HONG KONG" or Formulario["PAIS"].Valor == "IRLANDA" or Formulario["PAIS"].Valor == "ISLÂNDIA" or Formulario["PAIS"].Valor == "ISRAEL" or Formulario["PAIS"].Valor == "ITÁLIA" or Formulario["PAIS"].Valor == "JAPÃO" or Formulario["PAIS"].Valor == "KUAITE" or Formulario["PAIS"].Valor == "LIECHTENSTEIN" or Formulario["PAIS"].Valor == "LUXEMBURGO" or Formulario["PAIS"].Valor == "MÔNACO" or Formulario["PAIS"].Valor == "MONTENEGRO" or Formulario["PAIS"].Valor == "NORUEGA" or Formulario["PAIS"].Valor == "OMÃ" or Formulario["PAIS"].Valor == "PEÍSES BAIXOS" or Formulario["PAIS"].Valor == "PORTUGAL" or Formulario["PAIS"].Valor == "REINO UNIDO" or Formulario["PAIS"].Valor == "REPÚBLICA QUIRGUIZ" or Formulario["PAIS"].Valor == "SEICHELES" or Formulario["PAIS"].Valor == "SÉRVIA SUAZILÂNDIA" or Formulario["PAIS"].Valor == "SUÉCIA" or Formulario["PAIS"].Valor == "SUÍÇA" or Formulario["PAIS"].Valor == "VANUATU":
    if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE":
        Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "460"
                
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "420"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "390"
            
    elif Formulario["FUNCAO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "ASSESSOR EXEC DA PRESIDENCIA":
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "390"
            
    elif (("GERENTE" in Formulario["FUNCAO_DESLOCAMENTO"].Valor) or ("GERENTE" in Formulario["CARGO_DESLOCAMENTO"].Valor)) and ((Formulario["FUNCAO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO") or (Formulario["CARGO_DESLOCAMENTO"].Valor != "GERENTE EXECUTIVO")):
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "370"
                  
                  
    else:
            Formulario["CAMPO_VALIDACAO_DOLAR"].Valor = "350"
                    
if (Formulario["PAIS"].Valor != "") or (Formulario["PAIS"].Valor != None):
    Formulario["TIPO_DESTINO"].Valor = "Exterior"
    Formulario["TIPO_DESTINO"].Habilitado = False
```
  - TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO] obrigatório — Coluna=4
  - CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO] — Coluna=2
**CIDADE_DESTINO.ScriptModificado**
```python
sqlConsultaCidadeDestino = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao ||' - '|| c.id_estado as cidade FROM cidade_v c WHERE id_cidade = '"+Formulario["CIDADE_DESTINO"].Valor.ToString()+"'")

#sqlConsultaClassificacao = DB.ExecuteDataTable("select DISTINCT CLASSIFICACAO, CIDADE || ' - ' || UF AS cidadeuf from Z_00143_CIDADES_CLASSIFICACOES where CIDADE || ' - ' || UF = '"+sqlConsultaCidadeDestino.Rows[0]["CIDADE"].ToString()+"'")

sqlConsultaClassificacao = DB.ExecuteDataTable("select DISTINCT CLASSIFICACAO, CIDADE || ' - ' || UF AS cidadeuf from Z_00143_CIDADES_CLASSIFICACOES where CIDADE || ' - ' || UF = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE('"+sqlConsultaCidadeDestino.Rows[0]["CIDADE"].ToString()+"','Ã','A'),'Á','A'),'É','E'),'Í','I'),'Ó','O'),'Õ','O'),'Ú','U'),'Ç','C')")

for classificacao in sqlConsultaClassificacao.Rows:
    Formulario["CIDADE_CLASSIFICACAO"].Valor = classificacao["CLASSIFICACAO"].ToString()
```
  - CIDADE_CLASSIFICACAO "Cidade Classificação" [TextBox String → CPE_CSC.CIDADE_CLASSIFICACAO]
  - CIDADE_DESTINO_INTERNACIONAL "Cidade de Destino (Internacional)" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL] obrigatório — Coluna=2
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA] obrigatório
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] obrigatório — Coluna=3
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] obrigatório — Configuracao={"Mascara":"00:00"}
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] obrigatório — Coluna=3; Configuracao={"Mascara":"00:00"}
**RETORNO_HORA.ScriptModificado**
```python
import clr 
import datetime

data1 = ""
data2 = ""

data1 = Formulario["SAIDA"].Valor
data2 = Formulario["RETORNO_DIA"].Valor
 
delta = data2 - data1
diferenca = delta.Days

if diferenca == 0 or diferenca == '0':
    diferenca = 1


Formulario["DIAS_DE_TRA"].Valor = diferenca
Formulario["DIAS_DE_TRA"].Habilitado = False
```
  - DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
  - TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM] obrigatório
**TIPO_HOSPEDAGEM.ScriptModificado**
```python
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
    Formulario["QUANTIDADE_DIARIA"].Visivel = False
    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PARCELA_COMPLEMENTAR"].Visivel = False
    Formulario["PARCELA_COMPLEMENTAR"].Habilitado = False
    Formulario["TOTAL_COMPLEMENTAR"].Visivel = False
    Formulario["TOTAL_COMPLEMENTAR"].Habilitado = False    
    Formulario["TOTAL_COMPLEMENTAR"].Valor = "0" 
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = False        

if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa COM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = True
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = True

    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa COM apresentação de NF":
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False
       
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
    Formulario["QUANTIDADE_DIARIA"].Valor = ""
    Formulario["VALOR_DIARIA"].Valor = "" 
    
#Remover quando não houver mais tipo de hospedagens avulsas!!!!!!    
if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    Formulario["QUANTIDADE_DIARIA"].Visivel = True
    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA"].Visivel = True
    Formulario["VALOR_DIARIA"].Habilitado = True
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = True
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = True
    
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
    Formulario["PAHL_HOSPEDAGENS"].Habilitado = False
    Formulario["PAHL_HOSPEDAGENS"].Visivel = False
    
 
queryAdesaoDiariaAvulaSemApresentarNF = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA Where OCORRENCIA.ASSUNTO = 'Adesão a diárias avulsas sem comprovação documental' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+Formulario["FAVORECIDO_DESLOCAMENTO"].Valor+"'")

if queryAdesaoDiariaAvulaSemApresentarNF.Rows.Count == 0 and Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF":
    Formulario.ExibeMensagem("Parece que seu aceite, Adesão a diárias avulsas sem comprovação documental, não foi feito. O Aceite é necessário para este tipo de solicitação.")
 
if Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada":
    Formulario["VALOR_DIARIA"].Valor = 0
    Formulario["VALOR_DIARIA"].Visivel = False
    Formulario["VALOR_TOTAL_DIARIA"].Valor = 0
    Formulario["VALOR_TOTAL_DIARIA"].Visivel = False
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = 0
    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
    Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = 0
    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = 0
    
#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = True
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA"].Visivel = True
#    Formulario["VALOR_DIARIA"].Habilitado = True
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = True    
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = False    
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = False
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False    
    

#if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa" or Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional"):
#    Formulario["QUANTIDADE_DIARIA"].Visivel = False
#    Formulario["QUANTIDADE_DIARIA"].Habilitado = False
#    Formulario["VALOR_DIARIA"].Visivel = False
#    Formulario["VALOR_DIARIA"].Habilitado = False
#    Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
#    Formulario["VALOR_TOTAL_DIARIA"].Habilitado = True
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = False
#    Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Visivel = True
#    Formulario["DIARIA_AUTORIZADO_INTERNACIONAL"].Habilitado = True
#    Formulario["VALOR_DIARIA_DOLAR"].Visivel = True
#    Formulario["VALOR_DIARIA_DOLAR"].Habilitado = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Visivel = True
#    Formulario["CAMPO_VALIDACAO_DOLAR"].Habilitado = False
```
  - DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS] obrigatório
  - QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA] obrigatório
**QTD_REFEICAO_REDUZIDA.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    
qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario["SIM_NAO"].Valor == "Sim":
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = True
else:
    Formulario["NUM_ABERTURA_CHAMADO"].Visivel = False
```
  - QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL] obrigatório
**QTD_REFEICAO_INTEGRAL.ScriptModificado**
```python
import calculos_deslocamento_v29
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.


import System
import clr 
import datetime
import System.Text

Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False

qtdRef = qtdRefeicoes(Formulario["SAIDA"].Valor, Formulario["RETORNO_DIA"].Valor, Formulario["SAIDA_HORA"].Valor, Formulario["RETORNO_HORA"].Valor)


if Convert.ToInt32(qtdRef[0]['integral']) < Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor):
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = qtdRef[0]['integral']
    Formulario.ExibeMensagem("Quantidade de Refeições Integrais Excedida! Máximo permitido: " + qtdRef[0]['integral'].ToString() + " Verifique a Saída e o Retorno.")
if Convert.ToInt32(qtdRef[0]['reduzida']) < Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor):
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = qtdRef[0]['reduzida']
    Formulario.ExibeMensagem("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + qtdRef[0]['reduzida'].ToString() + " Verifique a Saída e o Retorno.")
    
valor = valorRefeicoes(Convert.ToInt32(Formulario["QTD_REFEICAO_INTEGRAL"].Valor),Convert.ToInt32(Formulario["QTD_REFEICAO_REDUZIDA"].Valor))

Formulario["VALOR_TOTAL_REFEICAO"].Valor = valor[0]['total']
Formulario["VALOR_REF_REDUZIDA"].Valor = valor[0]['reduzida']
Formulario["VALOR_REF_INTEGRAL"].Valor = valor[0]['integral']
```
  - VALOR_REF_REDUZIDA "Valor Refeições Reduzidas" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA] obrigatório
  - VALOR_REF_INTEGRAL "Valor refeições integrais" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS] obrigatório — Coluna=2
**VALOR_DESPESAS.ScriptModificado**
```python
import System

diariaAvulsa = 0
valorDist = 0 



#valorTotalPrestContas = OrdemServico.GetCustom("VALOR_DESPESAS") + OrdemServico.GetCustom("VALOR_DISTANCIA") + OrdemServico.GetCustom("VALOR_TOTAL_DIARIA")
#valorTotSemPrestContas = refeições, diaria de hotel contratada/sem hospedagem e parcela complementar

if (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica") or (Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa SEM apresentação de NF") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):

    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + totalDiaria + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
    
elif (Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada") and (Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Nacional" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem - Assistência Técnica" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Treinamento - Assistência Técnica"):
    valorTotalAdiantamento = 0
    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False


    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento

########Deslocamento para viagem internacional###############
elif Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
    
    valorTotalAdiantamento = 0


    totalDiaria = 0
    ##valorAvicao = 0
    outrasDespesas = 0
    ##valorDistancia = 0
    #complementar = 0

    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    totalDiaria = Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor)
    ##valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    ##valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    #complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    

    ##valorTotalAdiantamento =  totalDiaria + outrasDespesas + valorDistancia 
    valorTotalAdiantamento = totalDiaria + outrasDespesas
    
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False

    ##OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento
    
else:
    valorTotalAdiantamento = 0

    valorTotalRefeicao = 0
    #totalDiaria = 0
    #valorAvicao = 0
    outrasDespesas = 0
    valorDistancia = 0
    complementar = 0
    
    outrasDespesas = Convert.ToDecimal(Formulario["VALOR_DESPESAS"].Valor)
    #totalDiaria = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
    #valorAvicao = Convert.ToDecimal(Formulario["VALOR_PASSAGEM"].Valor)
    valorTotalRefeicao = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
    valorDistancia = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
    
    valorTotalAdiantamento = valorTotalRefeicao + outrasDespesas + valorDistancia + complementar

    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Valor = valorTotalAdiantamento
    Formulario["VALOR_TOTAL_ADIANTAMENTO"].Habilitado = False
    #Esta faltando pegar valor de diaria e da parcela complementar para o valor total
    


 
#Valores a prestar conta 
    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Avulsa":
#    
#    
#    diariaAvulsa = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#    
#    
#else:
#    diariaAvulsa = 0
#
#
#    
#if Formulario["VALOR_DISTANCIA"].Valor != 0:
#    valorDist = Convert.ToDecimal(Formulario["VALOR_DISTANCIA"].Valor)
#
#else:
#    valorDist = 0 
#    
#outrasDespesas2 = Convert.ToDecimal(outrasDespesas)
#
#valorTotalPrestContas = outrasDespesas2 + diariaAvulsa + valorDist
#
#
#
#Formulario["VALOR_TOT_PREST_CONTAS"].Valor = Convert.ToDecimal(valorTotalPrestContas)
#
#
#
##Valores sem necessidade de prestação de contas
#
#refeicoes = 0
#hospeda = 0
#complementar = 0
#
#
#
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA":
#
#    refeicoes = 0
#
#else:
#    refeicoes = Convert.ToDecimal(Formulario["VALOR_TOTAL_REFEICAO"].Valor)
#    
#
#    
#if Formulario["TIPO_HOSPEDAGEM"].Valor == "Contratada":
#   hospeda = Convert.ToDecimal(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#   
#elif Formulario["TIPO_HOSPEDAGEM"].Valor == "Sem Hospedagem":
#   hospeda = 0
#
#   
# 
#if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["TIPO_DESLOCAMENTO"].Valor == "Viagem a Serviço - Internacional":
#    complementar = 0
#else:
#    complementar = Convert.ToDecimal(Formulario["TOTAL_COMPLEMENTAR"].Valor)
#    
#
#    
#totalSemPrestContas = complementar + hospeda + refeicoes
#
#Formulario["VALORTOTSEMCOMPROV"].Valor = Convert.ToDecimal(totalSemPrestContas)
















    #OrdemServico["VALOR_TOTAL_ADIANTAMENTO"] = valorTotalAdiantamento
```
  - VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO] obrigatório
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO] obrigatório
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["CARGO_DESLOCAMENTO"].Visivel = True
Formulario["FUNCAO_DESLOCAMENTO"].Visivel = True
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Visivel = True
Formulario["MATRICULA_DESLOCAMENTO"].Visivel = True



Formulario["CARGO_DESLOCAMENTO"].Habilitado = False
Formulario["FUNCAO_DESLOCAMENTO"].Habilitado = False
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Habilitado = False
Formulario["MATRICULA_DESLOCAMENTO"].Habilitado = False



Formulario["CARGO_DESLOCAMENTO"].Valor = None
Formulario["FUNCAO_DESLOCAMENTO"].Valor = None
Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = None
Formulario["MATRICULA_DESLOCAMENTO"].Valor = None



cargo = ""
funcao = ""
desc_colaborador = ""
matricula = ""

if Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != "" or Formulario["FAVORECIDO_DESLOCAMENTO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["ORGAO_FAVORECIDO"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT SUBSTR(c.CARGO,INSTR(c.CARGO,'|')+1,LENGTH(c.CARGO)) AS CARGO1, c.FUNCAO_GRATIFICADA, c.DESC_COLABORADOR, c.MATRICULA, c.FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND C.NUMERO_SUBCR_NIVEL1 = O.SIGLA AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    #lista = Utils.ExecuteDataTable("SELECT SUBSTR(CARGO,INSTR(CARGO,'|')+1,LENGTH(CARGO)) AS CARGO1, FUNCAO_GRATIFICADA, DESC_COLABORADOR, MATRICULA, FIM_DATA_FUNCAO FROM PESSOA P INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO INNER JOIN CAD_FUNCIONARIO_V C ON C.NOME = P.NOME AND LPAD(C.NUMERO_SUBCR_NIVEL1,5) = LPAD(O.SIGLA,5) AND DATA_DE_DEMISSAO IS NULL AND P.NOME  = '"+nomeFavorecido+"'" + " AND P.ID_ORGAO = '" + orgaoFavorecido.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO1"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()

    Formulario["CARGO_DESLOCAMENTO"].Valor = cargo.ToString()
    Formulario["FUNCAO_DESLOCAMENTO"].Valor = funcao.ToString()
    Formulario["DESC_COLABORADOR_DESLOCAMENTO"].Valor = desc_colaborador.ToString()
    Formulario["MATRICULA_DESLOCAMENTO"].Valor = matricula.ToString()
    if desc_colaborador.ToString() != 'FUNCIONARIOS CONCURSADOS' and funcao.ToString()=='':
        Formulario["FUNCAO_DESLOCAMENTO"].Valor = cargo.ToString()
    
        


if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
else:
    Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
    
#if Formulario["FUNCAO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "GERENTE EXECUTIVO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR":
    #Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = False
#else:
    #Formulario["ACOMPANHANDO_GRUPO_A"].Visivel = True
    #Formulario["ACOMPANHANDO_GRUPO_A"].Valor = "Não"
```
  - MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - PREVISAO_DISTANCIA_KM "Previsão de distancia em KM (Para recebimento de R$1,30 por KM)" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM] obrigatório
**PREVISAO_DISTANCIA_KM.ScriptModificado**
```python
import System


Formulario["VALOR_DISTANCIA"].Habilitado = False

valorTotal = 0

distancia = Formulario["PREVISAO_DISTANCIA_KM"].Valor
valorTotal = distancia * 1.30 


Formulario["VALOR_DISTANCIA"].Valor = valorTotal
#OrdemServico["VALOR_DISTANCIA"] = valorTotal
#
```
  - VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA] obrigatório — Coluna=2
  - SIM_NAO_REFEICAO "O Empregado/Gestor terá direito a refeição complementar?" [DropDownList String → CPE_DESLOCAMENTO.SIM_NAO_REFEICAO] obrigatório
**SIM_NAO_REFEICAO.ScriptModificado**
```python
import clr 
import datetime
import System.Text
 


zero = 0
valorRefIntegral = 71
valorRefReduzida = 20.29



daysOffText = System.Text.StringBuilder()


##RETORNA SE A DATA PASSADA COMO PARAMETRO É FERIADO COM BASE NO SELECT
def isHoliday(day):
    holidays = DB.ExecuteDataTable("SELECT DATA FROM CALENDARIO C inner join FERIADO F on F.ID_CALENDARIO = c.ID_CALENDARIO WHERE C.DESCRICAO = 'Nacional'")
    #feriados = 0
    
    for holiday in holidays.Rows:
        if day == holiday["DATA"].Date:
            #feriados += 2
            return True
    return False


def countHolidays(firstDate, lastDate):
    totalHolidays = 0
    currentDay = firstDate

    while currentDay <= lastDate:
        if isHoliday(currentDay):
            totalHolidays += 1
        currentDay = currentDay.AddDays(1)

    return totalHolidays

    
def workingDays(totalDays, firstDate):

    totalWorkingDays = 0
    totalDaysOff = 0
    count = 0

   
    while count <= totalDays:
        dayOfWeek = firstDate.Date.AddDays(count).DayOfWeek
        day = firstDate.Date.AddDays(count)
        
        
        
        if (dayOfWeek == DayOfWeek.Sunday or dayOfWeek == DayOfWeek.Saturday)or isHoliday(day):
            totalDaysOff = totalDaysOff + 1
            daysOffText.AppendLine(" dayOff: "+str(day))
        
        count = count + 1
        totalWorkingDays = totalWorkingDays + 1
    return totalWorkingDays - totalDaysOff
   


    
def countSaturdays(firstDate, lastDate):
    saturdays = 0
    currentDay = firstDate
    
    while currentDay <= lastDate:
        if (currentDay.DayOfWeek == DayOfWeek.Sunday or currentDay.DayOfWeek == DayOfWeek.Saturday):
            saturdays += 2
        currentDay = currentDay.AddDays(1)  # Avance para o próximo dia
    
    return saturdays

    
firstDate = Formulario["SAIDA"].Valor
lastDate = Formulario["RETORNO_DIA"].Valor

totalDays = (lastDate - firstDate).TotalDays
count = 0





totalWorkingDays = workingDays(totalDays,firstDate)
holidaysCount = countHolidays(firstDate, lastDate)
saturdays = countSaturdays(firstDate, lastDate) + holidaysCount * 2


#Quantidade de refeições Reduzias e integrais
quantRed = totalWorkingDays
quantInt = saturdays + totalWorkingDays 






#Atribuindo valor a variável
saidaHora = Formulario["SAIDA_HORA"].Valor 
retornoHora = Formulario["RETORNO_HORA"].Valor 

#Split de horário, separando hora de minuto
hora = saidaHora.Split(':');     
horaRetorno = retornoHora.Split(':');

#Atribuindo valor de horário e minuto de acordo com o índice da variável
horarioSaida = hora[0]
minutoSaida = hora[1]

horarioRetorno = horaRetorno[0] 
minutoRetorno = horaRetorno[1]



#SAIDA DIAS ÚTEIS


#1 maior q o 2
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) >= 13 and Convert.ToInt32(horarioSaida) < 21):
#    quantRed = quantRed - 1
#   
#if workingDays(0,firstDate) and (Convert.ToInt32(horarioSaida) > 21):
#    quantInt = quantInt - 1
#   
#RETORNO DIAS ÚTEIS
#1 menor q o 2   
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 13:
#    quantRed = quantRed - 1
#    quantInt = quantInt - 1
#    
#if workingDays(0,lastDate) and Convert.ToInt32(horarioRetorno) <= 19 and Convert.ToInt32(horarioRetorno) > 13:
#    quantInt = quantInt - 1
#    #teste abaixo
#    quantRed = quantRed - 1





#DIAS UTEIS

if workingDays(0,firstDate):
    if (Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioSaida) > 21) or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if workingDays(0,lastDate):    
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantRed = quantRed - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
#Formulario.ExibeMensagem("hora:"+horarioRetorno.ToString()+" minuto:"+minutoRetorno.ToString())    
###############################################################
    
#SAÍDA FINAIS DE SEMANA E/OU FERIADOS

if not  workingDays(0,firstDate):
    if Convert.ToInt32(horarioSaida) > 13 or (Convert.ToInt32(horarioSaida) == 13 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
    if Convert.ToInt32(horarioSaida) > 21 or (Convert.ToInt32(horarioSaida) == 21 and Convert.ToInt32(minutoSaida) > 0):
        quantInt = quantInt - 1
if not  workingDays(0,lastDate):
    if (Convert.ToInt32(horarioRetorno) < 13 or (Convert.ToInt32(horarioRetorno) == 13 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1
    if (Convert.ToInt32(horarioRetorno) < 19 or (Convert.ToInt32(horarioRetorno) == 19 and Convert.ToInt32(minutoRetorno) == 0)):
        quantInt = quantInt - 1   


if Formulario["CARGO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor == "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO FISCAL" or Formulario["CARGO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["CARGO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "DIRETOR" or  Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO  FISCAL" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO DE ADMINISTRACAO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "MEMBRO COMITE DE AUDITORIA": 
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Visivel = False
    Formulario["SIM_NAO_REFEICAO"].Habilitado = False
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = quantRed
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = quantInt
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Visivel = True
    Formulario["SIM_NAO_REFEICAO"].Habilitado = True
  
    
if quantRed > (totalWorkingDays):
    mensagem = ("Quantidade de Refeições Reduzidas Excedida! Máximo permitido: " + str(totalWorkingDays + 1) + " Verifique a Saída e o Retorno.")
    Formulario.ExibeMensagem(mensagem)    
    Formulario["VALOR_TOTAL_REFEICAO"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    

############# calculo valor total

refIntegral = Formulario["QTD_REFEICAO_INTEGRAL"].Valor * valorRefIntegral
refReduzida = Formulario["QTD_REFEICAO_REDUZIDA"].Valor * valorRefReduzida
valorTotalRefeicoes = refIntegral + refReduzida

if Formulario["SIM_NAO_REFEICAO"].Valor == "Sim":
    Formulario["VALOR_TOTAL_REFEICAO"].Valor  = valorTotalRefeicoes
    Formulario["VALOR_REF_REDUZIDA"].Valor = refReduzida
    Formulario["VALOR_REF_INTEGRAL"].Valor = refIntegral
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = True
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = True
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = True
    Formulario["VALOR_REF_REDUZIDA"].Visivel = True
    Formulario["VALOR_REF_INTEGRAL"].Visivel = True
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = True
else:
    Formulario["QTD_REFEICAO_REDUZIDA"].Valor = zero
    Formulario["QTD_REFEICAO_INTEGRAL"].Valor = zero
    Formulario["QTD_REFEICAO_REDUZIDA"].Habilitado = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Habilitado = False
    Formulario["QTD_REFEICAO_REDUZIDA"].Visivel = False
    Formulario["QTD_REFEICAO_INTEGRAL"].Visivel = False
    Formulario["VALOR_REF_REDUZIDA"].Valor = zero
    Formulario["VALOR_REF_INTEGRAL"].Valor = zero
    Formulario["VALOR_TOTAL_REFEICAO"].Valor = zero  
    Formulario["VALOR_REF_REDUZIDA"].Visivel = False
    Formulario["VALOR_REF_INTEGRAL"].Visivel = False
    Formulario["VALOR_TOTAL_REFEICAO"].Visivel = False
```
  - VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO] obrigatório — Coluna=2
  - VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA] obrigatório
  - VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA] obrigatório
**VALOR_DIARIA.ScriptModificado**
```python
if Formulario["ACOMPANHANDO_GRUPO_A"].Valor == "Sim":
         Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor
    



if Formulario["FUNCAO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "DIRETOR" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "CONSELHEIRO" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "CONSELHEIRO" or Formulario["FUNCAO_DESLOCAMENTO"].Valor == "PRESIDENTE" or Formulario["CARGO_DESLOCAMENTO"].Valor ==  "PRESIDENTE": 
     Formulario["CAMPO_VALIDACAO_DIARIA"].Valor = Formulario["VALOR_DIARIA"].Valor


     
     
if Convert.ToDecimal(Formulario["VALOR_DIARIA"].Valor) >= Convert.ToDecimal(Formulario["CAMPO_VALIDACAO_DIARIA"].Valor):
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["CAMPO_VALIDACAO_DIARIA"].Valor
else:
    Formulario["VALOR_DIARIA_AUTORIZADO"].Valor = Formulario["VALOR_DIARIA"].Valor
    
    
Formulario["VALOR_TOTAL_DIARIA"].Habilitado = False
Formulario["VALOR_TOTAL_DIARIA"].Visivel = True
Formulario["CAMPO_VALIDACAO_DIARIA"].Habilitado = False
Formulario["CAMPO_VALIDACAO_DIARIA"].Visivel = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Habilitado = False
Formulario["VALOR_DIARIA_AUTORIZADO"].Visivel = True

valorTotal = 0

quantDiaria = Convert.ToDecimal(Formulario["QUANTIDADE_DIARIA"].Valor)
valorDiaria = Convert.ToDecimal(Formulario["VALOR_DIARIA_AUTORIZADO"].Valor)

valorTotal = quantDiaria * valorDiaria 

Formulario["VALOR_TOTAL_DIARIA"].Valor =  valorTotal 


OrdemServico["VALOR_TOTAL_DIARIA"] = valorTotal
```
  - VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO] obrigatório — Coluna=2
  - CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-001)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA] obrigatório
  - PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR] obrigatório
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM] obrigatório
  - COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR] obrigatório
**COTACAO_DOLAR.ScriptModificado**
```python
#import System
#
#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)
#
#
#Convert.ToDecimal(Formulario["DIARIA_COTACAO_REAL"].Valor) = valorTotal


valorTotal = 0
vtd = Formulario["VALOR_TOTAL_DIARIA"].Valor
cd = Convert.ToDecimal(Formulario["COTACAO_DOLAR"].Valor)

valorTotal = vtd * cd

Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal




#valorTotal = 0
#
#
#valorTotal = Formulario["VALOR_TOTAL_DIARIA"].Valor * (Formulario["COTACAO_DOLAR"].Valor)
#
#
#Formulario["DIARIA_COTACAO_REAL"].Valor = valorTotal
#

#diariaReal = ""
#cotacao = ""
#valorTotal = ""
#
#diariaReal = Convert.ToDouble(Formulario["VALOR_TOTAL_DIARIA"].Valor)
#cotacao = Convert.ToDouble(Formulario["COTACAO_DOLAR"].Valor)
```
  - DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL] obrigatório — Coluna=2
  - NUMERO_NT "Número da Nota Técnica" [TextBox String → CPE_CONTRATOS.NUMERO_NT] obrigatório — Configuracao={"Mascara":"0000/0000"}

### [369123] Tarefa "Aprovar Deslocamento - Gerente Favorecido"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVAR_DESLOCAMENTO
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
**ScriptInicio**
```python
# modifica a propriedade FavorecidoId
OrdemServico.FavorecidoId = Convert.ToInt32(OrdemServico["FAVORECIDO_DESLOCAMENTO"])
# salva modificação da propriedade FavorecidoId
OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos
  - Favorecido (nativo) obrigatório
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação conforme NI006; CopiarAnexados=true
  - (aprovação) SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - (aprovação) CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR]
  - (aprovação) SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA]
  - (aprovação) CIDADE_DESTINO_INTERNACIONAL "Cidade/País de Destino" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL]
  - (aprovação) CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - (aprovação) DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - (aprovação) VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO]
  - (aprovação) VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR]
  - (aprovação) VALOR_REF_REDUZIDA "Valor Refeição Reduzida" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA]
  - (aprovação) QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA]
  - (aprovação) NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO]
  - (aprovação) QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA]
  - (aprovação) OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM]
  - (aprovação) TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO]
  - (aprovação) RESERVA_DE_VOO "Informações da Reserva de Voo - Nacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO] — PermiteModificarAprovado=true
  - (aprovação) FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - (aprovação) VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA]
  - (aprovação) RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA]
  - (aprovação) MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO]
  - (aprovação) VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - (aprovação) CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - (aprovação) PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS]
  - (aprovação) PAH_HOTEL_EVENTO "Hotel do Evento" [TextBox String → CPE_CSC.PAH_HOTEL_EVENTO] — PermiteModificarAprovado=true
  - (aprovação) PAHL_PASSAGENS "Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS] — PermiteModificarAprovado=true
  - (aprovação) VIAGEM_LONGA "Distância da Viagem de Carro (Programa Valor)" [DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA]
  - (aprovação) DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL]
  - (aprovação) COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR]
  - (aprovação) MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - (aprovação) PAH_MOTIVO_SOL "Motivo da Solicitação" [DropDownList String → CPE_CSC.PAH_MOTIVO_SOL] — PermiteModificarAprovado=true
  - (aprovação) TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR]
  - (aprovação) CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO]
  - (aprovação) QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL]
  - (aprovação) RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA]
  - (aprovação) DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha) " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS] — PermiteModificarAprovado=true
  - (aprovação) TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM]
  - (aprovação) PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR]
  - (aprovação) PAH_DATA_ENTRADA "Data de Entrada no Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA] — PermiteModificarAprovado=true
  - (aprovação) PAH_EVENTO_HOTEL "Evento no Hotel?" [DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL] — PermiteModificarAprovado=true
  - (aprovação) DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL]
  - (aprovação) PAH_DATA_SAIDA "Data de Saída do Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA] — PermiteModificarAprovado=true
  - (aprovação) CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA]
  - (aprovação) CSC_OBS "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS] — PermiteModificarAprovado=true
  - (aprovação) FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
  - (aprovação) PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO] — PermiteModificarAprovado=true
  - (aprovação) ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A]
  - (aprovação) PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM] — PermiteModificarAprovado=true
  - (aprovação) DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - (aprovação) SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA]
  - (aprovação) VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA]
  - (aprovação) VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO]
  - (aprovação) RESERVA_DE_VOO_INTERNACIONAL "Informações para Reserva de Voo - Internacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL] — PermiteModificarAprovado=true
  - (aprovação) PREVISAO_DISTANCIA_KM "Previsão de distancia em KM" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM]
  - (aprovação) LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE]
  - (aprovação) PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO] — PermiteModificarAprovado=true
  - (aprovação) VALOR_REF_INTEGRAL "Valor Refeição Integral" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - (aprovação) VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA]
  - (aprovação) PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES] — PermiteModificarAprovado=true
  - (aprovação) PAHL_HOSPEDAGENS "Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS] — PermiteModificarAprovado=true
  - (aprovação) PAHL_LOCACOES "Locações" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES] — PermiteModificarAprovado=true
  - (aprovação) VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS]
  - (aprovação) TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO]
  - aprovador: Aprovação Viagem e Hospedagem - Conforme NI006v.87 (Unico)

### [369124] EventoFinal ""
Responsável: Responsavel Processo (papel 1378)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
**ScriptInicio**
```python
if OrdemServico.Numero.ToString() =='1136419':
    OrdemServico.SetCustom('SAIDA_HORA','08:57')
    
    
if OrdemServico["DESCRICAO_DESPESAS"] == "":
    OrdemServico.SetCustom('DESCRICAO_DESPESAS', 'NA')
OrdemServico.Salva()
```
**ScriptFim**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Pesquisa
idCliente = OrdemServico.ClienteId

listaPesq = DB.ExecuteDataTable("SELECT ID_PESQUISA FROM PESQUISA WHERE OS = '" + OrdemServico.Id.ToString() +"'")

for pesq in listaPesq.Rows:
    pesquisa = Pesquisa.Carrega(pesq["ID_PESQUISA"])

    # modifica a propriedade Avaliador
    pesquisa.Avaliador = Pessoa.Carrega(idCliente);

    # salva modificação da propriedade Avaliador
    Pesquisa.Salva(pesquisa)
```

### [369126] EventoIntermediarioMensagem "Reserva não realizada"
Destinatário: Cliente (papel 18)
ModeloComunicado: Deslocamento a Serviço - Reserva não realizada
Corpo do comunicado: Prezado,
A reserva OrdemServico.Numero - OrdemServico.Assunto solicitada não foi realizada.
Motivo: Complemento1 
Mais informações verifique pelo link Link.Edicao Worklist 
Atenciosamente,
Centro de Serviços Compartilhados
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("RESERVANAOREALIZADA")
```

### [369127] Tarefa "Incluir informações da Reserva"
Responsável: Responsável atual (papel 36)
Config: Codigo=PAH_EXEC_ATIV_SOL; UnidadeANO=Minutos
MotivoInterrupcaoSLA: Aguardando ação de intervenientes externos
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
#OrdemServico.ModificaCampoFormularioVisivel("CSC_NUM_SISLOC", True)
#OrdemServico.ModificaCampoFormularioHabilitado("CSC_NUM_SISLOC", False)

pessoa = Pessoa.Carrega("Id", Convert.ToInt32(OrdemServico["FAVORECIDO_DESLOCAMENTO"]))
orgao = Orgao.Carrega(pessoa.OrgaoId)

OrdemServico.Favorecido = pessoa

OrdemServico.SetCustom("MATRICULA_DESLOCAMENTO", pessoa["MATRICULA"])

lista = Utils.ExecuteDataTable(" select IDENTIDADE||'-'||ORGAO_IDENTIDADE as RG, data_de_aniversario as NASCIMENTO from cad_funcionario_v where matricula ='"+ pessoa["MATRICULA"].ToString() +"'") 

for linha in lista.Rows:
    OrdemServico.SetCustom("CSC_RG", linha["RG"])
    OrdemServico.SetCustom("CSC_DATA_NASCIMENTO", linha["NASCIMENTO"])
OrdemServico.Salva

#for controle in Formulario.Controles:
#    if controle.Key != "FAVORECIDO_DESLOCAMENTO":
#       Formulario[controle.Key].Visivel = False
#       Formulario[controle.Key].Valor = None

#OrdemServico["MATRICULA"] = pessoa["MATRICULA"]
OrdemServico["CPF"] = pessoa["CPF"]
OrdemServico["EMAIL_CLIENTE"] = pessoa.Email #["EMAIL"]
OrdemServico["TELEFONE_CLIENTE"] = pessoa.Telefone #["TELEFONE"]
OrdemServico["SCR_PRESTADOR"] = orgao.Descricao
#OrdemServico["CELULAR"] = None
# 
#OrdemServico["MATRICULA"].Visivel = True
#OrdemServico["CPF"].Visivel = True
#OrdemServico["EMAIL_CLIENTE"].Visivel = True
#OrdemServico["TELEFONE_CLIENTE"].Visivel = True
#OrdemServico["SCR_PRESTADOR"].Visivel = True
#OrdemServico["CELULAR"].Visivel = True
#
#OrdemServico["MATRICULA"].Habilitado = False
#OrdemServico["CPF"].Habilitado = False
#OrdemServico["EMAIL_CLIENTE"].Habilitado = False
#OrdemServico["TELEFONE_CLIENTE"].Habilitado = False
#OrdemServico["SCR_PRESTADOR"].Habilitado = False
#OrdemServico.["CELULAR"].Habilitado = True
#
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["PAHL_PASSAGENS"].Visivel = Formulario["PAHL_PASSAGENS"].Valor == True
Formulario["PAHL_PASSAGENS"].Habilitado = Formulario["PAHL_PASSAGENS"].Valor == False

Formulario["PAHL_HOSPEDAGENS"].Visivel = Formulario["PAHL_HOSPEDAGENS"].Valor == True
Formulario["PAHL_HOSPEDAGENS"].Habilitado = Formulario["PAHL_HOSPEDAGENS"].Valor == False

Formulario["PAHL_LOCACOES"].Visivel = Formulario["PAHL_LOCACOES"].Valor == True
Formulario["PAHL_LOCACOES"].Habilitado = Formulario["PAHL_LOCACOES"].Valor == False

Formulario["PAH_LOCALIZADORES"].Visivel = Formulario["PAHL_PASSAGENS"].Valor == True
Formulario["PAH_LOCALIZADORES"].Habilitado = Formulario["PAHL_PASSAGENS"].Valor == True

Formulario["CSC_VALOR1_TOTAL"].Visivel = Formulario["PAHL_PASSAGENS"].Valor == True
Formulario["CSC_VALOR1"].Visivel = Formulario["PAHL_HOSPEDAGENS"].Valor == True

Formulario["PAH_VOUCHER_HOSPEDAGEM"].Visivel = Formulario["PAHL_HOSPEDAGENS"].Valor == True
Formulario["PAH_VOUCHER_HOSPEDAGEM"].Habilitado = Formulario["PAHL_HOSPEDAGENS"].Valor == True

Formulario["PAHL_VOUCHER_CARRO"].Visivel = Formulario["PAHL_LOCACOES"].Valor == True
Formulario["PAHL_VOUCHER_CARRO"].Habilitado = Formulario["PAHL_LOCACOES"].Valor == True
Formulario["CSC_VALOR2"].Visivel = Formulario["PAHL_LOCACOES"].Valor == True

#OrdemServico.ModificaCampoFormularioVisivel("CSC_NUM_SISLOC", True)
#OrdemServico.ModificaCampoFormularioHabilitado("CSC_NUM_SISLOC", False)


pessoa = Pessoa.Carrega("Id", Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

OrdemServico.Favorecido = pessoa

#Formulario["MATRICULA"].Valor = pessoa["MATRICULA"]


#Formulario["CSC_NUM_SISLOC"].Habilitado = True
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Arquivo" classes: Arquivo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Voucher" classes: Voucher — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados do Favorecido
  - CELULAR "Celular do Favorecido" [TextBox String → CP_ORDEM_SERVICO.CELULAR]
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
**FAVORECIDO_DESLOCAMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
#pessoa = Pessoa.Carrega(Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor))
pessoa = Pessoa.Carrega("Id", Convert.ToInt32(Formulario["FAVORECIDO_DESLOCAMENTO"].Valor))
orgao = Orgao.Carrega(pessoa.OrgaoId)

OrdemServico.Favorecido = pessoa

for controle in Formulario.Controles:
    if controle.Key != "FAVORECIDO_DESLOCAMENTO":
       Formulario[controle.Key].Visivel = False
       Formulario[controle.Key].Valor = None

Formulario["MATRICULA"].Valor = pessoa["MATRICULA"]
Formulario["CPF"].Valor = pessoa["CPF"]
Formulario["EMAIL_CLIENTE"].Valor = pessoa.Email #["EMAIL"]
Formulario["TELEFONE_CLIENTE"].Valor = pessoa.Telefone #["TELEFONE"]
Formulario["SCR_PRESTADOR"].Valor = orgao.Descricao
Formulario["CELULAR"].Valor = None
 
Formulario["MATRICULA"].Visivel = True
Formulario["CPF"].Visivel = True
Formulario["EMAIL_CLIENTE"].Visivel = True
Formulario["TELEFONE_CLIENTE"].Visivel = True
Formulario["SCR_PRESTADOR"].Visivel = True
Formulario["CELULAR"].Visivel = True

Formulario["MATRICULA"].Habilitado = False
Formulario["CPF"].Habilitado = False
Formulario["EMAIL_CLIENTE"].Habilitado = False
Formulario["TELEFONE_CLIENTE"].Habilitado = False
Formulario["SCR_PRESTADOR"].Habilitado = False
Formulario["CELULAR"].Habilitado = True

#Formulario["CSC_NUM_SISLOC"].Visivel = True
#Formulario["CSC_NUM_SISLOC"].Habilitado = True
```
  - MATRICULA_DESLOCAMENTO "Matrícula do Favorecido" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - TELEFONE_CLIENTE "Telefone do Favorecido" [TextBox String(300) → CP_ORDEM_SERVICO.TELEFONE_CLIENTE]
  - SCR_PRESTADOR "UOR do Favorecido" [TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR]
**SCR_PRESTADOR.ScriptModificado**
```python
#OrdemServico.SetCustom("SCR", Formulario["SCR_PRESTADOR"].Valor)
```
  - EMAIL_CLIENTE "E-mail do Favorecido" [TextBox String(200) → CP_ORDEM_SERVICO.EMAIL_CLIENTE]
  - CPF "CPF" [TextBox String(15) → CP_ORDEM_SERVICO.CPF]
  - CSC_RG "RG" [TextBox String → CPE_CSC.CSC_RG] obrigatório
  - CSC_DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CPE_CSC.CSC_DATA_NASCIMENTO] obrigatório
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Localizador e Voucher - Solicitação
  - CSC_DATA_INICIO "Data da Saída" [DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO] obrigatório
  - CSC_DATA_FIM "Data do Retorno" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
  - CSC_VALOR1_TOTAL "Valor das Passagens" [TextBox Decimal → CPE_CSC.CSC_VALOR1_TOTAL] obrigatório
  - CSC_VALOR2 "Valor Total das Locações de Carro" [TextBox Decimal → CPE_CSC.CSC_VALOR2] obrigatório
  - CSC_OBS1 "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS1]
  - PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM] obrigatório
  - CSC_VALOR1 "Valor Total das Diárias" [TextBox Decimal → CPE_CSC.CSC_VALOR1] obrigatório
  - PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO] obrigatório
  - PAHL_NUM_ARGO "Número da OS Argo" [TextBox String → CPE_CSC.PAHL_NUM_ARGO] obrigatório
  - PAHL_PASSAGENS "Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS] obrigatório
  - PAHL_HOSPEDAGENS "Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS] obrigatório
  - PAHL_LOCACOES "Locações" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES] obrigatório
  - PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna CIA_AEREA obrigatório
    - coluna LOCALIZADOR obrigatório
    - coluna SEQUENCIA obrigatório
    - coluna VALOR_TRECHO

### [369131] Tarefa "Aprovar Deslocamento - Diretor do Favorecido"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVARDIREX
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do Diretor; CopiarAnexados=true; ReutilizaAprovacaoAnterior=true
  - (aprovação) SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA]
  - (aprovação) TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR]
  - (aprovação) QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA]
  - (aprovação) VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA]
  - (aprovação) PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS]
  - (aprovação) CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO]
  - (aprovação) RESERVA_DE_VOO "Informações da Reserva de Voo - Nacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO] — PermiteModificarAprovado=true
  - (aprovação) SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA]
  - (aprovação) CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - (aprovação) VALOR_REF_INTEGRAL "Valor Refeição Integral" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - (aprovação) PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES] — PermiteModificarAprovado=true
  - (aprovação) CSC_OBS "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS] — PermiteModificarAprovado=true
  - (aprovação) PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM] — PermiteModificarAprovado=true
  - (aprovação) CIDADE_DESTINO_INTERNACIONAL "Cidade/País de Destino" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL]
  - (aprovação) DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - (aprovação) VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA]
  - (aprovação) TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO]
  - (aprovação) COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR]
  - (aprovação) DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL]
  - (aprovação) VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA]
  - (aprovação) VIAGEM_LONGA "Distância da Viagem de Carro (Programa Valor)" [DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA]
  - (aprovação) DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL]
  - (aprovação) SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - (aprovação) PREVISAO_DISTANCIA_KM "Previsão de distancia em KM" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM]
  - (aprovação) FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - (aprovação) ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A]
  - (aprovação) TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM]
  - (aprovação) QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA]
  - (aprovação) RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA]
  - (aprovação) PAH_DATA_SAIDA "Data de Saída do Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA] — PermiteModificarAprovado=true
  - (aprovação) VALOR_REF_REDUZIDA "Valor Refeição Reduzida" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA]
  - (aprovação) CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - (aprovação) PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR]
  - (aprovação) OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM]
  - (aprovação) QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL]
  - (aprovação) PAHL_PASSAGENS "Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS] — PermiteModificarAprovado=true
  - (aprovação) PAH_EVENTO_HOTEL "Evento no Hotel?" [DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL] — PermiteModificarAprovado=true
  - (aprovação) PAHL_LOCACOES "Locações" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES] — PermiteModificarAprovado=true
  - (aprovação) VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS]
  - (aprovação) CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA]
  - (aprovação) TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO]
  - (aprovação) VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR]
  - (aprovação) NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO]
  - (aprovação) FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
  - (aprovação) CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR]
  - (aprovação) DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha) " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS]
  - (aprovação) MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - (aprovação) PAH_HOTEL_EVENTO "Hotel do Evento" [TextBox String → CPE_CSC.PAH_HOTEL_EVENTO] — PermiteModificarAprovado=true
  - (aprovação) LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE]
  - (aprovação) DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - (aprovação) VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO]
  - (aprovação) PAHL_HOSPEDAGENS "Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS] — PermiteModificarAprovado=true
  - (aprovação) VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO]
  - (aprovação) DATA_INICIO_AUX1 "Data Início da Viagem" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1] — PermiteModificarAprovado=true
  - (aprovação) PAH_DATA_ENTRADA "Data de Entrada no Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA] — PermiteModificarAprovado=true
  - (aprovação) RESERVA_DE_VOO_INTERNACIONAL "Informações para Reserva de Voo - Internacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL] — PermiteModificarAprovado=true
  - (aprovação) PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO] — PermiteModificarAprovado=true
  - (aprovação) PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO] — PermiteModificarAprovado=true
  - (aprovação) MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO]
  - (aprovação) VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - (aprovação) PAH_MOTIVO_SOL "Motivo da Solicitação" [DropDownList String → CPE_CSC.PAH_MOTIVO_SOL] — PermiteModificarAprovado=true
  - (aprovação) RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA]
  - aprovador: Diretor do Favorecido (Unico)

### [369132] SubProcesso "Publicação no DOU"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1373; ChamadaAssincrona=true; PassaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=3086; CustomProperty=CARGO_DESLOCAMENTO
  - CustomPropertyId=3087; CustomProperty=FUNCAO_DESLOCAMENTO
  - CustomPropertyId=3088; CustomProperty=DESC_COLABORADOR_DESLOCAMENTO
  - CustomPropertyId=3039; CustomProperty=TIPO_DESLOCAMENTO
  - CustomPropertyId=3043; CustomProperty=CIDADE_ORIGEM
  - CustomPropertyId=3102; CustomProperty=CIDADE_DESTINO_INTERNACIONAL
  - CustomPropertyId=3114; CustomProperty=PAIS
  - CustomPropertyId=3047; CustomProperty=SAIDA
  - CustomPropertyId=3083; CustomProperty=FAVORECIDO_DESLOCAMENTO
  - CustomPropertyId=3085; CustomProperty=MATRICULA_DESLOCAMENTO
  - CustomPropertyId=3053; CustomProperty=RETORNO_DIA
  - CustomPropertyId=3052; CustomProperty=SAIDA_HORA
  - CustomPropertyId=3054; CustomProperty=RETORNO_HORA
  - CustomPropertyId=3062; CustomProperty=VALOR_TOTAL_DIARIA
  - CustomPropertyId=3158; CustomProperty=COTACAO_DOLAR
  - CustomPropertyId=3159; CustomProperty=DIARIA_COTACAO_REAL
  - CustomPropertyId=3045; CustomProperty=OBJETIVO_VIAGEM
  - CustomPropertyId=3945; CustomProperty=NUMERO_NT
- Associação: Ativo=true; FraseAssociacao=Deslocamento a Serviço -> Publicação no DOU; FraseInversaAssociacao=Publicação no DOU <- Deslocamento a Serviço; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=DESLOCAMENTOPUBLIDOU; SeparadorSequencial=. | fonte: Deslocamento a Serviço → alvo: Publicação no DOU

### [369133] Tarefa "Aguardando data valida para pagamento"
Responsável: Responsavel Processo (papel 1378)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno

### [369134] Tarefa "Aprovar valor de atencipação de deslocamento maior que R$5000,00"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVAR>1000
MotivoInterrupcaoSLA: Aguardando Aprovação Gerencial
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação para adiantamento maior que R$5000,00; CopiarAnexados=true; ReutilizaAprovacaoAnterior=true
  - (aprovação) RESERVA_DE_VOO_INTERNACIONAL "Informações para Reserva de Voo - Internacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL] — PermiteModificarAprovado=true
  - (aprovação) QUANTIDADE_DIARIA "Quantidade de Diárias" [TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA]
  - (aprovação) COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR]
  - (aprovação) VALOR_REF_REDUZIDA "Valor Refeição Reduzida" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA]
  - (aprovação) TIPO_HOSPEDAGEM "Tipo de Hospedagem" [DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM]
  - (aprovação) DIARIA_AUTORIZADO_INTERNACIONAL "Valor Diária Autorizado US$" [TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL]
  - (aprovação) SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA]
  - (aprovação) RESERVA_DE_VOO "Informações da Reserva de Voo - Nacional" [DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO] — PermiteModificarAprovado=true
  - (aprovação) VALOR_DIARIA "Valor da Diaria R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA]
  - (aprovação) LISTA_INVIABILIDADE "Lista de Motivos que inviabilizam a videoconferência" [DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE]
  - (aprovação) DIAS_DE_TRA "Dias em Deslocamento" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - (aprovação) PAHL_PASSAGENS "Passagens Aéreas" [CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS] — PermiteModificarAprovado=true
  - (aprovação) PREVISAO_DISTANCIA_KM "Previsão de distancia em KM" [TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM]
  - (aprovação) OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM]
  - (aprovação) RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA]
  - (aprovação) PAH_VOUCHER_HOSPEDAGEM "Voucher de Hospedagem" [TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM] — PermiteModificarAprovado=true
  - (aprovação) PARCELA_COMPLEMENTAR "Parcela Complementar de hospedagem" [TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR]
  - (aprovação) PAHL_LOCACOES "Locações" [CheckBox Boolean → CPE_CSC.PAHL_LOCACOES] — PermiteModificarAprovado=true
  - (aprovação) SIM_NAO "Estará acompanhado Gerente Executivo / Gerente de Projeto I / Assesor Executivo / Superintendente?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - (aprovação) FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO]
  - (aprovação) CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM]
  - (aprovação) FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO]
  - (aprovação) VALOR_TOTAL_REFEICAO "Valor total previsto para refeições: R$" [TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO]
  - (aprovação) TIPO_DESTINO "Tipo da localidade de destino" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO]
  - (aprovação) CIDADE_DESTINO "Cidade de Destino" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO]
  - (aprovação) VALOR_TOTAL_DIARIA "Valor Total Diária:" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA]
  - (aprovação) VALOR_DIARIA_DOLAR "Valor Diária US$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR]
  - (aprovação) PAH_HOTEL_EVENTO "Hotel do Evento" [TextBox String → CPE_CSC.PAH_HOTEL_EVENTO] — PermiteModificarAprovado=true
  - (aprovação) TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO]
  - (aprovação) MEIO_LOCOMOCAO "Meio de locomoção principal" [DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO]
  - (aprovação) DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL]
  - (aprovação) MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO]
  - (aprovação) CAMPO_VALIDACAO_DOLAR "Diária máxima autorizada US$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR]
  - (aprovação) PAH_LOCALIZADORES "Localizador Aereo" [DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES] — PermiteModificarAprovado=true
  - (aprovação) CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO]
  - (aprovação) CIDADE_DESTINO_INTERNACIONAL "Cidade/País de Destino" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL]
  - (aprovação) RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA]
  - (aprovação) DATA_INICIO_AUX1 "Data Início da Viagem" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1] — PermiteModificarAprovado=true
  - (aprovação) SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA]
  - (aprovação) PAH_MOTIVO_SOL "Motivo da Solicitação" [DropDownList String → CPE_CSC.PAH_MOTIVO_SOL] — PermiteModificarAprovado=true
  - (aprovação) DESCRICAO_DESPESAS "Descrição de outras despesas (Preencher com "NA" caso não tenha) " [TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS]
  - (aprovação) DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO]
  - (aprovação) VALOR_TOTAL_ADIANTAMENTO "Valor total do adiantamento R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO]
  - (aprovação) VALOR_DISTANCIA "Valor previsto para percorrer distância R$" [TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA]
  - (aprovação) PAH_EVENTO_HOTEL "Evento no Hotel?" [DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL] — PermiteModificarAprovado=true
  - (aprovação) PAHL_VOUCHER_CARRO "Voucher de Locação de Carro" [TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO] — PermiteModificarAprovado=true
  - (aprovação) PAHL_LOCACOES_CARRO "Locações de Carro" [DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO] — PermiteModificarAprovado=true
  - (aprovação) VALOR_REF_INTEGRAL "Valor Refeição Integral" [TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL]
  - (aprovação) PAH_DATA_SAIDA "Data de Saída do Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA] — PermiteModificarAprovado=true
  - (aprovação) QTD_REFEICAO_INTEGRAL "Quantidade de Refeições Integrais" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL]
  - (aprovação) CAMPO_VALIDACAO_DIARIA "Diária máxima autorizada R$ (TAB320-373)" [TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA]
  - (aprovação) VALOR_DIARIA_AUTORIZADO "Valor Diária Autorizado" [TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO]
  - (aprovação) QTD_REFEICAO_REDUZIDA "Quantidade de refeições reduzidas" [TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA]
  - (aprovação) VALOR_DESPESAS "Valor de outras despesas R$ (preencher com "0" caso não tenha)" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS]
  - (aprovação) PAIS "País de Destino" [DropDownList String → CPE_DESLOCAMENTO.PAIS]
  - (aprovação) PAHL_HOSPEDAGENS "Hospedagens" [CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS] — PermiteModificarAprovado=true
  - (aprovação) ACOMPANHANDO_GRUPO_A "Estará acompanhando Presidente / Diretor / Conselheiro " [DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A]
  - (aprovação) CSC_OBS "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS] — PermiteModificarAprovado=true
  - (aprovação) NUM_ABERTURA_CHAMADO "N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando" [TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO]
  - (aprovação) PAH_DATA_ENTRADA "Data de Entrada no Hotel" [DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA] — PermiteModificarAprovado=true
  - (aprovação) TOTAL_COMPLEMENTAR "Total Parcela Complementar (Não é necessário prestar contas)" [TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR]
  - aprovador: Gerente de Divisão de Cliente (Unico)

### [369135] SubProcesso "Realizar Prestação de Contas"
Responsável: Responsavel Processo (papel 1378)
Config: AssociacaoId=765; ChamadaAssincrona=true; PassaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=481; CustomProperty=TELEFONE_CLIENTE
  - CustomPropertyId=1702; CustomProperty=PAHL_NUM_ARGO
  - CustomPropertyId=1357; CustomProperty=CSC_DATA_INICIO
  - CustomPropertyId=1358; CustomProperty=CSC_DATA_FIM
  - CustomPropertyId=1369; CustomProperty=CSC_VALOR1_TOTAL
  - CustomPropertyId=3099; CustomProperty=RESERVA_DE_VOO_INTERNACIONAL
  - CustomPropertyId=1353; CustomProperty=PAH_DATA_ENTRADA
  - CustomPropertyId=1354; CustomProperty=PAH_DATA_SAIDA
  - CustomPropertyId=1352; CustomProperty=PAH_EVENTO_HOTEL
  - CustomPropertyId=1355; CustomProperty=PAH_HOTEL_EVENTO
  - CustomPropertyId=1488; CustomProperty=PAHL_VOUCHER_CARRO
  - CustomPropertyId=1489; CustomProperty=PAHL_LOCACOES_CARRO
  - CustomPropertyId=580; CustomProperty=DESCRICAO_OBRIG
  - CustomPropertyId=1350; CustomProperty=CSC_OBS
  - CustomPropertyId=1368; CustomProperty=CSC_VALOR1
  - CustomPropertyId=1495; CustomProperty=CSC_VALOR2
  - CustomPropertyId=1362; CustomProperty=CSC_OBS1
  - CustomPropertyId=3083; CustomProperty=FAVORECIDO_DESLOCAMENTO
  - CustomPropertyId=3085; CustomProperty=MATRICULA_DESLOCAMENTO
  - CustomPropertyId=3086; CustomProperty=CARGO_DESLOCAMENTO
  - CustomPropertyId=3087; CustomProperty=FUNCAO_DESLOCAMENTO
  - CustomPropertyId=3088; CustomProperty=DESC_COLABORADOR_DESLOCAMENTO
  - CustomPropertyId=350; CustomProperty=CELULAR
  - CustomPropertyId=3127; CustomProperty=ACOMPANHANDO_GRUPO_A
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
  - CustomPropertyId=3125; CustomProperty=NUM_ABERTURA_CHAMADO
  - CustomPropertyId=3039; CustomProperty=TIPO_DESLOCAMENTO
  - CustomPropertyId=3043; CustomProperty=CIDADE_ORIGEM
  - CustomPropertyId=3044; CustomProperty=CIDADE_DESTINO
  - CustomPropertyId=3102; CustomProperty=CIDADE_DESTINO_INTERNACIONAL
  - CustomPropertyId=897; CustomProperty=DATA_INICIO_AUX1
  - CustomPropertyId=3114; CustomProperty=PAIS
  - CustomPropertyId=3046; CustomProperty=TIPO_DESTINO
  - CustomPropertyId=3047; CustomProperty=SAIDA
  - CustomPropertyId=3053; CustomProperty=RETORNO_DIA
  - CustomPropertyId=3052; CustomProperty=SAIDA_HORA
  - CustomPropertyId=3054; CustomProperty=RETORNO_HORA
  - CustomPropertyId=2255; CustomProperty=DIAS_DE_TRA
  - CustomPropertyId=3056; CustomProperty=TIPO_HOSPEDAGEM
  - CustomPropertyId=3059; CustomProperty=QUANTIDADE_DIARIA
  - CustomPropertyId=3128; CustomProperty=VALOR_DIARIA_DOLAR
  - CustomPropertyId=3132; CustomProperty=CAMPO_VALIDACAO_DOLAR
  - CustomPropertyId=3131; CustomProperty=DIARIA_AUTORIZADO_INTERNACIONAL
  - CustomPropertyId=3061; CustomProperty=VALOR_DIARIA
  - CustomPropertyId=3116; CustomProperty=VALOR_DIARIA_AUTORIZADO
  - CustomPropertyId=3117; CustomProperty=CAMPO_VALIDACAO_DIARIA
  - CustomPropertyId=3062; CustomProperty=VALOR_TOTAL_DIARIA
  - CustomPropertyId=3158; CustomProperty=COTACAO_DOLAR
  - CustomPropertyId=3159; CustomProperty=DIARIA_COTACAO_REAL
  - CustomPropertyId=3338; CustomProperty=PARCELA_COMPLEMENTAR
  - CustomPropertyId=3341; CustomProperty=TOTAL_COMPLEMENTAR
  - CustomPropertyId=3041; CustomProperty=LISTA_INVIABILIDADE
  - CustomPropertyId=3045; CustomProperty=OBJETIVO_VIAGEM
  - CustomPropertyId=3055; CustomProperty=MEIO_LOCOMOCAO
  - CustomPropertyId=807; CustomProperty=NUMERO_OC
  - CustomPropertyId=907; CustomProperty=NUMERO_DA_OC
  - CustomPropertyId=3076; CustomProperty=PREVISAO_DISTANCIA_KM
  - CustomPropertyId=3077; CustomProperty=VALOR_DISTANCIA
  - CustomPropertyId=3071; CustomProperty=QTD_REFEICAO_REDUZIDA
  - CustomPropertyId=3945; CustomProperty=NUMERO_NT
  - CustomPropertyId=3110; CustomProperty=VALOR_TOTAL_REFEICAO
  - CustomPropertyId=3150; CustomProperty=VALOR_REF_REDUZIDA
  - CustomPropertyId=3072; CustomProperty=QTD_REFEICAO_INTEGRAL
  - CustomPropertyId=161; CustomProperty=CPF
  - CustomPropertyId=781; CustomProperty=SCR_PRESTADOR
  - CustomPropertyId=484; CustomProperty=EMAIL_CLIENTE
  - CustomPropertyId=3151; CustomProperty=VALOR_REF_INTEGRAL
  - CustomPropertyId=3073; CustomProperty=DESCRICAO_DESPESAS
  - CustomPropertyId=3075; CustomProperty=VALOR_DESPESAS
  - CustomPropertyId=3078; CustomProperty=VALOR_TOTAL_ADIANTAMENTO
  - CustomPropertyId=4675; CustomProperty=SIM_NAO_REFEICAO
  - CustomPropertyId=1485; CustomProperty=PAHL_PASSAGENS
  - CustomPropertyId=1486; CustomProperty=PAHL_HOSPEDAGENS
  - PropertyId=1296; Property=Favorecido
  - CustomPropertyId=1487; CustomProperty=PAHL_LOCACOES
  - CustomPropertyId=1351; CustomProperty=PAH_MOTIVO_SOL
  - CustomPropertyId=1385; CustomProperty=PAH_LOCALIZADORES
  - CustomPropertyId=4862; CustomProperty=CIDADE_CLASSIFICACAO
  - CustomPropertyId=1347; CustomProperty=PAH_VOUCHER_HOSPEDAGEM
  - CustomPropertyId=1349; CustomProperty=RESERVA_DE_VOO
- Associação: Ativo=true; FraseAssociacao=Deslocamento a Serviço > Prestação de Contas; FraseInversaAssociacao=Prestação de Contas > Deslocamento a Serviço; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=DESLOCAMENTO; SeparadorSequencial=. | fonte: Deslocamento a Serviço → alvo: Prestação de Contas - Deslocamento

### [369140] EventoIntermediarioMensagem "Configurar ponto eletrônico"
Config: ListaDestinatarios=jornadadetrabalho@bbts.com.br
ModeloComunicado: Deslocamento a Serviço - Ponto Eletrônico
Corpo do comunicado: Prezados,
Solicitamos a configuração do perfil de ponto eletrônico do colaborador abaixo relacionado, em virtude de deslocamento a serviço:
Matrícula: OrdemServico.Customizado.MATRICULA_DESLOCAMENTO 
Nome Completo: OrdemServico.Customizado.FAVORECIDO_DESLOCAMENTO 
Período da viagem:
Data de início: OrdemServico.Customizado.SAIDA 
Data de término: OrdemServico.Customizado.RETORNO_DIA

## Papéis usados
### papel 508: Fila CSC - Passagens Aéreas e Hospedagem
Tipo=RelacaoPessoas | pessoas: Fila CSC - Passagens Aéreas e Hospedagem
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
### papel 1021: Cliente e Favorecido Deslocamento
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Favorecido Deslocamento (Script)
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 461: Fila CSC - Pendente de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação
### papel 1172: Aprovação Viagem e Hospedagem - Conforme NI006v.87
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
#favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.FavorecidoId))
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla

gestorPosicao = ""
if (cargoFavorecido == "PRESIDENTE" or cargoFavorecido == "DIRETOR" or cargoFavorecido == "ASSESSOR EXECUTIVO PRESIDENCIA" or cargoFavorecido == "MEMBRO COMITE DE AUDITORIA" or cargoFavorecido == "CONSELHEIRO DE ADMINISTRACAO" or cargoFavorecido == "CONSELHEIRO FISCAL") or (cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000009200" or orgaoFavorecido == "3000001330" or orgaoFavorecido == "3000009400" or orgaoFavorecido == "3000004052") or (cargoFavorecido == "GERENTE DE PROJETOS I" and orgaoFavorecido == "3000004051" or orgaoFavorecido == "3000004055"):
    uor = Orgao.Carrega("Sigla", "3000009430")
    gestor = uor.Gestor
    aprovador = gestor
#Disec aprovar viagem do Gerente Executivo Gesap
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000003402":
#        uor = Orgao.Carrega("Sigla", "3000009430")
#        gestor = uor.Gestor
#        aprovador = gestor
##Disup aprovar viagem do Gerente Executivo Gesuc
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000003401":
#        uor = Orgao.Carrega("Sigla", "3000003410")
#        gestor = uor.Gestor
#        aprovador = gestor
##UNIBBTS aprovar viagem do Gerente Executivo Gepes
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000003200":
#        uor = Orgao.Carrega("Sigla", "3000003260")
#        gestor = uor.Gestor
#        aprovador = gestor
##Dipav aprovar viagem do Gerente Executivo Gefic
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000003100":
#        uor = Orgao.Carrega("Sigla", "3000009350")
#        gestor = uor.Gestor
#        aprovador = gestor
##Supot aprovar viagem do Gerente Executivo Geape
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000008810":
#        uor = Orgao.Carrega("Sigla", "3000002050")
#        gestor = uor.Gestor
#        aprovador = gestor 
##Detic aprovar viagem do Gerente Executivo Getic
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000002026":
#        uor = Orgao.Carrega("Sigla", "3000002033")
#        gestor = uor.Gestor
#        aprovador = gestor 
##Govit aprovar viagem do Gerente Executivo Geati
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000008800":
#        uor = Orgao.Carrega("Sigla", "3000008406")
#        gestor = uor.Gestor
#        aprovador = gestor
##Difas aprovar viagem do Gerente Executivo Gesed
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "2000008422":
#        uor = Orgao.Carrega("Sigla", "2000008260")
#        gestor = uor.Gestor
#        aprovador = gestor       
##Diarc aprovar viagem do Gerente Executivo Gecob
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "2000008100":
#        uor = Orgao.Carrega("Sigla", "2000008109")
#        gestor = uor.Gestor
#        aprovador = gestor
##Diarb aprovar viagem do Gerente Executivo Gecor
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "2000008310":
#        uor = Orgao.Carrega("Sigla", "2000008310")
#        gestor = uor.Gestor
#        aprovador = gestor       
##Dipre aprovar viagem do Gerente Executivo Gelop
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "2000008310":
#        uor = Orgao.Carrega("Sigla", "2000008310")
#        gestor = uor.Gestor
#        aprovador = gestor              
##Dires aprovar viagem do Gerente Executivo Gered
#elif cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "2000004017":
#        uor = Orgao.Carrega("Sigla", "2000004019")
#        gestor = uor.Gestor
#        aprovador = gestor

else:
    if cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "4000001110":
        uor = Orgao.Carrega("Sigla", "4000001112")
        gestor = uor.Gestor
        aprovador = gestor
#Demais casos, gestor imediato aprova OS do seu subordinado        
    else:
        gestorid = favorecido.Orgao.GestorId
        gestor = favorecido.Orgao.Gestor
        if gestorid == favorecido.Id:
            gestor = favorecido.Orgao.OrgaoPai.Gestor
        aprovador = gestor
        
        Utils.LogInformation("Valor de gestorid: "+gestorid.ToString()+" valor de gestor: "+gestor.ToString()+"valor de favorecidoid: "+favorecido.Id.ToString()+"favorecido cargo: "+cargoFavorecido.ToString()+"favorecido sigla: "+orgaoFavorecido.ToString(),"DEBUG")
Atores.Adiciona(aprovador, "Aprovação Viagem e Hospedagem - Conforme NI006v.87")
```
### papel 145: Diretor do Favorecido
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Favorecido.Orgao.Gestor
gestorAreaPai = OrdemServico.Favorecido.Orgao.OrgaoPai.Sigla

#Adiciona o Presidente como aprovador de solicitações com a area PAI Presidente
#if OrdemServico.Favorecido.Orgao.Sigla == "4000001300":
#    gestor = Pessoa.Carrega(27818) #ID do Presidente
#    Atores.Adiciona(gestor, "Diretor de " + OrdemServico.Cliente.ToString())

#Variável de Controle do Loop infinito
countLoop = 0;

#Loop da busca do Gerente Executivo do Favorecido
#while (((gestor.Orgao.OrgaoPai.Descricao != "4000001300- PRESIDENCIA.")) and countLoop < 6):
#while (((gestor.Orgao.OrgaoPai.Sigla != "4000001300")) and countLoop < 6):
while (((gestor.Orgao.OrgaoPai.Sigla != "4000001300") and (gestor.Orgao.OrgaoPai.Sigla != "4000001100")) and countLoop < 6):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    countLoop = countLoop + 1
    
if (countLoop >= 6):
    Utils.LogError("SAIDA DO LOOP - PAPEL DIRETOR", "ERROR")
    
#Adiciona o Presidente como aprovador de solicitações com a area PAI Presidente
if gestorAreaPai == "4000001300":
    gestor = Pessoa.Carrega(27818) #ID do Presidente
    
Atores.Adiciona(gestor, "Diretor de " + OrdemServico.Cliente.ToString())
```
### papel 338: Gerente de Divisão de Cliente
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Cliente.Orgao.Gestor
#Variável de Controle do Loop infinito
countLoop = 0
#Loop da busca do Gerente
#while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao == "Gerência Divisão")) and countLoop < 6):
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Gerência Executiva") and countLoop < 6):
#    aux=0
    if gestor['CARGO_FUNCIONAL'].ToString() == "COORDENADOR" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE DIVISAO" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE REGIONAL DE OPERACOES" or gestor['CARGO_FUNCIONAL'].ToString() == "SUPERINTENDENTE" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE PROJETOS I" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE PROJETOS II" :
        gestor = gestor
#        aux=1
        break
    else:
        gestor = gestor.Orgao.OrgaoPai.Gestor
#        
#    countLoop = countLoop + 1
#
#if (countLoop >= 6):
#    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE DE DIVISÃO", "ERROR")
#
#    gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente de Divisão" + OrdemServico.Cliente.ToString())
```

## Campos customizados usados (definição global)

### RETORNO_DIA — Retorno dia
DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA

### TIPO_HOSPEDAGEM — Tipo de Hospedagem
DropDownList String → CPE_DESLOCAMENTO.TIPO_HOSPEDAGEM
Itens: Contratada;Avulsa;Avulsa SEM apresentação de NF;Sem Hospedagem

### QTD_REFEICAO_REDUZIDA — Quantidade de refeições reduzidas
TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_REDUZIDA

### QTD_REFEICAO_INTEGRAL — Quantidade de Refeições Integrais
TextBox Integer → CPE_DESLOCAMENTO.QTD_REFEICAO_INTEGRAL

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### SAIDA_HORA — Horário da Saída
TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA

### RETORNO_HORA — Horário do Retorno
TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA

### FAVORECIDO_DESLOCAMENTO — Favorecido
DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### OBS43 — Observação43
Memo String(900) → CPE_CSC.OBS43

### CIDADE_ORIGEM — Cidade de Origem
DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```

### OBS41 — Observação41
Memo String(900) → CPE_CSC.OBS41

### CIDADE_DESTINO — Cidade de Destino
DropDownList String → CPE_DESLOCAMENTO.CIDADE_DESTINO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```

### OBS42 — Observação42
Memo String(900) → CPE_CSC.OBS42

### OBS44 — Observação44
Memo String(900) → CPE_CSC.OBS44

### OBJETIVO_VIAGEM — Objetivo / Informações Adicionais:
TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM

### SAIDA — Saída dia
DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA

### PAH_DATA_ENTRADA — Data de Entrada
DatePicker DateTime → CPE_CSC.PAH_DATA_ENTRADA

### PAH_DATA_SAIDA — Data de Saída
DatePicker DateTime → CPE_CSC.PAH_DATA_SAIDA

### PAH_EVENTO_HOTEL — Evento no Hotel?
DropDownList String → CPE_CSC.PAH_EVENTO_HOTEL
Descrição: Evento será Realizado no Hotel?
Itens: Sim;Não

### RESERVA_DE_VOO_INTERNACIONAL — Informações para Reserva de Voo Internacional
DataGrid RecordList → Z_00143_RESERVA_DE_VOO_INTERNACIONAL.RESERVA_DE_VOO_INTERNACIONAL
Descrição: Reserva de Voo
Colunas do registro:
- SEQUENCIA "Nº do Trecho" [DropDownList Integer] itens: 1;2;3;4;5;6;7;8;9
- TRECHO "Trecho" [DropDownList String] itens: Ida;Volta
- CIDADE_ORIGEM "Cidade Origem" [TextBox String]
- AEROPORTO_ORIGEM "Aeroporto de Origem" [TextBox String]
- CIDADE_DESTINO "Cidade de Destino" [TextBox String]
- AEROPORTO_DESTINO "Aeroporto de Destino" [TextBox String]
- DATA_VOO "Data do Voo" [DatePicker DateTime]
- HORA_ESTIMADA_VOO "Horário Estimado para Voo" [TextBox String]
- DESPACHO_BAGAGENS "Despacho de Bagagens?" [DropDownList String] itens: Sim;Não
- QUANTIDADE_BAGAGENS "Quantidade de Bagagens" [TextBox Integer]

### CSC_OBS — Observação
Memo String(2000) → CPE_CSC.CSC_OBS

### DATA_INICIO_AUX1 — Início Auxiliar
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_INICIO_AUX1
Descrição: Data de Início Auxiliiar

### PAH_HOTEL_EVENTO — Hotel do Evento
TextBox String → CPE_CSC.PAH_HOTEL_EVENTO
Descrição: Hotel onde será realizado o evento

### PAHL_VOUCHER_CARRO — Voucher de Locação de Carro
TextBox String → CPE_CSC.PAHL_VOUCHER_CARRO

### PAHL_LOCACOES_CARRO — Locações de Carro
DataGrid RecordList → Z_00143_PAHL_LOCACOES_CARRO.PAHL_LOCACOES_CARRO
Colunas do registro:
- CARRO4X4 "4X4 ?" [CheckBox Boolean]
- LOCAL_RETIRADA "Local de Retirada" [TextBox String]
- DATA_HORA_RETIRADA "Data/Hora de Retirada" [DateTimePicker DateTime]
- LOCAL_DEVOLUCAO "Local de Devolução" [TextBox String]
- DATA_HORA_DEVOLUCAO "Data/Hora de Devolução" [DateTimePicker DateTime]
- VALOR_LOCACAO "Valor da Locação" [TextBox Decimal]

### PAH_MOTIVO_SOL — Motivo da Solicitação
DropDownList String → CPE_CSC.PAH_MOTIVO_SOL
Descrição: Tipo de Solicitação de Reserva
Itens: Atendimento técnico;Eventos / Treinamentos;Transferência de Funcionário;Convocação Gerencial;Outros

### PAH_LOCALIZADORES — Localizador Aereo
DataGrid RecordList → Z_00143_PAH_LOCALIZADORES.PAH_LOCALIZADORES
Colunas do registro:
- VALOR_TRECHO "Valor do trecho" [TextBox Decimal]
- SEQUENCIA "Sequência" [DropDownList Integer] itens: 1;2;3;4;5;6;7;8;9
- CIA_AEREA "Companhia Aerea" [DropDownList String] itens: Azul;Gol;Latam;Passaredo
- LOCALIZADOR "Localizador" [TextBox String]

### PAH_VOUCHER_HOSPEDAGEM — Voucher de Hospedagem
TextBox String → CPE_CSC.PAH_VOUCHER_HOSPEDAGEM

### RESERVA_DE_VOO — Informações para Reserva de Voo
DataGrid RecordList → Z_00143_RESERVA_DE_VOO.RESERVA_DE_VOO
Descrição: Reserva de Voo
Colunas do registro:
- TRECHO "Trecho" [DropDownList String] itens: Ida;Volta
- SEQUENCIA "Nº do Trecho" [DropDownList Integer] itens: 1;2;3;4;5;6;7;8;9
- CIDADE_ORIGEM "Cidade Origem" [DropDownList String]
**CIDADE_ORIGEM.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```
- AEROPORTO_DESTINO "Aeroporto de Destino" [TextBox String]
- DESPACHO_BAGAGENS "Despacho de Bagagens?" [DropDownList String] itens: Sim;Não
- QUANTIDADE_BAGAGENS "Quantidade de Bagagens" [TextBox Integer]
- AEROPORTO_ORIGEM "Aeroporto de Origem" [TextBox String]
- CIDADE_DESTINO "Cidade de Destino" [DropDownList String]
**CIDADE_DESTINO.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```
- DATA_VOO "Data do Voo" [DatePicker DateTime]
- HORA_ESTIMADA_VOO "Horário Estimado para Voo" [TextBox String]

### VALOR_DIARIA_DOLAR — Valor Diária US$
TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_DOLAR

### CAMPO_VALIDACAO_DOLAR — Campo de Validação Dolar
TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DOLAR

### DIARIA_AUTORIZADO_INTERNACIONAL — Valor Diária Autorizado US$
TextBox String → CPE_DESLOCAMENTO.DIARIA_AUTORIZADO_INTERNACIONAL

### VALOR_TOTAL_DIARIA — Valor total de diárias R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA

### TOTAL_COMPLEMENTAR — Total Parcela Complementar (Não é necessário prestar contas)
TextBox Decimal → CPE_DESLOCAMENTO.TOTAL_COMPLEMENTAR
Descrição: Total Parcela Complementar

### LISTA_INVIABILIDADE — Lista de Motivos que inviabilizam a videoconferência
DropDownList String → CPE_DESLOCAMENTO.LISTA_INVIABILIDADE
Itens: 0 - Atendimento Técnico;
1 - Auditoria;
2 - Vistoria;
3 - Fiscalização de execução de contrato;
4 - Licitação presencial;
5 - Audiência;
6 - Convocação gerencial;
7 - Saída para compras de material;
8 - Serviços Administrativos (banco, cartório, prefeitura);
9 - Reunião presencial (cliente, fornecedor);
10 - Indisponibilidade de sistema de vídeo conferencia;
11 - Processo interno de seleção;
12 - Contigência;
13 - Plantão;
14 - Manutenção do veículo;
15 - Transferência de Funcionário;
16 - Participação em Projeto

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### NUM_ABERTURA_CHAMADO — N° da Abertura de Chamado do Deslocamento a Serviço de Quem Está Acompanhando
TextBox String → CPE_DESLOCAMENTO.NUM_ABERTURA_CHAMADO

### CIDADE_DESTINO_INTERNACIONAL — Cidade/País de Destino
TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL

### DIAS_DE_TRA — DIAS DE TRAB
TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA
Descrição: DIAS DE TRABALHO

### QUANTIDADE_DIARIA — Quantidade de Diárias
TextBox Integer → CPE_DESLOCAMENTO.QUANTIDADE_DIARIA

### MEIO_LOCOMOCAO — Meio de locomoção principal
DropDownList String → CPE_DESLOCAMENTO.MEIO_LOCOMOCAO
Itens: Avião;Barco;Carro Locado;Carro Próprio;Carro da Frota;Carro por Aplicativo;Metrô;Taxi;Trem;Ônibus Interestadual;Ônibus Intermunicipal;Ônibus Municipal

### TIPO_DESLOCAMENTO — Tipo de Deslocamento
DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO
Itens: Viagem a Serviço - Nacional;Viagem a Serviço - Internacional;Viagem - Assistência Técnica;Treinamento - Assistência Técnica

### VALOR_DISTANCIA — Valor previsto para percorrer distância R$
TextBox String → CPE_DESLOCAMENTO.VALOR_DISTANCIA

### VALOR_DIARIA — Valor da Diaria R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DIARIA

### VALOR_DIARIA_AUTORIZADO — Valor Diária Autorizado
TextBox String → CPE_DESLOCAMENTO.VALOR_DIARIA_AUTORIZADO

### PREVISAO_DISTANCIA_KM — Previsão de distancia em KM
TextBox Decimal → CPE_DESLOCAMENTO.PREVISAO_DISTANCIA_KM

### VALOR_TOTAL_REFEICAO — Valor total previsto para refeições: R$
TextBox String → CPE_ORDEM_SERVICO.VALOR_TOTAL_REFEICAO

### VALOR_REF_REDUZIDA — Valor Refeição Reduzida
TextBox String → CPE_DESLOCAMENTO.VALOR_REF_REDUZIDA

### VALOR_REF_INTEGRAL — Valor Refeição Integral
TextBox String → CPE_DESLOCAMENTO.VALOR_REF_INTEGRAL

### DIARIA_COTACAO_REAL — Diária em Real
TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL

### PARCELA_COMPLEMENTAR — Parcela Complementar de hospedagem
TextBox Decimal → CPE_DESLOCAMENTO.PARCELA_COMPLEMENTAR

### LABEL3 — Texto Informativo
Label String(1024) → CP_ORDEM_SERVICO.LABEL3

### VALOR_DESPESAS — Valor de outras despesas R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_DESPESAS

### VALOR_TOTAL_ADIANTAMENTO — Valor total do adiantamento R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_ADIANTAMENTO

### CARGO_DESLOCAMENTO — Cargo
TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO

### MATRICULA_DESLOCAMENTO — Matrícula
TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO

### COTACAO_DOLAR — Cotação do Dólar americano (USD) 
TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR

### DESCRICAO_DESPESAS — Descrição de outras despesas
TextBox String(1000) → CPE_DESLOCAMENTO.DESCRICAO_DESPESAS

### FUNCAO_DESLOCAMENTO — Função
TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO

### DESC_COLABORADOR_DESLOCAMENTO — Tipo de Colaborador
TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO

### ACOMPANHANDO_GRUPO_A — Estará acompanhando Presidente / Direto / Conselheiro 
DropDownList String → CPE_DESLOCAMENTO.ACOMPANHANDO_GRUPO_A
Itens: Sim;Não

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### PAIS — País
DropDownList String → CPE_DESLOCAMENTO.PAIS
**LookupScript**
```python
#
```

### TIPO_DESTINO — Tipo da localidade de destino
DropDownList String → CPE_DESLOCAMENTO.TIPO_DESTINO
Itens: Capital;Interior

### CAMPO_VALIDACAO_DIARIA — Campo de de validação
TextBox String → CPE_DESLOCAMENTO.CAMPO_VALIDACAO_DIARIA

### PAHL_LOCACOES — Locações
CheckBox Boolean → CPE_CSC.PAHL_LOCACOES
Descrição: Locações de Carro

### PAHL_PASSAGENS — Passagens Aéreas
CheckBox Boolean → CPE_CSC.PAHL_PASSAGENS

### PAHL_HOSPEDAGENS — Hospedagens
CheckBox Boolean → CPE_CSC.PAHL_HOSPEDAGENS

### CELULAR — Celular
TextBox String → CP_ORDEM_SERVICO.CELULAR

### CIDADE_CLASSIFICACAO — Cidade Classificação
TextBox String → CPE_CSC.CIDADE_CLASSIFICACAO

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### NUMERO_NT — Número da Nota Técnica
TextBox String → CPE_CONTRATOS.NUMERO_NT

### VIAGEM_LONGA — Viagem de Longa Distância
DropDownList String → CPE_DESLOCAMENTO.VIAGEM_LONGA
Itens: Até 399km;A partir de 400km

### SIM_NAO_REFEICAO — Sim ou Não Refeição
DropDownList String → CPE_DESLOCAMENTO.SIM_NAO_REFEICAO
Itens: Sim;Não

### TELEFONE_CLIENTE — Ramal do Cliente
TextBox String(300) → CP_ORDEM_SERVICO.TELEFONE_CLIENTE

### SCR_PRESTADOR — UOR
TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR
Descrição: UOR onde está lotado o prestador de serviço

### EMAIL_CLIENTE — Email do Cliente
TextBox String(200) → CP_ORDEM_SERVICO.EMAIL_CLIENTE

### CPF — CPF
TextBox String(15) → CP_ORDEM_SERVICO.CPF

### CSC_RG — RG
TextBox String → CPE_CSC.CSC_RG

### CSC_DATA_NASCIMENTO — Data de nascimento
DatePicker DateTime → CPE_CSC.CSC_DATA_NASCIMENTO

### CSC_DATA_INICIO — Data Início
DatePicker DateTime → CPE_CSC.CSC_DATA_INICIO

### CSC_DATA_FIM — Data Fim
DatePicker DateTime → CPE_CSC.CSC_DATA_FIM

### CSC_VALOR1_TOTAL — Valor Total
TextBox Decimal → CPE_CSC.CSC_VALOR1_TOTAL

### CSC_VALOR2 — Valor
TextBox Decimal → CPE_CSC.CSC_VALOR2

### CSC_OBS1 — Observação/Detalhamento
Memo String(2000) → CPE_CSC.CSC_OBS1
Descrição: Observação

### CSC_VALOR1 — Valor
TextBox Decimal → CPE_CSC.CSC_VALOR1

### PAHL_NUM_ARGO — Número da OS Argo
TextBox String → CPE_CSC.PAHL_NUM_ARGO

## Biblioteca de scripts referenciada
calculos_deslocamento, calculos_deslocamento_v29, teste
(fonte em catalogo/biblioteca/<Nome>.py)
