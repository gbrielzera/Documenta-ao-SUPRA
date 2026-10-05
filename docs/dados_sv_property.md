# SV_PROPERTY

Caminho: Customização > Modelo de dados > Utilitários > SV_PROPERTY

Propriedades nativas de uma Classe de Negócio.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PROPERTY** | Identificador da Propriedade | int | number(6,0) | Não |
| **ID_CLASS** | Idenficador da Classe | int | number(6,0) | Não |
| **NAME** | Nome da Propriedade | varchar(100) | varchar(100) | Não |
| **TEXT** | Descrição resumida da Propriedade. Este texto é utilizado como rótulo para a propriedades em telas cadastro (CRUD) | varchar(500) | varchar(500) | Não |
| **DESCRIPTION** | Descrição completa da Propriedade. Este descritivo é utilizado para documentação de telas de cadastro. | text | clob | Não |
| **ORIGINAL_TEXT** | Descrição resumida Original da Propriedade | varchar(500) | varchar(500) | Não |
| **ORIGINAL_DESCRIPTION** | Descrição completa Original da Propriedade | text | clob | Não |
| **TYPE** | Tipo de dados da Propriedade conforme biblioteca de tipos da tecnologia Microsoft .NET | varchar(100) | varchar(100) | Não |
| **IS_TEXTUAL_REPRES** | Indica que a propriedade identifica textualmente uma classe | char(3) | char(3) | Não |
| **CHAR_CASE** | Caixa baixa, caixa alta, normal ou entrada de senha | varchar(250) | varchar(250) | Não |
| **TABLE_COLUMN** | Coluna de tabela que mantém a propriedade. Válido apenas para Classes de Entidade. | varchar(100) | varchar(100) | Sim |
| **LENGTH** | Tamanho de campos do tipo string. | int | number(6,0) | Sim |
| **PRIMARY_KEY** | Indica que o campo faz parte da chave primária da tabela de banco de dados | char(3) | char(3) | Não |

Tabelas referenciadas por SV_PROPERTY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_PROPERTY** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

Tabelas que dependem de SV_PROPERTY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PROPERTY_LAYOUT](dados_sv_property_layout) | \| **SV_PROPERTY_LAYOUT** \| **SV_PROPERTY** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [SV_CUSTOM_PROPERTY_SCOPE](dados_sv_custom_property_scope) | \| **SV_CUSTOM_PROPERTY_SCOPE** \| **SV_PROPERTY** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [DATA_REST](dados_data_rest) | \| **DATA_REST** \| **SV_PROPERTY** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [FIELD_REST](dados_field_rest) | \| **FIELD_REST** \| **SV_PROPERTY** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |
| [SV_LOCALIZATION](dados_sv_localization) | \| **SV_LOCALIZATION** \| **SV_PROPERTY** \| \|---\|---\| \| ID_PROPERTY \| ID_PROPERTY \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_PROPERTY.*
from SV_PROPERTY, SV_CLASS
where SV_PROPERTY.ID_CLASS = SV_CLASS.ID_CLASS
```
