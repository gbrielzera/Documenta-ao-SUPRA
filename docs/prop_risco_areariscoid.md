# AreaRiscoId

Caminho: Customização > Modelo de objetos > Processo > Risco > AreaRiscoId

Identificador do AreaRisco associado

**Exemplo 1: modificação da propriedade AreaRiscoId**

```
# carrega objeto Risco de identificador 1
risco = Risco.Carrega(1)
# modifica a propriedade AreaRiscoId
risco.AreaRiscoId = 1;
# salva modificação da propriedade AreaRiscoId
Risco.Salva(risco)
```
