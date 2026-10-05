# Subject

Caminho: Customização > Modelo de objetos > Utilitários > Message > Subject

Campo Assunto da Mensagem. Em mensagens de respostas o assunto é acrescido do ID da Mensagem.

**Exemplo 1: modificação da propriedade Subject**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade Subject
message.Subject = "Assunto";
# salva modificação da propriedade Subject
Message.Salva(message)
```
