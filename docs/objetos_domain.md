# Domain

Caminho: Customização > Modelo de objetos > Utilitários > Domain

Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Enabled** | Indica que o Domínio está ativo. Quando desabilitado não é possível ao usuário a operação de Login. | Booleano |
| **Id** | Identificador do Domínio | Inteiro |
| **Name** | Nome do Domínio | String |
| **ShortName** | Nome abreviado (código) que identifica um Domínio. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **ClearLog** | Limpa mensagens de log do domínio | void ClearLog(); |
| **SaveLogo** | Salva o logo da empresa | bool SaveLogo(byte[] logo); |
| **LoadLogo** | Carrega o Logo da empresa | byte[] LoadLogo(); |
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Domain Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Domain | Domain Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Domain Carrega(string nomePropriedade, object valorPropriedade); |
