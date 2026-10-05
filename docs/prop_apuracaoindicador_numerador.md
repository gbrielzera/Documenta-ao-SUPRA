# Numerador

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > Numerador

Numerador para apuração de indicadores que possuem como função de agregação Percentual

**Exemplo 1: modificação da propriedade Numerador**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade Numerador
apuracaoIndicador.Numerador = 0;
# salva modificação da propriedade Numerador
ApuracaoIndicador.Salva(apuracaoIndicador)
```
