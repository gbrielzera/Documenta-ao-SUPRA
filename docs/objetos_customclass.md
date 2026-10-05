# CustomClass

Caminho: Customização > Modelo de objetos > Utilitários > CustomClass

Customização de uma Classe de Negócio

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Class** | Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio. | [Class](objetos_class) |
| **ClassId** | Identificador da Classe | Inteiro |
| **Domain** | Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias | [Domain](objetos_domain) |
| **Id** | Identificador do Assinante | Inteiro |
| **TypeFullName** | Nome completo da Classe .NET incluindo Nome da Classe, Assembly, Culture e Public Token | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | CustomClass Carrega(int i); |
| **Novo** | Cria um novo registro do tipo CustomClass | CustomClass Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | CustomClass Carrega(string nomePropriedade, object valorPropriedade); |
