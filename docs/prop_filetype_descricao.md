# Descricao

Caminho: Customização > Modelo de objetos > Utilitários > FileType > Descricao

Descrição detalhada do tipo de arquivo. Este descritivo é utilizado para nomear pastas no repositório de arquivo e por este motivo não pode conter os seguintes caracteres \\ / : > ? * "

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto FileType de identificador 1
fileType = FileType.Carrega(1)
# modifica a propriedade Descricao
fileType.Descricao = "Descrição";
# salva modificação da propriedade Descricao
FileType.Salva(fileType)
```
