# TextualRepresention

Caminho: Customização > Modelo de objetos > Utilitários > Message > TextualRepresention

Representação textual do objeto de negócio associado com a Mensagem.

**Exemplo 1: modificação da propriedade TextualRepresention**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade TextualRepresention
message.TextualRepresention = "Registro associado";
# salva modificação da propriedade TextualRepresention
Message.Salva(message)
```
