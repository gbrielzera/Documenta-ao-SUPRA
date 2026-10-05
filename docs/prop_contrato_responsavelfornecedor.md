# ResponsavelFornecedor

Caminho: Customização > Modelo de objetos > Recurso > Contrato > ResponsavelFornecedor

Nome da pessoa responsavável pelo Contrato pelo Fornecedor contratado.

**Exemplo 1: modificação da propriedade ResponsavelFornecedor**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade ResponsavelFornecedor
contrato.ResponsavelFornecedor = "Responsável Fornecedor";
# salva modificação da propriedade ResponsavelFornecedor
Contrato.Salva(contrato)
```
