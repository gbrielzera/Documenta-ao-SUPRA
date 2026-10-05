# Role

Caminho: Customização > Modelo de objetos > Utilitários > Role

Conjunto de telas autorizadas para um determinado usuário. Importante: um usuário pode acumular diversos perfis e o menu final é formado pela soma de todos os acessos.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Domain** | Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias | [Domain](objetos_domain) |
| **Id** | Identificador do Perfil de acesso | Inteiro |
| **Name** | Nome do Perfil de acesso | String |
| **Reference** | Texto explicativo para utilização do Perfil de acesso. Pode ser utilizado para esclarecer sobre funções ou transações que podem ser acessadas pelo usuário que detém o perfil. | String |
| **Transactions** | Autorizações as transações atribuídos ao Perfil de Acesso. | [Lista de Authorization](objetos_authorization) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Role Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Role | Role Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Role Carrega(string nomePropriedade, object valorPropriedade); |
