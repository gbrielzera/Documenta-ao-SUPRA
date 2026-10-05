# DataHoraFimPrevistoOriginal

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraFimPrevistoOriginal

Data/hora original de finalização prevista

**Exemplo 1: modificação da propriedade DataHoraFimPrevistoOriginal**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraFimPrevistoOriginal
ocorrencia.DataHoraFimPrevistoOriginal = DateTime;
# salva modificação da propriedade DataHoraFimPrevistoOriginal
Ocorrencia.Salva(ocorrencia)
```
