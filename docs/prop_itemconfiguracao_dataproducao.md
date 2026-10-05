# DataProducao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > DataProducao

Data de entrada em Produção.

**Exemplo 1: modificação da propriedade DataProducao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade DataProducao
itemConfiguracao.DataProducao = DateTime;
# salva modificação da propriedade DataProducao
ItemConfiguracao.Salva(itemConfiguracao)
```
