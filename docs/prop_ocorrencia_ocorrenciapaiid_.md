# OcorrenciaPaiId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > OcorrenciaPaiId

Identificador da ocorrência que invocou o processo da ocorrência. Este campo pode ser diferente de OcorrenciaPrincipal se existirem mais de dois níveis de chamada.

**Exemplo 1: modificação da propriedade OcorrenciaPaiId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade OcorrenciaPaiId
ocorrencia.OcorrenciaPaiId = 1;
# salva modificação da propriedade OcorrenciaPaiId
Ocorrencia.Salva(ocorrencia)
```
