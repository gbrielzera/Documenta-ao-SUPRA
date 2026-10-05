# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > Localization > ClassId

Identificador da Classe de Negócio do objeto localilzado.

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto Localization de identificador 1
localization = Localization.Carrega(1)
# modifica a propriedade ClassId
localization.ClassId = 1;
# salva modificação da propriedade ClassId
Localization.Salva(localization)
```
