# Enabled

Caminho: Customização > Modelo de objetos > Utilitários > Module > Enabled

Indica que o Módulo está ativo no sistema. Uma vez inativo o Módulo não pode ser acessado por Usuários.

**Exemplo 1: modificação da propriedade Enabled**

```
# carrega objeto Module de identificador 1
module = Module.Carrega(1)
# modifica a propriedade Enabled
module.Enabled = true;
# salva modificação da propriedade Enabled
Module.Salva(module)
```
