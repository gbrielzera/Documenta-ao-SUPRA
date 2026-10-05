# CodigoReferencia

Caminho: Customização > Modelo de objetos > Recurso > Contrato > CodigoReferencia

Código do contrato gerado pela área de suprimentos.

**Exemplo 1: modificação da propriedade CodigoReferencia**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade CodigoReferencia
contrato.CodigoReferencia = "Código referência";
# salva modificação da propriedade CodigoReferencia
Contrato.Salva(contrato)
```
