# OcorrenciaId

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > OcorrenciaId

Identificador da Ocorrência de Processo associada

**Exemplo 1: modificação da propriedade OcorrenciaId**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade OcorrenciaId
timeSheet.OcorrenciaId = 1;
# salva modificação da propriedade OcorrenciaId
TimeSheet.Salva(timeSheet)
```
