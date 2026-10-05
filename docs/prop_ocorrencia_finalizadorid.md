# FinalizadorId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > FinalizadorId

Identificador da pessoa que finalizou a ocorrência.

**Exemplo 1: modificação da propriedade FinalizadorId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade FinalizadorId
ocorrencia.FinalizadorId = 1;
# salva modificação da propriedade FinalizadorId
Ocorrencia.Salva(ocorrencia)
```
