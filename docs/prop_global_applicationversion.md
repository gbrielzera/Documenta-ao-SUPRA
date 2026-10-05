# ApplicationVersion

Caminho: Customização > Modelo de objetos > Utilitários > Global > ApplicationVersion

Versão da aplicação

**Exemplo 1: modificação da propriedade ApplicationVersion**

```
# carrega objeto Global de identificador 1
global = Global.Carrega(1)
# modifica a propriedade ApplicationVersion
global.ApplicationVersion = "Versão de aplicação";
# salva modificação da propriedade ApplicationVersion
Global.Salva(global)
```
