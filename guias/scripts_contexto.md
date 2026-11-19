# Scripts IronPython — contexto por tipo de script (extraído dos fluxos reais)
Caminho: Guias > Scripts > Contexto por tipo

Gerado por tools/guias.py a partir dos scripts distintos de todos os XMLs. Os números são a quantidade de scripts distintos que usam o identificador: é evidência de uso real, não a API completa. A documentação oficial cobre pouco destes objetos; quando houver página, ela está indicada em guias/scripts.md.

## Membros mais usados por objeto
- **OrdemServico**: GetCustom (176), Numero (175), ResponsavelId (105), Servico (91), Salva (62), SetCustom (49), Id (44), AdicionaComentario (36), Cliente (34), Carrega (34), PossuiAprovacao (32), ClienteId (29), Nova (28), Favorecido (27), PossuiItem (22), Atividade (18), ObtemItem (15), AdicionaLinhaRegistro (14), ObtemMotivoReprovacao (14), ModificaCampoFormularioVisivel (14), ObtemMotivoGateway (11), ModificaCampoFormularioHabilitado (10), Assunto (9), Responsavel (8), IniciaSubProcesso (7), DataHoraCriacao (7), Justificativa (5), DescricaoDetalhada (5), ServicoId (5), CancelaAprovacao (4), NumeroSistema (4), MotivoCancelamento (4), ItensAnexados (3), ObtemAssociadasComoAlvo (2), DesenhoProcesso (2), OcorrenciaPrincipalId (2), AvancaAtividade (1), FinalizadorId (1), FavorecidoId (1), IniciaAprovacao (1)
- **Formulario["CAMPO"]**: Valor (269), Visivel (232), Habilitado (229), Itens (83)
- **DB**: ExecuteDataTable (522), ExecuteScalar (66), ExecuteNonQuery (36)
- **Pessoa**: Carrega (147)
- **Utils**: ExecuteDataTable (81), LogError (23), ExecuteScalar (21), LogInformation (18), LogInfo (3), IF (1)
- **FormularioRegistro["COLUNA"]**: Valor (51), Habilitado (32), Itens (16), Visivel (13), Valoragencias (1)
- **Formulario**: ExibeMensagem (68), Controles (12)
- **Mensagem**: Complemento (35), Assunto (19), Destinatarios (17), Corpo (4), Remetente (2)
- **Servico**: Carrega (52)
- **Atores**: Adiciona (44), Add (1)
- **Criticas**: AdicionaPendencia (41), AdicionaAviso (1)
- **Controle**: Valor (25), Visivel (2), Habilitado (2)
- **Orgao**: Carrega (24)
- **Ocorrencia**: Salva (1), Carrega (1)

## LookupScript — 378 scripts distintos
Onde: campo customizado (DropDownList/SearchList/DataGrid): script de recuperação de opções; preenche `Itens`
Identificadores de contexto: Itens (355), DB (307), OrdemServico (41), Pessoa (13)
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
Itens = DB.ExecuteDataTable("SELECT ID_CIDADE FROM CIDADE_V")
```
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
Itens = DB.ExecuteDataTable("SELECT to_char(pr.id_criterio) as id_criterio, pr.item, pr.pontuacao, pr.peso FROM tb_priorizacao pr where pr.descricao = 'IMAGEM'")
```
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT(STATE) as UF FROM ps_BBTS_ETAPA_CON2") #where BBTS_VAGA = '" + FormularioRegistro["CARGO"].Valor + "'")

#Itens = DB.ExecuteDataTable("select ID_ESTADO, DESCRICAO from ESTADO_V where ID_PAIS = 'BRA'")
#FormularioRegistro["NUM_NOTA_FISCAL"].Itens
```

## ScriptModificado — 296 scripts distintos
Onde: campo de formulário: executa quando o valor do campo muda (formulário dinâmico)
Identificadores de contexto: Formulario (207), OrdemServico (62), FormularioRegistro (56), Pessoa (45), Utils (35), DB (29), Controle (21), Orgao (11), Culture (10), Texto (10), OleDbDataAdapter (9), OleDbConnection (9), DayOfWeek (9)
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
#OrdemServico.SetCustom("SCR", Formulario["SCR_PRESTADOR"].Valor)
```
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
import System


Formulario["VALOR_DISTANCIA"].Habilitado = False

valorTotal = 0

distancia = Formulario["PREVISAO_DISTANCIA_KM"].Valor
valorTotal = distancia * 1.30 


Formulario["VALOR_DISTANCIA"].Valor = valorTotal
#OrdemServico["VALOR_DISTANCIA"] = valorTotal
#
```
Exemplo (de Nova_Estruturação_de_Negócios_Versão_30_Portal_de_Estruturação_de_Negócios):
```python
if Formulario["NN_CANCELA"].Valor == 'Sim':
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = True
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["Justificativa"].Visivel = True
    Formulario["Justificativa"].Valor = None
else:
    Formulario["NN_MOTIVO_CANCELAMENTO"].Valor = None
    Formulario["NN_MOTIVO_CANCELAMENTO"].Visivel = False
    Formulario["Justificativa"].Valor = None
    Formulario["Justificativa"].Visivel = False

#OrdemServico.Salva()
```

## ScriptFormCarregado — 155 scripts distintos
Onde: atividade: executa ao carregar o formulário da atividade
Identificadores de contexto: Formulario (147), OrdemServico (63), Pessoa (24), Utils (13), DB (12), Texto (9), Fornecedor (6), Contrato (5), PreencherCampoPessoa (5), SqlTexto (5), Servico (5), PrecifObtemCronogramaAtividade (4), DesabilitarCampo (3), PreencherCampo (3), Empresa (3), DefinirVisibilidade (3)
Exemplo (de Comunicação_de_Acidente_de_Trabalho_-_CAT_Versão_1_Comunicação_de_Acidente_de_Trabalho_-_CAT):
```python
OrdemServico.ModificaCampoFormularioVisivel('REG_POL1', False)
```
Exemplo (de Administração_-_Contratos_Versão_44_Solicitar_reserva_de_DGCOs):
```python
from Venki.Supravizio.Recurso.Custom import Fornecedor
from Venki.Supravizio.Recurso.Custom import Pessoa
Formulario['COMBOBOX1'].Itens = 'Fornecedor;Cliente'
Formulario['JURIDICA_FISICA'].Valor = 'Pessoa Jurídica'
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

## ScriptInicio — 129 scripts distintos
Onde: atividade: executa quando a atividade inicia (evento Inicialização)
Identificadores de contexto: OrdemServico (122), DB (76), HttpClient (57), MediaTypeWithQualityHeaderValue (57), AuthenticationHeaderValue (57), JsonConvert (57), StringContent (56), ServicePointManager (53), SecurityProtocolType (53), AvancaProximaAtividade (48), Query (40), Pessoa (18), Utils (13), Orgao (8), Contrato (8), URL_OS_SALVAR (7), Processo (6), Formulario (5), Fornecedor (5), Texto (4), LimparGridSubprocesso (3), ValorLinha (3), RegistrarLog (3), Pesquisa (3), JObject (3)
Exemplo (de Financeiro_-_Faturamento_de_Clientes_Versão_20_Faturamento_de_Clientes_-_Emissão_de_Notas_Fiscais):
```python
OrdemServico.ModificaCampoFormularioVisivel('NUM_DOCU', True)
```
Exemplo (de Administração_-_Contratos_Versão_44_Inserir_Documentos_Contratuais_no_Sisccon):
```python
correcoes = OrdemServico.ObtemMotivoReprovacao('VERIFICAROC').ToString()
OrdemServico.SetCustom('OBS4', correcoes)
AvancaProximaAtividade = True
```
Exemplo (de Serviços_Assistência_Técnica_Versão_12_Recebimento_de_EPI):
```python
campos = ["CODIGO", "DESCRICAO_DETALHADA", "NUM_ITEM", "QUANTIDADE_ESTIMADA", "TE_CARGO", "TE_MATRICULA", "TE_NOME_EMPREGADO", "TE_UOR", "TEXT", "TEXT_1", "TEXT2"]

for i in campos:
    OrdemServico.ModificaCampoFormularioHabilitado(i, False)
```

## Source — 121 scripts distintos
Onde: módulo da Biblioteca de Scripts (funções reutilizáveis; fonte em catalogo/biblioteca/)
Identificadores de contexto: DB (84), OrdemServico (60), Pessoa (52), Servico (51), JsonConvert (49), Utils (36), HttpClient (32), MediaTypeWithQualityHeaderValue (30), JArray (28), FASE (27), JValue (27), Tecnico (27), AuthenticationHeaderValue (25), ITERACAO (22), JObject (20), NUMERO_OC (17), ID_OCORRENCIA (13), StringContent (12), File (12), Dictionary (12), NormalizationForm (9), Erro (7), DATA_PREVISTA_FIM (6), DATA_PREVISTA_INICIO (6), ESFORCO_PREVISTO_INICIO (6)
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

## ExpressaoComparacaoDecision — 91 scripts distintos
Onde: gateway: expressão cujo resultado é comparado com cada alternativa
Identificadores de contexto: OrdemServico (89)
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
OrdemServico["SAIDA"].Date.AddDays(-29) <= DateTime.Now.Date
```
Exemplo (de Administração_-_Contratos_Versão_44_Inserir_Documentos_Contratuais_no_Sisccon):
```python
from Venki.Supravizio.Processo.Custom import Atividade
OrdemServico["TIPO_ATIVIDADE"] == "Atividade Fim"
```
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
OrdemServico['TIPO_DESLOCAMENTO'] == "Viagem - Assistência Técnica" or OrdemServico['TIPO_DESLOCAMENTO'] == "Treinamento - Assistência Técnica"
```

## ScriptEvento — 68 scripts distintos
Onde: evento intermediário de mensagem: ajusta a `Mensagem` antes do envio
Identificadores de contexto: OrdemServico (65), Mensagem (50), HttpClient (27), MediaTypeWithQualityHeaderValue (27), JsonConvert (27), URL_ALERTA (27), AuthenticationHeaderValue (27), ServicePointManager (27), StringContent (27), SecurityProtocolType (27), Solicitante (11), Pessoa (11), DB (9), MM (8), TipoSolicitacao (7), Reembolso (7), DataMesReferencia (5), DATA_PAGAMENTOdd (5), ValorInformado (5), DEP_FAVORECIDO_COBRA (5), Dependente (5), Fornecedor (4), Utils (4), Items_solicitados (3), Contrato (2)
Exemplo (de Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores):
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("INSBAS")
```
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("RESERVANAOREALIZADA")
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_84_Apoio_Psicológico):
```python
#consultaLista = DB.ExecuteDataTable("select agendamento.DATA, agendamento.HORA from Z_00143_AGENDAMENTO_DATA_HORA_PSICO agendamento where ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
#
#respostaVerificacao = ""
#
#for agendamento in consultaLista.Rows:
#    respostaVerificacao = respostaVerificacao+"<tr><td>"+agendamento["DATA"].ToString("dd/MM/yyyy")+"</td>"+"<td>"+agendamento["HORA"].ToString()+"</td></tr>"
#    
#    
#Mensagem.Complemento1 = "<table><tr><th>Data</th><th>Hora</th></tr>"+respostaVerificacao+"</table>"
```

## ScriptFim — 67 scripts distintos
Onde: atividade: executa quando a atividade termina
Identificadores de contexto: OrdemServico (62), DB (50), HttpClient (48), MediaTypeWithQualityHeaderValue (48), JsonConvert (48), AuthenticationHeaderValue (48), StringContent (48), ServicePointManager (46), SecurityProtocolType (46), Processo (6), Pessoa (4), Pesquisa (3), Fornecedor (2)
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

## ScriptSelecaoAtores — 45 scripts distintos
Onde: papel customizado por script: adiciona pessoas em `Atores`
Identificadores de contexto: Ator (45), Atores (45), OrdemServico (42), Pessoa (38), DB (14), Utils (6), Orgao (5)
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
Exemplo (de Administração_-_Contratos_Versão_44_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_):
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
gestor = OrdemServico.Responsavel.ObtemChefia(False)

# se for um diretor ou presidente (mudar os identificadores e relacionar todos)
if gestor.Id == 4458 or gestor.Id == 4459 or gestor.Id == 4460 or gestor.Id == 4461 or gestor.Id == 3805 or gestor.Id == 5313 or gestor.Id == 5457 or gestor.Id == 5903 or gestor.Id == 13787:
    gestor = Pessoa.Carrega(1194)

Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Responsavel.ToString())
```

## ValorComparacaoDecision — 42 scripts distintos
Onde: alternativa do gateway: valor comparado com a expressão do gateway
Exemplo (de Administração_-_Contratos_Versão_48_Projeto_Básico_Simplificado_Eletrônico_PBEE):
```python
3
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_84_Apoio_Psicológico):
```python
"Não"
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_84_Apoio_Psicológico):
```python
"AGENDAMENTOPSICO"
```

## ScriptValidacao — 42 scripts distintos
Onde: atividade: valida antes de avançar; pendências impedem a transição
Identificadores de contexto: OrdemServico (39), Criticas (35), DB (11), Utils (6), Pessoa (6), Atividade (3), Evento (2)
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

## ScriptConfirmado — 6 scripts distintos
Onde: campo/registro de formulário: executa ao confirmar a edição
Identificadores de contexto: Formulario (5), OrdemServico (4), Cancela (4), Utils (3), FormularioRegistro (3), Registro (2)
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
Exemplo (de Administração_-_Bens_Patrimoniais_Versão_38_Transferência_de_Bens_Patrimoniais):
```python
if (OrdemServico.Servico.Sigla == "TRANSFBENFUNCMSMUOR"):
    if ( Registro["RESPONSAVEL"] == None):
        Formulario.ExibeMensagem("O campo responsável é obrigatório")
        Cancela = True
```

## Regra — 6 scripts distintos
Onde: iniciador por regra/temporizador: fórmula que decide a geração de ocorrências
Identificadores de contexto: OrdemServico (4), DB (2)
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Prestação_de_Contas_-_Deslocamento):
```python
OrdemServico["FUNCAO_DESLOCAMENTO"] != "GERENTE EXECUTIVO" and OrdemServico["RETORNO_DIA"] <= DateTime.Now
```
Exemplo (de Administração_-_Passagens_Aéreas_e_ou_Hospedagem_Versão_39_Deslocamento_a_Serviço):
```python
DateTime.Now.Date.AddDays(5) >= OrdemServico["SAIDA"]
#DateTime.Now.Date <= OrdemServico["SAIDA"].Date.AddDays(-6)
#DateTime.Now() > OrdemServico.DataHoraSolicitacao.AddDays(27)
```
Exemplo (de Reembolsos__I.A_Versão_1_Reembolso_-_Iniciativa_IA):
```python
DB.ExecuteDataTable("SELECT M.STATUS FROM SV_MESSAGE M INNER JOIN OCORRENCIA O ON O.ID_OCORRENCIA = M.ID_OBJECT WHERE O.ID_OCORRENCIA = '" + OrdemServico.Id.ToString() + "'").Rows.Count > 2
```

## ExpressaoCalculo — 1 scripts distintos
Onde: expressão de cálculo de campo
Exemplo (de Administração_-_Contratos_Versão_44_Publicação_no_DOU):
```python
Utils.IF(OrdemServico.Cliente.PerfilCliente != None and OrdemServico.Cliente.PerfilClienteId == 1, 1, 2)
```

## ScriptAdicionado — 1 scripts distintos
Onde: campo de registro (grid): executa ao adicionar linha
Exemplo (de Lista_de_Treinamento_Versão_5_Lista_de_Treinamento):
```python
NovoRegistro['MULTIPLICADOR2'] = 'N/A'
```
