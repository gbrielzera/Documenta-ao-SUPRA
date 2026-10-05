# Azul

Caminho: Customização > Modelo de objetos > Processo > Categoria > Azul

Fator azul para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática.

**Exemplo 1: modificação da propriedade Azul**

```
# carrega objeto Categoria de identificador 1
categoria = Categoria.Carrega(1)
# modifica a propriedade Azul
categoria.Azul = 1;
# salva modificação da propriedade Azul
Categoria.Salva(categoria)
```
