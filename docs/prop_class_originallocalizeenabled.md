# OriginalLocalizeEnabled

Caminho: Customização > Modelo de objetos > Utilitários > Class > OriginalLocalizeEnabled

Opção de ativação do recurso de Localização definido pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário.

**Exemplo 1: modificação da propriedade OriginalLocalizeEnabled**

```
# carrega objeto Class de identificador 1
class = Class.Carrega(1)
# modifica a propriedade OriginalLocalizeEnabled
class.OriginalLocalizeEnabled = true;
# salva modificação da propriedade OriginalLocalizeEnabled
Class.Salva(class)
```
