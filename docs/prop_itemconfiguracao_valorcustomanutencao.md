# ValorCustoManutencao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ValorCustoManutencao

Valor do Custo de Manutenção Mensal do Item

**Exemplo 1: modificação da propriedade ValorCustoManutencao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade ValorCustoManutencao
itemConfiguracao.ValorCustoManutencao = 0;
# salva modificação da propriedade ValorCustoManutencao
ItemConfiguracao.Salva(itemConfiguracao)
```
