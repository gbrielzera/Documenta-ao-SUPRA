# GrupoTrabalho

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > GrupoTrabalho

Grupo de Trabalho do Solucionador no instante do Apontamento

**Exemplo 1: modificação da propriedade GrupoTrabalho**

```
# carrega objeto TimeSheet de identificador 78
timeSheet = TimeSheet.Carrega(78)
# modifica a propriedade GrupoTrabalho
timeSheet.GrupoTrabalho = GrupoTrabalho.Carrega(23);
# salva modificação da propriedade GrupoTrabalho
TimeSheet.Salva(timeSheet)
```
