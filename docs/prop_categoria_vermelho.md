# Vermelho

Caminho: Customização > Modelo de objetos > Processo > Categoria > Vermelho

Fator vermelho para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática.

**Exemplo 1: modificação da propriedade Vermelho**

```
# carrega objeto Categoria de identificador 1
categoria = Categoria.Carrega(1)
# modifica a propriedade Vermelho
categoria.Vermelho = 1;
# salva modificação da propriedade Vermelho
Categoria.Salva(categoria)
```
