# ExpressaoSelecao

Caminho: Customização > Modelo de objetos > Processo > Indicador > ExpressaoSelecao

Fórmula para seleção de registros baseados no Provedor do Indicador. Indicadores do tipo Percentual devem obrigatoriamente definir uma fórmula de seleção.

**Exemplo 1: modificação da propriedade ExpressaoSelecao**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade ExpressaoSelecao
indicador.ExpressaoSelecao = "Fórmula seleção";
# salva modificação da propriedade ExpressaoSelecao
Indicador.Salva(indicador)
```
