# AttachDate

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > AttachDate

Data/hora em que o arquivo foi anexado no registro

**Exemplo 1: modificação da propriedade AttachDate**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade AttachDate
attachmentFile.AttachDate = DateTime;
# salva modificação da propriedade AttachDate
AttachmentFile.Salva(attachmentFile)
```
