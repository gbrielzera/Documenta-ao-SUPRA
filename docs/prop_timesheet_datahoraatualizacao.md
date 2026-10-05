# DataHoraAtualizacao

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > DataHoraAtualizacao

Data/hora de última atualização do Apontamento

**Exemplo 1: modificação da propriedade DataHoraAtualizacao**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade DataHoraAtualizacao
timeSheet.DataHoraAtualizacao = DateTime;
# salva modificação da propriedade DataHoraAtualizacao
TimeSheet.Salva(timeSheet)
```
