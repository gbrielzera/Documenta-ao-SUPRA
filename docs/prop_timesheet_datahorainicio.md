# DataHoraInicio

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > DataHoraInicio

Data/hora de início

**Exemplo 1: modificação da propriedade DataHoraInicio**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade DataHoraInicio
timeSheet.DataHoraInicio = DateTime;
# salva modificação da propriedade DataHoraInicio
TimeSheet.Salva(timeSheet)
```
