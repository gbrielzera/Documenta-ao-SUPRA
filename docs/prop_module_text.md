# Text

Caminho: Customização > Modelo de objetos > Utilitários > Module > Text

Descrição resumida para utilização na interface com usuário.

**Exemplo 1: modificação da propriedade Text**

```
# carrega objeto Module de identificador 1
module = Module.Carrega(1)
# modifica a propriedade Text
module.Text = "Descrição resumida";
# salva modificação da propriedade Text
Module.Salva(module)
```
