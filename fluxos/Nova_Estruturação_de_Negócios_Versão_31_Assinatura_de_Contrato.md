# Fluxo: Assinatura de Contrato (1718) — versão 31
Caminho: Fluxos > Nova Estruturação de Negócios Versão 31 Assinatura de Contrato
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_31_Assinatura_de_Contrato.xml` | Supravizio 19.1.1 | SubProcessoId 20563 | DesenhoProcessoId 2893 | ProcessoId 79
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: HIVEPlace (Assinatura de Contrato e Aditivação de Contrato) (HIVEPLACE)

## Grafo do fluxo
- [327874] EventoInicial "" {Responsável atual} → [327880] CONTRATAÇÃO: Minuta Contratual 
- [327875] LinkInicial "" → [327880] CONTRATAÇÃO: Minuta Contratual 
- [327876] SubProcesso "PRECIFICAÇÃO: Parecer jurídico" {Responsável atual} → [327878] CONTRATAÇÂO: Parecer de Risco
- [327877] SubProcesso "CONTRATAÇÃO: Parecer Cibernético" {Responsável atual} → [327876] PRECIFICAÇÃO: Parecer jurídico
- [327878] SubProcesso "CONTRATAÇÂO: Parecer de Risco" {Responsável atual} → [327881] CONTRATAÇÃO: Assinatura de Novos Contratos 
- [327879] Tarefa "CONTRATAÇÃO: Anexar Contrato
" {Responsável atual} → [327883] 
- [327880] Tarefa "CONTRATAÇÃO: Minuta Contratual " {Favorecido Cobra} → [327882] CONTRATAÇÃO: Parecer LGPD
- [327881] SubProcesso "CONTRATAÇÃO: Assinatura de Novos Contratos " {Responsável atual} → [327879] CONTRATAÇÃO: Anexar Contrato

- [327882] SubProcesso "CONTRATAÇÃO: Parecer LGPD" {Responsável atual} → [327877] CONTRATAÇÃO: Parecer Cibernético
- [327883] EventoFinal "" {Responsável atual} → (fim)

## Atividades

### [327874] EventoInicial ""
Responsável: Responsável atual (papel 36)
Config: Configuracao={"ServicoIniciador":"HIVEPLACE"}

### [327875] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=1593; Nome=MARCELO CAVALCANTE DE OLIVEIRA LIMA; FraseAssociacao=Assinatura de Contrato

### [327876] SubProcesso "PRECIFICAÇÃO: Parecer jurídico"
Referência: Abrir chamado para parecer COJUR
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1582; Codigo=COJUR_DF1; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1295; Property=Servico
**ExpressaoValor**
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(189)
```
  - PropertyId=1223; Property=DescricaoDetalhada
**ExpressaoValor**
```python
OrdemServico.GetCustom("NN_OBJETO_PROPOSTA")
```
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
  - CustomPropertyId=129; CustomProperty=EMPRESAS ENVOLVIDAS
**ExpressaoValor**
```python
OrdemServico["NN_APELIDO_PROJETO"]
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2157; ClasseConfiguracao=Consolidação Técnica
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer Jurídico; FraseInversaAssociacao=Fonte: Assinatura de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERJURIDICOASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Contrato → alvo: Parecer Orçamentário

### [327877] SubProcesso "CONTRATAÇÃO: Parecer Cibernético"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1581; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2292; ClasseConfiguracao=Minuta
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer Cibernético; FraseInversaAssociacao=Fonte: Assinatura de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERCYBERASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Contrato → alvo: Parecer Cibernético

### [327878] SubProcesso "CONTRATAÇÂO: Parecer de Risco"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1585; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer de Risco; FraseInversaAssociacao=Fonte: Assinatura de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERDERISCOASSINATURA | fonte: Assinatura de Contrato → alvo: Parecer Conformidade

### [327879] Tarefa "CONTRATAÇÃO: Anexar Contrato
"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Inserir Contrato" classes: Instrumento Contratual Assinado — RequeridoInicial=true

### [327880] Tarefa "CONTRATAÇÃO: Minuta Contratual "
Responsável: Favorecido Cobra (papel 277)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Minuta Contratual" classes: Minuta — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
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

### [327881] SubProcesso "CONTRATAÇÃO: Assinatura de Novos Contratos "
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1584; Codigo=MINUTA; PassaTodosItens=true; RetornaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":true}
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- Associação: Ativo=true; FraseAssociacao=Alvo: Assinatura de Novos Contratos; FraseInversaAssociacao=Fonte: Assinatura de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=ASSINATURANOVOSCONTRATOS; SeparadorSequencial=. | fonte: Assinatura de Contrato → alvo: Assinatura de Novos Contratos e Aditivos com Clientes - (Uso exclusivo da GEREL)"

### [327882] SubProcesso "CONTRATAÇÃO: Parecer LGPD"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1579; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
**ExpressaoValor**
```python
OrdemServico.Responsavel
```
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2292; ClasseConfiguracao=Minuta
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer da LGPD; FraseInversaAssociacao=Fonte: Assinatura de contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERLGPDASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Contrato → alvo: Parecer da LGPD

### [327883] EventoFinal ""
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

### NN_CANCELA — Cancela chamado?
DropDownList String → CPE_NEGOCIOS.NN_CANCELA
Itens: Sim;Não

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

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
