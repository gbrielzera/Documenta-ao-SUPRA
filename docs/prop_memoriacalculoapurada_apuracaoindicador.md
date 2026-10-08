# Propriedade ApuracaoIndicador

Caminho: Propriedade ApuracaoIndicador

Valores apurador para um Indicador de Desempenho

**Exemplo 1: modificação da propriedade ApuracaoIndicador**

```
# carrega objeto MemoriaCalculoApurada de identificador 85
memoriaCalculoApurada = MemoriaCalculoApurada.Carrega(85)
# modifica a propriedade ApuracaoIndicador
memoriaCalculoApurada.ApuracaoIndicador = ApuracaoIndicador.Carrega(73);
# salva modificação da propriedade ApuracaoIndicador
MemoriaCalculoApurada.Salva(memoriaCalculoApurada)
```
