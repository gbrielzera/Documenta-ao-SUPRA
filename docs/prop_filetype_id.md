# Id

Caminho: Customização > Modelo de objetos > Utilitários > FileType > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um tipo de arquivo

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto FileType de identificador 1
fileType = FileType.Carrega(1)
# modifica a propriedade Id
fileType.Id = 1;
# salva modificação da propriedade Id
FileType.Salva(fileType)
```
