# Fluxo: Indenização por Guarda e Zelo do Veículo Locado (INDENAGUARD) — versão 10
Caminho: Fluxos > Utilização de veículo locado Versão 10 Indenização por Guarda e zelo do veículo da frota
XML: `XMLs para teste/Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota.xml` | Supravizio 19.1.1 | SubProcessoId 20511 | DesenhoProcessoId 2888 | ProcessoId 405
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: GEORGE DOS SANTOS SILVA
Classe do subprocesso: DescricaoCliente=Indenização por Guarda e Zelo do Veículo Locado; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Indenização por guarda e zelo do veículo locado (INDENIZAGUARD)

## Grafo do fluxo
- [327213] Tarefa "Analisar e Conferir os Valores" {Fila Empresa B} → [327208] Anexar os Comprovantes e Termos
- [327214] Tarefa "Aprovação Prestação de Contas - Potenza" {Fila Empresa A} → [G74521] Precisa de Ajuste?
- [327215] Tarefa "Anexar os Comprovantes e Termos" {Fila Empresa A} → [327214] Aprovação Prestação de Contas - Potenza
- [327217] Tarefa "Integração ERP
" {Responsável atual} → [327218] Sucesso
- [327227] Tarefa "Tratamento de Dados" {Responsável} → [327217] Integração ERP

- [327203] Tarefa "Analisar e Conferir os Valores" {Fila Empresa B} → [327206] Aprovação Prestação de Contas - IT2B
- [327211] LinkInicial "" → [327212] Solicitar aprovação do Gerente Imediato


- [327212] Tarefa "Solicitar aprovação do Gerente Imediato

" {Fila CSC - Pendente de Aprovação} → [G74519] Gerente aprovou?
- [327204] FimCancelamento "" → (fim)
- [327216] Tarefa "Cálculo indenização


" {Responsável atual} → [327222] Integração ERP

- [327218] EventoFinal "Sucesso" → (fim)
- [327219] FimCancelamento "" → (fim)
- [327220] EventoIntermediarioMensagem "Chamado finalizado" → [327218] Sucesso
- [327206] Tarefa "Aprovação Prestação de Contas - IT2B" {Fila Empresa B} → [G74521] Precisa de Ajuste?
- [327207] EventoFinal "" → (fim)
- [327208] Tarefa "Anexar os Comprovantes e Termos" {Fila Empresa B} → [327206] Aprovação Prestação de Contas - IT2B
- [327205] Tarefa "Analisar e Conferir os valores" {Fila Empresa A} → [327215] Anexar os Comprovantes e Termos
- [327209] Tarefa "Analisar e Conferir os valores" {Fila Empresa A} → [327214] Aprovação Prestação de Contas - Potenza
- [327210] EventoIntermediarioMensagem "Reprovado" → [327204] 
- [327221] LinkInicial "" {Responsável} → [327226] Indenização em Lote
- [327222] Tarefa "Integração ERP
" {Responsável atual} → [327220] Chamado finalizado
- [327224] Tarefa "Solicitar aprovação do Gerente Imediato

" {Fila CSC - Pendente de Aprovação} → [G74517] Gerente aprovou?
- [327225] EventoIntermediarioMensagem "Reprovado" → [327219] 
- [327226] EventoIntermediarioMensagem "Indenização em Lote" → [327227] Tratamento de Dados
- [327223] EventoInicial "Indenização por Guarda e Zelo do Veículo Locado" → [327224] Solicitar aprovação do Gerente Imediato


- [G74517] Gateway "Gerente aprovou?" → «Sim» [327216] Cálculo indenização


 | «Não» [327225] Reprovado
- [G74518] Gateway "Qual a empresa?" → «Potenza» [327209] Analisar e Conferir os valores | «IT2B» [327203] Analisar e Conferir os Valores
- [G74519] Gateway "Gerente aprovou?" → «Não» [327210] Reprovado | «Sim» [G74520] Qual a Empresa?
- [G74520] Gateway "Qual a Empresa?" → «Potenza» [327205] Analisar e Conferir os valores | «IT2B» [327213] Analisar e Conferir os Valores
- [G74521] Gateway "Precisa de Ajuste?" → «Não» [327207]  | «Sim» [G74518] Qual a empresa?

## Gateways
### [G74517] Gerente aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVAR") or OrdemServico.PossuiAprovacao("APROVARPS")
```
- alternativa → [327216] Cálculo indenização


: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [327225] Reprovado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G74518] Qual a empresa? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['EMPRESA_TERCEIRIZADA'] == "IT2B"
```
- alternativa → [327209] Analisar e Conferir os valores: OperadorDecision=Equal; ReferenciaDecision=Potenza; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [327203] Analisar e Conferir os Valores: OperadorDecision=Equal; ReferenciaDecision=IT2B; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G74519] Gerente aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVARPS")
```
- alternativa → [327210] Reprovado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
False
```
- alternativa → [G74520] Qual a Empresa?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
True
```
### [G74520] Qual a Empresa? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['EMPRESA_TERCEIRIZADA'].upper() == "POTENZA"
```
- alternativa → [327205] Analisar e Conferir os valores: OperadorDecision=Equal; ReferenciaDecision=Potenza; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [327213] Analisar e Conferir os Valores: OperadorDecision=Equal; ReferenciaDecision=IT2B; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```
### [G74521] Precisa de Ajuste? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROVIT2B") or OrdemServico.PossuiAprovacao("APROVPOTENZA")
```
- alternativa → [327207] : OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [G74518] Qual a empresa?: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [327213] Tarefa "Analisar e Conferir os Valores"
Responsável: Fila Empresa B (papel 1286)
**ScriptInicio**
```python
diasTotais = Convert.ToInt32(OrdemServico.GetCustom("DIAS"))
diasPosseVeiculo = Convert.ToInt32(OrdemServico.GetCustom("DIAS_DE_TRA"))
mes = Convert.ToInt32(OrdemServico.GetCustom("MES_REFERENCIA"))
ano = Convert.ToInt32(OrdemServico.GetCustom("ANO_REFERENCIA"))
valorInicial = 0
valor = 0

DiasNoMesAtual = DateTime.DaysInMonth(ano, mes)

OrdemServico.AdicionaComentario("Detalhes do Cálculo:\n\n(R$ 600,00 / Quantidade de dias do Mês) x Dias em posse do veículo (Que o gestor preencheu)", False)

OrdemServico.AdicionaComentario("(R$ 600,00 / {0}) x {1}".format(DiasNoMesAtual.ToString(), diasPosseVeiculo.ToString()), False)

valorInicial = (600.00 / DiasNoMesAtual)
valor = (valorInicial * diasPosseVeiculo)
valor = round(valor, 2)
OrdemServico.SetCustom("VALOR", valor)

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=VALORES IT2B
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - DIAS "Quantidade de dias em Posse do Veículo" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] obrigatório
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA] obrigatório
  - EMPRESA_TERCEIRIZADA "Empresa Terceirizada" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - TIPO_ATIVIDADE "Proporcional / Integral" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
  - DIAS_DE_TRA "Quantidade de Dias Definitivos em Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório

### [327214] Tarefa "Aprovação Prestação de Contas - Potenza"
Responsável: Fila Empresa A (papel 1287)
Config: Codigo=APROVPOTENZA
- Operação PR0002 Aprovar
  - (aprovação) EMPRESA_TERCEIRIZADA "Empresa Terceirizada" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA]
  - (aprovação) DIAS "Dias" [TextBox Integer → CPE_HOMOLOGACAO.DIAS]
  - (aprovação) MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA]
  - (aprovação) ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA]
  - (aprovação) TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - (aprovação) DIAS_DE_TRA "Dias Definitivos de Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - (aprovação) VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - (aprovação) TIPO_ATIVIDADE "Tipo de Atividade - informe" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE]
  - (aprovação) TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - aprovador: Gerente TE Favorecido  (Unico)

### [327215] Tarefa "Anexar os Comprovantes e Termos"
Responsável: Fila Empresa A (papel 1287)
- Operação PR0004 Associar Itens Configuração
  - anexo "Termo de Responsabilidade de Uso e Guarda do Veículo" classes: Arquivo 02 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração: Nome=COMPROVANTE
  - anexo "Comprovante de Depósito" classes: Arquivo 01 — RequeridoInicial=true

### [327217] Tarefa "Integração ERP
"
Responsável: Responsável atual (papel 36)
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

valorRetorno = OrdemServico["VALOR"].ToString()
OrdemServico.SetCustom("TE_VALOR_REEMBOLSO", valorRetorno)
uor = OrdemServico["TE_UOR"].ToString()
matricula = OrdemServico["TE_MATRICULA"].ToString()

#OrdemServico.AdicionaComentario(OrdemServico.Servico.Sigla.ToString(), False)

if OrdemServico.Servico.Sigla == 'INDVEICULOFROTALOTE':
    if not String.IsNullOrEmpty(OrdemServico.GetCustom('ID_PERSON')):
        idFavorecido = Convert.ToInt32(OrdemServico.GetCustom('ID_PERSON'))
        # OrdemServico.AdicionaComentario('Tudo certo com o ID!', False) 
        favorecido = Pessoa.Carrega(idFavorecido)
    #else:
        #OrdemServico.AdicionaComentario('ERRO NA LEITURA DO ID DA PESSOA: '+ OrdemServico.GetCustom('ID_PERSON'), False)
        
    uor = uor.split(' - ')[0]    
        
else:
    idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("TE_NOME_EMPREGADO"))
    favorecido = Pessoa.Carrega(idFavorecido)

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
valor = DB.ExecuteScalar("select replace('"+ OrdemServico.GetCustom("TE_VALOR_REEMBOLSO").ToString() + "',',','.') as valor from dual")
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
    OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")
    
#--- crédito
    OrdemServico.AdicionaComentario("Procedure para crédito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")

#----- insert no AP (PARA PAGAMENTO)
#verifica se houve os lançamentos anteriores no GL e não consta no AP
contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0' and (contInterfaceGL.ToString()>= '2' or contGL.ToString()>= '2'):
    OrdemServico.AdicionaComentario("Procedure para inserir no AP:  call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"', '"+ fornecedor +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"', '"+ fornecedor +"') ")


OrdemServico.Salva()
AvancaProximaAtividade = True
```

### [327227] Tarefa "Tratamento de Dados"
Responsável: Responsável (papel 751)
**ScriptInicio**
```python
diasTotais = 30
diasTrab = Convert.ToInt32(OrdemServico.GetCustom('VALOR_QUALIF'))

valorCampo = Convert.ToDecimal(OrdemServico.GetCustom('VALOR'))
tipo = OrdemServico.GetCustom('SIM_NAO')
valor = 0
valorDia = 0

if OrdemServico["ANO_REF"] == '2024':
    OrdemServico.SetCustom('VALOR', 300.00)
    if tipo == 'Proporcional':
        valorDia = (300.00 / diasTotais)
        valor = (valorDia * diasTrab)
        valor = round(valor,2)
        OrdemServico.SetCustom('VALOR', valor)
                
    else:
        OrdemServico.SetCustom('VALOR', 300.00)
        
        
else:
    OrdemServico.SetCustom('VALOR', 600.00)
    if tipo == 'Proporcional':
        valorDia = (600.00 / diasTotais)
        valor = (valorDia * diasTrab)
        valor = round(valor,2)
        OrdemServico.SetCustom('VALOR', valor)        

OrdemServico.Salva()
AvancaProximaAtividade = True
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Abertura
  - ID_PERSON "ID pessoa ERP" [TextBox String → CP_ORDEM_SERVICO.ID_PERSON]
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - SIM_NAO "Integral ou proporcional? Quando do ingresso no sistema de locação de veículos da frota BBTS, o colaborador deverá escolher a opção de pagamento PROPORCIONAL se sua entrada ocorrer no mês em andamento, levando em consideração os dias de utilização no mês em questão. Para os meses seguintes, optar pela modalidade de pagamento INTEGRAL. " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - VALOR_QUALIF "Quantidade de dias de utilização do veículo no mês" [TextBox Decimal → CPE_FINANCEIRO.VALOR_QUALIF]
  - MES_REFERENCIA "Mês de referencia" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA]
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF]
  - TE_VALOR_REEMBOLSO "Valor para reembolso" [TextBox Decimal → CPE_CSC.TE_VALOR_REEMBOLSO]
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]

### [327203] Tarefa "Analisar e Conferir os Valores"
Responsável: Fila Empresa B (papel 1286)
- Operação PR0004 Associar Itens Configuração
  - anexo "Termo de Guarda e Zelo" classes: Arquivo 02 — RequeridoInicial=true
- Operação PR0001 Preencher Campos: RotuloPreenchimento=VALORES IT2B - CORREÇÃO
  - ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA] obrigatório
  - EMPRESA_TERCEIRIZADA "Empresa Terceirizada" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - TIPO_ATIVIDADE "Tipo de Atividade - informe" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
  - DIAS_DE_TRA "Dias Definitivos de Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA_CORR obrigatório
    - coluna TIPO_CHAVE obrigatório
    - coluna CHAVE_PIX obrigatório
    - coluna BANCO obrigatório
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - DIAS "Dias" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] obrigatório
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de Depósito" classes: Arquivo 01 — RequeridoInicial=true

### [327211] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
OrdemServico.Servico.Sigla = 'INDENIZAGUARDPARAPS'
AvancaProximaAtividade = True
```
**ScriptFim**
```python
OrdemServico.Servico.Sigla = 'INDENIZAGUARDPARAPS'
OrdemServico.AdicionaComentario(OrdemServico.Servico.Sigla.ToString(), False)
OrdemServico.AdicionaComentario((OrdemServico.Servico.Sigla == 'INDENIZAGUARDPARAPS').ToString(), False)
OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
campos = ["ANO_REFERENCIA", "DIAS", "EMPRESA_TERCEIRIZADA", "MES_REFERENCIA", "TE_MATRICULA", "TE_NOME_EMPREGADO", "TE_UOR", "TIPO_ATIVIDADE", "VALOR"]

for i in campos:
    Formulario[i].Habilitado = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=ABERTURA POSTOS DE SERVIÇO
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - DIAS "Dias de posse do Veículo" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] obrigatório
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA] obrigatório
  - EMPRESA_TERCEIRIZADA "Empresa" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - TIPO_ATIVIDADE "Proporcional / Integral" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
- Associação de subprocesso: AssociacaoId=1568; FraseAssociacao=Veiculo Locado PS --> Base; Nome=VEICULOLOCADOPS

### [327212] Tarefa "Solicitar aprovação do Gerente Imediato

"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVARPS
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel("VALOR_DOD", True)
```
**ScriptValidacao**
```python
dias = Convert.ToInt32(OrdemServico["VALOR_DOD"])
#Utils.LogInformation("retorno do campo" , str(dias))

if dias >= 24:
    Criticas.AdicionaPendencia('A solicitação de idenização está limitada a 23 dias por mês.')
```
**ScriptFormCarregado**
```python
Formulario['VALOR'].Visivel = False
Formulario['VALOR'].Habilitado = False

Formulario['SIM_NAO'].Habilitado = False
Formulario['VALOR_QUALIF'].Habilitado = False
```
- Operação PR0002 Aprovar: ObrigatoriedadeMotivo=Todas
  - (aprovação) TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - (aprovação) EMPRESA_TERCEIRIZADA "Empresa Terceirizada" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA]
  - (aprovação) VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) DIAS "Dias" [TextBox Integer → CPE_HOMOLOGACAO.DIAS]
  - (aprovação) MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA]
  - (aprovação) ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA]
  - (aprovação) TIPO_ATIVIDADE "Tipo de Atividade - informe" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE]
  - (aprovação) TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - (aprovação) DIAS_DE_TRA "Dias Definitivos de Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] — Obrigatoriedade=Aprovacao
  - aprovador: Gerente TE Favorecido  (Unico)

### [327204] FimCancelamento ""

### [327216] Tarefa "Cálculo indenização


"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
diasTotais = 30
diasTrab = Convert.ToInt32(OrdemServico.GetCustom('VALOR_QUALIF'))

valorCampo = Convert.ToDecimal(OrdemServico.GetCustom('VALOR'))
tipo = OrdemServico.GetCustom('SIM_NAO')
valor = 0
valorDia = 0

if OrdemServico["ANO_REF"] == '2024':
    OrdemServico.SetCustom('VALOR', 300.00)
    if tipo == 'Proporcional':
        valorDia = (300.00 / diasTotais)
        valor = (valorDia * diasTrab)
        valor = round(valor,2)
        OrdemServico.SetCustom('VALOR', valor)
        AvancaProximaAtividade = True
                
    else:
        OrdemServico.SetCustom('VALOR', 300.00)
        AvancaProximaAtividade = True
        
        
else:
    OrdemServico.SetCustom('VALOR', 600.00)
    if tipo == 'Proporcional':
        valorDia = (600.00 / diasTotais)
        valor = (valorDia * diasTrab)
        valor = round(valor,2)
        OrdemServico.SetCustom('VALOR', valor)
        AvancaProximaAtividade = True

        
OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFormCarregado**
```python
#if OrdemServico.Servico.Sigla == 'INDENAGUARD':
#
#    Formulario['SIM_NAO'].Habilitado = False
#    Formulario['VALOR'].Habilitado = False
#    #Formulario['VALOR_DOD'].Habilitado = False
#    Formulario['VALOR_QUALIF'].Habilitado = False
#    Formulario['VALOR'].Visivel = True
#    Formulario['TE_VALOR_REEMBOLSO'].Visivel = False
#    Formulario['TE_VALOR_REEMBOLSO'].Habilitado = False
#    Formulario['ANO_REF'].Visivel = False
#    Formulario['ANO_REF'].Habilitado = False

#if Formulario['ANO_REF'].Valor == '2024':
#    Formulario['VALOR'].Valor = 300.00
#else:
#    Formulario['VALOR'].Valor = 600.00
```
- Operação PR0001 Preencher Campos
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF]
**ANO_REF.ScriptModificado**
```python
#if Formulario['ANO_REF'].Valor == '2024':
#    Formulario['VALOR'].Valor = 300.00
#else:
#    Formulario['VALOR'].Valor = 600.00
```
  - VALOR_QUALIF "Dias trabalhados" [TextBox Decimal → CPE_FINANCEIRO.VALOR_QUALIF]
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - TE_VALOR_REEMBOLSO "Valor para reembolso" [TextBox Decimal → CPE_CSC.TE_VALOR_REEMBOLSO]
  - SIM_NAO "Integral ou proporcional?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]

### [327218] EventoFinal "Sucesso"
**ScriptInicio**
```python
#if OrdemServico['ANO_REF'] == '2024':
#    OrdemServico['VALOR'] = 300.00
#else:
#    OrdemServico['VALOR'] = 600.00
```
**ScriptFormCarregado**
```python
Formulario['VALOR'].Visivel = True
Formulario['VALOR'].Habilitado = False
Formulario['ANO_REF'].Visivel = False
```
- Operação PR0001 Preencher Campos
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF] obrigatório
**ANO_REF.ScriptModificado**
```python
#if Formulario['ANO_REF'].Valor == "2024":
#    if Formulario['SIM_NAO'].Valor == 'Proporcional':
#        Formulario['VALOR'].Valor = Formulario['VALOR_QUALIF'].Valor*(300.00 / 30)
#    else:
#        Formulario['VALOR'].Valor = 300.00    
#else:
#    if Formulario['SIM_NAO'].Valor == 'Proporcional':
#        Formulario['VALOR'].Valor = Formulario['VALOR_QUALIF'].Valor*(600.00 / 30)
#    else:
#        Formulario['VALOR'].Valor = 600.00
```

### [327219] FimCancelamento ""

### [327220] EventoIntermediarioMensagem "Chamado finalizado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Aprovação Indenização por lotação em base destacada
Corpo do comunicado: Informamos que foi aberta a solicitação nº OrdemServico.Numero - Indenização por Lotação em Base Destacada, referente ao mês 
 OrdemServico.Customizado.MES_REFERENCIA / OrdemServico.Customizado.ANO_REF, conforme previsto na NI 1346.
O valor a ser creditado em sua conta será de R$ OrdemServico.Customizado.VALOR_PRESTACAO . 
Caso identifique alguma inconsistência, gentileza acionar o e-mail dires@bbts.com.br.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [327206] Tarefa "Aprovação Prestação de Contas - IT2B"
Responsável: Fila Empresa B (papel 1286)
Config: Codigo=APROVIT2B
- Operação PR0002 Aprovar
  - (aprovação) ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA]
  - (aprovação) MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA]
  - (aprovação) TIPO_ATIVIDADE "Proporcional / Integral" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE]
  - (aprovação) TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR]
  - (aprovação) VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - (aprovação) TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA]
  - (aprovação) DIAS "Quantidade de dias em Posse do Veículo" [TextBox Integer → CPE_HOMOLOGACAO.DIAS]
  - (aprovação) TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO]
  - (aprovação) EMPRESA_TERCEIRIZADA "Empresa Terceirizada" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA]
  - (aprovação) DIAS_DE_TRA "Quantidade de Dias Definitivos em Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA]
  - aprovador: Gerente TE Favorecido  (Unico)

### [327207] EventoFinal ""

### [327208] Tarefa "Anexar os Comprovantes e Termos"
Responsável: Fila Empresa B (papel 1286)
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de Depósito" classes: Arquivo 01 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Termo de Guarda e Zelo" classes: Arquivo 02 — RequeridoInicial=true

### [327205] Tarefa "Analisar e Conferir os valores"
Responsável: Fila Empresa A (papel 1287)
**ScriptInicio**
```python
diasTotais = Convert.ToInt32(OrdemServico.GetCustom("DIAS"))
diasPosseVeiculo = Convert.ToInt32(OrdemServico.GetCustom("DIAS_DE_TRA"))
mes = Convert.ToInt32(OrdemServico.GetCustom("MES_REFERENCIA"))
ano = Convert.ToInt32(OrdemServico.GetCustom("ANO_REFERENCIA"))
valorInicial = 0
valor = 0

DiasNoMesAtual = DateTime.DaysInMonth(ano, mes)

OrdemServico.AdicionaComentario("Detalhes do Cálculo:\n\n(R$ 600,00 / Quantidade de dias do Mês) x Dias em posse do veículo (Que o gestor preencheu)", False)

OrdemServico.AdicionaComentario("(R$ 600,00 / {0}) x {1}".format(DiasNoMesAtual.ToString(), diasPosseVeiculo.ToString()), False)

valorInicial = (600.00 / DiasNoMesAtual)
valor = (valorInicial * diasPosseVeiculo)
valor = round(valor, 2)
OrdemServico.SetCustom("VALOR", valor)

OrdemServico.Salva()
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=VALORES POTENZA
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - DIAS "Quantidade de dias em Posse do Veículo" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] obrigatório
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA] obrigatório
  - EMPRESA_TERCEIRIZADA "Empresa Terceirizada" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - TIPO_ATIVIDADE "Proporcional / Integral" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
  - DIAS_DE_TRA "Quantidade de Dias Definitivos em Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório

### [327209] Tarefa "Analisar e Conferir os valores"
Responsável: Fila Empresa A (papel 1287)
- Operação PR0001 Preencher Campos: RotuloPreenchimento=VALORES IT2B - CORREÇÃO
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - DIAS "Dias" [TextBox Integer → CPE_HOMOLOGACAO.DIAS] obrigatório
  - MES_REFERENCIA "Mês referência" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REFERENCIA "Ano referência" [DropDownList String → CPE_CSC.ANO_REFERENCIA] obrigatório
  - EMPRESA_TERCEIRIZADA "Empresa Terceirizada" [TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - TIPO_ATIVIDADE "Tipo de Atividade - informe" [DropDownList String → CPE_CSC.TIPO_ATIVIDADE] obrigatório
  - DIAS_DE_TRA "Dias Definitivos de Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] obrigatório
    - coluna BANCO obrigatório
    - coluna AGENCIA obrigatório
    - coluna CONTA_CORR obrigatório
    - coluna TIPO_CHAVE obrigatório
    - coluna CHAVE_PIX obrigatório
- Operação PR0004 Associar Itens Configuração
  - anexo "Termo de Guarda e Zelo" classes: Arquivo 02 — RequeridoInicial=true
- Operação PR0004 Associar Itens Configuração
  - anexo "Comprovante de Depósito" classes: Arquivo 01 — RequeridoInicial=true

### [327210] EventoIntermediarioMensagem "Reprovado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação Indenização Base Destacada
Corpo do comunicado: Prezado(a),
Informamos que sua solicitação de para receber a indenização por lotação em base destacada foi reprovado pelo seu Gestor.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [327221] LinkInicial ""
Responsável: Responsável (papel 751)
Config: TipoMensagem=MensagemProcesso
**ScriptInicio**
```python
if OrdemServico['ANO_REF'] == "2024":
    if OrdemServico['SIM_NAO'] == 'Proporcional':
        OrdemServico.SetCustom('VALOR', OrdemServico.GetCustom('VALOR_QUALIF')*(300.00 / 30))
    else:
        OrdemServico.SetCustom('VALOR', 300.00)
else:
    if OrdemServico['SIM_NAO'] == 'Proporcional':
        OrdemServico.SetCustom('VALOR', OrdemServico.GetCustom('VALOR_QUALIF')*(600.00 / 30))
    else:
        OrdemServico.SetCustom('VALOR', 600.00)
        

diasTotais = 30
diasTrab = Convert.ToInt32(OrdemServico.GetCustom('VALOR_QUALIF'))

valorCampo = Convert.ToDecimal(OrdemServico.GetCustom('VALOR'))
tipo = OrdemServico.GetCustom('SIM_NAO')
valor = 0
valorDia = 0

if OrdemServico["ANO_REF"] == '2024':
    OrdemServico.SetCustom('VALOR', 300.00)
    if tipo == 'Proporcional':
        valorDia = (300.00 / diasTotais)
        valor = (valorDia * diasTrab)
        valor = round(valor,2)
        OrdemServico.SetCustom('VALOR', valor)
                
    else:
        OrdemServico.SetCustom('VALOR', 300.00)
        
        
else:
    OrdemServico.SetCustom('VALOR', 600.00)
    if tipo == 'Proporcional':
        valorDia = (600.00 / diasTotais)
        valor = (valorDia * diasTrab)
        valor = round(valor,2)
        OrdemServico.SetCustom('VALOR', Convert.ToDecimal(valor))        

OrdemServico.Salva()
AvancaProximaAtividade = True
```
**ScriptFim**
```python
OrdemServico.Servico.Sigla = 'INDVEICULOFROTALOTE'
OrdemServico.Salva()
```
**ScriptFormCarregado**
```python
lista = ["ANO_REF", "ID_PERSON", "MES_REFERENCIA", "SIM_NAO", "TE_MATRICULA", "TE_UOR", "TE_VALOR_REEMBOLSO", "VALOR", "VALOR_QUALIF"]

for i in lista:
    Formulario.ExibeMensagem(Formulario[i].Valor.ToString() + '\n')
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Abertura
  - SIM_NAO "Integral ou proporcional? Quando do ingresso no sistema de locação de veículos da frota BBTS, o colaborador deverá escolher a opção de pagamento PROPORCIONAL se sua entrada ocorrer no mês em andamento, levando em consideração os dias de utilização no mês em questão. Para os meses seguintes, optar pela modalidade de pagamento INTEGRAL. " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - MES_REFERENCIA "Mês de referencia" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF] obrigatório
  - TE_VALOR_REEMBOLSO "Valor para reembolso" [TextBox Decimal → CPE_CSC.TE_VALOR_REEMBOLSO] obrigatório
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - VALOR_QUALIF "Quantidade de dias de utilização do veículo no mês" [TextBox Decimal → CPE_FINANCEIRO.VALOR_QUALIF] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - ID_PERSON "ID pessoa ERP" [TextBox String → CP_ORDEM_SERVICO.ID_PERSON] obrigatório
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
- Associação de subprocesso: AssociacaoId=1470; FraseAssociacao=Ind. Guarda e Zelo (LOTE) --> Base; Nome=INDLOTEPARABASE

### [327222] Tarefa "Integração ERP
"
Responsável: Responsável atual (papel 36)
**ScriptInicio**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Recurso.Custom import Pessoa
valorRetorno = OrdemServico["VALOR"].ToString()
OrdemServico.SetCustom("TE_VALOR_REEMBOLSO", valorRetorno)
uor = OrdemServico["TE_UOR"].ToString()
matricula = OrdemServico["TE_MATRICULA"].ToString()

nota = 'RIVL'
fornecedor = '001.110001.3000001000.219399.000000.000.00000'

#OrdemServico.AdicionaComentario(OrdemServico.Servico.Sigla.ToString(), False)

if OrdemServico.Servico.Sigla == 'INDVEICULOFROTALOTE':
    if not String.IsNullOrEmpty(OrdemServico.GetCustom('ID_PERSON')):
        idFavorecido = Convert.ToInt32(OrdemServico.GetCustom('ID_PERSON'))
        # OrdemServico.AdicionaComentario('Tudo certo com o ID!', False) 
        favorecido = Pessoa.Carrega(idFavorecido)
    #else:
        #OrdemServico.AdicionaComentario('ERRO NA LEITURA DO ID DA PESSOA: '+ OrdemServico.GetCustom('ID_PERSON'), False)
        
    uor = uor.split(' - ')[0]    
        
else:
    idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("TE_NOME_EMPREGADO"))
    favorecido = Pessoa.Carrega(idFavorecido)



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
valor = DB.ExecuteScalar("select replace('"+ OrdemServico.GetCustom("TE_VALOR_REEMBOLSO").ToString() + "',',','.') as valor from dual")
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
    OrdemServico.AdicionaComentario("Procedure para débito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ conta +"', "+valor.ToString() +", 0, '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")
    
#--- crédito
    OrdemServico.AdicionaComentario("Procedure para crédito GL: call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_GL_INTERFACE ('A','Locomoções', SYSDATE, '"+ fornecedor +"', 0, "+valor.ToString() +", '"+ nota +""+ numero + "', 'REEMBOLSO"+ numero +"','REEMBOLSO"+ numero +"') ")

#----- insert no AP (PARA PAGAMENTO)
#verifica se houve os lançamentos anteriores no GL e não consta no AP
contInterfaceGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM XXBBTSGATE.VW_BBTS_GL_INTERFACE WHERE USER_JE_SOURCE_NAME = 'Supravizio' AND REFERENCE10 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

contGL = DB.ExecuteScalar("SELECT COUNT(1) as CONTINSERIDAS FROM VW_BBTS_GL_INTERFACE_SV_PROCES WHERE DESCRIPTION2 LIKE '%"+nota+""+OrdemServico.Numero.ToString() + "%'")

if contInterfaceAP.ToString()=='0' and contAP.ToString()=='0' and (contInterfaceGL.ToString()>= '2' or contGL.ToString()>= '2'):
    OrdemServico.AdicionaComentario("Procedure para inserir no AP:  call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"', '"+ fornecedor +"') ", False)
    
    DB.ExecuteNonQuery(" call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('"+ nota +""+ numero + "', SYSDATE+1, '"+ matricula +"', "+valor.ToString() +", '"+ fornecedor +"', '"+ termo +"', '"+ fornecedor +"') ")


OrdemServico.Salva()
AvancaProximaAtividade = True














#
#
#
#
#qry = "SELECT MAX(INICIO_DATA_FUNCAO), EMPRESA, SUBSTR('"+sigla.ToString()+"', 1, 1) AS PREFIXO  FROM CAD_FUNCIONARIO_V WHERE DATA_DE_DEMISSAO IS NULL AND MATRICULA = '" + matricula.ToString() + "' GROUP BY EMPRESA"
#
#lista = Utils.ExecuteDataTable(qry)
#if (lista != None):
#    for linha in lista.Rows:
#        if (DBNull.Value.Equals(linha["EMPRESA"]) != True ):
#            empresa = linha["EMPRESA"].ToString()
#            #OrdemServico.SetCustom("NUM_CHAVE",empresa.ToString())
#            filial = empresa.ToString()
#            
#        if (DBNull.Value.Equals(linha["PREFIXO"]) != True ):
#            scr = linha["PREFIXO"].ToString()
#            #OrdemServico.SetCustom("NUM_ITEM",scr.ToString())
#            
#           
#      
#      
#
#      
#            
###Utils.LogInformation("filial" , str(filial)) ##Retorno do campo filial no log
##----- insert no AP
#
#sql = " call XXBBTSGATE.PR_BBTS_INSERT_AP_INTERFACE ('RTE"+ OrdemServico.Numero.ToString() + "', SYSDATE+1, '"+ OrdemServico.GetCustom("TE_MATRICULA").ToString() +"' , to_number(replace('" + OrdemServico.GetCustom("TE_VALOR_REEMBOLSO").ToString() + "',',','.')), '001." + filial + "." + str(uor) + "." + prefixo + "90303') "
#
##-- conta = "001."+ filial +"."+ uor +"."+ prefixo + rubrica +".000000.000.00000"
#
##OrdemServico.AdicionaComentario(sql.ToString(), False)
#DB.ExecuteNonQuery(sql.ToString())
#AvancaProximaAtividade = True
#
#
```

### [327224] Tarefa "Solicitar aprovação do Gerente Imediato

"
Responsável: Fila CSC - Pendente de Aprovação (papel 461)
Config: Codigo=APROVAR
**ScriptInicio**
```python
OrdemServico.ModificaCampoFormularioVisivel("VALOR_DOD", True)
```
**ScriptValidacao**
```python
dias = Convert.ToInt32(OrdemServico["VALOR_DOD"])
#Utils.LogInformation("retorno do campo" , str(dias))

if dias >= 24:
    Criticas.AdicionaPendencia('A solicitação de idenização está limitada a 23 dias por mês.')
```
**ScriptFormCarregado**
```python
Formulario['VALOR'].Visivel = False
Formulario['VALOR'].Habilitado = False

Formulario['SIM_NAO'].Habilitado = False
Formulario['VALOR_QUALIF'].Habilitado = False
```
- Operação PR0002 Aprovar
  - (aprovação) VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR]
  - (aprovação) MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA]
  - (aprovação) SIM_NAO "Integral ou proporcional?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] — PermiteModificarAprovado=true
  - (aprovação) SCR_PRESTADOR "UOR" [TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR]
  - (aprovação) VALOR_QUALIF "Quantidade de dias de utilização do veículo no mês" [TextBox Decimal → CPE_FINANCEIRO.VALOR_QUALIF]
  - (aprovação) FAVORECIDO_TODOS "Nome" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS]
  - (aprovação) QUANTIDADE "Quantidade de dias trabalhados no mês" [TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE]
  - (aprovação) OUTROS "O empregado está ciente das regras previstas no Regulamento e que a indenização possui característica indenizatória. Logo, não incidirá Imposto de Renda - IR, Contribuição Previdenciária - INSS e Fundo de Garantia por tempo de Serviço - FGTS, sendo devida ao empregado somente enquanto aderir ao veículo da frota locada. Declara ainda que ainda que assinou o Termo de Responsabilidade e/ou Termo de Ciência de uso do veículo, o qual refletirá sua responsabilidade pela guarda e zelo do automóvel." [CheckBox Boolean → CPE_ORDEM_SERVICO.OUTROS]
  - (aprovação) DIAS_DE_TRA "Dias Definitivos de Posse do Veículo" [TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA] — Obrigatoriedade=Aprovacao
  - aprovador: Gerente TE Favorecido  (Unico)

### [327225] EventoIntermediarioMensagem "Reprovado"
Destinatário: Cliente (papel 18)
ModeloComunicado: Reprovação Indenização Base Destacada
Corpo do comunicado: Prezado(a),
Informamos que sua solicitação de para receber a indenização por lotação em base destacada foi reprovado pelo seu Gestor.
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

### [327226] EventoIntermediarioMensagem "Indenização em Lote"
Destinatário: Cliente e Gerente Posição (papel 631)
ModeloComunicado: Indenização por guarda e zelo do veículo da Frota (Lote)
Corpo do comunicado: Prezado Colaborador,
Informamos a abertura do chamado OrdemServico.Numero de pagamento da indenização por Guarda e Zelo do veículo da Frota referente a competência de OrdemServico.Customizado.MES_REFERENCIA de OrdemServico.Customizado.ANO_REF .
Caso verifique alguma inconsistência, por gentileza entrar em contato com a caixa deslocamentotecnico@bbts.com.br.
Atenciosamente,
Central de Serviços

### [327223] EventoInicial "Indenização por Guarda e Zelo do Veículo Locado"
TipoSolicitacao: Serviços para veículo locado
**ScriptInicio**
```python
        



#if OrdemServico["ANO_REF"] == '2024':
#    OrdemServico.SetCustom('TE_VALOR_REEMBOLSO', 300.00)
#    if tipo == 'Proporcional':
#        valorDia = (300.00 / diasTotais)
#        valor = (valorDia * diasTrab)
#        valor = round(valor,2)
#        OrdemServico.SetCustom('TE_VALOR_REEMBOLSO', valor)
#                
#    else:
#        OrdemServico.SetCustom('TE_VALOR_REEMBOLSO', 300.00)
#else:
#    OrdemServico.SetCustom('TE_VALOR_REEMBOLSO', 600.00)
#    if tipo == 'Proporcional':
#        valorDia = (600.00 / diasTotais)
#        valor = (valorDia * diasTrab)
#        valor = round(valor,2)
#        OrdemServico.SetCustom('TE_VALOR_REEMBOLSO', valor)
```
**ScriptValidacao**
```python
import datetime

if (OrdemServico.GetCustom("OUTROS") == False):
        Criticas.AdicionaPendencia("Declaração pendente!!")
        
        
mesAtual = Convert.ToInt32(DateTime.Now.ToString("MM"))
mesDeclarado = Convert.ToInt32(OrdemServico["MES_REFERENCIA"])

anoAtual = Convert.ToInt32(DateTime.Now.ToString("yyyy"))
anoDeclarado = Convert.ToInt32(OrdemServico["ANO_REF"])

today = DateTime.Now;
prevDate = DateTime(anoDeclarado, mesDeclarado, 01)

#if OrdemServico.GetCustom("VALOR_QUALIF") >= 24:
#    Criticas.AdicionaPendencia('A solicitação de indenização para base destacada está limitada a 23 dias por mês.')

    
if anoDeclarado == anoAtual and mesDeclarado > mesAtual or anoDeclarado > anoAtual and mesDeclarado > mesAtual or anoDeclarado == anoAtual and mesDeclarado == mesAtual:
    Criticas.AdicionaPendencia("Não é permitido lançamentos futuros ou para o mês atual. Verifique sua solicitação e tente novamente.")
    
elif anoDeclarado > anoAtual:
    Criticas.AdicionaPendencia("Não é permitido lançamentos futuros ou para o mês atual. Verifique sua solicitação e tente novamente.")


elif mesDeclarado > 8:
    Criticas.AdicionaPendencia('Devido a uma regra interna, só é permitido solicitações até Outubro de 2025 (Mês 9)')

diffOfDates = ((today.Year - prevDate.Year) * 12) + today.Month - prevDate.Month

if diffOfDates >= 4:
    Criticas.AdicionaPendencia("A abertura retroativa está limitada a até 3 meses a partir do mês atual.")
     
    

##Consulta retorna OS aberta e/ou finalizadas no mês e ano referente para o favorecido/Cliente 

queryLotacao = DB.ExecuteDataTable("Select OCORRENCIA.ID_OCORRENCIA, OCORRENCIA.ID_CLIENTE, OCORRENCIA.ASSUNTO, OCORRENCIA.SITUACAO, OCORRENCIA.NUMERO, PESSOA.NOME, CPE_CSC.MES_REFERENCIA, CPE_CSC.ANO_REF From OCORRENCIA Inner Join CPE_CSC On OCORRENCIA.ID_OCORRENCIA = CPE_CSC.ID_OCORRENCIA Inner Join PESSOA On PESSOA.ID_PESSOA = CPE_CSC.TE_NOME_EMPREGADO Where PESSOA.ID_PESSOA = '"+OrdemServico["TE_NOME_EMPREGADO"]+"' And OCORRENCIA.ASSUNTO = 'Indenização por Guarda e Zelo do Veículo Locado' And (OCORRENCIA.SITUACAO = 'FinalizadaSucesso' or OCORRENCIA.SITUACAO = 'Aberto') And (CPE_CSC.MES_REFERENCIA = '"+OrdemServico["MES_REFERENCIA"]+"' And CPE_CSC.ANO_REF = '"+OrdemServico["ANO_REF"]+"') and OCORRENCIA.ID_OCORRENCIA != "+str(OrdemServico.Id))

if queryLotacao.Rows.Count != 0:
    osNum = queryLotacao.Rows[0]["NUMERO"]
    Criticas.AdicionaPendencia("Já existe a seguinte ordem de serviço para o mês e/ou ano referente: " + str(osNum))
```
**ScriptFormCarregado**
```python
Formulario['SIM_NAO'].Itens = 'Integral;Proporcional'
#Formulario['SIM_NAO'].Valor = 'Integral'

Formulario['VALOR_QUALIF'].Habilitado = False
Formulario['VALOR_QUALIF'].Visivel = False


Formulario['VALOR'].Habilitado = False
Formulario['VALOR'].Visivel = False
Formulario['ANO_REF'].Visivel = True

Formulario['VALOR_DOD'].Visivel = False


Formulario['TE_UOR'].Habilitado = False
Formulario["TE_UOR"].Visivel = False
Formulario['TE_MATRICULA'].Habilitado = False
Formulario['TE_MATRICULA'].Visivel = False
Formulario['MATRICULA'].Habilitado = False
Formulario['MATRICULA'].Visivel = False

Formulario['TE_VALOR_REEMBOLSO'].Visivel = False
```
- Operação PR0001 Preencher Campos: RotuloPreenchimento=Abertura
  - TE_MATRICULA "Matrícula" [TextBox String → CPE_CSC.TE_MATRICULA] obrigatório
  - TE_UOR "UOR" [TextBox String → CPE_CSC.TE_UOR] obrigatório
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - SIM_NAO "Integral ou proporcional? Quando do ingresso no sistema de locação de veículos da frota BBTS, o colaborador deverá escolher a opção de pagamento PROPORCIONAL se sua entrada ocorrer no mês em andamento, levando em consideração os dias de utilização no mês em questão. Para os meses seguintes, optar pela modalidade de pagamento INTEGRAL. " [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
**SIM_NAO.ScriptModificado**
```python
if Formulario['SIM_NAO'].Valor == 'Proporcional':
    Formulario['VALOR_QUALIF'].Habilitado = True
    Formulario['VALOR_QUALIF'].Visivel = True
    #Formulario['TE_VALOR_REEMBOLSO'].Habilitado = False
    #Formulario['TE_VALOR_REEMBOLSO'].Visivel = True
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = False
    #Formulario['TE_VALOR_REEMBOLSO'].Valor = 0
    
else:
    Formulario['VALOR_QUALIF'].Habilitado = False
    Formulario['VALOR_QUALIF'].Visivel = False
    #Formulario['TE_VALOR_REEMBOLSO'].Habilitado = False
    #Formulario['TE_VALOR_REEMBOLSO'].Visivel = False
    Formulario['VALOR'].Visivel = True
    Formulario['VALOR'].Habilitado = False
    #Formulario['VALOR'].Valor = 0
```
  - VALOR_QUALIF "Quantidade de dias de utilização do veículo no mês" [TextBox Decimal → CPE_FINANCEIRO.VALOR_QUALIF] obrigatório
  - MES_REFERENCIA "Mês de referencia" [DropDownList String(2) → CPE_CSC.MES_REFERENCIA] obrigatório
  - ANO_REF "Ano referência" [DropDownList String(4) → CPE_CSC.ANO_REF] obrigatório
**ANO_REF.ScriptModificado**
```python
if Formulario['ANO_REF'].Valor == "2024":
    if Formulario['SIM_NAO'].Valor == 'Proporcional':
        Formulario['VALOR'].Valor = Formulario['VALOR_QUALIF'].Valor*(300.00 / 30)
    else:
        Formulario['VALOR'].Valor = 300.00    
else:
    if Formulario['SIM_NAO'].Valor == 'Proporcional':
        Formulario['VALOR'].Valor = Formulario['VALOR_QUALIF'].Valor*(600.00 / 30)
    else:
        Formulario['VALOR'].Valor = 600.00

#if Formulario['ANO_REF'].Valor == '2024':
#    Formulario['VALOR'].Valor = 300.00
#    Formulario['TE_VALOR_REEMBOLSO'].Valor = 300.00
#else:
#    Formulario['VALOR'].Valor = 600.00
#    Formulario['TE_VALOR_REEMBOLSO'].Valor = 600.00



    
##diasTotais = Convert.ToInt32(OrdemServico.GetCustom('VALOR_DOD'))
```
  - VALOR "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR] obrigatório
  - TE_VALOR_REEMBOLSO "Valor para reembolso" [TextBox Decimal → CPE_CSC.TE_VALOR_REEMBOLSO] obrigatório
**TE_VALOR_REEMBOLSO.ScriptModificado**
```python
Formulario["VALOR"].Valor == Formulario["TE_VALOR_REEMBOLSO"].Valor
```
  - TE_NOME_EMPREGADO "Nome do empregado" [DropDownList String → CPE_CSC.TE_NOME_EMPREGADO] obrigatório
**TE_NOME_EMPREGADO.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
matricula = ""
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
    Formulario["TE_UOR"].Visivel = True
    Formulario['TE_MATRICULA'].Visivel = True
    #Formulario['MATRICULA'].Visivel = True

    #Formulario["TE_UOR"].Valor = orgaoFavorecido
    #Consulta o cargo e a função do Favorecido

lista = Utils.ExecuteDataTable("SELECT CASE WHEN p.cargo IS NOT NULL THEN p.cargo ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN cp.FUNCAO_GRATIFICADA IS NOT NULL THEN cp.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.DESC_COLABORADOR, CP.MATRICULA, C.FIM_DATA_FUNCAO, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON (C.NOME = P.NOME AND C.DATA_DE_DEMISSAO IS NULL) WHERE P.ID_PESSOA = '" + idFavorecidoCustom.ToString() + "'" )

for linha in lista.Rows:
    matricula = linha["MATRICULA"].ToString()

Formulario["TE_MATRICULA"].Valor = matricula.ToString()
Formulario['MATRICULA'].Valor = matricula.ToString()
Formulario["TE_UOR"].Valor = favorecidoCustom.Orgao.Sigla.ToString()
```
  - OUTROS "O empregado está ciente das regras previstas no Regulamento e que a indenização possui característica indenizatória. Logo, não incidirá Imposto de Renda - IR, Contribuição Previdenciária - INSS e Fundo de Garantia por tempo de Serviço - FGTS, sendo devida ao empregado somente enquanto aderir ao veículo da frota locada. Declara ainda que ainda que assinou o Termo de Responsabilidade e/ou Termo de Ciência de uso do veículo, o qual refletirá sua responsabilidade pela guarda e zelo do automóvel." [CheckBox Boolean → CPE_ORDEM_SERVICO.OUTROS] obrigatório
  - VALOR_DOD "Valor" [TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD]

## Papéis usados
### papel 1286: Fila Empresa B
Tipo=RelacaoPessoas | pessoas: Fila Empresa B
### papel 1287: Fila Empresa A
Tipo=RelacaoPessoas | pessoas: Fila Empresa A
### papel 1066: Gerente TE Favorecido 
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if (OrdemServico.GetCustom("TE_NOME_EMPREGADO")):
    favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("TE_NOME_EMPREGADO")))
    gestor = favorecidoBBTec.ObtemChefia(False)

    if favorecidoBBTec == gestor:
        gestor = gestor.Orgao.OrgaoPai.Gestor

    Atores.Adiciona(gestor, "Gerente do Favorecido")
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
### papel 751: Responsável
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
### papel 461: Fila CSC - Pendente de Aprovação
Tipo=RelacaoPessoas | pessoas: Fila CSC - Pendente de Aprovação
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 631: Cliente e Gerente Posição
Tipo=Composto
- composto por: Gerente Posição do Cliente (Script)
- composto por: Cliente (PessoaOrdemServico)

## Campos customizados usados (definição global)

### TE_NOME_EMPREGADO — Nome do empregado
DropDownList String → CPE_CSC.TE_NOME_EMPREGADO
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### TE_MATRICULA — Matrícula
TextBox String → CPE_CSC.TE_MATRICULA

### TE_UOR — UOR
TextBox String → CPE_CSC.TE_UOR
Descrição: Orgão

### DIAS — Dias
TextBox Integer → CPE_HOMOLOGACAO.DIAS

### MES_REFERENCIA — Mês referência
DropDownList String(2) → CPE_CSC.MES_REFERENCIA
Itens: 01;02;03;04;05;06;07;08;09;10;11;12

### ANO_REFERENCIA — Ano referência
DropDownList String → CPE_CSC.ANO_REFERENCIA

### EMPRESA_TERCEIRIZADA — Empresa Terceirizada
TextBox String → CP_ORDEM_SERVICO.EMPRESA_TERCEIRIZADA
Descrição: Nome da Empresa Terceirizada

### VALOR — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR
Descrição: Informe

### TIPO_ATIVIDADE — Tipo de Atividade - informe
DropDownList String → CPE_CSC.TIPO_ATIVIDADE
Descrição: Tipo de Atividade - Informe
Itens: Atividade Meio; Atividade Fim; Não se Aplica

### DIAS_DE_TRA — DIAS DE TRAB
TextBox String(2) → CPE_PESSOAS.DIAS_DE_TRA
Descrição: DIAS DE TRABALHO

### ID_PERSON — ID pessoa ERP
TextBox String → CP_ORDEM_SERVICO.ID_PERSON

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### VALOR_QUALIF — Valor da Proposta - Qualificação Financeira
TextBox Decimal → CPE_FINANCEIRO.VALOR_QUALIF

### ANO_REF — Ano referência
DropDownList String(4) → CPE_CSC.ANO_REF
Itens: 2027;2026;2025

### TE_VALOR_REEMBOLSO — Valor para reembolso
TextBox Decimal → CPE_CSC.TE_VALOR_REEMBOLSO

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### SCR_PRESTADOR — UOR
TextBox String → CP_ORDEM_SERVICO.SCR_PRESTADOR
Descrição: UOR onde está lotado o prestador de serviço

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### QUANTIDADE — Quantidade
TextBox Integer → CP_ORDEM_SERVICO.QUANTIDADE

### OUTROS — Acesso Outros Sistemas
CheckBox Boolean → CPE_ORDEM_SERVICO.OUTROS

### VALOR_DOD — Valor
TextBox Decimal → CP_ORDEM_SERVICO.VALOR_DOD
Descrição: Valor do orçamento

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
