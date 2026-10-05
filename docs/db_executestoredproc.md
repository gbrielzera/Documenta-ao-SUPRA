# ExecuteStoredProc

Caminho: Recursos Avançados > Objeto DB > ExecuteStoredProc

Executa um procedimento armazenado em banco de dados (Stored procedure).

## Assinaturas

public object ExecuteStoredProc(string storedProcName, string database)

public object ExecuteStoredProc(string storedProcName, string database, DbParameter[] parametros)

public object ExecuteStoredProc(string storedProcName, DbParameter[] parametros)

public object ExecuteStoredProc(string storedProcName)

### storedProcName

Nome da stored procedure mantida no banco de dados.

### database

Identificador da conexão com banco de dados configurado na camada servidora. Se não for informado o comando será executado no banco de dados do Supravizio.

### parametros

Coleção de parametros necessários para a chamada.

### Retorno

Retorna um object com o valor retornado pela procedure.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
#Carregando o Array
arrayParametros = System.Array.CreateInstance(DbParameter,2)
arrayParametros[0] = DB.NewDBInputParam("CategoryName","UsuarioCategory")
arrayParametros[1] = DB.NewDBInputParam("LogID",199)
#Executando
retorno = DB.ExecuteStoredProc("AddCategory",arrayParametros)
```
