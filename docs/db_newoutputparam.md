# NewDBOutputParam

Caminho: Recursos Avançados > Objeto DB > NewDBOutputParam

Este método retorna um novo parâmetro do tipo **Output** para procedure e pode ser utilizado em conjunto com a rotina ExecuteStoredProc para retorno de valores.

## Assinatura

public DbParameter NewDBOutputParam(string name)

### name

Nome do Parâmetro de saída. Este nome deve corresponder a um parâmetro existente na stored procedure.

### Retorna

Um novo parâmetro do tipo Output.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
#Carregando o Array
arrayParametros = System.Array.CreateInstance(DbParameter,2)
arrayParametros[0] = DB.NewDBOutputParam("CategoryName")
arrayParametros[1] = DB.NewDBOutputParam("LogID",199)
```
