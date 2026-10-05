# ErrorDetails

Caminho: Customização > Modelo de objetos > Utilitários > Message > ErrorDetails

Relatório contendo detalhes sobre erros ocorridos durante o envio da mensagem.

**Exemplo 1: modificação da propriedade ErrorDetails**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade ErrorDetails
message.ErrorDetails = "Detalhes sobre erros de envio";
# salva modificação da propriedade ErrorDetails
Message.Salva(message)
```
