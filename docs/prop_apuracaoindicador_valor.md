# Valor

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > Valor

Valor apurado para o Indicador

**Exemplo 1: modificação da propriedade Valor**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade Valor
apuracaoIndicador.Valor = 0;
# salva modificação da propriedade Valor
ApuracaoIndicador.Salva(apuracaoIndicador)
```
