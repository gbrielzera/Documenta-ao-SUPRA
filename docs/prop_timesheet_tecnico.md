# Tecnico

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > Tecnico

Solucionador que realizou o Apontamento

**Exemplo 1: modificação da propriedade Tecnico**

```
# carrega objeto TimeSheet de identificador 78
timeSheet = TimeSheet.Carrega(78)
# modifica a propriedade Tecnico
timeSheet.Tecnico = Pessoa.Carrega(23);
# salva modificação da propriedade Tecnico
TimeSheet.Salva(timeSheet)
```
