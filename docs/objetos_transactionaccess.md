# TransactionAccess

Caminho: Customização > Modelo de objetos > Utilitários > TransactionAccess

Acesso a Transação realizado por um Usuário do sistema.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AccessDateTime** | Data/hora de acesso da transação pelo Usuário. | Data/hora |
| **Transaction** | Transação acessada por um Usuário | [Transaction](objetos_transaction) |
| **TransactionId** | Identificador do(a) Transaction associado(a) | Inteiro |
| **UserSession** | Sessão de Usuário que realizou o acesso | [UserSession](objetos_usersession) |
| **UserSessionSessionId** | Identificador do(a) UserSession associado(a) | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | TransactionAccess Carrega(string nomePropriedade, object valorPropriedade); |
