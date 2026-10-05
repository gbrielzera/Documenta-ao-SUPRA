# DataFimValidade

Caminho: Customização > Modelo de objetos > Recurso > Contrato > DataFimValidade

Data de fim de Validade do Contrato

**Exemplo 1: modificação da propriedade DataFimValidade**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade DataFimValidade
contrato.DataFimValidade = DateTime;
# salva modificação da propriedade DataFimValidade
Contrato.Salva(contrato)
```
