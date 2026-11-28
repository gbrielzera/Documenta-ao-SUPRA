# Fluxo: Aceite POL900 - Política de Compliance e Antissuborno (ACEITEPOL900) — versão 1
Caminho: Fluxos > Aceite De Políticas Versão 1 Aceite POL900 - Política de Compliance e Antissuborno
XML: `XMLs para teste/Aceite_De_Políticas_Versão_1_Aceite_POL900_-_Política_de_Compliance_e_Antissuborno.xml` | Supravizio 19.1.1 | SubProcessoId 16540 | DesenhoProcessoId 2544 | ProcessoId 702
Órgão dono: 4000001100 - CONSELHO ADMINISTRACAO | Responsável: KENNIA DIAS DE SOUSA
Classe do subprocesso: Objetivo=Aceite POL900 - Política de Compliance e Antissuborno; DescricaoCliente=Aceite POL900 - Política de Compliance e Antissuborno; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Aceite POL 900; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Aceite POL900 - Política de Compliance e Antissuborno (ACEITEPOL900)

## Grafo do fluxo
- [263860] Tarefa "Aceite POL900 - Política de Compliance" → [263861] Sucesso
- [263861] EventoFinal "Sucesso" → (fim)
- [263859] EventoInicial "Evento Inicial" {Controle Disciplinar} → [263860] Aceite POL900 - Política de Compliance

## Atividades

### [263860] Tarefa "Aceite POL900 - Política de Compliance"
**ScriptInicio**
```python
OrdemServico.Salva()
AvancaProximaAtividade = True
```

### [263861] EventoFinal "Sucesso"

### [263859] EventoInicial "Evento Inicial"
Responsável: Controle Disciplinar (papel 675)
Config: Configuracao={"ServicoIniciador":"<Nenhum>"}
TipoSolicitacao: Aceite POL900 - Política de Compliance e Antissuborno
**ScriptValidacao**
```python
dataInicio_vigente='01/04/2025'
##Consulta retorna OS aberta e/ou finalizadas no mês e ano referente para o favorecido    
queryBaseDestacada = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join CP_ORDEM_SERVICO On OCORRENCIA.ID_OCORRENCIA = CP_ORDEM_SERVICO.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CP_ORDEM_SERVICO.FAVORECIDO_COBRA inner join classe_sub_processo csp on csp.id_classe_sub_processo=OCORRENCIA.id_classe_sub_proc Where csp.sigla = 'ACEITEPOL900' and (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' Or OCORRENCIA.SITUACAO = 'Aberto') and PESSOA.ID_PESSOA = '"+OrdemServico["FAVORECIDO_COBRA"]+"' and OCORRENCIA.ID_OCORRENCIA != "+str(OrdemServico.Id)+" and OCORRENCIA.data_hora_criacao >= to_date('"+dataInicio_vigente+"','DD/MM/RRRR')")

if queryBaseDestacada.Rows.Count != 0:
    osNum = queryBaseDestacada.Rows[0]["NUMERO"]
    Criticas.AdicionaPendencia("Parece que seu aceite já foi realizado, não sendo necessário realizá-lo novamente - OS: " + str(osNum))
    
if (OrdemServico.GetCustom("POSSUI_RESERVA")  == False):
    Criticas.AdicionaPendencia("Confirmação pendente")
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
#Formulario["FAVORECIDO_TODOS"].Visivel = False
#Formulario["FAVORECIDO_TODOS"].Habilitado = False
#Formulario["FAVORECIDO_COBRA"].Visivel = False
#Formulario["FAVORECIDO_COBRA"].Habilitado = False



Formulario['FAVORECIDO_COBRA'].Habilitado = False

OrdemServico.Assunto = OrdemServico.Servico.DescricaoCliente

Formulario["TE_MATRICULA"].Visivel = False
#Formulario["TE_CARGO"].Visivel = False
#Formulario["TE_FUNCAO"].Visivel = False
Formulario["TE_UOR"].Visivel = False

Formulario["TE_MATRICULA"].Habilitado = False
#Formulario["TE_CARGO"].Habilitado = False
#Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario['FAVORECIDO_COBRA'].Valor = OrdemServico.ClienteId.ToString()

matricula = ""
#cargo = ""
#funcao = ""
uor = ""


if Formulario["FAVORECIDO_COBRA"].Valor != "" or Formulario["FAVORECIDO_COBRA"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable(" SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        #cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()
        uor = linha["DESCRICAO"].ToString()

    #Formulario["TE_CARGO"].Valor = cargo.ToString()
    #Formulario["TE_FUNCAO"].Valor = funcao.ToString()
    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
    
    Formulario["TE_MATRICULA"].Visivel = True
    #Formulario["TE_CARGO"].Visivel = True
    #Formulario["TE_FUNCAO"].Visivel = True
    Formulario["TE_UOR"].Visivel = True

Formulario["LABEL2"].Valor = "<a target='_blank' href= https://bbts.docnix.com.br/bbts/corporate/index.html#/maxdoc/link/documento/1027>Clique aqui para acessar o link do documento e realizar sua leitura.</a>"
```
- Operação PR0001 Preencher Campos
  - POSSUI_RESERVA "Eu declaro estar ciente e concordo com os termos referentes ao Aceite POL900 - Política de Compliance e Antissuborno." [CheckBox Boolean → CP_ORDEM_SERVICO.POSSUI_RESERVA] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["TE_MATRICULA"].Visivel = True
#Formulario["TE_CARGO"].Visivel = False
#Formulario["TE_FUNCAO"].Visivel = False
Formulario["TE_UOR"].Visivel = True

Formulario["TE_MATRICULA"].Habilitado = False
#Formulario["TE_CARGO"].Habilitado = False
#Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario["TE_MATRICULA"].Valor = None
#Formulario["TE_CARGO"].Valor = None
#Formulario["TE_FUNCAO"].Valor = None
Formulario["TE_UOR"].Valor = None

matricula = ""
#cargo = ""
#funcao = ""
uor = ""

if Formulario["FAVORECIDO_COBRA"].Valor != "" or Formulario["FAVORECIDO_COBRA"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_COBRA"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        nomeFavorecido = favorecidoCustom.Nome
        orgaoFavorecido = favorecidoCustom.OrgaoId
    else:
        nomeFavorecido = OrdemServico.Favorecido.Nome
        orgaoFavorecido = OrdemServico.Favorecido.OrgaoId

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        #cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()
        uor = linha["DESCRICAO"].ToString()

    #Formulario["TE_CARGO"].Valor = cargo.ToString()
    #Formulario["TE_FUNCAO"].Valor = funcao.ToString()
    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
```
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - LABEL2 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2] obrigatório

## Papéis usados
### papel 675: Controle Disciplinar
Tipo=RelacaoPessoas | pessoas: Fila Controle Disciplinar

## Campos customizados usados (definição global)

### POSSUI_RESERVA — Possui Reserva?
CheckBox Boolean → CP_ORDEM_SERVICO.POSSUI_RESERVA

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
