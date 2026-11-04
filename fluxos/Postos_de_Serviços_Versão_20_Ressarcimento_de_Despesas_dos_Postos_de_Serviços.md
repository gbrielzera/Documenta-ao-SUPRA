# Fluxo: Resssarcimento de Despesas dos Postos de Serviços (RESSARCIMENTOPS) — versão 20
Caminho: Fluxos > Postos de Serviços Versão 20 Ressarcimento de Despesas dos Postos de Serviços
XML: `XMLs para teste/Postos_de_Serviços_Versão_20_Ressarcimento_de_Despesas_dos_Postos_de_Serviços.xml` | Supravizio 19.1.1 | SubProcessoId 23220 | DesenhoProcessoId 3057 | ProcessoId 662
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PermiteVisualizacaoGestorSubNiveis=true; Objetivo=Resssarcimento de Despesas dos Postos de Serviços; DescricaoCliente=Resssarcimento de Despesas dos Postos de Serviços; PublicarApontamentosAA=Nunca; ObjetivoPlano=Resssarcimento de Despesas dos Postos de Serviços
Serviços: Resssarcimento de Despesas dos Postos de Serviços (DESPESASPS)

## Grafo do fluxo
- [370311] Tarefa "Prestação de Contas e Inserção de Documentos" {Fila Empresa B} → [372338] Aprovação pelo fiscal
- [370312] Tarefa "Aprovação pelo fiscal" {Assessores Selog} → [G82854] Aprovado?
- [370314] EventoFinal "" → (fim)
- [370313] Tarefa "Validação da contabilidade" {Fila CSC - Financeiro} → [370314] 
- [370309] Tarefa "Encaminhar para o fornecedor B" {Fila Empresa B} → [370310] Tratar da Informação
- [370310] Tarefa "Tratar da Informação" {Fila Empresa B} → [370311] Prestação de Contas e Inserção de Documentos
- [372339] EventoIntermediarioMensagem "Abertura de chamado" → [G83193] POTENZA ou IT2B?
- [371692] Tarefa "Encaminhar para o fornecedor A" {Fila Empresa A} → [371693] Tratar da Informação
- [371693] Tarefa "Tratar da Informação" {Fila Empresa A} → [371694] Prestação de Contas e Inserção de Documentos
- [371694] Tarefa "Prestação de Contas e Inserção de Documentos" {Fila Empresa A} → [370312] Aprovação pelo fiscal
- [372338] Tarefa "Aprovação pelo fiscal" {Assessores Selog} → [G83310] Aprovado?
- [370256] EventoInicial "" {Cliente} → [372339] Abertura de chamado
- [G82854] Gateway "Aprovado?" → «Reprovado» [371694] Prestação de Contas e Inserção de Documentos | «Aprovado» [370313] Validação da contabilidade
- [G83193] Gateway "POTENZA ou IT2B?" → «POTENZA» [371692] Encaminhar para o fornecedor A | «IT2B» [370309] Encaminhar para o fornecedor B
- [G83310] Gateway "Aprovado?" → «Reprovado» [370311] Prestação de Contas e Inserção de Documentos | «Aprovado» [370313] Validação da contabilidade

## Gateways
### [G82854] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV")
```
- alternativa → [371694] Prestação de Contas e Inserção de Documentos: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Reprovado
**ValorComparacaoDecision**
```python
False
```
- alternativa → [370313] Validação da contabilidade: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Aprovado
**ValorComparacaoDecision**
```python
True
```
### [G83193] POTENZA ou IT2B? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['COMBOBOX1']
```
- alternativa → [371692] Encaminhar para o fornecedor A: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=POTENZA
**ValorComparacaoDecision**
```python
'Potenza'
```
- alternativa → [370309] Encaminhar para o fornecedor B: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=IT2B
**ValorComparacaoDecision**
```python
'IT2B'
```
### [G83310] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV2")
```
- alternativa → [370311] Prestação de Contas e Inserção de Documentos: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Reprovado
**ValorComparacaoDecision**
```python
False
```
- alternativa → [370313] Validação da contabilidade: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Aprovado
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [370311] Tarefa "Prestação de Contas e Inserção de Documentos"
Responsável: Fila Empresa B (papel 1286)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario['COMBOBOX2'].Habilitado = False
```
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)

grid1 = OrdemServico.GetCustom("AVARIA")
grid2 = OrdemServico.GetCustom("MULTAS")

qtd1 = grid1.Rows.Count
qtd2 = grid2.Rows.Count

if qtd1 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', True)

if qtd2 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', True)
```
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Selecione a empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - COMBOBOX2 "Tipo de Chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - AVARIA "Avaria" [DataGrid RecordList → Z_00143_AVARIA.AVARIA]
    - coluna NOME_DO_POSTO obrigatório
    - coluna DESCRICAO_AVARIA obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
  - MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
    - coluna NOME_DO_POSTO obrigatório
    - coluna CAT obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
    - coluna CODIGO obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Inserção de documentos" classes: Arquivo — RequeridoInicial=true

### [370312] Tarefa "Aprovação pelo fiscal"
Responsável: Assessores Selog (papel 1487)
Config: Codigo=APROV
- Operação PR0002 Aprovar: MinimoAprovadores=1
  - (aprovação) COMBOBOX1 "Empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - (aprovação) COMBOBOX2 "Tipo de chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - (aprovação) AVARIA "Avarias" [DataGrid RecordList → Z_00143_AVARIA.AVARIA]
  - (aprovação) MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
  - aprovador: Assessores Selog (Unico)

### [370314] EventoFinal ""

### [370313] Tarefa "Validação da contabilidade"
Responsável: Fila CSC - Financeiro (papel 550)

### [370309] Tarefa "Encaminhar para o fornecedor B"
Responsável: Fila Empresa B (papel 1286)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario['COMBOBOX2'].Habilitado = False
```
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)

grid1 = OrdemServico.GetCustom("AVARIA")
grid2 = OrdemServico.GetCustom("MULTAS")

qtd1 = grid1.Rows.Count
qtd2 = grid2.Rows.Count

if qtd1 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', True)

if qtd2 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', True)
```
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Selecione a empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - COMBOBOX2 "Tipo de Chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - AVARIA "Avaria" [DataGrid RecordList → Z_00143_AVARIA.AVARIA]
    - coluna NOME_DO_POSTO obrigatório
    - coluna DESCRICAO_AVARIA obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
  - MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
    - coluna NOME_DO_POSTO obrigatório
    - coluna CAT obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
    - coluna CODIGO obrigatório

### [370310] Tarefa "Tratar da Informação"
Responsável: Fila Empresa B (papel 1286)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario['COMBOBOX2'].Habilitado = False
```
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)

grid1 = OrdemServico.GetCustom("AVARIA")
grid2 = OrdemServico.GetCustom("MULTAS")

qtd1 = grid1.Rows.Count
qtd2 = grid2.Rows.Count

if qtd1 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', True)

if qtd2 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', True)
```
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Selecione a empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - COMBOBOX2 "Tipo de Chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - AVARIA "Avaria" [DataGrid RecordList → Z_00143_AVARIA.AVARIA]
    - coluna NOME_DO_POSTO obrigatório
    - coluna DESCRICAO_AVARIA obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
  - MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
    - coluna NOME_DO_POSTO obrigatório
    - coluna CAT obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
    - coluna CODIGO obrigatório

### [372339] EventoIntermediarioMensagem "Abertura de chamado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de chamado aberto
Corpo do comunicado: Prezado(a),
Foi registrada Ordem de Serviço nº OrdemServico.Numero referente ao serviço OrdemServico.Servico.
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços

### [371692] Tarefa "Encaminhar para o fornecedor A"
Responsável: Fila Empresa A (papel 1287)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario['COMBOBOX2'].Habilitado = False
```
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)

grid1 = OrdemServico.GetCustom("AVARIA")
grid2 = OrdemServico.GetCustom("MULTAS")

qtd1 = grid1.Rows.Count
qtd2 = grid2.Rows.Count

if qtd1 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', True)

if qtd2 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', True)
```
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Selecione a empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - COMBOBOX2 "Tipo de Chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - AVARIA "Avaria" [DataGrid RecordList → Z_00143_AVARIA.AVARIA] — PermiteAgrupamento=true
    - coluna NOME_DO_POSTO obrigatório
    - coluna DESCRICAO_AVARIA obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
  - MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
    - coluna NOME_DO_POSTO obrigatório
    - coluna CAT obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
    - coluna CODIGO obrigatório

### [371693] Tarefa "Tratar da Informação"
Responsável: Fila Empresa A (papel 1287)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario['COMBOBOX2'].Habilitado = False
```
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)

grid1 = OrdemServico.GetCustom("AVARIA")
grid2 = OrdemServico.GetCustom("MULTAS")

qtd1 = grid1.Rows.Count
qtd2 = grid2.Rows.Count

if qtd1 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', True)

if qtd2 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', True)
```
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Selecione a empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - COMBOBOX2 "Tipo de Chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - AVARIA "Avaria" [DataGrid RecordList → Z_00143_AVARIA.AVARIA] — PermiteAgrupamento=true
    - coluna NOME_DO_POSTO obrigatório
    - coluna DESCRICAO_AVARIA obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
  - MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
    - coluna CAT obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOME_DO_POSTO obrigatório
    - coluna NOTA obrigatório
    - coluna CODIGO obrigatório

### [371694] Tarefa "Prestação de Contas e Inserção de Documentos"
Responsável: Fila Empresa A (papel 1287)
**ScriptFormCarregado**
```python
Formulario['COMBOBOX1'].Habilitado = False
Formulario['COMBOBOX2'].Habilitado = False
```
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)

grid1 = OrdemServico.GetCustom("AVARIA")
grid2 = OrdemServico.GetCustom("MULTAS")

qtd1 = grid1.Rows.Count
qtd2 = grid2.Rows.Count

if qtd1 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', False)
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', True)

if qtd2 > 0:
    OrdemServico.ModificaCampoFormularioVisivel('AVARIA', False)
    OrdemServico.ModificaCampoFormularioVisivel('MULTAS', True)
```
- Operação PR0001 Preencher Campos
  - COMBOBOX1 "Selecione a empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - COMBOBOX2 "Tipo de Chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - AVARIA "Avaria" [DataGrid RecordList → Z_00143_AVARIA.AVARIA] — PermiteAgrupamento=true
    - coluna NOME_DO_POSTO obrigatório
    - coluna DESCRICAO_AVARIA obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
  - MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
    - coluna NOME_DO_POSTO obrigatório
    - coluna CAT obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
    - coluna CODIGO obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Inserção de documentos" classes: Arquivo — RequeridoInicial=true

### [372338] Tarefa "Aprovação pelo fiscal"
Responsável: Assessores Selog (papel 1487)
Config: Codigo=APROV2
- Operação PR0002 Aprovar: MinimoAprovadores=1
  - (aprovação) COMBOBOX1 "Empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - (aprovação) COMBOBOX2 "Tipo de chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2]
  - (aprovação) AVARIA "Avarias" [DataGrid RecordList → Z_00143_AVARIA.AVARIA]
  - (aprovação) MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
  - aprovador: Assessores Selog (Unico)

### [370256] EventoInicial ""
Responsável: Cliente (papel 18)
TipoSolicitacao: Postos de Serviços
**ScriptFormCarregado**
```python
Formulario['CSV'].Visivel = False
Formulario['CHECKBOX1'].Visivel = False
Formulario['MULTAS'].Visivel = False
Formulario['AVARIA'].Visivel = False

Formulario['COMBOBOX1'].Itens = 'Potenza;IT2B'
Formulario['COMBOBOX2'].Itens = 'Avaria;Multa'
```
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel("CSV")
```
- Operação PR0001 Preencher Campos
  - MULTAS "Multas" [DataGrid RecordList → Z_00143_MULTAS.MULTAS]
    - coluna NOME_DO_POSTO obrigatório
    - coluna CAT obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
    - coluna CODIGO obrigatório
  - COMBOBOX1 "Selecione a empresa" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - COMBOBOX2 "Tipo de Chamado" [DropDownList String → CPE_BOOTCAMP.COMBOBOX2] obrigatório
**COMBOBOX2.ScriptModificado**
```python
if Formulario['COMBOBOX2'].Valor == 'Avaria':
    Formulario['AVARIA'].Visivel = True
    Formulario['MULTAS'].Visivel = False
    Formulario['CHECKBOX1'].Visivel = True
    Formulario['CSV'].Visivel = True
    
if Formulario['COMBOBOX2'].Valor == 'Multa':
    Formulario['MULTAS'].Visivel = True
    Formulario['AVARIA'].Visivel = False
    Formulario['CHECKBOX1'].Visivel = True
    Formulario['CSV'].Visivel = True
```
  - AVARIA "Avaria" [DataGrid RecordList → Z_00143_AVARIA.AVARIA]
    - coluna NOME_DO_POSTO obrigatório
    - coluna DESCRICAO_AVARIA obrigatório
    - coluna DATA_HORA obrigatório
    - coluna VALOR obrigatório
    - coluna NOTA obrigatório
  - CHECKBOX1 "Ler planilha" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1]
- Operação PR0004 Associar Itens Configuração: Nome=CSV
  - anexo "Planilha ou CSV" classes: Arquivo 01 — RequeridoInicial=true

## Papéis usados
### papel 1286: Fila Empresa B
Tipo=RelacaoPessoas | pessoas: Fila Empresa B
### papel 1487: Assessores Selog
Tipo=RelacaoPessoas | pessoas: SIMAO COUTINHO DE ALBUQUERQUE NETO, ANDERSON VIEIRA DE SOUZA, BARBARA MATTOS SILVINO ALVES, GERALDO AMARO FERREIRA FILHO, INECIA PEREIRA DE SANTANA ALEGRANCI
### papel 550: Fila CSC - Financeiro
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pagamentos
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1287: Fila Empresa A
Tipo=RelacaoPessoas | pessoas: Fila Empresa A

## Campos customizados usados (definição global)

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### COMBOBOX2 — COMBOBOX2
DropDownList String → CPE_BOOTCAMP.COMBOBOX2

### AVARIA — Avaria
DataGrid RecordList → Z_00143_AVARIA.AVARIA
Colunas do registro:
- NOME_DO_POSTO "Nome do Posto" [TextBox String]
- DESCRICAO_AVARIA "Descrição da Avaria" [Memo String]
- DATA_HORA "Data e Hora" [DateTimePicker DateTime]
- VALOR "Valor" [TextBox String]
- NOTA "Nota de débito de pagamento a LM" [TextBox String]

### MULTAS — Multas
DataGrid RecordList → Z_00143_MULTAS.MULTAS
Colunas do registro:
- NOME_DO_POSTO "Nome do Posto" [TextBox String]
- CAT "CAT de Atendimento Placa" [TextBox String]
- DATA_HORA "Data e Hora" [DateTimePicker DateTime]
- VALOR "Valor" [TextBox String]
- NOTA "Nota de débito de pagamento a LM" [TextBox String]
- CODIGO "Código da Multa" [TextBox String]

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
