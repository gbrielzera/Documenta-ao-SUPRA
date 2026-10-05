# DataHoraFim

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > DataHoraFim

Data/hora de Fim

**Exemplo 1: modificação da propriedade DataHoraFim**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade DataHoraFim
timeSheet.DataHoraFim = DateTime;
# salva modificação da propriedade DataHoraFim
TimeSheet.Salva(timeSheet)
```
