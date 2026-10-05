# APROPRIACAO

Caminho: Customização > Modelo de dados > Processo > APROPRIACAO

Apropriação de horas trabalhadas

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_APROPRIACAO** | Identificador da Apropriação | int | number(6,0) | Não |
| **REFERENCIA** | Referência da Apropriação | varchar(500) | varchar(500) | Sim |
| **ID_PESSOA** | Identificador da Pessoa associada | int | number(6,0) | Não |
| **DATA_HORA_APROPRIACAO** | Data/Hora da Apropriação | datetime | date | Não |

Tabelas referenciadas por APROPRIACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **APROPRIACAO** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |

Tabelas que dependem de APROPRIACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APROPRIACAO_APROVACAO](dados_apropriacao_aprovacao) | \| **APROPRIACAO_APROVACAO** \| **APROPRIACAO** \| \|---\|---\| \| ID_APROPRIACAO \| ID_APROPRIACAO \| |
| [TIME_SHEET_APROPRIADO](dados_time_sheet_apropriado) | \| **TIME_SHEET_APROPRIADO** \| **APROPRIACAO** \| \|---\|---\| \| ID_APROPRIACAO \| ID_APROPRIACAO \| |
