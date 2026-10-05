# NumeroSerie

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > NumeroSerie

Número de série do Item

**Exemplo 1: modificação da propriedade NumeroSerie**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade NumeroSerie
itemConfiguracao.NumeroSerie = "Número série";
# salva modificação da propriedade NumeroSerie
ItemConfiguracao.Salva(itemConfiguracao)
```
