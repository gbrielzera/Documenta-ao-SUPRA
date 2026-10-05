# TemporalityClassId

Caminho: Customização > Modelo de objetos > Utilitários > Message > TemporalityClassId

Identificador da classe que possui temporalidade.

**Exemplo 1: modificação da propriedade TemporalityClassId**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade TemporalityClassId
message.TemporalityClassId = 1;
# salva modificação da propriedade TemporalityClassId
Message.Salva(message)
```
