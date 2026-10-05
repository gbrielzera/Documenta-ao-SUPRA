# ReferenciaCalculo

Caminho: Customização > Modelo de objetos > Processo > Indicador > ReferenciaCalculo

Texto explicativo sobre como o Indicador é calculado.

**Exemplo 1: modificação da propriedade ReferenciaCalculo**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade ReferenciaCalculo
indicador.ReferenciaCalculo = "Referência do cálculo";
# salva modificação da propriedade ReferenciaCalculo
Indicador.Salva(indicador)
```
