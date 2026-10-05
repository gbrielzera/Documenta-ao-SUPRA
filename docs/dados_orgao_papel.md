# ORGAO_PAPEL

Caminho: Customização > Modelo de dados > Processo > ORGAO_PAPEL

Órgãos relacionados em um papel para recuperação de atores.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do papel proprietário da relação de órgãos. | int | number(6,0) | Não |
| **ID_ORGAO** | Identificador do Órgão associado | int | number(6,0) | Não |
| **REGRA_RECUPERA** | Define quais colaboradores do órgão devem ser recuperados | varchar(250) | varchar(250) | Não |
| **INCLUIR_SUB_NIVEIS** | Indica que órgãos filhos devem ser incluídos na recuperação. | char(3) | char(3) | Não |
| **TIPO_COLABORADOR** | Define que a regra deve recuperar somente Empregados, somente Terceiros ou todos os tipos. | varchar(250) | varchar(250) | Sim |

Tabelas referenciadas por ORGAO_PAPEL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORGAO](dados_orgao) | \| **ORGAO** \| **ORGAO_PAPEL** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **ORGAO_PAPEL** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |

**Exemplo 1: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select ORGAO_PAPEL.*
from ORGAO_PAPEL, PAPEL_CLASSE_NEGOCIO
where ORGAO_PAPEL.ID_PAPEL_CLASSE_NEGOCIO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```
