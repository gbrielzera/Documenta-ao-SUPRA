# DataDesativacao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > DataDesativacao

Data de desativação do Item.

**Exemplo 1: modificação da propriedade DataDesativacao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade DataDesativacao
itemConfiguracao.DataDesativacao = DateTime;
# salva modificação da propriedade DataDesativacao
ItemConfiguracao.Salva(itemConfiguracao)
```
