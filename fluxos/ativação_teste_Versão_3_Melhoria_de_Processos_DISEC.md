# Fluxo: Melhoria de Processos DISEC (MELHORIAA) — versão 3
Caminho: Fluxos > ativação teste Versão 3 Melhoria de Processos DISEC
XML: `XMLs para teste/ativação_teste_Versão_3_Melhoria_de_Processos_DISEC.xml` | Supravizio 19.1.1 | SubProcessoId 21549 | DesenhoProcessoId 2982 | ProcessoId 768
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PermiteVisualizacaoGestorSubNiveis=true; PublicarApontamentosAA=Nunca

## Grafo do fluxo
- [342762] Tarefa "Validação do Gestor do Setor" {Gestor de Setor - DISEC} → [342764] Validação Disec
- [342761] Tarefa "Validação do Gestor de Centro" {Cliente} → [342762] Validação do Gestor do Setor
- [342763] Tarefa "Comparar antes/depois" {Disec} → [342766] Calcular percentual sobre total do centro
- [342764] Tarefa "Validação Disec" {Cliente} → [342763] Comparar antes/depois
- [342765] EventoFinal "" → (fim)
- [342766] Tarefa "Calcular percentual sobre total do centro" {Disec} → [342765] 
- [342767] EventoInicial "" {Cliente} → [342761] Validação do Gestor de Centro

## Atividades

### [342762] Tarefa "Validação do Gestor do Setor"
Responsável: Gestor de Setor - DISEC (papel 1490)
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO "Sim ou Nao" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - aprovador: Gestor de Setor - DISEC (Unico)

### [342761] Tarefa "Validação do Gestor de Centro"
Responsável: Cliente (papel 18)
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO10 "Aprovado?" [DropDownList String → CPE_CSC.SIM_NAO10]
  - aprovador: Gerente Superior Imediato (Unico)

### [342763] Tarefa "Comparar antes/depois"
Responsável: Disec (papel 816)
- Operação PR0001 Preencher Campos
  - OBSERVACAO "Observações" [TextBox String(2000) → CPE_CSC.OBSERVACAO] obrigatório

### [342764] Tarefa "Validação Disec"
Responsável: Cliente (papel 18)
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO1 "Sim ou Não" [DropDownList String → CPE_CSC.SIM_NAO1]
  - aprovador: Gerente de Divisão Disec (Unico)

### [342765] EventoFinal ""

### [342766] Tarefa "Calcular percentual sobre total do centro"
Responsável: Disec (papel 816)
- Operação PR0001 Preencher Campos
  - NUMERO_OC "Número de processos melhorados" [TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC] obrigatório

### [342767] EventoInicial ""
Responsável: Cliente (papel 18)
- Operação PR0001 Preencher Campos
  - TEXT "Registrar melhoria" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
    - coluna USO obrigatório
    - coluna CRITERIO obrigatório
    - coluna PERIODO obrigatório
    - coluna PROD_PRODUTO obrigatório
    - coluna TIPO obrigatório
    - coluna NECESSIDADE obrigatório
    - coluna CODIGO obrigatório
    - coluna SEGMENTO obrigatório
    - coluna DESCRICAO obrigatório
    - coluna PRECO obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar evidências" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true

## Papéis usados
### papel 1490: Gestor de Setor - DISEC
Tipo=RelacaoPessoas | pessoas: BRUNO ROBERTO OLIVEIRA PRADO
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 257: Gerente Superior Imediato
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Cliente.Orgao.OrgaoPai.Gestor

if gestor != None:
    Utils.LogError(gestor.ToString(), "erro")

# se for um diretor ou presidente (mudar os identificadores e relacionar todos)
if gestor.Id == 4458 or gestor.Id == 4459 or gestor.Id == 4460 or gestor.Id == 4461 or gestor.Id == 3805 or gestor.Id == 5313 or gestor.Id == 5457 or gestor.Id == 5903 or gestor.Id == 23450 or gestor.Id == 23490 or gestor.Id == 23547:
    gestor = OrdemServico.Cliente

Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())





#OrdemServico.Cancela(motivo)OrdemServico.Cancela(motivo)OrdemServico.Cancela(motivo)
```
### papel 816: Disec
Tipo=RelacaoOrgaos
### papel 758: Gerente de Divisão Disec
Tipo=RelacaoOrgaos

## Campos customizados usados (definição global)

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### SIM_NAO10 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO10
Itens: Sim;Não

### OBSERVACAO — .
TextBox String(2000) → CPE_CSC.OBSERVACAO
Descrição: Observação

### SIM_NAO1 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO1
Itens: Sim;Não

### NUMERO_OC — Número da OC
TextBox Integer → CP_ORDEM_SERVICO.NUMERO_OC

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
