# DatabaseConnection

Caminho: Customização > Modelo de objetos > Utilitários > DatabaseConnection

Conexão de banco de dados externo

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ConnectionString** | String de conexão do banco de dados | String |
| **Enabled** | Indica que o DatabaseConnection está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um DatabaseConnection | Inteiro |
| **Shortname** | Nome resumido do DatabaseConnection | String |
| **Type** | Tipo de conexão para o banco externo. | [DBConnectionType](enum_dbconnectiontype) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | DatabaseConnection Carrega(int i); |
| **Novo** | Cria um novo registro do tipo DatabaseConnection | DatabaseConnection Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | DatabaseConnection Carrega(string nomePropriedade, object valorPropriedade); |
