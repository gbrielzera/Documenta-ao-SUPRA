# ValorPrecoAquisicao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ValorPrecoAquisicao

Preço de aquisição do Item para demonstrativo de custeio pela rotina de Charge-back. O valor de aquisição é lançado no charge-back de competência relativa a Data de Entrega do Ativo.

**Exemplo 1: modificação da propriedade ValorPrecoAquisicao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade ValorPrecoAquisicao
itemConfiguracao.ValorPrecoAquisicao = 0;
# salva modificação da propriedade ValorPrecoAquisicao
ItemConfiguracao.Salva(itemConfiguracao)
```
