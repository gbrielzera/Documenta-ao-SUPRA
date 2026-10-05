# SV_CUSTOM_PROPERTY_SCOPE

Caminho: Customização > Modelo de dados > Utilitários > SV_CUSTOM_PROPERTY_SCOPE

Escopo para Propriedades Customizadas. Se não for cadastrada restrição de Escopo então a Propriedade Customizada vale para todos os objetos da Classe associada

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CUSTOM_PROPERTY** | Identificador da Propriedade Customizada | int | number(6,0) | Não |
| **ID_PROPERTY** | Identificador da Propriedade | int | number(6,0) | Não |
| **VALUE_SCOPE** | Valor da Propriedade para habilitar a Propriedade Customizada | varchar(500) | varchar(500) | Não |
| **OPERATOR** | Operador: igual, menor, maior que etc. | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por SV_CUSTOM_PROPERTY_SCOPE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **SV_CUSTOM_PROPERTY_SCOPE** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [SV_CUSTOM_PROPERTY](dados_sv_custom_property) | \| **SV_CUSTOM_PROPERTY** \| **SV_CUSTOM_PROPERTY_SCOPE** \| \|---\|---\| \| ID_CUSTOM_PROPERTY \| ID_CUSTOM_PROPERTY \| |

**Exemplo 1: join com a tabela SV_PROPERTY**

```
select SV_CUSTOM_PROPERTY_SCOPE.*, SV_PROPERTY.NAME
from SV_CUSTOM_PROPERTY_SCOPE, SV_PROPERTY
where SV_CUSTOM_PROPERTY_SCOPE.ID_PROPERTY = SV_PROPERTY.ID_PROPERTY
```

**Exemplo 2: join com a tabela SV_CUSTOM_PROPERTY**

```
select SV_CUSTOM_PROPERTY_SCOPE.*
from SV_CUSTOM_PROPERTY_SCOPE, SV_CUSTOM_PROPERTY
where SV_CUSTOM_PROPERTY_SCOPE.ID_CUSTOM_PROPERTY = SV_CUSTOM_PROPERTY.ID_CUSTOM_PROPERTY
```
