# EsforcoEstimado

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > EsforcoEstimado

Esforço (em horas) estimado para finalização do serviço.

**Exemplo 1: modificação da propriedade EsforcoEstimado**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade EsforcoEstimado
ocorrencia.EsforcoEstimado = 1;
# salva modificação da propriedade EsforcoEstimado
Ocorrencia.Salva(ocorrencia)
```
