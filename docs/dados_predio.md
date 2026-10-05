# PREDIO

Caminho: Customização > Modelo de dados > Recurso > PREDIO

Um Prédio define uma edificação dentro de uma Unidade de Negócio onde estão localizados Clientes ou Ativos (Itens de Configuração).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PREDIO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Predio | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Predio | varchar(500) | varchar(500) | Não |
| **ID_UNIDADE_NEGOCIO** | Identificador da Unidade de Negócio que possui o Prédio | int | number(6,0) | Sim |

Tabelas referenciadas por PREDIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [UNIDADE_NEGOCIO](dados_unidade_negocio) | \| **UNIDADE_NEGOCIO** \| **PREDIO** \| \|---\|---\| \| ID_UNIDADE_NEGOCIO \| ID_UNIDADE_NEGOCIO \| |

Tabelas que dependem de PREDIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [LOCAL](dados_local) | \| **LOCAL** \| **PREDIO** \| \|---\|---\| \| ID_PREDIO \| ID_PREDIO \| |

**Exemplo 1: join com a tabela UNIDADE_NEGOCIO**

```
select PREDIO.*
from PREDIO, UNIDADE_NEGOCIO
where PREDIO.ID_UNIDADE_NEGOCIO = UNIDADE_NEGOCIO.ID_UNIDADE_NEGOCIO
```
