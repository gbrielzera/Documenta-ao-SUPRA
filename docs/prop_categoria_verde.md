# Verde

Caminho: Customização > Modelo de objetos > Processo > Categoria > Verde

Fator verde para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática.

**Exemplo 1: modificação da propriedade Verde**

```
# carrega objeto Categoria de identificador 1
categoria = Categoria.Carrega(1)
# modifica a propriedade Verde
categoria.Verde = 1;
# salva modificação da propriedade Verde
Categoria.Salva(categoria)
```
