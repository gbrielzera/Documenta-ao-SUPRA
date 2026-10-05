# ModeloId

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ModeloId

Identificador do Modelo

**Exemplo 1: modificação da propriedade ModeloId**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade ModeloId
itemConfiguracao.ModeloId = 1;
# salva modificação da propriedade ModeloId
ItemConfiguracao.Salva(itemConfiguracao)
```
