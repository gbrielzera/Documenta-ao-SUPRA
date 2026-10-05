# DataHoraInicioReal

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraInicioReal

Data/hora início real

**Exemplo 1: modificação da propriedade DataHoraInicioReal**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraInicioReal
ocorrencia.DataHoraInicioReal = DateTime;
# salva modificação da propriedade DataHoraInicioReal
Ocorrencia.Salva(ocorrencia)
```
