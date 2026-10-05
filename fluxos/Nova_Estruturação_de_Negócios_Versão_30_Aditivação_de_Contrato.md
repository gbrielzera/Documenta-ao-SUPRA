# Fluxo: Aditivação de Contrato (1719) — versão 30
Caminho: Fluxos > Nova Estruturação de Negócios Versão 30 Aditivação de Contrato
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_30_Aditivação_de_Contrato.xml` | Supravizio 19.1.1 | SubProcessoId 20342 | DesenhoProcessoId 2875 | ProcessoId 79
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: HIVEPlace (Assinatura de Contrato e Aditivação de Contrato) (HIVEPLACE)

## Grafo do fluxo
- [326604] EventoInicial "" → [325393] Adicionamento do supravizio
- [325388] SubProcesso "CONTRATAÇÂO: Parecer de Risco" {Responsável atual} → [325392] Formalização interna
- [325389] Tarefa "CONTRATAÇÃO: Minuta Contratual de Aditivação" {Favorecido Cobra} → [325388] CONTRATAÇÂO: Parecer de Risco
- [325390] EventoFinal "" {Responsável atual} → (fim)
- [325392] Tarefa "Formalização interna" {Responsável atual} → [325390] 
- [325393] Tarefa "Adicionamento do supravizio" {Responsável atual} → [325389] CONTRATAÇÃO: Minuta Contratual de Aditivação

## Atividades

### [326604] EventoInicial ""
Config: Configuracao={"ServicoIniciador":"HIVEPLACE"}

### [325388] SubProcesso "CONTRATAÇÂO: Parecer de Risco"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1586; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer de Risco; FraseInversaAssociacao=Fonte: Aditivação de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERDERISCOADITIVACAO | fonte: Aditivação de Contrato → alvo: Parecer Conformidade

### [325389] Tarefa "CONTRATAÇÃO: Minuta Contratual de Aditivação"
Responsável: Favorecido Cobra (papel 277)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Minuta Contratual" classes: Minuta — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
  - NN_MOTIVO_CANCELAMENTO "Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)" [DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO]
**NN_MOTIVO_CANCELAMENTO.ScriptModificado**
```python
motivoCancelamento = Formulario["NN_MOTIVO_CANCELAMENTO"].Valor
justificativa = Formulario["Justificativa"].Valor

OrdemServico.SetCustom("NN_CANCELA", Formulario["NN_CANCELA"].Valor)
OrdemServico.SetCustom("NN_MOTIVO_CANCELAMENTO", motivoCancelamento.ToString())
OrdemServico.Justificativa = justificativa.ToString()
OrdemServico.Salva()

OrdemServico.Cancela(motivoCancelamento.ToString())

OrdemServico.Salva()
```
  - NN_CANCELA "Cancela chamado?" [DropDownList String → CPE_NEGOCIOS.NN_CANCELA]
**NN_CANCELA.ScriptModificado**
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

OrdemServico.Salva()
```
  - Justificativa (nativo)

### [325390] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [325392] Tarefa "Formalização interna"
Responsável: Responsável atual (papel 36)

### [325393] Tarefa "Adicionamento do supravizio"
Responsável: Responsável atual (papel 36)

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
### papel 277: Favorecido Cobra
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))

    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Campos customizados usados (definição global)

### NN_MOTIVO_CANCELAMENTO — Motivo do cancelamento(após a seleção de um motivo, o chamado será cancelado automaticamente)
DropDownList String → CPE_NEGOCIOS.NN_MOTIVO_CANCELAMENTO
Descrição: Motivo do cancelamento
Itens: Demanda absorvida por outro projeto;
Inviabilidade técnica/operacional;
Negociação suspensa pela BBTS;
Negociação suspensa pelo Cliente;
Duplicidade/Teste;
Proposta comercial não aceita - Preço;
Decisão estratégica da BBTS;
A pedido do cliente;Preço de referência expirado

### NN_CANCELA — Cancela chamado?
DropDownList String → CPE_NEGOCIOS.NN_CANCELA
Itens: Sim;Não

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
