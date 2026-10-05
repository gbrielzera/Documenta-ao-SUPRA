# TipoApontamentoId

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > TipoApontamentoId

Identificador do Tipo de Apontamento associado

**Exemplo 1: modificação da propriedade TipoApontamentoId**

```
# carrega objeto TimeSheet de identificador 1
timeSheet = TimeSheet.Carrega(1)
# modifica a propriedade TipoApontamentoId
timeSheet.TipoApontamentoId = 1;
# salva modificação da propriedade TipoApontamentoId
TimeSheet.Salva(timeSheet)
```
