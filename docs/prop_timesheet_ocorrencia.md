# Ocorrencia

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > Ocorrencia

Ocorrência associada

**Exemplo 1: modificação da propriedade Ocorrencia**

```
# carrega objeto TimeSheet de identificador 78
timeSheet = TimeSheet.Carrega(78)
# modifica a propriedade Ocorrencia
timeSheet.Ocorrencia = Ocorrencia.Carrega(23);
# salva modificação da propriedade Ocorrencia
TimeSheet.Salva(timeSheet)
```
