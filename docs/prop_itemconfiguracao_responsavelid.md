# ResponsavelId

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > ResponsavelId

Identificador da Pessoa associada

**Exemplo 1: modificação da propriedade ResponsavelId**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade ResponsavelId
itemConfiguracao.ResponsavelId = 1;
# salva modificação da propriedade ResponsavelId
ItemConfiguracao.Salva(itemConfiguracao)
```
