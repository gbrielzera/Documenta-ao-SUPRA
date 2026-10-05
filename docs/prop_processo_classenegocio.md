# ClasseNegocio

Caminho: Customização > Modelo de objetos > Processo > Processo > ClasseNegocio

Classe de Negócio utilizada pelo Processo.

**Exemplo 1: modificação da propriedade ClasseNegocio**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade ClasseNegocio
processo.ClasseNegocio = "OrdemServico";
# salva modificação da propriedade ClasseNegocio
Processo.Salva(processo)
```
