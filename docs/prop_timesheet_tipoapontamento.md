# TipoApontamento

Caminho: Customização > Modelo de objetos > Processo > TimeSheet > TipoApontamento

Tipo de Apontamento

**Exemplo 1: modificação da propriedade TipoApontamento**

```
# carrega objeto TimeSheet de identificador 78
timeSheet = TimeSheet.Carrega(78)
# modifica a propriedade TipoApontamento
timeSheet.TipoApontamento = TipoApontamento.Carrega(23);
# salva modificação da propriedade TipoApontamento
TimeSheet.Salva(timeSheet)
```
