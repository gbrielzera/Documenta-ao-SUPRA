# Id

Caminho: Customização > Modelo de objetos > Recurso > ChargeBack > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ChargeBack de identificador 1
chargeBack = ChargeBack.Carrega(1)
# modifica a propriedade Id
chargeBack.Id = 1;
# salva modificação da propriedade Id
ChargeBack.Salva(chargeBack)
```
