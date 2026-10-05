# Id

Caminho: Customização > Modelo de objetos > Utilitários > Message > Id

Identificador da Mensagem. Este valor é acrescentados no Subject da mensagem.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade Id
message.Id = 1;
# salva modificação da propriedade Id
Message.Salva(message)
```
