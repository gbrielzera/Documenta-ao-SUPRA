# DataHoraFimPlan

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraFimPlan

Data e hora de fim de planejamento

**Exemplo 1: modificação da propriedade DataHoraFimPlan**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraFimPlan
ocorrencia.DataHoraFimPlan = DateTime;
# salva modificação da propriedade DataHoraFimPlan
Ocorrencia.Salva(ocorrencia)
```
