# ShortName

Caminho: Customização > Modelo de objetos > Utilitários > Module > ShortName

Nome resumido (código) que identifica um Módulo.

**Exemplo 1: modificação da propriedade ShortName**

```
# carrega objeto Module de identificador 1
module = Module.Carrega(1)
# modifica a propriedade ShortName
module.ShortName = "Abreviatura";
# salva modificação da propriedade ShortName
Module.Salva(module)
```
