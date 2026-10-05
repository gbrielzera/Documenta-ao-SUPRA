# FileType

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > FileType

Tipos de arquivos que podem ser anexados em cadastros.

**Exemplo 1: modificação da propriedade FileType**

```
# carrega objeto AttachmentFile de identificador 94
attachmentFile = AttachmentFile.Carrega(94)
# modifica a propriedade FileType
attachmentFile.FileType = FileType.Carrega(57);
# salva modificação da propriedade FileType
AttachmentFile.Salva(attachmentFile)
```
