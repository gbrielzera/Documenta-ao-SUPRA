# DataEntrega

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > DataEntrega

Data em que o Item foi entregue

**Exemplo 1: modificação da propriedade DataEntrega**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade DataEntrega
itemConfiguracao.DataEntrega = DateTime;
# salva modificação da propriedade DataEntrega
ItemConfiguracao.Salva(itemConfiguracao)
```
