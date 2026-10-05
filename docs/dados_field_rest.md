# FIELD_REST

Caminho: Customização > Modelo de dados > Utilitários > FIELD_REST

Desabilita ou oculta campos em transações de cadastro.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ROLE** | Identificador do Perfil de acesso proprietário da regra | int | number(6,0) | Não |
| **ID_TRANSACTION** | Identificador da Transação proprietária da restrição | int | number(6,0) | Não |
| **ID_PROPERTY** | Identificador da Propriedade utilizada para modificação de regra de visualização | int | number(6,0) | Não |
| **ACTION** | Ação aplicada na restrição de visualização de campo | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por FIELD_REST

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **FIELD_REST** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [SV_AUTHORIZATION](dados_sv_authorization) | \| **SV_AUTHORIZATION** \| **FIELD_REST** \| \|---\|---\| \| ID_ROLE \| ID_ROLE \| \| ID_TRANSACTION \| ID_TRANSACTION \| |

**Exemplo 1: join com a tabela SV_PROPERTY**

```
select FIELD_REST.*, SV_PROPERTY.NAME
from FIELD_REST, SV_PROPERTY
where FIELD_REST.ID_PROPERTY = SV_PROPERTY.ID_PROPERTY
```
