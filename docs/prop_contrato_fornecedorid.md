# FornecedorId

Caminho: Customização > Modelo de objetos > Recurso > Contrato > FornecedorId

Identificador do Fornecedor associado

**Exemplo 1: modificação da propriedade FornecedorId**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade FornecedorId
contrato.FornecedorId = 1;
# salva modificação da propriedade FornecedorId
Contrato.Salva(contrato)
```
