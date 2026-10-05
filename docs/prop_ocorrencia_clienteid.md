# ClienteId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ClienteId

Identificador da pessoa que solicitou o serviço.

**Exemplo 1: modificação da propriedade ClienteId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade ClienteId
ocorrencia.ClienteId = 1;
# salva modificação da propriedade ClienteId
Ocorrencia.Salva(ocorrencia)
```
