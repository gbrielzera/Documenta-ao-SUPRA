# OriginalDescription

Caminho: Customização > Modelo de objetos > Utilitários > Class > OriginalDescription

Descrição completa definida originalmente pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário.

**Exemplo 1: modificação da propriedade OriginalDescription**

```
# carrega objeto Class de identificador 1
class = Class.Carrega(1)
# modifica a propriedade OriginalDescription
class.OriginalDescription = "Descrição original";
# salva modificação da propriedade OriginalDescription
Class.Salva(class)
```
