# RitmoNumerador

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > RitmoNumerador

Valor do Numerador utilizado na razao para cálculo de Ritmo. Este valor só é importante em Indicadores que realizem Contagem (Count).

**Exemplo 1: modificação da propriedade RitmoNumerador**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade RitmoNumerador
apuracaoIndicador.RitmoNumerador = 1;
# salva modificação da propriedade RitmoNumerador
ApuracaoIndicador.Salva(apuracaoIndicador)
```
