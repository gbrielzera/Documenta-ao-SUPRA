# TIPO_EVENTO

Caminho: Customização > Modelo de dados > Processo > TIPO_EVENTO

Um Tipo de Evento define um marco (evento) ocorrido em uma Ocorrência de Processo. Este evento pode ser publicado para o Cliente para que este realize o acompanhamento da sua solicitação. Um Tipo de Evento pode representar também uma ferramenta de envio de comunicados para Pessoas diversas.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_TIPO_EVENTO** | Número sequencial gerado automaticamente pelo sistema para identificar um Tipo de Evento. Este número não pode ser modificado pelo usuário. | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente quando um Evento deste Tipo ocorre. | varchar(500) | varchar(500) | Não |
| **ATIVA_MENSAGENS** | Ativa ou desativa o Envio de Mensagens na ocorrência de eventos deste Tipo | char(3) | char(3) | Não |
| **CODIGO** | Código que identifica o Evento | varchar(50) | varchar(50) | Não |
| **NOME** | Nome Abreviado do Tipo de Evento | varchar(500) | varchar(500) | Não |
| **TIPO_MENSAGEM** | Tipo de Mensagem gerada | varchar(250) | varchar(250) | Não |
| **FONTE** | Fonte do Tipo de Evento que pode ser Usuário ou Sistema. Tipos de Eventos originados pelo Sistema não podem ser Removidos. | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **EXP_MENSAGEM** | Script para determinar a mensagem gerada no Evento | varchar(500) | varchar(500) | Sim |

Tabelas que dependem de TIPO_EVENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [EVENTO_OCORR](dados_evento_ocorr) | \| **EVENTO_OCORR** \| **TIPO_EVENTO** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |
| [CLASSE_APONTAMENTO](dados_classe_apontamento) | \| **CLASSE_APONTAMENTO** \| **TIPO_EVENTO** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |
| [GATILHO_ASSOC](dados_gatilho_assoc) | \| **GATILHO_ASSOC** \| **TIPO_EVENTO** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |
| [MENSAGEM_EVENTO](dados_mensagem_evento) | \| **MENSAGEM_EVENTO** \| **TIPO_EVENTO** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |
