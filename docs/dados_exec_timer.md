# EXEC_TIMER

Caminho: Customização > Modelo de dados > Processo > EXEC_TIMER

Execução de Eventos baseados em Tempo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATIVIDADE** | Identificador do(a) Atividade associado(a) | int | number(6,0) | Não |
| **DATA_HORA_EXEC** | Data e hora que o Timer foi executado com sucesso | datetime | date | Não |

Tabelas referenciadas por EXEC_TIMER

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **EXEC_TIMER** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
