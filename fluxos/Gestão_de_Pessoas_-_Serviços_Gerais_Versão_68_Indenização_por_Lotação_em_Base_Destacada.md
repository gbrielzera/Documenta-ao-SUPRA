# Fluxo: Indenização por Lotação em Base Destacada (IDENIZACAOBASE) — versão 68
Caminho: Fluxos > Gestão de Pessoas - Serviços Gerais Versão 68 Indenização por Lotação em Base Destacada
XML: `XMLs para teste/Gestão_de_Pessoas_-_Serviços_Gerais_Versão_68_Indenização_por_Lotação_em_Base_Destacada.xml` | Supravizio 19.1.1 | SubProcessoId 21132 | DesenhoProcessoId 2889 | ProcessoId 113
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: CARLOS ALBERTO REZENDE SOUZA NETO
Classe do subprocesso: Objetivo=Indenização por Base Destacada; DescricaoCliente=Indenização por Lotação em Base Destacada; CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Orgao; PublicarApontamentosAA=Nunca; ObjetivoPlano=Indenização por Base Destacada; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Indenização por lotação em base destacada (IDENIZACAO)

## Grafo do fluxo
- [362813] LinkInicial "" {Cliente} → [362815] Cálculo indenização
- [362814] EventoInicial "Indenização por Lotação em Base Destacada" → [362815] Cálculo indenização
- [362815] Tarefa "Cálculo indenização" {Cliente} → [G81449] Há Valores para pagamento?
- [362816] EventoIntermediarioMensagem "Aprovação Indenização por lotação em base destacada" → [362818] 
- [362817] EventoFinal "" → (fim)
- [362818] EventoFinal "" {Cliente} → (fim)
- [362819] Tarefa "Enviar para o ERP" {Cliente} → [362816] Aprovação Indenização por lotação em base destacad
- [G81449] Gateway "Há Valores para pagamento?" → «Sim» [362819] Enviar para o ERP | «Não» [362817] 

## Gateways
### [G81449] Há Valores para pagamento? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['VALOR_PRESTACAO'] == Convert.ToDecimal(0) or OrdemServico['VALOR_PRESTACAO'] == '0'
```
- alternativa → [362819] Enviar para o ERP: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [362817] : OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [362813] LinkInicial ""
Responsável: Cliente (papel 18)
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
AvancaProximaAtividade = True
```
**ScriptFim**
```python
OrdemServico.Servico.Sigla = 'IDENIZACAO'
OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
campos = ["ANO_REF", "CATEGORIA_IDENIZACAO", "COMBOBOX", "DIAS", "DIAS_DE_TRA", "LOG_API", "MES_REFERENCIA", "TE_CARGO", "TE_FUNCAO", "TE_MATRICULA", "TE_NOME_EMPREGADO", "TE_UOR", "TIPO_BASE"]

for campo in campos:
    Formulario[campo].Habilitado = False
```
- Operação PR0001 Preencher Campos
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=2
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] — Coluna=3
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — Coluna=2
  - COMBOBOX "Base Destacada" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
  - TIPO_BASE "Tipo de Base" [DropDownList String → CPE_ASSTECNICA.TIPO_BASE] — Coluna=2
  - CATEGORIA_IDENIZACAO "Categoria" [DropDownList String → CPE_ASSTECNICA.CATEGORIA_IDENIZACAO] — Coluna=3
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF] obrigatório — Coluna=2
  - DIAS_DE_TRA "Dias Úteis Trabalhados no Mês" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório — Coluna=3
  - DIAS "Dias úteis no mês" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] — Coluna=2
  - LOG_API "Controle LOG Douglas" [Memo String(2000) → CPE_DADOS.LOG_API] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - ID_PERSON "ID da Pessoa" [TextBox String → CP_ORDEM_SERVICO.ID_PERSON] obrigatório
- Associação de subprocesso: AssociacaoId=1483; Nome=CARLOS ALBERTO REZENDE SOUZA NETO; FraseAssociacao=Base Lote --> Base

### [362814] EventoInicial "Indenização por Lotação em Base Destacada"
Config: DisponibilidadeAplicacoes=SomenteWorkspace; Configuracao={"ServicoIniciador":"IDENIZACAO"}
**ScriptFim**
```python
#OrdemServico.ModificaCampoFormularioVisivel("DIAS", True)
```
**ScriptValidacao**
```python
mesAtual = Convert.ToInt32(DateTime.Now.ToString("MM"))
mesDeclarado = Convert.ToInt32(OrdemServico["MES_REFERENCIA"])

anoAtual = Convert.ToInt32(DateTime.Now.ToString("yyyy"))
anoDeclarado = Convert.ToInt32(OrdemServico["ANO_REF"])

today = DateTime.Now;
prevDate = DateTime(anoDeclarado, mesDeclarado, 01)
#Criticas.AdicionaPendencia(prevDate.ToString())

diasTrab = Convert.ToInt32(OrdemServico.GetCustom("DIAS_DE_TRA"))

if diasTrab >= 24:
    Criticas.AdicionaPendencia('A solicitação de indenização para base destacada está limitada a 23 dias por mês.')
        
#if (OrdemServico.GetCustom("DEC_AUX_HOM")  == False) :
#    Criticas.AdicionaPendencia("A declaração das condições para solicitar a indenização para base destacada é um campo obrigatório")
 

    
if anoDeclarado == anoAtual and mesDeclarado > mesAtual or anoDeclarado > anoAtual and mesDeclarado > mesAtual or anoDeclarado == anoAtual and mesDeclarado == mesAtual:
    Criticas.AdicionaPendencia("Não é permitido lançamentos futuros ou para o mês atual. Verifique sua solicitação e tente novamente.")
    
elif anoDeclarado > anoAtual:
    Criticas.AdicionaPendencia("Não é permitido lançamentos futuros ou para o mês atual. Verifique sua solicitação e tente novamente.")
    


diffOfDates = ((today.Year - prevDate.Year) * 12) + today.Month - prevDate.Month

if diffOfDates >= 4:
    Criticas.AdicionaPendencia("A abertura retroativa está limitada a até 3 meses a partir do mês atual.")


##Consulta retorna OS aberta e/ou finalizadas no mês e ano referente para o favorecido    
queryBaseDestacada = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, PESSOA.ID_PESSOA, OCORRENCIA.ID_CLIENTE, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME, CPE_CSC.MES_REFERENCIA, CPE_CSC.ANO_REF From OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_CLIENTE Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Where PESSOA.ID_PESSOA = '"+OrdemServico["TE_NOME_EMPREGADO"]+"' And OCORRENCIA.ASSUNTO = 'Indenização por Lotação em Base Destacada' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' or OCORRENCIA.SITUACAO = 'Aberto') And (CPE_CSC.MES_REFERENCIA = '"+OrdemServico["MES_REFERENCIA"]+"' And CPE_CSC.ANO_REF = '"+OrdemServico["ANO_REF"]+"') and OCORRENCIA.ID_OCORRENCIA != "+str(OrdemServico.Id))

if queryBaseDestacada.Rows.Count != 0:
    osNum = queryBaseDestacada.Rows[0]["NUMERO"]
    Criticas.AdicionaPendencia("Já existe a seguinte ordem de serviço para o mês e/ou ano referente: " + str(osNum))
```
**ScriptFormCarregado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
import peopleSoft
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

# ====================================================
mes_atual = DateTime.Now.Month

Formulario['ANO_REF'].Valor = DateTime.Now.Year.ToString() if mes_atual > 3 else (DateTime.Now.Year - 1).ToString()
Formulario['TE_NOME_EMPREGADO'].Habilitado = True
Formulario['DIAS'].Visivel = False
Formulario['DIAS_DE_TRA'].Habilitado = False



OrdemServico.Assunto = OrdemServico.Servico.DescricaoCliente

Formulario["TE_MATRICULA"].Visivel = False
Formulario["TE_CARGO"].Visivel = False
Formulario["TE_FUNCAO"].Visivel = False
Formulario["TE_UOR"].Visivel = False
Formulario['ID_PERSON'].Visivel = False

Formulario["TE_MATRICULA"].Habilitado = False
Formulario["TE_CARGO"].Habilitado = False
Formulario["TE_FUNCAO"].Habilitado = False
Formulario["TE_UOR"].Habilitado = False
Formulario['LOG_API'].Habilitado = False


Formulario["VALOR"].Visivel = False
Formulario["TIPO_BASE"].Habilitado = False
Formulario["CATEGORIA_IDENIZACAO"].Habilitado = False


Formulario['TE_NOME_EMPREGADO'].Valor = DB.ExecuteScalar("SELECT DISTINCT TO_CHAR(p.id_pessoa) AS id_pessoa, p.nome || ' (' || p.usuario_rede || ')' AS nomemat, cp.matricula, p.ativo FROM pessoa p inner join cp_pessoa cp on cp.id_pessoa = p.id_pessoa WHERE TIPO_COLABORADOR = 'Empregado' AND p.ativo = 'Sim' AND p.id_pessoa = '"+OrdemServico.ClienteId.ToString()+"'")

matricula = ""
cargo = ""
funcao = ""
uor = ""


if Formulario["TE_NOME_EMPREGADO"].Valor != "" or Formulario["TE_NOME_EMPREGADO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["TE_NOME_EMPREGADO"].Valor)
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
    Formulario["COMBOBOX"].Itens = "TR-AGUA BOA;TR-ALAGOINHAS;TR-ALFENAS;TR-ALMENARA;TR-ALTA FLORESTA;TR-ALTAMIRA;TR-ARIQUEMES;TR-BACABAL;TR-BALSAS;TR-BARRA DO GARCAS;TR-BARREIRAS;TR-CACOAL;TR-CANTO DO BURITI;TR-CASCAVEL;TR-CHAPADAO DO SUL;TR-CHAPADINHA;TR-CHAPECO;TR-COLIDER;TR-CRATO;TR-EUNAPOLIS;TR-FLORIANO;TR-FRANCISCO BELTRAO;TR-GOVERNADOR VALADARES;TR-GUANHAES;TR-IMPERATRIZ;TR-JACOBINA;TR-JANAUBA;TR-JEQUIE;TR-JUAZEIRO DO NORTE;TR-JUINA;TR-MARABA;TR-MONTES CLAROS;TR-NOVA RUSSAS;TR-OEIRAS;TR-PARAGOMINAS;TR-PARAUAPEBAS;TR-PEIXOTO DE AZEVEDO;TR-PICOS;TR-PIRIPIRI;TR-POCOS DE CALDAS;TR-POUSO ALEGRE;TR-PRESIDENTE DUTRA;TR-PRIMAVERA DO LESTE;TR-REALEZA;TR-REDENCAO;TR-RIBEIRA DO POMBAL;TR-ROSARIO;TR-SANTA INES;TR-SANTO ANTONIO DE JESUS;TR-SAO LOURENCO;TR-SINOP;TR-TEIXEIRA DE FREITAS;TR-TEOFILO OTONI;TR-URUCUI;TR-VARGINHA;TR-VILA RICA;TR-VITORIA DA CONQUISTA;TR-XINGUARA;TR-ARACAJU;TR-ARAGUAINA;TR-ARCOVERDE;TR-BARBACENA;TR-BELA CRUZ;TR-CACHOEIRO DE ITAPEMIRIM;TR-CAMPINA GRANDE;TR-CAMPOS BELOS;TR-CAMPOS DOS GOYTACAZES;TR-CANOINHAS;TR-CARNAIBA;TR-CASTANHAL;TR-CATAGUASES;TR-CAXIAS;TR-COXIM;TR-CURITIBANOS;TR-DIVINOPOLIS;TR-FEIRA DE SANTANA;TR-FERNANDOPOLIS;TR-GUARABIRA;TR-GUARACIABA DO NORTE;TR-GUARAPUAVA;TR-IGUATU;TR-IPATINGA;TR-ITABAIANA;TR-JOACABA;TR-JUIZ DE FORA;TR-LAGES;TR-LINHARES;TR-LUCAS DO RIO VERDE;TR-MANHUACU;TR-OURO PRETO;TR-PARNAIBA;TR-PASSOS;TR-PELOTAS;TR-PORANGATU;TR-POSSE;TR-PRESIDENTE PRUDENTE;TR-QUIRINOPOLIS;TR-RIO DO SUL;TR-SANTA MARIA;TR-SAO JOSE DE UBA;TR-SOBRAL;TR-TANGARA DA SERRA;TR-TRES LAGOAS;TR-UMUARAMA;TR-UNIAO DA VITORIA;TR-VIDEIRA;TR-ANAPOLIS;TR-APUCARANA;TR-ARACATI;TR-ARACATUBA;TR-ARAPIRACA;TR-ARARANGUA;TR-ARARAQUARA;TR-ARARUAMA;TR-ASSIS;TR-ATIBAIA;TR-AVARE;TR-BARRETOS;TR-BATURITE;TR-BENTO GONCALVES;TR-BLUMENAU;TR-CABO FRIO;TR-CALDAS NOVAS;TR-CAMPO MOURAO;TR-CAPANEMA;TR-CARAGUATATUBA;TR-CARUARU;TR-CAXIAS DO SUL;TR-CENTENARIO DO SUL;TR-CERES;TR-CIANORTE;TR-CIDADE DE GOIAS;TR-CORNELIO PROCOPIO;TR-CRICIUMA;TR-CRUZ ALTA;TR-ERECHIM;TR-FRANCA;TR-FREDERICO WESTPHALEN;TR-GARANHUNS;TR-GOIANIA;TR-GRAVATA;TR-GUARAI;TR-GUARAPARI;TR-GUARATINGUETA;TR-GURUPI;TR-IPORA;TR-ITAJAI;TR-ITUMBIARA;TR-IVAIPORA;TR-JAU;TR-JOAO MONLEVADE;TR-JUNDIAI;TR-LAJEADO;TR-LIMOEIRO;TR-LIMOEIRO DO NORTE;TR-MACAE;TR-MARAGOGI;TR-MARICA;TR-MARILIA;TR-MARINGA;TR-MOCOCA;TR-MOGI DAS CRUZES;TR-MOGI-MIRIM;TR-NITEROI;TR-NOVA FRIBURGO;TR-ORLEANS;TR-PARAÍSO;TR-PARANAGUA;TR-PARANAVAI;TR-PATOS DE MINAS;TR-PETROPOLIS;TR-PIRACICABA;TR-PONTA GROSSA;TR-QUIXADA;TR-REGISTRO;TR-RIBEIRAO;TR-RIO CLARO;TR-RIO VERDE;TR-RONDONOPOLIS;TR-SANTA CRUZ DO SUL;TR-SANTANA DO IPANEMA;TR-SANTO ANDRE;TR-SANTO ANGELO;TR-SANTOS;TR-SAO CARLOS;TR-SAO JOSE DO RIO PRETO;TR-SAO JOSE DOS CAMPOS;TR-SERRA TALHADA;TR-SETE LAGOAS;TR-SOROCABA;TR-TORRES;TR-TUBARAO;TR-UBERABA;TR-UMIRIM;TR-UNAI;TR-VOLTA REDONDA;TR-ALEGRETE;TR-ARACUAI;TR-BOA VISTA;TR-BOM JESUS;TR-BOM JESUS DA LAPA;TR-CRUZEIRO DO SUL;TR-GUANAMBI;TR-IRECE;TR-JI-PARANA;TR-MACAPA;TR-OBIDOS;TR-PARINTINS;TR-PETROLINA;TR-PINHEIRO;TR-RORAINÓPOLIS;TR-SALGUEIRO;TR-SANTAREM;TR-SEABRA;TR-TABATINGA;TR-TEFE;TR-VILHENA;TR-ANGICOS;TR-CORUMBA;TR-CURRAIS NOVOS;TR-MOSSORO;TR-PATOS;TR-PAULO AFONSO;TR-RIO BRANCO;TR-SERRINHA;TR-SOUSA;TR-TUCURUI;TR-BAGE;TR-CACERES;TR-COLATINA;TR-DOURADOS;TR-FOZ DO IGUACU;TR-IGARAPE-MIRI;TR-JARDIM;TR-NOVA VENECIA;TR-SANTA ROSA;TR-SAO MIGUEL DO OESTE;TR-ITACOATIARA;TR-ILHEUS;TR-SANTO ANTONIO DA PLATINA"
    
    
##----------------------------------------------------------------------------------------------------------------------------------------------------------------

Formulario["VALOR"].Visivel = False
Formulario["TIPO_BASE"].Habilitado = False
Formulario["CATEGORIA_IDENIZACAO"].Habilitado = False
Formulario["TE_FUNCAO"].Visivel = False

Formulario['LABEL_GRANDE'].Valor = '<div style="display: flex; justify-content: center; align-items: center;"><div style="display: flex; align-items: center; width: 100%; background: linear-gradient(90deg, blue, rgb(2, 0, 18)); border-radius: 16px; padding: 2%;"><img src="https://intranet.bbts.com.br/templates/intranet/images/LogoTemplate-Agosto2025.gif" alt="Ícone" style="height: 40px; margin-right: 16px;"><br><p style="flex: 1; text-align: center; color: yellow; font-weight: 600; font-size: 16px; font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif; margin: 0;">A solicitação da Indenização por Lotação em Base Destacada deve ser proporcional aos dias úteis trabalhados, conforme preenchimento neste chamado.<br>O ressarcimento é devido aos empregados que residam em um dos municípios de atendimento da base destacada. <br>As solicitações abertas para meses futuros serão desconsideradas. <br>Caso haja mais de uma solicitação para o mesmo mês, somente será considerada a última solicitação aprovada pelo Gestor do empregado. <br>A indenização não se aplica à técnicos temporários, terceiros ou empregados lotados na base CAT deslocados para apoio temporário à base destacada. <br></p></div></div><br><br>'
```
- Operação PR0001 Preencher Campos
  - LABEL_GRANDE "A indenização não se aplica à técnicos temporários, terceiros ou empregados lotados na base CAT deslocados para apoio temporário à base destacada." [Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE]
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
**TE_NOME_EMPREGADO.ScriptModificado**
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

if Formulario["TE_NOME_EMPREGADO"].Valor != "" or Formulario["TE_NOME_EMPREGADO"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["TE_NOME_EMPREGADO"].Valor)
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
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório — Coluna=2
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório — Coluna=3
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — Coluna=2
  - COMBOBOX "Base Destacada" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
**COMBOBOX.ScriptModificado**
```python
config = {
 "TR-ACARAÚ": ("283,02", "COMUM", "C"),
 "TR-AGUA BOA": ("462,07", "COMUM", "A"),
 "TR-ALAGOINHAS": ("283,02", "COMUM", "C"),
 "TR-ALEGRETE": ("571,82", "ESPECIAL", "C"),
 "TR-ALFENAS": ("462,07", "COMUM", "A"),
 "TR-ALMENARA": ("462,07", "COMUM", "A"),
 "TR-ALTA FLORESTA": ("462,07", "COMUM", "A"),
 "TR-ALTAMIRA": ("462,07", "COMUM", "A"),
 "TR-ANAPOLIS": ("283,02", "COMUM", "C"),
 "TR-ANGICOS": ("658,46", "ESPECIAL", "B"),
 "TR-APUCARANA": ("283,02", "COMUM", "C"),
 "TR-ARACAJU": ("369,66", "COMUM", "B"),
 "TR-ARACATI": ("283,02", "COMUM", "C"),
 "TR-ARACATUBA": ("283,02", "COMUM", "C"),
 "TR-ARACUAI": ("571,82", "ESPECIAL", "C"),
 "TR-ARAGUAINA": ("369,66", "COMUM", "B"),
 "TR-ARAPIRACA": ("283,02", "COMUM", "C"),
 "TR-ARARANGUA": ("283,02", "COMUM", "C"),
 "TR-ARARAQUARA": ("283,02", "COMUM", "C"),
 "TR-ARARUAMA": ("283,02", "COMUM", "C"),
 "TR-ARCOVERDE": ("369,66", "COMUM", "B"),
 "TR-ARIQUEMES": ("283,02", "COMUM", "C"),
 "TR-ASSIS": ("283,02", "COMUM", "C"),
 "TR-ATIBAIA": ("283,02", "COMUM", "C"),
 "TR-AVARE": ("283,02", "COMUM", "C"),
 "TR-BACABAL": ("462,07", "COMUM", "A"),
 "TR-BAGE": ("571,82", "ESPECIAL", "C"),
 "TR-BALSAS": ("462,07", "COMUM", "A"),
 "TR-BARBACENA": ("369,66", "COMUM", "B"),
 "TR-BARRA DO GARCAS": ("462,07", "COMUM", "A"),
 "TR-BARREIRAS": ("462,07", "COMUM", "A"),
 "TR-BARRETOS": ("283,02", "COMUM", "C"),
 "TR-BATURITE": ("283,02", "COMUM", "C"),
 "TR-BELA CRUZ": ("369,66", "COMUM", "B"),
 "TR-BENTO GONCALVES": ("283,02", "COMUM", "C"),
 "TR-BLUMENAU": ("283,02", "COMUM", "C"),
 "TR-BOA VISTA": ("750,87", "ESPECIAL", "A"),
 "TR-BOM JESUS": ("750,87", "ESPECIAL", "A"),
 "TR-BOM JESUS DA LAPA": ("750,87", "ESPECIAL", "A"),
 "TR-CABO FRIO": ("283,02", "COMUM", "C"),
 "TR-CACERES": ("571,82", "ESPECIAL", "C"),
 "TR-CACHOEIRO DE ITAPEMIRIM": ("369,66", "COMUM", "B"),
 "TR-CACOAL": ("369,66", "COMUM", "B"),
 "TR-CALDAS NOVAS": ("283,02", "COMUM", "C"),
 "TR-CAMPINA GRANDE": ("369,66", "COMUM", "B"),
 "TR-CAMPO MOURAO": ("283,02", "COMUM", "C"),
 "TR-CAMPOS BELOS": ("369,66", "COMUM", "B"),
 "TR-CAMPOS DOS GOYTACAZES": ("369,66", "COMUM", "B"),
 "TR-CANOINHAS": ("369,66", "COMUM", "B"),
 "TR-CANTO DO BURITI": ("462,07", "COMUM", "A"),
 "TR-CAPANEMA": ("283,02", "COMUM", "C"),
 "TR-CARAGUATATUBA": ("283,02", "COMUM", "C"),
 "TR-CARNAIBA": ("369,66", "COMUM", "B"),
 "TR-CARUARU": ("283,02", "COMUM", "C"),
 "TR-CASCAVEL": ("462,07", "COMUM", "A"),
 "TR-CASTANHAL": ("369,66", "COMUM", "B"),
 "TR-CATAGUASES": ("369,66", "COMUM", "B"),
 "TR-CAXIAS": ("369,66", "COMUM", "B"),
 "TR-CAXIAS DO SUL": ("283,02", "COMUM", "C"),
 "TR-CENTENARIO DO SUL": ("283,02", "COMUM", "C"),
 "TR-CERES": ("283,02", "COMUM", "C"),
 "TR-CHAPADAO DO SUL": ("462,07", "COMUM", "A"),
 "TR-CHAPADINHA": ("462,07", "COMUM", "A"),
 "TR-CHAPECO": ("462,07", "COMUM", "A"),
 "TR-CIANORTE": ("283,02", "COMUM", "C"),
 "TR-CIDADE DE GOIAS": ("283,02", "COMUM", "C"),
 "TR-COLATINA": ("571,82", "ESPECIAL", "C"),
 "TR-COLIDER": ("462,07", "COMUM", "A"),
 "TR-CORNELIO PROCOPIO": ("283,02", "COMUM", "C"),
 "TR-CORUMBA": ("658,46", "ESPECIAL", "B"),
 "TR-COXIM": ("369,66", "COMUM", "B"),
 "TR-CRATO": ("462,07", "COMUM", "A"),
 "TR-CRICIUMA": ("283,02", "COMUM", "C"),
 "TR-CRUZ ALTA": ("283,02", "COMUM", "C"),
 "TR-CRUZEIRO DO SUL": ("750,87", "ESPECIAL", "A"),
 "TR-CURITIBANOS": ("369,66", "COMUM", "B"),
 "TR-CURRAIS NOVOS": ("658,46", "ESPECIAL", "B"),
 "TR-DIVINOPOLIS": ("369,66", "COMUM", "B"),
 "TR-DOURADOS": ("571,82", "ESPECIAL", "C"),
 "TR-ERECHIM": ("283,02", "COMUM", "C"),
 "TR-EUNAPOLIS": ("462,07", "COMUM", "A"),
 "TR-FEIRA DE SANTANA": ("369,66", "COMUM", "B"),
 "TR-FERNANDOPOLIS": ("369,66", "COMUM", "B"),
 "TR-FLORIANO": ("462,07", "COMUM", "A"),
 "TR-FOZ DO IGUACU": ("571,82", "ESPECIAL", "C"),
 "TR-FRANCA": ("283,02", "COMUM", "C"),
 "TR-FRANCISCO BELTRAO": ("369,66", "COMUM", "B"),
 "TR-FREDERICO WESTPHALEN": ("283,02", "COMUM", "C"),
 "TR-GARANHUNS": ("283,02", "COMUM", "C"),
 "TR-GOIANA": ("283,02", "COMUM", "C"),
 "TR-GOVERNADOR VALADARES": ("462,07", "COMUM", "A"),
 "TR-GRAVATA": ("283,02", "COMUM", "C"),
 "TR-GUANAMBI": ("750,87", "ESPECIAL", "A"),
 "TR-GUANHAES": ("462,07", "COMUM", "A"),
 "TR-GUARABIRA": ("369,66", "COMUM", "B"),
 "TR-GUARACIABA DO NORTE": ("369,66", "COMUM", "B"),
 "TR-GUARAI": ("283,02", "COMUM", "C"),
 "TR-GUARAPARI": ("283,02", "COMUM", "C"),
 "TR-GUARAPUAVA": ("369,66", "COMUM", "B"),
 "TR-GUARATINGUETA": ("283,02", "COMUM", "C"),
 "TR-GURUPI": ("283,02", "COMUM", "C"),
 "TR-IBAITI": ("369,66", "COMUM", "B"),
 "TR-IGARAPE-MIRI": ("571,82", "ESPECIAL", "C"),
 "TR-IGUATU": ("369,66", "COMUM", "B"),
 "TR-IMPERATRIZ": ("462,07", "COMUM", "A"),
 "TR-IPATINGA": ("369,66", "COMUM", "B"),
 "TR-IPORA": ("283,02", "COMUM", "C"),
 "TR-IRECE": ("750,87", "ESPECIAL", "A"),
 "TR-ITABAIANA": ("369,66", "COMUM", "B"),
 "TR-ITABUNA": ("462,07", "COMUM", "A"),
 "TR-ITAJAI": ("283,02", "COMUM", "C"),
 "TR-ITUMBIARA": ("283,02", "COMUM", "C"),
 "TR-IVAIPORA": ("283,02", "COMUM", "C"),
 "TR-JACOBINA": ("462,07", "COMUM", "A"),
 "TR-JANAUBA": ("462,07", "COMUM", "A"),
 "TR-JARDIM": ("571,82", "ESPECIAL", "C"),
 "TR-JAU": ("283,02", "COMUM", "C"),
 "TR-JEQUIE": ("462,07", "COMUM", "A"),
 "TR-JI-PARANA": ("658,46", "ESPECIAL", "B"),
 "TR-JOACABA": ("369,66", "COMUM", "B"),
 "TR-JOAO MONLEVADE": ("283,02", "COMUM", "C"),
 "TR-JUAZEIRO DO NORTE": ("462,07", "COMUM", "A"),
 "TR-JUINA": ("462,07", "COMUM", "A"),
 "TR-JUIZ DE FORA": ("369,66", "COMUM", "B"),
 "TR-JUNDIAI": ("283,02", "COMUM", "C"),
 "TR-LAGES": ("369,66", "COMUM", "B"),
 "TR-LAJEADO": ("283,02", "COMUM", "C"),
 "TR-LIMOEIRO": ("283,02", "COMUM", "C"),
 "TR-LIMOEIRO DO NORTE": ("283,02", "COMUM", "C"),
 "TR-LINHARES": ("369,66", "COMUM", "B"),
 "TR-LUCAS DO RIO VERDE": ("369,66", "COMUM", "B"),
 "TR-MACAE": ("283,02", "COMUM", "C"),
 "TR-MACAPA": ("750,87", "ESPECIAL", "A"),
 "TR-MANHUACU": ("369,66", "COMUM", "B"),
 "TR-MARAGOGI":("283,02", "COMUM", "C"),
 "TR-MARABA": ("462,07", "COMUM", "A"),
 "TR-MARAGOGI": ("283,02", "COMUM", "C"),
 "TR-MARICA": ("283,02", "COMUM", "C"),
 "TR-MARILIA": ("283,02", "COMUM", "C"),
 "TR-MARINGA": ("283,02", "COMUM", "C"),
 "TR-MOCOCA": ("283,02", "COMUM", "C"),
 "TR-MOGI DAS CRUZES": ("283,02", "COMUM", "C"),
 "TR-MOGI-MIRIM": ("283,02", "COMUM", "C"),
 "TR-MONTES CLAROS": ("462,07", "COMUM", "A"),
 "TR-MOSSORO": ("658,46", "ESPECIAL", "B"),
 "TR-NITEROI": ("283,02", "COMUM", "C"),
 "TR-NOVA FRIBURGO": ("283,02", "COMUM", "C"),
 "TR-NOVA RUSSAS": ("462,07", "COMUM", "A"),
 "TR-NOVA VENECIA": ("571,82", "ESPECIAL", "C"),
 "TR-OBIDOS": ("750,87", "ESPECIAL", "A"),
 "TR-OEIRAS": ("462,07", "COMUM", "A"),
 "TR-ORLEANS": ("283,02", "COMUM", "C"),
 "TR-OURO PRETO": ("369,66", "COMUM", "B"),
 "TR-PARAGOMINAS": ("462,07", "COMUM", "A"),
 "TR-PARANAGUA": ("283,02", "COMUM", "C"),
 "TR-PARANAVAI": ("283,02", "COMUM", "C"),
 "TR-PARAUAPEBAS": ("462,07", "COMUM", "A"),
 "TR-PARAÍSO": ("369,66", "COMUM", "B"),
 "TR-PARINTINS": ("750,87", "ESPECIAL", "A"),
 "TR-PARNAIBA": ("369,66", "COMUM", "B"),
 "TR-PASSOS": ("369,66", "COMUM", "B"),
 "TR-PATOS": ("658,46", "ESPECIAL", "B"),
 "TR-PATOS DE MINAS": ("283,02", "COMUM", "C"),
 "TR-PAULO AFONSO": ("658,46", "ESPECIAL", "B"),
 "TR-PEIXOTO DE AZEVEDO": ("462,07", "COMUM", "A"),
 "TR-PELOTAS": ("369,66", "COMUM", "B"),
 "TR-PETROLINA": ("750,87", "ESPECIAL", "A"),
 "TR-PETROPOLIS": ("283,02", "COMUM", "C"),
 "TR-PICOS": ("462,07", "COMUM", "A"),
 "TR-PINHEIRO": ("462,07", "COMUM", "A"),
 "TR-PIRACICABA": ("283,02", "COMUM", "C"),
 "TR-PIRIPIRI": ("462,07", "COMUM", "A"),
 "TR-POCOS DE CALDAS": ("369,66", "COMUM", "B"),
 "TR-PONTA GROSSA": ("283,02", "COMUM", "C"),
 "TR-PORANGATU": ("369,66", "COMUM", "B"),
 "TR-POSSE": ("369,66", "COMUM", "B"),
 "TR-POUSO ALEGRE": ("462,07", "COMUM", "A"),
 "TR-PRESIDENTE DUTRA": ("462,07", "COMUM", "A"),
 "TR-PRESIDENTE PRUDENTE": ("369,66", "COMUM", "B"),
 "TR-PRIMAVERA DO LESTE": ("369,66", "COMUM", "B"),
 "TR-QUIRINOPOLIS": ("369,66", "COMUM", "B"),
 "TR-QUIXADA": ("283,02", "COMUM", "C"),
 "TR-REALEZA": ("462,07", "COMUM", "A"),
 "TR-REDENCAO": ("462,07", "COMUM", "A"),
 "TR-REGISTRO": ("283,02", "COMUM", "C"),
 "TR-RIBEIRA DO POMBAL": ("462,07", "COMUM", "A"),
 "TR-RIBEIRAO": ("283,02", "COMUM", "C"),
 "TR-RIO BRANCO": ("750,87", "ESPECIAL", "A"),
 "TR-RIO CLARO": ("283,02", "COMUM", "C"),
 "TR-RIO DO SUL": ("369,66", "COMUM", "B"),
 "TR-RIO VERDE": ("283,02", "COMUM", "C"),
 "TR-RONDONOPOLIS": ("283,02", "COMUM", "C"),
 "TR-RORAINÓPOLIS": ("658,46", "ESPECIAL", "B"),
 "TR-ROSARIO": ("462,07", "COMUM", "A"),
 "TR-SALGUEIRO": ("750,87", "ESPECIAL", "A"),
 "TR-SANTA CRUZ DO SUL": ("283,02", "COMUM", "C"),
 "TR-SANTA INES": ("462,07", "COMUM", "A"),
 "TR-SANTA MARIA": ("369,66", "COMUM", "B"),
 "TR-SANTA ROSA": ("571,82", "ESPECIAL", "C"),
 "TR-SANTANA DO IPANEMA": ("283,02", "COMUM", "C"),
 "TR-SANTAREM": ("750,87", "ESPECIAL", "A"),
 "TR-SANTO ANDRE": ("283,02", "COMUM", "C"),
 "TR-SANTO ANGELO": ("283,02", "COMUM", "C"),
 "TR-SANTO ANTONIO DE JESUS": ("462,07", "COMUM", "A"),
 "TR-SANTOS": ("283,02", "COMUM", "C"),
 "TR-SAO CARLOS": ("283,02", "COMUM", "C"),
 "TR-SAO JOSE DE UBA": ("369,66", "COMUM", "B"),
 "TR-SAO JOSE DO RIO PRETO": ("283,02", "COMUM", "C"),
 "TR-SAO JOSE DOS CAMPOS": ("283,02", "COMUM", "C"),
 "TR-SAO LOURENCO": ("462,07", "COMUM", "A"),
 "TR-SAO MIGUEL DO OESTE": ("571,82", "ESPECIAL", "C"),
 "TR-SEABRA": ("750,87", "ESPECIAL", "A"),
 "TR-SERRA TALHADA": ("369,66", "COMUM", "B"),
 "TR-SERRINHA": ("658,46", "ESPECIAL", "B"),
 "TR-SETE LAGOAS": ("283,02", "COMUM", "C"),
 "TR-SINOP": ("462,07", "COMUM", "A"),
 "TR-SOBRAL": ("369,66", "COMUM", "B"),
 "TR-SOROCABA": ("283,02", "COMUM", "C"),
 "TR-SOUSA": ("658,46", "ESPECIAL", "B"),
 "TR-TABATINGA": ("750,87", "ESPECIAL", "A"),
 "TR-TANGARA DA SERRA": ("369,66", "COMUM", "B"),
 "TR-TEFE": ("750,87", "ESPECIAL", "A"),
 "TR-TEIXEIRA DE FREITAS": ("462,07", "COMUM", "A"),
 "TR-TEOFILO OTONI": ("462,07", "COMUM", "A"),
 "TR-TORRES": ("283,02", "COMUM", "C"),
 "TR-TRES LAGOAS": ("369,66", "COMUM", "B"),
 "TR-TUBARAO": ("283,02", "COMUM", "C"),
 "TR-TUCURUI": ("658,46", "ESPECIAL", "B"),
 "TR-UBERABA": ("283,02", "COMUM", "C"),
 "TR-UMIRIM": ("283,02", "COMUM", "C"),
 "TR-UMUARAMA": ("369,66", "COMUM", "B"),
 "TR-UNAI": ("283,02", "COMUM", "C"),
 "TR-UNIAO DA VITORIA": ("369,66", "COMUM", "B"),
 "TR-URUCUI": ("462,07", "COMUM", "A"),
 "TR-VARGINHA": ("462,07", "COMUM", "A"),
 "TR-VIDEIRA": ("369,66", "COMUM", "B"),
 "TR-VILA RICA": ("462,07", "COMUM", "A"),
 "TR-VILHENA": ("750,87", "ESPECIAL", "A"),
 "TR-VITORIA DA CONQUISTA": ("462,07", "COMUM", "A"),
 "TR-VOLTA REDONDA": ("283,02", "COMUM", "C"),
 "TR-XINGUARA": ("462,07", "COMUM", "A"),
}


base = Formulario["COMBOBOX"].Valor
dados = config.get(base)

if dados:
    valor, tipo, categoria = dados
    Formulario["VALOR"].Valor = valor
    Formulario["TIPO_BASE"].Valor = tipo
    Formulario["CATEGORIA_IDENIZACAO"].Valor = categoria
else:
    # fallback quando não achar a base
    Formulario["VALOR"].Valor = ""
    Formulario["TIPO_BASE"].Valor = ""
    Formulario["CATEGORIA_IDENIZACAO"].Valor = ""
```
  - TIPO_BASE "Tipo de Base" [DropDownList String → CPE_ASSTECNICA.TIPO_BASE] obrigatório — Coluna=2
  - CATEGORIA_IDENIZACAO "Categoria" [DropDownList String → CPE_ASSTECNICA.CATEGORIA_IDENIZACAO] obrigatório — Coluna=3
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
**MES_REFERENCIA.ScriptModificado**
```python
if not String.IsNullOrEmpty(str(Formulario['MES_REFERENCIA'].Valor)):
    Formulario['ANO_REF'].Habilitado = True
    Formulario['ANO_REF'].Visivel = True
```
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF] obrigatório — Coluna=2
**ANO_REF.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Feriado
from Venki.Supravizio.Recurso.Custom import Local
import peopleSoft
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.
'''from System import *


# ======================= VARIÁVEIS NECESSÁRIAS ============================================

mesDeclarado = Convert.ToInt32(Formulario["MES_REFERENCIA"].Valor)
anoDeclarado = Convert.ToInt32(Formulario["ANO_REF"].Valor)
prevDate = DateTime(anoDeclarado, mesDeclarado, 1)
matricula = str(Formulario['TE_MATRICULA'].Valor)
dataFormatada = prevDate.ToString("dd-MM-yyyy")
base_supravizio = Formulario['COMBOBOX'].Valor
base_SV_formatada = base_supravizio.split("-")[1].ToString()

# ======================= CONSULTA AUSENCIAS (PEOPLESOFT) ===================================

ausencias = consultaAusencias(matricula, dataFormatada)
for linha in ausencias:
    matricula = linha["cdMatricula"].ToString()
    dataInicio = linha["dtInicio"].ToString()
    dataFim = linha["dtFim"].ToString()
    tipo = linha["nmTipoAbs"].ToString()
    duracao = linha['nrDuracaoAbs'].ToString()
    diasDuracao = linha['nrDiasDuracao'].ToString()
    hrsDuracao = linha['nrHorasDuracao'].ToString()

mes_relatorio = dataInicio.split('-')[1]



# ======================= CONSULTA FUNCIONARIOS (PEOPLESOFT) ===================================

local = consultaFuncionarios('A',matricula)
for linha in local:
    situacao = linha['tpSituacao'].ToString()
    tr_local = linha['nmLocal'].ToString()
    nome = linha['nmNome'].ToString()

Formulario['LOG_API'].Valor = '=== AUSENCIAS ===\n\n' + 'Nome: ' + nome + '\nMatricula: ' + matricula +  '\nData Inicio: ' +  dataInicio + '\nData Fim: ' + dataFim + '\nTipo: ' + tipo + '\nDuração: ' + duracao + '\nDuração em Dias: ' + diasDuracao + '\nDuração em Horas: ' + hrsDuracao + '\n\n === LOCALIDADE === \n\n' + 'Localidade: ' + tr_local + '\n'



# ======================= FUNÇÃO PARA CALCULAR DIAS ÚTEIS DO MÊS E ANO SELECIONADO =======================

def ObterDiasUteis(ano, mes):
    dias_uteis = []
    dias_no_mes = DateTime.DaysInMonth(ano, mes)
    
    for dia in range(1, dias_no_mes + 1):
        data = DateTime(ano, mes, dia)
        if data.DayOfWeek != DayOfWeek.Saturday and data.DayOfWeek != DayOfWeek.Sunday:
            dias_uteis.append(data)
            
    return dias_uteis
    
dias = ObterDiasUteis(anoDeclarado, mesDeclarado)



# =============================================== PREENCHIMENTO DO CAMPO DIAS E SUAS DEVIDAS VALIÇÕES: ===============================================

# Verificação na tabela Feriados para ver se na TR que o técnico tá lotada tem feriados municipais
feriado_na_cidade_locada = DB.ExecuteDataTable("select * from tb_feriados_municipais fer where fer.CIDADE LIKE '" + base_SV_formatada +"'")

if feriado_na_cidade_locada.Rows.Count > 0:
    lista_feriados = [d["DT_FERIADO"].ToString("dd/MM/yyyy") for d in feriado_na_cidade_locada.Rows]
    feriados_convertidos = [DateTime.ParseExact(data, "dd/MM/yyyy", None) for data in lista_feriados]

    # Converte datas de férias (vindas da API)
    inicio_ferias = DateTime.ParseExact(dataInicio, "dd-MM-yyyy", None)
    fim_ferias = DateTime.ParseExact(dataFim, "dd-MM-yyyy", None)

    # Verifica se algum feriado está dentro do período de férias
    feriados_durante_ferias = [f for f in feriados_convertidos if f >= inicio_ferias and f <= fim_ferias]

    texto_feriados = "\n".join([f.ToString("dd/MM/yyyy") for f in feriados_durante_ferias])
    mes_feriados = [f.ToString("MM") for f in feriados_durante_ferias]

    if feriados_durante_ferias:
        Formulario['LOG_API'].Valor += "\n\nDias Úteis: {0}\nFeriados durante as férias:\n{1}\nMês dos Feriados: {2}".format(len(dias), texto_feriados, mes_feriados)
    else:
        Formulario['LOG_API'].Valor += "\n\nDias Úteis: {0}\nNão há feriados durante o período de férias.".format(len(dias))
else:
    Formulario['LOG_API'].Valor += "\n\nNão há feriados locais na TR que o(a) técnico(a) está lotado(a) no mês indicado."









Formulario['DIAS_DE_TRA'].Valor = len(dias)'''
```
  - DIAS_DE_TRA "Dias Úteis Trabalhados no Mês" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório — Coluna=3
  - VALOR "Valor da base" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - DIAS "Dias úteis no mês" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] — Coluna=2
  - CHECKBOX1 "CLIQUE AQUI PARA CALCULAR OS DIAS ÚTEIS TRABALHADOS" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX1] obrigatório
**CHECKBOX1.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Feriado
from Venki.Supravizio.Recurso.Custom import Local
import peopleSoft
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

COLETAR_AUSENCIAS_MODO = "daily"
Formulario['LOG_API'].Valor = ''


try:
    from System import String as NetString
except:
    NetString = None

def is_string(obj):
    if obj is None:
        return False
    try:
        if isinstance(obj, str):
            return True
    except:
        pass
        
    if NetString:
        try:
            if isinstance(obj, NetString):
                return True
        except:
            pass
    try:
        return obj.GetType().FullName == "System.String"
    except:
        return False

def to_str(x):
    try:
        return x.ToString()
    except:
        try:
            return str(x)
        except:
            return ""

def ParseDateSafe(s):
    if not s:
        return None
    formatos = ["dd-MM-yyyy", "dd/MM/yyyy", "yyyy-MM-dd", "yyyy/MM/dd", "dd.MM.yyyy", "yyyy.MM.dd"]
    for f in formatos:
        try:
            return DateTime.ParseExact(s, f, None)
        except:
            pass
    return None

def ObterDiasUteis(ano, mes):
    dias_uteis = []
    dias_no_mes = DateTime.DaysInMonth(ano, mes)
    for dia in range(1, dias_no_mes + 1):
        data = DateTime(ano, mes, dia)
        if data.DayOfWeek != DayOfWeek.Saturday and data.DayOfWeek != DayOfWeek.Sunday:
            dias_uteis.append(data)
    return dias_uteis

def clamp_periodo_ao_mes(di, df, ano, mes):
    if di is None or df is None:
        return (None, None)
    inicio_mes = DateTime(ano, mes, 1)
    fim_mes = DateTime(ano, mes, DateTime.DaysInMonth(ano, mes))
    ini = di if di > inicio_mes else inicio_mes
    fim = df if df < fim_mes else fim_mes
    if ini > fim:
        return (None, None)
    return (ini, fim)

def periodo_para_dias_uteis_set(di, df):
    s = set()
    if di is None or df is None:
        return s
    d = di
    while d <= df:
        if d.DayOfWeek != DayOfWeek.Saturday and d.DayOfWeek != DayOfWeek.Sunday:
            s.add(d.Date)  # usar .Date para normalizar
        d = d.AddDays(1)
    return s

def coletar_ausencias_mes(matricula, ano, mes):
    """
    Coleta todas as ausências no mês/ano dado.
    - Modo 'daily': consulta a API em cada dia do mês e agrega.
    - Modo 'single': consulta apenas no dia 01.
    Retorna uma lista de 'linhas' (JToken-like) sem duplicatas (por dtInicio/dtFim/tipo).
    """
    dias_no_mes = DateTime.DaysInMonth(ano, mes)

    def chama_api(data_dt):
        # peopleSoft.consultaAusencias espera data "dd-MM-yyyy"
        data_str = data_dt.ToString("dd-MM-yyyy")
        return consultaAusencias(matricula, data_str)

    vistos = set()
    agregadas = []

    if COLETAR_AUSENCIAS_MODO == "daily":
        resultados = [chama_api(DateTime(ano, mes, 1))]
    else:
        resultados = []
        for dia in range(1, dias_no_mes + 1):
            resultados.append(chama_api(DateTime(ano, mes, dia)))

    # Processa cada retorno
    for res in resultados:
        if res is None or is_string(res):
            # String/mensagem: ignorar para agregação
            continue

        # Iterável (JArray/JToken[]/lista)
        try:
            for linha in res:
                try:
                    di_raw = to_str(linha["dtInicio"])
                    df_raw = to_str(linha["dtFim"])
                    tp_raw = to_str(linha["nmTipoAbs"])
                except:
                    # Estrutura inesperada
                    continue

                key = (di_raw, df_raw, tp_raw)
                if key in vistos:
                    continue
                vistos.add(key)
                agregadas.append(linha)
        except:
            # Não iterável útil
            continue

    # Filtra as que realmente INTERSECTAM o mês/ano
    filtradas = []
    for linha in agregadas:
        di = ParseDateSafe(to_str(linha["dtInicio"]))
        df = ParseDateSafe(to_str(linha["dtFim"]))
        ini, fim = clamp_periodo_ao_mes(di, df, ano, mes)
        if ini is not None:
            filtradas.append(linha)

    return filtradas

# ======================= VARIÁVEIS INICIAIS ======================================
dataInicio = ''
dataFim = ''
tipo = ''
duracao = ''
diasDuracao = ''
hrsDuracao = ''
nome = ''
tr_local = ''
situacao = ''

mesDeclarado =      Convert.ToInt32(Formulario["MES_REFERENCIA"].Valor)
anoDeclarado =      Convert.ToInt32(Formulario["ANO_REF"].Valor)
dataRef =           DateTime(anoDeclarado, mesDeclarado, 1)
matricula =         to_str(Formulario['TE_MATRICULA'].Valor)
base_supravizio =   to_str(Formulario['COMBOBOX'].Valor)
base_SV_formatada = base_supravizio[3:] if base_supravizio and len(base_supravizio) > 3 else base_supravizio

# ======================= COLETA TODAS AS AUSÊNCIAS DO MÊS ========================
ausencias_mes = coletar_ausencias_mes(matricula, anoDeclarado, mesDeclarado)

# Extrai informações consolidadas do mês: conjunto de DIAS ÚTEIS AUSENTES
dias_ausentes_set = set()
lista_resumo_aus = []  # para LOG

for linha in ausencias_mes:
    di = ParseDateSafe(to_str(linha["dtInicio"]))
    df = ParseDateSafe(to_str(linha["dtFim"]))
    ini, fim = clamp_periodo_ao_mes(di, df, anoDeclarado, mesDeclarado)
    if ini is None:
        continue

    # Concatena o set de dias úteis deste período
    dias_periodo = periodo_para_dias_uteis_set(ini, fim)
    dias_ausentes_set |= dias_periodo

    # Campos opcionais para log
    try: tipo = to_str(linha["nmTipoAbs"])
    except: tipo = ''
    try: duracao = to_str(linha.get("nrDuracaoAbs")) if hasattr(linha, "get") else to_str(linha["nrDuracaoAbs"])
    except: duracao = ''
    try: diasDuracao = to_str(linha.get("nrDiasDuracao")) if hasattr(linha, "get") else to_str(linha["nrDiasDuracao"])
    except: diasDuracao = ''
    try: hrsDuracao = to_str(linha.get("nrHorasDuracao")) if hasattr(linha, "get") else to_str(linha["nrHorasDuracao"])
    except: hrsDuracao = ''

    lista_resumo_aus.append({
        "inicio": ini,
        "fim": fim,
        "tipo": tipo,
        "dias_uteis_no_mes": len(dias_periodo),
        "duracao_bruta": duracao,
        "diasDuracao": diasDuracao,
        "hrsDuracao": hrsDuracao
    })

# ======================= CONSULTA FUNCIONARIO / LOCAL ============================
id_fav = Convert.ToInt32(Formulario['TE_NOME_EMPREGADO'].Valor)
Formulario['ID_PERSON'].Valor = id_fav
ativo = DB.ExecuteDataTable("SELECT P.ID_PESSOA, P.NOME, P.ATIVO FROM PESSOA P WHERE P.ID_PESSOA LIKE '"+to_str(id_fav)+"'")

status = 'A'  # manter como no original
if status == 'A':   
    local = consultaFuncionarios('A', matricula)  
else:
    Formulario.ExibeMensagem('O funcionário está com status de demitido. Por favor, escolha alguém "Ativo".')
    local = consultaFuncionarios('I', matricula)

# Extrai nome/local (se houver)
if local is not None and not is_string(local):
    try:
        # pega a primeira linha
        it = iter(local)
        linha_loc = next(it)
        try: situacao = to_str(linha_loc['tpSituacao'])
        except: situacao = ''
        try: tr_local = to_str(linha_loc['nmLocal'])
        except: tr_local = ''
        try: nome = to_str(linha_loc['nmNome'])
        except: nome = ''
        try: uf = to_str(linha_loc['cdUF'])
        except: uf = ''
    except:
        pass
else:
    # Mensagem de erro? Mostra uma vez.
    if is_string(local):
        Formulario.ExibeMensagem(to_str(local))

# ======================= DIAS ÚTEIS DO MÊS =======================================
dias_uteis_mes = ObterDiasUteis(anoDeclarado, mesDeclarado)
dias_uteis_set = set([d.Date for d in dias_uteis_mes])

# ======================= FERIADOS MUNICIPAIS =====================================
mes_ano = "{}/{}".format(Formulario["MES_REFERENCIA"].Valor, Formulario["ANO_REF"].Valor)
Formulario.ExibeMensagem(to_str(mes_ano))
Formulario.ExibeMensagem(to_str(base_SV_formatada))

fer_tr = DB.ExecuteDataTable(
    "select * from tb_feriados_municipais fer "
    "where fer.CIDADE = '" + base_SV_formatada + 
    "' and TO_CHAR(fer.DT_FERIADO, 'MM/YYYY') = '" + to_str(mes_ano) + 
    "' and fer.SEMANA NOT IN ('sábado', 'domingo')"
)

lista_feriados = []
try:
    for d in fer_tr.Rows:
        try:
            lista_feriados.append(d["DT_FERIADO"].ToString("dd/MM/yyyy"))
        except:
            try:
                lista_feriados.append(to_str(d["DT_FERIADO"]))
            except:
                pass
except:
    pass

# Converte feriados do mês em set(Date) (apenas dias úteis já filtrados na query)
feriados_set = set()
for data in lista_feriados:
    dt = ParseDateSafe(data)
    if dt is not None:
        feriados_set.add(dt.Date)

# ======================= CÁLCULO FINAL (sem dupla subtração) =====================
# union = dias ausentes (úteis) ¿ feriados (úteis)
union_aus_fer = dias_ausentes_set | feriados_set
# Disponíveis = dias úteis do mês ¿ union
dias_trabalhaveis_reais_set = dias_uteis_set - union_aus_fer

# Estatísticas para LOG
total_uteis = len(dias_uteis_set)
qtd_ausentes_uteis = len(dias_ausentes_set)
qtd_feriados = len(feriados_set)
qtd_overlap = len(dias_ausentes_set & feriados_set)  # dias que são feriado e ausência (contam 1x)
total_finais = len(dias_trabalhaveis_reais_set)

# ======================= LOG ===============================================
# Bloco AUSÊNCIAS (lista completa do mês)
if len(lista_resumo_aus) > 0:
    Formulario['LOG_API'].Valor += "\n\n========== AUSENCIAS (MÊS) ==========\n\n"
    Formulario['LOG_API'].Valor += "Nome: {0}\nMatrícula: {1}\nTR Atual do Técnico: {2}\nUF Local do Técnico: {3}\n\n".format(nome, matricula, tr_local, uf)
    for i, a in enumerate(lista_resumo_aus, 1):
        Formulario['LOG_API'].Valor += (
            "{idx} | Tipo: {tipo} | Período (dentro do mês): {ini} a {fim} | Dias úteis neste período: {du} | "
            "DuracaoBruta: {db} | DiasDuracao: {dd} | HorasDuracao: {hd}\n"
        ).format(
            idx=i,
            tipo=a["tipo"],
            ini=a["inicio"].ToString("dd/MM/yyyy"),
            fim=a["fim"].ToString("dd/MM/yyyy"),
            du=a["dias_uteis_no_mes"],
            db=a["duracao_bruta"],
            dd=a["diasDuracao"],
            hd=a["hrsDuracao"]
        )
else:
    Formulario['LOG_API'].Valor += "\n\n========== AUSENCIAS (MÊS) ==========\n\n"
    Formulario['LOG_API'].Valor += "Nome: {0}\nMatrícula: {1}\nTR Atual do Técnico: {2}\n".format(nome, matricula, tr_local)
    Formulario['LOG_API'].Valor += "Sem ausências no mês/ano informado.\n"

# Bloco FERIADOS
if len(lista_feriados) > 0:
    Formulario['LOG_API'].Valor += '\nFeriados municipais ({0}): {1}\n'.format(len(lista_feriados), lista_feriados)
else:
    Formulario['LOG_API'].Valor += "\nNa cidade {0} não há feriados municipais no mês {1}.\n".format(to_str(base_SV_formatada), to_str(mesDeclarado))

# Bloco RESUMO FINAL
Formulario['LOG_API'].Valor += (
    "\n========== RESUMO (MÊS {mm}/{aa}) ==========\n"
    "Dias úteis do mês: {uteis}\n"
    "Dias de ausência (úteis): {aus}\n"
    "Feriados (úteis): {fer}\n"
    "Número de feriados no período de ausência/férias do funcionário: {ov}\n"
    "Dias úteis trabalhados (uteis - (aus ¿ fer)): {final}\n"
).format(
    mm=str(mesDeclarado).zfill(2),
    aa=anoDeclarado,
    uteis=total_uteis,
    aus=qtd_ausentes_uteis,
    fer=qtd_feriados,
    ov=qtd_overlap,
    final=total_finais
)

# ======================= SAÍDA FINAL ============================================
Formulario['DIAS_DE_TRA'].Valor = total_finais
Formulario['DIAS'].Valor = total_uteis
```
  - LOG_API "Controle LOG Douglas" [Memo String(2000) → CPE_DADOS.LOG_API] obrigatório
  - ID_PERSON "ID pessoa ERP" [TextBox String → CP_ORDEM_SERVICO.ID_PERSON] obrigatório
- ClientesAutorizados:
  - PapelProcessoId=67408; PapelAutorizado=Dires

### [362815] Tarefa "Cálculo indenização"
Responsável: Cliente (papel 18)
**ScriptInicio**
```python
diasTotais = Convert.ToInt32(OrdemServico.GetCustom("DIAS"))
diasTrab = Convert.ToInt32(OrdemServico.GetCustom("DIAS_DE_TRA"))
base = OrdemServico.GetCustom("COMBOBOX")
valorInicial = 0
valor = 0


# ====================================================================
mapa_bases = {
        "TR-BOM JESUS": 750.87,
        "TR-BOM JESUS DA LAPA": 750.87,
        "TR-IRECE": 750.87,
        "TR-MACAPA": 750.87,
        "TR-ORIXIMINA": 750.87,
        "TR-SANTAREM": 750.87,
        "TR-SEABRA": 750.87,
        "TR-TABATINGA": 750.87,
        "TR-TEFE": 750.87,
        "TR-OBIDOS": 750.87,
        "TR-VILHENA": 750.87,
        "TR-ARACUAI": 571.82,
        "TR-CRUZEIRO DO SUL": 750.87,
        "TR-GUANAMBI": 750.87,
        "TR-JI-PARANA": 658.46,
        "TR-PARINTINS": 750.87,
        "TR-PETROLINA": 750.87,
        "TR-RORAINÓPOLIS": 658.46,
        "TR-SALGUEIRO": 750.87,
        "TR-PINHEIRO": 462.07,
        "TR-ANGICOS": 658.46,
        "TR-CORUMBA": 658.46,
        "TR-CURRAIS NOVOS": 658.46,
        "TR-MOSSORO": 658.46,
        "TR-PATOS": 658.46,
        "TR-RIO BRANCO": 750.87,
        "TR-SERRINHA": 658.46,
        "TR-SOUSA": 658.46,
        "TR-TUCURUI": 658.46,
        "TR-PAULO AFONSO": 658.46,
        "TR-BAGE": 571.82,
        "TR-DOURADOS": 571.82,
        "TR-FOZ DO IGUACU": 571.82,
        "TR-JARDIM": 571.82,
        "TR-NOVA VENECIA": 571.82,
        "TR-SANTA ROSA": 571.82,
        "TR-SAO MIGUEL DO OESTE": 571.82,
        "TR-CACERES": 571.82,
        "TR-IGARAPE-MIRI": 571.82,
        "TR-COLATINA": 571.82,
        "TR-AGUA BOA": 462.07,
        "TR-ALAGOINHAS": 283.02,
        "TR-ALFENAS": 369.66,
        "TR-ALMENARA": 462.07,
        "TR-ALTA FLORESTA": 462.07,
        "TR-ALTAMIRA": 462.07,
        "TR-ARIQUEMES": 283.02,
        "TR-BACABAL": 462.07,
        "TR-BALSAS": 462.07,
        "TR-BARRA DO GARCAS": 462.07,
        "TR-BARREIRAS": 462.07,
        "TR-CACOAL": 369.66,
        "TR-CANTO DO BURITI": 462.07,
        "TR-CASCAVEL": 462.07,
        "TR-CHAPADINHA": 462.07,
        "TR-CHAPECO": 462.07,
        "TR-COLIDER": 462.07,
        "TR-CRATO": 462.07,
        "TR-EUNAPOLIS": 462.07,
        "TR-FLORIANO": 462.07,
        "TR-FRANCISCO BELTRAO": 369.66,
        "TR-GOVERNADOR VALADARES": 462.07,
        "TR-GUANHAES": 462.07,
        "TR-IMPERATRIZ": 462.07,
        "TR-JACOBINA": 462.07,
        "TR-JANAUBA": 462.07,
        "TR-JEQUIE": 462.07,
        "TR-JUAZEIRO DO NORTE": 462.07,
        "TR-JUINA": 462.07,
        "TR-MARABA": 462.07,
        "TR-MONTES CLAROS": 462.07,
        "TR-NOVA RUSSAS": 462.07,
        "TR-OEIRAS": 462.07,
        "TR-PARAGOMINAS": 462.07,
        "TR-PARAUAPEBAS": 462.07,
        "TR-PEIXOTO DE AZEVEDO": 462.07,
        "TR-PICOS": 462.07,
        "TR-PIRIPIRI": 462.07,
        "TR-POUSO ALEGRE": 462.07,
        "TR-PRESIDENTE DUTRA": 462.07,
        "TR-PRIMAVERA DO LESTE": 369.66,
        "TR-REALEZA": 462.07,
        "TR-REDENCAO": 462.07,
        "TR-RIBEIRA DO POMBAL": 462.07,
        "TR-ROSARIO": 462.07,
        "TR-SANTA INES": 462.07,
        "TR-SANTO ANTONIO DE JESUS": 462.07,
        "TR-SAO LOURENCO": 462.07,
        "TR-SINOP": 462.07,
        "TR-URUCUI": 462.07,
        "TR-VARGINHA": 462.07,
        "TR-VILA RICA": 462.07,
        "TR-VITORIA DA CONQUISTA": 462.07,
        "TR-XINGUARA": 462.07,
        "TR-POCOS DE CALDAS": 369.66,
        "TR-TEIXEIRA DE FREITAS": 462.07,
        "TR-TEOFILO OTONI": 462.07,
        "TR-ARACAJU": 369.66,
        "TR-ARAGUAINA": 369.66,
        "TR-ARCOVERDE": 369.66,
        "TR-BELA CRUZ": 369.66,
        "TR-CACHOEIRO DE ITAPEMIRIM": 369.66,
        "TR-CAMPINA GRANDE": 369.66,
        "TR-CAMPOS BELOS": 369.66,
        "TR-CAMPOS DOS GOYTACAZES": 369.66,
        "TR-CANOINHAS": 369.66,
        "TR-CARNAIBA": 369.66,
        "TR-CATAGUASES": 369.66,
        "TR-CAXIAS": 369.66,
        "TR-COXIM": 369.66,
        "TR-CURITIBANOS": 369.66,
        "TR-FEIRA DE SANTANA": 369.66,
        "TR-FERNANDOPOLIS": 369.66,
        "TR-GUARABIRA": 369.66,
        "TR-GUARACIABA DO NORTE": 369.66,
        "TR-GUARAPUAVA": 369.66,
        "TR-IGUATU": 369.66,
        "TR-IPATINGA": 369.66,
        "TR-ITABAIANA": 369.66,
        "TR-JOACABA": 369.66,
        "TR-JUIZ DE FORA": 369.66,
        "TR-LAGES": 369.66,
        "TR-LINHARES": 369.66,
        "TR-LUCAS DO RIO VERDE": 369.66,
        "TR-MANHUACU": 369.66,
        "TR-PARNAIBA": 369.66,
        "TR-PASSOS": 369.66,
        "TR-PELOTAS": 369.66,
        "TR-PORANGATU": 369.66,
        "TR-POSSE": 369.66,
        "TR-PRESIDENTE PRUDENTE": 369.66,
        "TR-QUIRINOPOLIS": 369.66,
        "TR-RIO DO SUL": 369.66,
        "TR-SANTA MARIA": 369.66,
        "TR-SAO JOSE DE UBA": 369.66,
        "TR-SOBRAL": 369.66,
        "TR-TANGARA DA SERRA": 369.66,
        "TR-TRES LAGOAS": 369.66,
        "TR-UMUARAMA": 369.66,
        "TR-UNIAO DA VITORIA": 369.66,
        "TR-VIDEIRA": 369.66,
        "TR-BARBACENA": 369.66,
        "TR-CASTANHAL": 369.66,
        "TR-DIVINOPOLIS": 369.66,
        "TR-OURO PRETO": 369.66,
        "TR-ANAPOLIS": 283.02,
        "TR-APUCARANA": 283.02,
        "TR-ARACATI": 283.02,
        "TR-ARACATUBA": 283.02,
        "TR-ARAPIRACA": 283.02,
        "TR-ARARANGUA": 283.02,
        "TR-ARARAQUARA": 283.02,
        "TR-ARARUAMA": 283.02,
        "TR-ASSIS": 283.02,
        "TR-ATIBAIA": 283.02,
        "TR-AVARE": 283.02,
        "TR-BARRETOS": 283.02,
        "TR-BATURITE": 283.02,
        "TR-BENTO GONCALVES": 283.02,
        "TR-BLUMENAU": 283.02,
        "TR-CABO FRIO": 283.02,
        "TR-CALDAS NOVAS": 283.02,
        "TR-CAMPO MOURAO": 283.02,
        "TR-CAPANEMA": 283.02,
        "TR-CARAGUATATUBA": 283.02,
        "TR-CARUARU": 283.02,
        "TR-CAXIAS DO SUL": 283.02,
        "TR-CENTENARIO DO SUL": 283.02,
        "TR-CERES": 283.02,
        "TR-CIANORTE": 283.02,
        "TR-CIDADE DE GOIAS": 283.02,
        "TR-CORNELIO PROCOPIO": 283.02,
        "TR-SAO RAIMUNDO NONATO": 750.87,
        "TR-CRICIUMA": 283.02,
        "TR-CRUZ ALTA": 283.02,
        "TR-ERECHIM": 283.02,
        "TR-FRANCA": 283.02,
        "TR-FREDERICO WESTPHALEN": 283.02,
        "TR-GARANHUNS": 283.02,
        "TR-GOIANA": 283.02,
        "TR-GRAVATA": 283.02,
        "TR-GUARAI": 283.02,
        "TR-GUARAPARI": 283.02,
        "TR-GUARATINGUETA": 283.02,
        "TR-GURUPI": 283.02,
        "TR-IPORA": 283.02,
        "TR-ITAJAI": 283.02,
        "TR-ITUMBIARA": 283.02,
        "TR-IVAIPORA": 283.02,
        "TR-JAU": 283.02,
        "TR-JOAO MONLEVADE": 283.02,
        "TR-JUNDIAI": 283.02,
        "TR-LAJEADO": 283.02,
        "TR-LIMOEIRO": 283.02,
        "TR-LIMOEIRO DO NORTE": 283.02,
        "TR-MACAE": 283.02,
        "TR-MARAGOGI": 283.02,
        "TR-MARICA": 283.02,
        "TR-MARILIA": 283.02,
        "TR-MARINGA": 283.02,
        "TR-MOCOCA": 283.02,
        "TR-MOGI DAS CRUZES": 283.02,
        "TR-MOGI-MIRIM": 283.02,
        "TR-NITEROI": 283.02,
        "TR-NOVA FRIBURGO": 283.02,
        "TR-ORLEANS": 283.02,
        "TR-PARAISO": 369.66,
        "TR-PARANAGUA": 283.02,
        "TR-PARANAVAI": 283.02,
        "TR-PATOS DE MINAS": 283.02,
        "TR-PETROPOLIS": 283.02,
        "TR-PIRACICABA": 283.02,
        "TR-PONTA GROSSA": 283.02,
        "TR-QUIXADA": 283.02,
        "TR-REGISTRO": 283.02,
        "TR-RIBEIRAO": 283.02,
        "TR-RIO CLARO": 283.02,
        "TR-RIO VERDE": 283.02,
        "TR-RONDONOPOLIS": 283.02,
        "TR-SANTA CRUZ DO SUL": 283.02,
        "TR-SANTANA DO IPANEMA": 283.02,
        "TR-SANTO ANDRE": 283.02,
        "TR-SANTO ANGELO": 283.02,
        "TR-SANTOS": 283.02,
        "TR-SAO CARLOS": 283.02,
        "TR-SAO JOSE DO RIO PRETO": 283.02,
        "TR-SAO JOSE DOS CAMPOS": 283.02,
        "TR-SERRA TALHADA": 369.66,
        "TR-SETE LAGOAS": 283.02,
        "TR-SOROCABA": 283.02,
        "TR-TORRES": 283.02,
        "TR-TUBARAO": 283.02,
        "TR-UBERABA": 283.02,
        "TR-UMIRIM": 283.02,
        "TR-UNAI": 283.02,
        "TR-VOLTA REDONDA": 283.02,
        "TR-ALEGRETE": 571.82,
        "TR-PAU DOS FERROS": 599.58,
        "TR-PONTES E LACERDA": 658.46,
        "TR-BOA VISTA": 750.87,
        "TR-CHAPADAO DO SUL": 462.07,
        "TR-DELMIRO GOUVEIA": 658.46,
        "TR-SAO MIGUEL DO GUAPORE": 658.46,
        "TR-ACARAU": 283.02,
        "TR-CAICO": 658.46,
        "TR-ITAPETINGA": 462.07,
        "TR-ITAPIPOCA": 283.02,
        "TR-TIANGUA": 369.66,
        "TR-UIRAUNA": 658.46, 
        "TR-VITORIA DE SANTO ANTAO": 283.02,
        "TR-ITACOATIARA": 658.46,
        "TR-ILHEUS": 369.66,
        "TR-SANTO ANTONIO DA PLATINA": 283.02
}

#Aqui eu verifico se a base está no dicionário e realizo o cálculo
if base in mapa_bases:
    valorInicial = (mapa_bases[base] / diasTotais)
    valor = (valorInicial * diasTrab)
    valor = round(valor, 2)
    OrdemServico.SetCustom("VALOR_PRESTACAO", valor)

else:
    OrdemServico.AdicionaComentario("=== ERRO!! === \nBase não encontrada, contate um solucionador", False)
    OrdemServico.SetCustom("VALOR_PRESTACAO", valor)

OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
Formulario['DIAS'].Visivel = True
```
- Operação PR0001 Preencher Campos
  - COMBOBOX "Base destacada" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
  - TIPO_BASE "Tipo de Base" [DropDownList String → CPE_ASSTECNICA.TIPO_BASE]
  - CATEGORIA_IDENIZACAO "Categoria" [DropDownList String → CPE_ASSTECNICA.CATEGORIA_IDENIZACAO]
  - DIAS_DE_TRA "Dias trabalhados" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
  - DIAS "Quantidade de dias úteis no mês da cidade de lotação do técnico Base TR, exceto sábados, domingos e feriados" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] obrigatório
**DIAS.ScriptModificado**
```python
#Formulario["VALOR"].Visivel = True
#Formulario["VALOR"].Habilitado = False
#
#diasTotais = Convert.ToDecimal(Formulario["DIAS"].Valor)
#diasTrab = Convert.ToDecimal(Formulario["DIAS_DE_TRA"].Valor)
#valorInicial = 0
#valor = 0
#
#
#
#
#
#if Formulario["COMBOBOX"].Valor == "TR-BOM JESUS":
#
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-BOM JESUS DA LAPA":
#
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-IRECE":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-MACAPA":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-ORIXIMINA":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTAREM":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-SEABRA":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-TABATINGA":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-TEFE":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-VILHENA":
#    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
##Tipo de base Especial, categoria B e valor 570,00
#    
#if Formulario["COMBOBOX"].Valor == "TR-ANGICOS":
#    
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#
#if Formulario["COMBOBOX"].Valor == "TR-CORUMBA":
#        
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CURRAIS NOVOS":
#        
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-MOSSORO":
#        
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PARINTINS":
#        
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-PATOS":
#        
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PAU DOS FERROS":
#        
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-RORAINÓPOLIS":
#        
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-SERRINHA":
#        
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-SOUSA":
#        
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#    
###Tipo de base Especial, categoria C e valor 495,00
#
#if Formulario["COMBOBOX"].Valor == "TR-BAGE":
#        
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#
#
#if Formulario["COMBOBOX"].Valor == "TR-DOURADOS":
#            
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#
#if Formulario["COMBOBOX"].Valor == "TR-FOZ DO IGUACU":
#            
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#
#if Formulario["COMBOBOX"].Valor == "TR-JARDIM":
#            
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#
#if Formulario["COMBOBOX"].Valor == "TR-NOVA VENECIA":
#            
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTA ROSA":
#            
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#
#if Formulario["COMBOBOX"].Valor == "TR-SAO MIGUEL DO OESTE":
#            
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#    
##Tipo de base Comum, categoria A e valor 400,00
#    
#if Formulario["COMBOBOX"].Valor == "TR-AGUA BOA":
#            
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-ALAGOINHAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-ALFENAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-ALMENARA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-ALTA FLORESTA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-ALTAMIRA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-ARACUAI":
#                
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-ARIQUEMES":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-BACABAL":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-BALSAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-BARRA DO GARCAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-BARREIRAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-BOA VISTA":
#                
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#    
#if Formulario["COMBOBOX"].Valor == "TR-CACOAL":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-CANTO DO BURITI":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-CASCAVEL":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-CHAPADINHA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-CHAPECO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-COLIDER":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-CRATO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-CRUZEIRO DO SUL":
#                
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-EUNAPOLIS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-FLORIANO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-GUANAMBI":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-IMPERATRIZ":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-ITABUNA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-JACOBINA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-JANAUBA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-JEQUIE":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-JI-PARANA":
#                
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-JUAZEIRO DO NORTE":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-JUINA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-MARABA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-MONTES CLAROS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-NOVA RUSSAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-OEIRAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-PARAUAPEBAS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-PEIXOTO DE AZEVEDO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-PICOS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-PIRIPIRI":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-POUSO ALEGRE":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-PRESIDENTE DUTRA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-PRIMAVERA DO LESTE":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-REALEZA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-REDENCAO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-RIBEIRA DO POMBAL":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-RIO BRANCO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-ROSARIO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-SALGUEIRO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTA INES":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-SANTO ANTONIO DE JESUS":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
#if Formulario["COMBOBOX"].Valor == "TR-SAO LOURENCO":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-SINOP":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-URUCUI":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-VARGINHA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-VILA RICA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-VITORIA DA CONQUISTA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-XINGUARA":
#                
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#    
##Tipo de base Comum, categoria B e valor 320,00    
#    
#    
#if Formulario["COMBOBOX"].Valor == "TR-ALEGRETE":
#                
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-ARACAJU":
#                
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-ARAGUAINA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-ARCOVERDE":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-BELA CRUZ":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CACHOEIRO DE ITAPEMIRIM":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CAMPINA GRANDE":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CAMPOS BELOS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CAMPOS DOS GOYTACAZES":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CANOINHAS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CARNAIBA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CATAGUASES":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CHAPADAO DO SUL":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-COLATINA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-COXIM":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-CURITIBANOS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-FEIRA DE SANTANA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-FERNANDOPOLIS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-FRANCISCO BELTRAO":
#                    
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-GOVERNADOR VALADARES":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-GUANHAES":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-GUARABIRA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-GUARACIABA DO NORTE":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-GUARAPUAVA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-IGUATU":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-IPATINGA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-ITABAIANA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-JOACABA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-JUIZ DE FORA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-LAGES":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-LINHARES":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-LUCAS DO RIO VERDE":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-MANHUACU":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PARAGOMINAS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PARNAIBA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PASSOS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PAULO AFONSO":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PELOTAS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PINHEIRO":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-POCOS DE CALDAS":
#                    
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-PONTES E LACERDA":
#                    
#    valorInicial = (650.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-PORANGATU":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-POSSE":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-PRESIDENTE PRUDENTE":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-QUIRINOPOLIS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-RIO DO SUL":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTA MARIA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-SAO JOSE DE UBA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-SOBRAL":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-TANGARA DA SERRA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-TEIXEIRA DE FREITAS":
#                    
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A"
#
#if Formulario["COMBOBOX"].Valor == "TR-TEOFILO OTONI":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-TRES LAGOAS":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-TUCURUI":
#                    
#    valorInicial = (570.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-UMUARAMA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-UNIAO DA VITORIA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#
#if Formulario["COMBOBOX"].Valor == "TR-VIDEIRA":
#                    
#    valorInicial = (320.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2) 
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "B"
#    
##Tipo de base Comum, categoria C e valor 245,00     
#
#if Formulario["COMBOBOX"].Valor == "TR-ANAPOLIS":
#                    
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"    
#
#if Formulario["COMBOBOX"].Valor == "TR-APUCARANA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#
#if Formulario["COMBOBOX"].Valor == "TR-ARACATI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#    
#if Formulario["COMBOBOX"].Valor == "TR-ARACATUBA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#    
#if Formulario["COMBOBOX"].Valor == "TR-ARAPIRACA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#
#if Formulario["COMBOBOX"].Valor == "TR-ARARANGUA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#    
#if Formulario["COMBOBOX"].Valor == "TR-ARARAQUARA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#
#if Formulario["COMBOBOX"].Valor == "TR-ARARUAMA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#
#if Formulario["COMBOBOX"].Valor == "TR-ASSIS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#
#if Formulario["COMBOBOX"].Valor == "TR-ATIBAIA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#
#if Formulario["COMBOBOX"].Valor == "TR-AVARE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"  
#
#if Formulario["COMBOBOX"].Valor == "TR-BARBACENA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-BARRETOS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-BATURITE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-BENTO GONCALVES":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-BLUMENAU":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CABO FRIO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CACERES":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CALDAS NOVAS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CAMPO MOURAO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CAPANEMA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CARAGUATATUBA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CARUARU":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CASTANHAL":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CAXIAS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CAXIAS DO SUL":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CENTENARIO DO SUL":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CERES":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CIANORTE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CIDADE DE GOIAS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-CORNELIO PROCOPIO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-CRICIUMA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-CRUZ ALTA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#    
#if Formulario["COMBOBOX"].Valor == "TR-DIVINOPOLIS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-ERECHIM":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-FRANCA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-FREDERICO WESTPHALEN":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-GARANHUNS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-GOIANA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-GRAVATA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-GUARAI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-GUARAPARI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-GUARATINGUETA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-GURUPI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-IBAITI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-IGARAPE-MIRI":
#                        
#    valorInicial = (495.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "ESPECIAL"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-IPORA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-ITAJAI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)   
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-ITUMBIARA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-IVAIPORA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-JAU":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-JOAO MONLEVADE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-JUNDIAI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-LAJEADO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-LIMOEIRO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#    
#if Formulario["COMBOBOX"].Valor == "TR-LIMOEIRO DO NORTE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-MACAE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-MARICA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-MARILIA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-MARINGA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-MOCOCA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-MOGI DAS CRUZES":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-MOGI-MIRIM":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-NITEROI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-NOVA FRIBURGO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-ORLEANS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-OURO PRETO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PARAÍSO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PARANAGUA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PARANAVAI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PATOS DE MINAS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PETROLINA":
#                        
#    valorInicial = (400.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "A" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PETROPOLIS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PIRACICABA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-PONTA GROSSA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-QUIXADA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-REGISTRO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-RIBEIRAO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-RIO CLARO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-RIO VERDE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-RONDONOPOLIS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTA CRUZ DO SUL":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTANA DO IPANEMA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-SANTO ANDRE":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTO ANGELO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SANTOS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-SAO CARLOS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SAO JOSE DO RIO PRETO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SAO JOSE DOS CAMPOS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SERRA TALHADA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SETE LAGOAS":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-SOROCABA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-TORRES":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-TUBARAO":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-UBERABA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#    
#if Formulario["COMBOBOX"].Valor == "TR-UMIRIM":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-UNAI":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C" 
#
#if Formulario["COMBOBOX"].Valor == "TR-VOLTA REDONDA":
#                        
#    valorInicial = (245.00 / diasTotais)
#    valor = (valorInicial * diasTrab)   
#    Formulario["VALOR"].Valor = round(valor,2)    
#    Formulario["TIPO_BASE"].Valor = "COMUM"    
#    Formulario["CATEGORIA_IDENIZACAO"].Valor = "C"
#    
#
```
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - VALOR_PRESTACAO "Valor da prestação" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_PRESTACAO]

### [362816] EventoIntermediarioMensagem "Aprovação Indenização por lotação em base destacada"
Destinatário: Cliente (papel 18)
Config: FinalizarInterrupcao=true
ModeloComunicado: Aprovação Indenização por lotação em base destacada
Corpo do comunicado: Informamos que foi aberta a solicitação nº OrdemServico.Numero - Indenização por Lotação em Base Destacada, referente ao mês 
 OrdemServico.Customizado.MES_REFERENCIA / OrdemServico.Customizado.ANO_REF, conforme previsto na NI 1346.
O valor a ser creditado em sua conta será de R$ OrdemServico.Customizado.VALOR_PRESTACAO . 
Caso identifique alguma inconsistência, gentileza acionar o e-mail dires@bbts.com.br.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [362817] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [362818] EventoFinal ""
Responsável: Cliente (papel 18)
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec
**ScriptFormCarregado**
```python
Formulario["VALOR_PRESTACAO"].Visivel = True
```
- Operação PR0001 Preencher Campos
  - VALOR_PRESTACAO "Valor proporcional" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_PRESTACAO] obrigatório

### [362819] Tarefa "Enviar para o ERP"
Responsável: Cliente (papel 18)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
sql="select name from sv_domain where enabled = 'Sim'"
dom = DB.ExecuteScalar(sql)
if dom == 'HOMOLOGAÇÃO':
    DB.ExecuteNonQuery("ALTER SESSION SET NLS_NUMERIC_CHARACTERS = '.,'")

nota = 'RIVL'
fornecedor = '001.110001.3000001000.219399.000000.000.00000'
idFavorecido = Convert.ToInt32(OrdemServico.GetCustom('ID_PERSON'))
favorecido = Pessoa.Carrega(idFavorecido)

valorRetorno = OrdemServico["VALOR_PRESTACAO"].ToString()
#uor = OrdemServico["TE_UOR"].ToString()
#uor = uor.split(' - ')[0]
matricula = OrdemServico["TE_MATRICULA"].ToString()

uor= DB.ExecuteScalar("select substr(organizacao,1,10) as uor from cad_funcionario_v where matricula='"+matricula.ToString()+"'")

OrdemServico.AdicionaComentario("fornecedor "+fornecedor.ToString(), False)

nomeFavorecido = favorecido.Nome
orgao = Orgao.Carrega(favorecido.OrgaoId)
sigla = orgao.Sigla

termo = '00 DDL'
rubrica = '90303'
numero = OrdemServico.Numero.ToString()

qry = "SELECT MAX(INICIO_DATA_FUNCAO), EMPRESA, SUBSTR('"+sigla.ToString()+"', 1, 1) AS PREFIXO  FROM CAD_FUNCIONARIO_V WHERE DATA_DE_DEMISSAO IS NULL AND MATRICULA = '" + matricula.ToString() + "' GROUP BY EMPRESA"

lista = Utils.ExecuteDataTable(qry)
if (lista != None):
    for linha in lista.Rows:
        if (DBNull.Value.Equals(linha["EMPRESA"]) != True ):
            filial = linha["EMPRESA"].ToString()
        if (DBNull.Value.Equals(linha["PREFIXO"]) != True ):
            inicio = linha["PREFIXO"].ToString()
    
#-- AJUSTANDO O PREFIXO EM CASOS DE ABERTURAS POR ÁREAS ESTRATÉGICAS
if inicio == '1' or inicio == '2':
    prefixo = '337'
else:
    prefixo = '343'
       

conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"

#Formatação do valor 
#OrdemServico.AdicionaComentario('Conta contábil de débito no GL: '+ conta, False)
valor = DB.ExecuteScalar("select replace('"+ OrdemServico.GetCustom("VALOR_PRESTACAO").ToString() + "',',','.') as valor from dual")
valor = DB.ExecuteScalar("select TO_char("+ valor.ToString() + ", '9999D99') as valor from dual")
valor = DB.ExecuteScalar("select replace('"+ valor.ToString() + "',',','.') as valor from dual")


#Validação de lançamentos anteriores, evitando duplicação de abertura
contInterfaceAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from XXBBTSGATE.VW_BBTS_AP_INVOICES_INTERFACE where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
    
contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

contAP = DB.ExecuteScalar("select COUNT(1) as CONTINSERIDAS from AP_INVOICES_ALL where source LIKE '%SUPRAVIZIO%' AND invoice_num = '"+nota+""+OrdemServico.Numero.ToString() + "'")
    
contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")
OrdemServico.AdicionaComentario(contInterfaceAP.ToString()+"WW"+contInterfaceGL.ToString()+"WWW"+contAP.ToString()+"WWWW"+contGL.ToString(), False)

#----- insert no GL PÀRA CONTABILIZAÇÃO (CONTABIL)

#--- débito
if contInterfaceGL.ToString()=='0' and contGL.ToString()=='0':
    OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Base Destacada', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Base Destacada', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")
    
#--- crédito
    OrdemServico.AdicionaComentario("Procedure para crédito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Base Destacada', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Base Destacada', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")

#----- insert no AP (PARA PAGAMENTO)
#verifica se houve os lançamentos anteriores no GL e não consta no AP
contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0' and (contInterfaceGL.ToString()>= '2' or contGL.ToString()>= '2'):
    OrdemServico.AdicionaComentario("Procedure para inserir no AP:  call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"', '"+ fornecedor +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"', '"+ fornecedor +"') ")


OrdemServico.Salva()
#OrdemServico.AdicionaComentario(OrdemServico.Servico.Sigla.ToString(), False)
AvancaProximaAtividade = True
```

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Campos customizados usados (definição global)

### TE_NOME_EMPREGADO — Nome do empregado
DropDownList String → CPE_CSC.TE_NOME_EMPREGADO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

### TIPO_BASE — Tipo de Base
DropDownList String → CPE_ASSTECNICA.TIPO_BASE
Itens: COMUM;ESPECIAL

### CATEGORIA_IDENIZACAO — Categoria
DropDownList String → CPE_ASSTECNICA.CATEGORIA_IDENIZACAO
Itens: A;B;C

### MES_REFERENCIA — Mês referência
DropDownList String(2) → CPE_CSC.MES_REFERENCIA
Itens: 01;02;03;04;05;06;07;08;09;10;11;12

### ANO_REF — Ano referência
DropDownList String(4) → CPE_CSC.ANO_REF
Itens: 2027;2026;2025

### DIAS_DE_TRA — DIAS DE TRAB
TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA
Descrição: DIAS DE TRABALHO

### DIAS — Dias
TextBox Integer → CPE_HOMOLOGACAO.DIAS

### LOG_API — LOG API
Memo String(2000) → CPE_DADOS.LOG_API

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### ID_PERSON — ID pessoa ERP
TextBox String → CP_ORDEM_SERVICO.ID_PERSON

### LABEL_GRANDE — Label Grande
Label String(2000) → CPE_MOVIMENTACAO_PESSOA.LABEL_GRANDE

### CHECKBOX1 — Checkbox1
CheckBox Boolean → CPE_PESSOAS.CHECKBOX1

### VALOR_PRESTACAO — Valor da prestação
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_PRESTACAO

## Biblioteca de scripts referenciada
peopleSoft, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
