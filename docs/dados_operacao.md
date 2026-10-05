# OPERACAO

Caminho: Customização > Modelo de dados > Processo > OPERACAO

Uma Operação define uma Ação que pode ser configurada em uma Atividade de Processo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OPERACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Operacao | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada da Operacao | varchar(500) | varchar(500) | Não |
| **FONTE** | Fonte da Operação. | varchar(250) | varchar(250) | Não |
| **CODIGO** | Código da Operação | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de OPERACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **OPERACAO** \| \|---\|---\| \| ID_OPERACAO \| ID_OPERACAO \| |
