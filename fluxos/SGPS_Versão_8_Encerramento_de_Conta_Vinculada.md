# Fluxo: Encerramento de Conta Vinculada (1749) — versão 8
Caminho: Fluxos > SGPS Versão 8 Encerramento de Conta Vinculada
XML: `XMLs para teste/SGPS_Versão_8_Encerramento_de_Conta_Vinculada.xml` | Supravizio 19.1.1 | SubProcessoId 20750 | DesenhoProcessoId 2744 | ProcessoId 360
Órgão dono: None | Responsável: None
Classe do subprocesso: CriterioChargeBack=Nenhum; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Encerramento de conta vinculada (ENCVINCULADA)

## Grafo do fluxo
- [334418] Tarefa "Aguardar o "de acordo"  do gerente e fiscal." {Favorecido Todos} → [334292] Acompanhar internalização no V360 e verificar se h
- [330470] EventoInicial "" → [G75918] Há necessidade de repactuação?
- [334290] Tarefa "Cadastrar no SGPS" {Fila CSC SGPS} → [334418] Aguardar o  | [334300] 
- [334292] Tarefa "Acompanhar internalização no V360 e verificar se há pendências" {Fila CSC SGPS} → [G75919] Existem pendências?
- [334293] Tarefa "Solicitar liberação total do valor da conta" {Fila CSC SGPS} → [334294] 
- [334294] EventoFinal "" → (fim)
- [334295] Tarefa "Pré-Notificar o fornecedor" {Fila CSC SGPS} → [334301]  | [G75920] Foi atendido?
- [334296] Tarefa "Abrir OS de notificação ao fornecedor" {Fila CSC SGPS} → [334297] Finalização
- [334297] EventoFinal "Finalização" → (fim)
- [334304] EventoIntermediarioMensagem "Aviso de tempo" → [334295] Pré-Notificar o fornecedor
- [334300] EventoIntermediarioTimer "" → [334302] Aviso de tempo
- [334301] EventoIntermediarioTimer "" → [334304] Aviso de tempo
- [334302] EventoIntermediarioMensagem "Aviso de tempo" → [334290] Cadastrar no SGPS
- [G75919] Gateway "Existem pendências?" → «Sim» [334295] Pré-Notificar o fornecedor | «Não» [334293] Solicitar liberação total do valor da conta
- [G75920] Gateway "Foi atendido?" → «Não» [334296] Abrir OS de notificação ao fornecedor | «Sim» [334293] Solicitar liberação total do valor da conta
- [G75918] Gateway "Há necessidade de repactuação?" → «Não» [334293] Solicitar liberação total do valor da conta | «Sim» [334290] Cadastrar no SGPS

## Gateways
### [G75919] Existem pendências? (EventBasedExclusiveDecision)
- alternativa → [334295] Pré-Notificar o fornecedor: SequenciaAvaliacao=1; OperadorDecision=Equal; RotuloMotivo=Sim; ReferenciaDecision=Sim
- alternativa → [334293] Solicitar liberação total do valor da conta: SequenciaAvaliacao=2; OperadorDecision=Equal; RotuloMotivo=Não; ReferenciaDecision=Não
### [G75920] Foi atendido? (EventBasedExclusiveDecision)
- alternativa → [334296] Abrir OS de notificação ao fornecedor: SequenciaAvaliacao=0; OperadorDecision=Equal; RotuloMotivo=Não; ReferenciaDecision=Não
- alternativa → [334293] Solicitar liberação total do valor da conta: SequenciaAvaliacao=1; OperadorDecision=Equal; RotuloMotivo=Sim; ReferenciaDecision=Sim
### [G75918] Há necessidade de repactuação? (EventBasedExclusiveDecision)
- alternativa → [334293] Solicitar liberação total do valor da conta: SequenciaAvaliacao=1; OperadorDecision=Equal; RotuloMotivo=Não; ReferenciaDecision=Não
- alternativa → [334290] Cadastrar no SGPS: SequenciaAvaliacao=0; OperadorDecision=Equal; RotuloMotivo=Sim; ReferenciaDecision=Sim

## Atividades

### [334418] Tarefa "Aguardar o "de acordo"  do gerente e fiscal."
Responsável: Favorecido Todos (papel 385)
- Operação PR0002 Aprovar: DescricaoAssuntoAprovacao=Aprovação do termo.; MinimoAprovadores=1
  - (aprovação) SIM_NAO "Aprovado?" [DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO]
  - (aprovação) DESCRIÇÃO OPCIONAL "Observações" [Memo String → CP_ORDEM_SERVICO.DESCRIÇÃO_OPCIONAL] — Obrigatoriedade=Reprovacao
  - aprovador: Favorecido Todos (Unico)
  - aprovador: Favorecido Todos 2 (Unico)

### [330470] EventoInicial ""
Config: Configuracao={"ServicoIniciador":"<Nenhum>"}
TipoSolicitacao: 36.04. Suprimentos Corporativos, Licitações e Contratos - SGPS
- Operação PR0004 Associar Itens Configuração
  - anexo "Termo de Quitação Assinado" classes: Arquivo — RequeridoInicial=true
- Operação PR0001 Preencher Campos
  - FAVORECIDO_TODOS "Selecione o Gestor do Contrato" [DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS] obrigatório
  - FAVORECIDO_TODOS_2 "Selecione o Fiscal de Serviço" [DropDownList String → CPE_CONTRATOS.FAVORECIDO_TODOS_2] obrigatório

### [334290] Tarefa "Cadastrar no SGPS"
Responsável: Fila CSC SGPS (papel 1189)

### [334292] Tarefa "Acompanhar internalização no V360 e verificar se há pendências"
Responsável: Fila CSC SGPS (papel 1189)

### [334293] Tarefa "Solicitar liberação total do valor da conta"
Responsável: Fila CSC SGPS (papel 1189)

### [334294] EventoFinal ""

### [334295] Tarefa "Pré-Notificar o fornecedor"
Responsável: Fila CSC SGPS (papel 1189)
- Operação PR0001 Preencher Campos
  - DESCRICAO_DETALHADA "Pendências ou Observações" [Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA]

### [334296] Tarefa "Abrir OS de notificação ao fornecedor"
Responsável: Fila CSC SGPS (papel 1189)

### [334297] EventoFinal "Finalização"

### [334304] EventoIntermediarioMensagem "Aviso de tempo"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Aviso de tempo SGPS
Corpo do comunicado: Predazo(a), lembre-se de avançar a atividade!
OrdemServico.Atividade. Atenciosamente, Central da TI.

### [334300] EventoIntermediarioTimer ""
Config: TempoIntervalo=5760

### [334301] EventoIntermediarioTimer ""
Config: TempoIntervalo=5760

### [334302] EventoIntermediarioMensagem "Aviso de tempo"
Destinatário: Responsável atual (papel 36)
ModeloComunicado: Aviso de tempo SGPS
Corpo do comunicado: Predazo(a), lembre-se de avançar a atividade!
OrdemServico.Atividade. Atenciosamente, Central da TI.

## Papéis usados
### papel 385: Favorecido Todos
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Pessoa
from Venki.Supravizio.Processo.Custom import Ator
if OrdemServico.GetCustom("FAVORECIDO_TODOS"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))

    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```
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
### papel 1189: Fila CSC SGPS
Tipo=RelacaoPessoas | pessoas: Fila CSC SGPS
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

### SIM_NAO — Sim ou Nao
DropDownList String(50) → CP_ORDEM_SERVICO.SIM_NAO
Descrição: Selecione uma das opções.
Itens: Sim;Não

### DESCRIÇÃO OPCIONAL — Descrição opcional
Memo String → CP_ORDEM_SERVICO.DESCRIÇÃO_OPCIONAL

### FAVORECIDO_TODOS — Favorecido
DropDownList String → CP_ORDEM_SERVICO.FAVORECIDO_TODOS
**LookupScript**
```python
Itens = DB.ExecuteDataTable("SELECT DISTINCT to_char(p.id_pessoa) as  id_pessoa,  p.nome ||  ' (' || p.usuario_rede || ') - '||f.status_matricula as nomemat FROM CAD_FUNCIONARIO_V F inner join cp_pessoa cp on f.matricula = CP.matricula inner join PESSOA P on cp.id_pessoa = p.id_pessoa order by nomemat")
```

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

### DESCRICAO_DETALHADA — Descrição detalhada
Memo String(1000) → CPE_CSC.DESCRICAO_DETALHADA

## Biblioteca de scripts referenciada
teste
(fonte em catalogo/biblioteca/<Nome>.py)
