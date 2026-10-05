# Fluxo: Hive Place (HIVEPLACE) — versão 31
Caminho: Fluxos > Nova Estruturação de Negócios Versão 31 Hive Place
XML: `XMLs para teste/Nova_Estruturação_de_Negócios_Versão_31_Hive_Place.xml` | Supravizio 19.1.1 | SubProcessoId 20565 | DesenhoProcessoId 2893 | ProcessoId 79
Órgão dono: None | Responsável: None
Classe do subprocesso: DescricaoCliente=Hive Place (Assinatura de Contrato e Aditivação de Contrato); CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: HIVEPlace (Assinatura de Contrato e Aditivação de Contrato) (HIVEPLACE)

## Grafo do fluxo
- [327898] SubProcesso "Portal de Estruturação de Novos Negócios" {Fila de Oportunidade} → [327899] 
- [327899] EventoFinal "" → (fim)
- [327900] EventoInicial "Assinatura de Contrato e Aditivação de Contrato" → [327898] Portal de Estruturação de Novos Negócios

## Atividades

### [327898] SubProcesso "Portal de Estruturação de Novos Negócios"
Responsável: Fila de Oportunidade (papel 599)
Config: ChamadaAssincrona=true; AssociacaoId=1542; PassaTodosItens=true; RetornaTodosItens=true
- ValoresInputs:
  - CustomPropertyId=2551; CustomProperty=APROVADOR_PB
  - CustomPropertyId=240; CustomProperty=CNPJ
  - CustomPropertyId=1074; CustomProperty=COMBOBOX1
  - CustomPropertyId=3636; CustomProperty=GRID_PESSOAS
  - CustomPropertyId=3613; CustomProperty=NN_DATA_REPROG
  - CustomPropertyId=958; CustomProperty=NN_GERENCIA_NEGOCIO
  - CustomPropertyId=1781; CustomProperty=NN_LINHA_NEGOCIO
  - CustomPropertyId=952; CustomProperty=NN_OBJETO_PROPOSTA
  - CustomPropertyId=1778; CustomProperty=NN_PORTFOLIO
  - CustomPropertyId=1783; CustomProperty=NN_PRAZO_ESTIMADO
  - CustomPropertyId=1782; CustomProperty=NN_PRODUTO
  - CustomPropertyId=1950; CustomProperty=NN_PRODUTO_EXISTENTE
  - CustomPropertyId=1779; CustomProperty=NN_SEGMENTO
  - CustomPropertyId=1785; CustomProperty=NN_STATUS_PROJETO
  - CustomPropertyId=506; CustomProperty=PREMISSA_DOD
  - CustomPropertyId=1002; CustomProperty=SIM_NAO
  - CustomPropertyId=3352; CustomProperty=CANALDEVENDA
  - CustomPropertyId=3585; CustomProperty=CANALDEVENDA1
  - CustomPropertyId=44; CustomProperty=MOTIVO
  - CustomPropertyId=3613; CustomProperty=NN_DATA_REPROG
  - CustomPropertyId=3598; CustomProperty=NN_DATAPICKER1
  - CustomPropertyId=3609; CustomProperty=NN_FORMACONTRATACAO
  - CustomPropertyId=3587; CustomProperty=NN_NUMERO_NDA
  - CustomPropertyId=3630; CustomProperty=NN_POC
- Associação: Ativo=true; FraseAssociacao=Hive Place > Portal Novos Negócios; FraseInversaAssociacao=Portal Novos Negócios > Hive Place; CardinalidadeFonte=ZeroOrOne; CardinalidadeAlvo=ZeroOrOne; Nome=HIVEPLACE | fonte: Hive Place → alvo: Portal de Estruturação de Negócios

### [327899] EventoFinal ""

### [327900] EventoInicial "Assinatura de Contrato e Aditivação de Contrato"
Config: Configuracao={"ServicoIniciador":"HIVEPLACE"}
TipoSolicitacao: Novos Negócios
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Projeto Básico — RequeridoInicial=true
  - anexo "Documentos da Qualificação" classes: Edital — RequeridoInicial=true
  - anexo "" classes: RFP RFI RFQ  — RequeridoInicial=true
  - anexo "" classes: Outros documentos — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - CANALDEVENDA "Contato(s) do Cliente" [DataGrid RecordList → Z_00143_CANALDEVENDA.CANALDEVENDA] obrigatório — FormaEdicaoWeb=JanelaPopup; LarguraJanelaPopup=300
    - coluna SETCLIENT obrigatório
    - coluna DATAINIPROSP obrigatório
    - coluna NOMECTTCLIENT obrigatório
    - coluna TELLCLIENT obrigatório
    - coluna DATARESPCLIENT obrigatório
    - coluna EMAILCLIENT obrigatório
    - coluna CARGOCLIENT obrigatório
  - CANALDEVENDA1 "Canal de Venda" [DropDownList String(900) → CPE_NEGOCIOS.CANALDEVENDA1] obrigatório
  - NN_DATAPICKER1 "Data inicio da Prospecção" [DatePicker DateTime → CPE_NEGOCIOS.NN_DATAPICKER1] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna DATA obrigatório
    - coluna SITUACAO obrigatório
  - NN_NUMERO_NDA "Número do Chamado do NDA " [TextBox String → CPE_NEGOCIOS.NN_NUMERO_NDA]
  - NN_FORMACONTRATACAO "Forma de Contratação" [DropDownList String → CPE_HOMOLOGACAO.NN_FORMACONTRATACAO] obrigatório
  - NN_POC "Teve POC/Piloto/Degustação" [DropDownList String → CPE_NEGOCIOS.NN_POC] obrigatório
**NN_POC.ScriptModificado**
```python
if Formulario['NN_POC'].Valor == 'Não':
    Formulario['MOTIVO'].Visivel = False
    Formulario['MOTIVO'].Habilitado = False
    
else:
    Formulario['MOTIVO'].Visivel = True
    Formulario['MOTIVO'].Habilitado = True
```
  - MOTIVO "Detalhamento POC/Piloto/Degustação" [Memo String(1500) → CP_ORDEM_SERVICO.MOTIVO] obrigatório
- Operação PR0001 Preencher Campos
  - NN_PRAZO_ESTIMADO "Prazo do contrato estimado" [DropDownList String → CPE_NEGOCIOS.NN_PRAZO_ESTIMADO] obrigatório
  - NN_PORTFOLIO "Referência de mercado (fornecedor/intervenientes/concorrentes/normas, etc)" [Memo String(2000) → CPE_NEGOCIOS.NN_PORTFOLIO] obrigatório
  - SIM_NAO "Projeto contido no orçamento?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - NN_DATA_REPROG "Resposta ao Cliente" [DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG] — FormaEdicaoWeb=JanelaPopup
    - coluna DATA obrigatório
    - coluna SITUACAO obrigatório
  - NN_GERENCIA_NEGOCIO "Área gestora do produto/serviço" [DropDownList String → CP_ORDEM_SERVICO.NN_GERENCIA_NEGOCIO] obrigatório
  - NN_LINHA_NEGOCIO "Linha de Negócio" [DropDownList String → CPE_NEGOCIOS.NN_LINHA_NEGOCIO] obrigatório
**NN_LINHA_NEGOCIO.ScriptModificado**
```python
from Venki.Supravizio.Configuracao.Custom import Software
if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Infraestrutura e Disponibilidade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de TAA;Disponibilidade Operacional de Bens de Automação Bancária;Monitoração de Ambientes;Infraestrutura de Data Center;Assistência Técnica de Sistemas de Portas Giratórias, Sala On-Line e Nobreak'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Gestão de Segurança':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Disponibilidade Operacional de Sistema de Alarme e Dispositivos de Resposta;Disponibilidade Operacional de Sistema de Imagens;PSIM - Plataforma de Integração e Gerenciamento de informações de segurança física;Cross Data Team (CDT);Managed Security Services Provider ¿ MSSP (Centro de Operação de Cyber Segurança ¿ SOC N1/N2/N3, Professional Security Services, Phishing, Pentest e Gestão de Vulnerabilidade)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Comunicação e Conectividade':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Intevia - Mensageria SMS;Intevia - Mensageria e e-mail marketing;Teya - Outsourcing de Telefonia (Plataforma de Voz e Vídeo)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Canais e Backoffice':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Centrais de Relacionamento e Telecobrança;Cobrança Extrajudicial de Dívidas;Gestão Eletrônica De Documentos (GED);Kit Pré-Ajuizamento;Microfilmagem'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções Digitais':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Fábrica de Software;Plataformas (Aprovve Service);Hiperautomação (LowCode)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Soluções de Parcerias Estratégicas':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Interoperabilidade (HIVEPlace);Revenda Especializada (Licenter)'



if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Correspondente Bancário':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Gestão de Correspondentes Bancários;Representação Comercial;Agente de Crédito Rural (ACR)'




if Formulario["NN_LINHA_NEGOCIO"].Valor == 'Outros':
    Formulario["NN_PRODUTO"].Visivel = True
    Formulario["NN_PRODUTO"].Itens = 'Outros'
```
  - NN_PRODUTO "Produto" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO] obrigatório
  - NN_STATUS_PROJETO "Status projeto" [DropDownList String → CPE_NEGOCIOS.NN_STATUS_PROJETO] obrigatório
  - APROVADOR_PB "GESTOR(ES) DO(S) PRODUTO(S) - (Gediv)" [DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna APROVADORES obrigatório
  - GRID_PESSOAS "Tomar Conhecimento da Oportunidade (Gerex e Super)" [DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS] — FormaEdicaoWeb=JanelaPopup
    - coluna PESSOAS
  - NN_OBJETO_PROPOSTA "Objetivo do Negócio (Necessidade do cliente)" [Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA] obrigatório
  - PREMISSA_DOD "Premissas/Restrições/Volumetria" [Memo String(2000) → CP_ORDEM_SERVICO.PREMISSA_DOD] obrigatório
  - NN_SEGMENTO "Segmento de Mercado" [DropDownList String → CPE_NEGOCIOS.NN_SEGMENTO] obrigatório
**NN_SEGMENTO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Local
if Formulario["NN_SEGMENTO"].Valor == 'Mercado':
    Formulario["COMBOBOX1"].Itens = '3Corp;AIDC;Aiko;Algar;Assban;Banco ABC;Banco Inter;Banco Original;Banco Pan;Banco Topázio;Banrisul;Basa;Bradesco;Brasil Digital;Brinks;Centurylink;Ceuma;Clear Sales;Connectoway;Conservo;Credfisa;Ctis;Daten;Dell;Digio;Dotz;Engepron;Engie;Envestcon;Espaço Y;E-Vida;FazSol;FGCOOP;Galgo;Gemalto;Gerdau;Globo;Grupo Saga;HCL Tech;IBCG;ICESP;Infinity;INPI;Lenovo;Lever Tech;Localiza;M4U;Mercantil;Montreal;Oi;Perto;Porto Seguro;PrevData;Prevpeb;Prosegur;Qintess;Ririera;Salutis;Sicob;Sicredi;Smiles;Thales;Valor Invest;Via Varejo;Viridi;Vivo;Zoom;SPDM - ASSOCIACAO PAULISTA PARA O DESENVOLVIMENTO DA MEDICINA;AUDIO CODES;Shooting House;Grupo Concórdia;Grupo Artico;AIDC;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'Governo':
    Formulario["COMBOBOX1"].Itens = 'Aeronáutica;AGU;ANA;Bacen;Banco do Nordeste;BANDES;Banestes;Banpará;BNDES;BRB;Caixa;Caixa Asset;Caixa Cartões;Caixa DTVM;Caixa Previ;Caixa Seguridade;Câmara dos Deputados;CBTU;CEB;CFP;Conab;Correios;Dataprev;Detran DF;EBC;Eletrobrás;Embasa;Emgea;Exército;Finep;FUNPREV PIAUÍ;Fusan;Governo da Bahia;Governo da SC;Governo do ACRE;HC-UFG;Hemobrás;IPLanrio;IPMT Teresina;Iprev;JUCESP;MDIC;ME e MTPS;Ministério das Comunicações;Ministério MDA;MME;MPF;Neoenergia;OAB;PCDF;Petrobrás;PJRN;Prevdata;Procuradoria-Geral da Fazenda Nacional;Prodam;Prode Pará;Prodemge;SCJF-DF;Sebrae;Sefaz MA;SEFAZ SP;Serpro;SJ Campos;SPTrans;TC Rondônia;TJ ES;TJ Sergipe;TJ SC;TJ TO;TRE Pará;TRE Roraima;TRF1ª;TRF2ª;TRF4ª;Valec;ANATEL;TRT4;Tribunal de Contas/RR;Tribunal de Contas/GO;SUPEL/RO;Pref. de Rio Branco/AC;CREA/PR;Detran/PE;Defensoria Pública/BA;Dataprev;Tribunal de Justiça/BA;Pref. de Schroeder/SC;Fund. Oswaldo Cruz/RJ;SEPLOG/SE;SESC/SE;Sec. de Seg. Pública/PI;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True

elif Formulario["NN_SEGMENTO"].Valor == 'Banco do Brasil':
    Formulario["COMBOBOX1"].Itens = 'USI;DITEC;DIOPE;DISEC;DIGOV;DICRE;DICOI;UCS;DIREC;UGE;UCR;DICOR;UAC;DINED;UAN;DIRAG;DIMEP;DIEMP;DIJUR;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
    
elif Formulario["NN_SEGMENTO"].Valor == 'ELBB':
    Formulario["COMBOBOX1"].Itens = 'ALELO;ALIANÇA DO BRASIL SEGUROS;ALIANÇA PAG;ALPHA SERV. DE AUTOATENDIMENTO;ATIVOS S.A. SEC. DE CRÉD. FINANCEIROS;BANCO PATAGONIA;BANCO VOTORANTIM;BB ADMINISTRADORA DE CARTÕES DE CRÉDITO;BB AG;BB AMERICAS;BB ASSET;BB ASSET MANAGEMENT IRELAND;BB BANCO DE INVESTIMENTO (BB-BI);BB CAYMAN ISLANDS HOLDING (BB-CI);BB CONSÓRCIOS;BB CORRETORA DE SEGUROS E ADMI.DE BENS S.A. (BB CORRETORA);BB ELO CARTÕES;BB LEASING;BB MAPFRE PARTICIPAÇÕES S.A;BB PREVIDÊNCIA;BB SECURITIES;BB SEGURIDADE;BB SEGUROS;BB USA HOLDING COMPANY INC;BRASIL DENTAL;BRASILCAP;BRASILPREV SEG. E PREV. S.A.;BRASILSEG;BV EMPREEND. E PARTICIPAÇÕES;BV INVEST. ALTERN. E GEST. DE RECUR;CADAM OVERSEAS LTD;CADAM;CAIXA DE ASSISTÊNCIA DOS EMPREGADOS (SIM);CÂMARA INTERBANCÁRIA DE PAGAMENTOS (CIP);CASSI;CATENO;CIA. HIDROMINERAL PIRATUBA;CICLIC;CIELO;CIELO S.A.;ECONOMUS;ELO HOLDING FINANCEIRA;ELO SERVIÇOS;ELOPAR;ESTRUT. BRAS. DE PROJ.;FUNDAÇÃO BANCO DO BRASIL (FBB);FUNDAÇÃO CODESC DE SEGURIDADE SOCIAL (FUSESC);GALGO SISTEMAS DE INFORMAÇÃO;GPAT COMPAÑIA FINANCIERA;KAOLIN INTERNATIONAL N.V.;KARTRA PARTICIPAÇÕES;LIVELO;MERCHANT E-SOLUTIONS;PAGGO SOLUÇÕES E MEIOS DE PAGAMENTOS;PREVBEP;PREVI;PROMOTIVA;QUOD;SERVINET SERVIÇOS;STELO;TBFORTE TRANSP. VALORES BRASIL FORTE;TBNET COM., LOCAÇÃO E ADM.;TECNOLOGIA BANCÁRIA;UBS BB SERV. \ ASSE. FIN. PART.;VOTORANTIM CORR. SEGUROS;OUTROS'
    Formulario['COMBOBOX1'].Visivel = True
```
  - COMBOBOX1 "Clientes" [DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1] obrigatório
  - CNPJ "CNPJ do Cliente" [TextBox String → CP_ORDEM_SERVICO.CNPJ] obrigatório — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00\\.000\\.000\\/0000\\-00"}
  - NN_PRODUTO_EXISTENTE "Produto do portfólio?" [DropDownList String → CPE_NEGOCIOS.NN_PRODUTO_EXISTENTE] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Qualificação da Oportunidade" classes: Qualificação de Oportunidade — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Anexo de documento" classes: Documentos — RequeridoInicial=true; PermiteMultiplosItens=true

## Papéis usados
### papel 599: Fila de Oportunidade
Tipo=RelacaoGrupos

## Campos customizados usados (definição global)

### CANALDEVENDA — Canal de Venda
DataGrid RecordList → Z_00143_CANALDEVENDA.CANALDEVENDA
Colunas do registro:
- NOMECTTCLIENT "Nome do contato do cliente" [TextBox String]
- TELLCLIENT "Telefone do cliente" [TextBox String]
- EMAILCLIENT "E-mail do cliente" [TextBox String]
- CARGOCLIENT "Cargo do cliente" [TextBox String]
- SETCLIENT "Setor do cliente" [TextBox String]

### CANALDEVENDA1 — Combo Box
DropDownList String(900) → CPE_NEGOCIOS.CANALDEVENDA1
Itens: Prospecção;Indicação;Parceria;Pós-venda;RFP/RFI/RFQ;Licitação;Canais Digitais;Network.

### NN_DATAPICKER1 — Data picker NN
DatePicker DateTime → CPE_NEGOCIOS.NN_DATAPICKER1

### NN_DATA_REPROG — Data de Reprogramaçãoo
DataGrid RecordList → Z_00143_NN_DATA_REPROG.NN_DATA_REPROG
Descrição: Data de Reprogramação
Colunas do registro:
- SITUACAO "Situação" [DropDownList String] itens: Reprogramação;Resposta ao cliente
- DATA "Data" [DateTimePicker DateTime]

### NN_NUMERO_NDA — Número NDA
TextBox String → CPE_NEGOCIOS.NN_NUMERO_NDA

### NN_FORMACONTRATACAO — Forma de Contratação
DropDownList String → CPE_HOMOLOGACAO.NN_FORMACONTRATACAO
Itens: Novo Contrato;Aditivo;Renovação;Recontratação

### NN_POC — Teve POC
DropDownList String → CPE_NEGOCIOS.NN_POC
Itens: POC;Piloto;Degustação;Não

### MOTIVO — Motivo da solicitação de serviço
Memo String(1500) → CP_ORDEM_SERVICO.MOTIVO

### NN_PRAZO_ESTIMADO — Prazo estimado do contrato
DropDownList String → CPE_NEGOCIOS.NN_PRAZO_ESTIMADO
Itens: 06 meses;12 meses;24 meses;36 meses;48 meses;60 meses

### NN_PORTFOLIO — Portfólio de soluções do provedor
Memo String(2000) → CPE_NEGOCIOS.NN_PORTFOLIO

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### NN_GERENCIA_NEGOCIO — Gerência Executiva do Negócio
DropDownList String → CP_ORDEM_SERVICO.NN_GERENCIA_NEGOCIO
**LookupScript**
```python
Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(id_orgao) AS id_orgao, DESCRICAO FROM ORGAO WHERE ATIVO LIKE 'Sim' ORDER BY DESCRICAO ")

#Itens = DB.ExecuteDataTable(" SELECT DISTINCT TO_CHAR(id_orgao) AS id_orgao, DESCRICAO FROM ORGAO WHERE ATIVO LIKE 'Sim' AND (DESCRICAO LIKE '%DIRE%' OR DESCRICAO LIKE '%GERE%' OR DESCRICAO LIKE '%GERÊ%' OR DESCRICAO LIKE '%PROGRA%') AND (DESCRICAO NOT LIKE '%DIV%' OR DESCRICAO NOT LIKE '%COMITE%' OR DESCRICAO NOT LIKE '%REGIO%') and id_orgao not in (1215, 1197) ORDER BY DESCRICAO ")
```

### NN_LINHA_NEGOCIO — Linha de Negócio
DropDownList String → CPE_NEGOCIOS.NN_LINHA_NEGOCIO
Itens: Infraestrutura e Disponibilidade;
Gestão de Segurança;
Comunicação e Conectividade;
Canais e Backoffice;Soluções Digitais;
Correspondente Bancário;Soluções de Parcerias Estratégicas;
Outros

### NN_PRODUTO — Produto
DropDownList String → CPE_NEGOCIOS.NN_PRODUTO
Itens: Disponibilidade Operacional de TAA;
Disponibilidade Operacional de Bens de Automação Bancária;
Monitoração de Ambientes;
Infraestrutura de Data Center;
Assistência Técnica;
DOSA;
DOCA;
DOSI;
PSIM;
SOC;
CDT;
Mensageria SMS;
Mensageria E-mail Marketing;
Outsourcing de Telefonia - PVV;
Central de Relacionamento e Telecobrança;
Cobrança Extrajudicial;
Preparação para Ajuizamento de Operações;
Microfilmagem;
Fábrica de Software;
Aprovve Service;
HIVEPlace;
Revenda Especializada;
Hosting de Data Center;
Gestão de rede de correspondentes substabelecidos;
Outros

### NN_STATUS_PROJETO — Status projeto
DropDownList String → CPE_NEGOCIOS.NN_STATUS_PROJETO
Itens: Normal;Alerta;Crítico

### APROVADOR_PB — Vistoriador dos Bens (no mínimo 3, sendo um o gestor de patrimônio)
DataGrid RecordList → Z_00143_APROVADOR_PB.APROVADOR_PB
Colunas do registro:
- APROVADORES "Aprovadores" [DropDownList String]
**APROVADORES.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### GRID_PESSOAS — Grid Pessoas
DataGrid RecordList → Z_00143_GRID_PESSOAS.GRID_PESSOAS
Colunas do registro:
- PESSOAS "Pessoas" [DropDownList String]
**PESSOAS.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE p.ativo = 'Sim' order by nomemat")
```

### NN_OBJETO_PROPOSTA — Objetivo da Proposta
Memo String(2000) → CP_ORDEM_SERVICO.NN_OBJETO_PROPOSTA

### PREMISSA_DOD — Premissas
Memo String(2000) → CP_ORDEM_SERVICO.PREMISSA_DOD
Descrição: O requisitante deve descrever fatores que, para fim de planejamento, são considerados reais, que afetam todos os aspectos do planejamento do projeto.


### NN_SEGMENTO — Segmento de Mercado
DropDownList String → CPE_NEGOCIOS.NN_SEGMENTO
Itens: Banco do Brasil;ELBB;Mercado;Governo

### COMBOBOX1 — Chamado Aberto?
DropDownList String(200) → CP_ORDEM_SERVICO.COMBOBOX1

### CNPJ — CNPJ
TextBox String → CP_ORDEM_SERVICO.CNPJ

### NN_PRODUTO_EXISTENTE — Produtu existente?
DropDownList String → CPE_NEGOCIOS.NN_PRODUTO_EXISTENTE
Descrição: Produto existente?
Itens: Sim;
Não

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
