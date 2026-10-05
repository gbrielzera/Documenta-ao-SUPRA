# ReportQuery

Caminho: Customização > Modelo de objetos > Utilitários > ReportQuery

Consulta criada pelo usuário para recuperação dos dados que serão apresentados pelo relatório. No caso de consultas do banco de dados do produto o usuário contará com o recurso Query Builder.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DatabaseConnection** | Conexão de banco de dados externo | [DatabaseConnection](objetos_databaseconnection) |
| **DatabaseConnectionId** | Identificador da conexão de base de dados externa utilizada para executar o comando SQL Select. No caso de consultas no banco do produto este campo estará sempre nulo. | Inteiro |
| **Name** | Corresponde ao nome da banda do relatório associada com a consulta. | String |
| **ReportId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Report | Inteiro |
| **SQL** | Comand SQL Select utilizado para recuperar os dados do relatório. | String |
