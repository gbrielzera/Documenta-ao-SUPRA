# NewDBInputOutputParam

Caminho: Recursos Avançados > Objeto DB > NewDBInputOutputParam

Este método retorna um novo parâmetro do tipo Input/Output para procedure e pode ser utilizado em conjunto com a rotina ExecuteStoredProc para passagem e retorno de valores.

## Assinatura

public DbParameter NewDBInputOutputParam(string name, object value)

### name

Nome do Parâmetro de entrada/saída. Este nome deve corresponder a um parâmetro existente na stored procedure.

### value

Valor atribuído ao parâmetro.

### Retorna

Um novo parâmetro do tipo Input/Output.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
#Carregando o Array
arrayParametros = System.Array.CreateInstance(DbParameter,2)
arrayParametros[0] = DB.NewDBInputOutputParam("CategoryName","UsuarioCategory")
arrayParametros[1] =  DB.NewDBInputOutputParam("LogID",199)
```
