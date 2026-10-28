# Fluxo: Base de Informações Técnicas (BIT) — versão 5
Caminho: Fluxos > Base de Informações Técnicas Versão 5 Base de Informações Técnicas
XML: `XMLs para teste/Base_de_Informações_Técnicas_Versão_5_Base_de_Informações_Técnicas.xml` | Supravizio 19.1.1 | SubProcessoId 23245 | DesenhoProcessoId 3028 | ProcessoId 762
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Base de Informações Técnicas; CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Suporte Técnico (SUPORTETECNICO)

## Grafo do fluxo
- [370747] Tarefa "Aprovação da Equipe Técnica" {Equipe Técnica} → [G82964] Aprovado?
- [370748] EventoInicial "" {Cliente} → [370747] Aprovação da Equipe Técnica
- [370749] Tarefa "Aprovação Administrativa" {Aprovação Final BIT} → [G82965] Aprovado?
- [370752] EventoFinal "Cancelado" → (fim)
- [370753] EventoIntermediarioMensagem "Reprovado" → [370752] Cancelado
- [370754] EventoFinal "" → (fim)
- [370756] Tarefa "Publicar conteúdo no BIT" {Cliente} → [370749] Aprovação Administrativa
- [370755] Tarefa "Ajustar solicitação" {Cliente} → [370747] Aprovação da Equipe Técnica
- [G82964] Gateway "Aprovado?" → «Aprovado» [370756] Publicar conteúdo no BIT | «Reprovado» [370755] Ajustar solicitação
- [G82965] Gateway "Aprovado?" → «Aprovado» [370754]  | «Reprovado» [370753] Reprovado

## Gateways
### [G82964] Aprovado? (DataBasedExclusiveDecision)
Codigo=TECNICOS
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVA")
```
- alternativa → [370756] Publicar conteúdo no BIT: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [370755] Ajustar solicitação: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G82965] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVACAO")
```
- alternativa → [370754] : OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [370753] Reprovado: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [370747] Tarefa "Aprovação da Equipe Técnica"
Responsável: Equipe Técnica (papel 1425)
Config: Codigo=APROVA
- Operação PR0002 Aprovar: MinimoAprovadores=1; ReprovarImediato=true
  - (aprovação) SIM_NAO_100 "Equipe Aprova?" [DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100]
  - item para aprovação "Anexar Contrato"
  - aprovador: Equipe Técnica (Unico)

### [370748] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"SUPORTETECNICO"}
TipoSolicitacao: Base de Informações Técnicas
**ScriptFormCarregado**
```python
Formulario['COMBOBOX'].Itens = "Infográficos: vídeos curtos, cards ou orientações;Infográficos: boletins técnicos e documentos gerais;FAQ's e fluxograma;Video tutorial; Manual"

Formulario['COMBOBOX__1'].Itens = "Baixa;Média;Alta"

Formulario['COMBOBOX_II'].Itens = "Novo;Atualização"
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Contrato" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true
- Operação PR0001 Preencher Campos
  - COMBOBOX "Tipo de Documento/Material" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
#if Formulario["COMBOBOX"].Valor == "Manual":
#    Formulario["COMBOBOX__1"].Itens = "Baixa;Alta"
#
#elif Formulario["COMBOBOX"].Valor == "POP":
#    Formulario["COMBOBOX__1"].Itens = "Baixa;Alta"  
#
#elif Formulario["COMBOBOX"].Valor == "PRO":
#    Formulario["COMBOBOX__1"].Itens = "Média;Baixa" 
#
#elif Formulario["COMBOBOX"].Valor == "Infográficos: vídeos curtos, cards ou orientações":
#    Formulario["COMBOBOX__1"].Itens = "Baixa"
#
#elif Formulario["COMBOBOX"].Valor == "Infográficos: boletins técnicos e documentos gerais" or Formulario["COMBOBOX"].Valor == "FAQ's e fluxograma":
#    Formulario["COMBOBOX__1"].Itens = "Média"
#
#elif Formulario["COMBOBOX"].Valor == "Vídeo tutorial":
#    Formulario["COMBOBOX__1"].Itens = "Alta"

#Ações

#if Formulario["COMBOBOX"].Valor == "Manual" or Formulario["COMBOBOX"].Valor == "POP" or Formulario["COMBOBOX"].Valor == "PRO":
    #Formulario["COMBOBOX_II"].Itens = "Novo;Atualização"

#else:
    #Formulario["COMBOBOX_II"].Itens = "Novo;Atualização"
```
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - COMBOBOX__1 "Complexidade" [DropDownList String → CPE_CSC.COMBOBOX__1] obrigatório
  - COMBOBOX_II "Ação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório

### [370749] Tarefa "Aprovação Administrativa"
Responsável: Aprovação Final BIT (papel 1426)
Config: Codigo=APROVACAO
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO3 "Aprovação final" [DropDownList String → CPE_CSC.SIM_NAO3]
  - item para aprovação ""
  - aprovador: Aprovação Final BIT (Unico)

### [370752] EventoFinal "Cancelado"

### [370753] EventoIntermediarioMensagem "Reprovado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aviso de reprovação de chamados
Corpo do comunicado: Prezado(a) OrdemServico.Cliente.Nome ,
A Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto não foi aprovada.
 Complemento1 
Para obter mais detalhes sobre a solicitação e a reprovação, CLIQUE no link =>> Link.Consulta 
Central de Serviços

### [370754] EventoFinal ""

### [370756] Tarefa "Publicar conteúdo no BIT"
Responsável: Cliente (papel 18)
- Operação PR0001 Preencher Campos
  - LINK_PROCESSO "Link do conteúdo publicado" [TextBox String → CPE_CJUR.LINK_PROCESSO] obrigatório

### [370755] Tarefa "Ajustar solicitação"
Responsável: Cliente (papel 18)
**ScriptFormCarregado**
```python
Formulario['DESCRICAO_DETALHADA'].Valor = OrdemServico.ObtemMotivoGateway('TECNICOS').ToString()

Formulario['COMBOBOX'].Itens = "Infográficos: vídeos curtos, cards ou orientações;Infográficos: boletins técnicos e documentos gerais;FAQ's e fluxograma;Video tutorial; Manual"

Formulario['COMBOBOX__1'].Itens = "Baixa;Média;Alta"

Formulario['COMBOBOX_II'].Itens = "Novo;Atualização"

for controle in Formulario.Controles.Keys:
    Formulario[controle].Habilitado = True
```
- Operação PR0001 Preencher Campos
  - DESCRICAO_DETALHADA "Observações da equipe técnica" [Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA]
- Operação PR0001 Preencher Campos
  - COMBOBOX "Tipo de Documento/Material" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
#if Formulario["COMBOBOX"].Valor == "Manual":
#    Formulario["COMBOBOX__1"].Itens = "Baixa;Alta"
#
#elif Formulario["COMBOBOX"].Valor == "POP":
#    Formulario["COMBOBOX__1"].Itens = "Baixa;Alta"  
#
#elif Formulario["COMBOBOX"].Valor == "PRO":
#    Formulario["COMBOBOX__1"].Itens = "Média;Baixa" 
#
#elif Formulario["COMBOBOX"].Valor == "Infográficos: vídeos curtos, cards ou orientações":
#    Formulario["COMBOBOX__1"].Itens = "Baixa"
#
#elif Formulario["COMBOBOX"].Valor == "Infográficos: boletins técnicos e documentos gerais" or Formulario["COMBOBOX"].Valor == "FAQ's e fluxograma":
#    Formulario["COMBOBOX__1"].Itens = "Média"
#
#elif Formulario["COMBOBOX"].Valor == "Vídeo tutorial":
#    Formulario["COMBOBOX__1"].Itens = "Alta"

#Ações

#if Formulario["COMBOBOX"].Valor == "Manual" or Formulario["COMBOBOX"].Valor == "POP" or Formulario["COMBOBOX"].Valor == "PRO":
    #Formulario["COMBOBOX_II"].Itens = "Novo;Atualização"

#else:
    #Formulario["COMBOBOX_II"].Itens = "Novo;Atualização"
```
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - COMBOBOX__1 "Complexidade" [DropDownList String → CPE_CSC.COMBOBOX__1] obrigatório
  - COMBOBOX_II "Ação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Contrato" classes: Anexo — RequeridoInicial=true; IncluirPaginaAssinatura=true

## Papéis usados
### papel 1425: Equipe Técnica
Tipo=RelacaoPessoas | pessoas: EMERSON SILVA SANTOS, RAFAEL DA SILVA VIAL
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1426: Aprovação Final BIT
Tipo=RelacaoPessoas | pessoas: ELIANE MACHAJEVSKI

## Campos customizados usados (definição global)

### SIM_NAO_100 — Sim ou Não
DropDownList String(500) → CPE_CONTRATOS02.SIM_NAO_100
Itens: Sim;Não

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### COMBOBOX__1 — COMBOBOX__1
DropDownList String → CPE_CSC.COMBOBOX__1
Itens: IPTU;Alvará Funcionamento;Vigilância Sanitária;AVCB/Bombeiros;Taxa Municipal;Taxa Estadual;Taxa Federal;Outros

### COMBOBOX_II — COMBOBOX_II
DropDownList String → CPE_BOOTCAMP.COMBOBOX_II

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

### LINK_PROCESSO — Link do Teor do Processo
TextBox String → CPE_CJUR.LINK_PROCESSO

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(2000) → CPE_CSC.DESCRICAO_DETALHADA

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
