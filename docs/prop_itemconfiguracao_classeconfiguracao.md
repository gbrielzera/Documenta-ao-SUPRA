# ClasseConfiguracao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ClasseConfiguracao

Tipo de Item de Configuração associado

**Exemplo 1: modificação da propriedade ClasseConfiguracao**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# modifica a propriedade ClasseConfiguracao
itemConfiguracao.ClasseConfiguracao = ClasseConfiguracao.Carrega(91);
# salva modificação da propriedade ClasseConfiguracao
ItemConfiguracao.Salva(itemConfiguracao)
```
