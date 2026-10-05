# Id

Caminho: Customização > Modelo de objetos > Utilitários > Localization > Id

Identificador do objeto de negócio localizado

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Localization de identificador 1
localization = Localization.Carrega(1)
# modifica a propriedade Id
localization.Id = 1;
# salva modificação da propriedade Id
Localization.Salva(localization)
```
