# User

Caminho: Customização > Modelo de objetos > Utilitários > User

Usuário autorizado a acessar o sistema.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CreatedByUserId** | Usuário administrador de segurança responsável pela criação do Usuário | Inteiro |
| **CreatedDate** | Data de criação do Usuário. | Data/hora |
| **Domain** | Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias | [Domain](objetos_domain) |
| **Id** | Identificador do Usuário gerado automaticamente. | Inteiro |
| **Password** | Senha de acesso do Usuário. Se for configurada uma URL do domínio na tela de configurações então a validação do usuário é feita no Serviço de Diretório e o conteúdo deste campo passa a ser ignorado. | String |
| **Roles** | Perfis de acesso do Usuário | [Lista de MemberOf](objetos_memberof) |
| **Username** | Nome de identificação do Usuário utilizado na tela de logon ou em chamadas webservices. Para autenticação via serviço de diretório este username deve corresponder exatamente ao nome de usuário no serviço de diretório. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | User Carrega(int i); |
| **Novo** | Cria um novo registro do tipo User | User Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | User Carrega(string nomePropriedade, object valorPropriedade); |
