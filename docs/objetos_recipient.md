# Recipient

Caminho: Customização > Modelo de objetos > Utilitários > Recipient

Destinatários de uma mensagem.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Address** | Endereço do destinatário da mensagem. | String |
| **Attempts** | Número de tentativas no envio que resultaram em erro (a mensagem não foi enviada). Este valor é incrementado pela rotina de envio de comunicados. | Inteiro |
| **Comment** | Comentários diversos sobre o envio | String |
| **LastEvent** | Evento relacionado a mensagem | [MessageEvent](enum_messageevent) |
| **LastEventDate** | Data e hora de ocorrência do último evento relacionado com o destinatário. Este campo é preenchido pelo sistema no registro e pela rotina de envio de comunicados. | Data/hora |
| **MessageId** | Identificador da Mensagem. Este valor é acrescentados no Subject da mensagem. | Inteiro |
| **Name** | Nome completo do Destinatário | String |
