# KeyValue

Caminho: Customização > Modelo de objetos > Utilitários > Message > KeyValue

Chave de recuperação do objeto associado com a Mensagem.

**Exemplo 1: modificação da propriedade KeyValue**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade KeyValue
message.KeyValue = "Chave objeto associado";
# salva modificação da propriedade KeyValue
Message.Salva(message)
```
