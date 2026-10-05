# LastAccessDateTime

Caminho: Customização > Modelo de objetos > Utilitários > Picture > LastAccessDateTime

Data e hora do último acesso a figura. Esta data/hora é gravada de forma assíncrona pela página que realiza este acesso.

**Exemplo 1: modificação da propriedade LastAccessDateTime**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade LastAccessDateTime
picture.LastAccessDateTime = DateTime;
# salva modificação da propriedade LastAccessDateTime
Picture.Salva(picture)
```
