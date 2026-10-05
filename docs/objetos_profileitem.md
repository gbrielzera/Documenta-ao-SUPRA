# ProfileItem

Caminho: Customização > Modelo de objetos > Utilitários > ProfileItem

Profile de Usuário

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ItemName** | Nome de identificação para o item de Profile | String |
| **LastModifiedDate** | Data de última modificação | Data/hora |
| **User** | Usuário dono do Profile | [User](objetos_user) |
| **UserId** | Identificador do Usuário | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ProfileItem Carrega(string nomePropriedade, object valorPropriedade); |
