# ResponsavelId

Caminho: Customização > Modelo de objetos > Recurso > Contrato > ResponsavelId

Identificador da Pessoa associada

**Exemplo 1: modificação da propriedade ResponsavelId**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade ResponsavelId
contrato.ResponsavelId = 1;
# salva modificação da propriedade ResponsavelId
Contrato.Salva(contrato)
```
