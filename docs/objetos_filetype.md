# FileType

Caminho: Customização > Modelo de objetos > Utilitários > FileType

Tipos de arquivos que podem ser anexados em cadastros.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CommentRequired** | Indica que é obrigatório o registro de um texto de comentário ao anexar o arquivo. | Booleano |
| **Descricao** | Descrição detalhada do tipo de arquivo. Este descritivo é utilizado para nomear pastas no repositório de arquivo e por este motivo não pode conter os seguintes caracteres \\ / : > ? * " | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um tipo de arquivo | Inteiro |
| **PublicAccess** | Indica que arquivos deste tipo são público e portanto podem ser acessados por qualquer usuário autenticado na aplicação. Arquivos que não são públicos podem ser acessados somente por usuários que possuem autorização na respectiva transação. | Booleano |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | FileType Carrega(int i); |
| **Novo** | Cria um novo registro do tipo FileType | FileType Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | FileType Carrega(string nomePropriedade, object valorPropriedade); |
