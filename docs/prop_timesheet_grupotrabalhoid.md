# GrupoTrabalhoId

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > GrupoTrabalhoId

Identfiicador do Grupo de Trabalho do Solucionador no instante em que foi realizado o apontamento

**Exemplo 1: modificação da propriedade GrupoTrabalhoId**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade GrupoTrabalhoId
timeSheet.GrupoTrabalhoId = 1;
# salva modificação da propriedade GrupoTrabalhoId
TimeSheet.Salva(timeSheet)
```
