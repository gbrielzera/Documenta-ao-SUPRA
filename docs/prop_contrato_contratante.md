# Contratante

Caminho: Customização > Modelo de objetos > Recurso > Contrato > Contratante

Empresa Contratante

**Exemplo 1: modificação da propriedade Contratante**

```
# carrega objeto Contrato de identificador 51
contrato = Contrato.Carrega(51)
# modifica a propriedade Contratante
contrato.Contratante = Empresa.Carrega(94);
# salva modificação da propriedade Contratante
Contrato.Salva(contrato)
```
