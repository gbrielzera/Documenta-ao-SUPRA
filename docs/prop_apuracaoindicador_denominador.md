# Denominador

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > Denominador

Denominador para apuração de indicadores que possuem como função de agregação Percentual

**Exemplo 1: modificação da propriedade Denominador**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade Denominador
apuracaoIndicador.Denominador = 0;
# salva modificação da propriedade Denominador
ApuracaoIndicador.Salva(apuracaoIndicador)
```
