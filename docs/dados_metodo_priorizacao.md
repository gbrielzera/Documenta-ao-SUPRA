# METODO_PRIORIZACAO

Caminho: Customização > Modelo de dados > Processo > METODO_PRIORIZACAO

Define uma Metodologia para Priorização de Ocorrências e cálculo de ANS.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_METODO_PRIORIZACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Método de Priorização de Ocorrências. | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada da ClasseSeveridade | varchar(500) | varchar(500) | Não |
| **EXPRESSAO_CALCULO** | Expressão utilizada para determinar a base de cálculo utilizada para seleção do Grau de Prioridade a partir. Para seleção do Grau de Prioridade é selecionado aquele com Limite Superior maior que o valor resultante na Expressão. A expressão deve retornar obrigatoriamente um número Inteiro não negativo. | text | clob | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **CLASSE_NEGOCIO** | Classe de negócio da Ocorrência onde será aplicado o Método de Priorização. | varchar(250) | varchar(250) | Não |
| **CALCULO_AUTOMATICO** | Indica que o cálculo é automático sempre que ocorrer modificação no campos Cliente, Serviço ou quando for adicionado ou removido um Item de Configuração. | char(3) | char(3) | Não |
| **REFERENCIA** | Texto de referência sobre o Método de Priorização. Procure especificar neste campo qual o propósito e a aplicação deste Método de Priorização. | text | clob | Sim |

Tabelas que dependem de METODO_PRIORIZACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **METODO_PRIORIZACAO** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **METODO_PRIORIZACAO** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |
| [GRAU_PRIORIDADE](dados_grau_prioridade) | \| **GRAU_PRIORIDADE** \| **METODO_PRIORIZACAO** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |
| [VARIAVEL_PRIORIZACAO](dados_variavel_priorizacao) | \| **VARIAVEL_PRIORIZACAO** \| **METODO_PRIORIZACAO** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |
