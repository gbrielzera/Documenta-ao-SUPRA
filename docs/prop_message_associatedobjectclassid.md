# AssociatedObjectClassId

Caminho: Customização > Modelo de objetos > Utilitários > Message > AssociatedObjectClassId

Identificador da Classe de Negócio do objeto associado com a mensagem

**Exemplo 1: modificação da propriedade AssociatedObjectClassId**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade AssociatedObjectClassId
message.AssociatedObjectClassId = 1;
# salva modificação da propriedade AssociatedObjectClassId
Message.Salva(message)
```
