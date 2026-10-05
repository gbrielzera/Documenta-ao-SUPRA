# CommandClass

Caminho: Customização > Modelo de objetos > Utilitários > CommandClass

Classe de Comandos para customização do aplicativo

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Binary** | Código binário | String |
| **Class** | Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio. | [Class](objetos_class) |
| **ClassId** | Identificador da Classe associada | Inteiro |
| **Description** | Descrição completa da Classe de Comando | String |
| **Id** | Identificador da Classe de Comando | Inteiro |
| **Name** | Nome da Classe incluindo namespace | String |
| **Source** | Código fonte da Classe | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | CommandClass Carrega(int i); |
| **Novo** | Cria um novo registro do tipo CommandClass | CommandClass Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | CommandClass Carrega(string nomePropriedade, object valorPropriedade); |
