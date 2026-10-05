# Command

Caminho: Customização > Modelo de objetos > Utilitários > Command

Um Comando pode ser um item de menu, botão ou qualquer outro recurso de interface para acesso a uma transação (janela windows, página Internet ou WebService).

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Id** | Identificador do Comando | Inteiro |
| **ParentCommand** | Comando utilizado como container deste item. Para um comando raiz de módulo ou botões customizados na barra de ferramentas este valor será nulo. | [Command](objetos_command) |
| **ParentCommandId** | Identificador do Comando Pai | Inteiro |
| **Sequence** | Define a sequência de exibição de comandos em lista (menu por exemplo). | Inteiro |
| **Text** | Texto exibido em itens de menu ou botões para seleção de comando pelo usuário. | String |
| **Transaction** | Transação que será acessada quando o comando for executado. Quando não preenchido significa que o comando será utilizado como um container para outros sub-comandos. | [Transaction](objetos_transaction) |
| **TransactionId** | Identificador da Transação associada | Inteiro |
| **User** | Usuário proprietário do Comando. Esta propriedade é utilizada para customização da barra de ferramentas do sistema. | [User](objetos_user) |
| **UserId** | Identificador do Usuário proprietário do Comando | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Command Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Command | Command Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Command Carrega(string nomePropriedade, object valorPropriedade); |
