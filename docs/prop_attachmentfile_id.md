# Id

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > Id

Identificador do arquivo

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade Id
attachmentFile.Id = 1;
# salva modificação da propriedade Id
AttachmentFile.Salva(attachmentFile)
```
