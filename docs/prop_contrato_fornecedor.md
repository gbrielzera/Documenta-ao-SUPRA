# Fornecedor

Caminho: Customização > Modelo de objetos > Recurso > Contrato > Fornecedor

Um Fornecedor é uma tipo especial de Empresa habilitada como prestador de serviços para a área.

**Exemplo 1: modificação da propriedade Fornecedor**

```
# carrega objeto Contrato de identificador 51
contrato = Contrato.Carrega(51)
# modifica a propriedade Fornecedor
contrato.Fornecedor = Fornecedor.Carrega(94);
# salva modificação da propriedade Fornecedor
Contrato.Salva(contrato)
```
