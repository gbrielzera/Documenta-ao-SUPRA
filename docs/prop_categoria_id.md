# Id

Caminho: Customização > Modelo de objetos > Processo > Categoria > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma Categoria

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Categoria de identificador 1
categoria = Categoria.Carrega(1)
# modifica a propriedade Id
categoria.Id = 1;
# salva modificação da propriedade Id
Categoria.Salva(categoria)
```
