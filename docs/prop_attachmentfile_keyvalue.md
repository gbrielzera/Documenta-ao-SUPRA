# KeyValue

Caminho: Customização > Modelo de objetos > Utilitários > AttachmentFile > KeyValue

Chave de identificação do Objeto de Negócio modificado.

**Exemplo 1: modificação da propriedade KeyValue**

```
# carrega objeto AttachmentFile de identificador 1
attachmentFile = AttachmentFile.Carrega(1)
# modifica a propriedade KeyValue
attachmentFile.KeyValue = "Chave";
# salva modificação da propriedade KeyValue
AttachmentFile.Salva(attachmentFile)
```
