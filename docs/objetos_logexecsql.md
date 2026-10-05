# LogExecSQL

Caminho: Customização > Modelo de objetos > Utilitários > LogExecSQL

Log de execução de comandos SQL

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Enviroment** | Ambiente configurado no sistema no instante em que o comando SQL foi executado. Para ambiente de produção não é possível executar comando SQL de modificação ou comandos que contenham a palavra 'commit' | String |
| **ErrorMessage** | Mensagem de erro gerada pela execução do comando SQL. Se o comando for executado com sucesso então este campo será nulo. | String |
| **ExecDateTime** | Data e hora em que o comando SQL foi executado | Data/hora |
| **Rollback** | Indica que foi necessário executar a rotina de rollback | Booleano |
| **SQL** | Comando SQL executado pelo usuário | String |
| **User** | Usuário que executou o comando SQL | [User](objetos_user) |
| **UserId** | Identificador do usuário que executou o comando SQL. | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | LogExecSQL Carrega(string nomePropriedade, object valorPropriedade); |
