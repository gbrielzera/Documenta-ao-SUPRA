# Fluxo: Comprovantes de Valores Pagos a Fornecedores (COMPROVPAGOSFORNECEDORES) — versão 21
Caminho: Fluxos > Financeiro - Serviços Gerais Versão 21 Comprovantes de Valores Pagos a Fornecedores
XML: `XMLs para teste/Financeiro_-_Serviços_Gerais_Versão_21_Comprovantes_de_Valores_Pagos_a_Fornecedores.xml` | Supravizio 19.1.1 | SubProcessoId 19812 | DesenhoProcessoId 2795 | ProcessoId 150
Órgão dono: 3000003110 - DIVISAO DE FINANCAS | Responsável: MIGUEL PIRES VILELLA
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Comprovantes de Valores Pagos a Fornecedores (COMPROVANTEFORNECEDORES)

## Grafo do fluxo
- [327339] Tarefa "Preenchimento de Informações" {Cliente} → [316391] Verificar solicitação.
- [316390] Tarefa "Adicionar observações da verificação." {Fila CSC - Pagamentos} → [316395] Notificar atendimento
- [316391] Tarefa "Verificar solicitação." {Fila CSC - Pagamentos} → [G72520] Qual o tipo da solicitação?
- [316392] LinkInicial "" → [316391] Verificar solicitação.
- [316393] EventoFinal "Sucesso" → (fim)
- [316394] Tarefa "Anexar comprovante de pagamento." {Fila CSC - Pagamentos} → [316395] Notificar atendimento
- [316395] EventoIntermediarioMensagem "Notificar atendimento" → [316393] Sucesso
- [316396] EventoInicial "Início" → [327339] Preenchimento de Informações
- [G72520] Gateway "Qual o tipo da solicitação?" → «Comprovante» [G74407] Deseja corrigir as informações? | «Conferência» [G74409] Deseja corrigir o tipo de solicitação?
- [G72521] Gateway "Foi realizada o pagamento da Nota Fiscal?" → «Sim» [316394] Anexar comprovante de pagamento. | «Não» [316390] Adicionar observações da verificação.
- [G74407] Gateway "Deseja corrigir as informações?" → «Sim» [327339] Preenchimento de Informações | «Não» [G72521] Foi realizada o pagamento da Nota Fiscal?
- [G74409] Gateway "Deseja corrigir o tipo de solicitação?" → «Sim» [327339] Preenchimento de Informações | «Não» [316390] Adicionar observações da verificação.

## Gateways
### [G72520] Qual o tipo da solicitação? (EventBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico["TIPO_SOL_COMPROVA_PAGO_F"]
```
- alternativa → [G74407] Deseja corrigir as informações?: OperadorDecision=Equal; ReferenciaDecision=Comprovante; SequenciaAvaliacao=0; RotuloMotivo=Comprovante
- alternativa → [G74409] Deseja corrigir o tipo de solicitação?: OperadorDecision=Equal; ReferenciaDecision=Conferência; SequenciaAvaliacao=1; RotuloMotivo=Conferência
### [G72521] Foi realizada o pagamento da Nota Fiscal? (EventBasedExclusiveDecision)
- alternativa → [316394] Anexar comprovante de pagamento.: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0; RotuloMotivo=Sim
- alternativa → [316390] Adicionar observações da verificação.: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1; RotuloMotivo=Não
### [G74407] Deseja corrigir as informações? (EventBasedExclusiveDecision)
- alternativa → [327339] Preenchimento de Informações: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1; RotuloMotivo=Sim
- alternativa → [G72521] Foi realizada o pagamento da Nota Fiscal?: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0; RotuloMotivo=Não
### [G74409] Deseja corrigir o tipo de solicitação? (EventBasedExclusiveDecision)
- alternativa → [327339] Preenchimento de Informações: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1; RotuloMotivo=Sim
- alternativa → [316390] Adicionar observações da verificação.: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0; RotuloMotivo=Não

## Atividades

### [327339] Tarefa "Preenchimento de Informações"
Responsável: Cliente (papel 18)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - NOME_FORNECEDOR "Nome do Fornecedor/Favorecido" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - TIPO_SOL_COMPROVA_PAGO_F "Tipo da solicitação" [DropDownList String → CPE_CSC.TIPO_SOL_COMPROVA_PAGO_F] obrigatório
  - NUMERO_RI "Número do RI (se houver)" [TextBox String → CPE_CSC.NUMERO_RI]
  - NÚMERO DA NOTA FISCAL "Número da Nota fiscal ou Número da Ordem de Serviço" [TextBox String → CP_ORDEM_SERVICO.NÚMERO_DA_NOTA_FISCAL]
  - VALORNOTAFISCAL "Valor da Nota Fiscal ou Valor do Pagamento" [TextBox Decimal → CPE_CSC.VALORNOTAFISCAL] obrigatório
    - coluna VALOR_NOTA_FISCAL_SERVICO obrigatório
    - coluna MES_DE_REFERENCIA obrigatório
    - coluna NUMERO_NOTA_SERVICO obrigatório
  - DATA_PAGAMENTO_NF "Data de Pagamento da Nota Fiscal" [DatePicker DateTime → CPE_CSC.DATA_PAGAMENTO_NF]
  - DescricaoDetalhada (nativo) obrigatório

### [316390] Tarefa "Adicionar observações da verificação."
Responsável: Fila CSC - Pagamentos (papel 705)
- Operação PR0001 Preencher Campos
  - OBSERVACAO "Observações da verificação" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexos" classes: Arquivo — RequeridoInicial=true

### [316391] Tarefa "Verificar solicitação."
Responsável: Fila CSC - Pagamentos (papel 705)
MotivoInterrupcaoSLA: Aguardando aprovação

### [316392] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - NÚMERO DA NOTA FISCAL "Número da Nota fiscal ou Número da Ordem de Serviço" [TextBox String → CP_ORDEM_SERVICO.NÚMERO_DA_NOTA_FISCAL]
  - ORGANIZACAO_ERP "Organização ERP" [DropDownList String → CPE_CONTRATOS02.ORGANIZACAO_ERP] obrigatório
- Associação de subprocesso: AssociacaoId=1366; Nome=ROSELI FERREIRA DOS SANTOS; FraseAssociacao=Lançamento de IPTU/Taxas > Comprovante de Valores pagos a Fornecedores

### [316393] EventoFinal "Sucesso"

### [316394] Tarefa "Anexar comprovante de pagamento."
Responsável: Fila CSC - Pagamentos (papel 705)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0001 Preencher Campos
  - OBSERVACAO "Observações da verificação" [TextBox String(2000) → CPE_CSC.OBSERVACAO]
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de pagamento" classes: Comprovante de pagamento — RequeridoInicial=true

### [316395] EventoIntermediarioMensagem "Notificar atendimento"
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

### [316396] EventoInicial "Início"
TipoSolicitacao: 14.02. Finanças, Controladoria e Contabilidade - Pagamentos

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 705: Fila CSC - Pagamentos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pagamentos

## Campos customizados usados (definição global)

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### TIPO_SOL_COMPROVA_PAGO_F — Tipo de solicitação em comprovantes de valores pagos a fornecedores
DropDownList String → CPE_CSC.TIPO_SOL_COMPROVA_PAGO_F
Itens: Comprovante de Pagamento;Conferência do valor pago; Liberação SGPS; Provisão de SGPS;Benefícios; SISLOC; FOPAG(Salário, férias, vale transporte);RCC;Comprovantes judiciais

### NUMERO_RI — Numero RI
TextBox String → CPE_CSC.NUMERO_RI

### NÚMERO DA NOTA FISCAL — Numero da Nota Fiscal
TextBox String → CP_ORDEM_SERVICO.NÚMERO_DA_NOTA_FISCAL

### VALORNOTAFISCAL — Valor da Nota Fiscal
TextBox Decimal → CPE_CSC.VALORNOTAFISCAL

### DATA_PAGAMENTO_NF — Data de Pagamento da Nota Fiscal
DatePicker DateTime → CPE_CSC.DATA_PAGAMENTO_NF

### OBSERVACAO — .
TextBox String(2000) → CPE_CSC.OBSERVACAO
Descrição: Observação

### ORGANIZACAO_ERP — Organização ERP
DropDownList String → CPE_CONTRATOS02.ORGANIZACAO_ERP
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT TO_CHAR(ORGANIZATION_ID) ID,ORGANIZATION_CODE ||' - '|| ORGANIZATION_NAME AS ORGANIZACAO FROM ORG_ORGANIZATION_DEFINITIONS ORDER BY ORGANIZACAO")
```

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
