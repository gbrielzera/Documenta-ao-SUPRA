# Scripts IronPython — contexto por tipo de script (extraído dos fluxos reais)
Caminho: Guias > Scripts > Contexto por tipo

Gerado por tools/guias.py a partir dos scripts distintos de todos os XMLs. Os números são a quantidade de scripts distintos que usam o identificador: é evidência de uso real, não a API completa. A documentação oficial cobre pouco destes objetos; quando houver página, ela está indicada em guias/scripts.md.

## Membros mais usados por objeto
- **OrdemServico**: GetCustom (206), Numero (185), Servico (115), ResponsavelId (105), Salva (72), SetCustom (61), Id (52), AdicionaComentario (47), Cliente (40), Favorecido (38), PossuiAprovacao (38), Carrega (35), ClienteId (32), Nova (29), PossuiItem (25), Atividade (22), AdicionaLinhaRegistro (20), ObtemItem (19), ObtemMotivoReprovacao (17), ModificaCampoFormularioVisivel (15), Assunto (14), ModificaCampoFormularioHabilitado (13), IniciaSubProcesso (11), ObtemMotivoGateway (11), Responsavel (8), DescricaoDetalhada (7), DataHoraCriacao (7), MotivoCancelamento (6), Justificativa (5), ServicoId (5), CancelaAprovacao (4), NumeroSistema (4), ItensAnexados (3), ClasseSubProcesso (3), ObtemAssociadasComoAlvo (2), DesenhoProcesso (2), OcorrenciaPrincipalId (2), SubProcesso (2), AvancaAtividade (1), FinalizadorId (1)
- **Formulario["CAMPO"]**: Valor (307), Habilitado (263), Visivel (262), Itens (90)
- **DB**: ExecuteDataTable (544), ExecuteScalar (87), ExecuteNonQuery (38)
- **Pessoa**: Carrega (171)
- **Utils**: ExecuteDataTable (98), LogError (24), ExecuteScalar (24), LogInformation (20), LogInfo (3), IF (1)
- **FormularioRegistro["COLUNA"]**: Valor (61), Habilitado (32), Itens (16), Visivel (13), Valoragencias (1)
- **Mensagem**: Complemento (42), Assunto (29), Destinatarios (20), Corpo (7), Remetente (2)
- **Formulario**: ExibeMensagem (78), Controles (12)
- **Servico**: Carrega (54)
- **Atores**: Adiciona (51), Add (1)
- **Criticas**: AdicionaPendencia (49), AdicionaAviso (1)
- **Controle**: Valor (32), Habilitado (2), Visivel (2)
- **Orgao**: Carrega (27)
- **Ocorrencia**: Salva (1), Carrega (1)

## LookupScript — 382 scripts distintos
Onde: campo customizado (DropDownList/SearchList/DataGrid): script de recuperação de opções; preenche `Itens`
Identificadores de contexto: Itens (359), DB (307), OrdemServico (41), Pessoa (14)
Exemplo (de Aceite_De_Políticas_Versão_1_Aceite_POL900_-_Política_de_Compliance_e_Antissuborno):
```python
Itens = DB.ExecuteDataTable("SELECT ID_CIDADE FROM CIDADE_V")
```
Exemplo (de Aceite_De_Políticas_Versão_1_Aceite_POL900_-_Política_de_Compliance_e_Antissuborno):
```python
Itens = DB.ExecuteDataTable("SELECT to_char(pr.id_criterio) as id_criterio, pr.item, pr.pontuacao, pr.peso FROM tb_priorizacao pr where pr.descricao = 'IMAGEM'")
```
Exemplo (de Aceite_De_Políticas_Versão_1_Aceite_POL900_-_Política_de_Compliance_e_Antissuborno):
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT(STATE) as UF FROM ps_BBTS_ETAPA_CON2") #where BBTS_VAGA = '" + FormularioRegistro["CARGO"].Valor + "'")

#Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")
#FormularioRegistro["NUM_NOTA_FISCAL"].Itens
```

## ScriptModificado — 335 scripts distintos
Onde: campo de formulário: executa quando o valor do campo muda (formulário dinâmico)
Identificadores de contexto: Formulario (233), OrdemServico (83), FormularioRegistro (66), Pessoa (57), Utils (46), DB (37), Controle (28), Orgao (11), OleDbDataAdapter (10), OleDbConnection (10), Culture (10), Texto (10), DayOfWeek (9)
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
#OrdemServico.SetCustom("SCR", Formulario["SCR_PRESTADOR"].Valor)
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_93_Reembolso):
```python
if FormularioRegistro['TIPO'].Valor == 'Medicamentos que atuam como agentes Metabólicos Increnoativos: Ozempic, Mounjaro, entre outros, vide NI103':
    FormularioRegistro['QUANTIDADE'].Habilitado = True
else:
    FormularioRegistro['QUANTIDADE'].Habilitado = False
```
Exemplo (de Administração_-_Contratos_Versão_44_Inserir_Documentos_Contratuais_no_Sisccon):
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario['FISICA_JUDIRICA'].Valor == "Pessoa Jurídica":
    Formulario['CSC_CPF'].Habilitado = False
    Formulario['CSC_CPF'].Visivel = False
    Formulario['CNPJ'].Habilitado = True
    Formulario['CNPJ'].Visivel = True

if Formulario['FISICA_JUDIRICA'].Valor != "Pessoa Jurídica":
    Formulario['CSC_CPF'].Habilitado = True
    Formulario['CSC_CPF'].Visivel = True
    Formulario['CNPJ'].Habilitado = False
    Formulario['CNPJ'].Visivel = False
```

## ScriptFormCarregado — 183 scripts distintos
Onde: atividade: executa ao carregar o formulário da atividade
Identificadores de contexto: Formulario (172), OrdemServico (73), Pessoa (27), Utils (16), DB (13), Texto (9), Contrato (7), Fornecedor (7), PreencherCampoPessoa (5), SqlTexto (5), Servico (5), Empresa (4), PrecifObtemCronogramaAtividade (4)
Exemplo (de Comunicação_de_Acidente_de_Trabalho_-_CAT_Versão_1_Comunicação_de_Acidente_de_Trabalho_-_CAT):
```python
OrdemServico.ModificaCampoFormularioVisivel('REG_POL1', False)
```
Exemplo (de Financeiro_-_Serviços_Gerais_Versão_22_Financeiro_-_Contas_a_Pagar):
```python
#Formulario["OBS1"].Visivel = True
#Formulario["OBS1"].Habilitado = True

#Formulario["OBSERVACAO"].Visivel = True
#Formulario["OBSERVACAO"].Habilitado = True


Formulario["Justificativa"].Habilitado = False
```
Exemplo (de Administração_-_Contratos_Versão_48_Projeto_Básico_Simplificado_Eletrônico_PBEE):
```python
Formulario["VALOR_REFERENCIAL"].Habilitado = False
Formulario["PARECER_QUALIF"].Habilitado = False
Formulario["CONTA_ORCAMENTARIA"].Habilitado = False
Formulario["CODIGO_ITEM"].Habilitado = False
Formulario["SIM_NAO14"].Visivel = False
#Formulario["CODIGO_ITEM"].Visivel = False
#Formulario["VALOR_REFERENCIAL"].Visivel = False
Formulario['CSC_ESCOLARIDADE'].Visivel = True
Formulario['UOR'].Visivel = True
Formulario['UOR'].Habilitado = True
```

## ScriptInicio — 159 scripts distintos
Onde: atividade: executa quando a atividade inicia (evento Inicialização)
Identificadores de contexto: OrdemServico (143), DB (85), AvancaProximaAtividade (61), MediaTypeWithQualityHeaderValue (58), AuthenticationHeaderValue (58), HttpClient (58), JsonConvert (58), StringContent (56), ServicePointManager (53), SecurityProtocolType (53), Query (40), Pessoa (23), Utils (16), Orgao (10), Contrato (9), URL_OS_SALVAR (7), Atividade (7), Fornecedor (6), Processo (6), Formulario (5), Texto (4), RegistrarLog (3), LimparGridSubprocesso (3), ValorLinha (3), Pesquisa (3)
Exemplo (de Financeiro_-_Faturamento_de_Clientes_Versão_20_Faturamento_de_Clientes_-_Emissão_de_Notas_Fiscais):
```python
OrdemServico.ModificaCampoFormularioVisivel('NUM_DOCU', True)
```
Exemplo (de Contrato_com_Clientes_Versão_30_Assinatura_de_Novos_Contratos_e_Aditivos_com_Clientes -_(Uso_exclusivo_da_GEREL)''):
```python
OrdemServico.SetCustom('CSC_NUMERO', OrdemServico.GetCustom('NUM_CONTRATO'))
#OrdemServico.SetCustom('OBJETO_CONTRATACAO', 'PRJ_OBJETO')
```
Exemplo (de Administração_-_Contratos_Versão_44_Solicitar_reserva_de_DGCOs):
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
OrdemServico.SetCustom('NOME_DAS', OrdemServico.Numero.ToString())
OrdemServico.ModificaCampoFormularioHabilitado('NOME_DAS', False)
OrdemServico.ModificaCampoFormularioVisivel('NOME_DAS', False)
OrdemServico.SetCustom('JURIDICA_FISICA', 'Pessoa Jurídica')

AvancaProximaAtividade = True
```

## Source — 122 scripts distintos
Onde: módulo da Biblioteca de Scripts (funções reutilizáveis; fonte em catalogo/biblioteca/)
Identificadores de contexto: DB (85), OrdemServico (61), Pessoa (53), Servico (52), JsonConvert (50), Utils (37), HttpClient (33), MediaTypeWithQualityHeaderValue (31), JArray (29), JValue (28), Tecnico (28), FASE (27), AuthenticationHeaderValue (26), ITERACAO (22), JObject (21), NUMERO_OC (17), ID_OCORRENCIA (13), StringContent (13), Dictionary (13), File (13), NormalizationForm (9), Erro (7), ESFORCO_PREVISTO_INICIO (6), DATA_PREVISTA_INICIO (6), DATA_PREVISTA_FIM (6)
Exemplo (de Financeiro_-_Serviços_Gerais_Versão_38_Comprovantes_de_Valores_Pagos_a_Fornecedores Gabriel):
```python
def isHoliday(day):
    holidays = DB.ExecuteDataTable("select data from feriado ")
    for holiday in holidays.rows:
        if day == holiday["data"].date:
            return True
    return False
```
Exemplo (de Financeiro_-_Serviços_Gerais_Versão_38_Comprovantes_de_Valores_Pagos_a_Fornecedores Gabriel):
```python
def cronograma_dod_aloceventual(NUMERO_OC, FASE, ITERACAO, DATA_INICIO_REAL):

    #OrdemServico.AdicionaComentario("teste" + DATA_INICIO_REAL.ToString() , False)
    
    qry = "UPDATE CRONOGRAMA_DOD SET DATA_INICIO_REAL = to_date('"+DATA_INICIO_REAL.ToString()+"','DD/MM/YYYY hh24:mi:ss') WHERE NUMERO_OC = "+NUMERO_OC.ToString()+" AND FASE = "+FASE.ToString()+" AND ITERACAO = "+ITERACAO.ToString()+ ""
    
    DB.ExecuteNonQuery(qry)
    
    presistencia = "commit"
    
    DB.ExecuteNonQuery(presistencia)
```
Exemplo (de Financeiro_-_Serviços_Gerais_Versão_38_Comprovantes_de_Valores_Pagos_a_Fornecedores Gabriel):
```python
def cronograma_dod_realiza_sub(ID_OCORRENCIA, FASE, ITERACAO, ESFORCO_REAL):
    
    qry = " UPDATE CRONOGRAMA_DOD SET DATA_FIM_REAL = to_date(to_char(sysdate, 'DD/MM/YYYY hh24:mi:ss'), 'DD/MM/YYYY hh24:mi:ss') , ESFORCO_REAL = " + ESFORCO_REAL.ToString() + " WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_realizado - " + qry  , False)

    DB.ExecuteNonQuery(qry)
    
    persistencia = "commit"
    
    DB.ExecuteNonQuery(persistencia)
```

## ExpressaoComparacaoDecision — 104 scripts distintos
Onde: gateway: expressão cujo resultado é comparado com cada alternativa
Identificadores de contexto: OrdemServico (102)
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
OrdemServico["SAIDA"].Date.AddDays(-29) <= DateTime.Now.Date
```
Exemplo (de Gestão_de_Pessoas_-_Serviços_Gerais_Versão_68_Indenização_por_Lotação_em_Base_Destacada):
```python
OrdemServico['VALOR_PRESTACAO'] == Convert.ToDecimal(0) or OrdemServico['VALOR_PRESTACAO'] == '0'
```
Exemplo (de Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores):
```python
OrdemServico.Servico.Sigla == "REGNFCDGCOMERSERSMO"
    #Formulario["Outros"].Visivel = True
    #Formulario["Outros"].Habilitado = True
```

## ScriptEvento — 78 scripts distintos
Onde: evento intermediário de mensagem: ajusta a `Mensagem` antes do envio
Identificadores de contexto: OrdemServico (75), Mensagem (60), MediaTypeWithQualityHeaderValue (27), ServicePointManager (27), URL_ALERTA (27), AuthenticationHeaderValue (27), JsonConvert (27), HttpClient (27), SecurityProtocolType (27), StringContent (27), DB (18), Pessoa (12), Solicitante (11), MM (8), Fornecedor (7), Utils (7), Reembolso (7), TipoSolicitacao (7), Contrato (6), DataMesReferencia (5), DATA_PAGAMENTOdd (5), Dependente (5), ValorInformado (5), DEP_FAVORECIDO_COBRA (5), Processo (4)
Exemplo (de Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores):
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("INSBAS")
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_84_Apoio_Psicológico):
```python
Mensagem.Complemento1 = "Devido a não confirmação do Agendamento ao Apoio psicológico, por parte do favorecido "+ OrdemServico.Cliente.Nome +", não haverá consulta."
```
Exemplo (de Solicitações_de_Serviços_Versão_29_Validar_eixo_pedagógico_e_demais_insumos):
```python
#Mensagem.Destinatarios.Add(OrdemServico["CSC_EMAIL_PESSOAL"])
Mensagem.Assunto = "Validar Eixo Pedagógico e demais insumos - Aprovado " 

motivo = OrdemServico.ObtemMotivoReprovacao("APROVAEIXO").ToString()

Mensagem.Complemento1 = "Prezados, " + OrdemServico.Cliente.Nome +"<br><Br>Gostaria de informar que, conforme solicitado, o eixo pedagógico e demais insumos não foi aprovado pelo motivo: " +  motivo.ToString() + ".<br>Gentileza realizar os ajustes solicitados e abrir nova ordem de serviço com os insumos revisados e atualizados.<br><br>Atenciosamente,<br><Br>"
```

## ScriptFim — 73 scripts distintos
Onde: atividade: executa quando a atividade termina
Identificadores de contexto: OrdemServico (66), DB (52), MediaTypeWithQualityHeaderValue (48), AuthenticationHeaderValue (48), JsonConvert (48), HttpClient (48), StringContent (48), ServicePointManager (46), SecurityProtocolType (46), Processo (6), Pessoa (5), Pesquisa (3), Fornecedor (2), Atividade (2)
Exemplo (de Gestão_de_Pessoas_-_Serviços_Gerais_Versão_68_Indenização_por_Lotação_em_Base_Destacada):
```python
OrdemServico.Servico.Sigla = 'IDENIZACAO'
OrdemServico.Salva()
```
Exemplo (de Financeiro_-_Faturamento_de_Clientes_Versão_20_Faturamento_de_Clientes_-_Emissão_de_Notas_Fiscais):
```python
linhas = OrdemServico.GetCustom('GRID_NF').Rows.Count
OrdemServico.SetCustom('NUM_DOCU', linhas.ToString())
```
Exemplo (de Contrato_com_Clientes_Versão_30_Assinatura_de_Novos_Contratos_e_Aditivos_com_Clientes -_(Uso_exclusivo_da_GEREL)''):
```python
OrdemServico.ModificaCampoFormularioHabilitado('RAZAO_SOCIAL_CLIENTE', False)
OrdemServico.ModificaCampoFormularioHabilitado('JURIDICA_FISICA', False)
OrdemServico.ModificaCampoFormularioHabilitado('CSC_CPF', False)
OrdemServico.ModificaCampoFormularioHabilitado('CNPJ', False)
```

## ScriptSelecaoAtores — 52 scripts distintos
Onde: papel customizado por script: adiciona pessoas em `Atores`
Identificadores de contexto: Atores (52), Ator (52), OrdemServico (49), Pessoa (43), DB (17), Orgao (6), Utils (6)
Exemplo (de Comunicação_de_Acidente_de_Trabalho_-_CAT_Versão_1_Comunicação_de_Acidente_de_Trabalho_-_CAT):
```python
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Favorecido)
```
Exemplo (de Administração_-_Contratos_Versão_44_Inserir_Documentos_Contratuais_no_Sisccon):
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("RESPONSAVEL_PROCESSO"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("RESPONSAVEL_PROCESSO")))

    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```
Exemplo (de Programa_Valor_Versão_15_Atualizar_Perfil-Especialidade):
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

## ValorComparacaoDecision — 51 scripts distintos
Onde: alternativa do gateway: valor comparado com a expressão do gateway
Identificadores de contexto: OrdemServico (6)
Exemplo (de Gestão_de_Pessoas_-_Trabalhador_Temporário_Versão_17_Cadastro_de_Trabalhador_Temporário-_Posto_de_Serviço_(ERP_e-ou_Peoplesoft)):
```python
OrdemServico["CSC_ACESSO_SISBB"]!=True and OrdemServico["CSC_ACESSO_VPN"]!=True and OrdemServico["CSC_ACESSO_ERP"]!=True and OrdemServico["CSC_ACESSO_WIFI"]!=True and OrdemServico["CSC_ACESSO_TOA"]!=True and OrdemServico["CSC_ACESSO_SICON"]!=True
```

## ScriptValidacao — 50 scripts distintos
Onde: atividade: valida antes de avançar; pendências impedem a transição
Identificadores de contexto: OrdemServico (47), Criticas (43), DB (16), Pessoa (6), Utils (6), Atividade (3), Evento (2)
Exemplo (de Ascensão_Profissional_e_Movimentação_de_Pessoas_Versão_69_Contratação_de_Estagiário):
```python
if OrdemServico.GetCustom("ENTREGA_DOCUMENTO") == "Parcial" :
    Criticas.AdicionaPendencia("Entrega de documentação parcial !")
```
Exemplo (de Administração_-_Contratos_Versão_44_Solicitar_reserva_de_DGCOs):
```python
sql = "select count(1) from bbts_gescon_funcionario P where p.matricula = '"+OrdemServico.Cliente["MATRICULA"].ToString()+"'"
resultado = DB.ExecuteScalar(sql)
if resultado.ToString() == '0':
    Criticas.AdicionaPendencia('O Solicitante não está devidamente cadastrado no Gescon!')
```
Exemplo (de Contrato_com_Clientes_Versão_30_Assinatura_de_Novos_Contratos_e_Aditivos_com_Clientes -_(Uso_exclusivo_da_GEREL)''):
```python
matriculaCondTitu = str(OrdemServico.GetCustom("MATRICULA_CONDUT_TITU"))
matriculaCondSup = str(OrdemServico.GetCustom("MATRICULA_CONDUT_SUP"))

if matriculaCondTitu == matriculaCondSup:
    Criticas.AdicionaPendencia('O assessor escolhido não pode assumir dois papeis no contrato!')
    
elif (matriculaCondTitu == '0' or matriculaCondTitu == 0) or (matriculaCondSup == '0' or matriculaCondSup == 0):
    Criticas.AdicionaPendencia('O assessor escolhido não pode assumir dois papeis no contrato!')
```

## ExpressaoValor — 25 scripts distintos
Onde: ValorInput de atividade (ex.: chamada de subprocesso/iniciador): expressão do valor
Identificadores de contexto: Servico (21), OrdemServico (4)
Exemplo (de Nova_Estruturação_de_Negócios_Versão_30_Assinatura_de_Contrato):
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(189)
```
Exemplo (de Administração_-_Serviços_Gerais_Versão_26_Atividade_02_Gabriel):
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega('Sigla','REQCAT')
```
Exemplo (de Contrato_com_Clientes_Versão_30_Assinatura_de_Novos_Contratos_e_Aditivos_com_Clientes -_(Uso_exclusivo_da_GEREL)''):
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CNTFATERPAR")
```

## Regra — 14 scripts distintos
Onde: iniciador por regra/temporizador: fórmula que decide a geração de ocorrências
Identificadores de contexto: OrdemServico (8), DB (5)
Exemplo (de Gestão_de_Pessoas_-_Concurso_Versão_8_Avaliação_Período_Experiência_-_GDP):
```python
DateTime.AddDays(OrdemServico["DATA_POSSE"], 85) == DateTime.Now.Date
```
Exemplo (de Gestão_de_Pessoas_-_Concurso_Versão_8_Avaliação_Período_Experiência_-_GDP):
```python
DateTime.AddDays(OrdemServico["DATA_POSSE"], 40) == DateTime.Now.Date
```
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Prestação_de_Contas_-_Deslocamento):
```python
OrdemServico["FUNCAO_DESLOCAMENTO"] != "GERENTE EXECUTIVO" and OrdemServico["RETORNO_DIA"] <= DateTime.Now
```

## ScriptConfirmado — 7 scripts distintos
Onde: campo/registro de formulário: executa ao confirmar a edição
Identificadores de contexto: Formulario (5), Cancela (4), OrdemServico (4), FormularioRegistro (3), Utils (3), Registro (2)
Exemplo (de Gestão_de_Pessoas_-_Trabalhador_Temporário_Versão_17_Cadastro_de_Trabalhador_Temporário-_Posto_de_Serviço_(ERP_e-ou_Peoplesoft)):
```python
#Formulario.ExibeMensagem(Formulario['CSC_TRABALHADOR_TEMPORARIO'].Valor.ToString()+'sdfsdfs')
```
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
if Registro["DATA_HORA_DEVOLUCAO"] < Registro["DATA_HORA_RETIRADA"]:
   Formulario.ExibeMensagem("ATENÇÃO: Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
```
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Prestação_de_Contas_-_Deslocamento):
```python
#if Registro["DATA_HORA_DEVOLUCAO"] < Registro["DATA_HORA_RETIRADA"]:
#   Formulario.ExibeMensagem("ATENÇÃO: Data/Hora da Devolução não pode ser menor que Data/Hora da Retirada!")
```

## ScriptAdicionado — 2 scripts distintos
Onde: campo de registro (grid): executa ao adicionar linha
Exemplo (de Gestão_de_Pessoas_-_Trabalhador_Temporário_Versão_17_Cadastro_de_Trabalhador_Temporário-_Posto_de_Serviço_(ERP_e-ou_Peoplesoft)):
```python
if OrdemServico.Servico.Sigla.ToString() != 'CADTRABALHADORTEMPORARIO':
    dt= OrdemServico.GetCustom("CSC_LISTA_RESP_ERP")
    mat = OrdemServico.GetCustom("CSC_TRABALHADOR_TEMPORARIO")
    if dt.Rows.Count == 0:
        #sql_erp = "select ROWNUM-1 as RECID, RESP AS MODULOS from ERP_RESP_V where MATRICULA = '3829'"
        sql_erp = "select ROWNUM as RECID, RESPONSABILIDADE AS MODULOS from ERP_RESP_V where MATRICULA = '"+mat.ToString()+"'"
        info_erp = DB.ExecuteDataTable(sql_erp)
        if info_erp.Rows.Count == 0:
            Tabela.Clear()
        else:
            for linha_x in info_erp.Rows:
                Tabela.NewRow()
                Tabela.ImportRow(linha_x)
```

## ExpressaoCalculo — 1 scripts distintos
Onde: expressão de cálculo de campo
Exemplo (de Administração_-_Contratos_Versão_44_Publicação_no_DOU):
```python
Utils.IF(OrdemServico.Cliente.PerfilCliente != None and OrdemServico.Cliente.PerfilClienteId == 1, 1, 2)
```
