# SV_REPORT_PARAM

Caminho: Customização > Modelo de dados > Utilitários > SV_REPORT_PARAM

Relação de parâmetros do relatório

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **NAME** | Nome do parâmetro definido no instante em que o usuário monta o comando SQL de select ou manualmente na janela de parâmetros. | varchar(500) | varchar(500) | Não |
| **ID_REPORT** | Identificador do relatório proprietário do parâmetro. | int | number(6,0) | Não |
| **TYPE** | Tipo de dado do parâmetro | varchar(500) | varchar(500) | Não |
| **LOOKUP_QUERY** | Relação de itens separados por ponto e vírtula ou consulta SQL utilizada para recuperar registros que servirão de opções. Todos estes itens são apresentados em um controle do tipo 'Combobox'. | text | clob | Sim |
| **ID_DB_CONNECTION** | Identificador da configuração de banco externo utilizado para alimentar os itens disponíveis para seleção no parâmetro. | int | number(6,0) | Sim |

Tabelas referenciadas por SV_REPORT_PARAM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_DB_CONNECTION](dados_sv_db_connection) | \| **SV_DB_CONNECTION** \| **SV_REPORT_PARAM** \| \|---\|---\| \| ID_DB_CONNECTION \| ID_DB_CONNECTION \| |
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **SV_REPORT_PARAM** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| |

**Exemplo 1: join com a tabela SV_DB_CONNECTION**

```
select SV_REPORT_PARAM.*, SV_DB_CONNECTION.SHORT_NAME
from SV_REPORT_PARAM left outer join SV_DB_CONNECTION on SV_REPORT_PARAM.ID_DB_CONNECTION = SV_DB_CONNECTION.ID_DB_CONNECTION
```

**Exemplo 2: join com a tabela SV_REPORT**

```
select SV_REPORT_PARAM.*
from SV_REPORT_PARAM, SV_REPORT
where SV_REPORT_PARAM.ID_REPORT = SV_REPORT.ID_REPORT
```
