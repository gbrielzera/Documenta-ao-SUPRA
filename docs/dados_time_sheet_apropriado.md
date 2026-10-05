# TIME_SHEET_APROPRIADO

Caminho: Customização > Modelo de dados > Processo > TIME_SHEET_APROPRIADO

Apontamento Apropriado

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_APROPRIACAO** | Identificador da Apropriação | int | number(6,0) | Não |
| **ID_OCORRENCIA** | Identificador do(a) TimeSheet associado(a) | int | number(6,0) | Não |
| **SEQUENCIAL** | Identificador do(a) TimeSheet associado(a) | int | number(6,0) | Não |

Tabelas referenciadas por TIME_SHEET_APROPRIADO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIME_SHEET](dados_time_sheet) | \| **TIME_SHEET** \| **TIME_SHEET_APROPRIADO** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| \| SEQUENCIAL \| SEQUENCIAL \| |
| [APROPRIACAO](dados_apropriacao) | \| **APROPRIACAO** \| **TIME_SHEET_APROPRIADO** \| \|---\|---\| \| ID_APROPRIACAO \| ID_APROPRIACAO \| |

**Exemplo 1: join com a tabela APROPRIACAO**

```
select TIME_SHEET_APROPRIADO.*
from TIME_SHEET_APROPRIADO, APROPRIACAO
where TIME_SHEET_APROPRIADO.ID_APROPRIACAO = APROPRIACAO.ID_APROPRIACAO
```
