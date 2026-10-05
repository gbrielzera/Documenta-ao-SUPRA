# Fluxo: Base de Informações Técnicas (BIT) — versão 2
Caminho: Fluxos > Base de Informações Técnicas Versão 2 Base de Informações Técnicas
XML: `XMLs para teste/Base_de_Informações_Técnicas_Versão_2_Base_de_Informações_Técnicas.xml` | Supravizio 19.1.1 | SubProcessoId 21502 | DesenhoProcessoId 2970 | ProcessoId 762
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Base de Informações Técnicas; CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Suporte Técnico (SUPORTETECNICO)

## Grafo do fluxo
- [341946] EventoInicial "" {Cliente} → [341947] Aprovação da Equipe Técnica
- [341947] Tarefa "Aprovação da Equipe Técnica" {Equipe Técnica} → [341949] Aprovação Eliane
- [341949] Tarefa "Aprovação Eliane" {Aprovação Final BIT} → [341950] Sucesso
- [341950] EventoFinal "Sucesso" → (fim)

## Atividades

### [341946] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"SUPORTETECNICO"}
TipoSolicitacao: Base de Informações Técnicas
**ScriptFormCarregado**
```python
Formulario['COMBOBOX'].Itens = "Infográficos: vídeos curtos, cards ou orientações;Infográficos: boletins técnicos e documentos gerais;FAQ's e fluxograma;Video tutorial; Manual"

Formulario['COMBOBOX__1'].Itens = "Baixa;Média;Alta"

Formulario['COMBOBOX_II'].Itens = "Novo;Atualização"
```
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
  - anexo "Anexar Contrato" classes: Anexo — RequeridoInicial=true

### [341947] Tarefa "Aprovação da Equipe Técnica"
Responsável: Equipe Técnica (papel 1425)
- Operação PR0002 Aprovar: MinimoAprovadores=1
  - (aprovação) SIM_NAO_100 "Equipe Aprova?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO_100]
  - aprovador: Equipe Técnica (Unico)

### [341949] Tarefa "Aprovação Eliane"
Responsável: Aprovação Final BIT (papel 1426)
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO3 "Aprovação final" [DropDownList String → CPE_CSC.SIM_NAO3]
  - aprovador: Aprovação Final BIT (Unico)

### [341950] EventoFinal "Sucesso"

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1425: Equipe Técnica
Tipo=RelacaoPessoas | pessoas: HILTON SANTIAGO LORCA, DANUZIO FERREIRA TENORIO
### papel 1426: Aprovação Final BIT
Tipo=RelacaoPessoas | pessoas: ELIANE MACHAJEVSKI

## Campos customizados usados (definição global)

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX

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

### SIM_NAO_100 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO_100
Itens: Sim;Não

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
