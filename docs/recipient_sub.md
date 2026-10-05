# Receptores

Caminho: Janelas > Utilitários > Mensagens > Receptores

Destinatários de uma mensagem.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Endereço** | Endereço do destinatário da mensagem. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ADDRESS da tabela [SV_RECIPIENT](dados_sv_recipient). |
|---|---|
| **Nome** | Nome completo do Destinatário Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NAME da tabela [SV_RECIPIENT](dados_sv_recipient). |
| **Evento** | Evento relacionado a mensagem Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna LAST_EVENT da tabela [SV_RECIPIENT](dados_sv_recipient). |
| **Data/hora último evento** | Data e hora de ocorrência do último evento relacionado com o destinatário. Este campo é preenchido pelo sistema no registro e pela rotina de envio de comunicados. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna LAST_EVENT_DATE da tabela [SV_RECIPIENT](dados_sv_recipient). |
| **Comentários** | Comentários diversos sobre o envio |
| **Tentativas** | Número de tentativas no envio que resultaram em erro (a mensagem não foi enviada). Este valor é incrementado pela rotina de envio de comunicados. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATTEMPTS da tabela [SV_RECIPIENT](dados_sv_recipient). |
