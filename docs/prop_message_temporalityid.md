# TemporalityId

Caminho: Customização > Modelo de objetos > Utilitários > Message > TemporalityId

Identificador da classe de temporalidade referenciada em TemporalityClass.

**Exemplo 1: modificação da propriedade TemporalityId**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade TemporalityId
message.TemporalityId = 1;
# salva modificação da propriedade TemporalityId
Message.Salva(message)
```
