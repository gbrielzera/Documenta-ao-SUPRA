# ATOR_ITEM

Caminho: Customização > Modelo de dados > Ativos > ATOR_ITEM

Atores

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATOR_ITEM** | Número sequencial gerado automaticamente pelo sistema para Identificar um AtoresItem | int | number(6,0) | Não |
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do PapelClasseNegocio associado | int | number(6,0) | Não |
| **ID_ITEM** | Item de Configuração proprietário da redefinição de Papel | int | number(6,0) | Não |
| **ID_PAPEL_REDIR** | Identificador do Papel utilizado para redirecionamento. | int | number(6,0) | Sim |
| **ID_PESSOA** | Identificador da Pessoa atribuída como Ator para o Papel | int | number(6,0) | Sim |

Tabelas referenciadas por ATOR_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **ATOR_ITEM** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_REDIR \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **ATOR_ITEM** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ATOR_ITEM** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [ITEM](dados_item) | \| **ITEM** \| **ATOR_ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela ITEM**

```
select ATOR_ITEM.*
from ATOR_ITEM, ITEM
where ATOR_ITEM.ID_ITEM = ITEM.ID_ITEM
```
