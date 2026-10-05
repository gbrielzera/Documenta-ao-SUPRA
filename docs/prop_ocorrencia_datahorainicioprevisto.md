# DataHoraInicioPrevisto

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraInicioPrevisto

Data e hora de início previsto de atendimento. O início previsto pode sofrer diversas modificações no decorrer do atendimento.

**Exemplo 1: modificação da propriedade DataHoraInicioPrevisto**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraInicioPrevisto
ocorrencia.DataHoraInicioPrevisto = DateTime;
# salva modificação da propriedade DataHoraInicioPrevisto
Ocorrencia.Salva(ocorrencia)
```
