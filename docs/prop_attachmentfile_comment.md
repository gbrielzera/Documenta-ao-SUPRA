# Comment

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > Comment

Comentário feito pelo usuário no instante de anexação do arquivo ao registro

**Exemplo 1: modificação da propriedade Comment**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade Comment
attachmentFile.Comment = "Comentário";
# salva modificação da propriedade Comment
AttachmentFile.Salva(attachmentFile)
```
