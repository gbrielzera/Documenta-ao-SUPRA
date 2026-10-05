# UserSession

Caminho: Customização > Modelo de objetos > Utilitários > UserSession

Mantém informações da sessão de conexão de usuário.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ApplicationId** | Nome da aplicação onde foi realizado o Logon | String |
| **ConnectedUsers** | Registro da quantidade de usuários conectados no instante do Logon. São desconsideradas sessões iniciadas por rotinas de manutenção de dados e processamento de Jobs (Logon de sistema). | Inteiro |
| **LogonDateTime** | Data/hora do início de conexão. | Data/hora |
| **LogonType** | Tipo de Logon que gerou a sessão de usuário | [LogonType](enum_logontype) |
| **LogoutDateTime** | Data/hora do fim de conexão. | Data/hora |
| **LogoutReason** | Motivo do logout do usuário | String |
| **SessionId** | Identificador gerado automaticamente pelo sistema para Identificação da Sessão. | String |
| **User** | Usuário autorizado a acessar o sistema. | [User](objetos_user) |
| **UserId** | Identificador do(a) User associado(a) | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **GetActiveSessions** | Obtem a relação de usuários conectados na aplicação. | Venki.Services.Security.UserSessionList GetActiveSessions(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | UserSession Carrega(string nomePropriedade, object valorPropriedade); |
