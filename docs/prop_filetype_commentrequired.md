# CommentRequired

Caminho: Customização > Modelo de objetos > Utilitários > FileType > CommentRequired

Indica que é obrigatório o registro de um texto de comentário ao anexar o arquivo.

**Exemplo 1: modificação da propriedade CommentRequired**

```
# carrega objeto FileType de identificador 1
fileType = FileType.Carrega(1)
# modifica a propriedade CommentRequired
fileType.CommentRequired = true;
# salva modificação da propriedade CommentRequired
FileType.Salva(fileType)
```
