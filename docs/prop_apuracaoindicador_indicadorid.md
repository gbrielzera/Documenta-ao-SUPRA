# IndicadorId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > IndicadorId

Identificador do(a) Indicador associado(a)

**Exemplo 1: modificação da propriedade IndicadorId**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade IndicadorId
apuracaoIndicador.IndicadorId = 1;
# salva modificação da propriedade IndicadorId
ApuracaoIndicador.Salva(apuracaoIndicador)
```
