# MotivoCancelamento

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > MotivoCancelamento

Texto descrevendo motivo pelo qual o registro foi cancelado.

**Exemplo 1: modificação da propriedade MotivoCancelamento**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade MotivoCancelamento
ocorrencia.MotivoCancelamento = "Motivo cancelamento";
# salva modificação da propriedade MotivoCancelamento
Ocorrencia.Salva(ocorrencia)
```
