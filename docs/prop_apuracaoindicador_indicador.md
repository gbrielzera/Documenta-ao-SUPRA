# Indicador

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > Indicador

Indicador que gerou apuração

**Exemplo 1: modificação da propriedade Indicador**

```
# carrega objeto ApuracaoIndicador de identificador 78
apuracaoIndicador = ApuracaoIndicador.Carrega(78)
# modifica a propriedade Indicador
apuracaoIndicador.Indicador = Indicador.Carrega(23);
# salva modificação da propriedade Indicador
ApuracaoIndicador.Salva(apuracaoIndicador)
```
