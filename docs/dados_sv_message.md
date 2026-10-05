# SV_MESSAGE

Caminho: Customização > Modelo de dados > Utilitários > SV_MESSAGE

Mensagens enviadas em resposta a Eventos ou ferramentas de comunicação do sistema.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID** | Identificador da Mensagem. Este valor é acrescentados no Subject da mensagem. | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **SUBJECT** | Campo Assunto da Mensagem. Em mensagens de respostas o assunto é acrescido do ID da Mensagem. | varchar(500) | varchar(500) | Não |
| **BODY** | Corpo da mensagem para envio. O formato pode ser configurado pela propriedade Mime-Format. | text | clob | Sim |
| **STATUS** | Situação da Mensagem | varchar(250) | varchar(250) | Não |
| **PRIORITY** | Prioridade que é atribuida para a Mensagem. Esta é a prioridade da mensagem enviada. | varchar(250) | varchar(250) | Não |
| **REQUEST_DATE** | Data e hora em que a Mensagem foi registrada | datetime | date | Não |
| **RECOVERY_CODE** | Código de recuperação para a Mensagem. Possui uso e preenchimento conforme critérios definidos pelo sistema usuário. | varchar(500) | varchar(500) | Sim |
| **FROM_ADDRESS** | Endereço de email remetente da mensagem. | varchar(500) | varchar(500) | Não |
| **MIME_FORMAT** | Formato MIME da Mensagem | varchar(500) | varchar(500) | Não |
| **REQUEST_READ_RECEIPT** | Configura a Mensagem para solicitar confirmação de leitura pelo usuário destinatário. | char(3) | char(3) | Não |
| **FROM_NAME** | Nome do remetente da mensagem | varchar(500) | varchar(500) | Sim |
| **ERROR_DETAIL** | Relatório contendo detalhes sobre erros ocorridos durante o envio da mensagem. | varchar(500) | varchar(500) | Sim |
| **ID_INITIAL** | Identificador da Mensagem inicial. Esta chave é utilizada para identificar respostas de mensagens iniciais. | int | number(6,0) | Sim |
| **KEY_VALUE** | Chave de recuperação do objeto associado com a Mensagem. | varchar(500) | varchar(500) | Sim |
| **TEXTUAL_REPRESENTATION** | Representação textual do objeto de negócio associado com a Mensagem. | varchar(500) | varchar(500) | Sim |
| **ID_CLASS** | Identificador da Classe de Negócio do objeto associado com a mensagem | int | number(6,0) | Sim |
| **PARAMETERS** | Parâmetros de envio | varchar(500) | varchar(500) | Sim |
| **PARAM_INFO** | Descritivo dos parâmetros de envio em formato legível pelo usuário. | varchar(500) | varchar(500) | Sim |
| **TEMPORALITY_EXP_DATE** | Após a data de expiração o registro de mensagem é excluído do sistema. | datetime | date | Sim |
| **ID_TEMPORALITY_CLASS** | Identificador da classe que possui temporalidade. | int | number(6,0) | Sim |
| **ID_TEMPORALITY** | Identificador da classe de temporalidade referenciada em TemporalityClass. | int | number(6,0) | Sim |
| **REPLY_ADDRESS** | Conta utilizada para reply quando o destinatário responder o comunicado. Quando não informada é utilizada a conta configurada no job de envio de emails. | varchar(100) | varchar(100) | Sim |

Tabelas referenciadas por SV_MESSAGE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_MESSAGE** \| \|---\|---\| \| ID_CLASS \| ID_TEMPORALITY_CLASS \| |
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_MESSAGE** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_MESSAGE](dados_sv_message) | \| **SV_MESSAGE** \| **SV_MESSAGE** \| \|---\|---\| \| ID \| ID_INITIAL \| |

Tabelas que dependem de SV_MESSAGE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_MESSAGE](dados_sv_message) | \| **SV_MESSAGE** \| **SV_MESSAGE** \| \|---\|---\| \| ID_INITIAL \| ID \| |
| [SV_RECIPIENT](dados_sv_recipient) | \| **SV_RECIPIENT** \| **SV_MESSAGE** \| \|---\|---\| \| ID \| ID \| |
| [SV_MESSAGE_ATTACH](dados_sv_message_attach) | \| **SV_MESSAGE_ATTACH** \| **SV_MESSAGE** \| \|---\|---\| \| ID \| ID \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_MESSAGE.*, SV_CLASS.NAME
from SV_MESSAGE left outer join SV_CLASS on SV_MESSAGE.ID_TEMPORALITY_CLASS = SV_CLASS.ID_CLASS
```

**Exemplo 2: join com a tabela SV_CLASS**

```
select SV_MESSAGE.*, SV_CLASS.NAME
from SV_MESSAGE left outer join SV_CLASS on SV_MESSAGE.ID_CLASS = SV_CLASS.ID_CLASS
```

**Exemplo 3: join com a tabela SV_MESSAGE**

```
select SV_MESSAGE.*, SV_MESSAGE2.SUBJECT
from SV_MESSAGE left outer join SV_MESSAGE SV_MESSAGE2 on SV_MESSAGE.ID_INITIAL = SV_MESSAGE2.ID
```
