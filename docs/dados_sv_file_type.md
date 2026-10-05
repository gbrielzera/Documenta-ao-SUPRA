# SV_FILE_TYPE

Caminho: Customização > Modelo de dados > Utilitários > SV_FILE_TYPE

Tipos de arquivos que podem ser anexados em cadastros.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_FILE_TYPE** | Número sequencial gerado automaticamente pelo sistema para Identificar um tipo de arquivo | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do tipo de arquivo. Este descritivo é utilizado para nomear pastas no repositório de arquivo e por este motivo não pode conter os seguintes caracteres \\ / : > ? * " | varchar(500) | varchar(500) | Não |
| **COMMENT_REQUIRED** | Indica que é obrigatório o registro de um texto de comentário ao anexar o arquivo. | char(3) | char(3) | Não |
| **PUBLIC_ACCESS** | Indica que arquivos deste tipo são público e portanto podem ser acessados por qualquer usuário autenticado na aplicação. Arquivos que não são públicos podem ser acessados somente por usuários que possuem autorização na respectiva transação. | char(3) | char(3) | Não |

Tabelas que dependem de SV_FILE_TYPE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_ATTACHMENT_FILE](dados_sv_attachment_file) | \| **SV_ATTACHMENT_FILE** \| **SV_FILE_TYPE** \| \|---\|---\| \| ID_FILE_TYPE \| ID_FILE_TYPE \| |
