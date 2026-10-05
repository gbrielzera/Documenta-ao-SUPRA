# DataHoraInicioPlan

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraInicioPlan

Data e hora de início planejado

**Exemplo 1: modificação da propriedade DataHoraInicioPlan**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraInicioPlan
ocorrencia.DataHoraInicioPlan = DateTime;
# salva modificação da propriedade DataHoraInicioPlan
Ocorrencia.Salva(ocorrencia)
```
