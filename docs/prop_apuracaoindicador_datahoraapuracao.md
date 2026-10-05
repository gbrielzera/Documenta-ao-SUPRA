# DataHoraApuracao

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > DataHoraApuracao

Data e hora em que foi apurado o valor do Indicador

**Exemplo 1: modificação da propriedade DataHoraApuracao**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade DataHoraApuracao
apuracaoIndicador.DataHoraApuracao = DateTime;
# salva modificação da propriedade DataHoraApuracao
ApuracaoIndicador.Salva(apuracaoIndicador)
```
