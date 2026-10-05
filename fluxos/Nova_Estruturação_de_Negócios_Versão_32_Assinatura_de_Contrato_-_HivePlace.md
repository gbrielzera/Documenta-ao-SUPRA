# Fluxo: Assinatura de Contrato - HivePlace (1718) — versão 32
Caminho: Fluxos > Nova Estruturação de Negócios Versão 32 Assinatura de Contrato - HivePlace
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_32_Assinatura_de_Contrato_-_HivePlace.xml` | Supravizio 19.1.1 | SubProcessoId 20710 | DesenhoProcessoId 2906 | ProcessoId 79
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: HIVEPlace (Assinatura de Contrato e Aditivação de Contrato) (HIVEPLACE)

## Grafo do fluxo
- [329792] EventoInicial "" {Responsável atual} → [329798] CONTRATAÇÃO: Minuta Contratual 
- [329800] SubProcesso "CONTRATAÇÃO: Parecer LGPD" {Responsável atual} → [329795] CONTRATAÇÃO: Parecer Cibernético
- [329801] EventoFinal "" {Responsável atual} → (fim)
- [329794] SubProcesso "PRECIFICAÇÃO: Parecer jurídico" {Responsável atual} → [329796] CONTRATAÇÂO: Parecer de Risco
- [329795] SubProcesso "CONTRATAÇÃO: Parecer Cibernético" {Responsável atual} → [329794] PRECIFICAÇÃO: Parecer jurídico
- [329796] SubProcesso "CONTRATAÇÂO: Parecer de Risco" {Responsável atual} → [329797] CONTRATAÇÃO: Anexar Contrato

- [329797] Tarefa "CONTRATAÇÃO: Anexar Contrato
" {Responsável atual} → [329801] 
- [329798] Tarefa "CONTRATAÇÃO: Minuta Contratual " {Favorecido Cobra} → [329800] CONTRATAÇÃO: Parecer LGPD

## Atividades

### [329792] EventoInicial ""
Responsável: Responsável atual (papel 36)
Config: Configuracao={"ServicoIniciador":"HIVEPLACE"}
TipoSolicitacao: HivePlace - Assinatura ou Aditivação de Contrato.
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
Formulario["COMBOBOX__1"].Itens = "Novo Contrato;Aditivo;Renovação;Recontratação"
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Proposta Comercial" classes: Arquivo 01 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Ata de Reunião do Comitê HIVEPlace
" classes: Arquivo 03 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Outros documentos pertinentes" classes: Arquivo — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Nota Técnica de Aprovação do Negócio
" classes: Arquivo 02 — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - NN_RISCO_AMBIENTAL "Premissas/Restrições/Volumetria" [Memo String(2000) → CP_ORDEM_SERVICO.NN_RISCO_AMBIENTAL] obrigatório
  - NN_OBJETO_PROPOSTA "Objetivo do Negócio" [Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA] obrigatório
  - DESCRICAO2 "Detalhamento POC/Piloto/Degustação" [Memo String(2000) → CP_ORDEM_SERVICO.DESCRICAO2] obrigatório
  - CNPJ_FORNECEDOR "CNPJ" [TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - PRAZO_FINAL "Prazo do Contrato Estimado" [DatePicker DateTime → CP_ORDEM_SERVICO.PRAZO_FINAL] obrigatório
  - GESTOR "Gestor do Produto - GEDIV" [DropDownList String → CPE_PESSOAS.GESTOR] obrigatório
  - NOME_NOME "Cliente" [TextBox String(100) → CPE_PESSOAS.NOME_NOME] obrigatório
  - SIM_NAO "Teve POC/Piloto/Degustação" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - COMBOBOX__1 "Tipo de Contrato" [DropDownList String → CPE_CSC.COMBOBOX__1] obrigatório

### [329800] SubProcesso "CONTRATAÇÃO: Parecer LGPD"
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
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer da LGPD; FraseInversaAssociacao=Fonte: Assinatura de contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERLGPDASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Contrato - HivePlace → alvo: Parecer da LGPD

### [329801] EventoFinal ""
Responsável: Responsável atual (papel 36)

### [329794] SubProcesso "PRECIFICAÇÃO: Parecer jurídico"
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
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer Jurídico; FraseInversaAssociacao=Fonte: Assinatura de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERJURIDICOASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Contrato - HivePlace → alvo: Parecer Orçamentário

### [329795] SubProcesso "CONTRATAÇÃO: Parecer Cibernético"
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
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer Cibernético; FraseInversaAssociacao=Fonte: Assinatura de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERCYBERASSINATURA; SeparadorSequencial=. | fonte: Assinatura de Contrato - HivePlace → alvo: Parecer Cibernético

### [329796] SubProcesso "CONTRATAÇÂO: Parecer de Risco"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1585; RetornaTodosItens=true
- ValoresInputs:
  - PropertyId=1311; Property=Cliente
- Associação: Ativo=true; FraseAssociacao=Alvo: Parecer de Risco; FraseInversaAssociacao=Fonte: Assinatura de Contrato; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=PARECERDERISCOASSINATURA | fonte: Assinatura de Contrato - HivePlace → alvo: Parecer Conformidade

### [329797] Tarefa "CONTRATAÇÃO: Anexar Contrato
"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Inserir Contrato" classes: Instrumento Contratual Assinado — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [329798] Tarefa "CONTRATAÇÃO: Minuta Contratual "
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

### NN_RISCO_AMBIENTAL — Risco Ambiental
Memo String(2000) → CP_ORDEM_SERVICO.NN_RISCO_AMBIENTAL

### NN_OBJETO_PROPOSTA — Objetivo da Proposta
Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA

### DESCRICAO2 — Continuação da Análise Audit
Memo String(2000) → CP_ORDEM_SERVICO.DESCRICAO2

### CNPJ_FORNECEDOR — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ_FORNECEDOR

### PRAZO_FINAL — Prazo final
DatePicker DateTime → CP_ORDEM_SERVICO.PRAZO_FINAL
Descrição: Caso a recomendação já tenha sido reprogramada, indicar o prazo de vencimento deferido na última reprogramação.

### GESTOR — Gestor
DropDownList String → CPE_PESSOAS.GESTOR
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### NOME_NOME — Campo para Nome
TextBox String(100) → CPE_PESSOAS.NOME_NOME

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### COMBOBOX__1 — COMBOBOX__1
DropDownList String → CPE_CSC.COMBOBOX__1
Itens: IPTU;Alvará Funcionamento;Vigilância Sanitária;AVCB/Bombeiros;Taxa Municipal;Taxa Estadual;Taxa Federal;Outros

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
