# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > Picture > ClassId

Identificador da classe de negócio do objeto proprietário da figura

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade ClassId
picture.ClassId = 1;
# salva modificação da propriedade ClassId
Picture.Salva(picture)
```
