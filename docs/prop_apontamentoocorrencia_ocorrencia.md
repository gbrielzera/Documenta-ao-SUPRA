# Ocorrencia

Caminho: Customização > Modelo de objetos > Processo > ApontamentoOcorrencia > Ocorrencia

Ocorrência associada

**Exemplo 1: modificação da propriedade Ocorrencia**

```
# carrega objeto ApontamentoOcorrencia de identificador 94
apontamentoOcorrencia = ApontamentoOcorrencia.Carrega(94)
# modifica a propriedade Ocorrencia
apontamentoOcorrencia.Ocorrencia = Ocorrencia.Carrega(82);
# salva modificação da propriedade Ocorrencia
ApontamentoOcorrencia.Salva(apontamentoOcorrencia)
```
