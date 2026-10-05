# DataHoraFimReal

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraFimReal

Data/hora fim real

**Exemplo 1: modificação da propriedade DataHoraFimReal**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraFimReal
ocorrencia.DataHoraFimReal = DateTime;
# salva modificação da propriedade DataHoraFimReal
Ocorrencia.Salva(ocorrencia)
```
