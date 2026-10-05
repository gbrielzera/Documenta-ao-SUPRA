# Priority

Caminho: Customização > Modelo de objetos > Utilitários > Message > Priority

Prioridade que é atribuida para a Mensagem. Esta é a prioridade da mensagem enviada.

**Exemplo 1: modificação da propriedade Priority**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade Priority
message.Priority = "Normal";
# salva modificação da propriedade Priority
Message.Salva(message)
```
