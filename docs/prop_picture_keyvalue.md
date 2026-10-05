# KeyValue

Caminho: Customização > Modelo de objetos > Utilitários > Picture > KeyValue

Chave primária do objeto de negócio proprietário da figura

**Exemplo 1: modificação da propriedade KeyValue**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade KeyValue
picture.KeyValue = "Chave do objeto proprietário";
# salva modificação da propriedade KeyValue
Picture.Salva(picture)
```
