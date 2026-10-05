# OcorrenciaId

Caminho: Customização > Modelo de objetos > Processo > ApontamentoOcorrencia > OcorrenciaId

Identificador da Ocorrência associada

**Exemplo 1: modificação da propriedade OcorrenciaId**

```
# carrega objeto ApontamentoOcorrencia de identificador 1
apontamentoOcorrencia = ApontamentoOcorrencia.Carrega(1)
# modifica a propriedade OcorrenciaId
apontamentoOcorrencia.OcorrenciaId = 1;
# salva modificação da propriedade OcorrenciaId
ApontamentoOcorrencia.Salva(apontamentoOcorrencia)
```
