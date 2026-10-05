# Modelo

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Modelo

Modelo de Item de Configuração segundo especificação de um Fabricante.

**Exemplo 1: modificação da propriedade Modelo**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# modifica a propriedade Modelo
itemConfiguracao.Modelo = Modelo.Carrega(91);
# salva modificação da propriedade Modelo
ItemConfiguracao.Salva(itemConfiguracao)
```
