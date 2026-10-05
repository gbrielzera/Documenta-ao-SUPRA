# MENSAGEM_EVENTO

Caminho: Customização > Modelo de dados > Processo > MENSAGEM_EVENTO

Mensagens programadas para um determinado Evento.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_MENSAGEM_EVENTO** | Identificador da Mensagem configurada para o Tipo de Evento | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada sobre a Mensagem do Evento | varchar(500) | varchar(500) | Não |
| **ID_TIPO_EVENTO** | Identificador do Tipo de Evento | int | number(6,0) | Não |
| **ID_PROCESSO** | Identificador do Tipo de Serviço associado | int | number(6,0) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **SCRIPT_MENSAGEM** | Script para montagem da Mensagem a ser enviada. Neste script são preenchidos atributos do objeto Mensagem. Se não for preenchido qualquer um destes atributos então a mensagem não é enviada. | text | clob | Sim |
| **ID_MODELO_COMUNICA** | Identificador do Modelo de Comunicado associado | int | number(6,0) | Sim |
| **ID_PAPEL_DESTINATARIO** | Identificador do papel de processo que define o destinatário da mensagem | int | number(6,0) | Sim |
| **TEMPORALIDADE** | Define após quantos dias a mensagem será excluída da base de dados. Se for 0 (zero) ela será excluída assim que o email for enviado. Se estiver sem preenchimento a mensagem não será excluída. | int | number(6,0) | Sim |
| **LISTA_DESTINATARIOS** | Relação de endereços de emails separados por ponto e vírgula que são utilizados como destinatários do comunicado. Pode ser preenchido em conjunto com o papel de processo de Destinatários. | varchar(500) | varchar(500) | Sim |
| **ENDERECO_REPLY** | Endereço configurado para reply na mensagem enviada. Se não for configurado então será utilizada a caixa de email do job de envio de mensagens. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por MENSAGEM_EVENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PROCESSO](dados_processo) | \| **PROCESSO** \| **MENSAGEM_EVENTO** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |
| [MODELO_COMUNICA](dados_modelo_comunica) | \| **MODELO_COMUNICA** \| **MENSAGEM_EVENTO** \| \|---\|---\| \| ID_MODELO_COMUNICA \| ID_MODELO_COMUNICA \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **MENSAGEM_EVENTO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_DESTINATARIO \| |
| [TIPO_EVENTO](dados_tipo_evento) | \| **TIPO_EVENTO** \| **MENSAGEM_EVENTO** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |

**Exemplo 1: join com a tabela PROCESSO**

```
select MENSAGEM_EVENTO.*, PROCESSO.DESCRICAO
from MENSAGEM_EVENTO left outer join PROCESSO on MENSAGEM_EVENTO.ID_PROCESSO = PROCESSO.ID_PROCESSO
```

**Exemplo 2: join com a tabela MODELO_COMUNICA**

```
select MENSAGEM_EVENTO.*, MODELO_COMUNICA.DESCRICAO
from MENSAGEM_EVENTO left outer join MODELO_COMUNICA on MENSAGEM_EVENTO.ID_MODELO_COMUNICA = MODELO_COMUNICA.ID_MODELO_COMUNICA
```

**Exemplo 3: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select MENSAGEM_EVENTO.*, PAPEL_CLASSE_NEGOCIO.NOME
from MENSAGEM_EVENTO left outer join PAPEL_CLASSE_NEGOCIO on MENSAGEM_EVENTO.ID_PAPEL_DESTINATARIO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

**Exemplo 4: join com a tabela TIPO_EVENTO**

```
select MENSAGEM_EVENTO.*
from MENSAGEM_EVENTO, TIPO_EVENTO
where MENSAGEM_EVENTO.ID_TIPO_EVENTO = TIPO_EVENTO.ID_TIPO_EVENTO
```
