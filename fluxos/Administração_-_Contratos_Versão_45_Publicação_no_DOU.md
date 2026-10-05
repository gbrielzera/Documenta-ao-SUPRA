# Fluxo: Publicação no DOU (PUBLICARDOU) — versão 45
Caminho: Fluxos > Administração - Contratos Versão 45 Publicação no DOU
XML: `XMLs para teste/Administração_-_Contratos_Versão_45_Publicação_no_DOU.xml` | Supravizio 19.1.1 | SubProcessoId 21951 | DesenhoProcessoId 3021 | ProcessoId 127
Órgão dono: 3000003410 - DIVISAO DE PLANEJAMENTO E IMPORTACAO | Responsável: SIMONE CHAVES DE PAULA LEITE
Classe do subprocesso: Objetivo=Publicação no DOU; DescricaoCliente=Publicação no DOU; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Publicação de Aviso de Editais (Licitação, Credenciamento, Chamamento Público, Consulta Pública) (PUBAVISOEDI); Publicação de Aviso de Rescisão, Distrato, Extrato de Contrato, Extrato de Aditivo e Aviso de Retificações (PUBAVISOS); Publicação de Outros Documentos (PUBOUTROSDOC)

## Grafo do fluxo
- [348512] Tarefa "Iniciar tratamento da demanda" {Fila CSC - Contratos} → [348519] Informar dados do Lançamento do RI

- [348513] LinkInicial "Deslocamento a Serviço" → [348512] Iniciar tratamento da demanda
- [348514] EventoInicial "Publicação no DOU" → [348512] Iniciar tratamento da demanda
- [348515] LinkInicial "" → [348512] Iniciar tratamento da demanda
- [348516] Tarefa "Consultar publicação" {Responsável atual} → [348517] 
- [348517] EventoFinal "" {Responsável atual} → (fim)
- [348518] SubProcesso "Abertura de OS para Financeiro - Contas a Pagar" {Responsável atual} → [348516] Consultar publicação
- [348519] Tarefa "Informar dados do Lançamento do RI
" {Responsável atual} → [348518] Abertura de OS para Financeiro - Contas a Pagar

## Atividades

### [348512] Tarefa "Iniciar tratamento da demanda"
Responsável: Fila CSC - Contratos (papel 688)

### [348513] LinkInicial "Deslocamento a Serviço"
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - COTACAO_DOLAR "Cotação do Dólar americano (USD) " [TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR] obrigatório
  - DESC_COLABORADOR_DESLOCAMENTO "Tipo de Colaborador" [TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO] obrigatório
  - CARGO_DESLOCAMENTO "Cargo" [TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO] obrigatório
  - CIDADE_DESTINO_INTERNACIONAL "Cidade/País de Destino" [TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL] obrigatório
  - TIPO_DESLOCAMENTO "Tipo de Deslocamento" [DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO] obrigatório
  - CIDADE_ORIGEM "Cidade de Origem" [DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM] obrigatório
  - DIARIA_COTACAO_REAL "Diária em Real" [TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL] obrigatório
  - FAVORECIDO_DESLOCAMENTO "Favorecido" [DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO] obrigatório
  - VALOR_TOTAL_DIARIA "Valor total de diárias R$" [TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA] obrigatório
  - FUNCAO_DESLOCAMENTO "Função" [TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO] obrigatório
  - MATRICULA_DESLOCAMENTO "Matrícula" [TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO] obrigatório
  - NUMERO_NT "Número da Nota Técnica" [TextBox String → CPE_CONTRATOS.NUMERO_NT] obrigatório
  - PAIS "País" [DropDownList String → CPE_DESLOCAMENTO.PAIS] obrigatório
  - RETORNO_DIA "Retorno dia" [DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA] obrigatório
  - RETORNO_HORA "Horário do Retorno" [TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA] obrigatório
  - SAIDA "Saída dia" [DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA] obrigatório
  - SAIDA_HORA "Horário da Saída" [TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA] obrigatório
  - OBJETIVO_VIAGEM "Objetivo / Informações Adicionais:" [TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM] obrigatório
- Associação de subprocesso: AssociacaoId=1373; Nome=ADIR CORDEIRO DOS SANTOS FILHO; FraseAssociacao=Deslocamento a Serviço -> Publicação no DOU

### [348514] EventoInicial "Publicação no DOU"
TipoSolicitacao: 05.04. Suprimentos Corporativos, Licitações e Contratos - Contratos
**ScriptFormCarregado**
```python
Formulario['DGCO_BB'].Visivel = False
```
- Operação PR0001 Preencher Campos
  - DATA_EMISSAO_NF "Data desejada para a Publicação (Quando a data para publicação não for informada, a mesma ocorrerá no dia útil seguinte ao registro no site da Imprensa Nacional):" [DatePicker DateTime → CPE_CSC.DATA_EMISSAO_NF]
  - POSSUI_DGCO "Possui DGCO?" [DropDownList String → CPE_CSC.POSSUI_DGCO] obrigatório
**POSSUI_DGCO.ScriptModificado**
```python
if Formulario['POSSUI_DGCO'].Valor == "Sim":
    Formulario['DGCO_BB'].Visivel = True
    Formulario['DGCO_BB'].Habilitado = True
   
    
if Formulario['POSSUI_DGCO'].Valor != "Sim":
    Formulario['DGCO_BB'].Visivel = False  
    Formulario['DGCO_BB'].Habilitado = False
```
  - DGCO_BB "Número do DGCO:" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório — Configuracao={"Mascara":"00000/0000"}
    - coluna NUMERO_SERIE_PATRI obrigatório
    - coluna DESCRICAO_PATRIMONIO obrigatório
    - coluna CONDICAO_USO obrigatório
    - coluna NUMERO_PATRIMONIO obrigatório
  - LABEL1 "Obs: A Ordem de Serviço será fechada após a efetiva publicação no DOU juntamente com a inclusão do certificado anexo." [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - NOME_FORNECEDOR "Informar o tipo da publicação e o DGCO (Ex: Extrato de Contrato)" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=PEDIDO DE PUBLICAÇÃO
  - anexo "Pedido de Publicação no DOU (Arquivos no formato .rtf)" classes: Pedido de Publicação no DOU — RequeridoInicial=true

### [348515] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - LABEL1 "Descrição Detalhada:" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
  - DATA1 "Data de Publicação no DOU" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA1] obrigatório
- Associação de subprocesso: AssociacaoId=386; Nome=RAPHAEL GRUPILO NASCIMENTO; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Publicação no DOU

### [348516] Tarefa "Consultar publicação"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração: Nome=EXTRATO DA PUBLICAÇÃO
  - anexo "Extrato de Publicação" classes: Extrato da Publicação no DOU — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=MATÉRIA CERTIFICADA
  - anexo "Matéria Certificada" classes: Matéria Certificada — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - OBS1 "Observação" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - DATA_ENTREGA "Data da Publicação" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENTREGA] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=RECIBO DA PUBLICAÇÃO
  - anexo "Recibo da Publicação" classes: Recibo da Publicação no DOU — RequeridoInicial=true

### [348517] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [348518] SubProcesso "Abertura de OS para Financeiro - Contas a Pagar"
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1110; RetornaTodosItens=true; Configuracao={"ExibirBotaoNovaSubprocessos":false}
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- ValoresInputs:
  - CustomPropertyId=2063; CustomProperty=NUMERO_RI
  - CustomPropertyId=2060; CustomProperty=BOLETO
  - CustomPropertyId=253; CustomProperty=DATA_EMISSAO
- PassagemItens:
  - SuperClasse=Artefato; ClasseConfiguracaoId=2763; ClasseConfiguracao=Anexo
  - SuperClasse=Artefato; ClasseConfiguracaoId=2223; ClasseConfiguracao=Anexo
- Associação: Ativo=true; FraseAssociacao=Publicação do DOU -> Financeiro - Contas a Pagar (Douglas); FraseInversaAssociacao=Financeiro - Contas a Pagar -> Publicação do DOU (Douglas); CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=DOUCONPA; SeparadorSequencial=. | fonte: Publicação no DOU → alvo: Financeiro - Contas a Pagar

### [348519] Tarefa "Informar dados do Lançamento do RI
"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Boleto" classes: Anexo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - NUMERO_RI "Número do RI" [TextBox String → CPE_CSC.NUMERO_RI] obrigatório
  - BOLETO "Valor do Boleto" [TextBox String → CPE_CSC.BOLETO] obrigatório
  - DATA_EMISSAO "Data do Lançamento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO] obrigatório

## Papéis usados
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### COTACAO_DOLAR — Cotação do Dólar americano (USD) 
TextBox String → CPE_DESLOCAMENTO.COTACAO_DOLAR

### DESC_COLABORADOR_DESLOCAMENTO — Tipo de Colaborador
TextBox String → CPE_DESLOCAMENTO.DESC_COLABORADOR_DESLOCAMENTO

### CARGO_DESLOCAMENTO — Cargo
TextBox String → CPE_DESLOCAMENTO.CARGO_DESLOCAMENTO

### CIDADE_DESTINO_INTERNACIONAL — Cidade/País de Destino
TextBox String → CPE_DESLOCAMENTO.CIDADE_DESTINO_INTERNACIONAL

### TIPO_DESLOCAMENTO — Tipo de Deslocamento
DropDownList String → CPE_DESLOCAMENTO.TIPO_DESLOCAMENTO
Itens: Viagem a Serviço - Nacional;Viagem a Serviço - Internacional;Viagem - Assistência Técnica;Treinamento - Assistência Técnica

### CIDADE_ORIGEM — Cidade de Origem
DropDownList String → CPE_DESLOCAMENTO.CIDADE_ORIGEM
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT to_char(id_cidade) as id, c.descricao as cidade FROM cidade_v c ORDER BY c.descricao")
```

### DIARIA_COTACAO_REAL — Diária em Real
TextBox String → CPE_DESLOCAMENTO.DIARIA_COTACAO_REAL

### FAVORECIDO_DESLOCAMENTO — Favorecido
DropDownList String → CPE_DESLOCAMENTO.FAVORECIDO_DESLOCAMENTO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### VALOR_TOTAL_DIARIA — Valor total de diárias R$
TextBox Decimal → CPE_DESLOCAMENTO.VALOR_TOTAL_DIARIA

### FUNCAO_DESLOCAMENTO — Função
TextBox String → CPE_DESLOCAMENTO.FUNCAO_DESLOCAMENTO

### MATRICULA_DESLOCAMENTO — Matrícula
TextBox Integer → CPE_DESLOCAMENTO.MATRICULA_DESLOCAMENTO

### NUMERO_NT — Número da Nota Técnica
TextBox String → CPE_CONTRATOS.NUMERO_NT

### PAIS — País
DropDownList String → CPE_DESLOCAMENTO.PAIS
**LookupScript**
```python
#
```

### RETORNO_DIA — Retorno dia
DatePicker DateTime → CPE_DESLOCAMENTO.RETORNO_DIA

### RETORNO_HORA — Horário do Retorno
TextBox String → CPE_DESLOCAMENTO.RETORNO_HORA

### SAIDA — Saída dia
DatePicker DateTime → CPE_DESLOCAMENTO.SAIDA

### SAIDA_HORA — Horário da Saída
TextBox String → CPE_DESLOCAMENTO.SAIDA_HORA

### OBJETIVO_VIAGEM — Objetivo / Informações Adicionais:
TextBox String → CPE_DESLOCAMENTO.OBJETIVO_VIAGEM

### DATA_EMISSAO_NF — Data da Emissão
DatePicker DateTime → CPE_CSC.DATA_EMISSAO_NF
Descrição: Data da Emissão (Em caso de mais de uma NF, informar a data da NF que foi emitida primeiro)

### POSSUI_DGCO — Possui DGCO?
DropDownList String → CPE_CSC.POSSUI_DGCO
Itens: Sim;Não

### DGCO_BB — DGCO
TextBox String(300) → CPE_FINANCEIRO.DGCO_BB

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### DATA1 — Data
DatePicker DateTime → CP_ORDEM_SERVICO.DATA1

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### DATA_ENTREGA — Data de entrega
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_ENTREGA
Descrição: Data prevista para entrega

### NUMERO_RI — Numero RI
TextBox String → CPE_CSC.NUMERO_RI

### BOLETO — Numero do Boleto
TextBox String → CPE_CSC.BOLETO

### DATA_EMISSAO — Data da Emissão
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_EMISSAO

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
