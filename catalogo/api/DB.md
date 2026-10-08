# DB (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Connectors > DB

class `Venki.Services.Connectors.DB` — services.dll v18.1.1.0
Herda de **Connector**: os membros da classe base também valem aqui.

## Propriedades (1)
- bool EnableCache {get;set;}

## Métodos (21)
- DataTable ExecuteDataTable(string commandText)
- DataTable ExecuteDataTable(string commandText, List paramListNames, List paramListValues)
- DataTable ExecuteDataTable(string commandText, string database)
- DataTable ExecuteDataTable(string commandText, string database, List paramListNames, List paramListValues)
- object ExecuteScalar(string commandText)
- object ExecuteScalar(string commandText, string database)
- object ExecuteScalar(string commandText, List paramListNames, List paramListValues)
- object ExecuteScalar(string commandText, string database, List paramListNames, List paramListValues)
- int ExecuteNonQuery(string commandText)
- int ExecuteNonQuery(string commandText, string database)
- int ExecuteNonQuery(string commandText, List paramListNames, List paramListValues)
- int ExecuteNonQuery(string commandText, string database, List paramListNames, List paramListValues)
- DbParameter NewDBInputParam(string name, object value)
- DbParameter NewDBInputOutputParam(string name, object value)
- DbParameter NewDBOutputParam(string name)
- object ExecuteStoredProc(string storedProcName, string database)
- object ExecuteStoredProc(string storedProcName, string database, List paramListNames, List paramListValues)
- object ExecuteStoredProc(string storedProcName, string database, DbParameter[] parameters)
- object ExecuteStoredProc(string storedProcName, string paramName1, object paramValue1, string paramName2, object paramValue2, string paramName3, object paramValue3)
- object ExecuteStoredProc(string storedProcName, DbParameter[] parameters)
- object ExecuteStoredProc(string storedProcName, List paramListNames, List paramListValues)
