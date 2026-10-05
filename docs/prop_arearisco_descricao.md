# Descricao

Caminho: Customização > Modelo de objetos > Processo > AreaRisco > Descricao

Descrição detalhada do AreaRisco

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto AreaRisco de identificador 1
areaRisco = AreaRisco.Carrega(1)
# modifica a propriedade Descricao
areaRisco.Descricao = "Descrição";
# salva modificação da propriedade Descricao
AreaRisco.Salva(areaRisco)
```
