# Fluxo: Cadastro de Equipamento e Usuário TOA (CADEQUIPAMENTOTOA) — versão 2
Caminho: Fluxos > Rede de Atendimento Versão 2 Cadastro de Equipamento e Usuário TOA
XML: `XMLs para teste/Rede_de_Atendimento_Versão_2_Cadastro_de_Equipamento_e_Usuário_TOA.xml` | Supravizio 19.1.1 | SubProcessoId 7856 | DesenhoProcessoId 1163 | ProcessoId 123
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: SERGIO MARTINS DA SILVA
Classe do subprocesso: Objetivo=Atendimento as solicitações de alteração de cadastro de equipamento e cadastro do usuários do TOA; DescricaoCliente=Cadastro de Equipamento e Usuário TOA; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorMacroprocesso; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; ObjetivoPlano=Atendimento as solicitações de alteração de cadastro de equipamento e cadastro do usuários do TOA; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Cadastro de Equipamento (CADEQUIPAMENTO); Cadastro de Usuário TOA (CADUSUARIOTOA)

## Grafo do fluxo
- [126097] Tarefa "Conferir Informações e Cadastrar" {Responsável atual} → [G34748] Serviço realizado?
- [126098] EventoInicial "" {Solucionador serviço} → [126100] Aprovação do Gestor
- [126099] FimCancelamento "Cancelado" {Responsável atual} → (fim)
- [126100] Tarefa "Aprovação do Gestor" {Solucionador serviço} → [G34749] Gestor Aprovou?
- [126101] EventoIntermediarioMensagem "Mensagem de término" → [126102] 
- [126102] EventoFinal "" {Responsável atual} → (fim)
- [G34748] Gateway "Serviço realizado?" → «Não» [126099] Cancelado | «Sim» [126101] Mensagem de término
- [G34749] Gateway "Gestor Aprovou?" → «Aprovado» [126097] Conferir Informações e Cadastrar | «Reprovado» [126099] Cancelado

## Gateways
### [G34748] Serviço realizado? (EventBasedExclusiveDecision)
- alternativa → [126099] Cancelado: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=1
- alternativa → [126101] Mensagem de término: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=0
### [G34749] Gestor Aprovou? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.PossuiAprovacao("APROV_GESTOR")
```
- alternativa → [126097] Conferir Informações e Cadastrar: OperadorDecision=Equal; ReferenciaDecision=Aprovado; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
True
```
- alternativa → [126099] Cancelado: OperadorDecision=Equal; ReferenciaDecision=Reprovado; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [126097] Tarefa "Conferir Informações e Cadastrar"
Responsável: Responsável atual (papel 36)
**ScriptFormCarregado**
```python
#Alterar a visibilidade de todos os campos
for controle in Formulario.Controles:
    Formulario[controle.Key].Visivel = False
    Formulario[controle.Key].Habilitado = False

Formulario["ASST_SERVICO_ATENDIMENTO"].Visivel = True
Formulario["ASST_SERVICO_ATENDIMENTO"].Habilitado = True

#Popula o campo de acordo com o serviço
if OrdemServico.Servico.Sigla == "CADUSUARIOTOA":
    Formulario["ASST_SERVICO_ATENDIMENTO"].Itens = 'Alteração de endereço do técnico no TOA;Alteração da zona de Trabalho no TOA;Cancelamento de tarefa TOA'
else:
    Formulario["ASST_SERVICO_ATENDIMENTO"].Itens = 'Alteração de prefixo/sag;Alteração mantenedor;Cadastro(equipamento fora do parque)'
    
if Formulario["ASST_SERVICO_ATENDIMENTO"].Valor == "Alteração de prefixo/sag":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]

if Formulario["ASST_SERVICO_ATENDIMENTO"].Valor == "Alteração mantenedor":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO","ASST_MANTENEDO_CORRETO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO","ASST_MANTENEDO_CORRETO"] 
   
if Formulario["ASST_SERVICO_ATENDIMENTO"].Valor == "Cadastro(equipamento fora do parque)":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   

if Formulario["ASST_SERVICO_ATENDIMENTO"].Valor == "Alteração de endereço do técnico no TOA":
   camposVisiveis = ["ASST_NOME_FUNCIONARIO","ASST_MATRICULA","ASST_CEP","ASST_ENDERECO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_NOME_FUNCIONARIO","ASST_CEP","ASST_ENDERECO","ASST_OBSERVACAO"]

if Formulario["ASST_SERVICO_ATENDIMENTO"].Valor == "Alteração da zona de Trabalho no TOA":
   camposVisiveis = ["ASST_NOME_FUNCIONARIO","ASST_MATRICULA","ASST_ZONA_TRABALHO_ATUAL","ASST_ZONA_TRABALHO_ANTIGA","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_NOME_FUNCIONARIO","ASST_ZONA_TRABALHO_ATUAL","ASST_ZONA_TRABALHO_ANTIGA","ASST_OBSERVACAO"]
   
if Formulario["ASST_SERVICO_ATENDIMENTO"].Valor == "Cancelamento de tarefa TOA":
   camposVisiveis = ["ASST_NUMERO_CHAMADO","ASST_NUMERO_TAREFA","ASST_NUMERO_BEM","ASST_JUSTIFICATIVA"]
   camposHabilitados = ["ASST_NUMERO_CHAMADO","ASST_NUMERO_TAREFA","ASST_NUMERO_BEM","ASST_JUSTIFICATIVA"]
   
   
if Formulario["ASST_SERVICO_ATENDIMENTO"].Valor != None and Formulario["ASST_SERVICO_ATENDIMENTO"].Valor != '':
   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado

       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = True
              break
       Formulario[controle.Key].Visivel = visivel

       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = False
              break
       Formulario[controle.Key].Habilitado = habilitado
   Formulario["ASST_SERVICO_ATENDIMENTO"].Habilitado=False
```
- Operação PR0001 Preencher Campos
  - ASST_SERVICO_ATENDIMENTO "Tipo do Serviço" [DropDownList String → CPE_ASSTECNICA.ASST_SERVICO_ATENDIMENTO] obrigatório
**ASST_SERVICO_ATENDIMENTO.ScriptModificado**
```python
#controle de campos visíveis e habilitados
for controle in Formulario.Controles:
    Formulario[controle.Key].Visivel = False
    Formulario[controle.Key].Habilitado = False

Controle.Visivel = True
Controle.Habilitado = True


if Controle.Valor == "Alteração de prefixo/sag" or Controle.Valor == "Alteração mantenedor":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   
if Controle.Valor == "Cadastro(equipamento fora do parque)":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   

if Controle.Valor == "Alteração de endereço do técnico no TOA":
   camposVisiveis = ["ASST_NOME_FUNCIONARIO","ASST_MATRICULA","ASST_CEP","ASST_ENDERECO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_NOME_FUNCIONARIO","ASST_CEP","ASST_ENDERECO","ASST_OBSERVACAO"]

if Controle.Valor == "Alteração da zona de Trabalho no TOA":
   camposVisiveis = ["ASST_NOME_FUNCIONARIO","ASST_MATRICULA","ASST_ZONA_TRABALHO_ATUAL","ASST_ZONA_TRABALHO_ANTIGA","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_NOME_FUNCIONARIO","ASST_ZONA_TRABALHO_ATUAL","ASST_ZONA_TRABALHO_ANTIGA","ASST_OBSERVACAO"]
   
if Controle.Valor == "Cancelamento de tarefa TOA":
   camposVisiveis = ["ASST_NUMERO_CHAMADO","ASST_NUMERO_TAREFA","ASST_NUMERO_BEM","ASST_JUSTIFICATIVA"]
   camposHabilitados = ["ASST_NUMERO_CHAMADO","ASST_NUMERO_TAREFA","ASST_NUMERO_BEM","ASST_JUSTIFICATIVA"]
   
   
if Controle.Valor != None and Controle.Valor != '':
   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado

       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = True
              break
       Formulario[controle.Key].Visivel = visivel

       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = True
              break
       Formulario[controle.Key].Habilitado = habilitado
```
  - ASST_NUMERO_EQUIPAMENTO "Nº Bem do Equipamento" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_EQUIPAMENTO] obrigatório
  - ASST_TIPO_EQUIPAMENTO "Tipo Equipamento" [TextBox String → CPE_ASSTECNICA.ASST_TIPO_EQUIPAMENTO]
  - ASST_NUMERO_CONTRATO "Nº Contrato" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_CONTRATO]
  - ASST_INFORMAR_EQPT "Informar EQPT" [TextBox String → CPE_ASSTECNICA.ASST_INFORMAR_EQPT]
  - ASST_HOUVE_REMANEJAMENTO "Houve Remanejamento?" [DropDownList String → CPE_ASSTECNICA.ASST_HOUVE_REMANEJAMENTO]
  - ASST_SOLIC_TRANSBORDO " Houve Solicitação de Transbordo?" [DropDownList String → CPE_ASSTECNICA.ASST_SOLIC_TRANSBORDO]
  - ASST_CAT "Qual o CAT" [TextBox String → CPE_ASSTECNICA.ASST_CAT] obrigatório
  - ASST_LAT "Qual o LAT" [TextBox String → CPE_ASSTECNICA.ASST_LAT] obrigatório
  - ASST_MANTENEDO_CORRETO "Mantenedor Correto" [TextBox String → CPE_ASSTECNICA.ASST_MANTENEDO_CORRETO] obrigatório
  - ASST_PREFIXO_CORRETO "Prefixo Correto" [TextBox String → CPE_ASSTECNICA.ASST_PREFIXO_CORRETO] obrigatório
  - ASST_SAG_CORRETO "Sag Correto" [TextBox String → CPE_ASSTECNICA.ASST_SAG_CORRETO] obrigatório
  - ASST_NOME_FUNCIONARIO "Nome do Funcionário" [DropDownList String → CPE_ASSTECNICA.ASST_NOME_FUNCIONARIO]
**ASST_NOME_FUNCIONARIO.ScriptModificado**
```python
if Controle.Valor.ToString() != '' and Controle.Valor != None:
    Formulario["ASST_MATRICULA"].Valor = DB.ExecuteScalar("select cp.matricula from cp_pessoa cp where cp.id_pessoa = '"+ Controle.Valor.ToString()+"'")
else:
    Formulario["ASST_MATRICULA"].Valor = None
```
  - ASST_MATRICULA "Matrícula" [TextBox String → CPE_ASSTECNICA.ASST_MATRICULA] obrigatório
  - ASST_ENDERECO "Novo Endereço" [TextBox String(500) → CPE_ASSTECNICA.ASST_ENDERECO] obrigatório
  - ASST_CEP "CEP" [TextBox String → CPE_ASSTECNICA.ASST_CEP] obrigatório
  - ASST_ZONA_TRABALHO_ANTIGA "Zona de trabalho antiga" [TextBox String → CPE_ASSTECNICA.ASST_ZONA_TRABALHO_ANTIGA] obrigatório
  - ASST_ZONA_TRABALHO_ATUAL "Zona de trabalho atual" [TextBox String → CPE_ASSTECNICA.ASST_ZONA_TRABALHO_ATUAL] obrigatório
  - ASST_NUMERO_CHAMADO "Número do chamado" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_CHAMADO] obrigatório
  - ASST_NUMERO_TAREFA "Número da Tarefa" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_TAREFA] obrigatório
  - ASST_NUMERO_BEM "Número do bem" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_BEM] obrigatório
  - ASST_JUSTIFICATIVA "Justificativa" [Memo String(500) → CPE_ASSTECNICA.ASST_JUSTIFICATIVA] obrigatório
  - ASST_OBSERVACAO "Observação" [Memo String(500) → CPE_ASSTECNICA.ASST_OBSERVACAO]

### [126098] EventoInicial ""
Responsável: Solucionador serviço (papel 366)
TipoSolicitacao: Rede de Atendimento
**ScriptFormCarregado**
```python
import peopleSoft
# Fim do cabeçalho de importações de scripts. Para adicionar uma nova referência de script utilize o comando 'Importar bibliotecas de scripts'.

## Teste de consulta a API pode ser comentado caso atrapalhe o desenvolvimento
a=consultaAusencias('112359','01-12-2026')

for linha in a:
    matricula = linha["cdMatricula"].ToString()
    dataInicio = linha["dtInicio"].ToString()
    dataFim = linha["dtFim"].ToString()
    tipo = linha["nmTipoAbs"].ToString() 
    #return resultado
Formulario.ExibeMensagem('matricula :'+matricula.ToString()+ ' |dataInicio :'+dataInicio.ToString()+' |dataFim :'+dataFim.ToString()+' |Tipo :'+tipo.ToString())

b=consultaFuncionarios('A', '112359')

for linha in b:
    matricula = linha["cdMatricula"].ToString()
    local = linha["nmLocal"].ToString()
    nome = linha["nmNome"].ToString()
    #return resultado
Formulario.ExibeMensagem('matricula :'+matricula.ToString()+ ' |Local :'+local.ToString()+' |Nome :'+nome.ToString())

## Fim do Teste de consulta a API pode ser comentado caso atrapalhe o desenvolvimento

OrdemServico.Assunto = OrdemServico.Servico.Descricao
# Oculta todos os campos
for controle in Formulario.Controles:
    Formulario[controle.Key].Visivel = False
    Formulario[controle.Key].Habilitado = False
    Formulario[controle.Key].Valor = None

Formulario["ASST_SERVICO_ATENDIMENTO"].Visivel = True
Formulario["ASST_SERVICO_ATENDIMENTO"].Habilitado = True
Formulario["ASST_SERVICO_ATENDIMENTO"].Valor = None

#Popula o campo de acordo com o serviço
if OrdemServico.Servico.Sigla == "CADUSUARIOTOA":
    Formulario["ASST_SERVICO_ATENDIMENTO"].Itens = 'Alteração de endereço do técnico no TOA;Alteração da zona de Trabalho no TOA;Cancelamento de tarefa TOA'
else:
    Formulario["ASST_SERVICO_ATENDIMENTO"].Itens = 'Alteração de prefixo/sag;Alteração mantenedor;Cadastro(equipamento fora do parque)'
```
- Operação PR0001 Preencher Campos
  - ASST_SERVICO_ATENDIMENTO "Tipo do Serviço" [DropDownList String → CPE_ASSTECNICA.ASST_SERVICO_ATENDIMENTO] obrigatório
**ASST_SERVICO_ATENDIMENTO.ScriptModificado**
```python
#controle de campos visíveis e habilitados
for controle in Formulario.Controles:
    Formulario[controle.Key].Visivel = False
    Formulario[controle.Key].Habilitado = False

Controle.Visivel = True
Controle.Habilitado = True


if Controle.Valor == "Alteração de prefixo/sag":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]

if Controle.Valor == "Alteração mantenedor":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO","ASST_MANTENEDO_CORRETO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_HOUVE_REMANEJAMENTO", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_SOLIC_TRANSBORDO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO","ASST_MANTENEDO_CORRETO"]   
   
   
if Controle.Valor == "Cadastro(equipamento fora do parque)":
   camposVisiveis = ["ASST_CAT", "ASST_LAT", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_CAT", "ASST_LAT", "ASST_INFORMAR_EQPT","ASST_NUMERO_CONTRATO","ASST_NUMERO_EQUIPAMENTO","ASST_PREFIXO_CORRETO","ASST_SAG_CORRETO","ASST_TIPO_EQUIPAMENTO","ASST_OBSERVACAO"]
   

if Controle.Valor == "Alteração de endereço do técnico no TOA":
   camposVisiveis = ["ASST_NOME_FUNCIONARIO","ASST_MATRICULA","ASST_CEP","ASST_ENDERECO","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_NOME_FUNCIONARIO","ASST_CEP","ASST_ENDERECO","ASST_OBSERVACAO"]

if Controle.Valor == "Alteração da zona de Trabalho no TOA":
   camposVisiveis = ["ASST_NOME_FUNCIONARIO","ASST_MATRICULA","ASST_ZONA_TRABALHO_ATUAL","ASST_ZONA_TRABALHO_ANTIGA","ASST_OBSERVACAO"]
   camposHabilitados = ["ASST_NOME_FUNCIONARIO","ASST_ZONA_TRABALHO_ATUAL","ASST_ZONA_TRABALHO_ANTIGA","ASST_OBSERVACAO"]
   
if Controle.Valor == "Cancelamento de tarefa TOA":
   camposVisiveis = ["ASST_NUMERO_CHAMADO","ASST_NUMERO_TAREFA","ASST_NUMERO_BEM","ASST_JUSTIFICATIVA"]
   camposHabilitados = ["ASST_NUMERO_CHAMADO","ASST_NUMERO_TAREFA","ASST_NUMERO_BEM","ASST_JUSTIFICATIVA"]
   
   
if Controle.Valor != None and Controle.Valor != '':
   for controle in Formulario.Controles:
       # preserva a visibilidade atual dos campos
       visivel = Formulario[controle.Key].Visivel
       habilitado = Formulario[controle.Key].Habilitado

       for campo in camposVisiveis:
           if controle.Key == campo:
              visivel = True
              break
       Formulario[controle.Key].Visivel = visivel

       for campo in camposHabilitados:
           if controle.Key == campo:
              habilitado = True
              break
       Formulario[controle.Key].Habilitado = habilitado
```
  - ASST_NUMERO_EQUIPAMENTO "Nº bem do equipamento" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_EQUIPAMENTO] obrigatório
  - ASST_TIPO_EQUIPAMENTO "Tipo Equipamento" [TextBox String → CPE_ASSTECNICA.ASST_TIPO_EQUIPAMENTO]
  - ASST_NUMERO_CONTRATO "Nº Contrato" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_CONTRATO]
  - ASST_INFORMAR_EQPT "Informar EQPT" [TextBox String → CPE_ASSTECNICA.ASST_INFORMAR_EQPT]
  - ASST_HOUVE_REMANEJAMENTO "Houve Remanejamento?" [DropDownList String → CPE_ASSTECNICA.ASST_HOUVE_REMANEJAMENTO]
  - ASST_SOLIC_TRANSBORDO " Houve Solicitação de Transbordo?" [DropDownList String → CPE_ASSTECNICA.ASST_SOLIC_TRANSBORDO]
  - ASST_CAT "Qual o CAT" [TextBox String → CPE_ASSTECNICA.ASST_CAT] obrigatório
  - ASST_LAT "Qual o LAT" [TextBox String → CPE_ASSTECNICA.ASST_LAT] obrigatório
  - ASST_MANTENEDO_CORRETO "Mantenedor Correto" [TextBox String → CPE_ASSTECNICA.ASST_MANTENEDO_CORRETO] obrigatório
  - ASST_PREFIXO_CORRETO "Prefixo Correto" [TextBox String → CPE_ASSTECNICA.ASST_PREFIXO_CORRETO] obrigatório
  - ASST_SAG_CORRETO "Sag Correto" [TextBox String → CPE_ASSTECNICA.ASST_SAG_CORRETO] obrigatório
  - ASST_NOME_FUNCIONARIO "Nome do Funcionário" [DropDownList String → CPE_ASSTECNICA.ASST_NOME_FUNCIONARIO]
**ASST_NOME_FUNCIONARIO.ScriptModificado**
```python
if Controle.Valor.ToString() != '' and Controle.Valor != None:
    Formulario["ASST_MATRICULA"].Valor = DB.ExecuteScalar("select cp.matricula from cp_pessoa cp where cp.id_pessoa = '"+ Controle.Valor.ToString()+"'")
else:
    Formulario["ASST_MATRICULA"].Valor = None
```
  - ASST_MATRICULA "Matrícula" [TextBox String → CPE_ASSTECNICA.ASST_MATRICULA] obrigatório
  - ASST_ENDERECO "Novo Endereço" [TextBox String(500) → CPE_ASSTECNICA.ASST_ENDERECO] obrigatório
  - ASST_CEP "CEP" [TextBox String → CPE_ASSTECNICA.ASST_CEP] obrigatório
  - ASST_ZONA_TRABALHO_ANTIGA "Zona de trabalho antiga" [TextBox String → CPE_ASSTECNICA.ASST_ZONA_TRABALHO_ANTIGA] obrigatório
  - ASST_ZONA_TRABALHO_ATUAL "Zona de trabalho atual" [TextBox String → CPE_ASSTECNICA.ASST_ZONA_TRABALHO_ATUAL] obrigatório
  - ASST_NUMERO_CHAMADO "Número do chamado" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_CHAMADO] obrigatório
  - ASST_NUMERO_TAREFA "Número da Tarefa" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_TAREFA] obrigatório
  - ASST_NUMERO_BEM "Número do bem" [TextBox String → CPE_ASSTECNICA.ASST_NUMERO_BEM] obrigatório
  - ASST_JUSTIFICATIVA "Justificativa" [Memo String(500) → CPE_ASSTECNICA.ASST_JUSTIFICATIVA] obrigatório
  - ASST_OBSERVACAO "Observação" [Memo String(500) → CPE_ASSTECNICA.ASST_OBSERVACAO]
- Operação PR0004 Associar Itens Configuração
  - anexo "" classes: Anexo — RequeridoInicial=true

### [126099] FimCancelamento "Cancelado"
Responsável: Responsável atual (papel 36)

### [126100] Tarefa "Aprovação do Gestor"
Responsável: Solucionador serviço (papel 366)
Config: Codigo=APROV_GESTOR
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do Gestor
  - (aprovação) CSC_OBS2 "Observação" [Memo String(2000) → CPE_CSC.CSC_OBS2]
  - aprovador: Gerente Posição do Cliente (Unico)

### [126101] EventoIntermediarioMensagem "Mensagem de término"
Destinatário: Cliente (papel 18)
ModeloComunicado: Término de serviço CESEC
Corpo do comunicado: Prezado(a) OrdemServico.Cliente,
Em atendimento à Ordem de Serviço nº OrdemServico.Numero - OrdemServico.Assunto, comunico que foi realizado o término da atividade pelo Cesec.
Para mais detalhes sobre esta solicitação, clique no link a seguir ==> Link.Consulta.
Atenciosamente,
Central de Serviços

### [126102] EventoFinal ""
Responsável: Responsável atual (papel 36)
ClassePesquisaSatisfacao: Pesquisa de Satisfação - Assistência Técnica

## Papéis usados
### papel 36: Responsável atual
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Responsável
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
# adiciona o responsável pela OS na lista de atores do papel
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```
### papel 366: Solucionador serviço
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.Servico.ResponsávelTecnico
### papel 563: Gerente Posição do Cliente
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
#gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select cp.ID_PESSOA from CP_PESSOA cp inner join pessoa p on cp.id_pessoa = p.id_pessoa and p.ativo = 'Sim' WHERE MATRICULA = substr('"+favorecido["GESTOR_POSICAO"].ToString()+"',1,6)")))

gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor)
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

### ASST_SERVICO_ATENDIMENTO — Serviço para atendimento
DropDownList String → CPE_ASSTECNICA.ASST_SERVICO_ATENDIMENTO

### ASST_NUMERO_EQUIPAMENTO — Numero do Equipamento
TextBox String → CPE_ASSTECNICA.ASST_NUMERO_EQUIPAMENTO
Descrição: Numero do Bem do Equipamento

### ASST_TIPO_EQUIPAMENTO — Tipo Equipamento
TextBox String → CPE_ASSTECNICA.ASST_TIPO_EQUIPAMENTO

### ASST_NUMERO_CONTRATO — Número Contrato
TextBox String → CPE_ASSTECNICA.ASST_NUMERO_CONTRATO

### ASST_INFORMAR_EQPT — Informar EQPT
TextBox String → CPE_ASSTECNICA.ASST_INFORMAR_EQPT

### ASST_HOUVE_REMANEJAMENTO — Houve Remanejamento
DropDownList String → CPE_ASSTECNICA.ASST_HOUVE_REMANEJAMENTO
Itens: Sim;Não

### ASST_SOLIC_TRANSBORDO — Houve Solicitação de Transbordo
DropDownList String → CPE_ASSTECNICA.ASST_SOLIC_TRANSBORDO
Itens: Sim;Não

### ASST_CAT — CAT
TextBox String → CPE_ASSTECNICA.ASST_CAT
Descrição: CAT 

### ASST_LAT — LAT
TextBox String → CPE_ASSTECNICA.ASST_LAT

### ASST_MANTENEDO_CORRETO — Mantenedor Correto
TextBox String → CPE_ASSTECNICA.ASST_MANTENEDO_CORRETO

### ASST_PREFIXO_CORRETO — Prefixo Correto
TextBox String → CPE_ASSTECNICA.ASST_PREFIXO_CORRETO

### ASST_SAG_CORRETO — Sag Correto
TextBox String → CPE_ASSTECNICA.ASST_SAG_CORRETO

### ASST_NOME_FUNCIONARIO — Nome do Funcionário
DropDownList String → CPE_ASSTECNICA.ASST_NOME_FUNCIONARIO
**LookupScript**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
Itens = DB.ExecuteDataTable("select to_char(p.id_pessoa) as ID, cp.matricula||'-'||p.nome as descricao from Pessoa p inner join cp_pessoa cp on cp.id_pessoa=p.id_pessoa where p.ativo='Sim'")
```

### ASST_MATRICULA — Matrícula
TextBox String → CPE_ASSTECNICA.ASST_MATRICULA

### ASST_ENDERECO — Novo Endereço
TextBox String(500) → CPE_ASSTECNICA.ASST_ENDERECO

### ASST_CEP — CEP
TextBox String → CPE_ASSTECNICA.ASST_CEP

### ASST_ZONA_TRABALHO_ANTIGA — Zona de trabalho antiga
TextBox String → CPE_ASSTECNICA.ASST_ZONA_TRABALHO_ANTIGA

### ASST_ZONA_TRABALHO_ATUAL — Zona de trabalho atual
TextBox String → CPE_ASSTECNICA.ASST_ZONA_TRABALHO_ATUAL

### ASST_NUMERO_CHAMADO — Número do chamado
TextBox String → CPE_ASSTECNICA.ASST_NUMERO_CHAMADO

### ASST_NUMERO_TAREFA — Número da Tarefa
TextBox String → CPE_ASSTECNICA.ASST_NUMERO_TAREFA

### ASST_NUMERO_BEM — Número do bem
TextBox String → CPE_ASSTECNICA.ASST_NUMERO_BEM

### ASST_JUSTIFICATIVA — Justificativa
Memo String(500) → CPE_ASSTECNICA.ASST_JUSTIFICATIVA

### ASST_OBSERVACAO — Observação
Memo String(500) → CPE_ASSTECNICA.ASST_OBSERVACAO

### CSC_OBS2 — Observação
Memo String(2000) → CPE_CSC.CSC_OBS2

## Biblioteca de scripts referenciada
peopleSoft, teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
