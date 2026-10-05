# Codigo

Caminho: Customização > Modelo de objetos > Processo > Indicador > Codigo

Código de identificação do Indicador

**Exemplo 1: modificação da propriedade Codigo**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade Codigo
indicador.Codigo = "IN001";
# salva modificação da propriedade Codigo
Indicador.Salva(indicador)
```
