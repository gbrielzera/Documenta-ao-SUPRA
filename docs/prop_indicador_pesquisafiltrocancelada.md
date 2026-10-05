# PesquisaFiltroCancelada

Caminho: Customização > Modelo de objetos > Processo > Indicador > PesquisaFiltroCancelada

Seleciona Pesquisas de Satisfação canceladas

**Exemplo 1: modificação da propriedade PesquisaFiltroCancelada**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade PesquisaFiltroCancelada
indicador.PesquisaFiltroCancelada = true;
# salva modificação da propriedade PesquisaFiltroCancelada
Indicador.Salva(indicador)
```
