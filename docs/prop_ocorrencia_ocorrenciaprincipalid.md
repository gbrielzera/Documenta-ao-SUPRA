# OcorrenciaPrincipalId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > OcorrenciaPrincipalId

Identificador da ocorrência principal correspondente ao macro-fluxo que invocou a ocorrência.

**Exemplo 1: modificação da propriedade OcorrenciaPrincipalId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade OcorrenciaPrincipalId
ocorrencia.OcorrenciaPrincipalId = 1;
# salva modificação da propriedade OcorrenciaPrincipalId
Ocorrencia.Salva(ocorrencia)
```
