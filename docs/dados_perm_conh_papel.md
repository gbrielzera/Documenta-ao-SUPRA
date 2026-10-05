# PERM_CONH_PAPEL

Caminho: Customização > Modelo de dados > Ativos > PERM_CONH_PAPEL

Entidade responsavel por montar o relacionamento entre Conhecimento e Papel

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do PapelClasseNegocio associado | int | number(6,0) | Não |
| **ID_CONHECIMENTO** | Identifica o conhecimento associado | int | number(6,0) | Não |

Tabelas referenciadas por PERM_CONH_PAPEL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **PERM_CONH_PAPEL** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [CONHECIMENTO](dados_conhecimento) | \| **CONHECIMENTO** \| **PERM_CONH_PAPEL** \| \|---\|---\| \|  \| ID_CONHECIMENTO \| |

**Exemplo 1: join com a tabela CONHECIMENTO**

```
select PERM_CONH_PAPEL.*
from PERM_CONH_PAPEL, CONHECIMENTO
where PERM_CONH_PAPEL.ID_CONHECIMENTO = CONHECIMENTO.
```
