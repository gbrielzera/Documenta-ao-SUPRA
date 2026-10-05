# DataExpiracaoGarantia

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > DataExpiracaoGarantia

Data para Expiração de uma eventual garantia

**Exemplo 1: modificação da propriedade DataExpiracaoGarantia**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade DataExpiracaoGarantia
itemConfiguracao.DataExpiracaoGarantia = DateTime;
# salva modificação da propriedade DataExpiracaoGarantia
ItemConfiguracao.Salva(itemConfiguracao)
```
