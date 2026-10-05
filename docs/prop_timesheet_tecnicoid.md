# TecnicoId

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > TecnicoId

Identificador do Solucionador associado ao apontamento

**Exemplo 1: modificação da propriedade TecnicoId**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade TecnicoId
timeSheet.TecnicoId = 1;
# salva modificação da propriedade TecnicoId
TimeSheet.Salva(timeSheet)
```
