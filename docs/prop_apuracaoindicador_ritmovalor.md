# RitmoValor

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > RitmoValor

Valor de Ritmo do Indicador estimado até fim do Período associado. Este valor será igual ao Valor apurado se o período estiver finalizado e só é importante em Indicadores que realizem Contagem (Count).

**Exemplo 1: modificação da propriedade RitmoValor**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade RitmoValor
apuracaoIndicador.RitmoValor = 0;
# salva modificação da propriedade RitmoValor
ApuracaoIndicador.Salva(apuracaoIndicador)
```
