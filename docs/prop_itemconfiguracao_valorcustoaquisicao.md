# ValorCustoAquisicao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ValorCustoAquisicao

Custom total de aquisição do Item

**Exemplo 1: modificação da propriedade ValorCustoAquisicao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade ValorCustoAquisicao
itemConfiguracao.ValorCustoAquisicao = 0;
# salva modificação da propriedade ValorCustoAquisicao
ItemConfiguracao.Salva(itemConfiguracao)
```
