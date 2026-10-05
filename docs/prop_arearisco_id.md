# Id

Caminho: Customização > Modelo de objetos > Processo > AreaRisco > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um AreaRisco

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto AreaRisco de identificador 1
areaRisco = AreaRisco.Carrega(1)
# modifica a propriedade Id
areaRisco.Id = 1;
# salva modificação da propriedade Id
AreaRisco.Salva(areaRisco)
```
