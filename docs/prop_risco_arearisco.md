# AreaRisco

Caminho: Customização > Modelo de objetos > Processo > Risco > AreaRisco

Área de Risco

**Exemplo 1: modificação da propriedade AreaRisco**

```
# carrega objeto Risco de identificador 78
risco = Risco.Carrega(78)
# modifica a propriedade AreaRisco
risco.AreaRisco = AreaRisco.Carrega(23);
# salva modificação da propriedade AreaRisco
Risco.Salva(risco)
```
