# DuracaoMinutos

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > DuracaoMinutos

Duração de um apontamento em minutos

**Exemplo 1: modificação da propriedade DuracaoMinutos**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade DuracaoMinutos
timeSheet.DuracaoMinutos = 1;
# salva modificação da propriedade DuracaoMinutos
TimeSheet.Salva(timeSheet)
```
