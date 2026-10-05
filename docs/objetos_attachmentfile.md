# AttachmentFile

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile

Arquivos anexados aos registros

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AttachDate** | Data/hora em que o arquivo foi anexado no registro | Data/hora |
| **Class** | Item anexado ao registro | [Class](objetos_class) |
| **ClassId** | Identificador do(a) Class associado(a) | Inteiro |
| **Comment** | Comentário feito pelo usuário no instante de anexação do arquivo ao registro | String |
| **FileName** | Nome do arquivo salvo | String |
| **FileType** | Tipos de arquivos que podem ser anexados em cadastros. | [FileType](objetos_filetype) |
| **FileTypeId** | Identificador do(a) FileType associado(a) | Inteiro |
| **FullFileName** | Nome do arquivo no servidor de arquivos | String |
| **Id** | Identificador do arquivo | Inteiro |
| **KeyValue** | Chave de identificação do Objeto de Negócio modificado. | String |
| **TextualRepresentation** | Representação textual | String |
| **User** | Usuário que anexou o arquivo ao registro | [User](objetos_user) |
| **UserId** | Identificador do usuário responsável por anexar o arquivo ao registro | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | AttachmentFile Carrega(int i); |
| **Novo** | Cria um novo registro do tipo AttachmentFile | AttachmentFile Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | AttachmentFile Carrega(string nomePropriedade, object valorPropriedade); |
