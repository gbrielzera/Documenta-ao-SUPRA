# AssociatedObjectClass

Caminho: Customização > Modelo de objetos > Utilitários > Message > AssociatedObjectClass

Classe de Negócio do objeto associado com a Mensagem

**Exemplo 1: modificação da propriedade AssociatedObjectClass**

```
# carrega objeto Message de identificador 94
message = Message.Carrega(94)
# modifica a propriedade AssociatedObjectClass
message.AssociatedObjectClass = Class.Carrega(57);
# salva modificação da propriedade AssociatedObjectClass
Message.Salva(message)
```
