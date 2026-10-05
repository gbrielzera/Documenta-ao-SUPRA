# DataHoraResponsavel

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraResponsavel

Data/hora em que foi definido o Responsável corrente da ocorrência.

**Exemplo 1: modificação da propriedade DataHoraResponsavel**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraResponsavel
ocorrencia.DataHoraResponsavel = DateTime;
# salva modificação da propriedade DataHoraResponsavel
Ocorrencia.Salva(ocorrencia)
```
