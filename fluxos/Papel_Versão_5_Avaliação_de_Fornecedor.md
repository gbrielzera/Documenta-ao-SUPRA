# Fluxo: Avaliação de Fornecedor (AVALFORNECEDOR) — versão 5
Caminho: Fluxos > Papel Versão 5 Avaliação de Fornecedor
XML: `XMLs para teste/Papel_Versão_5_Avaliação_de_Fornecedor.xml` | Supravizio 19.1.1 | SubProcessoId 23674 | DesenhoProcessoId 3130 | ProcessoId 752
Órgão dono: 3000009430 - DIVISAO DE GERENCIAMENTO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: Objetivo=Avaliação de Fornecedor; DescricaoCliente=Avaliação de Fornecedor; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Avaliação de Fornecedor; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Avaliação do Fornecedor - Fiscalização Administrativa (AVALIARFORNECEDOR); Avaliação do Fornecedor - Fiscalização de Serviço (AVALIARFORNECEDORSERV)

## Grafo do fluxo
- [379656] EventoFinal "" → (fim)
- [379657] Tarefa "Analisar Solicitação" {Fila CSC - Contratos} → [G84509] Qual a Nota?
- [379658] Tarefa "Aprovação do  Gestor do Contrato" {Fila CSC - Contratos} → [G84510] Aprovado?
- [379659] Tarefa "Inserir Gescon" {Responsável atual} → [379663] Conclusão do Chamado
- [379660] FimCancelamento "" → (fim)
- [379661] Tarefa "Aprovação do  Fiscal" {Fila CSC - Contratos} → [379657] Analisar Solicitação
- [379662] EventoInicial "Inicio" → [379661] Aprovação do  Fiscal
- [379663] EventoIntermediarioMensagem "Conclusão do Chamado" → [379656] 
- [G84509] Gateway "Qual a Nota?" → «<2» [379658] Aprovação do  Gestor do Contrato | «>=2» [379659] Inserir Gescon
- [G84510] Gateway "Aprovado?" → «Aprovado» [379659] Inserir Gescon | «Reprovado» [379660] 

## Gateways
### [G84509] Qual a Nota? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom('VALOR')
```
- alternativa → [379658] Aprovação do  Gestor do Contrato: OperadorDecision=LessThan; ReferenciaDecision=<2; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
2
```
- alternativa → [379659] Inserir Gescon: OperadorDecision=GreaterThanEqual; ReferenciaDecision=>=2; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
2
```
### [G84510] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [379659] Inserir Gescon: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [379660] : OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [379656] EventoFinal ""
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
- Relatorios:
  - FormatoExportacao=PDF

### [379657] Tarefa "Analisar Solicitação"
Responsável: Fila CSC - Contratos (papel 688)
Config: Codigo=ANALISAR; ConfirmaResponsabilidade=true; PermiteCancelamentoAA=true
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Recurso.Custom import Pessoa
if OrdemServico.GetCustom('JURIDICA_FISICA') == "Pessoa Jurídica":
    sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+OrdemServico.GetCustom("CNPJ").ToString()+"','.',''),'/',''),'-','')"
    lista = DB.ExecuteDataTable(sql)
    if lista.Rows.Count > 0:
        AvancaProximaAtividade = True

if OrdemServico.GetCustom('JURIDICA_FISICA') == "Pessoa Física":
    sql="SELECT NOME_RAZAO_SOCIAL FROM bbts_gescon_fornecedor where cpf_cnpj = replace(replace(replace('"+OrdemServico.GetCustom("CSC_CPF").ToString()+"','.',''),'/',''),'-','')"
    lista = DB.ExecuteDataTable(sql)
    if lista.Rows.Count > 0:
        AvancaProximaAtividade = True
        
OrdemServico.AnexaExportacaoRelatorio('Avaliação do Fornecedor2','ARQUIVO',['OS'],[OrdemServico.Numero],"pdf")

AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
#anexo = OrdemServico.ObtemItem("ARQUIVO");
#repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
#arquivo = repositorio + "\\" + anexo.Localizacao
#Formulario.ExibeMensagem('arquivo')
#
#import System.IO
#pdfFilePath = arquivo
#bytes = System.IO.File.ReadAllBytes(pdfFilePath)
#Formulario.ExibeMensagem(bytes[0,2].ToString())
#sr = System.IO.StreamReader(arquivo)
#teste = bytes.BitConverter.ToString().Replace("-","")  
#for linha in bytes:
#   Formulario.ExibeMensagem(linha.ToString()) 
#bytes = System.IO.StreamReader(pdfFilePath) 
#pdfbase=bytes
#pdfbase=Convert.ToBase64String(bytes);
#conta = bytes.length
#pdfbase='leonam'
#Formulario.ExibeMensagem(pdfbase.ToString())
#pdfbase='leonam'
#sql="insert into TESTE_ARQ(ARQUIVO) values(utl_encode.BASE64_ENCODE('"+BitConverter.ToString(bytes).ToString()+"'))"
#sql="insert into TESTE_ARQ(ARQUIVO) values('"+pdfbase+"')"
#Formulario.ExibeMensagem(sql)
#DB.ExecuteNonQuery("insert into TESTE_ARQ(ARQUIVO) values(SYS.utl_encode.BASE64_ENCODE('@valor'))",bytes.ToString())
#DB.ExecuteNonQuery(sql)

#anexo = OrdemServico.ObtemItem("ARQCARGANF");
#repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
#arquivo = repositorio + "\\" + anexo.Localizacao
#
#arqNF = OrdemServico.ItensAnexados
#Formulario.ExibeMensagem(arquivo)
#if arquivo.Length > 0:
#    sr = System.IO.StreamReader(arquivo)    
#    #try:
#    #Ignora a primeira linha
#    linha = sr.ReadLine()
#    linha = sr.ReadLine()
#\\santacruz1.cobra.com.br\supravizio$\Anexos\Administração - Contratos\Arquivo\707139_947287_teste.pdf
```
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Arquivo — RequeridoInicial=true

### [379658] Tarefa "Aprovação do  Gestor do Contrato"
Responsável: Fila CSC - Contratos (papel 688)
Config: Codigo=APROVAR
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Gestor do Contrato
  - item para aprovação "Itens para aprovação"
  - aprovador: Gestor do Contrato (Unico)

### [379659] Tarefa "Inserir Gescon"
Responsável: Responsável atual (papel 36)
Config: Codigo=DGCO
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import System
from System.IO import *
from System.Text  import *
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
from Newtonsoft.Json import *
from Newtonsoft.Json.Linq import *
from System.Net.Http import *
from System.Net.Http.Headers import * 

item = OrdemServico.ObtemArtefato()
repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
arquivo = repositorio + "\\" + item.Localizacao
#OrdemServico.AdicionaComentario(arquivo.ToString(),False)
if arquivo.Length > 0:
    sr = StreamReader(arquivo, Encoding.Default)
    AsString = sr.ReadToEnd();
    bytes = Encoding.Default.GetBytes(AsString)
  
    AsBase64String = Convert.ToBase64String(bytes);
    #imprimendo na ordem de serviço 
    #OrdemServico.AdicionaComentario("incode: "+AsString, False)
    #Armazenando no campo descrição detalhada   
    #OrdemServico.DescricaoDetalhada = AsBase64String

    
## Envia arquivo em BLOB por API
anexo = OrdemServico.ObtemItem("ARQUIVO");
repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
arquivo = repositorio + "\\" + anexo.Localizacao
uri="http://ords.bbts.com.br:8080/bbts/ebs/spvz/v1/arquivos/"

script = "$headers = New-Object 'System.Collections.Generic.Dictionary[[String],[String]]'\n $headers.Add('FILE_NAME', '"+anexo.Descricao+"') \n $headers.Add('SISTEMA_ORIGEM', 'SUPRAVIZIO') \n $headers.Add('SISTEMA_DESTINO', 'GESCON') \n "

script= script + "$boundary = [System.Guid]::NewGuid().ToString() \n $FilePath = '"+arquivo+"' \n $TheFile = [System.IO.File]::ReadAllBytes($FilePath) \n $TheFileContent = [System.Text.Encoding]::GetEncoding('iso-8859-1').GetString($TheFile) \n $LF = "+'"`r`n"'+" \n "

script=script+ "$bodyLines = ("+'"--$boundary"'+", \n "+'"Content-Disposition: form-data; name= `"Description`"$LF"'+", \n "+'"This is a file Im uploading"'+", \n "+'"--$boundary"'+", \n "+'"Content-Disposition: form-data; name=`"photo`"; filename=`"'+arquivo+'`""'+", \n "+'"Content-Type: application/pdf$LF"'+", \n $TheFileContent, \n "+'"--$boundary--$LF"'+" ) -join $LF \n "

script=script+ "$resposta = Invoke-RestMethod '"+uri+"' -Method POST -ContentType "+'"multipart/form-data; boundary=$boundary"'+" -Body $bodyLines -Headers $Headers \n $Resposta.'X-ORDS-STATUS-CODE'"

dat=PowerShell.PSExecuteCmdlet(script)
OrdemServico.AdicionaComentario("ID Arquivo: "+dat.ToString(), False)

##Inserir a avaliação no Gescon

matriFunc_inclui = OrdemServico.Cliente["MATRICULA"]
matriFunc_avalia = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("COMBOBOX1")))["MATRICULA"]
ano = OrdemServico.GetCustom("ANO")
media = OrdemServico.GetCustom("VALOR")
tipo_avaliador = "FISCAL_SERVICO"
if OrdemServico.GetCustom("COMBOBOX") != 'Fiscalização Administrativa':
    tipo_avaliador = "FISCAL_SERVICO"
else:
    tipo_avaliador = "FISCALIZACAO_ADMINISTRATIVA"

sql = "select ID from bbts_gescon_contrato where DGCO = '"+OrdemServico.GetCustom("CSC_DGCO")+"'"
idContrato = DB.ExecuteScalar(sql)
if OrdemServico.GetCustom("CSC_COMBOBOX") == "Jan/Fev/Mar" :
    trimestre="TRIMESTRE_1"
if OrdemServico.GetCustom("CSC_COMBOBOX") == "Abr/Mai/Jun" :
    trimestre="TRIMESTRE_2"
if OrdemServico.GetCustom("CSC_COMBOBOX") == "Jul/Ago/Set" :
    trimestre="TRIMESTRE_3"
if OrdemServico.GetCustom("CSC_COMBOBOX") == "Out/Nov/Dez" :
    trimestre="TRIMESTRE_4"

sql_avaliacao="call xxbbtsgate.pg_bbts_fornecedor.pr_avaliacao_fornecedor('"+matriFunc_inclui.ToString()+"', '"+matriFunc_avalia.ToString()+"','"+ano.ToString()+"',replace('"+media.ToString()+"',',','.'),'"+idContrato.ToString()+"','"+tipo_avaliador.ToString()+"','','"+trimestre.ToString()+"')"
DB.ExecuteScalar(sql_avaliacao)

sql_conf="select count(1) from xxbbtsgate.BBTS_GESCON_FORN_CONTR_AVALIACAO where id_contrato = '"+idContrato.ToString()+"' and ano = '"+ano.ToString()+"' and TIPO_AVALIADOR = '"+tipo_avaliador.ToString()+"' and EN_TRIMESTRE = '"+trimestre.ToString()+"'"
resultado = DB.ExecuteScalar(sql_conf)


if resultado == 0:
    
    OrdemServico.AdicionaComentario("A Avaliação não foi inserida no Gescon: " + sql_avaliacao, False)
else:
    OrdemServico.AdicionaComentario("Avaliação inserida com sucesso", False)
    AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos
  - CSC_DGCO "Insira o número do DGCO" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000/0000"}
- Relatorios:
  - FormatoExportacao=PDF

### [379660] FimCancelamento ""

### [379661] Tarefa "Aprovação do  Fiscal"
Responsável: Fila CSC - Contratos (papel 688)
Config: Codigo=APROVAR_FISCAL
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Fiscal do Contrato; MinimoAprovadores=1
  - (aprovação) VALOR "Nota Média" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - (aprovação) COMBOBOX "Tipo do Formulário de Avaliação" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX]
  - (aprovação) ANO "Ano" [TextBox Integer → CP_ORDEM_SERVICO.ANO]
  - (aprovação) CSC_COMBOBOX "Informe o Período da Avaliação:" [DropDownList String → CPE_CSC.CSC_COMBOBOX]
  - (aprovação) AVALIACAO_FORNECEDOR "Avaliação do Fornecedor" [DataGrid RecordList → Z_00143_AVALIACAO_FORNECEDOR.AVALIACAO_FORNECEDOR]
  - (aprovação) CSC_DGCO "DGCO" [TextBox String → CPE_CSC.CSC_DGCO]
  - item para aprovação "Itens para aprovação"
  - aprovador: Fiscal do Serviço (Unico)
  - relatório: FormatoExportacao=PDF

### [379662] EventoInicial "Inicio"
TipoSolicitacao: 05.04. Suprimentos Corporativos, Licitações e Contratos - Contratos
**ScriptValidacao**
```python
if OrdemServico.GetCustom("OPCAO_DE_CONFIRMACAO") == False:
    Criticas.AdicionaPendencia("Favor marcar o campo Calcula Média.")

lista = OrdemServico.GetCustom("AVALIACAO_FORNECEDOR")
if lista.Rows.Count != 0:
    for linha in lista.Rows:
        if Convert.ToInt32(linha["NOTA"])<= 2 and (OrdemServico.DescricaoDetalhada == None or OrdemServico.DescricaoDetalhada == ''):
           Criticas.AdicionaPendencia("Conforme normativo a nota menor ou igual a 2(dois), deve ser justificada.")

dgco = OrdemServico.GetCustom("CSC_DGCO")
ano = OrdemServico.GetCustom("ANO")
tipo = OrdemServico.GetCustom("COMBOBOX")
periodo = OrdemServico.GetCustom("CSC_COMBOBOX")

sql = "select o2.numero from ocorrencia o2 inner join CPE_CSC cpe2 on cpe2.id_ocorrencia = o2.id_ocorrencia inner join cp_ordem_servico cpo2 on cpo2.id_ocorrencia = o2.id_ocorrencia inner join CP_ORDEM_SERVICO cpeh2 on cpeh2.id_ocorrencia = o2.id_ocorrencia inner join ordem_servico os2 on os2.id_ocorrencia = o2.id_ocorrencia where  o2.situacao != 'Cancelado' and cpe2.CSC_DGCO='"+dgco.ToString()+"' and cpo2.ano = '"+ano.ToString()+"' and cpe2.csc_combobox = '"+periodo.ToString()+"' and cpeh2.combobox = '"+tipo.ToString()+"' and o2.numero <> '"+OrdemServico.Numero.ToString()+"'"
sql1 = "select distinct o2.numero from ocorrencia o2 inner join CPE_CSC cpe2 on cpe2.id_ocorrencia = o2.id_ocorrencia inner join cp_ordem_servico cpo2 on cpo2.id_ocorrencia = o2.id_ocorrencia inner join CP_ORDEM_SERVICO cpeh2 on cpeh2.id_ocorrencia = o2.id_ocorrencia inner join ordem_servico os2 on os2.id_ocorrencia = o2.id_ocorrencia where  o2.situacao != 'Cancelado' and cpe2.CSC_DGCO='"+dgco.ToString()+"' and cpo2.ano = '"+ano.ToString()+"' and cpe2.csc_combobox = '"+periodo.ToString()+"' and cpeh2.combobox = '"+tipo.ToString()+"'"

resultado = DB.ExecuteDataTable(sql)

if resultado.Rows.Count != 0:
    resultado2 = DB.ExecuteDataTable(sql1)
    if resultado2.Rows.Count != 0:
        for linha in resultado2.Rows:
            Criticas.AdicionaPendencia("Já existe uma avaliação para este DGCO e período/ano: " + linha['NUMERO'].ToString())
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Fornecedor
OrdemServico.Assunto = "Formulário para Avaliação do Índice de Desempenho do Fornecedor"
#Formulario.ExibeMensagem(OrdemServico.Cliente['MATRICULA'].ToString())
Formulario["COMBOBOX"].Itens = "Serviços Especializados;Conservação e Limpeza;Serviços de Vigilância;Serviço de Manutenção Predial;Serviços Terceirizados com Cessão de Mão de Obra;Fornecimento de bens;Reparo de Peças;Fiscalização Administrativa;Serviços Advocatícios"
Formulario["CSC_COMBOBOX"].Itens = "Jan/Fev/Mar;Abr/Mai/Jun;Jul/Ago/Set;Out/Nov/Dez"

OrdemServico.SetCustom("AVALIACAO_FORNECEDOR", None)
Formulario["AVALIACAO_FORNECEDOR"].Visivel = False
Formulario["LABEL1"].Visivel = False
Formulario["LABEL1"].Valor = "<b>Observação:</b><br> Verificar a compatibilidade dos itens propostos na tabela com o objeto contratado, excluindo aqueles que não se aplicarem à contratação. Outros itens poderão ser incluídos de acordo com as especificações do projeto básico. Os itens deverão ser pontuados com os valores 1, 2 ou 3, conforme especificado abaixo.<br><br>"
Formulario["LABEL2"].Visivel = False
Formulario["LABEL2"].Valor = "<b>PONTUAÇÃO:</b><br>1 ¿ A empresa não atende à exigência.<br>2 ¿ A empresa atende parcialmente à exigência.<br>3 ¿ A empresa atende à exigência plenamente.<br><br>"

Formulario["LABEL3"].Valor = "<b>Orientações para preenchimento do formulário:</b><br><b>1.</b>Ao receber a cópia do contrato, o fiscal do serviço deverá tomar conhecimento do inteiro teor das especificações do projeto básico e das condições pactuadas, e elaborar o roteiro de fiscalização.<br><b>2.</b>Os itens para avaliação deverão ser determinados considerando-se as disposições contratuais, incluindo aqueles de natureza trabalhista expressos na NI 412 ¿ Gestão de Contratos, no caso de serviços terceirizados com cessão de mão de obra.<br>"
Formulario["LABEL4"].Valor = "<b>3.</b>A prestação dos serviços deverá ser fiscalizada ao longo de todo o período de vigência do contrato.<br><b>4.</b>Trimestralmente, por meio de uma escala de pontuação presente no formulário padrão, o fiscal deverá pontuar o desempenho da empresa contratada no cumprimento de cada item presente no roteiro, registrando ao final de cada trimestre a média da avaliação. A média trimestral deverá então ser inserida no sistema Gescon, juntamente com este formulário devidamente datado, carimbado e assinado.<br><b>5.</b>Ao final de cada semestre, o fiscal do serviço deverá registrar a média das avaliações trimestrais, gerando então uma média semestral que poderá variar de 1 a 3."
Formulario["LABEL5"].Valor = "<b>6.</b>Quando a pontuação de um item for 1 ou 2, deverá ser incluída no respectivo formulário a justificativa para tal pontuação.<br><b>7.</b>A assinatura do gestor do contrato será necessária apenas quando a média trimestral estiver entre 1 e 2.<br><b>8.</b>As avaliações periódicas subsidiarão a tomada de decisão pelo gestor do item ou serviço quanto à prorrogação ou encerramento dos contratos firmados."
Formulario["VALOR"].Valor = None
Formulario["VALOR"].Habilitado = False

if OrdemServico.Servico.Sigla == "AVALIARFORNECEDOR":
    Formulario["COMBOBOX"].Itens = "Fiscalização Administrativa"
else: 
    Formulario["COMBOBOX"].Itens = "Serviços Especializados;Conservação e Limpeza;Serviços de Vigilância;Serviço de Manutenção Predial;Serviços Terceirizados com Cessão de Mão de Obra;Fornecimento de bens;Reparo de Peças;Serviços Advocatícios"
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo" classes: Anexo — RequeridoInicial=true; PermiteMultiplosItens=true
- Operação PR0001 Preencher Campos
  - ANO "Ano da avaliação" [TextBox Integer → CP_ORDEM_SERVICO.ANO] obrigatório
**ANO.ScriptModificado**
```python
dgco = Formulario["CSC_DGCO"].Valor
ano = Formulario["ANO"].Valor
tipo = Formulario["COMBOBOX"].Valor
periodo = Formulario["CSC_COMBOBOX"].Valor

sql = "select count(o2.numero) from ocorrencia o2 inner join CPE_CSC cpe2 on cpe2.id_ocorrencia = o2.id_ocorrencia inner join cp_ordem_servico cpo2 on cpo2.id_ocorrencia = o2.id_ocorrencia inner join CPE_HOMOLOGACAO cpeh2 on cpeh2.id_ocorrencia = o2.id_ocorrencia inner join ordem_servico os2 on os2.id_ocorrencia = o2.id_ocorrencia where  o2.situacao != 'Cancelado' and cpe2.CSC_DGCO='"+dgco.ToString()+"' and cpo2.ano = '"+ano.ToString()+"' and cpe2.csc_combobox = '"+periodo.ToString()+"' and cpeh2.combobox = '"+tipo.ToString()+"'"
sql1 = "select distinct o2.numero from ocorrencia o2 inner join CPE_CSC cpe2 on cpe2.id_ocorrencia = o2.id_ocorrencia inner join cp_ordem_servico cpo2 on cpo2.id_ocorrencia = o2.id_ocorrencia inner join CPE_HOMOLOGACAO cpeh2 on cpeh2.id_ocorrencia = o2.id_ocorrencia inner join ordem_servico os2 on os2.id_ocorrencia = o2.id_ocorrencia where  o2.situacao != 'Cancelado' and cpe2.CSC_DGCO='"+dgco.ToString()+"' and cpo2.ano = '"+ano.ToString()+"' and cpe2.csc_combobox = '"+periodo.ToString()+"' and cpeh2.combobox = '"+tipo.ToString()+"'"

result = DB.ExecuteScalar(sql)

if result != 0:
    result = DB.ExecuteScalar(sql1)
    Formulario.ExibeMensagem("Já existe uma avaliação para este DGCO e período/ano: " + result.ToString())

#Formulario.ExibeMensagem(DateTime.Now.Year.ToString())  
if Convert.ToInt32(Controle.Valor) > DateTime.Now.Year:
    Controle.Valor = None
    Formulario.ExibeMensagem("Ano não pode ser maior que o ano corrente")
```
  - AVALIACAO_FORNECEDOR "Avaliação da prestação dos serviços" [DataGrid RecordList → Z_00143_AVALIACAO_FORNECEDOR.AVALIACAO_FORNECEDOR] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=1000; PosicaoRotulo=Topo
**AVALIACAO_FORNECEDOR.ScriptModificado**
```python
Formulario["OPCAO_DE_CONFIRMACAO"].Valor = False
#Formulario.ExibeMensagem(FormularioRegistro["NOTA"].Valor.ToString())
if Convert.ToInt32(FormularioRegistro["NOTA"].Valor) <= 2:
    Formulario.ExibeMensagem("Conforme o normativo, nota igual ou menor a dois, deve ser justificada.")
```
**AVALIACAO_FORNECEDOR.ScriptRemovido**
```python
OrdemServico.SetCustom("OPCAO_DE_CONFIRMACAO",False)
```
    - coluna NOTA obrigatório
    - coluna ITEM obrigatório
  - OPCAO_DE_CONFIRMACAO "Calcular Média:" [CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO] obrigatório
**OPCAO_DE_CONFIRMACAO.ScriptModificado**
```python
lista = OrdemServico.GetCustom("AVALIACAO_FORNECEDOR")
qtd=0
soma = 0
media = None

if lista.Rows.Count == 0:
    Formulario.ExibeMensagem("O campo com as avaliações está vazio.")
else:
    for linha in lista.Rows:
        if linha["NOTA"].ToString()!= None and linha["NOTA"].ToString()!= "":
            qtd = qtd + 1
            #Formulario.ExibeMensagem(qtd.ToString())
            soma = soma + Convert.ToDecimal(linha["NOTA"])
    media = soma / qtd
if media != None:
    Formulario["VALOR"].Valor = Math.Round(Convert.ToDecimal(media),2)
```
  - NOME_FORNECEDOR "Empresa contratada:" [TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR] obrigatório
  - CSC_OBS "Objeto da contratação:" [Memo String(2000) → CPE_CSC.CSC_OBS] obrigatório
  - CSC_DATA_FIM "Vigência do contrato:" [DatePicker DateTime → CPE_CSC.CSC_DATA_FIM] obrigatório
  - COMBOBOX "Tipo do Formulário de Avaliação" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario["COMBOBOX1"].Valor = ''
Formulario["COMBOBOX1"].Itens = None
Formulario["CSC_DGCO"].Valor = ''
OrdemServico.SetCustom("AVALIACAO_FORNECEDOR", None)
Formulario["AVALIACAO_FORNECEDOR"].Visivel = False
Formulario["LABEL1"].Visivel = False
Formulario["LABEL2"].Visivel = False
if Formulario["COMBOBOX"].Valor == "Conservação e Limpeza":
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento de prazos'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências relacionadas à execução do objeto contratual'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Mão de obra, materiais e equipamentos adequados'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Utilização de uniformes e equipamentos de proteção individual apropriados'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Execução das rotinas de serviços periódicos estabelecidos no contrato'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Manutenção de um bom estado de limpeza, organização e conservação'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Produtos de limpeza e higienização disponibilizados com a qualidade, quantidade e frequência estabelecidas no contrato'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega da relação dos empregados alocados no contrato contendo nome completo, cargo ou função, horário do posto de trabalho, números da carteira de identidade (RG) e da inscrição no Cadastro de Pessoas Físicas (CPF), com indicação dos responsáveis técnicos pela execução dos serviços, quando for o caso'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega da carteira de Trabalho e Previdência Social (CTPS) dos empregados admitidos e dos responsáveis técnicos pela execução dos serviços, quando for o caso, devidamente assinada pela contratada'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos exames médicos admissionais dos empregados da contratada que prestarão os serviços'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Indicação e manutenção de um preposto no local da execução do serviço, conforme a frequência determinada no contrato, representando um canal de comunicação entre a BB Tecnologia e Serviços e a empresa contratada, evitando assim a caracterização de subordinação hierárquica entre funcionários terceirizados e o fiscal do serviço'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega periódica das CTPS dos profissionais alocados para a prestação dos serviços contratados para, por amostragem, conferir as anotações com a finalidade de verificar, em especial, data de admissão, descrição do posto de serviço, valor do salário-base, a existência de anotações que mencionem a BB Tecnologia e Serviços e eventuais alterações do contrato de trabalho'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos termos de rescisão dos contratos de trabalho dos empregados prestadores de serviço devidamente homologados, quando exigível pelo sindicato da categoria'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega das guias de recolhimento da contribuição previdenciária e do FGTS, referentes às rescisões contratuais'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos extratos dos depósitos efetuados nas contas vinculadas individuais do FGTS de cada empregado dispensado'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos exames médicos demissionais dos empregados dispensados'])
    
    Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL2"].Visivel = True
    
    
    
if Formulario["COMBOBOX"].Valor == "Serviços Especializados":
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento de prazos'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento do Acordo de Nível de Serviços'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências relacionadas à execução do objeto contratual'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Mão de obra, materiais e equipamentos adequados'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Utilização de uniformes e equipamentos de proteção individual apropriados'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação de documentação técnica inerente ao objeto da contratação'])
    Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL2"].Visivel = True
    
if Formulario["COMBOBOX"].Valor == "Serviços de Vigilância":
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento de prazos'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências relacionadas à execução do objeto contratual'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Comprovação da formação técnica específica da mão de obra oferecida, através de certificado de Curso de Formação de Vigilantes, expedido por instituições devidamente habilitadas e reconhecidas'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Inspeção dos postos de vigilância de acordo com a rotina contratada'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Execução das rotinas de serviços periódicos estabelecidos no contrato'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Utilização de uniformes e equipamentos apropriados pelos vigilantes'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento da jornada diária de trabalho e dos intervalos para descanso previstos em lei '])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Realização de rondas na periodicidade determinada no contrato'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Registro de ocorrências identificadas durante o turno de trabalho'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Permissão do ingresso nas instalações apenas de pessoas previamente autorizadas e identificadas.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Controle de entrada e saída de veículos na empresa'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Fiscalização da entrada e saída de materiais '])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Controle da entrada de visitantes'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Repasse aos vigilantes que estão assumindo o posto, quando da rendição, de todas as orientações recebidas e em vigor'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação da relação dos empregados alocados no contrato contendo nome completo, cargo ou função, horário do posto de trabalho, números da carteira de identidade (RG) e da inscrição no Cadastro de Pessoas Físicas (CPF), com indicação dos responsáveis técnicos pela execução dos serviços, quando for o caso'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega da carteira de Trabalho e Previdência Social (CTPS) dos empregados admitidos e dos responsáveis técnicos pela execução dos serviços, quando for o caso, devidamente assinada pela contratada'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação dos exames médicos admissionais dos empregados que prestarão os serviços'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Indicação e manutenção de um preposto no local da execução do serviço, conforme a frequência determinada no contrato, representando um canal de comunicação entre a BB Tecnologia e Serviços e a empresa contratada, evitando assim a caracterização de subordinação hierárquica entre funcionários terceirizados e o fiscal do serviço'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega periódica das CTPS dos profissionais alocados para a prestação dos serviços contratados para, por amostragem, conferir as anotações com a finalidade de verificar, em especial, data de admissão, descrição do posto de serviço, valor do salário-base, a existência de anotações que mencionem a BB Tecnologia e Serviços e eventuais alterações do contrato de trabalho'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação dos termos de rescisão dos contratos de trabalho dos empregados prestadores de serviço devidamente homologados, quando exigível pelo sindicato da categoria'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação de Guias de recolhimento da contribuição previdenciária e do FGTS, referentes às rescisões contratuais'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação dos extratos dos depósitos efetuados nas contas vinculadas individuais do FGTS de cada empregado dispensado'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação de exames médicos demissionais dos empregados dispensados'])
    
    Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL2"].Visivel = True
    
    
    
    
    
    
if Formulario["COMBOBOX"].Valor == "Serviço de Manutenção Predial":
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento de prazos.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências relacionadas à execução do objeto contratual.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Comprovação da formação técnica específica da mão de obra oferecida está de acordo com o exigido no contrato.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Realização dos serviços de manutenção preventiva e corretiva conforme estabelecido no contrato.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Realização dos serviços na periodicidade determinada em contrato.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Execução das rotinas de serviços periódicos estabelecidos no contrato.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Utilização de uniformes e equipamentos apropriados.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento da jornada diária de trabalho.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Disponibilização das ferramentas e equipamentos necessários à execução dos serviços.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Manutenção de condições de segurança e higiene necessárias à preservação da integridade física e da saúde dos empregados.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação dos relatórios de ocorrências para fiscalização da contratante, na periodicidade determinada no contrato.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Unidades de climatização mantidas com suas fichas de acompanhamento de manutenção preventiva atualizadas mensalmente.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega da relação dos empregados alocados no contrato contendo nome completo, cargo ou função, horário do posto de trabalho, números da carteira de identidade (RG) e da inscrição no Cadastro de Pessoas Físicas (CPF), com indicação dos responsáveis técnicos pela execução dos serviços, quando for o caso.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega da carteira de Trabalho e Previdência Social (CTPS) dos empregados admitidos e dos responsáveis técnicos pela execução dos serviços, quando for o caso, devidamente assinada pela contratada'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos exames médicos admissionais dos empregados da contratada que prestarão os serviços.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Indicação e manutenção de um preposto no local da execução do serviço, conforme a frequência determinada no contrato, representando um canal de comunicação entre a BB Tecnologia e Serviços e a empresa contratada, evitando assim a caracterização de subordinação hierárquica entre funcionários terceirizados e o fiscal do serviço.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega periódica das CTPS dos profissionais alocados para a prestação dos serviços contratados para, por amostragem, conferir as anotações com a finalidade de verificar, em especial, data de admissão, descrição do posto de serviço, valor do salário-base, a existência de anotações que mencionem a BB Tecnologia e Serviços e eventuais alterações do contrato de trabalho.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos termos de rescisão dos contratos de trabalho dos empregados prestadores de serviço devidamente homologados, quando exigível pelo sindicato da categoria'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega das guias de recolhimento da contribuição previdenciária e do FGTS, referentes às rescisões contratuais'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos extratos dos depósitos efetuados nas contas vinculadas individuais do FGTS de cada empregado dispensado.'])
    OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos exames médicos demissionais dos empregados dispensados.'])
    Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
    Formulario["LABEL1"].Visivel = True
    Formulario["LABEL2"].Visivel = True
    
    
    
    
if Formulario["COMBOBOX"].Valor == "Serviços Terceirizados com Cessão de Mão de Obra":
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento de prazos.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências relacionadas à execução do objeto contratual.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Mão de obra, materiais e equipamentos adequados..'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Utilização de uniformes e equipamentos de proteção individual apropriados.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Execução das rotinas de serviços periódicos estabelecidos no contrato.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega da relação dos empregados alocados no contrato contendo nome completo, cargo ou função, horário do posto de trabalho, números da carteira de identidade (RG) e da inscrição no Cadastro de Pessoas Físicas (CPF), com indicação dos responsáveis técnicos pela execução dos serviços, quando for o caso..'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega da carteira de Trabalho e Previdência Social (CTPS) dos empregados admitidos e dos responsáveis técnicos pela execução dos serviços, quando for o caso, devidamente assinada pela contratada.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos exames médicos admissionais dos empregados da contratada que prestarão os serviços.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Indicação e manutenção de um preposto no local da execução do serviço, conforme a frequência determinada no contrato, representando um canal de comunicação entre a BB Tecnologia e Serviços e a empresa contratada, evitando assim a caracterização de subordinação hierárquica entre funcionários terceirizados e o fiscal do serviço.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega periódica das CTPS dos profissionais alocados para a prestação dos serviços contratados para, por amostragem, conferir as anotações com a finalidade de verificar, em especial, data de admissão, descrição do posto de serviço, valor do salário-base, a existência de anotações que mencionem a BB Tecnologia e Serviços e eventuais alterações do contrato de trabalho.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos termos de rescisão dos contratos de trabalho dos empregados prestadores de serviço devidamente homologados, quando exigível pelo sindicato da categoria.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega das guias de recolhimento da contribuição previdenciária e do FGTS, referentes às rescisões contratuais.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos extratos dos depósitos efetuados nas contas vinculadas individuais do FGTS de cada empregado dispensado.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos exames médicos demissionais dos empregados dispensados.'])
      
     Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
     Formulario["LABEL1"].Visivel = True
     Formulario["LABEL2"].Visivel = True

     
if Formulario["COMBOBOX"].Valor == "Fornecimento de bens":     
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Cumprimento de prazos.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos bens de acordo com as especificações exigidas no contrato.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega dos bens nas quantidades solicitadas.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Integridade dos bens.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Utilização de embalagens apropriadas.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação do termo de garantia dos bens.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação de bens com as certificações exigidas.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Atendimento às instruções normativas indicadas no projeto básico.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['.'])
       
     Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
     Formulario["LABEL1"].Visivel = True
     Formulario["LABEL2"].Visivel = True

     
if Formulario["COMBOBOX"].Valor == "Reparo de Peças":     
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Entrega das peças reparadas dentro do prazo estabelecido em contrato.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Reparos realizados de acordo com a qualidade estabelecida em contrato.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências relacionadas à execução do objeto contratual.'])
 
     Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
     Formulario["LABEL1"].Visivel = True
     Formulario["LABEL2"].Visivel = True
     
     
     
if Formulario["COMBOBOX"].Valor == "Fiscalização Administrativa":       
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Regularidade fiscal e trabalhista.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Apresentação de documentos exigidos no contrato.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Regularidade das notas fiscais.'])
     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências de caráter administrativo.'])
   
     Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
     Formulario["LABEL1"].Visivel = True
     Formulario["LABEL2"].Visivel = True
     
     
     
#if Formulario["COMBOBOX"].Valor == "Serviços Advocatícios":     
#     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Das consultas feitas ao fornecedor de serviços jurídicos quanto à efetividade da defesa, qual foi o grau de satisfação?'])
#     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Quanto à qualidade dos serviços prestados em que grau de satisfação o fornecedor se enquadra?'])
#     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Das demandas postas pela BBTS sob a responsabilidade do prestador de serviços jurídicos, qual é o grau de satisfação quanto ao resultado dos serviços (audiência, diligências, atendimento, etc)?'])
#     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Na condução dos processos postos pela BBTS sob a responsabilidade do prestador de serviços jurídicos, em que grau o mesmo poderá ser enquadrado quanto ao cumprimento dos prazos judiciais?'])
#     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Quanto à efetividade/tempestividade no atendimento às solicitações da BBTS, em que grau o fornecedor de serviços é enquadrado?'])
#     OrdemServico.AdicionaLinhaRegistro('AVALIACAO_FORNECEDOR', ['ITEM'], ['Incidência/Resolução de ocorrências relacionada à execução do objeto contratual.'])
#     
#     Formulario["LABEL1"].Valor = "<b>Observação:</b><br> Atribuir a cada requisito a pontuação que mais se aproxima da realidade da empresa (observado ou comprovado documentalmente). Se o requisito não se aplicar (NA) ao tipo de fornecimento, não atribuir pontuação. Nota de 0 a 100.<br><br>"
#     Formulario["LABEL2"].Valor = "<b>PONTUAÇÃO:</b><br>0¿25 ¿ A empresa não atende à exigência.<br>26-80 ¿ A empresa atende parcialmente à exigência / Apresentou problemas com acertos.<br>81-99 ¿ Resultado de desempenho satisfatório.<br>100 - Resultado de desempenho plenamente satisfatório.<br> <br>"
#
#     Formulario["LABEL3"].Valor = "<b>Orientações para preenchimento do formulário:</b><br><b>1.</b>Ao receber a cópia do contrato, o fiscal do serviço deverá tomar conhecimento do inteiro teor das especificações do projeto básico e das condições pactuadas, e elaborar o roteiro de fiscalização.<br><b>2.</b>Os itens para avaliação deverão ser determinados considerando-se as disposições contratuais, incluindo aqueles de natureza trabalhista expressos na NI 412 ¿ Gestão de Contratos, no caso de serviços terceirizados com cessão de mão de obra.<br>"
#     Formulario["LABEL4"].Valor = "<b>3.</b>A prestação dos serviços deverá ser fiscalizada ao longo de todo o período de vigência do contrato.<br><b>4.</b>Semestralmente, por meio de uma escala de pontuação presente no formulário padrão, o fiscal deverá pontuar o desempenho da empresa contratada no cumprimento de cada item presente no roteiro. Após a conversão da média semestral, que poderá variar de 1 a 3, deverá então ser inserida no sistema Gescon, juntamente com este formulário devidamente datado e assinado."
#     Formulario["LABEL5"].Valor = "<b>5.</b>Quando a pontuação de um item for de 0 a 80, deverá ser incluída no respectivo formulário a justificativa para tal pontuação.<br><b>6.</b>A assinatura do gestor do contrato será necessária apenas quando a média trimestral estiver entre 0 e 80.<br><b>7.</b>As avaliações periódicas subsidiarão a tomada de decisão pelo gestor do item ou serviço quanto à prorrogação ou encerramento dos contratos firmados.<br> <br>"
#     
#     Formulario["AVALIACAO_FORNECEDOR"].Visivel = True
#     Formulario["LABEL1"].Visivel = True
#     Formulario["LABEL2"].Visivel = True
```
  - GESTOR_SOLICITA "Gestor do Contrato:" [DropDownList String → CPE_PESSOAS.GESTOR_SOLICITA] obrigatório
  - CSC_COMBOBOX "Informe o Período da Avaliação:" [DropDownList String → CPE_CSC.CSC_COMBOBOX] obrigatório
  - COMBOBOX1 "Fiscal Avaliador: " [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1]
  - VALOR "Média Trimestral:" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - CSC_DGCO "DGCO nº:" [TextBox String → CPE_CSC.CSC_DGCO] obrigatório — Configuracao={"Mascara":"00000/0000"}
**CSC_DGCO.ScriptModificado**
```python
from Venki.Supravizio.Processo.Custom import Servico
sql="SELECT gf.nome_razao_social, gc.OBJETO, gic.dt_fim_vigencia FROM bbts_gescon_fornecedor GF INNER JOIN BBTS_GESCON_CONTRATO GC ON gc.id_fornecedor = GF.ID INNER JOIN BBTS_GESCON_INSTRUMENTO_CONTRATUAL gic ON gc.id = gic.id_contrato WHERE replace(replace(replace(gc.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and gic.DT_FIM_VIGENCIA = (select max(gic2.DT_FIM_VIGENCIA) from BBTS_GESCON_INSTRUMENTO_CONTRATUAL gic2 where gic.id_contrato=gic2.id_contrato)"

lista = DB.ExecuteDataTable(sql)
if lista.Rows.Count == 0:
    Formulario.ExibeMensagem("Este DGCO não está cadastrado no Gescon.")
    Formulario["NOME_FORNECEDOR"].Valor = None
    Formulario["NOME_FORNECEDOR"].Habilitado = False
    Formulario["CSC_OBS"].Valor = None
    Formulario["CSC_OBS"].Habilitado = False
    Formulario["CSC_DATA_FIM"].Valor = None
    Formulario["CSC_DATA_FIM"].Habilitado = False

else:
    for linha in lista.Rows:
        Formulario["NOME_FORNECEDOR"].Valor = linha["NOME_RAZAO_SOCIAL"]
        Formulario["NOME_FORNECEDOR"].Habilitado = False
        
        Formulario["CSC_OBS"].Valor = linha["OBJETO"]
        Formulario["CSC_OBS"].Habilitado = False
        
        Formulario["CSC_DATA_FIM"].Valor = linha["dt_fim_vigencia"]
        Formulario["CSC_DATA_FIM"].Habilitado = False
        

if Formulario["COMBOBOX"].Valor != 'Fiscalização Administrativa':
    ##Fiscal Servico
    sql_fs="select to_char(cpp.id_pessoa) as ID, f.nome as NOME from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular or f.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on to_char(cpp.matricula) = to_char(f.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_SERVICO'"
else:
##Fiscal Administrativo
    sql_fs="select to_char(cpp.id_pessoa) as ID, f.nome as NOME from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular or f.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on to_char(cpp.matricula) = to_char(f.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_ADMINISTRATIVA'"

fiscais = DB.ExecuteDataTable(sql_fs)

if fiscais.Rows.Count != 0 :
    Formulario["COMBOBOX1"].Itens = DB.ExecuteDataTable(sql_fs)
    Formulario["COMBOBOX1"].Habilitado = True
else:
    Formulario.ExibeMensagem('Este contrato não tem fiscal de serviço ativo.')
    Formulario["COMBOBOX1"].Itens = None
    Formulario["COMBOBOX1"].Valor = None
    Formulario["COMBOBOX1"].Habilitado = False
    
#NOME_CONTRATO
##Gestor do contrato
#sql_g="select f.nome as NOME from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular or f.id = d.id_suplente LEFT OUTER join cp_pessoa cpp on cpp.matricula = f.matricula where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'GESTAO_CONTRATO'"

sql_g="SELECT To_char(cpp.id_pessoa) as id, f.nome AS NOME FROM bbts_gescon_designacao d INNER JOIN bbts_gescon_contrato c ON c.id = d.id_contrato INNER JOIN bbts_gescon_funcionario f ON f.id = d.id_titular OR f.id = d.id_suplente INNER JOIN cp_pessoa cpp ON to_char(cpp.matricula) = to_char(f.matricula) where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+Controle.Valor.ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'GESTAO_CONTRATO'"

gestor = DB.ExecuteDataTable(sql_g)

if gestor.Rows.Count != 0 :
    Formulario["GESTOR_SOLICITA"].Itens = DB.ExecuteDataTable(sql_g)
    Formulario["GESTOR_SOLICITA"].Habilitado = True
else:
    Formulario.ExibeMensagem('Este contrato não tem gestor do contrato ativo.')
    Formulario["GESTOR_SOLICITA"].Itens = None
    Formulario["GESTOR_SOLICITA"].Valor = None
    Formulario["GESTOR_SOLICITA"].Habilitado = False
```
  - DescricaoDetalhada (nativo) "É obrigatório justificar no campo abaixo todos os itens que foram pontuados com nota menor ou igual a 2, listando os motivos da pontuação para cada item."
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1] obrigatório
  - LABEL3 "Texto Informativo" [Label String(1024) → CP_ORDEM_SERVICO.LABEL3] obrigatório
  - LABEL4 "LABEL4" [Label String(1024) → CPE_PDCI2019.LABEL4] obrigatório
  - LABEL5 "Texto Informativo" [Label String(1024) → CPE_ORDEM_SERVICO.LABEL5] obrigatório
  - LABEL2 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL2] obrigatório

### [379663] EventoIntermediarioMensagem "Conclusão do Chamado"
Destinatário: Cliente (papel 18)
Config: Codigo=CONCLUSÃO DO CHAMADO
ModeloComunicado: Conclusão do Chamado - DGCO
Corpo do comunicado: Prezado(a), 
o chamado OrdemServico.Numero foi finalizado.
Segue o número do DGCO: OrdemServico.Customizado.CSC_DGCO 
Atenciosamente,
Portal de Autoatendimento

## Papéis usados
### papel 688: Fila CSC - Contratos
Tipo=RelacaoPessoas | pessoas: Fila CSC - Contratos
### papel 828: Gestor do Contrato
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
idPessoa = OrdemServico["FAVORECIDO_COBRA"]

if idPessoa!= None:
    p = Pessoa.Carrega("Id",idPessoa )
    Atores.Adiciona(p);
```
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 756: Fiscal do Serviço
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
from Venki.Supravizio.Processo.Custom import Servico
if OrdemServico.SubProcesso.ClasseSubProcesso.Sigla =='AVALFORNECEDOR':    
    if OrdemServico.GetCustom("COMBOBOX") != 'Fiscalização Administrativa':
        ##Fiscal Servico
        sql_fs="select to_char(cpp.id_pessoa) as FISCAL_SERVICO, f.nome as NOME from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular or f.id = d.id_suplente LEFT OUTER join pessoa cpp on upper(cpp.usuario_rede) = replace(replace(replace(f.email, 'MODIF_',''),'@BBTS.COM.BR',''),'@BBTECNO.COM.BR','') where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+OrdemServico.GetCustom('CSC_DGCO').ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_SERVICO'"
    else:
    ##Fiscal Administrativo
        sql_fs="select to_char(cpp.id_pessoa) as FISCAL_SERVICO, f.nome as NOME from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular or f.id = d.id_suplente LEFT OUTER join pessoa cpp on upper(cpp.usuario_rede) = replace(replace(replace(f.email, 'MODIF_',''),'@BBTS.COM.BR',''),'@BBTECNO.COM.BR','') where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+OrdemServico.GetCustom('CSC_DGCO').ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_ADMINISTRATIVA'"

    pesquisa01 = DB.ExecuteDataTable(sql_fs)
    for pessoa in pesquisa01.Rows:
        fiscalServico = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SERVICO"]))
        Atores.Adiciona(fiscalServico)

else:

    pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_SERVICO, FISCAL_SUPLENTE FROM Z_00143_FISCAL_SER WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")

    for pessoa in pesquisa01.Rows:
        fiscalServico = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SERVICO"]))
        fiscalSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SUPLENTE"]))
        Atores.Adiciona(fiscalServico)
        Atores.Adiciona(fiscalSuplente)
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

### CSC_DGCO — DGCO
TextBox String → CPE_CSC.CSC_DGCO

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### ANO — Ano
TextBox Integer → CP_ORDEM_SERVICO.ANO

### CSC_COMBOBOX — CSC_COMBOBOX
DropDownList String → CPE_CSC.CSC_COMBOBOX
Itens: Jan/Fev/Mar;Abr/Mai/Jun;Jul/Ago/Set;Out/Nov/Dez

### AVALIACAO_FORNECEDOR — Avaliação do Fornecedor
DataGrid RecordList → Z_00143_AVALIACAO_FORNECEDOR.AVALIACAO_FORNECEDOR
Colunas do registro:
- ITEM "Item Avaliado" [TextBox String]
- NOTA "NOTA" [DropDownList String] itens: 1;2;3

### OPCAO_DE_CONFIRMACAO — Campo confirma uma afirmação
CheckBox Boolean → CP_ORDEM_SERVICO.OPCAO_DE_CONFIRMACAO
Descrição: Campo genérico para confirmação de uma afirmação

### NOME_FORNECEDOR — Nome do Fornecedor/Favorecido
TextBox String → CP_ORDEM_SERVICO.NOME_FORNECEDOR
Descrição: Fornecedor/Favorecido

### CSC_OBS — Observação
Memo String(2000) → CPE_CSC.CSC_OBS

### CSC_DATA_FIM — Data Fim
DatePicker DateTime → CPE_CSC.CSC_DATA_FIM

### GESTOR_SOLICITA — Gestor da área do Solicitante
DropDownList String → CPE_PESSOAS.GESTOR_SOLICITA

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### LABEL3 — Texto Informativo
Label String(1024) → CP_ORDEM_SERVICO.LABEL3

### LABEL4 — LABEL4
Label String(1024) → CPE_PDCI2019.LABEL4

### LABEL5 — Texto Informativo
Label String(1024) → CPE_ORDEM_SERVICO.LABEL5

### LABEL2 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL2
Descrição: Texto informativo

## Biblioteca de scripts referenciada
ebs, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
