# RequestReadReceipt

Caminho: Customização > Modelo de objetos > Utilitários > Message > RequestReadReceipt

Configura a Mensagem para solicitar confirmação de leitura pelo usuário destinatário.

**Exemplo 1: modificação da propriedade RequestReadReceipt**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade RequestReadReceipt
message.RequestReadReceipt = true;
# salva modificação da propriedade RequestReadReceipt
Message.Salva(message)
```
