# User

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > User

Usuário que anexou o arquivo ao registro

**Exemplo 1: modificação da propriedade User**

```
# carrega objeto AttachmentFile de identificador 94
attachmentFile = AttachmentFile.Carrega(94)
# modifica a propriedade User
attachmentFile.User = User.Carrega(57);
# salva modificação da propriedade User
AttachmentFile.Salva(attachmentFile)
```
