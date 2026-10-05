# LOCAL

Caminho: Customização > Modelo de dados > Recurso > LOCAL

Um Local pode representar um andar, sala ou outra unidade de um Prédio. Também são utilizados para definir localização de Clientes e Ativos (Itens de Configuração).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_LOCAL** | Número sequencial gerado automaticamente pelo sistema para Identificar um Local | int | number(6,0) | Não |
| **ID_PREDIO** | Identificador do Prédio que contém o Local | int | number(6,0) | Não |
| **COMPLEMENTO** | Complemento (sala ou andar) que identifica o Local | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Local está ativo no sistema. Quando inativo o local passa a não ser exibido na aplicação de Autoatendimento. | char(3) | char(3) | Não |

Tabelas referenciadas por LOCAL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PREDIO](dados_predio) | \| **PREDIO** \| **LOCAL** \| \|---\|---\| \| ID_PREDIO \| ID_PREDIO \| |

Tabelas que dependem de LOCAL

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **LOCAL** \| \|---\|---\| \| ID_LOCAL \| ID_LOCAL \| |

**Exemplo 1: join com a tabela PREDIO**

```
select LOCAL.*
from LOCAL, PREDIO
where LOCAL.ID_PREDIO = PREDIO.ID_PREDIO
```
