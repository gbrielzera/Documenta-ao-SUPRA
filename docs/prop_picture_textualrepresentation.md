# TextualRepresentation

Caminho: Customização > Modelo de objetos > Utilitários > Picture > TextualRepresentation

Representação textual do objeto de negócio proprietário da figura

**Exemplo 1: modificação da propriedade TextualRepresentation**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade TextualRepresentation
picture.TextualRepresentation = "Representação textual";
# salva modificação da propriedade TextualRepresentation
Picture.Salva(picture)
```
