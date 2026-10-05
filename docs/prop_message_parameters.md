# Parameters

Caminho: Customização > Modelo de objetos > Utilitários > Message > Parameters

Parâmetros de envio

**Exemplo 1: modificação da propriedade Parameters**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade Parameters
message.Parameters = "Parâmetros de envio";
# salva modificação da propriedade Parameters
Message.Salva(message)
```
