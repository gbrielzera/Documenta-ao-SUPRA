# Class

Caminho: Customização > Modelo de objetos > Utilitários > Picture > Class

Classe de negócio do objeto de negócio proprietário da figura

**Exemplo 1: modificação da propriedade Class**

```
# carrega objeto Picture de identificador 94
picture = Picture.Carrega(94)
# modifica a propriedade Class
picture.Class = Class.Carrega(57);
# salva modificação da propriedade Class
Picture.Salva(picture)
```
