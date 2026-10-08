# Scripts IronPython — contexto por tipo de script (extraído dos fluxos reais)
Caminho: Guias > Scripts > Contexto por tipo

Gerado por tools/guias.py a partir dos scripts distintos de todos os XMLs. Os números são a quantidade de scripts distintos que usam o identificador: é evidência de uso real, não a API completa. A documentação oficial cobre pouco destes objetos; quando houver página, ela está indicada em guias/scripts.md.

## Membros mais usados por objeto
- **OrdemServico**: GetCustom (119), Servico (76), Numero (37), Carrega (30), SetCustom (28), Cliente (25), Nova (25), Id (22), PossuiAprovacao (22), PossuiItem (19), Salva (16), Atividade (16), AdicionaComentario (15), ClienteId (14), ObtemItem (14), AdicionaLinhaRegistro (13), ResponsavelId (12), Favorecido (11), ModificaCampoFormularioHabilitado (10), ObtemMotivoReprovacao (9), Responsavel (8), ModificaCampoFormularioVisivel (7), IniciaSubProcesso (6), DataHoraCriacao (6), Justificativa (5), DescricaoDetalhada (5), ObtemMotivoGateway (5), MotivoCancelamento (4), Assunto (3), ItensAnexados (2), OcorrenciaPrincipalId (2), NumeroSistema (2), ServicoId (2), AvancaAtividade (1), FinalizadorId (1), SubProcesso (1), CancelaAprovacao (1), ObtemAtoresProcesso (1), Cancela (1)
- **Formulario["CAMPO"]**: Valor (158), Visivel (130), Habilitado (119), Itens (65)
- **DB**: ExecuteDataTable (375), ExecuteScalar (54), ExecuteNonQuery (33)
- **Utils**: ExecuteDataTable (51), LogError (20), ExecuteScalar (18), LogInformation (13), LogInfo (3), IF (1)
- **Pessoa**: Carrega (95)
- **FormularioRegistro["COLUNA"]**: Valor (44), Habilitado (22), Itens (9), Visivel (6), Valoragencias (1)
- **Servico**: Carrega (46)
- **Formulario**: ExibeMensagem (42), Controles (2)
- **Atores**: Adiciona (35), Add (1)
- **Mensagem**: Complemento (14), Assunto (8), Corpo (4), Destinatarios (4), Remetente (2)
- **Criticas**: AdicionaPendencia (27), AdicionaAviso (1)
- **Controle**: Valor (20)
- **Orgao**: Carrega (16)
- **Ocorrencia**: Carrega (1), Salva (1)

## LookupScript — 367 scripts distintos
Onde: campo customizado (DropDownList/SearchList/DataGrid): script de recuperação de opções; preenche `Itens`
Identificadores de contexto: Itens (345), DB (302), OrdemServico (41), Pessoa (13)
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
Itens = DB.ExecuteDataTable("SELECT ID_CIDADE FROM CIDADE_V")
```
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
Itens = DB.ExecuteDataTable(" SELECT to_char(pr.id_criterio) as id_criterio, pr.item_mensurado FROM tb_priorizacao_v2 pr where pr.categoria = 'PRAZO_ORCADO' ")
```
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
Itens = DB.ExecuteDataTable("SELECT ED.DESCRICAO FROM PESSOA INNER JOIN TB_CAD_PEC_APROVADO AP ON (PESSOA.ID_PESSOA = AP.ID_PESSOA) INNER JOIN TB_CUSTOM_EDITAL_PEC ED ON (ED.ID_EDITAL_PEC = AP.ID_EDITAL_PEC) WHERE PESSOA.ID_PESSOA = '" + OrdemServico.ClienteId.ToString() + "' ")
```

## ScriptModificado — 155 scripts distintos
Onde: campo de formulário: executa quando o valor do campo muda (formulário dinâmico)
Identificadores de contexto: Formulario (113), FormularioRegistro (43), OrdemServico (36), Pessoa (29), Utils (26), Controle (16), DB (14), Culture (10), Texto (10), Orgao (9), OleDbConnection (8), OleDbDataAdapter (8), Software (4), LimparCampo (4), Char (3), LerLinhasAba (3), ZipArchive (3), LerDocumentoXml (3), File (3), GridPossuiDGCO (3), Inteiro (3), ZipArchiveMode (3), PrimeiroFilho (3), ObterEntradaZip (3), LerXlsx (3)
Exemplo (de Administração_-_Contratos_Versão_44_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_):
```python
OrdemServico['FORNECEDOR'] = FormularioRegistro['FORNECEDOR'].Valor
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso):
```python
dt = OrdemServico.GetCustom("LISTA_NF")
if (dt.Rows.Count>=3):
    FormularioRegistro["CNPJ"].Habilitado=False
    FormularioRegistro["NUMERO_NF"].Habilitado=False
    Formulario["LISTA_MEDICAMENTOS"].Habilitado = True
    Formulario["LISTA_MEDICAMENTOS"].Visivel = True
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_88_Auxílio_Órtese,_Prótese_e_Recursos_para_Saúde_-_Reembolso):
```python
if Formulario["SIM_NAO"].Valor != None:
    Formulario["COMBOBOX"].Habilitado = True
    
if Formulario["Valor"].Valor != None:
    if Formulario["VALOR"].Valor >= 20000:
        Formulario["VALOR_TOTAL"].Valor = 20000
    elif Formulario["SIM_NAO"].Valor == "Sim":
        Formulario["VALOR_TOTAL"].Valor = 0.9 * Formulario["VALOR"].Valor
    else:
        Formulario["VALOR_TOTAL"].Valor = Formulario["VALOR"].Valor
    Formulario["VALOR_AUTORIZADO"].Valor = 0.01 * Formulario["VALOR_TOTAL"].Valor
```

## Source — 110 scripts distintos
Onde: módulo da Biblioteca de Scripts (funções reutilizáveis; fonte em catalogo/biblioteca/)
Identificadores de contexto: DB (75), OrdemServico (52), Pessoa (44), Servico (43), JsonConvert (40), Utils (30), HttpClient (28), FASE (27), MediaTypeWithQualityHeaderValue (26), Tecnico (24), JArray (23), ITERACAO (22), JValue (22), AuthenticationHeaderValue (22), JObject (18), NUMERO_OC (17), ID_OCORRENCIA (13), Dictionary (11), File (11), StringContent (10), NormalizationForm (8), Erro (7), DATA_PREVISTA_FIM (6), ESFORCO_PREVISTO_INICIO (6), DATA_PREVISTA_INICIO (6)
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

## ScriptFormCarregado — 109 scripts distintos
Onde: atividade: executa ao carregar o formulário da atividade
Identificadores de contexto: Formulario (105), OrdemServico (37), Pessoa (14), Texto (9), DB (7), Utils (7), Fornecedor (6), PreencherCampoPessoa (5), SqlTexto (5), Contrato (4), PrecifObtemCronogramaAtividade (4), DesabilitarCampo (3), PreencherCampo (3), DefinirVisibilidade (3), Atividade (2), Servico (2), Empresa (2), DefinirHabilitado (2), ExibirMensagem (2), PreencherCampoTexto (2), Processo (2)
Exemplo (de Comunicação_de_Acidente_de_Trabalho_-_CAT_Versão_1_Comunicação_de_Acidente_de_Trabalho_-_CAT):
```python
OrdemServico.ModificaCampoFormularioVisivel('REG_POL1', False)
```
Exemplo (de Base_de_Informações_Técnicas_Versão_4_Solicitação_Precificação_de_Item):
```python
Formulario['COMBOBOX__1'].Habilitado = False
Formulario['TEXT'].Habilitado = False
#Formulario['TEXT2'].Visivel = False

#Formulario['COMBOBOX'].Itens = 'BBTS MANUTENÇÃO;BBTS ATIVOS;BBTS FIEL DEPOSITÁRIO;Outro'
```
Exemplo (de Administração_-_Contratos_Versão_44_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_):
```python
Formulario['COMBOBOX_V'].Itens = '1- Não atendimento às exigências contratuais;2- Atendimento parcial às exigências contratuais;3- Pleno atendimento às exigências contratuais'

Formulario['COMBOBOX_XX'].Itens = '1- Não atendimento às exigências contratuais;2- Atendimento parcial às exigências contratuais;3- Pleno atendimento às exigências contratuais'

Formulario['TEXT'].Habilitado = False
```

## ExpressaoComparacaoDecision — 65 scripts distintos
Onde: gateway: expressão cujo resultado é comparado com cada alternativa
Identificadores de contexto: OrdemServico (65)
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
OrdemServico["SIM_NAO_100"] == 'Mandar para o time de Desenvolvimento'
```
Exemplo (de Administração_-_Contratos_Versão_44_Inserir_Documentos_Contratuais_no_Sisccon):
```python
from Venki.Supravizio.Processo.Custom import Atividade
OrdemServico["TIPO_ATIVIDADE"] == "Atividade Fim"
```
Exemplo (de Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores):
```python
OrdemServico.Servico.Sigla == "PAGFORNECSEMDGCO"
    #Formulario["Outros"].Visivel = True
    #Formulario["Outros"].Habilitado = True
```

## ScriptInicio — 62 scripts distintos
Onde: atividade: executa quando a atividade inicia (evento Inicialização)
Identificadores de contexto: OrdemServico (56), AvancaProximaAtividade (27), DB (17), Pessoa (10), Utils (7), Orgao (4), Formulario (4), Texto (4), HttpClient (4), JsonConvert (4), AuthenticationHeaderValue (4), MediaTypeWithQualityHeaderValue (4), ValorLinha (3), RegistrarLog (3), LimparGridSubprocesso (3), JObject (3), StringContent (3), PrecifObtemCronogramaAtividade (3), Inteiro (2), Fornecedor (2), Thread (2), Servico (2)
Exemplo (de Financeiro_-_Faturamento_de_Clientes_Versão_20_Faturamento_de_Clientes_-_Emissão_de_Notas_Fiscais):
```python
OrdemServico.ModificaCampoFormularioVisivel('NUM_DOCU', True)
```
Exemplo (de Contrato_com_Clientes_Versão_30_Assinatura_de_Novos_Contratos_e_Aditivos_com_Clientes -_(Uso_exclusivo_da_GEREL)''):
```python
OrdemServico.SetCustom('CSC_NUMERO', OrdemServico.GetCustom('NUM_CONTRATO'))
#OrdemServico.SetCustom('OBJETO_CONTRATACAO', 'PRJ_OBJETO')
```
Exemplo (de Ascensão_Profissional_e_Movimentação_de_Pessoas_Versão_69_Contratação_de_Estagiário):
```python
from Venki.Supravizio.Recurso.Custom import Orgao
#orgao = Orgao.Carrega("Id", OrdemServico.GetCustom("SCR_MOVI"));
#if (orgao != None):
#	OrdemServico.SetCustom("DESCRICAO_ORGAO",orgao.ToString())
#else:
#	OrdemServico.SetCustom("DESCRICAO_ORGAO","ORGAO NAO ENCONTRADO")
```

## ScriptSelecaoAtores — 36 scripts distintos
Onde: papel customizado por script: adiciona pessoas em `Atores`
Identificadores de contexto: Ator (36), Atores (36), OrdemServico (34), Pessoa (30), DB (11), Utils (4), Orgao (3)
Exemplo (de Comunicação_de_Acidente_de_Trabalho_-_CAT_Versão_1_Comunicação_de_Acidente_de_Trabalho_-_CAT):
```python
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Favorecido)
```
Exemplo (de Administração_-_Contratos_Versão_44_Inserir_Documentos_Contratuais_no_Sisccon):
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_TODOS"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))

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

## ScriptEvento — 28 scripts distintos
Onde: evento intermediário de mensagem: ajusta a `Mensagem` antes do envio
Identificadores de contexto: OrdemServico (25), Mensagem (23), Fornecedor (4), DB (3), Contrato (2)
Exemplo (de Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores):
```python
Mensagem.Complemento1 = OrdemServico.ObtemMotivoGateway("INSBAS")
```
Exemplo (de Nova_Estruturação_de_Negócios_Versão_32_Parecer_Cibernético):
```python
#OrdemServico.AdicionaComentario("Notificação 1 enviada com sucesso", False)
```
Exemplo (de Administração_-_Contratos_Versão_44_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_):
```python
if OrdemServico["PENF_EMAIL"] != None:        
    lista = OrdemServico["PENF_EMAIL"].Split(";")      
    for email in lista:                
        Mensagem.Destinatarios.Add(email)
    
remetente = (OrdemServico.Responsavel).ToString()
Mensagem.Remetente = remetente
#OrdemServico.AdicionaComentario(Mensagem.Remetente, False)
result = "".join(Mensagem.Destinatarios)
#OrdemServico.AdicionaComentario(result, False)
```

## ValorComparacaoDecision — 27 scripts distintos
Onde: alternativa do gateway: valor comparado com a expressão do gateway
Exemplo (de Administração_-_Serviços_Gerais_Versão_26_Atividade_02_Gabriel):
```python
1
```
Exemplo (de Administração_-_Alteração_e_Criação_de_Subprocessos_e_Relatórios_Versão_14_Criação-Alteração_de_Subprocessos_-_Novo_Fluxo):
```python
False
```
Exemplo (de Administração_-_Serviços_Gerais_Versão_26_Atividade_02_Gabriel):
```python
'DESPARQUIVAMENTO'
```

## ScriptValidacao — 26 scripts distintos
Onde: atividade: valida antes de avançar; pendências impedem a transição
Identificadores de contexto: OrdemServico (23), Criticas (21), Pessoa (4), DB (4), Utils (3), Atividade (3), Evento (2)
Exemplo (de Ascensão_Profissional_e_Movimentação_de_Pessoas_Versão_69_Contratação_de_Estagiário):
```python
if OrdemServico.GetCustom("ENTREGA_DOCUMENTO") == "Parcial" :
    Criticas.AdicionaPendencia("Entrega de documentação parcial !")
```
Exemplo (de Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso):
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if String.IsNullOrEmpty(OrdemServico["MATRICULA"].ToString()):
   pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
   OrdemServico["MATRICULA"] = pessoa["MATRICULA"]
   OrdemServico.Salva()
```
Exemplo (de Lista_de_Treinamento_Versão_5_Lista_de_Treinamento):
```python
grid = OrdemServico.GetCustom('LISTA_PARTICIPANTES')

if grid.Rows.Count == 0:
    Criticas.AdicionaPendencia('Não foi registrado nenhum participante.')
    
grid2 = OrdemServico.GetCustom('LISTA_TREINAMENTO2')

if grid2.Rows.Count == 0:
    Criticas.AdicionaPendencia('Não foi registrado nenhum treinamento.')
    
if grid2.Rows.Count > 1:
    Criticas.AdicionaPendencia('Você só deve cadastrar um treinamento por vez.')
```

## ExpressaoValor — 22 scripts distintos
Onde: ValorInput de atividade (ex.: chamada de subprocesso/iniciador): expressão do valor
Identificadores de contexto: Servico (18), OrdemServico (4)
Exemplo (de Nova_Estruturação_de_Negócios_Versão_30_Assinatura_de_Contrato):
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega(189)
```
Exemplo (de Administração_-_Serviços_Gerais_Versão_26_Atividade_02_Gabriel):
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega('Sigla','NUMDOC')
```
Exemplo (de Contrato_com_Clientes_Versão_30_Assinatura_de_Novos_Contratos_e_Aditivos_com_Clientes -_(Uso_exclusivo_da_GEREL)''):
```python
from Venki.Supravizio.Processo.Custom import Servico
Servico.Carrega("Sigla", "CADCONTRATO")
```

## ScriptFim — 16 scripts distintos
Onde: atividade: executa quando a atividade termina
Identificadores de contexto: OrdemServico (12), DB (3), Pessoa (3), HttpClient (2), JsonConvert (2), AuthenticationHeaderValue (2), StringContent (2), MediaTypeWithQualityHeaderValue (2)
Exemplo (de Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores):
```python
OrdemServico["RESPONSAVEL_ATUAL"] = OrdemServico.ResponsavelId
```
Exemplo (de Financeiro_-_Faturamento_de_Clientes_Versão_20_Faturamento_de_Clientes_-_Emissão_de_Notas_Fiscais):
```python
linhas = OrdemServico.GetCustom('GRID_NF').Rows.Count
OrdemServico.SetCustom('NUM_DOCU', linhas.ToString())
```
Exemplo (de Administração_-_Contratos_Versão_44_Pré-Notificação_do_Índice_de_Desempenho_de_Fornecedores_(IDF)_):
```python
#OrdemServico.AdicionaComentario((OrdemServico.GetCustom('FISCAL_ADM_SGPS') == '').ToString(), False)
#OrdemServico.AdicionaComentario(OrdemServico.GetCustom('FISCAL_ADM_SGPS'), False)
```

## ScriptConfirmado — 3 scripts distintos
Onde: campo/registro de formulário: executa ao confirmar a edição
Identificadores de contexto: Cancela (3), Formulario (3), OrdemServico (3), Utils (2), FormularioRegistro (2)
Exemplo (de Administração_-_Bens_Patrimoniais_Versão_38_Transferência_de_Bens_Patrimoniais):
```python
if (OrdemServico.Servico.Sigla == "TRANSFBENFUNCMSMUOR"):
    if ( Registro["RESPONSAVEL"] == None):
        Formulario.ExibeMensagem("O campo responsável é obrigatório")
        Cancela = True
```

## Regra — 2 scripts distintos
Onde: iniciador por regra/temporizador: fórmula que decide a geração de ocorrências
Exemplo (de Administração_-_Serviços_Gerais_Versão_26_Atividade_02_Gabriel):
```python
1<>2
```
Exemplo (de Suprimentos_-_Contratos_Versão_27_Registro_de_Notas_Fiscais_de_Fornecedores):
```python
2880
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
