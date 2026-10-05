# Status

Caminho: Customização > Modelo de objetos > Utilitários > Global > Status

Situação final após atualização de versão

**Exemplo 1: modificação da propriedade Status**

```
# carrega objeto Global de identificador 1
global = Global.Carrega(1)
# modifica a propriedade Status
global.Status = "Situação";
# salva modificação da propriedade Status
Global.Salva(global)
```
