# UserId

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > UserId

Identificador do usuário responsável por anexar o arquivo ao registro

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade UserId
attachmentFile.UserId = 1;
# salva modificação da propriedade UserId
AttachmentFile.Salva(attachmentFile)
```
