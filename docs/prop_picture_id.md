# Id

Caminho: Customização > Modelo de objetos > Utilitários > Picture > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma Picture

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Picture de identificador 1
picture = Picture.Carrega(1)
# modifica a propriedade Id
picture.Id = 1;
# salva modificação da propriedade Id
Picture.Salva(picture)
```
