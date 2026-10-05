# ValorCustoAquisicao

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > ValorCustoAquisicao

Valor do Custo de Aquisição Padrão para Itens do tipo. Este valor pode ser redefinido com o campo correspondente no Item.

**Exemplo 1: modificação da propriedade ValorCustoAquisicao**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade ValorCustoAquisicao
classeConfiguracao.ValorCustoAquisicao = 0;
# salva modificação da propriedade ValorCustoAquisicao
ClasseConfiguracao.Salva(classeConfiguracao)
```
