# Sequencia

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > Sequencia

Sequencia

**Exemplo 1: modificação da propriedade Sequencia**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade Sequencia
apuracaoIndicador.Sequencia = 1;
# salva modificação da propriedade Sequencia
ApuracaoIndicador.Salva(apuracaoIndicador)
```
