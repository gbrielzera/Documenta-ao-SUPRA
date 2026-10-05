# Publicado

Caminho: Customização > Modelo de objetos > Recurso > ChargeBack > Publicado

Indica que os dados do Charge-back são públicos para áreas Clientes na aplicação de Autoatendimento

**Exemplo 1: modificação da propriedade Publicado**

```
# carrega objeto ChargeBack de identificador 1
chargeBack = ChargeBack.Carrega(1)
# modifica a propriedade Publicado
chargeBack.Publicado = true;
# salva modificação da propriedade Publicado
ChargeBack.Salva(chargeBack)
```
