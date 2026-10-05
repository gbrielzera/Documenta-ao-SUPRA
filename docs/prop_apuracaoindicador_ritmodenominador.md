# RitmoDenominador

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > RitmoDenominador

Valor do denominador da razão utilizada para cálculo de Ritmo. Este valor só é importante em Indicadores que realizem Contagem (Count).

**Exemplo 1: modificação da propriedade RitmoDenominador**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade RitmoDenominador
apuracaoIndicador.RitmoDenominador = 1;
# salva modificação da propriedade RitmoDenominador
ApuracaoIndicador.Salva(apuracaoIndicador)
```
