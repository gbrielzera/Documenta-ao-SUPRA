# TempoInterrupcaoSLA

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > TempoInterrupcaoSLA

Tempo total de interrupção da contagem de tempo do Acordo de Nível de Serviço. Este tempo é mantido pela inclusão/aprovação de registros de interrupção de ANS definidos no Acordo de Nível de Serviço.

**Exemplo 1: modificação da propriedade TempoInterrupcaoSLA**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade TempoInterrupcaoSLA
ordemServico.TempoInterrupcaoSLA = 1;
# salva modificação da propriedade TempoInterrupcaoSLA
OrdemServico.Salva(ordemServico)
```
