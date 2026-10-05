# CategoriaRisco

Caminho: Customização > Modelo de objetos > Processo > Risco > CategoriaRisco

Categoria do Risco

**Exemplo 1: modificação da propriedade CategoriaRisco**

```
# carrega objeto Risco de identificador 78
risco = Risco.Carrega(78)
# modifica a propriedade CategoriaRisco
risco.CategoriaRisco = CategoriaRisco.Carrega(23);
# salva modificação da propriedade CategoriaRisco
Risco.Salva(risco)
```
