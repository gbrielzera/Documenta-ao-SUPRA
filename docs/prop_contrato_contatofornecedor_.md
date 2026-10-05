# ContatoFornecedor

Caminho: Customização > Modelo de objetos > Recurso > Contrato > ContatoFornecedor

Telefone ou email de contato com Responsável pelo Contrato pelo Fornecedor.

**Exemplo 1: modificação da propriedade ContatoFornecedor**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade ContatoFornecedor
contrato.ContatoFornecedor = "CT 0101/2009";
# salva modificação da propriedade ContatoFornecedor
Contrato.Salva(contrato)
```
