# NewDBInputParam

Caminho: Recursos Avançados > Objeto DB > NewDBInputParam

Este método retorna um novo parâmetro do tipo **Input** para procedure e pode ser utilizado em conjunto com a rotina ExecuteStoredProc para passagem.

## Assinatura

public DbParameter NewDBInputParam(string name, object value)

### name

Nome do Parâmetro de entrada. Este nome deve corresponder a um parâmetro existente na stored procedure.

### value

Valor do parâmetro.

### Retorna

Um novo parâmetro do tipo Input.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
#Carregando o Array
arrayParametros = System.Array.CreateInstance(DbParameter,2)
arrayParametros[0] = DB.NewDBInputParam("CategoryName","UsuarioCategory")
arrayParametros[1] = DB.NewDBInputParam("LogID",199)
```
