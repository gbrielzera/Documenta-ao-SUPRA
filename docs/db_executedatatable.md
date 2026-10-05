# ExecuteDataTable

Caminho: Recursos Avançados > Objeto DB > ExecuteDataTable

Executa um comando SQL e retorna um objeto do tipo DataTable (tabela de dados do ADO.NET) contendo o resultado da consulta.

## Assinaturas

public DataTable ExecuteDataTable(string commandText)

public DataTable ExecuteDataTable(string commandText, string database)

### commandText

Comando SQL Select utilizado para recuperação de registros.

### database

Identificador da conexão com banco de dados configurado na camada servidora. Se não for informado o comando será executado no banco de dados do Supravizio.

### Retorno

Objeto DataTable contendo os registros recuperados. Se nenhum registro for recuperado então retorna um DataTable vazio. Para mais informações sobre o tipo DataTable veja [DataTable Class (System.Data)](http://msdn.microsoft.com/en-us/library/system.data.datatable.aspx) no site da Microsoft.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
# Os CPF são retornados da tabela VENKI_CLIENTES utilizando o ExecuteDataTable
tabela = DB.ExecuteDataTable("select CPF from VENKI_CLIENTES_VW VW where LOWER(TRIM(VW.USUARIO_REDE))='" + OrdemServico.Favorecido.UsuarioRede.Tolower(),trim() + "'")
for dr in tabela.Rows:
    Utils.LogInformation("O CPF" + dr["CPF"].ToString() + " foi retornado utilizando a função Utils.ExecuteDataTable", "ExecuteDataTable")
```
