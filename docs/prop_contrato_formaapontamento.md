# FormaApontamento

Caminho: Customização > Modelo de objetos > Recurso > Contrato > FormaApontamento

Forma de definição de apontamentos, se por total de horas ou por período

**Exemplo 1: modificação da propriedade FormaApontamento**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade FormaApontamento
contrato.FormaApontamento = "Periodo";
# salva modificação da propriedade FormaApontamento
Contrato.Salva(contrato)
```
