# SV_PICTURE

Caminho: Customização > Modelo de dados > Utilitários > SV_PICTURE

Figura utilizada em diversos outros objetos

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PICTURE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Picture | int | number(6,0) | Não |
| **TEXTUAL_REPRESENTATION** | Representação textual do objeto de negócio proprietário da figura | varchar(500) | varchar(500) | Sim |
| **DESCRIPTION** | Descrição detalhada sobre o conteúdo da imagem. | varchar(500) | varchar(500) | Sim |
| **ID_CLASS** | Identificador da classe de negócio do objeto proprietário da figura | int | number(6,0) | Não |
| **KEY_VALUE** | Chave primária do objeto de negócio proprietário da figura | varchar(500) | varchar(500) | Sim |
| **FORMAT** | Extensão do arquivo informando o formato da figura | varchar(500) | varchar(500) | Sim |
| **CONTENT** | Conteúdo binário da figura | varbinary(4000) | blob | Não |
| **CREATION** | Data e hora em que a figura foi inserida no banco de dados. | datetime | date | Não |
| **LAST_ACCESS** | Data e hora do último acesso a figura. Esta data/hora é gravada de forma assíncrona pela página que realiza este acesso. | datetime | date | Sim |
| **TEMPORALITY** | Prazo em dias para manutenção da figura no banco de dados. Este prazo tem como referência o último acesso a figura. | int | number(6,0) | Sim |

Tabelas referenciadas por SV_PICTURE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_PICTURE** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

Tabelas que dependem de SV_PICTURE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_MESSAGE_ATTACH](dados_sv_message_attach) | \| **SV_MESSAGE_ATTACH** \| **SV_PICTURE** \| \|---\|---\| \| ID_PICTURE \| ID_PICTURE \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_PICTURE.*, SV_CLASS.NAME
from SV_PICTURE, SV_CLASS
where SV_PICTURE.ID_CLASS = SV_CLASS.ID_CLASS
```
