# DataHoraFimPrevisto

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraFimPrevisto

Data e hora prevista para términdo do atendimento. A previsão de fim pode sofrer diversas modificações no decorrer do atendimento.

**Exemplo 1: modificação da propriedade DataHoraFimPrevisto**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraFimPrevisto
ocorrencia.DataHoraFimPrevisto = DateTime;
# salva modificação da propriedade DataHoraFimPrevisto
Ocorrencia.Salva(ocorrencia)
```
