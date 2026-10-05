# FullFileName

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > FullFileName

Nome do arquivo no servidor de arquivos

**Exemplo 1: modificação da propriedade FullFileName**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade FullFileName
attachmentFile.FullFileName = "Nome do arquivo no servidor de arquivos";
# salva modificação da propriedade FullFileName
AttachmentFile.Salva(attachmentFile)
```
