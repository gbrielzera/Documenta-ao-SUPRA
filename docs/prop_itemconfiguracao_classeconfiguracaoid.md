# ClasseConfiguracaoId

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ClasseConfiguracaoId

Identificador do Tipo de Item associado

**Exemplo 1: modificação da propriedade ClasseConfiguracaoId**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade ClasseConfiguracaoId
itemConfiguracao.ClasseConfiguracaoId = 1;
# salva modificação da propriedade ClasseConfiguracaoId
ItemConfiguracao.Salva(itemConfiguracao)
```
