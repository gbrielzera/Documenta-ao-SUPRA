# LogChangeEnabled

Caminho: Customização > Modelo de objetos > Utilitários > Class > LogChangeEnabled

Indica que o Log de modificações está ativado. Quando ativado o sistema gera registro (log) de todas as modificações em objetos deste tipo.

**Exemplo 1: modificação da propriedade LogChangeEnabled**

```
# carrega objeto Class de identificador 1
class = Class.Carrega(1)
# modifica a propriedade LogChangeEnabled
class.LogChangeEnabled = true;
# salva modificação da propriedade LogChangeEnabled
Class.Salva(class)
```
