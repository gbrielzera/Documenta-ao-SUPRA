# FormulaResponsavel

Caminho: Customização > Modelo de objetos > Processo > Indicador > FormulaResponsavel

Fórmula para recuperação responsável por uma Ordem de Serviço ou Pesquisa de Satisfação.

**Exemplo 1: modificação da propriedade FormulaResponsavel**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade FormulaResponsavel
indicador.FormulaResponsavel = "Fórmula para recuperação de Responsável";
# salva modificação da propriedade FormulaResponsavel
Indicador.Salva(indicador)
```
