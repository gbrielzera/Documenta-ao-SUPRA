# DataHoraApontamento

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > DataHoraApontamento

Data/hora em que foi feito o apontamento

**Exemplo 1: modificação da propriedade DataHoraApontamento**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade DataHoraApontamento
timeSheet.DataHoraApontamento = DateTime;
# salva modificação da propriedade DataHoraApontamento
TimeSheet.Salva(timeSheet)
```
