# Fluxo: Recebimento de EPI (RECEBIMENTOEPI) — versão 12
Caminho: Fluxos > Serviços Assistência Técnica Versão 12 Recebimento de EPI
XML: `XMLs para teste/Serviços_Assistência_Técnica_Versão_12_Recebimento_de_EPI.xml` | Supravizio 19.1.1 | SubProcessoId 21071 | DesenhoProcessoId 2947 | ProcessoId 31
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: GEORGE DOS SANTOS SILVA
Classe do subprocesso: Objetivo=Recebimento de Equipamentos de Proteção; DescricaoCliente=Recebimento de Equipamentos de Proteção (EP); CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Recebimento de EPI; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Recebimento de EPI (RECEBIMENTOEPI); Recebimento de EPC (RECEBIMENTOEPC)

## Grafo do fluxo
- [336049] Tarefa "Solicitar aprovação do empregado" {Favorecido Cobra} → [G76200] Aprovado?
- [336296] LinkInicial "" {Favorecido} → [336049] Solicitar aprovação do empregado
- [336041] EventoFinal "" {Cliente} → (fim)
- [336043] EventoIntermediarioMensagem "OS reprovada" → [336045] 
- [336044] EventoInicial "" → [336046] Preencher Declaração
- [336045] EventoFinal "" → (fim)
- [336046] Tarefa "Preencher Declaração" {Favorecido Cobra} → [336049] Solicitar aprovação do empregado
- [336047] Tarefa "Gerar FQ1333-002
" {Favorecido Cobra} → [336048] Chamado Finalizado - Recebimento de EPI
- [336048] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI" → [336041] 
- [G76200] Gateway "Aprovado?" → «Reprovado» [336043] OS reprovada | «Aprovado» [336047] Gerar FQ1333-002


## Gateways
### [G76200] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [336043] OS reprovada: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
- alternativa → [336047] Gerar FQ1333-002
: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```

## Atividades

### [336049] Tarefa "Solicitar aprovação do empregado"
Responsável: Favorecido Cobra (papel 277)
Config: Codigo=APROVAR
**ScriptInicio**
```python
campos = ["CODIGO", "DESCRICAO_DETALHADA", "NUM_ITEM", "QUANTIDADE_ESTIMADA", "TE_CARGO", "TE_MATRICULA", "TE_NOME_EMPREGADO", "TE_UOR", "TEXT", "TEXT_1", "TEXT2"]

for i in campos:
    OrdemServico.ModificaCampoFormularioHabilitado(i, False)
```
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Recebimento de EPIs; ReenvioEmailAprovacao=24
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) DESCRICAO_DETALHADA "Descrição" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA]
  - (aprovação) EQUIP_EPI "Equipamentos EPI" [DataGrid RecordList → Z_00143_EQUIP_EPI.EQUIP_EPI] — PermiteModificarAprovado=true
  - (aprovação) TEXT2 "Unidade" [TextBox String → CPE_CSC.TEXT2]
  - (aprovação) QUANTIDADE_ESTIMADA "Quantidade" [DropDownList String → CPE_CSC.QUANTIDADE_ESTIMADA]
  - (aprovação) FAVORECIDO_COBRA "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA]
  - (aprovação) CODIGO "Código" [Memo String(2000) → CPE_ORDEM_SERVICO.CODIGO]
  - (aprovação) NUM_ITEM "CA" [TextBox String(30) → CP_ORDEM_SERVICO.NUM_ITEM]
  - (aprovação) TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - (aprovação) TEXT_1 "Item" [TextBox String(1000) → CPE_CSC.TEXT_1]
  - (aprovação) OBS1 " Declaração" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - (aprovação) TEXT "Data de retirada" [TextBox String(1000) → CPE_CSC.TEXT]
  - aprovador: Favorecido Cobra (Unico)
  - relatório: FormatoExportacao=PDF; RotuloLink=FQ1333-002: FICHA DE CONTROLE E ENTREGA DE EPI
- Relatorios:
  - FormatoExportacao=PDF

### [336296] LinkInicial ""
Responsável: Favorecido (papel 76)
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - TEXT "Data de retirada" [TextBox String(1000) → CPE_CSC.TEXT] obrigatório
  - TEXT_1 "Item" [TextBox String(1000) → CPE_CSC.TEXT_1] obrigatório
  - CODIGO "Código" [Memo String(2000) → CPE_ORDEM_SERVICO.CODIGO] obrigatório
  - NUM_ITEM "CA" [TextBox String(30) → CP_ORDEM_SERVICO.NUM_ITEM] obrigatório
  - QUANTIDADE_ESTIMADA "Quantidade" [DropDownList String → CPE_CSC.QUANTIDADE_ESTIMADA] obrigatório
  - TEXT2 "Unidade" [TextBox String → CPE_CSC.TEXT2] obrigatório
  - DESCRICAO_DETALHADA "Descrição" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA] obrigatório
  - TE_NOME_EMPREGADO "Favorecido" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
  - TE_CARGO "CARGO" [TextBox String → CPE_CSC.TE_CARGO] obrigatório
- Associação de subprocesso: AssociacaoId=1642; FraseAssociacao=EPI (Lote) -> EPI; Nome=RECEBIMENTOEPILOTE

### [336041] EventoFinal ""
Responsável: Cliente (papel 18)
- Relatorios:
  - FormatoExportacao=PDF

### [336043] EventoIntermediarioMensagem "OS reprovada"
Destinatário: Cliente e Favorecido (papel 398)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [336044] EventoInicial ""
TipoSolicitacao: Recebimento de EPI
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
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO]
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - EQUIP_EPI "Equipamentos EPI" [DataGrid RecordList → Z_00143_EQUIP_EPI.EQUIP_EPI] obrigatório — FormaEdicaoWeb=JanelaPopup
    - coluna UNIDADE obrigatório
    - coluna DESCRICAO obrigatório
    - coluna RETIRADA obrigatório
    - coluna ITEM obrigatório
**EQUIP_EPI.ITEM.ScriptModificado**
```python
item = FormularioRegistro['ITEM'].Valor.ToString()
FormularioRegistro['CODIGO'].Habilitado = False
FormularioRegistro['CA'].Habilitado = False
FormularioRegistro['DESCRICAO'].Habilitado = False

if item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026888 - 34':
    FormularioRegistro['CODIGO'].Valor = '026888'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026889 - 35':
    FormularioRegistro['CODIGO'].Valor = '026889'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026890 - 36':
    FormularioRegistro['CODIGO'].Valor = '026890'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026891 - 37':
    FormularioRegistro['CODIGO'].Valor = '026891'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026892 - 38':
    FormularioRegistro['CODIGO'].Valor = '026892'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026893 - 39':
    FormularioRegistro['CODIGO'].Valor = '026893'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026894 - 40':
    FormularioRegistro['CODIGO'].Valor = '026894'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026895 - 41':
    FormularioRegistro['CODIGO'].Valor = '026895'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026896 - 42':
    FormularioRegistro['CODIGO'].Valor = '026896'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026897 - 43':
    FormularioRegistro['CODIGO'].Valor = '026897'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026898 - 44':
    FormularioRegistro['CODIGO'].Valor = '026898'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026899 - 45':
    FormularioRegistro['CODIGO'].Valor = '026899'
    FormularioRegistro['CA'].Valor = '34550'
    FormularioRegistro['DESCRICAO'].Valor = 'Calçado de segurança tipo bota, fechamento em cadarço, confeccionado em microfibra, palmilha de montagem em fibras não metálicas resistentes à perfuração, costurada pelo processo strobel, forro interno em tecido, solado de poliuretano bidensidade injetado diretamente no cabedal, biqueira de composite, resistente à absorção de energia na região do calcanhar e à passagem de corrente elétrica. Restrição: PARA TRABALHOS COM BAIXA TENSÃO (ATÉ 500 V) EM AMBIENTE SECO. Certificado de Aprovação: 34550'

elif item == 'Óculos Proteção Carbografite Pro Vision Incolor | R$ 7,77 - 003432':
    FormularioRegistro['CODIGO'].Valor = '003432'
    FormularioRegistro['CA'].Valor = '6942'
    FormularioRegistro['DESCRICAO'].Valor = 'Óculos de segurança constituído de armação e visor confeccionados em uma única peça de policarbonato com meia borda superior e meia borda lateral, hastes tipo espátula confeccionadas do mesmo material da armação com seis fendas fixadas à armação através de pinos plásticos. Certificado de Aprovação: 6942'

elif item == 'Óculos Proteção Libus Argon Anti Risco Incolor | R$ 6,47 - 033504':
    FormularioRegistro['CODIGO'].Valor = '033504'
    FormularioRegistro['CA'].Valor = '35765'
    FormularioRegistro['DESCRICAO'].Valor = 'Óculos de segurança, constituídos de um arco de material plástico preto com um pino central e uma fenda em cada extremidade, utilizadas para o encaixe de um visor de policarbonato na cor incolor, com apoio nasal e proteção lateral injetados do mesmo material, com um orifício na parte frontal superior e uma fenda em cada extremidade para o encaixe no arco. O arco possui borda superior com meia-proteção nas bordas. As hastes, do tipo espátula, são confeccionadas do mesmo material do arco e são compostas de duas peças; uma semi-haste vazada, com uma das extremidades fixadas ao arco por meio de parafuso metálico e outra semi-haste com um pino plástico em uma das extremidades e que se encaixa na semi-haste anterior e que permite o ajuste do tamanho. Certificado de Aprovação; 35765'

elif item == 'Óculos Proteção Libus Ecoline Antiembaçante Incolor | R$ 10,30 - 033509':
    FormularioRegistro['CODIGO'].Valor = '033509'
    FormularioRegistro['CA'].Valor = '36032'
    FormularioRegistro['DESCRICAO'].Valor = 'Óculos de segurança, constituídos de armação e visor confeccionado em uma única peça de policarbonato incolor, com ponte e apoio nasal injetado do mesmo material. As hastes, do tipo espátula, são confeccionadas de material plástico preto e são fixadas às extremidades do visor através de parafusos metálicos. Possui tratamento anti embaçante. Certificado de Aprovação; 36032'

elif item == 'Óculos Proteção Libus Ecoline Anti Risco Incolor | R$ 5,15 - 033508':
    FormularioRegistro['CODIGO'].Valor = '033508'
    FormularioRegistro['CA'].Valor = '36032'
    FormularioRegistro['DESCRICAO'].Valor = 'Óculos de segurança, constituídos de armação e visor confeccionado em uma única peça de policarbonato incolor com ponte e apoio nasal injetado do mesmo material. As hastes, do tipo espátula, são confeccionadas de material plástico preto e são fixadas às extremidades do visor através de parafusos metálicos. Certificado de Aprovação; 36032'

elif item == 'Óculos Proteção Sobrepor Libus Visita Cinza | R$ 7,77 - 041784':
    FormularioRegistro['CODIGO'].Valor = '041784'
    FormularioRegistro['CA'].Valor = '35763'
    FormularioRegistro['DESCRICAO'].Valor = 'Óculos de segurança constituídos de armação e visor confeccionados em uma única peça de policarbonato disponível nas cores incolor e cinza com meia borda superior, hastes tipo espátula confeccionadas do mesmo material da armação na cor cinza com seis fendas para ventilação e fixadas à armação através de pinos plásticos. Proteção dos Olhos do usuário contra impactos de partículas volantes, contra raios ultravioleta (U) e, no caso da lente de cor cinza, contra luz intensa. CA Nº 35.763'

elif item == 'Óculos Proteção Sobrepor Libus Visita Incolor | R$ 7,77 - 033513':
    FormularioRegistro['CODIGO'].Valor = '033513'
    FormularioRegistro['CA'].Valor = '36032'
    FormularioRegistro['DESCRICAO'].Valor = 'Óculos de segurança'

elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela EG 1PAR | R$ 3,36 - 053989':
    FormularioRegistro['CODIGO'].Valor = '053989'
    FormularioRegistro['CA'].Valor = '51147'
    FormularioRegistro['DESCRICAO'].Valor = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela G 1PAR | R$ 3,36 - 053988':
    FormularioRegistro['CODIGO'].Valor = '053988'
    FormularioRegistro['CA'].Valor = '51147'
    FormularioRegistro['DESCRICAO'].Valor = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela M 1PAR | R$ 3,36 - 053987':
    FormularioRegistro['CODIGO'].Valor = '053987'
    FormularioRegistro['CA'].Valor = '51147'
    FormularioRegistro['DESCRICAO'].Valor = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

elif item == 'Luva Látex Flocada Go Safety Multiuso Amarela P1PAR | R$ 3,36 - 053986':
    FormularioRegistro['CODIGO'].Valor = '053986'
    FormularioRegistro['CA'].Valor = '51147'
    FormularioRegistro['DESCRICAO'].Valor = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

elif item == 'Luva Látex Volk Slim Multiuso Forrada Amarela M | R$ 3,36 - 025338':
    FormularioRegistro['CODIGO'].Valor = '025338'
    FormularioRegistro['CA'].Valor = '51147'
    FormularioRegistro['DESCRICAO'].Valor = 'Principais características: Textura antiderrapante: Superfície externa que proporciona aderência segura. Elasticidade: Permite uma ampla gama de movimentos e destreza manual. Proteção química moderada: Barreira eficaz contra agentes químicos.'

elif item == 'Luva Poliamida Volk Tátil PU Palma e Dedos Preta M | R$ 3,40 - 025306':
    FormularioRegistro['CODIGO'].Valor = '025306'
    FormularioRegistro['CA'].Valor = '30916'
    FormularioRegistro['DESCRICAO'].Valor = 'Luva de segurança confeccionada em fibras sintéticas, revestimento da face palmar e ponta dos dedos em poliuretano (PU), punho com inserções de fibras elásticas e acabamento em fibras sintéticas. Luva para proteção contra agentes mecânicos. Certificado de Aprovação; 30916'

elif item == 'Luva Tricotada Volk Black Tractor Térmica Banho Borracha G | R$ 10,44 - 050908':
    FormularioRegistro['CODIGO'].Valor = '050908'
    FormularioRegistro['CA'].Valor = '37981'
    FormularioRegistro['DESCRICAO'].Valor = 'Luva de segurança confeccionada em fibras sintéticas e fibras naturais, revestimento de face palmar, face palmar dos dedos e ponta dos dedos em borracha vulcanizada; punho com fibras elásticas e acabamento em fibras sintéticas. CA 37981'
    
FormularioRegistro['UNIDADE'].Valor = 'UNIDADE-QUANTIDADE'
```
    - coluna CA obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna CODIGO obrigatório
  - OBS1 "Declaração" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - FAVORECIDO_COBRA "Nome do Empregado que receberá o EPI" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] obrigatório
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
  - TE_MATRICULA "Matrícula do(a) Empregado(a) que receberá o EPI" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório

### [336045] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [336046] Tarefa "Preencher Declaração"
Responsável: Favorecido Cobra (papel 277)
**ScriptInicio**
```python
##OrdemServico.Salva()
AvancaProximaAtividade = True
```

### [336047] Tarefa "Gerar FQ1333-002
"
Responsável: Favorecido Cobra (papel 277)
**ScriptInicio**
```python
OrdemServico.Salva()
AvancaProximaAtividade = True
```
- Relatorios:
  - FormatoExportacao=PDF

### [336048] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI"
Destinatário: Cliente e Gerente Posição (papel 631)
Config: ListaDestinatarios=dires@bbts.com.br; saude@bbts.com.br
ModeloComunicado: Chamado Finalizado
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
Atenciosamente,
Central de Serviços
- Relatorios:
  - FormatoExportacao=PDF

## Papéis usados
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
### papel 76: Favorecido
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Favorecido
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Favorecido)
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 398: Cliente e Favorecido
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Favorecido (PessoaOrdemServico)
### papel 631: Cliente e Gerente Posição
Tipo=Composto
- composto por: Gerente Posição do Cliente (Script)
- composto por: Cliente (PessoaOrdemServico)

## Campos customizados usados (definição global)

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA

### EQUIP_EPI — Equipamentos EPI
DataGrid RecordList → Z_00143_EQUIP_EPI.EQUIP_EPI
Colunas do registro:
- RETIRADA "Retirada" [DatePicker DateTime]
- ITEM "Item" [DropDownList String]
**ITEM.LookupScript**
```python
combobox = [
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026888 - 34',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026889 - 35',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026890 - 36',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026891 - 37',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026892 - 38',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026893 - 39',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026894 - 40',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026895 - 41',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026896 - 42',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026897 - 43',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026898 - 44',
    'Bota Marluvas 70B29CPAP Preta MMicro Bico Composite | 026899 - 45',
    'Óculos Proteção Carbografite Pro Vision Incolor | R$ 7,77 - 003432',
    'Óculos Proteção Libus Argon Anti Risco Incolor | R$ 6,47 - 033504',
    'Óculos Proteção Libus Ecoline Antiembaçante Incolor | R$ 10,30 - 033509',
    'Óculos Proteção Libus Ecoline Anti Risco Incolor | R$ 5,15 - 033508',
    'Óculos Proteção Sobrepor Libus Visita Cinza | R$ 7,77 - 041784',
    'Óculos Proteção Sobrepor Libus Visita Incolor | R$ 7,77 - 033513',
    'Luva Látex Flocada Go Safety Multiuso Amarela EG 1PAR | R$ 3,36 - 053989',
    'Luva Látex Flocada Go Safety Multiuso Amarela G 1PAR | R$ 3,36 - 053988',
    'Luva Látex Flocada Go Safety Multiuso Amarela M 1PAR | R$ 3,36 - 053987',
    'Luva Látex Flocada Go Safety Multiuso Amarela P1PAR | R$ 3,36 - 053986',
    'Luva Látex Volk Slim Multiuso Forrada Amarela M | R$ 3,36 - 025338',
    'Luva Poliamida Volk Tátil PU Palma e Dedos Preta M | R$ 3,40 - 025306',
    'Luva Tricotada Volk Black Tractor Térmica Banho Borracha G | R$ 10,44 - 050908'
]

Itens = combobox
```
- CA "CA" [TextBox Integer]
- QUANTIDADE "Quantidade" [TextBox Integer]
- UNIDADE "UNIDADE" [DropDownList String] itens: UNIDADE-QUANTIADADE
**UNIDADE.LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT UOM_CODE, UNIT_OF_MEASURE_TL || '-' || UOM_CLASS FROM LISTA_UNIDADE_MEDIDA ORDER BY UNIT_OF_MEASURE_TL")
```
- DESCRICAO "Descrição do Equipamento" [Memo String]
- CODIGO "CODIGO" [TextBox String]

### TEXT2 — TEXT2
TextBox String → CPE_CSC.TEXT2

### QUANTIDADE_ESTIMADA — Quantidade estimada
DropDownList String → CPE_CSC.QUANTIDADE_ESTIMADA
Itens: 1-5;6-10;11-15;16-20;acima de 20

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### CODIGO — Código
Memo String(2000) → CPE_ORDEM_SERVICO.CODIGO

### NUM_ITEM — Número do Ítem
TextBox String(30) → CP_ORDEM_SERVICO.NUM_ITEM

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### TEXT_1 — TEXT_1
TextBox String(1000) → CPE_CSC.TEXT_1

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### TEXT — TEXT
TextBox String(1000) → CPE_CSC.TEXT

### TE_NOME_EMPREGADO — Nome do empregado
DropDownList String → CPE_CSC.TE_NOME_EMPREGADO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
