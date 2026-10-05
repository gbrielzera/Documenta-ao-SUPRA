# SV_CUSTOM_CLASS

Caminho: Customização > Modelo de dados > Utilitários > SV_CUSTOM_CLASS

Customização de uma Classe de Negócio

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CUSTOM_CLASS** | Identificador do Assinante | int | number(6,0) | Não |
| **ID_CLASS** | Identificador da Classe | int | number(6,0) | Não |
| **TYPE_FULL_NAME** | Nome completo da Classe .NET incluindo Nome da Classe, Assembly, Culture e Public Token | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas referenciadas por SV_CUSTOM_CLASS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_DOMAIN](dados_sv_domain) | \| **SV_DOMAIN** \| **SV_CUSTOM_CLASS** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_CUSTOM_CLASS** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

**Exemplo 1: join com a tabela SV_DOMAIN**

```
select SV_CUSTOM_CLASS.*, SV_DOMAIN.NAME
from SV_CUSTOM_CLASS, SV_DOMAIN
where SV_CUSTOM_CLASS.ID_DOMAIN = SV_DOMAIN.ID_DOMAIN
```

**Exemplo 2: join com a tabela SV_CLASS**

```
select SV_CUSTOM_CLASS.*, SV_CLASS.NAME
from SV_CUSTOM_CLASS, SV_CLASS
where SV_CUSTOM_CLASS.ID_CLASS = SV_CLASS.ID_CLASS
```
