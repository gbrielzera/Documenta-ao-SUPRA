# TipoPosse

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > TipoPosse

Tipo de Posse

**Exemplo 1: modificação da propriedade TipoPosse**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# modifica a propriedade TipoPosse
itemConfiguracao.TipoPosse = TipoPosse.Carrega(91);
# salva modificação da propriedade TipoPosse
ItemConfiguracao.Salva(itemConfiguracao)
```
