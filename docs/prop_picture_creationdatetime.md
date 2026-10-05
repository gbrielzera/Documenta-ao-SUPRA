# CreationDateTime

Caminho: Customização > Modelo de objetos > Utilitários > Picture > CreationDateTime

Data e hora em que a figura foi inserida no banco de dados.

**Exemplo 1: modificação da propriedade CreationDateTime**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade CreationDateTime
picture.CreationDateTime = DateTime;
# salva modificação da propriedade CreationDateTime
Picture.Salva(picture)
```
