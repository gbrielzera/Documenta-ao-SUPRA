# DataInicioValidade

Caminho: Customização > Modelo de objetos > Recurso > Contrato > DataInicioValidade

Data início de Validade do Contrato

**Exemplo 1: modificação da propriedade DataInicioValidade**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade DataInicioValidade
contrato.DataInicioValidade = DateTime;
# salva modificação da propriedade DataInicioValidade
Contrato.Salva(contrato)
```
