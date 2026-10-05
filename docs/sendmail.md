# SendMail

Caminho: Recursos Avançados > Objeto Utils > SendMail

Envia um email utilizando o mecanismo de envio de comunicados do produto.

## Assinaturas

public void SendMail(string from, string to, string subject, string body)

public void SendMail(string from, string to, string subject, string body, string recoveryCode)

public void SendMail(string from, string to, string subject, string body, Venki.Core.Custom.SessionObjectProxy dataItem)

public void SendMail(string from, string to, string subject, string body, Venki.Core.Custom.SessionObjectProxy dataItem, int? temporality)

### from

### Remetente do e-mail

### to

Destinatário do e-mail

### subject

Campo assunto do e-mail enviado

### body

Corpo do e-mail

### dataItem

Registro do Supravizio que será associado a mensagem. Se for fornecido o objeto OrdemServico, por exemplo, a mensagem será exibida na aba de comunicados da respectiva Ordem de Serviço. Veja [Comunicados e Ordens de Serviço](comunicados).

### temporality

A temporalidade é o tempo (em dias) de vida da mensagem no banco de dados. A partir deste prazo a mensagem será removida liberando espaço no banco de dados.

### recoveryCode

Código que pode utilizado para recuperação da mensagem via comando SQL.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Finalização**

```
#Envia um e-mail confirmando a concessão de um acesso
Utils.SendMail("emailremetente@supravizio.com", "emaildestinatario@supravizio.com","Acesso Concedido.", "O acesso foi concedido com sucesso")
```
