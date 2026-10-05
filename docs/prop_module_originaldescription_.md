# OriginalDescription

Caminho: Customização > Modelo de objetos > Utilitários > Module > OriginalDescription

Descrição original do Módulo

**Exemplo 1: modificação da propriedade OriginalDescription**

```
# carrega objeto Module de identificador 1
module = Module.Carrega(1)
# modifica a propriedade OriginalDescription
module.OriginalDescription = "Descrição original";
# salva modificação da propriedade OriginalDescription
Module.Salva(module)
```
