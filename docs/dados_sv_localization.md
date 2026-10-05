# SV_LOCALIZATION

Caminho: Customização > Modelo de dados > Utilitários > SV_LOCALIZATION

Localização de objetos

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_CLASS** | Identificador da Classe de Negócio do objeto localilzado. | int | number(6,0) | Não |
| **ID_CULTURE** | Identificador da Cultura associada com a localização. | int | number(6,0) | Não |
| **ID_PROPERTY** | Identificador do(a) Property associado(a) | int | number(6,0) | Não |
| **ID** | Identificador do objeto de negócio localizado | int | number(6,0) | Não |
| **TEXTUAL_REPRESENTATION** | Representação textual do registro localizado | varchar(500) | varchar(500) | Não |
| **TEXT_VALUE** | Texto localizado | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por SV_LOCALIZATION

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_LOCALIZATION** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_CULTURE](dados_sv_culture) | \| **SV_CULTURE** \| **SV_LOCALIZATION** \| \|---\|---\| \| ID_CULTURE \| ID_CULTURE \| |
| [SV_PROPERTY](dados_sv_property) | \| **SV_PROPERTY** \| **SV_LOCALIZATION** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_LOCALIZATION.*, SV_CLASS.NAME
from SV_LOCALIZATION, SV_CLASS
where SV_LOCALIZATION.ID_CLASS = SV_CLASS.ID_CLASS
```

**Exemplo 2: join com a tabela SV_CULTURE**

```
select SV_LOCALIZATION.*, SV_CULTURE.DESCRIPTION
from SV_LOCALIZATION, SV_CULTURE
where SV_LOCALIZATION.ID_CULTURE = SV_CULTURE.ID_CULTURE
```

**Exemplo 3: join com a tabela SV_PROPERTY**

```
select SV_LOCALIZATION.*, SV_PROPERTY.NAME
from SV_LOCALIZATION, SV_PROPERTY
where SV_LOCALIZATION.ID_PROPERTY = SV_PROPERTY.ID_PROPERTY
```
