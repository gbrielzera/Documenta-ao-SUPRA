# OPERACAO_ATIVIDADE

Caminho: Customização > Modelo de dados > Processo > OPERACAO_ATIVIDADE

Operação de uma Atividade

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OPERACAO_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | int | number(6,0) | Não |
| **ATIVO** | Quando Ativa uma Operação pode ser inicializada automaticamente (geração da solicitação de aprovação por exemplo). A Ativação da Operação também define o comportamento da rotina de Validação de Processo. Se Ativa a Validação é executada caso contrário é ignorada. | char(3) | char(3) | Não |
| **ID_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Atividade | int | number(6,0) | Não |
| **ID_OPERACAO** | Identificador do Operacao associado | int | number(6,0) | Não |
| **DESC_ASSUNTO_APROV** | Descritivo para Assunto da Aprovação | varchar(500) | varchar(500) | Sim |
| **BLOQUEAR_PENDENCIA** | Não permite a transição para a próxima atividade se existirem pendências de processo. | char(3) | char(3) | Não |
| **COPIAR_ANEXADOS** | Copiar para versão para aprovação todos os Itens associados na Ocorrência. Quando selecionado são ignoradas as configurações por Tipo de Item de Configuração. | char(3) | char(3) | Não |
| **MIN_APROV** | Quantidade mínima de aprovações para aprovação total da solicitação. A reprovação ocorre quando o número mínimo de aprovadores não pode ser atingido. Se este campo não for preenchido então a solicitação só é totalmente aprovada quando Todos aprovarem. | int | number(6,0) | Sim |
| **SEQUENCIA** | Sequência em que são apresentadas as operações de uma atividade. | int | number(6,0) | Não |
| **EXIGE_APROPRIACOES** | Exige que na aprovação sejam anexadas Apropriações de horas trabalhadas. | char(3) | char(3) | Não |
| **UTIL_ITEND_SOL** | A solicitação é pré-aprovada pelo usuário que solicitou o serviço utilizando o portal de Autoatendimento ou a transação Workspace. No caso do Autoatendimento este recurso só estará habilitado se não for permitida a troca de Cliente na tela de abertura. | char(3) | char(3) | Não |
| **REUTILIZA_APROV_ANT** | Reutiliza aprovações do mesmo aprovador em atividades anteriores no processo. São consideradas apenas solicitações aprovadas com sucesso. | char(3) | char(3) | Não |
| **ROTULO_PREENCH** | Descritivo utilizado como rótulo no agrupamento de campos criado no assistente de processos para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **INICIA_AUTOMATICO** | Inicia automaticamente quando iniciar a tarefa. | char(3) | char(3) | Não |
| **REPROVA_IMEDIATO** | A solicitação é totalmente reprovada assim que o primeiro avalidador realizar a reprovação. | char(3) | char(3) | Não |
| **REENVIO_EMAIL_APROV** | Frequência em horas do reenvio do email de aprovação. | int | number(6,0) | Sim |
| **ROTULO_APROVAR** | Rótulo do botao 'Aprovar' existente na página de aprovações da aplicação de Autoatendimento e no diálogo de aprovação do módulo solucionador. | varchar(100) | varchar(100) | Sim |
| **ROTULO_REPROVAR** | Rótulo do botao 'Reprovar' existente na página de aprovações da aplicação de Autoatendimento e no diálogo de aprovação do módulo solucionador. | varchar(100) | varchar(100) | Sim |

Tabelas referenciadas por OPERACAO_ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO](dados_operacao) | \| **OPERACAO** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO \| ID_OPERACAO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

Tabelas que dependem de OPERACAO_ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ASSUNTO_APROVACAO](dados_assunto_aprovacao) | \| **ASSUNTO_APROVACAO** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [FIGURA](dados_figura) | \| **FIGURA** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [CLASSE_APROVACAO](dados_classe_aprovacao) | \| **CLASSE_APROVACAO** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [APROVADOR_OPERACAO](dados_aprovador_operacao) | \| **APROVADOR_OPERACAO** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [CAMPO_PREENCH](dados_campo_preench) | \| **CAMPO_PREENCH** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [CLASSE_ANEXO](dados_classe_anexo) | \| **CLASSE_ANEXO** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [CAMPO_APROV](dados_campo_aprov) | \| **CAMPO_APROV** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [CAMPO_PREENCH_APROV](dados_campo_preench_aprov) | \| **CAMPO_PREENCH_APROV** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
| [REL_OPERACAO](dados_rel_operacao) | \| **REL_OPERACAO** \| **OPERACAO_ATIVIDADE** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

**Exemplo 1: join com a tabela OPERACAO**

```
select OPERACAO_ATIVIDADE.*, OPERACAO.DESCRICAO
from OPERACAO_ATIVIDADE, OPERACAO
where OPERACAO_ATIVIDADE.ID_OPERACAO = OPERACAO.ID_OPERACAO
```

**Exemplo 2: join com a tabela ATIVIDADE**

```
select OPERACAO_ATIVIDADE.*
from OPERACAO_ATIVIDADE, ATIVIDADE
where OPERACAO_ATIVIDADE.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```
