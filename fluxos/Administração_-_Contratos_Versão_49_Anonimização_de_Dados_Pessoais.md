# Fluxo: Anonimização de Dados Pessoais (ANONIMIZACAO) — versão 49
Caminho: Fluxos > Administração - Contratos Versão 49 Anonimização de Dados Pessoais
XML: `XMLs para teste/Administração_-_Contratos_Versão_49_Anonimização_de_Dados_Pessoais.xml` | Supravizio 19.1.1 | SubProcessoId 23675 | DesenhoProcessoId 3113 | ProcessoId 127
Órgão dono: 3000003410 - DIVISAO DE PLANEJAMENTO E IMPORTACAO | Responsável: SIMONE CHAVES DE PAULA LEITE
Classe do subprocesso: Objetivo=Anonimização de Dados Pessoais; DescricaoCliente=Anonimização de Dados Pessoais - Publicação site BBTS; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadoresGrupo; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Serviço de Anonimização de Dados Pessoais (SRVANONIMIZACAODDPSSAIS)

## Grafo do fluxo
- [379691] EventoFinal "" {Responsável atual} → (fim)
- [379692] Tarefa "Avaliar anonimização
" {Responsável atual} → [G84514] Aprovou?
- [379693] Tarefa "Verificar Solicitação" {Fila CSC - Contratos} → [379694] Anonimizar Documento
- [379694] Tarefa "Anonimizar Documento" {Responsável atual} → [379692] Avaliar anonimização

- [379695] EventoInicial "" → [379693] Verificar Solicitação
- [379696] EventoIntermediarioMensagem "Término da Atividade" → [379691] 
- [379697] LinkInicial "" → [379693] Verificar Solicitação
- [G84514] Gateway "Aprovou?" → «Aprovado» [379696] Término da Atividade | «Reprovado» [379694] Anonimizar Documento

## Gateways
### [G84514] Aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("GERENTECESECBRASILIA")
```
- alternativa → [379696] Término da Atividade: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=1; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [379694] Anonimizar Documento: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=0; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [379691] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [379692] Tarefa "Avaliar anonimização
"
Responsável: Responsável atual (papel 36)
Config: Codigo=GERENTECESECBRASILIA
MotivoInterrupcaoSLA: Aguardando aprovação
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do Documento Anonização da Dados; MinimoAprovadores=1; ReenvioEmailAprovacao=24
  - (aprovação) DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB]
  - (aprovação) SIM_NAO7 "Sim ou Não" [DropDownList String → CPE_CSC.SIM_NAO7]
  - (aprovação) NOME_FORNECEDOR "Nome do Fornecedor/Favorecido" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR]
  - item para aprovação ""
  - aprovador: Analista Disec (Unico)

### [379693] Tarefa "Verificar Solicitação"
Responsável: Fila CSC - Contratos (papel 688)
Config: ConfirmaResponsabilidade=true

### [379694] Tarefa "Anonimizar Documento"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração
  - anexo "Documento Anonimizado" classes: Documento Anonimizado — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - SIM_NAO7 "O contrato anonimizado está salvo como imagem?" [DropDownList String → CPE_CSC.SIM_NAO7] obrigatório

### [379695] EventoInicial ""
TipoSolicitacao: 05.04. Suprimentos Corporativos, Licitações e Contratos - Contratos
- Operação PR0004 Associar Itens Configuração
  - anexo "Contrato ou aditivo assinado" classes: Instrumento Contratual Assinado — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - TIPO_DOCUMENTO "Tipo de Documento" [DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO] obrigatório
  - SIM_NAO5 "O processo de assinatura do instrumento contratual tramitou pela Gesuc?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] obrigatório — Configuracao={"Mascara":"00000/0000"}
  - NOME_FORNECEDOR "Nome Fornecedor" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - RESPONSAVEL_INFORMACAO "Responsável pela Informação" [DropDownList String → CPE_CSC.RESPONSAVEL_INFORMACAO] obrigatório
  - URL1 "Informe a URL da página para publicação do Contrato/Aditivo/ARP/Apostilamento no site da BBTS." [TextBox String → CP_ORDEM_SERVICO.URL1] obrigatório
  - OBS1 "Descrição Detalhada - Relacionada a publicação do Contrato/Aditivo/ARP/Apostilamento no site da BBTS" [Memo String(2000) → CPE_CONTRATOS.OBS1] obrigatório

### [379696] EventoIntermediarioMensagem "Término da Atividade"
Destinatário: Gerente da Dicof (papel 716)
ModeloComunicado: Término da Atividade
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome,
Em atendimento a Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto comunico que foi realizado o término da atividade.
Para mais detalhes sobre esta solicitação Link.Consulta.
Atenciosamente

### [379697] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - URL1 "Informe a URL da página para publicação do Instrumento Contratual no site da BBTS." [TextBox String → CP_ORDEM_SERVICO.URL1]
  - RESPONSAVEL_INFORMACAO "Responsável pela Informação" [DropDownList String → CPE_CSC.RESPONSAVEL_INFORMACAO]
  - OBS2 "Descrição Detalhada" [Memo String(2000) → CPE_CONTRATOS.OBS2]
  - TIPO_DOCUMENTO "Tipo de documento" [DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO]
  - DGCO_BB "DGCO" [TextBox String(300) → CPE_FINANCEIRO.DGCO_BB] — Configuracao={"Mascara":"00000/0000"}
  - SIM_NAO5 "O processo de assinatura do instrumento contratual tramitou pela Gesuc?" [DropDownList String → CPE_CSC.SIM_NAO5] obrigatório
- Associação de subprocesso: AssociacaoId=362; FraseAssociacao=Inserir Documentos Contratuais no Gescon -> Anonimização de Dados Pessoais; Nome=ANONIMIZACAOGESCON

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
### papel 1015: Analista Disec
Tipo=RelacaoPessoas | pessoas: WANESSA PINHEIRO DE OLIVEIRA FERNANDES, ALINE RODRIGUES DE ABREU, PHABRIENNY CRISTINE DE SOUZA
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos
### papel 716: Gerente da Dicof
Tipo=RelacaoOrgaos

## Campos customizados usados (definição global)

### DGCO_BB — DGCO
TextBox String(300) → CPE_FINANCEIRO.DGCO_BB

### SIM_NAO7 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO7
Itens: Sim;Não

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### TIPO_DOCUMENTO — Tipo de documento
DropDownList String → CP_ORDEM_SERVICO.TIPO_DOCUMENTO
Itens: Contrato;Aditivo;Ata de Registro de Preço; Apostilamento; Convênio

### SIM_NAO5 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO5
Itens: Sim;Não

### RESPONSAVEL_INFORMACAO — Responsável pela Informação
DropDownList String → CPE_CSC.RESPONSAVEL_INFORMACAO
**LookupScript**
```python
Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(p.id_pessoa) AS id_pessoa, p.nome || ' (' || p.usuario_rede || ')' AS nomemat FROM PESSOA P where p.ativo = 'Sim' ORDER BY nomemat ")
```

### URL1 — Endereço da Página WEB
TextBox String → CP_ORDEM_SERVICO.URL1

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### OBS2 — Observação2
Memo String(2000) → CPE_CONTRATOS.OBS2
Descrição: Informe

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
