# Observacao

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > Observacao

Texto de Observação para detalhamento do apontamento.

**Exemplo 1: modificação da propriedade Observacao**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade Observacao
timeSheet.Observacao = "Observação";
# salva modificação da propriedade Observacao
TimeSheet.Salva(timeSheet)
```
