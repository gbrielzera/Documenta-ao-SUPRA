# MensagemEvento

Caminho: Customização > Modelo de objetos > Processo > MensagemEvento

Mensagens programadas para um determinado Evento.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada sobre a Mensagem do Evento | String |
| **EnderecoReply** | Endereço configurado para reply na mensagem enviada. Se não for configurado então será utilizada a caixa de email do job de envio de mensagens. | String |
| **Id** | Identificador da Mensagem configurada para o Tipo de Evento | Inteiro |
| **ListaDestinatarios** | Relação de endereços de emails separados por ponto e vírgula que são utilizados como destinatários do comunicado. Pode ser preenchido em conjunto com o papel de processo de Destinatários. | String |
| **ModeloComunicado** | Template utilizado para montar o corpo do email. | [ModeloComunicado](objetos_modelocomunicado) |
| **ModeloComunicadoId** | Identificador do Modelo de Comunicado associado | Inteiro |
| **PapelDestinatario** | Papel de processo que define os destinatários da mensagem | [PapelClasseNegocio](objetos_papelclassenegocio) |
| **PapelDestinatarioId** | Identificador do papel de processo que define o destinatário da mensagem | Inteiro |
| **Processo** | O envio da mensagem ocorre somente para Ordens de Serviço deste Processo. | [Processo](objetos_processo) |
| **ProcessoId** | Identificador do Tipo de Serviço associado | Inteiro |
| **ScriptMensagem** | Script para montagem da Mensagem a ser enviada. Neste script são preenchidos atributos do objeto Mensagem. Se não for preenchido qualquer um destes atributos então a mensagem não é enviada. | String |
| **Temporalidade** | Define após quantos dias a mensagem será excluída da base de dados. Se for 0 (zero) ela será excluída assim que o email for enviado. Se estiver sem preenchimento a mensagem não será excluída. | Inteiro |
| **TipoEventoId** | Identificador do Tipo de Evento | Inteiro |
