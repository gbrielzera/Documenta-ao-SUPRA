# Fluxo: Comprovantes de Valores Pagos a Fornecedores (COMPROVPAGOSFORNECEDORES) — versão 38
Caminho: Fluxos > Financeiro - Serviços Gerais Versão 38 Comprovantes de Valores Pagos a Fornecedores Gabriel
XML: `XMLs para teste/Financeiro_-_Serviços_Gerais_Versão_38_Comprovantes_de_Valores_Pagos_a_Fornecedores Gabriel.xml` | Supravizio 19.1.1 | SubProcessoId 24096 | DesenhoProcessoId 2428 | ProcessoId 136
Órgão dono: 3000003110 - DIVISAO DE FINANCAS | Responsável: MIGUEL PIRES VILELLA
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Comprovantes de Valores Pagos a Fornecedores (COMPROVANTEFORNECEDORES)

## Grafo do fluxo
- [372312] LinkInicial "" → [372314] Verificar solicitação.
- [372313] Tarefa "Adicionar observações da verificação." {Fila CSC - Pagamentos} → [372317] Notificar atendimento
- [372314] Tarefa "Verificar solicitação." {Fila CSC - Pagamentos} → [G82968] Qual o tipo da solicitação?
- [372315] EventoFinal "Sucesso" → (fim)
- [372316] Tarefa "Anexar comprovante de pagamento." {Fila CSC - Pagamentos} → [372317] Notificar atendimento
- [372317] EventoIntermediarioMensagem "Notificar atendimento" → [372315] Sucesso
- [372318] EventoInicial "Início" → [372314] Verificar solicitação.
- [G82967] Gateway "Foi realizada o pagamento da Nota Fiscal?" → «Sim» [372316] Anexar comprovante de pagamento. | «Não» [372313] Adicionar observações da verificação.
- [G82968] Gateway "Qual o tipo da solicitação?" → «Comprovante» [G82967] Foi realizada o pagamento da Nota Fiscal? | «Conferência» [372313] Adicionar observações da verificação.

## Gateways
### [G82967] Foi realizada o pagamento da Nota Fiscal? (EventBasedExclusiveDecision)
- alternativa → [372316] Anexar comprovante de pagamento.: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0; RotuloMotivo=Sim
- alternativa → [372313] Adicionar observações da verificação.: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; RotuloMotivo=Não
### [G82968] Qual o tipo da solicitação? (EventBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["TIPO_SOL_COMPROVA_PAGO_F"]
```
- alternativa → [G82967] Foi realizada o pagamento da Nota Fiscal?: OperadorDecision=Equal; ReferenciaDecision=Comprovante; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
"Comprovante de Pagamento"
```
- alternativa → [372313] Adicionar observações da verificação.: OperadorDecision=Equal; ReferenciaDecision=Conferência; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
"Conferência do valor pago"
```

## Atividades

### [372312] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - NÚMERO DA NOTA FISCAL "Número da Nota fiscal ou Número da Ordem de Serviço" [TextBox String → CP_ORDEM_SERVICO.NÚMERO_DA_NOTA_FISCAL]
  - ORGANIZACAO_ERP "Organização ERP" [DropDownList String → CPE_CONTRATOS02.ORGANIZACAO_ERP] obrigatório
- Associação de subprocesso: AssociacaoId=621; FraseAssociacao=Lançamento de IPTU/Taxas > Comprovante de Valores pagos a Fornecedores; Nome=LANÇAMENTO DE IPTU/TAXAS > COMPROVANTE DE VALORES PAGOS A FUNCIONARIOS

### [372313] Tarefa "Adicionar observações da verificação."
Responsável: Fila CSC - Pagamentos (papel 705)
- Operação PR0001 Preencher Campos
  - OBSERVACAO "Observações da verificação" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexos" classes: Arquivo — RequeridoInicial=true

### [372314] Tarefa "Verificar solicitação."
Responsável: Fila CSC - Pagamentos (papel 705)
MotivoInterrupcaoSLA: Aguardando aprovação

### [372315] EventoFinal "Sucesso"
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [372316] Tarefa "Anexar comprovante de pagamento."
Responsável: Fila CSC - Pagamentos (papel 705)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0001 Preencher Campos
  - OBSERVACAO "Observações da verificação" [TextBox String(2000) → CPE_CSC.OBSERVACAO]
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de pagamento" classes: Comprovante de pagamento — RequeridoInicial=true

### [372317] EventoIntermediarioMensagem "Notificar atendimento"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado atendido com sucesso
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
 Complemento1 
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços
**ScriptEvento**
```python
Mensagem.Complemento1 = OrdemServico["OBSERVACAO"]
```
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=1655; ClasseConfiguracao=Arquivo
  - ClasseConfiguracaoId=2281; ClasseConfiguracao=Comprovante de pagamento

### [372318] EventoInicial "Início"
TipoSolicitacao: 14.02. Finanças, Controladoria e Contabilidade - Pagamentos
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - NUMERO_RI "Número do RI (se houver)" [TextBox String → CPE_CSC.NUMERO_RI]
  - DATA_PAGAMENTO_NF "Data de Pagamento da Nota Fiscal" [DatePicker DateTime → CPE_CSC.DATA_PAGAMENTO_NF]
  - VALORNOTAFISCAL "Valor da Nota Fiscal ou Valor do Pagamento" [TextBox Decimal → CPE_CSC.VALORNOTAFISCAL] obrigatório
    - coluna NUMERO_NOTA_SERVICO obrigatório
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna MES_DE_REFERENCIA obrigatório
  - DescricaoDetalhada (nativo) obrigatório
  - NÚMERO DA NOTA FISCAL "Número da Nota fiscal ou Número da Ordem de Serviço" [TextBox String → CP_ORDEM_SERVICO.NÚMERO_DA_NOTA_FISCAL]
  - NOME_FORNECEDOR "Nome do Fornecedor/Favorecido" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - TIPO_SOL_COMPROVA_PAGO_F "Tipo da solicitação" [DropDownList String → CPE_CSC.TIPO_SOL_COMPROVA_PAGO_F] obrigatório

## Papéis usados
### papel 705: Fila CSC - Pagamentos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pagamentos
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### NÚMERO DA NOTA FISCAL — Numero da Nota Fiscal
TextBox String → CP_ORDEM_SERVICO.NÚMERO_DA_NOTA_FISCAL

### ORGANIZACAO_ERP — Organização ERP
DropDownList String → CPE_CONTRATOS02.ORGANIZACAO_ERP
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT TO_CHAR(ORGANIZATION_ID) ID,ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS ORDER BY ORGANIZACAO")
```

### OBSERVACAO — .
TextBox String(2000) → CPE_CSC.OBSERVACAO
Descrição: Observação

### NUMERO_RI — Numero RI
TextBox String → CPE_CSC.NUMERO_RI

### DATA_PAGAMENTO_NF — Data de Pagamento da Nota Fiscal
DatePicker DateTime → CPE_CSC.DATA_PAGAMENTO_NF

### VALORNOTAFISCAL — Valor da Nota Fiscal
TextBox Decimal → CPE_CSC.VALORNOTAFISCAL

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### TIPO_SOL_COMPROVA_PAGO_F — Tipo de solicitação em comprovantes de valores pagos a fornecedores
DropDownList String → CPE_CSC.TIPO_SOL_COMPROVA_PAGO_F
Itens: Comprovante de Pagamento;Conferência do valor pago; Liberação SGPS; Provisão de SGPS;Benefícios; SISLOC; FOPAG(Salário, férias, vale transporte);RCC;Comprovantes judiciais
