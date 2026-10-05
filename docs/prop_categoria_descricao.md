# Descricao

Caminho: Customização > Modelo de objetos > Processo > Categoria > Descricao

Descrição detalhada da Categoria

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Categoria de identificador 1
categoria = Categoria.Carrega(1)
# modifica a propriedade Descricao
categoria.Descricao = "Descrição";
# salva modificação da propriedade Descricao
Categoria.Salva(categoria)
```
