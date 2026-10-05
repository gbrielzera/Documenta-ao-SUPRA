# ValorPrecoManutencao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ValorPrecoManutencao

Preço de Charge-back de manutenção mensal

**Exemplo 1: modificação da propriedade ValorPrecoManutencao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade ValorPrecoManutencao
itemConfiguracao.ValorPrecoManutencao = 0;
# salva modificação da propriedade ValorPrecoManutencao
ItemConfiguracao.Salva(itemConfiguracao)
```
