# Localizacao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Localizacao

Localização do Item. Pode ser um local físico ou pessoa que utiliza

**Exemplo 1: modificação da propriedade Localizacao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade Localizacao
itemConfiguracao.Localizacao = "Localização";
# salva modificação da propriedade Localizacao
ItemConfiguracao.Salva(itemConfiguracao)
```
