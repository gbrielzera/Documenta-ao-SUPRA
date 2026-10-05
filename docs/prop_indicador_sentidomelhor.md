# SentidoMelhor

Caminho: Customização > Modelo de objetos > Processo > Indicador > SentidoMelhor

Indica o melhor desempenho para um valor apurado em relação a Meta estipulada para o Indicador.

**Exemplo 1: modificação da propriedade SentidoMelhor**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade SentidoMelhor
indicador.SentidoMelhor = "Acima";
# salva modificação da propriedade SentidoMelhor
Indicador.Salva(indicador)
```
