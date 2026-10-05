# Fluxo: Recebimento de Ferramentas (RECEBEFERRAMENTA) — versão 12
Caminho: Fluxos > Serviços Assistência Técnica Versão 12 Recebimento de Ferramentas
XML: `XMLs para teste/Serviços_Assistência_Técnica_Versão_12_Recebimento_de_Ferramentas.xml` | Supravizio 19.1.1 | SubProcessoId 20793 | DesenhoProcessoId 2918 | ProcessoId 31
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: JOSE AFRANIO ARAUJO BRANDAO
Classe do subprocesso: Objetivo=Recebimento de Ferramentas; DescricaoCliente=Recebimento de Ferramentas; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Recebimento de Ferramenta (RECEBIMENTOFERRAMENTA)

## Grafo do fluxo
- [331259] EventoIntermediarioMensagem "Aviso Recebimento de Ferramenta" → [331266] Sucesso
- [331260] EventoInicial "" → [331258] Preencher Declaração
- [331261] EventoIntermediarioMensagem "OS Reprovada" → [331262] 
- [331262] FimCancelamento "" → (fim)
- [331263] Tarefa "Gerar FQ1333-004
" {Favorecido Cobra} → [331265] Chamado Finalizado - Recebimento de Ferramenta
- [331264] Tarefa "Solicitar aprovação do empregado" {Favorecido Cobra} → [G75317] Aprovado?
- [331265] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de Ferramenta" → [331259] Aviso Recebimento de Ferramenta
- [331266] EventoFinal "Sucesso" {Cliente} → (fim)
- [331258] Tarefa "Preencher Declaração" {Favorecido Cobra} → [331264] Solicitar aprovação do empregado
- [G75317] Gateway "Aprovado?" → «Aprovado» [331263] Gerar FQ1333-004
 | «Reprovado» [331261] OS Reprovada

## Gateways
### [G75317] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [331263] Gerar FQ1333-004
: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
- alternativa → [331261] OS Reprovada: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [331259] EventoIntermediarioMensagem "Aviso Recebimento de Ferramenta"
Destinatário: Gerente Favorecido Cobra (papel 278)
ModeloComunicado: Chamado Finalizado - Recebimento de EPI
Corpo do comunicado: Prezado(a) Gestor(a),
Informamos que o(a) empregado(a) OrdemServico.Customizado.FAVORECIDO_COBRA recebeu os equipamentos de proteção individual descritos no documento em anexo e confirmou o recebimento através da ordem de serviço número OrdemServico.Numero .
Atenciosamente,
Central de Serviços
- Relatorios:
  - FormatoExportacao=PDF

### [331260] EventoInicial ""
TipoSolicitacao: Recebimento de EPI - EPC - Uniformes
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
OrdemServico.Assunto = OrdemServico.Servico.DescricaoCliente

Formulario["TE_MATRICULA"].Visivel = False
Formulario["TE_CARGO"].Visivel = False
Formulario["TE_FUNCAO"].Visivel = False
Formulario["TE_UOR"].Visivel = False


Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_CARGO"].Habilitado = False
Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario['FAVORECIDO_COBRA'].Valor = DB.ExecuteScalar("SELECT DISTINCT TO_CHAR(p.id_pessoa) AS id_pessoa, p.nome || ' (' || p.usuario_rede || ')' AS nomemat, cp.matricula, p.ativo FROM pessoa p inner join cp_pessoa cp on cp.id_pessoa = p.id_pessoa WHERE TIPO_COLABORADOR = 'Empregado' AND p.ativo = 'Sim' AND p.id_pessoa = '"+OrdemServico.ClienteId.ToString()+"'")

matricula = ""
cargo = ""
funcao = ""
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

    lista = Utils.ExecuteDataTable(" SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.MATRICULA = CP.MATRICULA AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

    for linha in lista.Rows:
        cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()
        uor = linha["DESCRICAO"].ToString()

    Formulario["TE_CARGO"].Valor = cargo.ToString()
    Formulario["TE_FUNCAO"].Valor = funcao.ToString()
    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
    
    
    Formulario["TE_MATRICULA"].Visivel = True
    Formulario["TE_CARGO"].Visivel = True
    Formulario["TE_FUNCAO"].Visivel = True
    Formulario["TE_UOR"].Visivel = True
    
    
Formulario['OBS1'].Valor = "Declaro ter recebido da BB TECNOLOGIA E SERVIÇOS, para meu uso em serviço e proteção pessoal, os equipamentos de proteção pessoal (EPI abaixo descriminados, os quais me comprometo a utilizar corretamente sempre que for atuar em minha jornada de trabalho, ao mesmo tempo que me responsabilizo pelo bom uso, limpeza e guarda deles, respondendo pecuniariamente pelo eventual desaparecimento e/ou danos causados por descuido ou mau uso. Declaro ainda ter lido os normativos relacionados (NI 1333-001, PRO 1333-001 e MN 1333-001), comprometendo-me a cumprir integralmente seu conteúdo e zelar pela minha própria segurança durante a rotina laboral, em conformidade com as medidas gerais de disciplina da empresa e Normas Regulamentadoras do Ministério do Trabalho e Previdência. Declaro saber que o uso dos equipamentos é obrigatório e que, nos termos da legislação vigente que regulamenta o assunto, eventual descumprimento dessa orientação, ou seja, o não cumprimento dos termos aqui estabelecidos importará em ato faltoso do empregado, com aplicação de penalidades, tudo em conformidade com o ritual constante da Norma Interna 116, a qual também declaro conhecer. Declaro saber também que terei que devolvê-los no ato de meu desligamento da empresa, exceto os descartáveis."
    
Formulario["OBS1"].Habilitado = False
Formulario["OBS1"].Visivel = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Dados Cadastrais
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - KITEQUIPAMENTOS "KIT Equipamentos" [DataGrid RecordList → Z_00143_KITEQUIPAMENTOS.KITEQUIPAMENTOS] obrigatório
    - coluna ITEM obrigatório
**KITEQUIPAMENTOS.ITEM.ScriptModificado**
```python
if FormularioRegistro["ITEM"].Valor == "FERR-000302":
    FormularioRegistro["DESCRICAO"].Valor = "Chave de fenda simples 1/8 x 4"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000303":
    FormularioRegistro["DESCRICAO"].Valor = "Chave de fenda simples 3/16 x 6"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000304":
    FormularioRegistro["DESCRICAO"].Valor = "Chave de fenda simples 5/16 x 8"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000305":
    FormularioRegistro["DESCRICAO"].Valor = "Chave de fenda cruzada 1/8 x 6"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000306":
    FormularioRegistro["DESCRICAO"].Valor = "Chave de fenda cruzada 3/16 x 6"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000307":
    FormularioRegistro["DESCRICAO"].Valor = "Chave de fenda simples 5/16 x 6"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000308":
    FormularioRegistro["DESCRICAO"].Valor = "Alicate de corte com isolamento até 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000309":
    FormularioRegistro["DESCRICAO"].Valor = "Alicate de bico com isolamento até 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000310":
    FormularioRegistro["DESCRICAO"].Valor = "Chave torx isolada T8"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000311":
    FormularioRegistro["DESCRICAO"].Valor = "Chave torx isolada T9"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000312":
    FormularioRegistro["DESCRICAO"].Valor = "Chave torx isolada T10"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000313":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE DE FENDA SIMPLES 1/8 X 4 POL COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000314":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE DE FENDA SIMPLES 3/16 X 6 POL COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000315":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE DE FENDA SIMPLES 5/16 X 8 POL COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000316":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE DE FENDA CRUZADA 1/8 X 6 POL COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000317":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE DE FENDA CRUZADA 3/16 X 6 POL COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000318":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE DE FENDA CRUZADA 5/16 X 6 POL COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000319":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 ALICATE DE CORTE DIAGONAL MODELO SUECO COM ISOLAMENTO ATÉ 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000320":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 ALICATE DE BICO RETO 6/12 POL COM ISOLAMENTO ATÉ 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000321":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE TORX T 8 (HEXALOBULAR) COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000322":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE TORX T 9 (HEXALOBULAR) COM ISOLAMENTO ATE 1000V"
    
    
if FormularioRegistro["ITEM"].Valor == "FERR-000323":
    FormularioRegistro["DESCRICAO"].Valor = "T-50 CHAVE TORX T 10 (HEXALOBULAR) COM ISOLAMENTO ATE 1000V"
```
    - coluna CA
    - coluna QUANTIDADE obrigatório
    - coluna UNIDADE obrigatório
    - coluna DESCRICAO obrigatório
    - coluna RETIRADA obrigatório
  - OBS1 "Observação1" [Memo String(2000) → CPE_CONTRATOS.OBS1] obrigatório
  - FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
**FAVORECIDO_COBRA.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["TE_MATRICULA"].Visivel = True
Formulario["TE_CARGO"].Visivel = True
Formulario["TE_FUNCAO"].Visivel = True
Formulario["TE_UOR"].Visivel = True

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_CARGO"].Habilitado = False
Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False

Formulario["TE_MATRICULA"].Valor = None
Formulario["TE_CARGO"].Valor = None
Formulario["TE_FUNCAO"].Valor = None
Formulario["TE_UOR"].Valor = None

matricula = ""
cargo = ""
funcao = ""
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
        cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "" or linha["FIM_DATA_FUNCAO"].ToString() == None:
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        
        desc_colaborador = linha["DESC_COLABORADOR"].ToString()
        matricula = linha["MATRICULA"].ToString()
        uor = linha["DESCRICAO"].ToString()

    Formulario["TE_CARGO"].Valor = cargo.ToString()
    Formulario["TE_FUNCAO"].Valor = funcao.ToString()
    #Formulario["DESC_COLABORADOR"].Valor = desc_colaborador.ToString()
    Formulario["TE_MATRICULA"].Valor = matricula.ToString()
    Formulario["TE_UOR"].Valor = uor.ToString()
```
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] obrigatório

### [331261] EventoIntermediarioMensagem "OS Reprovada"
Destinatário: Cliente e Favorecido (papel 398)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [331262] FimCancelamento ""

### [331263] Tarefa "Gerar FQ1333-004
"
Responsável: Favorecido Cobra (papel 277)
**ScriptInicio**
```python
OrdemServico.Salva()
AvancaProximaAtividade = True
```
- Relatorios:
  - FormatoExportacao=PDF

### [331264] Tarefa "Solicitar aprovação do empregado"
Responsável: Favorecido Cobra (papel 277)
Config: Codigo=APROVAR
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Recebimento de Ferramenta; ReenvioEmailAprovacao=24
  - (aprovação) OBS1 "Observação1" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO]
  - (aprovação) FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO]
  - (aprovação) EQUIPAMENTOS "Equipamentos" [DataGrid RecordList → Z_00143_EQUIPAMENTOS.EQUIPAMENTOS]
  - aprovador: Favorecido Cobra (Unico)
- Relatorios:
  - FormatoExportacao=PDF

### [331265] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de Ferramenta"
Destinatário: Cliente e Favorecido (papel 398)
Config: ListaDestinatarios=dires@bbts.com.br
ModeloComunicado: Chamado Finalizado Cesec
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
 Link.Pesquisa 
Atenciosamente,
Central de Serviços
- Relatorios:
  - FormatoExportacao=PDF

### [331266] EventoFinal "Sucesso"
Responsável: Cliente (papel 18)
- Relatorios:
  - FormatoExportacao=PDF

### [331258] Tarefa "Preencher Declaração"
Responsável: Favorecido Cobra (papel 277)
**ScriptInicio**
```python
##OrdemServico.Salva()
AvancaProximaAtividade = True
```

## Papéis usados
### papel 278: Gerente Favorecido Cobra
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
#gestor = favorecidoBBTec.ObtemChefia(False)

#if favorecidoBBTec == gestor:
#    gestor = gestor.Orgao.OrgaoPai.Gestor

Atores.Adiciona(gestor, "Gerente do Favorecido")
```
### papel 398: Cliente e Favorecido
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Favorecido (PessoaOrdemServico)
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
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### KITEQUIPAMENTOS — KIT Equipamentos
DataGrid RecordList → Z_00143_KITEQUIPAMENTOS.KITEQUIPAMENTOS
Descrição: KIT Equipamentos 
Colunas do registro:
- RETIRADA "Retirada" [DatePicker DateTime]
- ITEM "Item" [DropDownList String] itens: FERR-000302;FERR-000303;FERR-000304;FERR-000305;FERR-000306;FERR-000307;FERR-000308;FERR-000309;FERR-000310;FERR-000311;FERR-000312;FERR-000313;FERR-000314;FERR-000315;FERR-000316;FERR-000317;FERR-000318;FERR-000319;FERR-000320;FERR-000321;FERR-000322;FERR-000323
- QUANTIDADE "Quantidade" [TextBox Integer]
- UNIDADE "Unidade" [DropDownList String]
**UNIDADE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT UOM_CODE, UNIT_OF_MEASURE_TL || '-' || UOM_CLASS FROM LISTA_UNIDADE_MEDIDA ORDER BY UNIT_OF_MEASURE_TL")
```
- DESCRICAO "Descrição" [Memo String]

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Não') order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

### EQUIPAMENTOS — Equipamentos
DataGrid RecordList → Z_00143_EQUIPAMENTOS.EQUIPAMENTOS
Colunas do registro:
- UNIDADE "UNIDADE" [DropDownList String]
**UNIDADE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT UOM_CODE, UNIT_OF_MEASURE_TL || '-' || UOM_CLASS FROM LISTA_UNIDADE_MEDIDA ORDER BY UNIT_OF_MEASURE_TL")
```
- DESCRICAO "Descrição do Equipamento" [Memo String]
- ITEM "Item" [DropDownList String] itens: UNIF-000005;UNIF-000027;UNIF-000006;UNIF-000028;UNIF-000008;UNIF-000001;UNIF-000007;FERR-000276;FERR-000277;FERR-000279;FERR-000278;FERR-000093;FERR-000094;NADM-002230
- QUANTIDADE "Quantidade" [TextBox Integer]
- RETIRADA "Retirada" [DatePicker DateTime]
- CA "CA" [TextBox Integer]

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
