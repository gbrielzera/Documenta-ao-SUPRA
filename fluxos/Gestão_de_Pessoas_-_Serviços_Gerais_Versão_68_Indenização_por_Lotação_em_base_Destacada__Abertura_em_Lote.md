# Fluxo: Indenização por Lotação em base Destacada (Abertura em Lote) (BASEDESTACADALOTE) — versão 68
Caminho: Fluxos > Gestão de Pessoas - Serviços Gerais Versão 68 Indenização por Lotação em base Destacada (Abertura em Lote)
XML: `XMLs para teste/Gestão_de_Pessoas_-_Serviços_Gerais_Versão_68_Indenização_por_Lotação_em_base_Destacada_(Abertura_em_Lote).xml` | Supravizio 19.1.1 | SubProcessoId 21133 | DesenhoProcessoId 2889 | ProcessoId 113
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: CARLOS ALBERTO REZENDE SOUZA NETO
Classe do subprocesso: Objetivo=Indenização por Lotação em base Destacada (Abertura em Lote); DescricaoCliente=Indenização por Lotação em base Destacada (Abertura em Lote); CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Orgao; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Indenização por lotação em base destacada (IDENIZACAO)

## Grafo do fluxo
- [362820] EventoFinal "" → (fim)
- [362821] EventoInicial "Indenização por Lotação em Base Destacada" {Cliente} → [362822] 
- [362822] SubProcesso "" {Responsável atual} → [362823] Avaliar os Subchamados e avançar para finalização
- [362823] Tarefa "Avaliar os Subchamados e avançar para finalização" {Cliente} → [362820] 

## Atividades

### [362820] EventoFinal ""
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [362821] EventoInicial "Indenização por Lotação em Base Destacada"
Responsável: Cliente (papel 18)
TipoSolicitacao: 25.01. Gestão de Pessoas - Serviços Gerais
**ScriptValidacao**
```python
grid = OrdemServico.GetCustom('BASE_DESTACADA_LOTE')
matricula = ''

for i in grid.Rows:
    matricula = i['MATRICULA'].ToString()
    query = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, PESSOA.NOME From CP_PESSOA Inner Join PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA = '"+ matricula +"' AND PESSOA.ATIVO = 'Sim'")
    
    if query.Rows.Count == 0 or query.Rows.Count == None:
        Criticas.AdicionaPendencia("ATENCÃO!\nA MATRICULA {} NÃO É VALIDA. POR FAVOR, REVISE.".format(matricula.ToString()))
        
        
    if "Inativo" in i['FUNCIONARIO'].ToString():
        Criticas.AdicionaPendencia("Existem funcionários Inativos na planilha que você anexou. Por favor, revise no Peoplesoft a situação desse funcionário e se a matrícula do mesmo está correta.\nSe necessário, abra um chamado avulsa para esse funcionário.")
        
    
    mesAtual = Convert.ToInt32(DateTime.Now.ToString("MM"))
    mesDeclarado = Convert.ToInt32(i["MES_REFERENCIA"])

    anoAtual = Convert.ToInt32(DateTime.Now.ToString("yyyy"))
    anoDeclarado = Convert.ToInt32(i["ANO_REFERENCIA"])

    today = DateTime.Now;
    prevDate = DateTime(anoDeclarado, mesDeclarado, 01)

    if anoDeclarado == anoAtual and mesDeclarado > mesAtual or anoDeclarado > anoAtual and mesDeclarado > mesAtual or anoDeclarado == anoAtual and mesDeclarado == mesAtual:
        Criticas.AdicionaPendencia("Não é permitido lançamentos futuros ou para o mês atual. Verifique sua solicitação e tente novamente.")
        
    elif anoDeclarado > anoAtual:
        Criticas.AdicionaPendencia("Não é permitido lançamentos futuros ou para o mês atual. Verifique sua solicitação e tente novamente.")

    diffOfDates = ((today.Year - prevDate.Year) * 12) + today.Month - prevDate.Month

    if diffOfDates >= 4:
        Criticas.AdicionaPendencia("A abertura retroativa está limitada a até 3 meses a partir do mês atual.")
      
    queryBaseDestacada = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, PESSOA.ID_PESSOA, OCORRENCIA.ID_CLIENTE, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME, CPE_CSC.MES_REFERENCIA, CPE_CSC.ANO_REF From OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = OCORRENCIA.ID_CLIENTE Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Where PESSOA.ID_PESSOA = '"+OrdemServico["TE_NOME_EMPREGADO"]+"' And OCORRENCIA.ASSUNTO = 'Indenização por Lotação em Base Destacada' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' or OCORRENCIA.SITUACAO = 'Aberto') And (CPE_CSC.MES_REFERENCIA = '"+OrdemServico["MES_REFERENCIA"]+"' And CPE_CSC.ANO_REF = '"+OrdemServico["ANO_REF"]+"') and OCORRENCIA.ID_OCORRENCIA != "+str(OrdemServico.Id))

    if queryBaseDestacada.Rows.Count != 0:
        osNum = queryBaseDestacada.Rows[0]["NUMERO"]
        Criticas.AdicionaPendencia("Já existe a seguinte ordem de serviço para o mês e/ou ano referente: " + str(osNum))
```
**ScriptFormCarregado**
```python
Formulario['LABEL1'].Valor = '<div style="display: flex; justify-content: center; align-items: center;"><div style="display: flex; align-items: center; width: 100%; background: linear-gradient(90deg, blue, rgb(2, 0, 18)); border-radius: 16px; padding: 2%;"><img src="https://intranet.bbts.com.br/templates/intranet/images/LogoTemplate-Agosto2025.gif" alt="Ícone" style="height: 40px; margin-right: 16px;"><br><p style="flex: 1; text-align: center; color: yellow; font-weight: 600; font-size: 16px; font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif; margin: 0;">A solicitação da Indenização por Lotação em Base Destacada deve ser proporcional aos dias úteis trabalhados, conforme preenchimento neste chamado.<br>O ressarcimento é devido aos empregados que residam em um dos municípios de atendimento da base destacada. <br>As solicitações abertas para meses futuros serão desconsideradas. <br>Caso haja mais de uma solicitação para o mesmo mês, somente será considerada a última solicitação aprovada pelo Gestor do empregado. <br>A indenização não se aplica à técnicos temporários, terceiros ou empregados lotados na base CAT deslocados para apoio temporário à base destacada. <br><br>LINK PARA DOWNLOAD DA PLANILHA MODELO: <a href="https://bbtecno.sharepoint.com/:x:/t/TimeDirat/IQCF4kBeZPzgQaz1rhrbqethAYudPLNAkxiKx6cCAW913Rg?download=1">CLIQUE AQUI!</a></p></div></div><br><br>'
# ===============================================================================

#Formulario['LABEL34'].Valor = '<b style="background-color: blue; color: yellow; font-size: 24px; padding: 2%; border-radius: 16px; margin: 5px;">Clique <a href="https://bbtecno-my.sharepoint.com/:x:/g/personal/ext-douglas_moura_bbts_com_br/ESOCYO7_1G9KkRi6egW3mHUBHFqTzdL8qP1TP4KG6lVurQ?download=1" style="text-decoration: none; color: greenyellow; font-size: 24px;"> AQUI </a> para baixar a planilha modelo desse fluxo </b>'


elementos = ['ANO_REF', 'CATEGORIA_IDENIZACAO', 'COMBOBOX', 'DIAS', 'DIAS_DE_TRA', 'LOG_API', 'MES_REFERENCIA', 'TE_CARGO', 'TE_FUNCAO', 'TE_MATRICULA', 'TE_NOME_EMPREGADO', 'TE_UOR', 'TIPO_BASE', 'VALOR']

for i in elementos:
    Formulario[i].Visivel = False
    Formulario[i].Habilitado = False

OrdemServico.Assunto = OrdemServico.Servico.DescricaoCliente

Formulario["COMBOBOX"].Itens = "TR-AGUA BOA;TR-ALAGOINHAS;TR-ALFENAS;TR-ALMENARA;TR-ALTA FLORESTA;TR-ALTAMIRA;TR-ARIQUEMES;TR-BACABAL;TR-BALSAS;TR-BARRA DO GARCAS;TR-BARREIRAS;TR-BOA VISTA;TR-CACOAL;TR-CANTO DO BURITI;TR-CASCAVEL;TR-CHAPADAO DO SUL;TR-CHAPADINHA;TR-CHAPECO;TR-COLIDER;TR-CRATO;TR-EUNAPOLIS;TR-FLORIANO;TR-FRANCISCO BELTRAO;TR-GOVERNADOR VALADARES;TR-GUANHAES;TR-IMPERATRIZ;TR-JACOBINA;TR-JANAUBA;TR-JEQUIE;TR-JUAZEIRO DO NORTE;TR-JUINA;TR-MARABA;TR-MONTES CLAROS;TR-NOVA RUSSAS;TR-OEIRAS;TR-PARAGOMINAS;TR-PARAUAPEBAS;TR-PEIXOTO DE AZEVEDO;TR-PICOS;TR-PIRIPIRI;TR-POCOS DE CALDAS;TR-POUSO ALEGRE;TR-PRESIDENTE DUTRA;TR-PRIMAVERA DO LESTE;TR-REALEZA;TR-REDENCAO;TR-RIBEIRA DO POMBAL;TR-ROSARIO;TR-SANTA INES;TR-SANTO ANTONIO DE JESUS;TR-SAO LOURENCO;TR-SINOP;TR-TEIXEIRA DE FREITAS;TR-TEOFILO OTONI;TR-URUCUI;TR-VARGINHA;TR-VILA RICA;TR-VITORIA DA CONQUISTA;TR-XINGUARA;TR-ARACAJU;TR-ARAGUAINA;TR-ARCOVERDE;TR-BARBACENA;TR-BELA CRUZ;TR-CACHOEIRO DE ITAPEMIRIM;TR-CAMPINA GRANDE;TR-CAMPOS BELOS;TR-CAMPOS DOS GOYTACAZES;TR-CANOINHAS;TR-CARNAIBA;TR-CASTANHAL;TR-CATAGUASES;TR-CAXIAS;TR-COXIM;TR-CURITIBANOS;TR-DIVINOPOLIS;TR-FEIRA DE SANTANA;TR-FERNANDOPOLIS;TR-GUARABIRA;TR-GUARACIABA DO NORTE;TR-GUARAPUAVA;TR-IGUATU;TR-IPATINGA;TR-ITABAIANA;TR-JOACABA;TR-JUIZ DE FORA;TR-LAGES;TR-LINHARES;TR-LUCAS DO RIO VERDE;TR-MANHUACU;TR-OURO PRETO;TR-PARNAIBA;TR-PASSOS;TR-PELOTAS;TR-PORANGATU;TR-POSSE;TR-PRESIDENTE PRUDENTE;TR-QUIRINOPOLIS;TR-RIO DO SUL;TR-SANTA MARIA;TR-SAO JOSE DE UBA;TR-SOBRAL;TR-TANGARA DA SERRA;TR-TRES LAGOAS;TR-UMUARAMA;TR-UNIAO DA VITORIA;TR-VIDEIRA;TR-ANAPOLIS;TR-APUCARANA;TR-ARACATI;TR-ARACATUBA;TR-ARAPIRACA;TR-ARARANGUA;TR-ARARAQUARA;TR-ARARUAMA;TR-ASSIS;TR-ATIBAIA;TR-AVARE;TR-BARRETOS;TR-BATURITE;TR-BENTO GONCALVES;TR-BLUMENAU;TR-CABO FRIO;TR-CALDAS NOVAS;TR-CAMPO MOURAO;TR-CAPANEMA;TR-CARAGUATATUBA;TR-CARUARU;TR-CAXIAS DO SUL;TR-CENTENARIO DO SUL;TR-CERES;TR-CIANORTE;TR-CIDADE DE GOIAS;TR-CORNELIO PROCOPIO;TR-CRICIUMA;TR-CRUZ ALTA;TR-ERECHIM;TR-FRANCA;TR-FREDERICO WESTPHALEN;TR-GARANHUNS;TR-GOIANA;TR-GRAVATA;TR-GUARAI;TR-GUARAPARI;TR-GUARATINGUETA;TR-GURUPI;TR-IPORA;TR-ITAJAI;TR-ITUMBIARA;TR-IVAIPORA;TR-JAU;TR-JOAO MONLEVADE;TR-JUNDIAI;TR-LAJEADO;TR-LIMOEIRO;TR-LIMOEIRO DO NORTE;TR-MACAE;TR-MARICA;TR-MARILIA;TR-MARINGA;TR-MOCOCA;TR-MOGI DAS CRUZES;TR-MOGI-MIRIM;TR-NITEROI;TR-NOVA FRIBURGO;TR-ORLEANS;TR-PARAÍSO;TR-PARANAGUA;TR-PARANAVAI;TR-PATOS DE MINAS;TR-PETROPOLIS;TR-PIRACICABA;TR-PONTA GROSSA;TR-QUIXADA;TR-REGISTRO;TR-RIBEIRAO;TR-RIO CLARO;TR-RIO VERDE;TR-RONDONOPOLIS;TR-SANTA CRUZ DO SUL;TR-SANTANA DO IPANEMA;TR-SANTO ANDRE;TR-SANTO ANGELO;TR-SANTOS;TR-SAO CARLOS;TR-SAO JOSE DO RIO PRETO;TR-SAO JOSE DOS CAMPOS;TR-SERRA TALHADA;TR-SETE LAGOAS;TR-SOROCABA;TR-TORRES;TR-TUBARAO;TR-UBERABA;TR-UMIRIM;TR-UNAI;TR-VOLTA REDONDA;TR-ALEGRETE;TR-ARACUAI;TR-BOA VISTA;TR-BOM JESUS;TR-BOM JESUS DA LAPA;TR-CRUZEIRO DO SUL;TR-GUANAMBI;TR-IRECE;TR-JI-PARANA;TR-MACAPA;TR-OBIDOS;TR-PARINTINS;TR-PETROLINA;TR-PINHEIRO;TR-RORAINÓPOLIS;TR-SALGUEIRO;TR-SANTAREM;TR-SEABRA;TR-TABATINGA;TR-TEFE;TR-VILHENA;TR-ANGICOS;TR-CORUMBA;TR-CURRAIS NOVOS;TR-MOSSORO;TR-PATOS;TR-PAULO AFONSO;TR-RIO BRANCO;TR-SERRINHA;TR-SOUSA;TR-TUCURUI;TR-BAGE;TR-CACERES;TR-COLATINA;TR-DOURADOS;TR-FOZ DO IGUACU;TR-IGARAPE-MIRI;TR-JARDIM;TR-NOVA VENECIA;TR-SANTA ROSA;TR-SAO MIGUEL DO OESTE;TR-MARAGOGI;TR-ITACOATIARA;TR-ILHEUS;TR-SANTO ANTONIO DA PLATINA"
```
- Operação PR0004 Associar Itens Configuração
  - anexo "Planilha da Base Destacada Preenchida" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=GRID
  - LABEL1 "Texto Informativo" [Label String(2000) → CP_ORDEM_SERVICO.LABEL1]
  - BASE_DESTACADA_LOTE "Base Destacada Lote" [DataGrid RecordList → Z_00143_BASE_DESTACADA_LOTE.BASE_DESTACADA_LOTE] obrigatório
    - coluna BASE obrigatório
    - coluna MES_REFERENCIA obrigatório
    - coluna ANO_REFERENCIA obrigatório
    - coluna ID_FUNCIONARIO obrigatório
**BASE_DESTACADA_LOTE.ID_FUNCIONARIO.ScriptModificado**
```python
mat = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA From PESSOA Inner Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA WHERE PESSOA.ID_PESSOA = '"+ FormularioRegistro['ID_FUNCIONARIO'].Valor.ToString() +"'")
```
    - coluna MATRICULA obrigatório
    - coluna FUNCIONARIO obrigatório
    - coluna TIPO_BASE obrigatório
    - coluna CLASSIFICACAO obrigatório
    - coluna UF obrigatório
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
 "TR-ACARAÚ": ("283,02", "COMUM", "C"),
 "TR-CAICÓ": ("658,46", "ESPECIAL", "B"),
 "TR-ITAPETINGA": ("462,07", "COMUM", "A"),
 "TR-ITAPIPOCA": ("283,02", "COMUM", "C"),
 "TR-TIANGUÁ": ("369,66", "COMUM", "B"),
 "TR-UIRAÚNA": ("658,46", "ESPECIAL", "B"),
 "TR-VITÓRIA DE SANTO ANTÃO": ("283,02", "COMUM", "C")
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
  - CHECKBOX2 "Clique aqui para carregar os dados da Planillha" [CheckBox Boolean → CPE_PESSOAS.CHECKBOX2] obrigatório
**CHECKBOX2.ScriptModificado**
```python
if Controle.Valor == True:
    if OrdemServico.PossuiItem("ARQUIVO"):

        import clr
        import System
        clr.AddReference("System.Data")
        from System.Data import DataSet
        from System.Data.OleDb import OleDbConnection, OleDbDataAdapter
        from System import String, DBNull

        def readExcel(nomesCampos, nomeGrid):

            repositorio = Utils.ExecuteScalar("select FILES_PATH from SERVICES_PARAM")
            anexo = OrdemServico.ObtemItem("ARQUIVO")
            _Arquivo = repositorio + "\\" + anexo.Localizacao

            _StringConexao = String.Format(
                "Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties='Excel 12.0 Xml;HDR=YES;ReadOnly=False';",
                _Arquivo
            )

            conexao = OleDbConnection(_StringConexao)

            cmd_text = ("SELECT [FUNCIONARIO],[BASE],[UF DA BASE],[MÊS REFERENCIA],[ANO REFERENCIA] FROM [BASE$] WHERE [FUNCIONARIO] IS NOT NULL AND [BASE] IS NOT NULL AND [MÊS REFERENCIA] IS NOT NULL AND [ANO REFERENCIA] IS NOT NULL")
            adapter = OleDbDataAdapter(cmd_text, conexao)

            ds = DataSet()
            conexao.Open()
            adapter.Fill(ds)

            total_linhas = 0
            adicionadas = 0
            sem_match = 0
            erros = 0

            tbl = ds.Tables[0]

            for linha in tbl.Rows:
                total_linhas += 1

                def get_val(row, col):
                    try:
                        if row.IsNull(col):
                            return None
                        return str(row[col]).strip()
                    except:
                        return None


                config = {
                 "TR-ACARAU": ("283,02", "COMUM", "C"),
                 "TR-AGUA BOA": ("462,07", "COMUM", "A"),
                 "TR-ALAGOINHAS": ("283,02", "COMUM", "C"),
                 "TR-ALEGRETE": ("571,82", "ESPECIAL", "C"),
                 "TR-ALFENAS": ("369,66", "COMUM", "B"),
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
                 "TR-CAICO": ("658,46", "ESPECIAL", "B"),
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
                 "TR-IGARAPE-MIRI": ("571,82", "ESPECIAL", "C"),
                 "TR-IGUATU": ("369,66", "COMUM", "B"),
                 "TR-IMPERATRIZ": ("462,07", "COMUM", "A"),
                 "TR-IPATINGA": ("369,66", "COMUM", "B"),
                 "TR-IPORA": ("283,02", "COMUM", "C"),
                 "TR-IRECE": ("750,87", "ESPECIAL", "A"),
                 "TR-ITABAIANA": ("369,66", "COMUM", "B"),
                 "TR-ITAJAI": ("283,02", "COMUM", "C"),
                 "TR-ITAPETINGA": ("462,07", "COMUM", "A"),
                 "TR-ITAPIPOCA": ("283,02", "COMUM", "C"),
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
                 "TR-SAO RAIMUNDO NONATO": ("750,87", "ESPECIAL", "A"),
                 "TR-SOUSA": ("658,46", "ESPECIAL", "B"),
                 "TR-TABATINGA": ("750,87", "ESPECIAL", "A"),
                 "TR-TANGARA DA SERRA": ("369,66", "COMUM", "B"),
                 "TR-TEFE": ("750,87", "ESPECIAL", "A"),
                 "TR-TEIXEIRA DE FREITAS": ("462,07", "COMUM", "A"),
                 "TR-TEOFILO OTONI": ("462,07", "COMUM", "A"),
                 "TR-TIANGUA": ("369,66", "COMUM", "B"),
                 "TR-TORRES": ("283,02", "COMUM", "C"),
                 "TR-TRES LAGOAS": ("369,66", "COMUM", "B"),
                 "TR-TUBARAO": ("283,02", "COMUM", "C"),
                 "TR-TUCURUI": ("658,46", "ESPECIAL", "B"),
                 "TR-UBERABA": ("283,02", "COMUM", "C"),
                 "TR-UIRAUNA": ("658,46", "ESPECIAL", "B"),
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
                 "TR-VITORIA DE SANTO ANTAO": ("283,02", "COMUM", "C"),
                 "TR-VOLTA REDONDA": ("283,02", "COMUM", "C"),
                 "TR-XINGUARA": ("462,07", "COMUM", "A"),
                 "TR-DELMIRO GOUVEIA": ("658,46", "ESPECIAL", "B"),
                 "TR-MOGI MIRIM": ("283,02", "COMUM", "C"),
                 "TR-ORIXIMINA": ("750,87", "ESPECIAL", "A"),
                 "TR-PONTES E LACERDA": ("658,46", "ESPECIAL", "B"),
                 "TR-SAO MIGUEL DO GUAPORE": ("658,46", "ESPECIAL", "B"),
                 "TR-ITACOATIARA": ("658,46", "ESPECIAL", "B"),
                 "TR-ILHEUS": ("369,66", "COMUM", "B"),
                 "TR-SANTO ANTONIO DA PLATINA": ("283,02", "COMUM", "B")
             
                }



                favorecido = get_val(linha, "FUNCIONARIO")
                base = get_val(linha, "BASE")
                uf = get_val(linha, "UF DA BASE")
                mes = get_val(linha, "MÊS REFERENCIA")
                ano = get_val(linha, "ANO REFERENCIA")

                tipo_base = ''
                categoria = ''

                if base in config:
                    valor, tipo_base, categoria = config[base]
                    tipo_base = tipo_base
                    categoria = categoria      

                    if not any([favorecido, base, uf, mes, ano]):
                        continue

                nome_fav = (favorecido or "").split('(')[0].strip()
                nome_like = nome_fav.replace("'", "''") + "%"

                sql = ("Select Distinct To_Char(p.ID_PESSOA) As ID_PESSOA, p.NOME || ' (' || p.USUARIO_REDE || ') - ' || f.status_matricula As nomemat, ORGAO.DESCRICAO, cp.MATRICULA, p.ATIVO From CAD_FUNCIONARIO_V f Inner Join CP_PESSOA cp On f.matricula = cp.matricula Inner Join PESSOA p On cp.ID_PESSOA = p.id_pessoa Inner Join ORGAO On p.ID_ORGAO = ORGAO.ID_ORGAO Where Upper(p.NOME) LIKE UPPER('" + nome_like + "') And p.ATIVO = 'Sim' Order By nomemat")

                try:
                    dados = DB.ExecuteDataTable(sql)

                    if dados.Rows.Count > 0:
                        row = dados.Rows[0]
                        id = row['ID_PESSOA'].ToString()
                        matricula = row['MATRICULA'].ToString()

                        valores = [id, matricula, favorecido, base, uf, tipo_base, categoria, mes, ano]
                        OrdemServico.AdicionaLinhaRegistro(nomeGrid, nomesCampos, valores)
                        adicionadas += 1
                    else:
                        sem_match += 1

                except Exception as ex:
                    erros += 1
                    continue

            conexao.Close()

            qtd = 0
            try:
                qtd = OrdemServico.GetCustom(nomeGrid).Rows.Count
            except:
                pass

            resumo = (
                "Importação concluída!\n\n"
                "Linhas lidas: {0}\n"
                "Adicionadas: {1}\n"
                "Funcionário ou Base não encontrada: {2}\n"
                "Erros: {3}\n"
                "Total na GRID agora: {4}"
            ).format(total_linhas, adicionadas, sem_match, erros, qtd)

            Formulario.ExibeMensagem(resumo)
            Formulario["CHECKBOX2"].Habilitado = False

        readExcel(
            ["ID_FUNCIONARIO", "MATRICULA", "FUNCIONARIO", "BASE", "UF","TIPO_BASE", "CLASSIFICACAO", "MES_REFERENCIA", "ANO_REFERENCIA"],
            "BASE_DESTACADA_LOTE"
        )


        #Formulario['CHECKBOX1'].Visivel = True
        #Formulario['CHECKBOX1'].Habilitado = True


    else:
        Formulario.ExibeMensagem("Não tem Arquivo anexado para importação.")
        Controle.Valor = False
```
  - VALOR "Valor da base" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - DIAS "Dias úteis no mês" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] — Coluna=2
  - LOG_API "Controle LOG Douglas" [Memo String(2000) → CPE_DADOS.LOG_API] obrigatório
- ClientesAutorizados:
  - PapelProcessoId=64981; PapelAutorizado=Douglas - Teste
  - PapelProcessoId=67398; PapelAutorizado=Supravizio - Administração
  - PapelProcessoId=67408; PapelAutorizado=Dires

### [362822] SubProcesso ""
Responsável: Responsável atual (papel 36)
Config: AssociacaoId=1483
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Feriado
from Venki.Supravizio.Recurso.Custom import Pessoa
import peopleSoft
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

from System import DateTime, DayOfWeek

# ========================= Helpers mínimos ==============================

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
    formatos = ["dd-MM-yyyy", "dd/MM/yyyy", "yyyy-MM-dd", "yyyy/MM/dd"]
    for f in formatos:
        try:
            return DateTime.ParseExact(s, f, None)
        except:
            pass
    try:
        return DateTime.Parse(s)  # caso não funcione
    except:
        return None

def to_int_safe(v, default=0):
    try:
        return Convert.ToInt32(v)
    except:
        try:
            return int(str(v))
        except:
            return default

def to_list(value):

    if value is None:
        return []
    try:
        if isinstance(value, str):
            return []
    except:
        pass
    try:
        if hasattr(value, "Rows"):
            return list(value.Rows)
    except:
        pass
    try:
        if hasattr(value, "ContainsKey"):
            return [value]
        if isinstance(value, dict):
            return [value]
    except:
        pass
    try:
        return list(value)
    except:
        return []

def periodo_para_dias_uteis_no_mes(di, df, ano_, mes_):
    s = set()
    if di is None or df is None:
        return s
    ini_mes = DateTime(ano_, mes_, 1)
    fim_mes = DateTime(ano_, mes_, DateTime.DaysInMonth(ano_, mes_))
    ini = di if di > ini_mes else ini_mes
    fim = df if df < fim_mes else fim_mes
    if ini > fim:
        return s
    d = ini
    while d <= fim:
        if d.DayOfWeek != DayOfWeek.Saturday and d.DayOfWeek != DayOfWeek.Sunday:
            s.add(d.Date)
        d = d.AddDays(1)
    return s

# ========================= Script principal ==============================

grid = OrdemServico.GetCustom('BASE_DESTACADA_LOTE')

for i in grid.Rows:
    funcionario   = i['FUNCIONARIO'].ToString()
    base          = i['BASE'].ToString()
    uf            = i['UF'].ToString()
    mes           = Convert.ToInt32(i['MES_REFERENCIA'])
    ano           = Convert.ToInt32(i['ANO_REFERENCIA'])
    id            = Convert.ToInt32(i['ID_FUNCIONARIO'])  # int corrige Pessoa.Carrega
    tipo_base     = i['TIPO_BASE'].ToString()
    classificacao = i['CLASSIFICACAO'].ToString()
    matricula     = i['MATRICULA'].ToString()

    # A nova API recebe o período no formato dd/MM/yyyy.
    primeiroDiaConsulta = DateTime(ano, mes, 1)
    ultimoDiaConsulta = DateTime(ano, mes, DateTime.DaysInMonth(ano, mes))
    dataInicialConsulta = primeiroDiaConsulta.ToString("dd/MM/yyyy")
    dataFinalConsulta = ultimoDiaConsulta.ToString("dd/MM/yyyy")

    # A função da biblioteca peopleSoft realiza as duas chamadas:
    # tipo=A (Ausência) e tipo=F (Férias), consolidando os itens retornados.
    ausencias_raw = consultaAusenciasFerias(
        matricula,
        dataInicialConsulta,
        dataFinalConsulta
    )
    ausencias = to_list(ausencias_raw)

    # ------- LOG base para acompanhamento -------
    teste = (
        "==== RELATÓRIO DE LOTAÇÃO - LOG ====\n\n"
        "Colaborador : {0}\n"
        "Matrícula   : {1}\n"
        "Período consultado na API: {2} a {3}\n"
        "------------------------------------------------------------------\n"
        "AUSÊNCIAS E FÉRIAS ENCONTRADAS NA API SYSAID\n"
    ).format(funcionario, matricula, dataInicialConsulta, dataFinalConsulta)

    # ======================= CÁLCULO DIAS ÚTEIS / FERIADOS / RESUMO =======================
    dias_uteis_set = set()
    dias_no_mes = DateTime.DaysInMonth(ano, mes)
    for dia in range(1, dias_no_mes + 1):
        d = DateTime(ano, mes, dia)
        if d.DayOfWeek != DayOfWeek.Saturday and d.DayOfWeek != DayOfWeek.Sunday:
            dias_uteis_set.add(d.Date)

    dias_ausentes_set = set()
    ausencias_lista_para_log = []

    if len(ausencias) > 0:
        for a in ausencias:
            try:
                data_saida = to_str(a["data_saida"])
                data_retorno = to_str(a["data_retorno"])
                di = ParseDateSafe(data_saida)
                df = ParseDateSafe(data_retorno)
            except:
                data_saida = ""
                data_retorno = ""
                di = None
                df = None

            if di is not None and df is not None:
                dias_periodo = periodo_para_dias_uteis_no_mes(di, df, ano, mes)
                dias_ausentes_set |= dias_periodo

                try:
                    duracao_calendario = (df.Date - di.Date).Days + 1
                except:
                    duracao_calendario = ""

                ausencias_lista_para_log.append(
                    "Início: {0} | Retorno: {1} | Duração calendário: {2} dia(s)".format(
                        data_saida,
                        data_retorno,
                        to_str(duracao_calendario)
                    )
                )
            else:
                ausencias_lista_para_log.append(
                    "Registro ignorado por data inválida | Início: {0} | Retorno: {1}".format(
                        data_saida,
                        data_retorno
                    )
                )

    base_SV_formatada = base[3:] if base and len(base) > 3 else base

    mes_ano = "{}/{}".format(str(mes).zfill(2), ano)

    primeiroDia  = DateTime(ano, mes, 1)
    proximoMes   = primeiroDia.AddMonths(1)
    d1_lit = primeiroDia.ToString("yyyy-MM-dd")  # para usar como DATE 'YYYY-MM-DD' no Oracle
    d2_lit = proximoMes.ToString("yyyy-MM-dd")

    cidade_sql = (base_SV_formatada or '').replace("'", "''")
    uf_sql     = (uf or '').replace("'", "''")


    fer_tr = DB.ExecuteDataTable(
    "SELECT fer.DT_FERIADO, fer.UF, fer.CIDADE, fer.TIPO, fer.SEMANA "
    "FROM tb_feriados_municipais fer "
    "WHERE ( (fer.CIDADE = '" + cidade_sql + "' AND fer.UF = '" + uf_sql + "') "
    "        OR (fer.TIPO = 'Nacional' OR (fer.UF = 'BR' AND UPPER(fer.CIDADE) IN ('TODOS','TODAS'))) ) "
    "  AND fer.DT_FERIADO >= DATE '" + d1_lit + "' "
    "  AND fer.DT_FERIADO <  DATE '" + d2_lit + "' "
    "  AND TO_CHAR(fer.DT_FERIADO, 'DY', 'NLS_DATE_LANGUAGE=ENGLISH') NOT IN ('SAT','SUN') "
    "ORDER BY fer.DT_FERIADO"
    )

    lista_feriados = []
    feriados_municipais_log = []
    feriados_nacionais_log = []
    try:
        for d in fer_tr.Rows:
            try:
                data_fmt = d["DT_FERIADO"].ToString("dd/MM/yyyy")
            except:
                data_fmt = to_str(d["DT_FERIADO"])

            lista_feriados.append(data_fmt)

            try:
                tipo_fer = to_str(d["TIPO"]).strip().upper()
            except:
                tipo_fer = ""
            try:
                uf_fer = to_str(d["UF"]).strip().upper()
            except:
                uf_fer = ""
            try:
                cid_fer = to_str(d["CIDADE"]).strip()
            except:
                cid_fer = ""

            if tipo_fer == "NACIONAL" or (uf_fer == "BR" and cid_fer.strip().upper() in ("TODOS", "TODAS")):
                feriados_nacionais_log.append(data_fmt)
            else:
                feriados_municipais_log.append("{0} - {1}/{2}".format(data_fmt, cid_fer, uf_fer))
    except:
        pass


    feriados_set = set()
    for data_str in lista_feriados:
        dt = ParseDateSafe(data_str)
        if dt is not None:
            feriados_set.add(dt.Date)

    union_aus_fer = dias_ausentes_set | feriados_set
    dias_trabalhaveis_reais_set = dias_uteis_set - union_aus_fer


    qtd_ausentes_uteis = len(dias_ausentes_set)
    qtd_feriados = len(feriados_set)
    qtd_overlap = len(dias_ausentes_set & feriados_set)
    total_finais = len(dias_trabalhaveis_reais_set)
    total_uteis = len(dias_uteis_set) - qtd_feriados

    teste += "\n------------------------------------------------------------------\n"
    teste += "AUSÊNCIAS E FÉRIAS (NO MÊS DA SOLICITAÇÃO)\n\n"
    if len(ausencias_lista_para_log) > 0:
        teste += "  ¿ Registros:\n    - " + "\n    - ".join(ausencias_lista_para_log) + "\n"
    else:
        teste += "  ¿ Registros: Nenhuma ausência ou férias encontrada para o mês da solicitação\n"

    teste += "\nFERIADOS ({mm}/{aa})\n\n".format(mm=str(mes).zfill(2), aa=ano)
    if len(feriados_municipais_log) > 0:
        teste += "  ¿ Municipais/Estaduais ({0}): {1}\n".format(
            len(feriados_municipais_log), "; ".join(feriados_municipais_log)
        )
    else:
        teste += "  ¿ Municipais/Estaduais: nenhum\n"
    if len(feriados_nacionais_log) > 0:
        teste += "  ¿ Nacionais ({0}): {1}\n".format(
            len(feriados_nacionais_log), ", ".join(feriados_nacionais_log)
        )
    else:
        teste += "  ¿ Nacionais: nenhum\n"

    teste += (
        "\n==== RESUMO ({mm}/{aa}) ====\n\n"
        "Dias úteis do mês: {uteis}\n"
        "Dias úteis (descontando feriados): {uteis_fer}\n"
        "Dias de ausência/férias (apenas dias úteis): {aus}\n"
        "Feriados(Municipal e/ou estadual) : {fer}\n"
        "Interseção (ausência/férias - feriado) : {ov}\n"
        "Dias trabalhados reais: {final}\n"
    ).format(
        uteis = str(len(dias_uteis_set)),
        mm=str(mes).zfill(2),
        aa=ano,
        uteis_fer=total_uteis,
        aus=qtd_ausentes_uteis,
        fer=qtd_feriados,
        ov=qtd_overlap,
        final=total_finais
    )
    # ===== FIM: Seções de AUSÊNCIAS (mês), FERIADOS e RESUMO (apenas texto) =====



    # ======================= Subprocesso / Campos =======================

    sub = OrdemServico.IniciaSubProcesso(OrdemServico.Atividade)

    sub.Cliente = Pessoa.Carrega(id)
    sub.Assunto = "Indenização por Lotação em Base Destacada"

    lista = Utils.ExecuteDataTable(
        "SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, "
        "CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, "
        "C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO "
        "FROM PESSOA P "
        "INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA "
        "INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO "
        "LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) "
        "WHERE P.ID_PESSOA = '" + id.ToString() + "'"
    )



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
        "TR-PARAÍSO": 369.66,
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

    valor_base = 0.0

    if base in mapa_bases:
        sub["VALOR"] = mapa_bases[base]
        valor_base = mapa_bases[base]


    valor_final_log = Convert.ToDecimal((valor_base / total_uteis) * total_finais)
    teste += (
        "\n ----- Cálculo do valor -----\n\n"
        "(Valor da Base / (Dias úteis no Mês - Feriados)) * Dias trabalhados reais\n"
        "({0} / {1}) x {2}\n"
        "{3}"
    ).format(str(valor_base), str(total_uteis), str(total_finais), str(valor_final_log))    



    funcao = ""
    for linha in lista.Rows:
        cargo = linha["CARGO"].ToString()
        if linha["FIM_DATA_FUNCAO"] is None or linha["FIM_DATA_FUNCAO"].ToString().strip() == "":
            funcao = linha["FUNCAO_GRATIFICADA"].ToString()
        uor = linha["DESCRICAO"].ToString()

        sub["TE_CARGO"] = cargo
        sub["TE_FUNCAO"] = funcao
        sub["TE_UOR"]   = uor


    sub["TE_NOME_EMPREGADO"] = funcionario
    sub["TE_MATRICULA"]      = matricula
    sub["COMBOBOX"]          = base
    sub["MES_REFERENCIA"]    = mes
    sub["ANO_REF"]           = ano
    sub["TIPO_BASE"]         = tipo_base
    sub["CATEGORIA_IDENIZACAO"] = classificacao
    sub["DIAS_DE_TRA"]          = total_finais
    sub["DIAS"]                 = total_uteis
    sub["LOG_API"] = (teste.ToString() if hasattr(teste,"ToString") else str(teste))[:2000]
    sub["ID_PERSON"]            = id

    sub.Salva()
    sub.AvancaAtividade()

AvancaProximaAtividade = True
```
- Associação: Ativo=true; FraseAssociacao=Base Lote --> Base; FraseInversaAssociacao=Base --> Base Lote; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=BASELOTEPARABASE; SeparadorSequencial=. | fonte: Indenização por Lotação em base Destacada (Abertura em Lote) → alvo: Indenização por Lotação em Base Destacada

### [362823] Tarefa "Avaliar os Subchamados e avançar para finalização"
Responsável: Cliente (papel 18)

## Papéis usados
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
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

## Campos customizados usados (definição global)

### LABEL1 — Texto Informativo
Label String(2000) → CP_ORDEM_SERVICO.LABEL1

### BASE_DESTACADA_LOTE — Base Destacada Lote
DataGrid RecordList → Z_00143_BASE_DESTACADA_LOTE.BASE_DESTACADA_LOTE
Colunas do registro:
- FUNCIONARIO "Funcionário" [TextBox String]
- BASE "Base Destacada" [DropDownList String]
**BASE.LookupScript**
```python
#
```
- MES_REFERENCIA "Mês Referência" [TextBox String]
- ANO_REFERENCIA "Ano Referência" [TextBox String]
- ID_FUNCIONARIO "ID Funcionário" [TextBox String]
- TIPO_BASE "TIPO BASE" [TextBox String]
- CLASSIFICACAO "CLASSIFICACAO BASE" [TextBox String]
- UF "UF" [TextBox String]
- MATRICULA "MATRICULA" [TextBox String]

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

### CHECKBOX2 — Checkbox2
CheckBox Boolean → CPE_PESSOAS.CHECKBOX2

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### DIAS — Dias
TextBox Integer → CPE_HOMOLOGACAO.DIAS

### LOG_API — LOG API
Memo String(2000) → CPE_DADOS.LOG_API

## Biblioteca de scripts referenciada
peopleSoft, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
