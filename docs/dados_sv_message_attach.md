# SV_MESSAGE_ATTACH

Caminho: Customização > Modelo de dados > Utilitários > SV_MESSAGE_ATTACH

Arquivo anexado na mensagem para envio.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID** | Identificador da Mensagem proprietária do arquivo anexado. | int | number(6,0) | Não |
| **FILE_NAME** | Nome completo do arquivo incluindo caminho onde está localizado. IMPORTATE: este arquivo deve estar disponível no instante em que a mensagem for enviada. | varchar(500) | varchar(500) | Não |
| **DELETE_AFTER_SENT** | O arquivo deve ser removido após o envil do email. | char(3) | char(3) | Não |
| **CONTENT_ID** | Contend Id de anexos inseridos na mensagem | varchar(500) | varchar(500) | Sim |
| **ATTACH_DELETED** | Indica que o arquivo foi removido na pasta de arquivos anexados que é mantido no servidor de arquivos. | char(3) | char(3) | Não |
| **ID_PICTURE** | Identificador do(a) Picture associado(a) | int | number(6,0) | Sim |

Tabelas referenciadas por SV_MESSAGE_ATTACH

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_PICTURE](dados_sv_picture) | \| **SV_PICTURE** \| **SV_MESSAGE_ATTACH** \| \|---\|---\| \| ID_PICTURE \| ID_PICTURE \| |
| [SV_MESSAGE](dados_sv_message) | \| **SV_MESSAGE** \| **SV_MESSAGE_ATTACH** \| \|---\|---\| \| ID \| ID \| |

**Exemplo 1: join com a tabela SV_PICTURE**

```
select SV_MESSAGE_ATTACH.*, SV_PICTURE.DESCRIPTION
from SV_MESSAGE_ATTACH left outer join SV_PICTURE on SV_MESSAGE_ATTACH.ID_PICTURE = SV_PICTURE.ID_PICTURE
```

**Exemplo 2: join com a tabela SV_MESSAGE**

```
select SV_MESSAGE_ATTACH.*
from SV_MESSAGE_ATTACH, SV_MESSAGE
where SV_MESSAGE_ATTACH.ID = SV_MESSAGE.ID
```
