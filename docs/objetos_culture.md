# Culture

Caminho: Customização > Modelo de objetos > Utilitários > Culture

Cultura disponível para localização de conteúdo de objetos de negócio. Todo usuário possui uma cultura associada e esta cultura é importante para apresentação da interface que pode ser localizada.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Description** | Descrição detalhada do Culture | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Cultura | Inteiro |
| **ShortName** | Nome resumido que identifica uma Cultura na tecnologia Microsoft.NET | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Culture Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Culture | Culture Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Culture Carrega(string nomePropriedade, object valorPropriedade); |
