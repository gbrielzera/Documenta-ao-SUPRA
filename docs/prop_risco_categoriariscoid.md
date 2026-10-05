# CategoriaRiscoId

Caminho: Customização > Modelo de objetos > Processo > Risco > CategoriaRiscoId

Identificador do CategoriaRisco associado

**Exemplo 1: modificação da propriedade CategoriaRiscoId**

```
# carrega objeto Risco de identificador 1
risco = Risco.Carrega(1)
# modifica a propriedade CategoriaRiscoId
risco.CategoriaRiscoId = 1;
# salva modificação da propriedade CategoriaRiscoId
Risco.Salva(risco)
```
