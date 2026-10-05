# Descricao

Caminho: Customização > Modelo de objetos > Processo > CategoriaRisco > Descricao

Descrição detalhada do CategoriaRisco

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto CategoriaRisco de identificador 1
categoriaRisco = CategoriaRisco.Carrega(1)
# modifica a propriedade Descricao
categoriaRisco.Descricao = "Descrição";
# salva modificação da propriedade Descricao
CategoriaRisco.Salva(categoriaRisco)
```
