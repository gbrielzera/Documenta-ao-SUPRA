# Fluxo: Registro de Notas Fiscais de Fornecedores (RECEBIMENTONF1) — versão 27
Caminho: Fluxos > Suprimentos - Contratos Versão 27 Registro de Notas Fiscais de Fornecedores
XML: `XMLs para teste/Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores.xml` | Supravizio 19.1.1 | SubProcessoId 22009 | DesenhoProcessoId 2867 | ProcessoId 151
Órgão dono: 3000003341 - CENTRO DE SERVICOS COMPARTILHADOS DE CONTRATOS | Responsável: ALINE RODRIGUES DE ABREU
Classe do subprocesso: Objetivo=Recebimento de Notas Fiscais de Fornecedores; DescricaoCliente=Registro de Notas Fiscais de Fornecedores; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadoresGrupo; AcessoTotalAdmin=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Atestar Nota Fiscal de Serviço.; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Registro de Despesas e Ressarcimentos (REGDESPERESSARC); Registro de Pagamento Autorizado por Nota Técnica (PAGMENTOSREVENDA); Registro de Nota Fiscal com DGCO - Mercadoria (REGNFCDGCOMERSERSMO); Registro de Nota Fiscal com DGCO - Serviços (REGNFCDGCOSERCMO); Registro de Nota Fiscal com DGCO - SGPS (REGNFDGCOSGPS); Registro de Nota Fiscal sem DGCO (Compras Diretas) (PAGFORNECSEMDGCO)

## Grafo do fluxo
- [352430] LinkInicial "" → [350220] Verificar Insumos Obrigatórios
- [352429] FimCancelamento "Cancelado" → (fim)
- [352426] EventoFinal "Cancelado automaticamente por falta de ajustes" → (fim)
- [350202] EventoIntermediarioMensagem "Cobrança de Insumos Faltantes" → [350210] Resolver pendências (Inserir pausa)
- [350203] LinkInicial "" → [350220] Verificar Insumos Obrigatórios
- [350204] EventoIntermediarioMensagem "Aviso de cancelamento" → [352426] Cancelado automaticamente por falta de ajustes
- [350205] EventoFinal "Sucesso" {Responsável atual} → (fim)
- [350185] SubProcesso "Provisionar - SGPS" {Responsável atual} → [350213] E-mail de nota fiscal lançada com sucesso
- [350211] Tarefa "Provisionar Valores de Verbas Trabalhistas - SGPS" {Responsável atual} → [350185] Provisionar - SGPS
- [350210] Tarefa "Resolver pendências (Inserir pausa)" {Cliente} → [350222]  | [350223]  | [350220] Verificar Insumos Obrigatórios
- [350212] SubProcesso "Fiscalização Administrativa" {Responsável atual} → [350213] E-mail de nota fiscal lançada com sucesso
- [350213] EventoIntermediarioMensagem "E-mail de nota fiscal lançada com sucesso" → [G79063] A NF lançada refere se ao Fornecedor ABR Telecom?
- [350214] Tarefa "Lançamento da Despesa e Reembolso" {Equipe Registro NF} → [350213] E-mail de nota fiscal lançada com sucesso
- [350215] LinkInicial "" → [350220] Verificar Insumos Obrigatórios
- [350216] SubProcesso "Consulta Fisco - Tributária (Estadual, Municipal ou Federal)" {Responsável atual} → [G79053] Qual o tipo de serviço?
- [350217] Tarefa "Lançar Nota Fiscal ERP/RI" {Responsável atual} → [G79051] Qual o tipo de serviço?
- [350188] Tarefa "Aprovar e Liberar Tipo de Lançamento" {Responsável atual} → [G79054] Aprovou?

- [350189] EventoIntermediarioMensagem "Chamado atendido com sucesso" → [350205] Sucesso
- [350186] Tarefa "Verificar Solicitação/Nota Técnica" {Equipe Registro NF} → [350217] Lançar Nota Fiscal ERP/RI
- [350187] Tarefa "Preencher os campos da consulta fisco - tributária" {Responsável atual} → [350216] Consulta Fisco - Tributária (Estadual, Municipal o
- [350219] EventoInicial "Registro de Notas Fiscais de Fornecedores" {Equipe Registro NF} → [350220] Verificar Insumos Obrigatórios
- [350193] Tarefa "Verificar localizado Rio de Janeiro" {Responsável atual} → [G79062] Localizada no Rio?
- [350195] SubProcesso "Fiscalização Administrativa" {Responsável atual} → [350213] E-mail de nota fiscal lançada com sucesso
- [350196] Tarefa "Liberar Tipo de Nota para Lançamento" {Fila Fiscal} → [350186] Verificar Solicitação/Nota Técnica
- [350197] SubProcesso "Baixa de Pagamento de NFS- ABR Telecom" {Responsável atual} → [350189] Chamado atendido com sucesso
- [350198] Tarefa "Consulta ao DIFAL
" {Responsável atual} → [G79052] Insumos básicos ok?
- [350200] EventoIntermediarioMensagem "E-mail " → [352429] Cancelado
- [350220] Tarefa "Verificar Insumos Obrigatórios" {Equipe Registro NF} → [350193] Verificar localizado Rio de Janeiro
- [350221] SubProcesso "Fiscalização Administrativa" {Responsável atual} → [350211] Provisionar Valores de Verbas Trabalhistas - SGPS
- [350222] EventoIntermediarioTimer "" → [350202] Cobrança de Insumos Faltantes
- [350223] EventoIntermediarioTimer "" → [350204] Aviso de cancelamento
- [G79050] Gateway "Qual o tipo de serviço?" → «Outros» [G79055] Qual o tipo de serviço? | «Registro de Nota Fiscal com DGCO - Mercadoria» [350212] Fiscalização Administrativa
- [G79051] Gateway "Qual o tipo de serviço?" → «Nota Técnica» [350189] Chamado atendido com sucesso | «Outros» [G79061] Qual o tipo de serviço?
- [G79052] Gateway "Insumos básicos ok?" → «Sim» [G79065] Há a necessidade de pedir o parecer  fisco-tributá | «Não» [350202] Cobrança de Insumos Faltantes
- [G79053] Gateway "Qual o tipo de serviço?" → «Outros» [G79057] Qual o tipo de demanda? | «Pagamento de Revenda» [350188] Aprovar e Liberar Tipo de Lançamento
- [G79054] Gateway "Aprovou?
" → «Reprovado» [350200] E-mail  | «Aprovado» [350196] Liberar Tipo de Nota para Lançamento
- [G79055] Gateway "Qual o tipo de serviço?" → «Registro de Nota Fiscal com DGCO - Serviços» [350212] Fiscalização Administrativa | «Outros» [G79064] Registro de Notas Fiscal com DGCO - SGPS?
- [G79062] Gateway "Localizada no Rio?" → «Não» [G79052] Insumos básicos ok? | «Sim» [G79059] Verificada Aplicação Difal?

- [G79063] Gateway "A NF lançada refere se ao Fornecedor ABR Telecom?" → «Sim» [350197] Baixa de Pagamento de NFS- ABR Telecom | «Não» [350205] Sucesso
- [G79064] Gateway "Registro de Notas Fiscal com DGCO - SGPS?" → «Não» [350195] Fiscalização Administrativa | «Sim» [350221] Fiscalização Administrativa
- [G79057] Gateway "Qual o tipo de demanda?" → «Despesa e Reembolso» [350214] Lançamento da Despesa e Reembolso | «Outros» [350217] Lançar Nota Fiscal ERP/RI
- [G79059] Gateway "Verificada Aplicação Difal?
" → «Não» [350198] Consulta ao DIFAL
 | «Sim» [G79052] Insumos básicos ok?
- [G79061] Gateway "Qual o tipo de serviço?" → «Registro de Nota Fiscal sem DGCO (Compras Diretas)» [350213] E-mail de nota fiscal lançada com sucesso | «Outros» [G79050] Qual o tipo de serviço?
- [G79065] Gateway "Há a necessidade de pedir o parecer  fisco-tributária?" → «Sim» [350187] Preencher os campos da consulta fisco - tributária | «Não» [G79053] Qual o tipo de serviço?

## Gateways
### [G79050] Qual o tipo de serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "REGNFCDGCOMERSERSMO"
    #Formulario["Outros"].Visivel = True
    #Formulario["Outros"].Habilitado = True
```
- alternativa → [G79055] Qual o tipo de serviço?: OperadorDecision=Equal; ReferenciaDecision=Outros; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [350212] Fiscalização Administrativa: OperadorDecision=Equal; ReferenciaDecision=Registro de Nota Fiscal com DGCO - Mercadoria; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G79051] Qual o tipo de serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "PAGMENTOSREVENDA"
    #Formulario["Outros"].Visivel = True
    #Formulario["Outros"].Habilitado = True
```
- alternativa → [350189] Chamado atendido com sucesso: OperadorDecision=Equal; ReferenciaDecision=Nota Técnica; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G79061] Qual o tipo de serviço?: OperadorDecision=Equal; ReferenciaDecision=Outros; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
### [G79052] Insumos básicos ok? (EventBasedExclusiveDecision)
Codigo=INSBAS
- alternativa → [G79065] Há a necessidade de pedir o parecer  fisco-tributá: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
Sim
```
- alternativa → [350202] Cobrança de Insumos Faltantes: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; RotuloMotivo=Listar documentação/informação faltante:; MotivoObrigatorio=true; PublicarRespostaAA=true
**ValorComparacaoDecision**
```python
Não
```
### [G79053] Qual o tipo de serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "PAGMENTOSREVENDA"
```
- alternativa → [G79057] Qual o tipo de demanda?: OperadorDecision=Equal; ReferenciaDecision=Outros; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [350188] Aprovar e Liberar Tipo de Lançamento: OperadorDecision=Equal; ReferenciaDecision=Pagamento de Revenda; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G79054] Aprovou?
 (DataBasedExclusiveDecision)
Codigo=A
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVV")
```
- alternativa → [350200] E-mail : OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [350196] Liberar Tipo de Nota para Lançamento: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
### [G79055] Qual o tipo de serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "REGNFCDGCOSERCMO"
    #Formulario["Outros"].Visivel = True
    #Formulario["Outros"].Habilitado = True
```
- alternativa → [350212] Fiscalização Administrativa: OperadorDecision=Equal; ReferenciaDecision=Registro de Nota Fiscal com DGCO - Serviços; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G79064] Registro de Notas Fiscal com DGCO - SGPS?: OperadorDecision=Equal; ReferenciaDecision=Outros; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G79062] Localizada no Rio? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["COMBOBOX_III"] == "Sim"
```
- alternativa → [G79052] Insumos básicos ok?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G79059] Verificada Aplicação Difal?
: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G79063] A NF lançada refere se ao Fornecedor ABR Telecom? (EventBasedExclusiveDecision)
Codigo=BAPGNFABRT
- alternativa → [350197] Baixa de Pagamento de NFS- ABR Telecom: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
- alternativa → [350205] Sucesso: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
### [G79064] Registro de Notas Fiscal com DGCO - SGPS? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla
```
- alternativa → [350195] Fiscalização Administrativa: OperadorDecision=NotEqual; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
"REGNFDGCOSGPS"
```
- alternativa → [350221] Fiscalização Administrativa: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
"REGNFDGCOSGPS"
```
### [G79057] Qual o tipo de demanda? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "REGDESPERESSARC"
```
- alternativa → [350214] Lançamento da Despesa e Reembolso: OperadorDecision=Equal; ReferenciaDecision=Despesa e Reembolso; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [350217] Lançar Nota Fiscal ERP/RI: OperadorDecision=Equal; ReferenciaDecision=Outros; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
### [G79059] Verificada Aplicação Difal?
 (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["COMBOBOX_IV"] == "Sim"
```
- alternativa → [350198] Consulta ao DIFAL
: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G79052] Insumos básicos ok?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G79061] Qual o tipo de serviço? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.Servico.Sigla == "PAGFORNECSEMDGCO"
    #Formulario["Outros"].Visivel = True
    #Formulario["Outros"].Habilitado = True
```
- alternativa → [350213] E-mail de nota fiscal lançada com sucesso: OperadorDecision=Equal; ReferenciaDecision=Registro de Nota Fiscal sem DGCO (Compras Diretas); SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G79050] Qual o tipo de serviço?: OperadorDecision=Equal; ReferenciaDecision=Outros; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
### [G79065] Há a necessidade de pedir o parecer  fisco-tributária? (EventBasedExclusiveDecision)
Codigo=FISCO
- alternativa → [350187] Preencher os campos da consulta fisco - tributária: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0; PublicarRespostaAA=true
- alternativa → [G79053] Qual o tipo de serviço?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1

## Atividades

### [352430] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL DE SERVICOS
  - anexo "Nota Fiscal de Serviço" classes: Nota Fiscal de Serviço — ProduzidoTermino=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}
  - FORNECEDOR1 "Fornecedor/Parceiro" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1]
**FORNECEDOR1.ScriptModificado**
```python
Formulario["FORNECEDOR1"].Valor = String.ToUpper(Formulario["FORNECEDOR1"].Valor)
```
  - NATUREZA_SERV "Natureza do serviço" [DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV]
  - QUANTIDADE "Quantidade de Notas Fiscais" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE]
  - VALOR_DA_NOTA_FISCAL "Número(s) da(s) Nota(s) e Valor(es) da(s) Nota(s)" [DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL] — QtdColunasFormulario=1
    - coluna ORGANIZACAO
    - coluna NUMERO_OC obrigatório
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna DATA_DE_VENCIMENTO_NO_RI
    - coluna NUM_ITEM
    - coluna DATA_DE_REGISTRO obrigatório
    - coluna DATA_PGTO
    - coluna CONDICAO_DE_PAGAMENTO
    - coluna NOME_ARQUIVO obrigatório
    - coluna NUMERO_LINHAS obrigatório
    - coluna NUMERO_DO_DOCUMENTO obrigatório
    - coluna CONDICAO_DE_PGTO
    - coluna DATA_DE_REGISTRO_NO_RI
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna VALOR_DO_DOCUMENTO obrigatório
    - coluna MULTA obrigatório
    - coluna NUMERO_RI obrigatório
  - DATA_EMISSAO "Data de emissão (Em caso de mais de uma NF, informar a data da NF que foi emitida primeiro)" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO]
  - DATA_VENCIMENTO "Data de Vencimento (Em caso de mais de uma NF, informar a data da NF que vencerá primeiro)" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]
  - TIPOS_DE_NF "Objeto do documento fiscal" [DropDownList String(50) → CPE_CONTRATOS.TIPOS_DE_NF]
  - JUSTIFICATIVA "Justificativa de abertura de chamado fora do prazo" [TextBox String(1999) → CPE_CSC.JUSTIFICATIVA]
  - SIM_NAO1 "Houve emissão de documento fiscal no período passado?" [DropDownList String → CPE_CSC.SIM_NAO1]
**SIM_NAO1.ScriptModificado**
```python
if Formulario['SIM_NAO1'].Valor == "Sim":
    Formulario['JUSTIFICATIVA1'].Visivel = False
    Formulario['JUSTIFICATIVA1'].Habilitado = False

    
if Formulario['SIM_NAO1'].Valor != "Sim":
    Formulario['JUSTIFICATIVA1'].Visivel = True  
    Formulario['JUSTIFICATIVA1'].Habilitado = True
```
  - JUSTIFICATIVA1 "Motivo da não emissão de documento fiscal" [Memo String → CPE_CSC.JUSTIFICATIVA]
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS EXTRA
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Previdência — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "Documento" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: FGTS — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Benefícios — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Folha Empregados — RequeridoInicial=true; PermiteMultiplosItens=true
- Associação de subprocesso: AssociacaoId=666; Nome=BRUNO ROBERTO OLIVEIRA PRADO; FraseAssociacao=Pré Validação de Faturamento - SGPS -> Registro de Notas Fiscais de Fornecedores

### [352429] FimCancelamento "Cancelado"

### [352426] EventoFinal "Cancelado automaticamente por falta de ajustes"

### [350202] EventoIntermediarioMensagem "Cobrança de Insumos Faltantes"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso sobre a falta de documentos ou informações 2
Corpo do comunicado: Prezado(a),
Solicitamos a inclusão da documentação/informação faltante para que possamos dar continuidade ao tratamento da ordem de serviço OrdemServico.
O prazo para atendimento à solicitação contida neste e-mail é de 5 (cinco) dias úteis. Após este prazo, o chamado será cancelado.
Pendências: 
 Complemento1 
Atenciosamente,
 Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("INSBAS")
```

### [350203] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração
  - anexo "Documento" classes: Anexo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL DE SERVIÇO
  - anexo "Nota Fiscal" classes: Nota Fiscal — ProduzidoTermino=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - DESCRICAO_DETALHADA "Descrição detalhada" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]
  - DATA_EMISSAO "Data da Emissão" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO]
  - DATA_VENCIMENTO "Data do Vencimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]
  - CONTA_CONTABIL1 "Conta Contábil" [TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1]
  - FORNECEDOR01 "Fornecedor" [TextBox String → CPE_CSC.FORNECEDOR01]
  - CSC_UOR_LISTA "UOR" [DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA]
  - NATUREZA_SERV "Natureza do serviço" [DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV]
  - QUANTIDADE "Quantidade" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE]
  - COMBOBOX2 "Tipo Fornecedor" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - VALOR_DA_NOTA_FISCAL "Número(s) da(s) Nota(s) e Valor(es) da(s) Nota(s)" [DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL] — QtdColunasFormulario=1
    - coluna NUM_ITEM
    - coluna DATA_DE_VENCIMENTO_NO_RI
    - coluna CONDICAO_DE_PAGAMENTO
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna NOME_ARQUIVO obrigatório
    - coluna DATA_PGTO
    - coluna ORGANIZACAO
    - coluna NUMERO_OC obrigatório
    - coluna NUMERO_LINHAS obrigatório
    - coluna DATA_DE_REGISTRO_NO_RI
    - coluna NUMERO_DO_DOCUMENTO obrigatório
    - coluna DATA_DE_REGISTRO obrigatório
    - coluna VALOR_DO_DOCUMENTO obrigatório
    - coluna CONDICAO_DE_PGTO
    - coluna MULTA obrigatório
    - coluna NUMERO_RI obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=NFADITAMENTO3
  - anexo "Nota Fiscal do Adiantamento" classes: Modelo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Análise Fisco-Tributária" classes: Análise Fisco-Tributária — RequeridoInicial=true
- Associação de subprocesso: AssociacaoId=1180; Nome=ALINE RODRIGUES DE ABREU; FraseAssociacao=PDPEP -> Registro de Nota Fiscal de Fornecedores

### [350204] EventoIntermediarioMensagem "Aviso de cancelamento"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [350205] EventoFinal "Sucesso"
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
**ScriptFim**
```python
OrdemServico.FinalizadorId = Convert.ToInt32(OrdemServico.ResponsavelId)
```
- Relatorios:
  - FormatoExportacao=PDF

### [350185] SubProcesso "Provisionar - SGPS"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=626
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Servico
listaGrid = OrdemServico.GetCustom("DADOS_LACAMENTO")
for linha in listaGrid.Rows:
    sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)
    #idCliente = OrdemServico.ClienteId
    #sub.Cliente = Pessoa.Carrega(idCliente)
    #sub.Responsavel = Pessoa.Carrega(idCliente)
    #sub.Favorecido = Pessoa.Carrega(idCliente)
    servico = Servico.Carrega(1397)
    sub.Servico = servico
    sub.Assunto = "Provisionar - SGPS"
    sub["ASSUNTO_GUIA"]= OrdemServico["ASSUNTO_GUIA"] #Motivo
    sub["DATA_EFETIVACAO"]= linha["DATA_PAGAMENTO_RI"] #Data Pagamento RI
    sub["DGCO_BB"]= OrdemServico["CSC_DGCO"] 
    sub["NOME_CONTRATO"]= linha["ORGANIZACAO"] #Organização
    sub["NOME_FORNECEDOR"]= OrdemServico["FORNECEDOR1"] #Nome Fornecedor
    sub["NUMERO_NF"]= linha["NUMERO_NOTA_FISCAL"] #Nº Nota (ERP)
    sub["NUMERO_RI"]= linha["NUMERO_RI"] #Numero RI
    sub["VALOR"]= linha["VALOR_NOTA_FISCAL"] #Valor total da NF
    sub["VALOR_TOTAL_PROVISAO"]= linha["VALOR_RETENCAO"] #Valor da provisão
    sub.Salva()
    sub.AvancaAtividade()
```
- ValoresInputs:
  - CustomPropertyId=709; CustomProperty=VALOR
  - CustomPropertyId=3364; CustomProperty=VALOR_TOTAL_PROVISAO
  - CustomPropertyId=760; CustomProperty=ASSUNTO_GUIA
  - CustomPropertyId=537; CustomProperty=DATA_EFETIVACAO
  - CustomPropertyId=1967; CustomProperty=DGCO_BB
  - CustomPropertyId=1916; CustomProperty=NOME_CONTRATO
  - CustomPropertyId=792; CustomProperty=NOME_FORNECEDOR
  - CustomPropertyId=3214; CustomProperty=NUMERO_NF
  - CustomPropertyId=2063; CustomProperty=NUMERO_RI
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1683; ClasseConfiguracao=Nota Fiscal de Serviço
  - SuperClasse=Artefato; ClasseConfiguracaoId=2223; ClasseConfiguracao=Anexo
  - SuperClasse=Artefato; ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1683; ClasseConfiguracao=Nota Fiscal de Serviço
- Associação: Ativo=true; FraseAssociacao=Registro de Nota Fiscal -> Provisão de Verba Tabalhista; FraseInversaAssociacao=Provisão de Verba Tabalhista <- Registro de Nota Fisca; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=REGISTRONOTAFISCAL | fonte: Registro de Notas Fiscais de Fornecedores → alvo: Provisionar - SGPS

### [350211] Tarefa "Provisionar Valores de Verbas Trabalhistas - SGPS"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
gridSolicitacao = OrdemServico.GetCustom("VALOR_DA_NOTA_FISCAL")
gridVerificacao = "DADOS_LACAMENTO"

colunas = ["NUMERO_NOTA_FISCAL", "NUMERO_RI", "VALOR_NOTA_FISCAL", "ORGANIZACAO", "DATA_PAGAMENTO_RI", "VALOR_RETENCAO"]

OrdemServico["DADOS_LACAMENTO"].Rows.Clear()

for dadosSolicitacao in gridSolicitacao.Rows:
    OrdemServico.AdicionaLinhaRegistro(gridVerificacao, colunas, [dadosSolicitacao["NUMERO_NOTA_SERVICO"], dadosSolicitacao["NUM_ITEM"], dadosSolicitacao["VALOR_NOTA_FISCAL_SERVICO"], dadosSolicitacao["ORGANIZACAO"], dadosSolicitacao["DATA_PGTO"]])
    
    #CONDICAO_DE_PGTO
    #DATA_PGTO
    #NUM_ITEM
    #NUMERO_NOTA_SERVICO
    #ORGANIZACAO
    #VALOR_NOTA_FISCAL_SERVICO
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Outros anexos" classes: Arquivo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=NOTAS FISCAIS DE SERVIÇO
  - anexo "Nota Fiscal de Serviço" classes: Nota Fiscal de Serviço — ProduzidoTermino=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Print da Tela de aprovação do SGPS" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - DADOS_LACAMENTO "Dados de Lançamento" [DataGrid RecordList → Z_00143_DADOS_LACAMENTO.DADOS_LACAMENTO] obrigatório
    - coluna NUMERO_RI obrigatório
    - coluna VALOR_RETENCAO obrigatório
    - coluna VALOR_NOTA_FISCAL obrigatório
    - coluna ORGANIZACAO obrigatório
    - coluna DATA_PAGAMENTO_RI obrigatório
    - coluna NUMERO_NOTA_FISCAL obrigatório
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório
  - FORNECEDOR1 "Nome do Fornecedor" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1] obrigatório
  - QUANTIDADE "Quantidade" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE] obrigatório
  - ASSUNTO_GUIA "Motivo" [TextBox String → CP_ORDEM_SERVICO.ASSUNTO_GUIA] obrigatório

### [350210] Tarefa "Resolver pendências (Inserir pausa)"
Responsável: Cliente (papel 18)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTAÇÃO
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "Documentos" classes: Documentos — RequeridoInicial=true; PermiteMultiplosItens=true

### [350212] SubProcesso "Fiscalização Administrativa"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=449; PassaTodosItens=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
OrdemServico.SetCustom("FORNECEDOR1",String.ToUpper(OrdemServico.GetCustom("FORNECEDOR1")))
OrdemServico.Salva
```
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla","FISCADMCONT")
```
  - CustomPropertyId=906; CustomProperty=NATUREZA_SERV
  - CustomPropertyId=874; CustomProperty=QUANTIDADE
  - CustomPropertyId=1902; CustomProperty=VALOR_DA_NOTA_FISCAL
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=510; CustomProperty=FAVORECIDO_TODOS
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=254; CustomProperty=DATA_VENCIMENTO
  - CustomPropertyId=2164; CustomProperty=DESCRICAO_DETALHADA
  - CustomPropertyId=447; CustomProperty=FORNECEDOR1
  - CustomPropertyId=790; CustomProperty=SIGLA_SCR
**ExpressaoValor**
```python
OrdemServico.Servico.Sigla
```
  - CustomPropertyId=253; CustomProperty=DATA_EMISSAO
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- Associação: Ativo=true; FraseAssociacao=Registro de Notas Fiscais de Fornecedores -> Fiscalização Administrativa - Registro de Notas Fiscais; FraseInversaAssociacao=Fiscalização Administrativa - Registro de Notas Fiscais -> Registro de Notas Fiscais de Fornecedores; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=FISCADM; SeparadorSequencial=. | fonte: Registro de Notas Fiscais de Fornecedores → alvo: Fiscalização Administrativa V360 (Uso Exclusivo do CESEC)

### [350213] EventoIntermediarioMensagem "E-mail de nota fiscal lançada com sucesso"
Destinatário: Cliente (papel 18)
Config: ListaDestinatarios=fiscalizacaoadministrativa@bbts.com.br
ModeloComunicado: Chamado atendido com sucesso
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
 Complemento1 
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços

### [350214] Tarefa "Lançamento da Despesa e Reembolso"
Responsável: Equipe Registro NF (papel 140)
- Operação PR0001 Preencher Campos
  - CSC_DATA_RECEBIMENTO "Data do Pagamento" [DatePicker DateTime → CPE_CSC.CSC_DATA_RECEBIMENTO] obrigatório
  - CSC_CEP "Número do RI" [TextBox String → CPE_CSC.CSC_CEP] obrigatório
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS_3 "Responsável pelo tratamento" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_3] obrigatório

### [350215] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0004 Associar Itens Configuração
  - anexo "Documento" classes: Documentos — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] — Configuracao={"Mascara":"00000/0000"}
  - NOME_FORNECEDOR "Fornecedor/Parceiro" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR]
  - NATUREZA_SERV "Natureza do serviço" [DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV]
    - coluna NUMERO obrigatório
    - coluna IDIOMA obrigatório
    - coluna CIDADE obrigatório
    - coluna LOGRADOURO obrigatório
    - coluna ESTADO obrigatório
    - coluna SIGLA_PAIS obrigatório
    - coluna TIPO_LOGRADOURO obrigatório
    - coluna BAIRRO obrigatório
    - coluna NOME_ENDERECO obrigatório
    - coluna PAIS obrigatório
    - coluna CEP obrigatório
    - coluna COMPRA obrigatório
    - coluna PAGAMENTO obrigatório
  - QUANTIDADE "Quantidade" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE]
  - DATA_EMISSAO "Data da Emissão" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO]
  - DATA_VENCIMENTO "Data do Vencimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]
  - VALOR_DA_NF "Número da Nota Fiscal e Valor" [DataGrid RecordList → Z_00143_VALOR_DA_NF.VALOR_DA_NF]
    - coluna NUMERO_RI obrigatório
    - coluna ORGANIZACAO obrigatório
    - coluna NUM_ITEM obrigatório
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna DATA_PGTO obrigatório
    - coluna CONDICAO_DE_PGTO obrigatório
    - coluna MES_DE_REFERENCIA obrigatório
  - OBS1 "Informações Complementares" [Memo String(2000) → CPE_CONTRATOS.OBS1]
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Fiscal de Serviço" classes: Nota Fiscal de Serviço — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Documento" classes: Anexo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "FQ412-066" classes: FQ412-066 — RequeridoInicial=true
- Associação de subprocesso: AssociacaoId=948; Nome=FERNANDO DAU GUEDES; FraseAssociacao=Pré-faturamento mensal - ABR Telecom -> Registro de Notas Fiscais de Fornecedores

### [350216] SubProcesso "Consulta Fisco - Tributária (Estadual, Municipal ou Federal)"
Responsável: Responsável atual (papel 36)
Config: ChamadaAssincrona=true; AssociacaoId=374; RetornaTodosItens=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=254; CustomProperty=DATA_VENCIMENTO
  - CustomPropertyId=1977; CustomProperty=SIM_NAO1
  - CustomPropertyId=1960; CustomProperty=SIM_NAO2
  - CustomPropertyId=858; CustomProperty=OPCAO_DE_CONFIRMACAO
  - CustomPropertyId=860; CustomProperty=DADOS_CONS_NOTA_FISCAL
  - CustomPropertyId=2597; CustomProperty=CONS_NOTA_FISCAL_TIPO_
  - CustomPropertyId=1808; CustomProperty=CSC_CIDADE
  - CustomPropertyId=253; CustomProperty=DATA_EMISSAO
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=1768; ClasseConfiguracao=Nota Técnica
  - SuperClasse=Artefato; ClasseConfiguracaoId=1683; ClasseConfiguracao=Nota Fiscal de Serviço
  - SuperClasse=Artefato; ClasseConfiguracaoId=1685; ClasseConfiguracao=Nota Fiscal
- RetornoItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2178; ClasseConfiguracao=Parecer Tributário
- Associação: Ativo=true; FraseAssociacao=Recebimento de Notas Fiscais de Fornecedores -> Consulta Fisco - Tributária (Estadual, Municipal ou Federal); FraseInversaAssociacao=Consulta Fisco - Tributária (Estadual, Municipal ou Federal) -> Recebimento de Notas Fiscais de Fornecedores; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=CONFISCOTRIBUTARIA; SeparadorSequencial=. | fonte: Registro de Notas Fiscais de Fornecedores → alvo: Consulta Fisco - Tributária (Estadual, Municipal ou Federal)

### [350217] Tarefa "Lançar Nota Fiscal ERP/RI"
Responsável: Responsável atual (papel 36)
Config: Codigo=LANÇARNOTAFISCALERPRI
**ScriptFormCarregado**
```python
#Formulario["RESP_ATEND_DOD"].Itens = DB.ExecuteDataTable("SELECT to_char(p.id_pessoa) id_pessoa, p.nome FROM tecnico tec, pessoa p, grupo_trabalho gt WHERE tec.id_pessoa = p.id_pessoa and gt.id_grupo_trabalho = tec.id_grupo_trabalho AND tec.ativo = 'Sim' and gt.sigla in ('CSCACESSECRJ','CSCFINANCEIRO') ORDER BY p.nome")
#Formulario["RESP_ATEND_DOD"].Itens = DB.ExecuteDataTable("SELECT to_char(p.id_pessoa) id_pessoa, p.nome FROM tecnico tec, pessoa p, grupo_trabalho gt WHERE tec.id_pessoa = p.id_pessoa and gt.id_grupo_trabalho = tec.id_grupo_trabalho AND tec.ativo = 'Sim' and gt.sigla = 'CSCFINANCEIRO' ORDER BY p.nome")

#Formulario["RESP_ATEND_DOD"].Habilitado = True

#for controle in Formulario.Controles:
#    Formulario[controle.Key].Visivel = True
#
#Formulario["VALOR_DA_NF"].Visivel= False
#Formulario["ALCADA1"].Visivel= False
#Formulario["ALCADA2"].Visivel= False
#Formulario["ALCADA3"].Visivel= False
#Formulario["ALCADA4"].Visivel= False
#if OrdemServico.GetCustom("ALCADA1").Rows.Count != 0 or OrdemServico.GetCustom("ALCADA2").Rows.Count != 0 or OrdemServico.GetCustom("ALCADA3").Rows.Count != 0 or OrdemServico.GetCustom("ALCADA4").Rows.Count != 0 :
#    Formulario["VALOR_DA_NF"].Visivel = True
#    
#    if OrdemServico.GetCustom("ALCADA1").Rows.Count != 0 :
#        Formulario["ALCADA1"].Visivel = True
#    if OrdemServico.GetCustom("ALCADA2").Rows.Count != 0 :
#        Formulario["ALCADA2"].Visivel = True
#    if OrdemServico.GetCustom("ALCADA3").Rows.Count != 0 :
#        Formulario["ALCADA3"].Visivel = True
#    if OrdemServico.GetCustom("ALCADA4").Rows.Count != 0 :
#        Formulario["ALCADA4"].Visivel = True
#else:
#    
#    Formulario["VALOR_DA_NF"].Visivel = True
#
```
**ScriptFim**
```python
import clr
import System

clr.AddReference("Supravizio.Custom")

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


#def RegistrarLog(texto):
#    try:
#        OrdemServico.AdicionaComentario(
#            texto,
#            True
#        )
#    except:
#        pass


grid_origem = OrdemServico.GetCustom(
    "VALOR_DA_NF"
)

grid_destino = OrdemServico.GetCustom(
    "VALOR_DA_NOTA_FISCAL"
)

atualizados = 0
ja_iguais = 0
ignorados = 0
erros = 0
detalhes = ""

quantidade_origem = 0
quantidade_destino = 0


try:
    quantidade_origem = grid_origem.Rows.Count
    quantidade_destino = grid_destino.Rows.Count

    quantidade_processar = quantidade_origem

    if quantidade_destino < quantidade_processar:
        quantidade_processar = quantidade_destino


    for indice in range(quantidade_processar):

        try:
            linha_origem = grid_origem.Rows[indice]
            linha_destino = grid_destino.Rows[indice]

            numero_ri = Texto(
                linha_origem["NUMERO_RI"]
            )

            numero_ri_atual = Texto(
                linha_destino["NUMERO_RI"]
            )

            detalhes += (
                "\nLinha {0}: origem NUMERO_RI='{1}'; "
                "destino NUMERO_RI='{2}'."
            ).format(
                indice + 1,
                numero_ri,
                numero_ri_atual
            )


            if numero_ri == "":
                ignorados += 1

                detalhes += (
                    "\nLinha {0}: ignorada porque a origem "
                    "não possui NUMERO_RI."
                ).format(
                    indice + 1
                )

                continue


            if numero_ri_atual != numero_ri:

                linha_destino["NUMERO_RI"] = numero_ri

                atualizados += 1

                detalhes += (
                    "\nLinha {0}: NUMERO_RI atualizado no destino."
                ).format(
                    indice + 1
                )

            else:

                ja_iguais += 1

                detalhes += (
                    "\nLinha {0}: o destino já possuía "
                    "o mesmo NUMERO_RI."
                ).format(
                    indice + 1
                )


        except Exception as exLinha:

            erros += 1

            detalhes += (
                "\nErro na linha {0}: {1}"
            ).format(
                indice + 1,
                Texto(exLinha)
            )


    if quantidade_origem > quantidade_destino:

        detalhes += (
            "\nAviso: a grid VALOR_DA_NF possui {0} linha(s), "
            "mas a grid VALOR_DA_NOTA_FISCAL possui somente {1}. "
            "Foram processadas {2} linha(s)."
        ).format(
            quantidade_origem,
            quantidade_destino,
            quantidade_processar
        )


    if quantidade_destino > quantidade_origem:

        detalhes += (
            "\nAviso: a grid VALOR_DA_NOTA_FISCAL possui {0} linha(s), "
            "mas a grid VALOR_DA_NF possui somente {1}. "
            "As linhas excedentes do destino não foram alteradas."
        ).format(
            quantidade_destino,
            quantidade_origem
        )


    try:
        OrdemServico.Salva()

        detalhes += (
            "\nOS salva após a conferência/atualização "
            "dos números de RI."
        )

    except Exception as exSalva:

        detalhes += (
            "\nAviso: não foi possível executar "
            "OrdemServico.Salva(): {0}"
        ).format(
            Texto(exSalva)
        )


except Exception as ex:

    erros += 1

    detalhes += (
        "\nErro geral ao copiar os números de RI: {0}"
    ).format(
        Texto(ex)
    )


resumo = (
    "Atualização dos números de RI concluída!\n\n"
    "Linhas atualizadas: {0}\n"
    "Linhas que já possuíam o mesmo RI: {1}\n"
    "Linhas ignoradas sem número de RI: {2}\n"
    "Erros: {3}\n"
    "Linhas na origem VALOR_DA_NF: {4}\n"
    "Linhas no destino VALOR_DA_NOTA_FISCAL: {5}\n\n"
    "Detalhes:{6}"
).format(
    atualizados,
    ja_iguais,
    ignorados,
    erros,
    quantidade_origem,
    quantidade_destino,
    detalhes
)

#RegistrarLog(
#    resumo
#)
```
- Operação PR0001 Preencher Campos
  - VALOR_DA_NF "Dados de Lançamento" [DataGrid RecordList → Z_00143_VALOR_DA_NF.VALOR_DA_NF] obrigatório — FormaEdicaoWeb=JanelaPopup; Coluna=2
    - coluna NUMERO_RI obrigatório
    - coluna DATA_DE_PAGAM obrigatório
    - coluna NUMERO_DA_NF obrigatório
    - coluna NUMERO_OC obrigatório
    - coluna NUMERO_LINHAS obrigatório
    - coluna DATA_DE_REGISTRO_NO_RI obrigatório
    - coluna NOME_ARQUIVO obrigatório
    - coluna CONDICAO_DE_PGTO obrigatório
    - coluna DATA_DE_REGISTRO obrigatório
    - coluna DATA_DE_VENCIMENTO_NO_RI obrigatório
    - coluna CONDICAO_DE_PAGAMENTO obrigatório
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna NUM_ITEM obrigatório
    - coluna VALOR_NF obrigatório
    - coluna DATA_PGTO obrigatório
    - coluna NUMERO_DO_RI obrigatório
    - coluna MULTA obrigatório
    - coluna ORGANIZACAO obrigatório
    - coluna MES_DE_REFERENCIA obrigatório

### [350188] Tarefa "Aprovar e Liberar Tipo de Lançamento"
Responsável: Responsável atual (papel 36)
Config: Codigo=APROVV
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Entrada de Nota Fiscal de Revenda; CopiarAnexados=true; MinimoAprovadores=1; ReprovarImediato=true; ObrigatoriedadeMotivo=Todas
  - (aprovação) QUANTIDADE "Quantidade" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE]
  - (aprovação) VALOR_DA_NOTA_FISCAL "Valor(es) da(s) Nota(s)" [DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL] — PermiteModificarAprovado=true
  - (aprovação) FORNECEDOR2 "Fornecedor" [TextBox String → CPE_CSC.FORNECEDOR2]
  - (aprovação) DescricaoDetalhada (nativo) "Informações Adicionais"
  - (aprovação) DATA_VENCIMENTO "Data do Vencimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]
  - (aprovação) CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO]
  - (aprovação) SALDO_NOTA_TECNICA "Descritivo do Saldo da Nota Técnica" [DataGrid RecordList → Z_00143_SALDO_NOTA_TECNICA.SALDO_NOTA_TECNICA]
  - (aprovação) DATA_EMISSAO "Data da Emissão" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO]
  - item para aprovação ""
  - item para aprovação ""
  - item para aprovação ""
  - aprovador: Difin (Unico)

### [350189] EventoIntermediarioMensagem "Chamado atendido com sucesso"
Destinatário: Cliente (papel 18)
Config: ListaDestinatarios=fiscalizacaoadministrativa@bbts.com.br;flavia.souza@bbts.com.br;bruno.prado@bbts.com.br;contasapagar@bbts.com.br
ModeloComunicado: Chamado atendido com sucesso
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
 Complemento1 
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços

### [350186] Tarefa "Verificar Solicitação/Nota Técnica"
Responsável: Equipe Registro NF (papel 140)
MotivoInterrupcaoSLA: Aguardando Ação do Cliente Interno
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS_3 "Responsável pelo tratamento" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_3] obrigatório

### [350187] Tarefa "Preencher os campos da consulta fisco - tributária"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
#Formulario["DADOS_CONS_NOTA_FISCAL"].Visivel= True
#Formulario["DADOS_CONS_NOTA_FISCAL"].Habilitado= True
if Formulario["SIM_NAO1"].Valor == 'Sim':    
    Formulario["SIM_NAO2"].Visivel = True    
    Formulario["SIM_NAO2"].Habilitado = True    
if Formulario["SIM_NAO1"].Valor != 'Sim':    
    Formulario["SIM_NAO2"].Visivel = False    
    Formulario["SIM_NAO2"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - SIM_NAO2 "Tem contrato?" [DropDownList String → CPE_CSC.SIM_NAO2] obrigatório
**SIM_NAO2.ScriptModificado**
```python
if Formulario["SIM_NAO1"].Valor == 'Sim': 
    Formulario["SIM_NAO2"].Visivel = True
    Formulario["SIM_NAO2"].Habilitado = True   
if Formulario["SIM_NAO1"].Valor != 'Sim':   
    Formulario["SIM_NAO2"].Visivel = False     
    Formulario["SIM_NAO2"].Habilitado = False
```
  - DADOS_CONS_NOTA_FISCAL "Dados para Consulta de Nota Fiscal" [DataGrid RecordList → Z_00143_DADOS_CONS_NOTA_FISCAL.DADOS_CONS_NOTA_FISCAL] obrigatório
    - coluna RAZAO_SOCIAL_FORNECEDOR obrigatório
    - coluna OBJETO_NOTA_FISCAL obrigatório
    - coluna LOCAL_PAGAMENTO obrigatório
    - coluna LOCAL_EMISSAO obrigatório
    - coluna CNPJ obrigatório
    - coluna NUMERO_NOTA_FISCAL obrigatório
    - coluna LOCAL_PRESTACAO_SERVICO obrigatório
  - CONS_NOTA_FISCAL_TIPO_ "Selecione uma opção a respeito da nota fiscal:" [DropDownList String → CPE_TIP_SOL01.CONS_NOTA_FISCAL_TIPO_] obrigatório
  - CSC_CIDADE "Local da entrada da NF (Cidade/UF da BBTS):" [TextBox String(500) → CPE_CSC.CSC_CIDADE] obrigatório
  - SIM_NAO1 "O lançamento vai gerar pagamento a fornecedor?" [DropDownList String → CPE_CSC.SIM_NAO1] obrigatório
**SIM_NAO1.ScriptModificado**
```python
if Formulario["SIM_NAO1"].Valor == 'Sim': 
    Formulario["SIM_NAO2"].Visivel = True
    Formulario["SIM_NAO2"].Habilitado = True   
if Formulario["SIM_NAO1"].Valor != 'Sim':   
    Formulario["SIM_NAO2"].Visivel = False     
    Formulario["SIM_NAO2"].Habilitado = False
```
  - OPCAO_DE_CONFIRMACAO "Documento Existente" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO] obrigatório

### [350219] EventoInicial "Registro de Notas Fiscais de Fornecedores"
Responsável: Equipe Registro NF (papel 140)
TipoSolicitacao: 30.04. Suprimentos Corporativos, Licitações e Contratos - Recebimento de de documentos para pagamento de Fornecedores
**ScriptFormCarregado**
```python
Formulario["CSC_MATRICULA"].Visivel = False
Formulario["CSC_MATRICULA"].Habilitado = False
Formulario["CSC_NOTA_FISCAL"].Visivel = False
Formulario["CSC_NOTA_FISCAL"].Habilitado = False
Formulario["TEXT"].Visivel = False


if (OrdemServico.Servico.Sigla == "PAGMENTOSREVENDA"):
    Formulario["NATUREZA_SERV"].Visivel = False
    Formulario["NATUREZA_SERV"].Habilitado = False 
    Formulario["SALDO_NOTA_TECNICA"].Visivel = True
    Formulario["SALDO_NOTA_TECNICA"].Habilitado = True
    #Formulario["VALOR_DO_DOCUMENTO"].Visivel = False
    #Formulario["VALOR_DO_DOCUMENTO"].Habilitado = False
    Formulario["LABEL57"].Visivel = True
    Formulario["LABEL57"].Habilitado = True
    Formulario["CSC_NOTA_FISCAL"].Visivel = True
    Formulario["CSC_NOTA_FISCAL"].Habilitado = True
    Formulario["TEXT"].Visivel = True
    
if (OrdemServico.Servico.Sigla != "PAGMENTOSREVENDA"):
    Formulario["SALDO_NOTA_TECNICA"].Visivel = False
    Formulario["SALDO_NOTA_TECNICA"].Habilitado = False
    #Formulario["VALOR_DO_DOCUMENTO"].Visivel = False
    #Formulario["VALOR_DO_DOCUMENTO"].Habilitado = False
    
if (OrdemServico.Servico.Sigla == "PAGFORNECSEMDGCO"):
    Formulario["CSC_DGCO"].Visivel = False
    Formulario["CSC_DGCO"].Habilitado = False
    #Formulario["VALOR_DO_DOCUMENTO"].Visivel = False
    #Formulario["VALOR_DO_DOCUMENTO"].Habilitado = False
    Formulario["LABEL57"].Visivel = False
    Formulario["LABEL57"].Habilitado = False
    Formulario["CSC_MATRICULA"].Visivel = False
    Formulario["CSC_MATRICULA"].Habilitado = False
    Formulario["CSC_NOTA_FISCAL"].Visivel = False
    Formulario["CSC_NOTA_FISCAL"].Habilitado = False
    Formulario["CSC_NUM_SISLOC"].Visivel = False
    Formulario["CSC_NUM_SISLOC"].Habilitado = False
    
if (OrdemServico.Servico.Sigla == "REGDESPERESSARC"):
    Formulario["DATA_EMISSAO"].Visivel = False
    Formulario["DATA_EMISSAO"].Habilitado = False
    Formulario["DATA_VENCIMENTO"].Visivel = True
    Formulario["DATA_VENCIMENTO"].Habilitado = True
    Formulario["NATUREZA_SERV"].Visivel = False
    Formulario["NATUREZA_SERV"].Habilitado = False
    Formulario["CSC_DGCO"].Visivel = False
    Formulario["CSC_DGCO"].Habilitado = False
    #Formulario["VALOR_DO_DOCUMENTO"].Visivel = True
    #Formulario["VALOR_DO_DOCUMENTO"].Habilitado = True
    Formulario["VALOR_DA_NOTA_FISCAL"].Visivel = True
    Formulario["VALOR_DA_NOTA_FISCAL"].Habilitado = True
    Formulario["LABEL57"].Visivel = False
    Formulario["LABEL57"].Habilitado = False
    Formulario["CSC_MATRICULA"].Visivel = False
    Formulario["CSC_MATRICULA"].Habilitado = False
    Formulario["CSC_NOTA_FISCAL"].Visivel = False
    Formulario["CSC_NOTA_FISCAL"].Habilitado = False
    Formulario["CSC_NUM_SISLOC"].Visivel = False
    Formulario["CSC_NUM_SISLOC"].Habilitado = False    
    
if (OrdemServico.Servico.Sigla == "REGNFDGCOSGPS"):
    Formulario["LABEL57"].Visivel = False
    Formulario["LABEL57"].Habilitado = False
    Formulario["CSC_MATRICULA"].Visivel = False
    Formulario["CSC_MATRICULA"].Habilitado = False
    Formulario["CSC_NOTA_FISCAL"].Visivel = False
    Formulario["CSC_NOTA_FISCAL"].Habilitado = False
    Formulario["CSC_NUM_SISLOC"].Visivel = False
    Formulario["CSC_NUM_SISLOC"].Habilitado = False
    
if (OrdemServico.Servico.Sigla == "REGNFCDGCOSERCMO"):
    Formulario["LABEL57"].Visivel = False
    Formulario["LABEL57"].Habilitado = False
    Formulario["CSC_MATRICULA"].Visivel = False
    Formulario["CSC_MATRICULA"].Habilitado = False
    Formulario["CSC_NOTA_FISCAL"].Visivel = False
    Formulario["CSC_NOTA_FISCAL"].Habilitado = False
    Formulario["CSC_NUM_SISLOC"].Visivel = False
    Formulario["CSC_NUM_SISLOC"].Habilitado = False
    
if (OrdemServico.Servico.Sigla == "REGNFCDGCOMERSERSMO"):
    Formulario["LABEL57"].Visivel = False
    Formulario["LABEL57"].Habilitado = False
    Formulario["CSC_MATRICULA"].Visivel = False
    Formulario["CSC_MATRICULA"].Habilitado = False
    Formulario["CSC_NOTA_FISCAL"].Visivel = False
    Formulario["CSC_NOTA_FISCAL"].Habilitado = False
    Formulario["CSC_NUM_SISLOC"].Visivel = False
    Formulario["CSC_NUM_SISLOC"].Habilitado = False
```
**ScriptInicio**
```python
OrdemServico.SetCustom("CLAUSULA CONTRATUAL"," ")
OrdemServico.SetCustom("MULTA"," ")
```
**ScriptValidacao**
```python
import re

data_vencimento = Convert.ToDateTime(OrdemServico.GetCustom("DATA_VENCIMENTO"))
data_atual = DateTime(DateTime.Now.Year, DateTime.Now.Month, DateTime.Now.Day, 0, 0, 0)

if OrdemServico.Servico.Sigla == 'PAGMENTOSREVENDA' and String.IsNullOrEmpty(OrdemServico.GetCustom('TEXT')):
    Criticas.AdicionaPendencia('Escreva o Registro de Pagamento Autorizado por Nota Técnica!')

#if (len(OrdemServico.GetCustom("DGCO").replace(" ",""))) < 10:
    #Criticas.AdicionaPendencia("Favor preencher o campo DGCO no formato 00000/0000.")
    
#Criticas.AdicionaPendencia("Teste" + Utils.ExecuteScript(re('[^\d*\;*\s]',OrdemServico.GetCustom("NUM_SEQ"))).toString())
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Documento de comprovação" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - LABEL57 "Caso não haja DGCO, preencher somente com "zeros" o campo abaixo." [Label String(1500) → CPE_CSC.LABEL57] obrigatório
  - CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}
  - FORNECEDOR1 "Fornecedor/Parceiro" [TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1] obrigatório
**FORNECEDOR1.ScriptModificado**
```python
Formulario["FORNECEDOR1"].Valor = String.ToUpper(Formulario["FORNECEDOR1"].Valor)
```
  - NATUREZA_SERV "Natureza do serviço" [DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV] obrigatório
  - QUANTIDADE "Quantidade de Notas Fiscais" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE] obrigatório
  - SALDO_NOTA_TECNICA "Descritivo do Saldo da Nota Técnica" [DataGrid RecordList → Z_00143_SALDO_NOTA_TECNICA.SALDO_NOTA_TECNICA] obrigatório
    - coluna VALOR obrigatório
    - coluna SALDO_ATUAL obrigatório
    - coluna PARCEIRO obrigatório
    - coluna PRODUTO obrigatório
    - coluna NUMERO_NT obrigatório
    - coluna SALDO_REMANESCENTE obrigatório
  - LABEL1 "ATENÇÃO! O campo "Número da RI" está bloqueado nesse momento, e só será preenchido ao longo do chamado!" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - VALOR_DA_NOTA_FISCAL "Número(s) da(s) Nota(s) e Valor(es) da(s) Nota(s)" [DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL] obrigatório — QtdColunasFormulario=1
    - coluna NUMERO_RI
    - coluna CONDICAO_DE_PAGAMENTO
    - coluna MULTA obrigatório
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna DATA_DE_VENCIMENTO_NO_RI
    - coluna NUM_ITEM
    - coluna DATA_PGTO
    - coluna ORGANIZACAO
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna DATA_DE_REGISTRO obrigatório
    - coluna NOME_ARQUIVO obrigatório
    - coluna NUMERO_OC obrigatório
    - coluna NUMERO_LINHAS obrigatório
    - coluna DATA_DE_REGISTRO_NO_RI
    - coluna NUMERO_DO_DOCUMENTO obrigatório
    - coluna VALOR_DO_DOCUMENTO obrigatório
    - coluna CONDICAO_DE_PGTO
  - DATA_EMISSAO "Data de emissão (Em caso de mais de uma NF, informar a data da NF que foi emitida primeiro)" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO] obrigatório
  - DATA_VENCIMENTO "Data de Vencimento (Em caso de mais de uma NF, informar a data da NF que vencerá primeiro)" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO] obrigatório
  - DESCRICAO_DETALHADA "Informações Adicionais" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]
  - CSC_MATRICULA "Filial:" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_NOTA_FISCAL "UOR" [TextBox String → CPE_CSC.CSC_NOTA_FISCAL] obrigatório
  - CSC_NUM_SISLOC "Conta Contábil" [TextBox String → CPE_CSC.CSC_NUM_SISLOC] obrigatório
  - TEXT "Código de Item no ERP (Exemplo: CSRV-000000)" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"AAAA-000000"}
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL DE MERCADORIAS
  - anexo "Nota Fiscal" classes: Nota Fiscal — ProduzidoTermino=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração: Nome=NOTA FISCAL DE SERVIÇOS
  - anexo "Nota Fiscal" classes: Nota Fiscal de Serviço — ProduzidoTermino=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Análise Fisco-Tributária" classes: Análise Fisco-Tributária — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "FQ412-066" classes: FQ412-066 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=DOCUMENTOS
  - anexo "Documentos" classes: Documentos — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: FGTS — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Previdência — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Carta de Exclusividade — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Folha Empregados — RequeridoInicial=true; PermiteMultiplosItens=true
  - anexo "" classes: Benefícios — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Técnica" classes: Nota Técnica — RequeridoInicial=true

### [350193] Tarefa "Verificar localizado Rio de Janeiro"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
Formulario["COMBOBOX_III"].Itens = "Sim;Não"
Formulario["COMBOBOX_IV"].Itens = "Sim;Não"
Formulario["COMBOBOX_IV"].Visivel = False
Formulario["COMBOBOX_IV"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - COMBOBOX_III "A NF de mercadoria tem o tomador localizado no Rio de Janeiro?" [DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III] obrigatório
**COMBOBOX_III.ScriptModificado**
```python
if Formulario["COMBOBOX_III"].Valor == "Sim":
    Formulario["COMBOBOX_IV"].Visivel = True
    Formulario["COMBOBOX_IV"].Habilitado = True
else:
    Formulario["COMBOBOX_IV"].Visivel = False
    Formulario["COMBOBOX_IV"].Habilitado = False
```
  - COMBOBOX_IV "Foi verificada a aplicação do Difal?" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_IV] obrigatório

### [350195] SubProcesso "Fiscalização Administrativa"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=449; PassaTodosItens=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
OrdemServico.SetCustom("FORNECEDOR1",String.ToUpper(OrdemServico.GetCustom("FORNECEDOR1")))
```
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla","FISCADMCONT")
```
  - CustomPropertyId=906; CustomProperty=NATUREZA_SERV
  - CustomPropertyId=874; CustomProperty=QUANTIDADE
  - CustomPropertyId=1902; CustomProperty=VALOR_DA_NOTA_FISCAL
  - CustomPropertyId=253; CustomProperty=DATA_EMISSAO
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=510; CustomProperty=FAVORECIDO_TODOS
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - CustomPropertyId=790; CustomProperty=SIGLA_SCR
**ExpressaoValor**
```python
OrdemServico.Servico.Sigla
```
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=254; CustomProperty=DATA_VENCIMENTO
  - CustomPropertyId=2164; CustomProperty=DESCRICAO_DETALHADA
  - CustomPropertyId=447; CustomProperty=FORNECEDOR1
- Associação: Ativo=true; FraseAssociacao=Registro de Notas Fiscais de Fornecedores -> Fiscalização Administrativa - Registro de Notas Fiscais; FraseInversaAssociacao=Fiscalização Administrativa - Registro de Notas Fiscais -> Registro de Notas Fiscais de Fornecedores; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=FISCADM; SeparadorSequencial=. | fonte: Registro de Notas Fiscais de Fornecedores → alvo: Fiscalização Administrativa V360 (Uso Exclusivo do CESEC)

### [350196] Tarefa "Liberar Tipo de Nota para Lançamento"
Responsável: Fila Fiscal (papel 365)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0001 Preencher Campos
  - CSC_TIPO_NF "Tipo de Nota" [TextBox String → CPE_CSC.CSC_TIPO_NF] obrigatório
  - CSC_ORGANIZACAO "Organização" [DropDownList String → CPE_CSC.CSC_ORGANIZACAO] obrigatório
  - PRAZO_FINAL "Prazo para Lançamento da Nota Fiscal" [DatePicker DateTime → CP_ORDEM_SERVICO.PRAZO_FINAL] obrigatório
  - OBS5 "Observação" [Memo String(2000) → CPE_CONTRATOS.OBS5]

### [350197] SubProcesso "Baixa de Pagamento de NFS- ABR Telecom"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=960
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=447; CustomProperty=FORNECEDOR1
  - CustomPropertyId=1902; CustomProperty=VALOR_DA_NOTA_FISCAL
- Associação: Ativo=true; FraseAssociacao=Registro de Notas Fiscais de Fornecedores->Baixa de Pagamento de NFS-ABR Telecom; FraseInversaAssociacao=Baixa de Pagamento de NFS-ABR Telecom->Registro de Notas Fiscais de Fornecedores; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=RECEBIMENTONF1; SeparadorSequencial=. | fonte: Registro de Notas Fiscais de Fornecedores → alvo: Baixa de Pagamento de NFS- ABR Telecom

### [350198] Tarefa "Consulta ao DIFAL
"
Responsável: Responsável atual (papel 36)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptFormCarregado**
```python
Formulario["OBS20"].Valor = "Verificar junto ao escritório de contabilidade se a mercadoria indicada na NF-e em anexo exige o pagamento imediato do DIFAL.                                                                                        ATENÇÃO!!! AVANÇAR O CHAMADO APENAS QUANDO FINALIZAR A VERIFICAÇÃO"
Formulario["OBS20"].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - OBS20 "Observação:" [Memo String(40000) → CPE_CSC.OBS20] obrigatório

### [350200] EventoIntermediarioMensagem "E-mail "
Config: ListaDestinatarios=pagamentos@bbtecno.com.br
ModeloComunicado: Aviso sobre encaminhamento
Corpo do comunicado: OrdemServico.Cliente.Nome,
Foi encaminhado o chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Acesse a aplicação Supravizio e consulte a solicitação via tela Workspace.
Atenciosamente, 
Central de Serviços
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
Mensagem.Assunto = "NF Serviços - Fornecedor: " + OrdemServico.GetCustom("FORNECEDOR1") + " - DGCO: " + OrdemServico.GetCustom("DGCO")
```

### [350220] Tarefa "Verificar Insumos Obrigatórios"
Responsável: Equipe Registro NF (papel 140)
Config: UnidadeANO=Minutos
**ScriptFormCarregado**
```python
#Formulario["DATA_VENCIMENTO"].Habilitado = False

if (OrdemServico.Servico.Sigla == "PAGMENTOSREVENDA"):
    Formulario["DATA_FIM_ESTIMADA"].Visivel = True
    Formulario["DATA_FIM_ESTIMADA"].Habilitado = False
    
if (OrdemServico.Servico.Sigla == "PAGFORNECSEMDGCO"):
    Formulario["DATA_FIM_ESTIMADA"].Visivel = True
    Formulario["DATA_FIM_ESTIMADA"].Habilitado = False
    Formulario["FAVORECIDO_COBRA"].Visivel = False
    Formulario["FAVORECIDO_COBRA"].Habilitado = False
    Formulario["FAVORECIDO_TODOS"].Visivel = False
    Formulario["FAVORECIDO_TODOS"].Habilitado = False
    
if (OrdemServico.Servico.Sigla == "REGNFCDGCOSERCMO"):
    Formulario["DATA_FIM_ESTIMADA"].Visivel = True
    Formulario["DATA_FIM_ESTIMADA"].Habilitado = False
    
if (OrdemServico.Servico.Sigla == "REGNFCDGCOMERSERSMO"):
    Formulario["DATA_FIM_ESTIMADA"].Visivel = True
    Formulario["DATA_FIM_ESTIMADA"].Habilitado = False

if (OrdemServico.Servico.Sigla == "REGDESPERESSARC"):
    Formulario["PRAZO1"].Visivel = False
    Formulario["PRAZO1"].Habilitado = False
    Formulario["DATA_VENCIMENTO"].Visivel = True
    Formulario["DATA_VENCIMENTO"].Habilitado = True
    Formulario["DATA_FIM_ESTIMADA"].Visivel = False
    Formulario["DATA_FIM_ESTIMADA"].Habilitado = False
    Formulario["FAVORECIDO_COBRA"].Visivel = False
    Formulario["FAVORECIDO_COBRA"].Habilitado = False
    Formulario["FAVORECIDO_TODOS"].Visivel = False
    Formulario["FAVORECIDO_TODOS"].Habilitado = False    

if (OrdemServico.Servico.Sigla == "REGNFDGCOSGPS"):
    Formulario["DATA_FIM_ESTIMADA"].Visivel = True
    Formulario["DATA_FIM_ESTIMADA"].Habilitado = False
```
**Regra**
```python
2880
```
**ScriptInicio**
```python
dias = 5

#conta dias uteis
item  = 1
dataFim = Convert.ToDateTime(OrdemServico.GetCustom("DATA_VENCIMENTO"))
while item <= dias :
    if (dataFim.DayOfWeek == DayOfWeek.Sunday):
        dataFim = dataFim.AddDays(-2)
    else:
        if (dataFim.DayOfWeek == DayOfWeek.Saturday):
            dataFim = dataFim.AddDays(-1)
    dataFim = dataFim.AddDays(-1)
    item += 1

if (dataFim.DayOfWeek == DayOfWeek.Sunday):
    dataFim = dataFim.AddDays(-2)
else:
    if (dataFim.DayOfWeek == DayOfWeek.Saturday):
        dataFim = dataFim.AddDays(-1)

OrdemServico.SetCustom("DATA_FIM_ESTIMADA", DateTime(dataFim.Year, dataFim.Month, dataFim.Day, 23, 59, 0))








#############################################################################################################

#dias = 5

#conta dias uteis
#item  = 1
#dataFim = DateTime.Now
#while item <= dias :
#   if (dataFim.DayOfWeek == DayOfWeek.Sunday):
#       dataFim = dataFim.AddDays(1)
#   else:
#       if (dataFim.DayOfWeek == DayOfWeek.Saturday):
#           dataFim = dataFim.AddDays(2)
#   dataFim = dataFim.AddDays(1)
#   item += 1

#if (dataFim.DayOfWeek == DayOfWeek.Sunday):
#   dataFim = dataFim.AddDays(1)
#else:
#   if (dataFim.DayOfWeek == DayOfWeek.Saturday):
#       dataFim = dataFim.AddDays(2)

#OrdemServico.SetCustom("DATA_FIM_ESTIMADA", DateTime(dataFim.Year, dataFim.Month, dataFim.Day, 18, 0, 0))
```
**ScriptFim**
```python
OrdemServico["RESPONSAVEL_ATUAL"] = OrdemServico.ResponsavelId
```
**ScriptValidacao**
```python
#rubricat = Convert.ToString(OrdemServico.GetCustom("NUM_SEQ")

#if (rubricat.isdigit() != True):
#   Criticas.AdicionaPendencia("Rubrica contábil deve ser numérica!")

#if OrdemServico.Numero == 251480:
#    Criticas.AdicionaPendencia(Convert.ToDateTime(OrdemServico.GetCustom("DATA_FIM_ESTIMADA")).ToString())
#    Criticas.AdicionaPendencia(DateTime.Now.ToString())
    #(Convert.ToDateTime(OrdemServico.GetCustom("DATA_FIM_ESTIMADA"))) >= DateTime.Now
```
- Operação PR0001 Preencher Campos
  - DATA_VENCIMENTO "Data de Vencimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO]
**DATA_VENCIMENTO.ScriptModificado**
```python
dias = 5

#conta dias uteis
item  = 1
dataFim = Convert.ToDateTime(Formulario["DATA_VENCIMENTO"].Valor)
while item <= dias :
    if (dataFim.DayOfWeek == DayOfWeek.Sunday):
        dataFim = dataFim.AddDays(-2)
    else:
        if (dataFim.DayOfWeek == DayOfWeek.Saturday):
            dataFim = dataFim.AddDays(-1)
    dataFim = dataFim.AddDays(-1)
    item += 1

if (dataFim.DayOfWeek == DayOfWeek.Sunday):
    dataFim = dataFim.AddDays(-2)
else:
    if (dataFim.DayOfWeek == DayOfWeek.Saturday):
        dataFim = dataFim.AddDays(-1)

#OrdemServico.SetCustom("DATA_FIM_ESTIMADA", DateTime(dataFim.Year, dataFim.Month, dataFim.Day, 18, 0, 0))

Formulario["DATA_FIM_ESTIMADA"].Valor = DateTime(dataFim.Year, dataFim.Month, dataFim.Day, 23, 59, 0)
```
  - DATA_FIM_ESTIMADA "Data limite para registro da nota fiscal" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_FIM_ESTIMADA] obrigatório
  - PRAZO1 "Prazo Atrasado" [CheckBox Boolean → CPE_ORDEM_SERVICO.PRAZO1]
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS_3 "Responsável pelo tratamento" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_3] obrigatório
  - FAVORECIDO_COBRA "Gestor do Contrato:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - FAVORECIDO_TODOS "Fiscal de Serviço:" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
- Acoes:
  - Acao=Email; ModeloComunicadoId=254; Percentual=100; Temporalidade=30; CodigoGrupoANO=98c348c4-b624-499a-b326-3fc3c306bc5a; ModeloComunicado=Aviso sobre o prazo - chamado aberto 48 horas

### [350221] SubProcesso "Fiscalização Administrativa"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=449; PassaTodosItens=true
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
**ScriptInicio**
```python
OrdemServico.SetCustom("FORNECEDOR1",String.ToUpper(OrdemServico.GetCustom("FORNECEDOR1")))
```
- ValoresInputs:
  - CustomPropertyId=447; CustomProperty=FORNECEDOR1
  - CustomPropertyId=906; CustomProperty=NATUREZA_SERV
  - CustomPropertyId=874; CustomProperty=QUANTIDADE
  - CustomPropertyId=1902; CustomProperty=VALOR_DA_NOTA_FISCAL
  - CustomPropertyId=1833; CustomProperty=CSC_DGCO
  - CustomPropertyId=510; CustomProperty=FAVORECIDO_TODOS
  - CustomPropertyId=550; CustomProperty=FAVORECIDO_COBRA
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla","FISCADMCONT")
```
  - CustomPropertyId=253; CustomProperty=DATA_EMISSAO
  - CustomPropertyId=254; CustomProperty=DATA_VENCIMENTO
  - CustomPropertyId=2164; CustomProperty=DESCRICAO_DETALHADA
- Associação: Ativo=true; FraseAssociacao=Registro de Notas Fiscais de Fornecedores -> Fiscalização Administrativa - Registro de Notas Fiscais; FraseInversaAssociacao=Fiscalização Administrativa - Registro de Notas Fiscais -> Registro de Notas Fiscais de Fornecedores; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=FISCADM; SeparadorSequencial=. | fonte: Registro de Notas Fiscais de Fornecedores → alvo: Fiscalização Administrativa V360 (Uso Exclusivo do CESEC)

### [350222] EventoIntermediarioTimer ""
Config: TempoIntervalo=720

### [350223] EventoIntermediarioTimer ""
Config: TempoIntervalo=7200

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
### papel 140: Equipe Registro NF
Tipo=RelacaoPessoas | pessoas: Fila CSC - Financeiro
### papel 793: Difin
Tipo=RelacaoOrgaos
### papel 365: Fila Fiscal
Tipo=RelacaoPessoas | pessoas: Fila Fiscal

## Campos customizados usados (definição global)

### CSC_DGCO — DGCO
TextBox String → CPE_CSC.CSC_DGCO

### FORNECEDOR1 — Fornecedor
TextBox String → CP_ORDEM_SERVICO.FORNECEDOR1

### NATUREZA_SERV — Natureza do serviço
DropDownList String → CP_ORDEM_SERVICO.NATUREZA_SERV
Itens: Ajudante de Armazém;Aluguel;Aquisição de bens;Despachante;Gestão de Pessoas;Limpeza;Locação de Bens;Manutenção de Bens;Mão de Obra;Outros;Recepção;Serviço de Contabilidade;Serviços de Infraestrutura;Serviços de TI;Vigilância Monitoramento;Vigilância Patrimonial

### QUANTIDADE — Quantidade
TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE

### VALOR_DA_NOTA_FISCAL — Valor(es) da(s) Nota(s)
DataGrid RecordList → Z_00143_VALOR_DA_NOTA_FISCAL.VALOR_DA_NOTA_FISCAL
Colunas do registro:
- NUMERO_NOTA_SERVICO "Número da Nota Fiscal" [TextBox String]
- VALOR_NOTA_FISCAL_SERVICO "Valor da Nota Fiscal" [TextBox Decimal]
- ORGANIZACAO "ORGANIZACAO" [DropDownList String]
**ORGANIZACAO.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT TO_CHAR(ORGANIZATION_ID) ID,ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS ORDER BY ORGANIZACAO")
```
- NUM_ITEM "Número do RI" [TextBox Integer]
- NUMERO_RI "Número da RI" [TextBox String]
- NOME_ARQUIVO "Nome do Arquivo da Nota Fiscal" [TextBox String]
- DATA_PGTO "Data de Pagamento" [DatePicker DateTime]
- CONDICAO_DE_PGTO "Condição de pagamento da OC (Conforme ERP)" [TextBox String]

### DATA_EMISSAO — Data da Emissão
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO

### DATA_VENCIMENTO — Data do Vencimento
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_VENCIMENTO

### TIPOS_DE_NF — Tipos de NF
DropDownList String(50) → CPE_CONTRATOS.TIPOS_DE_NF
Itens: Mão-de-obra;Mercadoria;Serviço

### JUSTIFICATIVA — Justificativa
TextBox String(1999) → CPE_CSC.JUSTIFICATIVA

### SIM_NAO1 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO1
Itens: Sim;Não

### JUSTIFICATIVA1 — Justificativa1
Memo String → CPE_CSC.JUSTIFICATIVA

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

### CONTA_CONTABIL1 — Conta Contábil
TextBox String → CPE_FINANCEIRO.CONTA_CONTABIL1

### FORNECEDOR01 — Fornecedor
TextBox String → CPE_CSC.FORNECEDOR01

### CSC_UOR_LISTA — UOR
DropDownList String(500) → CPE_CSC.CSC_UOR_LISTA
**LookupScript**
```python
Itens=DB.ExecuteDataTable(" SELECT DISTINCT SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO where nome <> SCR ||' - ' ORDER BY SCR ")
```

### COMBOBOX2 — COMBOBOX2
DropDownList String → CPE_BOOTCAMP.COMBOBOX2

### DADOS_LACAMENTO — Dados de Lançamento
DataGrid RecordList → Z_00143_DADOS_LACAMENTO.DADOS_LACAMENTO
Colunas do registro:
- NUMERO_NOTA_FISCAL "Numero da Nota Fiscal" [TextBox String]
- NUMERO_RI "Numero RI" [TextBox String]
- VALOR_NOTA_FISCAL "Valor da Nota Fiscal" [TextBox String]
- ORGANIZACAO "Organização" [TextBox String]
- DATA_PAGAMENTO_RI "Data Pagamento RI" [TextBox String]
- VALOR_RETENCAO "Valor da Retenção" [TextBox String]

### ASSUNTO_GUIA — Assunto
TextBox String → CP_ORDEM_SERVICO.ASSUNTO_GUIA
Descrição: Assunto da guia de pagamento

### CSC_DATA_RECEBIMENTO — Data de Recebimento
DatePicker DateTime → CPE_CSC.CSC_DATA_RECEBIMENTO

### CSC_CEP — CEP
TextBox String → CPE_CSC.CSC_CEP

### FAVORECIDO_TODOS_3 — Favorecido
DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_3
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

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### VALOR_DA_NF — Número(s) e Valor(es) da(s) Nota(s) Fiscal(is)
DataGrid RecordList → Z_00143_VALOR_DA_NF.VALOR_DA_NF
Colunas do registro:
- NUMERO_RI "Número da RI" [TextBox String]
- NUMERO_NOTA_SERVICO "Número da NF" [TextBox String]
- VALOR_NOTA_FISCAL_SERVICO "Valor da NF" [TextBox Decimal]
- MES_DE_REFERENCIA "Mês" [DropDownList String] itens: JAN;FEV;MAR;ABR;MAI;JUN;JUL;AGO;SET;OUT;NOV;DEZ

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### FORNECEDOR2 — Fornecedor
TextBox String → CPE_CSC.FORNECEDOR2

### SALDO_NOTA_TECNICA — Descritivo do Saldo da Nota Técnica
DataGrid RecordList → Z_00143_SALDO_NOTA_TECNICA.SALDO_NOTA_TECNICA
Colunas do registro:
- NUMERO_NT "Número da NT" [TextBox String]
- PARCEIRO "Parceiro" [TextBox String]
- PRODUTO "Produto" [TextBox String]
- VALOR "Valor Aprovado na Nota Técnica" [TextBox Decimal]
- SALDO_ATUAL "Saldo Atual da Nota Técnica" [TextBox Decimal]
- SALDO_REMANESCENTE "Saldo Remanescente da Nota Técnica" [TextBox String]

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### DADOS_CONS_NOTA_FISCAL — Dados para Consulta de Nota Fiscal
DataGrid RecordList → Z_00143_DADOS_CONS_NOTA_FISCAL.DADOS_CONS_NOTA_FISCAL
Descrição: Dados para Consulta de Nota Fiscal ISQN
Colunas do registro:
- LOCAL_PAGAMENTO "Local de Pagamento" [TextBox String]
- LOCAL_EMISSAO "Local de Emissão da Nota Fiscal" [TextBox String]
- RAZAO_SOCIAL_FORNECEDOR "Razão Social do Fornecedor" [TextBox String]
- CNPJ "CNPJ (Número)" [TextBox String]
- NUMERO_NOTA_FISCAL "Número da Nota Fiscal" [TextBox String]
- OBJETO_NOTA_FISCAL "Objeto da Nota Fiscal" [TextBox String]

### CONS_NOTA_FISCAL_TIPO_ — A nota fiscal é de
DropDownList String → CPE_TIP_SOL01.CONS_NOTA_FISCAL_TIPO_
Descrição: Selecione uma opção a respeito da nota fiscal
Itens: Contratação de serviço; Compra de produto; NF de movimentação de Itens (demonstração, comodato); Aluguel de Imóveis

### CSC_CIDADE — Cidade
TextBox String(500) → CPE_CSC.CSC_CIDADE
**LookupScript**
```python
#Itens = DB.ExecuteDataTable("SELECT DESCRICAO FROM CIDADE_V ORDER BY DESCRICAO")
```

### OPCAO_DE_CONFIRMACAO — Campo confirma uma afirmação
CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO
Descrição: Campo genérico para confirmação de uma afirmação

### LABEL57 — LABEL57
Label String(1500) → CPE_CSC.LABEL57

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### CSC_MATRICULA — Matrícula
TextBox String → CPE_CSC.CSC_MATRICULA

### CSC_NOTA_FISCAL — CSC_NOTA_FISCAL
TextBox String → CPE_CSC.CSC_NOTA_FISCAL

### CSC_NUM_SISLOC — Número da Abertura no Sisloc
TextBox String → CPE_CSC.CSC_NUM_SISLOC

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### COMBOBOX_III — COMBOBOX_III
DropDownList String → CPE_BENS_INVENTARIO.COMBOBOX_III

### COMBOBOX_IV — COMBOBOX_IV
DropDownList String → CPE_BOOTCAMP.COMBOBOX_IV

### CSC_TIPO_NF — CSC_TIPO_NF
TextBox String → CPE_CSC.CSC_TIPO_NF

### CSC_ORGANIZACAO — CSC_ORGANIZACAO
DropDownList String → CPE_CSC.CSC_ORGANIZACAO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT TO_CHAR(ORGANIZATION_ID) ID,ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS ORDER BY ORGANIZACAO")
```

### PRAZO_FINAL — Prazo final
DatePicker DateTime → CP_ORDEM_SERVICO.PRAZO_FINAL
Descrição: Caso a recomendação já tenha sido reprogramada, indicar o prazo de vencimento deferido na última reprogramação.

### OBS5 — Observação5
Memo String(2000) → CPE_CONTRATOS.OBS5

### OBS20 — Observação20
Memo String(40000) → CPE_CSC.OBS20

### DATA_FIM_ESTIMADA — Data fim estimada
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_FIM_ESTIMADA

### PRAZO1 — Prazo
CheckBox Boolean → CPE_ORDEM_SERVICO.PRAZO1

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
