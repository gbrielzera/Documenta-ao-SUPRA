# Fluxo: Cadastro na VOETUR (VOETUR) — versão 39
Caminho: Fluxos > Administração - Passagens Aéreas e ou Hospedagem Versão 39 Cadastro na VOETUR
XML: `XMLs para teste/Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Cadastro_na_VOETUR.xml` | Supravizio 19.1.1 | SubProcessoId 23096 | DesenhoProcessoId 2962 | ProcessoId 103
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Cadastro na VOETUR; CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Cadastro na VOETUR (VOETUR)

## Grafo do fluxo
- [369392] LinkInicial "" → [G82740] Qual ação na VOETUR/ARGO?
- [369393] Tarefa "Cadastrar colaborador no ARGO (consultar e viajar)" {Fila CSC - Serviços Gerais} → [369395] 
- [369396] Tarefa "Cadastrar colaborador no ARGO (consultar)" {Fila CSC - Serviços Gerais} → [369395] 
- [369397] EventoInicial "" → [G82740] Qual ação na VOETUR/ARGO?
- [369395] EventoFinal "" → (fim)
- [369394] Tarefa "Atualizar cargo do colaborador no ARGO" {Fila CSC - Serviços Gerais} → [369395] 
- [G82740] Gateway "Qual ação na VOETUR/ARGO?" → «Cadastro no ARGO (consultar e viajar)» [369393] Cadastrar colaborador no ARGO (consultar e viajar) | «Cadastro no ARGO (consultar)» [369396] Cadastrar colaborador no ARGO (consultar) | «Atualizar cargo» [369394] Atualizar cargo do colaborador no ARGO

## Gateways
### [G82740] Qual ação na VOETUR/ARGO? (EventBasedExclusiveDecision)
Codigo=GATEWAY1
- alternativa → [369393] Cadastrar colaborador no ARGO (consultar e viajar): OperadorDecision=Equal; ReferenciaDecision=Cadastro no ARGO (consultar e viajar); SequenciaAvaliacao=0
- alternativa → [369396] Cadastrar colaborador no ARGO (consultar): OperadorDecision=Equal; ReferenciaDecision=Cadastro no ARGO (consultar); SequenciaAvaliacao=1
- alternativa → [369394] Atualizar cargo do colaborador no ARGO: OperadorDecision=Equal; ReferenciaDecision=Atualizar cargo; SequenciaAvaliacao=2

## Atividades

### [369392] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Associação de subprocesso: AssociacaoId=1686; FraseAssociacao=Nomeação -> VOETUR; Nome=VOETUR

### [369393] Tarefa "Cadastrar colaborador no ARGO (consultar e viajar)"
Responsável: Fila CSC - Serviços Gerais (papel 483)
**ScriptInicio**
```python
lista = DB.ExecuteDataTable( "SELECT " "CP.MATRICULA, " "CP.CPF, " "CP.DATA_NASCIMENTO, " "P.EMAIL, " "C.IDENTIDADE, " "C.SEXO, " "CASE " "WHEN INSTR(C.CARGO, '|') > 0 " "THEN TRIM(SUBSTR(C.CARGO, INSTR(C.CARGO, '|') + 1)) " "ELSE TRIM(C.CARGO) " "END AS CARGO, " "O.SIGLA, " "O.DESCRICAO " "FROM PESSOA P " "INNER JOIN CP_PESSOA CP " "ON CP.ID_PESSOA = P.ID_PESSOA " "INNER JOIN ORGAO O " "ON O.ID_ORGAO = P.ID_ORGAO " "LEFT JOIN CAD_FUNCIONARIO_V C " "ON LTRIM(TRIM(C.MATRICULA), '0') = " "LTRIM(TRIM(TO_CHAR(CP.MATRICULA)), '0') " "AND UPPER(TRIM(C.STATUS_MATRICULA)) = 'ATIVO' " "WHERE P.ID_PESSOA = " + str( int( OrdemServico.GetCustom( "FAVORECIDO_COBRA" ) ) ) )

for linha in lista.Rows:
    OrdemServico.SetCustom("MATRICULA", Convert.ToDecimal(linha["MATRICULA"]))
    OrdemServico.SetCustom("CPF", linha["CPF"].ToString())
    OrdemServico.SetCustom("DATA_NASCIMENTO", linha["DATA_NASCIMENTO"])
    OrdemServico.SetCustom("EMAIL", linha["EMAIL"].ToString())
    OrdemServico.SetCustom("RG", linha["IDENTIDADE"].ToString())
    OrdemServico.SetCustom("SEXO", linha["SEXO"].ToString())
    OrdemServico.SetCustom("CARGO_ATUAL", linha["CARGO"].ToString())
    OrdemServico.SetCustom("TE_UOR", linha["SIGLA"].ToString() + " - " + linha["DESCRICAO"].ToString())
```
- Operação PR0001 Preencher Campos
  - DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_NASCIMENTO] obrigatório
  - SEXO "Sexo" [TextBox String → CP_ORDEM_SERVICO.SEXO] obrigatório
  - FAVORECIDO_COBRA "Nome completo" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - RG "RG" [TextBox String → CPE_CSC.RG] obrigatório
  - CPF "CPF" [TextBox String(15) → CP_ORDEM_SERVICO.CPF] obrigatório
  - TE_UOR "UOR (atual)" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - SCR_TODOS_RH "UOR nova" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
  - CARGO_ATUAL "Cargo (atual)" [TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL] obrigatório
  - FUNCAO_DAS_NOMEA "Cargo novo" [DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA] obrigatório
  - EMAIL "E-mail" [TextBox String → CP_ORDEM_SERVICO.EMAIL] obrigatório

### [369396] Tarefa "Cadastrar colaborador no ARGO (consultar)"
Responsável: Fila CSC - Serviços Gerais (papel 483)
**ScriptInicio**
```python
lista = DB.ExecuteDataTable( "SELECT " "CP.MATRICULA, " "CP.CPF, " "CP.DATA_NASCIMENTO, " "P.EMAIL, " "C.IDENTIDADE, " "C.SEXO, " "CASE " "WHEN INSTR(C.CARGO, '|') > 0 " "THEN TRIM(SUBSTR(C.CARGO, INSTR(C.CARGO, '|') + 1)) " "ELSE TRIM(C.CARGO) " "END AS CARGO, " "O.SIGLA, " "O.DESCRICAO " "FROM PESSOA P " "INNER JOIN CP_PESSOA CP " "ON CP.ID_PESSOA = P.ID_PESSOA " "INNER JOIN ORGAO O " "ON O.ID_ORGAO = P.ID_ORGAO " "LEFT JOIN CAD_FUNCIONARIO_V C " "ON LTRIM(TRIM(C.MATRICULA), '0') = " "LTRIM(TRIM(TO_CHAR(CP.MATRICULA)), '0') " "AND UPPER(TRIM(C.STATUS_MATRICULA)) = 'ATIVO' " "WHERE P.ID_PESSOA = " + str( int( OrdemServico.GetCustom( "FAVORECIDO_COBRA" ) ) ) )

for linha in lista.Rows:
    OrdemServico.SetCustom("MATRICULA", Convert.ToDecimal(linha["MATRICULA"]))
    OrdemServico.SetCustom("CPF", linha["CPF"].ToString())
    OrdemServico.SetCustom("DATA_NASCIMENTO", linha["DATA_NASCIMENTO"])
    OrdemServico.SetCustom("EMAIL", linha["EMAIL"].ToString())
    OrdemServico.SetCustom("RG", linha["IDENTIDADE"].ToString())
    OrdemServico.SetCustom("SEXO", linha["SEXO"].ToString())
    OrdemServico.SetCustom("CARGO_ATUAL", linha["CARGO"].ToString())
    OrdemServico.SetCustom("TE_UOR", linha["SIGLA"].ToString() + " - " + linha["DESCRICAO"].ToString())
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Nome completo" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - RG "RG" [TextBox String → CPE_CSC.RG] obrigatório
  - CPF "CPF" [TextBox String(15) → CP_ORDEM_SERVICO.CPF] obrigatório
  - DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_NASCIMENTO] obrigatório
  - SEXO "Sexo" [TextBox String → CP_ORDEM_SERVICO.SEXO] obrigatório
  - TE_UOR "UOR (atual)" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - SCR_TODOS_RH "UOR nova" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
  - CARGO_ATUAL "Cargo (atual)" [TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL] obrigatório
  - FUNCAO_DAS_NOMEA "Cargo novo" [DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA] obrigatório
  - EMAIL "E-mail" [TextBox String → CP_ORDEM_SERVICO.EMAIL] obrigatório

### [369397] EventoInicial ""
TipoSolicitacao: 08.03. Administração e Patrimônio - Deslocamento a Serviço
**ScriptFormCarregado**
```python
Formulario["COMBOBOX"].Itens = (
    "Cadastro (Consultar + Viajar);"
    "Cadastro (Apenas consultar);"
    "Atualizar Cargo"
)

excecoes = ["COMBOBOX"]
for controle in Formulario.Controles:
    if controle.Key not in excecoes:
        try:
            Formulario[controle.Key].Visivel = False
        except:
            pass

opcao = Formulario["COMBOBOX"].Valor
campos = []
if opcao == "Cadastro (Consultar + Viajar)":
    campos = ["MATRICULA", "FAVORECIDO_COBRA", "RG", "CPF", "DATA_NASCIMENTO",
              "SEXO", "SCR_TODOS_RH", "FUNCAO_DAS_NOMEA", "EMAIL"]
elif opcao == "Cadastro (Apenas consultar)":
    campos = ["FAVORECIDO_COBRA", "MATRICULA", "EMAIL", "SCR_TODOS_RH", "FUNCAO_DAS_NOMEA"]
elif opcao == "Atualizar Cargo":
    campos = ["FAVORECIDO_COBRA", "MATRICULA", "SCR_TODOS_RH", "FUNCAO_DAS_NOMEA"]

for campo in campos:
    Formulario[campo].Visivel = True
```
- Operação PR0001 Preencher Campos
  - COMBOBOX "Selecione o tipo do chamado" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
for controle in Formulario.Controles:
    if controle.Key != "COMBOBOX":
        try:
            Formulario[controle.Key].Visivel = False
        except:
            pass

opcao = Controle.Valor
campos = []
if opcao == "Cadastro (Consultar + Viajar)":
    campos = ["MATRICULA", "FAVORECIDO_COBRA", "RG", "CPF", "DATA_NASCIMENTO",
              "SEXO", "SCR_TODOS_RH", "FUNCAO_DAS_NOMEA", "EMAIL"]
elif opcao == "Cadastro (Apenas consultar)":
    campos = ["FAVORECIDO_COBRA", "MATRICULA", "EMAIL", "SCR_TODOS_RH", "FUNCAO_DAS_NOMEA"]
elif opcao == "Atualizar Cargo":
    campos = ["FAVORECIDO_COBRA", "MATRICULA", "SCR_TODOS_RH", "FUNCAO_DAS_NOMEA"]

for campo in campos:
    Formulario[campo].Visivel = True
```
  - FAVORECIDO_COBRA "Nome completo" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - RG "RG" [TextBox String → CPE_CSC.RG] obrigatório
  - CPF "CPF" [TextBox String(15) → CP_ORDEM_SERVICO.CPF] obrigatório
  - DATA_NASCIMENTO "Data de nascimento" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_NASCIMENTO] obrigatório
  - SEXO "Sexo" [TextBox String → CP_ORDEM_SERVICO.SEXO] obrigatório
  - TE_UOR "UOR (atual)" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - SCR_TODOS_RH "UOR nova" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
  - CARGO_ATUAL "Cargo (atual)" [TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL] obrigatório
  - FUNCAO_DAS_NOMEA "Cargo novo" [DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA] obrigatório
  - EMAIL "E-mail" [TextBox String → CP_ORDEM_SERVICO.EMAIL] obrigatório

### [369395] EventoFinal ""

### [369394] Tarefa "Atualizar cargo do colaborador no ARGO"
Responsável: Fila CSC - Serviços Gerais (papel 483)
**ScriptInicio**
```python
lista = DB.ExecuteDataTable( "SELECT " "CP.MATRICULA, " "CP.CPF, " "CASE " "WHEN INSTR(C.CARGO, '|') > 0 " "THEN TRIM(SUBSTR(C.CARGO, INSTR(C.CARGO, '|') + 1)) " "ELSE TRIM(C.CARGO) " "END AS CARGO, " "O.SIGLA, " "O.DESCRICAO " "FROM PESSOA P " "INNER JOIN CP_PESSOA CP " "ON CP.ID_PESSOA = P.ID_PESSOA " "INNER JOIN ORGAO O " "ON O.ID_ORGAO = P.ID_ORGAO " "LEFT JOIN CAD_FUNCIONARIO_V C " "ON LTRIM(TRIM(C.MATRICULA), '0') = " "LTRIM(TRIM(TO_CHAR(CP.MATRICULA)), '0') " "AND UPPER(TRIM(C.STATUS_MATRICULA)) = 'ATIVO' " "WHERE P.ID_PESSOA = " + str( int( OrdemServico.GetCustom( "FAVORECIDO_COBRA" ) ) ) )

for linha in lista.Rows:
    OrdemServico.SetCustom("MATRICULA", Convert.ToDecimal(linha["MATRICULA"]))
    OrdemServico.SetCustom("CPF", linha["CPF"].ToString())
    OrdemServico.SetCustom("CARGO_ATUAL", linha["CARGO"].ToString())
    OrdemServico.SetCustom("TE_UOR", linha["SIGLA"].ToString() + " - " + linha["DESCRICAO"].ToString())
```
- Operação PR0001 Preencher Campos
  - FAVORECIDO_COBRA "Nome completo" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - CPF "CPF" [TextBox String(15) → CP_ORDEM_SERVICO.CPF] obrigatório
  - TE_UOR "UOR (atual)" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - SCR_TODOS_RH "UOR nova" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
  - CARGO_ATUAL "Cargo (atual)" [TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL] obrigatório
  - FUNCAO_DAS_NOMEA "Cargo novo" [DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA] obrigatório

## Papéis usados
### papel 483: Fila CSC - Serviços Gerais
Tipo=RelacaoPessoas | pessoas: Fila CSC - Serviços Gerais

## Campos customizados usados (definição global)

### DATA_NASCIMENTO — Data de Nascimento
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_NASCIMENTO

### SEXO — Sexo
TextBox String → CP_ORDEM_SERVICO.SEXO

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### RG — RG
TextBox String → CPE_CSC.RG

### CPF — CPF
TextBox String(15) → CP_ORDEM_SERVICO.CPF

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### CARGO_ATUAL — Cargo
TextBox String → CP_ORDEM_SERVICO.CARGO_ATUAL

### FUNCAO_DAS_NOMEA — Função DAS
DropDownList String → CP_ORDEM_SERVICO.FUNCAO_DAS_NOMEA
Descrição: Função
Itens: ANALISTA DE TECNOLOGIA I;
ANALISTA DE TECNOLOGIA II;
ANALISTA DE TECNOLOGIA III;
ANALISTA DE TECNOLOGIA IV;
ASSESSOR JUNIOR;
ASSESSOR EXEC DA PRESIDENCIA;
ASSESSOR MASTER;
ASSESSOR PLENO;
ASSESSOR SENIOR;
DIRETOR;
GERENTE DE AREA I;
GERENTE DE AREA II;
GERENTE DE CENTRO I;
GERENTE DE CENTRO II;
GERENTE DE CENTRO III;
GERENTE DE CENTRO DE TIC I;
GERENTE DE CENTRO DE TIC II;
GERENTE DE DIVISAO;
GERENTE EXECUTIVO;
GERENTE DE GRUPO DE TIC;
GERENTE DE GRUPO I;
GERENTE DE GRUPO II;
GERENTE DE GRUPO III;
GERENTE DE PROJETOS I;
GERENTE DE PROJETOS II;
GERENTE REGIONAL DE OPERACOES;
GERENTE DE SETOR;SU…

### EMAIL — Email
TextBox String → CP_ORDEM_SERVICO.EMAIL

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
