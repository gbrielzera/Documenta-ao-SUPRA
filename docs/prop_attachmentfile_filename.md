# FileName

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > FileName

Nome do arquivo salvo

**Exemplo 1: modificação da propriedade FileName**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade FileName
attachmentFile.FileName = "Nome do arquivo salvo";
# salva modificação da propriedade FileName
AttachmentFile.Salva(attachmentFile)
```
