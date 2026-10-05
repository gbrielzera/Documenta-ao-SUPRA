# Ativo

Caminho: Customização > Modelo de objetos > Processo > Categoria > Ativo

Indica que a Categoria está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Categoria de identificador 1
categoria = Categoria.Carrega(1)
# modifica a propriedade Ativo
categoria.Ativo = true;
# salva modificação da propriedade Ativo
Categoria.Salva(categoria)
```
