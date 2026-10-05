# Fluxo: Solicitação de Declarações (SOLICDECL) — versão 67
Caminho: Fluxos > Gestão de Pessoas - Serviços Gerais Versão 67 Solicitação de Declarações
XML: `XMLs para teste/Gestão_de_Pessoas_-_Serviços_Gerais_Versão_67_Solicitação_de_Declarações.xml` | Supravizio 19.1.1 | SubProcessoId 20383 | DesenhoProcessoId 2877 | ProcessoId 113
Órgão dono: 3000003210 - DIVISAO DE BENEFICIOS E MOVIMENTACOES DE PESSOAL | Responsável: PALOMA SABINE AMADO ROSA VARGAS
Classe do subprocesso: Objetivo=Solicitação de Declarações; DescricaoCliente=Solicitação de Declarações; MetodoPriorizacaoId=2; CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Solicitação de Declarações (SOLICDECL)

## Grafo do fluxo
- [325910] EventoFinal "Finalizado com sucesso" → (fim)
- [325911] FimCancelamento "Cancelado" → (fim)
- [325912] Tarefa "Emitir e anexar declaração para assinatura" {Responsável atual} → [325913] Solicitar assinatura da declaração
- [325913] EventoIntermediarioMensagem "Solicitar assinatura da declaração" → [331397] Aguardar assinatura do gerente
- [325915] EventoInicial "Solicitação de Declarações" → [325918] Verificar Solicitação
- [325916] EventoIntermediarioMensagem "Enviar notificação de atendido com sucesso" → [325910] Finalizado com sucesso
- [325917] EventoIntermediarioMensagem "Notificar cancelamento" → [325911] Cancelado
- [325918] Tarefa "Verificar Solicitação" {Fila CSC - Serviços Gestão Pessoas} → [G74307] Solicitação confere?
- [331397] Tarefa "Aguardar assinatura do gerente" {Favorecido Todos 2} → [336323] Alerta para assinatura (6h) | [G75159] Declaração está certa?
- [338499] Tarefa "Analisar documento assinado" {Fila CSC - Serviços Gestão Pessoas} → [G76592] Declaração assinada corretamente?
- [336323] EventoIntermediarioTimer "Alerta para assinatura (6h)" → [336324] Solicitar assinatura da declaração
- [336324] EventoIntermediarioMensagem "Solicitar assinatura da declaração" → [331397] Aguardar assinatura do gerente
- [G75159] Gateway "Declaração está certa?" → «Sim» [338499] Analisar documento assinado | «Não» [325912] Emitir e anexar declaração para assinatura
- [G74307] Gateway "Solicitação confere?" → «Sim» [325912] Emitir e anexar declaração para assinatura | «Não» [325917] Notificar cancelamento
- [G76592] Gateway "Declaração assinada corretamente?" → «Sim» [325916] Enviar notificação de atendido com sucesso | «Não» [325912] Emitir e anexar declaração para assinatura

## Gateways
### [G75159] Declaração está certa? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['SIM_NAO2'] == 'Sim'
```
- alternativa → [338499] Analisar documento assinado: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [325912] Emitir e anexar declaração para assinatura: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não
**ValorComparacaoDecision**
```python
False
```
### [G74307] Solicitação confere? (EventBasedExclusiveDecision)
- alternativa → [325912] Emitir e anexar declaração para assinatura: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
- alternativa → [325917] Notificar cancelamento: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
### [G76592] Declaração assinada corretamente? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico['SIM_NAO3'] == 'Sim'
```
- alternativa → [325916] Enviar notificação de atendido com sucesso: SequenciaAvaliacao=0; OperadorDecision=Equal; ReferenciaDecision=Sim; RotuloMotivo=Sim
**ValorComparacaoDecision**
```python
True
```
- alternativa → [325912] Emitir e anexar declaração para assinatura: SequenciaAvaliacao=1; OperadorDecision=Equal; ReferenciaDecision=Não; RotuloMotivo=Não
**ValorComparacaoDecision**
```python
False
```

## Atividades

### [325910] EventoFinal "Finalizado com sucesso"
ClassePesquisaSatisfacao: Pesquisa de Satisfação NPS - Cesec

### [325911] FimCancelamento "Cancelado"

### [325912] Tarefa "Emitir e anexar declaração para assinatura"
Responsável: Responsável atual (papel 36)
- Operação PR0004 Associar Itens Configuração: Nome=DECLARAÇÃO PARA ASSINATURA
  - anexo "Declaração para assinatura" classes: Declaração para assinatura — RequeridoInicial=true; PermiteMultiplosItens=true

### [325913] EventoIntermediarioMensagem "Solicitar assinatura da declaração"
Destinatário: Gestor Cesec (papel 807)
ModeloComunicado: Solicitar assinatura da declaração
Corpo do comunicado: Prezado(a),
Solicitamos a assinatura da declaração anexa para continuidade do processo. 
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2389; ClasseConfiguracao=Declaração para assinatura

### [325915] EventoInicial "Solicitação de Declarações"
TipoSolicitacao: 25.01. Gestão de Pessoas - Serviços Gerais
- Operação PR0001 Preencher Campos
  - ENDERECO_FORNECEDOR "Local de Trabalho BBTS (EX.: Brasília, Goiânia)" [TextBox String(300) → CP_ORDEM_SERVICO.ENDERECO_FORNECEDOR] obrigatório
  - CEP_ "CEP" [TextBox String → CPE_TIP_SOL01.CEP_] — Configuracao={"SalvaLiteralMascara":true, "Mascara":"00000\\-000"}
  - SIM_NAO "Soliticação é de Brasília?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO] obrigatório
  - FAVORECIDO_TODOS "Favorecido" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
**FAVORECIDO_TODOS.ScriptModificado**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
if Formulario["FAVORECIDO_TODOS"].Valor != "" and Formulario["FAVORECIDO_TODOS"].Valor != None:

    idFavorecidoCustom = Convert.ToInt32(Formulario["FAVORECIDO_TODOS"].Valor)
    favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
    if favorecidoCustom != None:
        Formulario["MATRICULA"].Valor = favorecidoCustom["MATRICULA"].ToString()
```
  - MATRICULA "Matrícula" [TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA] obrigatório
  - ESPECIFICACAO_DECLARACAO "Especificação da declaração solicitada" [TextBox String → CPE_ORDEM_SERVICO.ESPECIFICACAO_DECLARACAO]
- Operação PR0004 Associar Itens Configuração: Nome=ANEXO
  - anexo "" classes: Insumos para emissão da declaração — RequeridoInicial=true; PermiteMultiplosItens=true

### [325916] EventoIntermediarioMensagem "Enviar notificação de atendido com sucesso"
Destinatário: Cliente e Responsavel Atual (papel 544)
ModeloComunicado: Chamado atendido com sucesso
Corpo do comunicado: Prezado,
A Ordem de Serviço nº OrdemServico.Numero sobre o Assunto: OrdemServico.Assunto foi atendido com sucesso!
 Complemento1 
Para maiores informações Link.Consulta .
Atenciosamente,
Central de Serviços
- TiposAnexosMensagem:
  - ClasseConfiguracaoId=2395; ClasseConfiguracao=Declaração assinada

### [325917] EventoIntermediarioMensagem "Notificar cancelamento"
Destinatário: Cliente (papel 18)
ModeloComunicado: Chamado para cancelamento
Corpo do comunicado: Prezado(a),
O chamado interno OrdemServico - Solicitação de Declarações foi cancelado pelo motivo:
Motivo: Complemento1 
Caso queira consultar os detalhes desta solicitação clique aqui Link.Consulta.
Atenciosamente,
Central de Serviços

### [325918] Tarefa "Verificar Solicitação"
Responsável: Fila CSC - Serviços Gestão Pessoas (papel 583)
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS_2 "Selecione o gerente que irá assinar." [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_2] obrigatório

### [331397] Tarefa "Aguardar assinatura do gerente"
Responsável: Favorecido Todos 2 (papel 1379)
MotivoInterrupcaoSLA: Aguardando Ação de Interveniente Interno
- Operação PR0001 Preencher Campos
  - DESCRICAO1 "Campo para observações." [Memo String → CP_ORDEM_SERVICO.DESCRICAO1]
  - SIM_NAO2 "A declaração está certa?" [DropDownList String → CPE_CSC.SIM_NAO2]
**SIM_NAO2.ScriptModificado**
```python
Formulario['SIM_NAO2'].Itens = 'Sim;Não'
```
- Operação PR0004 Associar Itens Configuração: Nome=DECLARAÇÃO ASSINADA
  - anexo "Declaração anexada" classes: Declaração assinada — RequeridoInicial=true; PermiteMultiplosItens=true

### [338499] Tarefa "Analisar documento assinado"
Responsável: Fila CSC - Serviços Gestão Pessoas (papel 583)
- Operação PR0001 Preencher Campos
  - SIM_NAO3 "Declaração assinada corretamente?" [DropDownList String → CPE_CSC.SIM_NAO3] obrigatório
**SIM_NAO3.ScriptModificado**
```python
Formulario['SIM_NAO3'].Itens = 'Sim;Não'
```
  - DESCDOTACAO "Observações (OPCIONAL)" [Memo String → CPE_BOOTCAMP.DESCDOTACAO]

### [336323] EventoIntermediarioTimer "Alerta para assinatura (6h)"
Config: TempoIntervalo=360

### [336324] EventoIntermediarioMensagem "Solicitar assinatura da declaração"
Destinatário: Favorecido Todos 2 (papel 1379)
ModeloComunicado: Solicitar assinatura da declaração
Corpo do comunicado: Prezado(a),
Solicitamos a assinatura da declaração anexa para continuidade do processo. 
Para maiores informações Link.Consulta 
Atenciosamente,
Central de Serviços

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
### papel 807: Gestor Cesec
Tipo=RelacaoPessoas | pessoas: PATRICIA DA SILVA BARROS
### papel 544: Cliente e Responsavel Atual
Tipo=Composto
- composto por: Cliente (PessoaOrdemServico)
- composto por: Responsável atual (PessoaOrdemServico)
### papel 18: Cliente
Tipo=PessoaOrdemServico; NomeCampoOcorrencia=Nativo.OrdemServico.Cliente
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```
### papel 583: Fila CSC - Serviços Gestão Pessoas
Tipo=RelacaoPessoas | pessoas: Fila CSC - Serviços Gestão Pessoas
### papel 1379: Favorecido Todos 2
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Aprovador
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_TODOS_2"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS_2")))

    if favorecido != None:
        Atores.Adiciona(favorecido, "Aprovador")
```

## Campos customizados usados (definição global)

### ENDERECO_FORNECEDOR — Endereço
TextBox String(300) → CP_ORDEM_SERVICO.ENDERECO_FORNECEDOR

### CEP_ — CEP
TextBox String → CPE_TIP_SOL01.CEP_
Descrição: CEP:

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

### MATRICULA — Matrícula
TextBox Decimal → CP_ORDEM_SERVICO.MATRICULA

### ESPECIFICACAO_DECLARACAO — Especificacao  Declaracao
TextBox String → CPE_ORDEM_SERVICO.ESPECIFICACAO_DECLARACAO
Descrição: Especificacao Declaracao

### FAVORECIDO_TODOS_2 — Favorecido
DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_2
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")








#Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa WHERE f.status_matricula = 'Ativo' AND p.ativo = 'Sim' order by nomemat")

#sqlValor = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat, f.status_matricula, p.ATIVO FROM CAD_FUNCIONARIO_V F, PESSOA P WHERE F.NOME = P.NOME AND f.status_matricula = 'Ativo' AND p.ativo = 'Sim' AND P.ID_PESSOA = "+ValorCorrente

#sqlEntrada = "SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa, p.nome ||  ' (' || p.usuario_rede || ')' as nomemat, f.status_matricula, p.ATIVO FROM CAD_FUNCIONARIO_V F, PESSOA P WHERE F.NOME = P.NOME AND f.status_matricula = 'Ativo' AND p.ativo = 'Sim' AND UPPER(P.NOME) like UPPER('%"+EntradaUsuario+"%')"


#sqlOrder = " order by nomemat asc"
# 
#if not String.IsNullOrEmpty(ValorCorrente) and not String.IsNullOrEmpty(EntradaUsuario):
#
#   Itens = DB.ExecuteDataTable("(" + sqlValor + ") UNION (" + sqlEntrada + " ) " + sqlOrder)
# 
#elif String.IsNullOrEmpty(EntradaUsuario) and String.IsNullOrEmpty(ValorCorrente):
# 
#   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
#   #None
# 
#elif String.IsNullOrEmpty(EntradaUsuario):
#   
 #  Itens = DB.ExecuteDataTable( sqlValor + sqlOrder)
# 
#else:
#   
#   Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
```

### DESCRICAO1 — Caixa de texto
Memo String → CP_ORDEM_SERVICO.DESCRICAO1

### SIM_NAO2 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO2
Itens: Sim;Não

### SIM_NAO3 — Sim ou Não
DropDownList String → CPE_CSC.SIM_NAO3
Descrição: Informe
Itens: Sim;Não

### DESCDOTACAO — Descrição de Dotação
Memo String → CPE_BOOTCAMP.DESCDOTACAO

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
