# Id

Caminho: Customização > Modelo de objetos > Processo > CategoriaRisco > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um CategoriaRisco

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto CategoriaRisco de identificador 1
categoriaRisco = CategoriaRisco.Carrega(1)
# modifica a propriedade Id
categoriaRisco.Id = 1;
# salva modificação da propriedade Id
CategoriaRisco.Salva(categoriaRisco)
```
