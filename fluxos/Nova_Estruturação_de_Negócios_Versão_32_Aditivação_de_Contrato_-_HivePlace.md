# Fluxo: Aditivação de Contrato - HivePlace (1719) — versão 32
Caminho: Fluxos > Nova Estruturação de Negócios Versão 32 Aditivação de Contrato - HivePlace
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_32_Aditivação_de_Contrato_-_HivePlace.xml` | Supravizio 19.1.1 | SubProcessoId 20707 | DesenhoProcessoId 2906 | ProcessoId 79
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: HIVEPlace (Assinatura de Contrato e Aditivação de Contrato) (HIVEPLACE)

## Grafo do fluxo
- [329774] EventoFinal "" {Responsável atual} → (fim)
- [329769] Tarefa "Adicionamento do supravizio" {Responsável atual} → [329773] CONTRATAÇÃO: Minuta Contratual de Aditivação
- [329770] EventoInicial "" → [329769] Adicionamento do supravizio
- [329772] SubProcesso "CONTRATAÇÂO: Parecer de Risco" {Responsável atual} → [329775] Formalização interna
- [329773] Tarefa "CONTRATAÇÃO: Minuta Contratual de Aditivação" {Favorecido Cobra} → [329772] CONTRATAÇÂO: Parecer de Risco
- [329775] Tarefa "Formalização interna" {Responsável atual} → [329774] 

## Atividades

### [329774] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [329769] Tarefa "Adicionamento do supravizio"
Responsável: Responsável atual (papel 36)

### [329770] EventoInicial ""
Config: Configuracao={"ServicoIniciador":"HIVEPLACE"}
TipoSolicitacao: HivePlace - Assinatura ou Aditivação de Contrato.
- Operação PR0004 Associar Itens Configuração
  - anexo "Outros Documentos pertinentes" classes: Arquivo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Técnica de Aprovação do Aditivo" classes: Arquivo 01 — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CNPJ "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - GESTOR "Gestor do Produto - GEDIV" [DropDownList String → CPE_PESSOAS.GESTOR] obrigatório
  - NOME_NOME "Cliente" [TextBox String(100) → CPE_PESSOAS.NOME_NOME] obrigatório
  - NUM_VERSAO "DGCO Vigente" [TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO] obrigatório
    - coluna NUMERO obrigatório
    - coluna NUMERONF obrigatório
  - NN_OBJETO_PROPOSTA "Objetivo do Negócio/Aditivo" [Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Ata do Coges" classes: Arquivo 02 — RequeridoInicial=true

### [329772] SubProcesso "CONTRATAÇÂO: Parecer de Risco"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1586; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer de Risco; FraseInversaAssociacao=Fonte: Aditivação de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERDERISCOADITIVACAO | fonte: Aditivação de Contrato - HivePlace → alvo: Parecer Conformidade

### [329773] Tarefa "CONTRATAÇÃO: Minuta Contratual de Aditivação"
Responsável: Favorecido Cobra (papel 277)
**ScriptFormCarregado**
```python
Formulario['NN_CANCELA'].Itens = 'Sim;Não'
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Minuta Contratual" classes: Minuta — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Formulário de Cancelamento
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

### [329775] Tarefa "Formalização interna"
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

### CNPJ — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ

### GESTOR — Gestor
DropDownList String → CPE_PESSOAS.GESTOR
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### NOME_NOME — Campo para Nome
TextBox String(100) → CPE_PESSOAS.NOME_NOME

### NUM_VERSAO — Número da Posição
TextBox Integer → CP_ORDEM_SERVICO.NUM_VERSAO

### NN_OBJETO_PROPOSTA — Objetivo da Proposta
Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA

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
