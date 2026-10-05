# Picture

Caminho: Customização > Modelo de objetos > Utilitários > Picture

Figura utilizada em diversos outros objetos

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Class** | Classe de negócio do objeto de negócio proprietário da figura | [Class](objetos_class) |
| **ClassId** | Identificador da classe de negócio do objeto proprietário da figura | Inteiro |
| **Content** | Conteúdo binário da figura | System.Object |
| **CreationDateTime** | Data e hora em que a figura foi inserida no banco de dados. | Data/hora |
| **Description** | Descrição detalhada sobre o conteúdo da imagem. | String |
| **Format** | Extensão do arquivo informando o formato da figura | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Picture | Inteiro |
| **KeyValue** | Chave primária do objeto de negócio proprietário da figura | String |
| **LastAccessDateTime** | Data e hora do último acesso a figura. Esta data/hora é gravada de forma assíncrona pela página que realiza este acesso. | Data/hora |
| **Temporality** | Prazo em dias para manutenção da figura no banco de dados. Este prazo tem como referência o último acesso a figura. | Inteiro |
| **TextualRepresentation** | Representação textual do objeto de negócio proprietário da figura | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Picture Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Picture | Picture Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Picture Carrega(string nomePropriedade, object valorPropriedade); |
