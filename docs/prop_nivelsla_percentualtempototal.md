# PercentualTempoTotal

Caminho: Customização > Modelo de objetos > Processo > NivelSLA > PercentualTempoTotal

Percentual do tempo total do Acordo de Nível de Serviço

**Exemplo 1: modificação da propriedade PercentualTempoTotal**

```
# carrega objeto NivelSLA de identificador 1
nivelSLA = NivelSLA.Carrega(1)
# modifica a propriedade PercentualTempoTotal
nivelSLA.PercentualTempoTotal = 1;
# salva modificação da propriedade PercentualTempoTotal
NivelSLA.Salva(nivelSLA)
```
