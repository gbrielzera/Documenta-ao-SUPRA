# DataCadastro

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > DataCadastro

Data em que o Item de Configuração foi cadastrado no sistema.

**Exemplo 1: modificação da propriedade DataCadastro**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade DataCadastro
itemConfiguracao.DataCadastro = DateTime;
# salva modificação da propriedade DataCadastro
ItemConfiguracao.Salva(itemConfiguracao)
```
