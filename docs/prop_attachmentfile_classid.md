# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > ClassId

Identificador do(a) Class associado(a)

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade ClassId
attachmentFile.ClassId = 1;
# salva modificação da propriedade ClassId
AttachmentFile.Salva(attachmentFile)
```
