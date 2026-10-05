# Fluxo: Base de Informações Técnicas (BIT) — versão 1
Caminho: Fluxos > Base de Informações Técnicas Versão 1 Base de Informações Técnicas
XML: `XMLs para teste/Base_de_Informações_Técnicas_Versão_1_Base_de_Informações_Técnicas.xml` | Supravizio 19.1.1 | SubProcessoId 20552 | DesenhoProcessoId 2890 | ProcessoId 762
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Suporte Técnico (SUPORTETECNICO)

## Grafo do fluxo
- [327752] EventoInicial "" {Cliente} → [327754] Anexo de Infográficos
- [327754] Tarefa "Anexo de Infográficos" {Cliente} → [327755] Aprovação da Equipe Técnica
- [327756] Tarefa "Aprovação Eliane" {Cliente} → [327757] Sucesso
- [327757] EventoFinal "Sucesso" → (fim)
- [327755] Tarefa "Aprovação da Equipe Técnica" {Cliente} → [327756] Aprovação Eliane

## Atividades

### [327752] EventoInicial ""
Responsável: Cliente (papel 18)
Config: Configuracao={"ServicoIniciador":"SUPORTETECNICO"}
TipoSolicitacao: Base de Informações Técnicas
**ScriptFormCarregado**
```python
Formulario["COMBOBOX"].Itens = "Infográficos: vídeos curtos, cards ou orientações;Infográficos: boletins técnicos e documentos gerais;FAQ's e fluxograma;Vídeo tutorial;PRO;POP;Manual"
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - COMBOBOX "Tipo de Documento/Material" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
if Formulario["COMBOBOX"].Valor == "Manual":
    Formulario["COMBOBOX__1"].Itens = "Baixa;Alta"
    
elif Formulario["COMBOBOX"].Valor == "POP":
    Formulario["COMBOBOX__1"].Itens = "Baixa;Alta"  

elif Formulario["COMBOBOX"].Valor == "PRO":
    Formulario["COMBOBOX__1"].Itens = "Média;Baixa" 

elif Formulario["COMBOBOX"].Valor == "Infográficos: vídeos curtos, cards ou orientações":
    Formulario["COMBOBOX__1"].Itens = "Baixa"

elif Formulario["COMBOBOX"].Valor == "Infográficos: boletins técnicos e documentos gerais" or Formulario["COMBOBOX"].Valor == "FAQ's e fluxograma":
    Formulario["COMBOBOX__1"].Itens = "Média"

elif Formulario["COMBOBOX"].Valor == "Vídeo tutorial":
    Formulario["COMBOBOX__1"].Itens = "Alta"

#Ações

if Formulario["COMBOBOX"].Valor == "Manual" or Formulario["COMBOBOX"].Valor == "POP" or Formulario["COMBOBOX"].Valor == "PRO":
    Formulario["COMBOBOX_II"].Itens = "Criação;Atualização"

else:
    Formulario["COMBOBOX_II"].Itens = "Criação"
```
  - COMBOBOX__1 "Complexidade" [DropDownList String → CPE_CSC.COMBOBOX__1] obrigatório
**COMBOBOX__1.ScriptModificado**
```python
if Formulario["COMBOBOX"].Valor == "Infográficos: boletins técnicos e documentos gerais" or Formulario["COMBOBOX"].Valor == "FAQ's e fluxograma" or Formulario["COMBOBOX"].Valor == "Infográficos: vídeos curtos, cards ou orientações":
    Formulario["COMBOBOX_II"].Itens = "Criação"

elif Formulario["COMBOBOX"].Valor == "Manual" and Formulario["COMBOBOX__1"].Valor == "Alta":
    Formulario["COMBOBOX_II"].Itens = "Criação"

elif Formulario["COMBOBOX"].Valor == "Manual" and Formulario["COMBOBOX__1"].Valor == "Baixa":
    Formulario["COMBOBOX_II"].Itens = "Atualização"

elif Formulario["COMBOBOX"].Valor == "POP" and Formulario["COMBOBOX__1"].Valor == "Alta":
    Formulario["COMBOBOX_II"].Itens = "Criação"

elif Formulario["COMBOBOX"].Valor == "POP" and Formulario["COMBOBOX__1"].Valor == "Baixa":
    Formulario["COMBOBOX_II"].Itens = "Atualização"

elif Formulario["COMBOBOX"].Valor == "PRO" and Formulario["COMBOBOX__1"].Valor == "Média":
    Formulario["COMBOBOX_II"].Itens = "Criação"
    
elif Formulario["COMBOBOX"].Valor == "PRO" and Formulario["COMBOBOX__1"].Valor == "Baixa":
    Formulario["COMBOBOX_II"].Itens = "Atualização"
```
  - COMBOBOX_II "Ação" [DropDownList String → CPE_BOOTCAMP.COMBOBOX_II] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Contrato" classes: Anexo — ExibicaoAutomaticaAA=true; RequeridoInicial=true; IncluirPaginaAssinatura=true

### [327754] Tarefa "Anexo de Infográficos"
Responsável: Cliente (papel 18)
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexar Infográfico" classes: Arquivo — RequeridoInicial=true; IncluirPaginaAssinatura=true

### [327756] Tarefa "Aprovação Eliane"
Responsável: Cliente (papel 18)
- Operação PR0002 Aprovar
  - (aprovação) SIM_NAO3 "Aprovação final" [DropDownList String → CPE_CSC.SIM_NAO3]
  - aprovador: Aprovação Final BIT (Unico)

### [327757] EventoFinal "Sucesso"

### [327755] Tarefa "Aprovação da Equipe Técnica"
Responsável: Cliente (papel 18)
- Operação PR0002 Aprovar: MinimoAprovadores=1
  - (aprovação) SIM_NAO_100 "Equipe Aprova?" [DropDownList String → CPE_CONTRATOS02.SIM_NAO_100]
  - aprovador: Equipe Técnica (Unico)

## Papéis usados
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
### papel 1425: Equipe Técnica
Tipo=RelacaoPessoas | pessoas: HILTON SANTIAGO LORCA, DANUZIO FERREIRA TENORIO

## Campos customizados usados (definição global)

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX

### COMBOBOX__1 — COMBOBOX__1
DropDownList String → CPE_CSC.COMBOBOX__1
Itens: IPTU;Alvará Funcionamento;Vigilância Sanitária;AVCB/Bombeiros;Taxa Municipal;Taxa Estadual;Taxa Federal;Outros

### COMBOBOX_II — COMBOBOX_II
DropDownList String → CPE_BOOTCAMP.COMBOBOX_II

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

### SIM_NAO_100 — Sim ou Não
DropDownList String → CPE_CONTRATOS02.SIM_NAO_100
Itens: Sim;Não

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
