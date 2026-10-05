# SV_RECIPIENT

Caminho: Customização > Modelo de dados > Utilitários > SV_RECIPIENT

Destinatários de uma mensagem.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID** | Identificador da Mensagem. Este valor é acrescentados no Subject da mensagem. | int | number(6,0) | Não |
| **ADDRESS** | Endereço do destinatário da mensagem. | varchar(500) | varchar(500) | Não |
| **NAME** | Nome completo do Destinatário | varchar(500) | varchar(500) | Não |
| **LAST_EVENT** | Evento relacionado a mensagem | varchar(250) | varchar(250) | Não |
| **LAST_EVENT_DATE** | Data e hora de ocorrência do último evento relacionado com o destinatário. Este campo é preenchido pelo sistema no registro e pela rotina de envio de comunicados. | datetime | date | Não |
| **COMMENTS** | Comentários diversos sobre o envio | varchar(500) | varchar(500) | Sim |
| **ATTEMPTS** | Número de tentativas no envio que resultaram em erro (a mensagem não foi enviada). Este valor é incrementado pela rotina de envio de comunicados. | int | number(6,0) | Não |

Tabelas referenciadas por SV_RECIPIENT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_MESSAGE](dados_sv_message) | \| **SV_MESSAGE** \| **SV_RECIPIENT** \| \|---\|---\| \| ID \| ID \| |

**Exemplo 1: join com a tabela SV_MESSAGE**

```
select SV_RECIPIENT.*
from SV_RECIPIENT, SV_MESSAGE
where SV_RECIPIENT.ID = SV_MESSAGE.ID
```
