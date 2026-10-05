# GrupoIndicador

Caminho: Customização > Modelo de objetos > Processo > Indicador > GrupoIndicador

Um Grupo de Indicadores é utilizado para classificar um Indicador de Desempenho. Também permite que Indicadores relacionados sejam agrupados na exibição feita pelo Executive Dashboard.

**Exemplo 1: modificação da propriedade GrupoIndicador**

```
# carrega objeto Indicador de identificador 78
indicador = Indicador.Carrega(78)
# modifica a propriedade GrupoIndicador
indicador.GrupoIndicador = GrupoIndicador.Carrega(23);
# salva modificação da propriedade GrupoIndicador
Indicador.Salva(indicador)
```
