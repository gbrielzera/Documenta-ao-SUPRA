# Query

Caminho: Customização > Modelo de objetos > Utilitários > Query

Consultas SQL elaboradas pelo usuário do sistema.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Creator** | Usuário que criou a consulta SQL | [User](objetos_user) |
| **DatabaseConnection** | Conexão de banco de dados externo | [DatabaseConnection](objetos_databaseconnection) |
| **DatabaseConnectionId** | Identificador da conexão de banco de dados externo | Inteiro |
| **Descricao** | Descrição detalhada do Query | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Query | Inteiro |
| **SQL** | Texto da consulta SQL editada pelo usuário | String |
| **UserId** | Identificador do usuário criador da consulta | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Query Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Query | Query Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Query Carrega(string nomePropriedade, object valorPropriedade); |
