# FileTypeId

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > FileTypeId

Identificador do(a) FileType associado(a)

**Exemplo 1: modificação da propriedade FileTypeId**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade FileTypeId
attachmentFile.FileTypeId = 1;
# salva modificação da propriedade FileTypeId
AttachmentFile.Salva(attachmentFile)
```
