# ExpressaoValor

Caminho: Customização > Modelo de objetos > Processo > Indicador > ExpressaoValor

Fórmula para determinar o Valor do Indicador. Se não for preenchido é assumida a Projeção de Contagem de registros que atendam Fórmula de Seleção. A Fórmula de Valor deve ser utilizada em conjunto com a função de Agregação para determinar o valor final de apuração do Indicador.

**Exemplo 1: modificação da propriedade ExpressaoValor**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade ExpressaoValor
indicador.ExpressaoValor = "Fórmula valor";
# salva modificação da propriedade ExpressaoValor
Indicador.Salva(indicador)
```
