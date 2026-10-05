# SV_CHANGE_LOG

Caminho: Customização > Modelo de dados > Utilitários > SV_CHANGE_LOG

Registro de modificação de um objeto.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHANGE_LOG** | Identificador da Modificação | decimal(15,2) | number(15,2) | Não |
| **TYPE** | Tipo de modificação que pode ser uma Inserção, Remoção ou Modificação propriamente dita. | varchar(250) | varchar(250) | Não |
| **DATE_TIME** | Data e hora da modificação | datetime | date | Não |
| **ID_DOMAIN** | Identificador do Domínio do Usuário quando ocorreu a modificação. Se o Usuário for transferido de Domínio este campo mantém histórico. | int | number(6,0) | Não |
| **ID_CLASS** | Identificador da Classe do Objeto modificado. | int | number(6,0) | Não |
| **ID_USER** | Identificador do Usuário que realizou a modificação. | int | number(6,0) | Não |
| **ID_CHANGE_LOG_PARENT** | Identificador da Modificação Pai. Este campo é preenchido para objetos que são Partes em associações do tipo Composition. | int | number(6,0) | Sim |
| **KEY_VALUE** | Chave de identificação do Objeto de Negócio modificado. | varchar(500) | varchar(500) | Não |
| **TEXTUAL_REPRESENTATION** | Representação textual do registro modificado | varchar(500) | varchar(500) | Não |
| **VERSION** | Número de Versão para o registro. | int | number(6,0) | Não |

Tabelas referenciadas por SV_CHANGE_LOG

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_CHANGE_LOG** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

Tabelas que dependem de SV_CHANGE_LOG

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CHANGE_ITEM](dados_sv_change_item) | \| **SV_CHANGE_ITEM** \| **SV_CHANGE_LOG** \| \|---\|---\| \| ID_CHANGE_LOG \| ID_CHANGE_LOG \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_CHANGE_LOG.*, SV_CLASS.NAME
from SV_CHANGE_LOG, SV_CLASS
where SV_CHANGE_LOG.ID_CLASS = SV_CLASS.ID_CLASS
```
