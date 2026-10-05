# TipoEvento

Caminho: Customização > Modelo de objetos > Processo > TipoEvento

Um Tipo de Evento define um marco (evento) ocorrido em uma Ocorrência de Processo. Este evento pode ser publicado para o Cliente para que este realize o acompanhamento da sua solicitação. Um Tipo de Evento pode representar também uma ferramenta de envio de comunicados para Pessoas diversas.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AtivaMensagens** | Ativa ou desativa o Envio de Mensagens na ocorrência de eventos deste Tipo | Booleano |
| **Codigo** | Código que identifica o Evento | String |
| **Descricao** | Texto que descreve claramente quando um Evento deste Tipo ocorre. | String |
| **ExpressaoMensagem** | Script para determinar a mensagem gerada no Evento | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para identificar um Tipo de Evento. Este número não pode ser modificado pelo usuário. | Inteiro |
| **Mensagens** | Template de mensagens que serão enviadas quando ocorrer um Evento deste Tipo | [Lista de MensagemEvento](objetos_mensagemevento) |
| **Nome** | Nome Abreviado do Tipo de Evento | String |
| **TipoMensagem** | Tipo de Mensagem gerada | [TipoMensagem](enum_tipomensagem) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | TipoEvento Carrega(int i); |
| **Novo** | Cria um novo registro do tipo TipoEvento | TipoEvento Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | TipoEvento Carrega(string nomePropriedade, object valorPropriedade); |
