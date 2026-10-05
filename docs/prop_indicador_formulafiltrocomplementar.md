# FormulaFiltroComplementar

Caminho: Customização > Modelo de objetos > Processo > Indicador > FormulaFiltroComplementar

Fórmula para filtro complementar

**Exemplo 1: modificação da propriedade FormulaFiltroComplementar**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade FormulaFiltroComplementar
indicador.FormulaFiltroComplementar = "Fórmula para filtro complementar";
# salva modificação da propriedade FormulaFiltroComplementar
Indicador.Salva(indicador)
```
