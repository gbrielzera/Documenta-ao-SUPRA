# ParameterClass

Caminho: Customização > Modelo de objetos > Utilitários > Module > ParameterClass

Nome da Classe responsável por manter os parâmetros do Módulo.

**Exemplo 1: modificação da propriedade ParameterClass**

```
# carrega objeto Module de identificador 1
module = Module.Carrega(1)
# modifica a propriedade ParameterClass
module.ParameterClass = "Parameter Class name";
# salva modificação da propriedade ParameterClass
Module.Salva(module)
```
