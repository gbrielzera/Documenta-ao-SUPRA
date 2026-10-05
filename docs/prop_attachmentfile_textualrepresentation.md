# TextualRepresentation

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > TextualRepresentation

Representação textual

**Exemplo 1: modificação da propriedade TextualRepresentation**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade TextualRepresentation
attachmentFile.TextualRepresentation = "Representação textual";
# salva modificação da propriedade TextualRepresentation
AttachmentFile.Salva(attachmentFile)
```
