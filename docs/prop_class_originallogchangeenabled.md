# OriginalLogChangeEnabled

Caminho: Customização > Modelo de objetos > Utilitários > Class > OriginalLogChangeEnabled

Opção de ativação do log de modificações definida pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário.

**Exemplo 1: modificação da propriedade OriginalLogChangeEnabled**

```
# carrega objeto Class de identificador 1
class = Class.Carrega(1)
# modifica a propriedade OriginalLogChangeEnabled
class.OriginalLogChangeEnabled = true;
# salva modificação da propriedade OriginalLogChangeEnabled
Class.Salva(class)
```
