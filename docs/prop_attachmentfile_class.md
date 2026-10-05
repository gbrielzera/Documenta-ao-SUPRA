# Class

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > Class

Item anexado ao registro

**Exemplo 1: modificação da propriedade Class**

```
# carrega objeto AttachmentFile de identificador 94
attachmentFile = AttachmentFile.Carrega(94)
# modifica a propriedade Class
attachmentFile.Class = Class.Carrega(57);
# salva modificação da propriedade Class
AttachmentFile.Salva(attachmentFile)
```
