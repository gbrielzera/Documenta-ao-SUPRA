# DataAceite

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > DataAceite

Data de aceite do Item

**Exemplo 1: modificação da propriedade DataAceite**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade DataAceite
itemConfiguracao.DataAceite = DateTime;
# salva modificação da propriedade DataAceite
ItemConfiguracao.Salva(itemConfiguracao)
```
