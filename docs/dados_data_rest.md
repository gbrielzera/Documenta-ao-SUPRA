# DATA_REST

Caminho: Customização > Modelo de dados > Utilitários > DATA_REST

Filtra registros para edição em transações de cadastro.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ROLE** | Identificador do Perfil de acesso proprietário da regra | int | number(6,0) | Não |
| **ID_TRANSACTION** | Identificador da Transação proprietária da restrição | int | number(6,0) | Não |
| **ID_PROPERTY** | Identificador da Propriedade utilizada para comparação nos registros. | int | number(6,0) | Não |
| **OPERATOR** | Operador utilizado para montar a expressão utilizada como critério de filtro | varchar(250) | varchar(250) | Não |
| **VALUE_FORMULA** | Fórmula que será computada para formar expressão de filtro. | text | clob | Não |

Tabelas referenciadas por DATA_REST

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **DATA_REST** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [SV_AUTHORIZATION](dados_sv_authorization) | \| **SV_AUTHORIZATION** \| **DATA_REST** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| \| ID_TRANSACTION \| ID_TRANSACTION \| |

**Exemplo 1: join com a tabela SV_PROPERTY**

```
select DATA_REST.*, SV_PROPERTY.NAME
from DATA_REST, SV_PROPERTY
where DATA_REST.ID_PROPERTY = SV_PROPERTY.ID_PROPERTY
```
