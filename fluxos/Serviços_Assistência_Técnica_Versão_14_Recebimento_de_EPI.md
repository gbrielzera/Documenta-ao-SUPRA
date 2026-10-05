# Fluxo: Recebimento de EPI (RECEBIMENTOEPI) — versão 14
Caminho: Fluxos > Serviços Assistência Técnica Versão 14 Recebimento de EPI
XML: `XMLs para teste/Serviços_Assistência_Técnica_Versão_14_Recebimento_de_EPI.xml` | Supravizio 19.1.1 | SubProcessoId 21616 | DesenhoProcessoId 2989 | ProcessoId 31
Órgão dono: 2000004019 - DIVISAO DE APOIO A REDE DE SERVICOS | Responsável: GEORGE DOS SANTOS SILVA
Classe do subprocesso: Objetivo=Recebimento de Equipamentos de Proteção; DescricaoCliente=Recebimento de Equipamentos de Proteção (EP); CriterioChargeBack=Nenhum; RegraAutorizacao=Publico; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Recebimento de EPI; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Recebimento de EPI (RECEBIMENTOEPI); Recebimento de EPC (RECEBIMENTOEPC)

## Grafo do fluxo
- [343514] EventoIntermediarioTimer "" → [343515] Aviso para o Técnico
- [343515] EventoIntermediarioMensagem "Aviso para o Técnico" → [343516] Aviso para o gerente de grupo
- [343516] EventoIntermediarioMensagem "Aviso para o gerente de grupo" → [343517] Aviso para o gerente de centro
- [343517] EventoIntermediarioMensagem "Aviso para o gerente de centro" → [343526] Solicitar aprovação do empregado
- [343518] EventoFinal "" {Cliente} → (fim)
- [343519] EventoIntermediarioMensagem "Aviso recebimento de EPI" → [343527] Chamado Finalizado - Recebimento de EPI
- [343521] EventoInicial "" → [343523] Preencher Declaração
- [343522] EventoFinal "" → (fim)
- [343523] Tarefa "Preencher Declaração" {Favorecido Cobra} → [343526] Solicitar aprovação do empregado
- [343524] Tarefa "Gerar FQ1333-002
" {Favorecido Cobra} → [343525] Chamado Finalizado - Recebimento de EPI
- [343525] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI" → [343519] Aviso recebimento de EPI
- [343526] Tarefa "Solicitar aprovação do empregado" {Favorecido Cobra} → [343514]  | [G77697] Aprovado?
- [343520] EventoIntermediarioMensagem "OS reprovada" → [343522] 
- [343527] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI" → [343528] Chamado Finalizado - Recebimento de EPI
- [343528] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI" → [343518] 
- [G77697] Gateway "Aprovado?" → «Aprovado» [343524] Gerar FQ1333-002
 | «Reprovado» [343520] OS reprovada

## Gateways
### [G77697] Aprovado? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR")
```
- alternativa → [343524] Gerar FQ1333-002
: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [343520] OS reprovada: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [343514] EventoIntermediarioTimer ""
Config: TempoIntervalo=1440

### [343515] EventoIntermediarioMensagem "Aviso para o Técnico"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Pendência de Aprovação - DIRES
Corpo do comunicado: Prezados(as),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Comunicamos que a atividade OrdemServico.Atividade está pendente de aprovação.
 OrdemServico.Customizado.EQUIP_EPI

### [343516] EventoIntermediarioMensagem "Aviso para o gerente de grupo"
Destinatário: Gerente Superior Imediato Favorecido Cobra (papel 1301)
ModeloComunicado: Pendência de Aprovação - DIRES
Corpo do comunicado: Prezados(as),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Comunicamos que a atividade OrdemServico.Atividade está pendente de aprovação.
 OrdemServico.Customizado.EQUIP_EPI

### [343517] EventoIntermediarioMensagem "Aviso para o gerente de centro"
Destinatário: Gerente de Centro do favorecido (papel 1349)
ModeloComunicado: Pendência de Aprovação - DIRES
Corpo do comunicado: Prezados(as),
O chamado interno OrdemServico.Numero - OrdemServico.Assunto.
Comunicamos que a atividade OrdemServico.Atividade está pendente de aprovação.
 OrdemServico.Customizado.EQUIP_EPI

### [343518] EventoFinal ""
Responsável: Cliente (papel 18)
- Relatorios:
  - FormatoExportacao=PDF

### [343519] EventoIntermediarioMensagem "Aviso recebimento de EPI"
Destinatário: Favorecido Cobra (papel 277)
ModeloComunicado: Chamado Finalizado - Recebimento de EPI
Corpo do comunicado: Prezado(a) Gestor(a),
Informamos que o(a) empregado(a) OrdemServico.Customizado.FAVORECIDO_COBRA recebeu os equipamentos de proteção individual descritos no documento em anexo e confirmou o recebimento através da ordem de serviço número OrdemServico.Numero .
Atenciosamente,
Central de Serviços
- Relatorios:
  - FormatoExportacao=PDF

### [343521] EventoInicial ""
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
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
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
    FormularioRegistro['CA'].Valor = ''
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
```
    - coluna CA obrigatório
    - coluna QUANTIDADE obrigatório
    - coluna CODIGO obrigatório
  - TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] obrigatório
  - TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO]

### [343522] EventoFinal ""
Config: TipoFinalizacao=NaoRealizado

### [343523] Tarefa "Preencher Declaração"
Responsável: Favorecido Cobra (papel 277)
**ScriptInicio**
```python
##OrdemServico.Salva()
AvancaProximaAtividade = True
```

### [343524] Tarefa "Gerar FQ1333-002
"
Responsável: Favorecido Cobra (papel 277)
**ScriptInicio**
```python
OrdemServico.Salva()
AvancaProximaAtividade = True
```
- Relatorios:
  - FormatoExportacao=PDF

### [343525] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI"
Destinatário: Favorecido Cobra e Gerente (papel 1281)
Config: ListaDestinatarios=dires@bbts.com.br;saude@bbts.com.br
ModeloComunicado: Chamado Finalizado
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
Atenciosamente,
Central de Serviços
- Relatorios:
  - FormatoExportacao=PDF

### [343526] Tarefa "Solicitar aprovação do empregado"
Responsável: Favorecido Cobra (papel 277)
Config: Codigo=APROVAR
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovar Recebimento de EPIs; ReenvioEmailAprovacao=24
  - (aprovação) OBS1 " Declaração" [Memo String(2000) → CPE_CONTRATOS.OBS1]
  - (aprovação) EQUIP_EPI "Equipamentos EPI" [DataGrid RecordList → Z_00143_EQUIP_EPI.EQUIP_EPI] — PermiteModificarAprovado=true
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] — PermiteModificarAprovado=true
  - (aprovação) TE_FUNCAO "Função" [TextBox String → CPE_CSC.TE_FUNCAO] — PermiteModificarAprovado=true
  - (aprovação) TE_CARGO "Cargo" [TextBox String → CPE_CSC.TE_CARGO] — PermiteModificarAprovado=true
  - (aprovação) FAVORECIDO_COBRA "Colaborador BBTS" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA] — PermiteModificarAprovado=true
  - aprovador: Favorecido Cobra (Unico)
  - relatório: FormatoExportacao=PDF; RotuloLink=FQ1333-002: FICHA DE CONTROLE E ENTREGA DE EPI
- Relatorios:
  - FormatoExportacao=PDF

### [343520] EventoIntermediarioMensagem "OS reprovada"
Destinatário: Cliente e Favorecido (papel 398)
ModeloComunicado: Chamado cancelado
Corpo do comunicado: Prezado(a),
O chamado OrdemServico.Numero - OrdemServico.Assunto foi cancelado. Verifique o motivo abaixo:
Motivo: Complemento2 
Para mais informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [343527] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI"
Destinatário: Gerente Superior Imediato Favorecido Cobra (papel 1301)
ModeloComunicado: Chamado Finalizado
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
Atenciosamente,
Central de Serviços

### [343528] EventoIntermediarioMensagem "Chamado Finalizado - Recebimento de EPI"
Destinatário: Gerente de Centro do favorecido (papel 1349)
ModeloComunicado: Chamado Finalizado
Corpo do comunicado: Prezado(a), OrdemServico.Customizado.FAVORECIDO_COBRA 
Informamos que a Ordem de Serviço nº OrdemServico foi concluída com sucesso!
Atenciosamente,
Central de Serviços

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
### papel 1301: Gerente Superior Imediato Favorecido Cobra
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
gestor = favorecidoBBTec.ObtemChefia(False)

if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor

Atores.Adiciona(gestor, "Gerente do Imediato Favorecido")
```
### papel 1349: Gerente de Centro do favorecido
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
subordinado = OrdemServico.GetCustom("FAVORECIDO_COBRA")
 
gestor = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL As CargoPessoa, PESSOA1.NOME As NomeGestor, CP_PESSOA1.CARGO_FUNCIONAL As CargoGestor, PESSOA2.NOME As NomeGestorDoGestor, CP_PESSOA2.CARGO_FUNCIONAL As CargoGestorDoGestor, SUBORDINADO.NOME As NomeSubordinado, CP_SUBORDINADO.CARGO_FUNCIONAL As CargoSubordinado, PESSOA1.ID_PESSOA From PESSOA Left Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Left Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Left Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = ORGAO.ID_GESTOR Left Join CP_PESSOA CP_PESSOA1 On CP_PESSOA1.ID_PESSOA = PESSOA1.ID_PESSOA Left Join ORGAO ORGAO1 On ORGAO1.ID_ORGAO = PESSOA1.ID_ORGAO Left Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = ORGAO1.ID_GESTOR Left Join CP_PESSOA CP_PESSOA2 On CP_PESSOA2.ID_PESSOA = PESSOA2.ID_PESSOA Left Join ORGAO ORGAO2 On ORGAO2.ID_GESTOR = PESSOA.ID_PESSOA Left Join PESSOA SUBORDINADO On SUBORDINADO.ID_ORGAO = ORGAO2.ID_ORGAO Left Join CP_PESSOA CP_SUBORDINADO On CP_SUBORDINADO.ID_PESSOA = SUBORDINADO.ID_PESSOA Where SUBORDINADO.ID_PESSOA = '"+OrdemServico['FAVORECIDO_COBRA'].ToString()+"'")
 
if gestor.Rows.Count != 0 or gestor.Rows.Count != None:
    for i in gestor.Rows:
        id_gestor = Convert.ToInt32(i['ID_PESSOA'])
    gtor = Pessoa.Carrega(id_gestor)
    Atores.Adiciona(gtor)
```
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 1281: Favorecido Cobra e Gerente
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

    
gestorMatricula = str(OrdemServico.GetCustom('MATRICULA'))
 
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + gestorMatricula + "'")        
 
idAnalista = 0
 
for row in lista.Rows:    
 
    idAnalista = row['ID_PESSOA']
```
### papel 398: Cliente e Favorecido
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Favorecido (PessoaOrdemServico)

## Campos customizados usados (definição global)

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### OBS1 — Observação1
Memo String(2000) → CPE_CONTRATOS.OBS1
Descrição: Informe

### FAVORECIDO_COBRA — Colaborador BBTS
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_COBRA
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM cp_pessoa cp inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE 1=1 and (p.ativo = 'Sim' or p.ativo = 'Nao') order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

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

### TE_CARGO — Cargo
TextBox String → CPE_CSC.TE_CARGO

### TE_FUNCAO — Função
TextBox String → CPE_CSC.TE_FUNCAO

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
