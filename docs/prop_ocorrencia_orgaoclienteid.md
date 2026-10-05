# OrgaoClienteId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > OrgaoClienteId

Identificador do Orgao Cliente

**Exemplo 1: modificação da propriedade OrgaoClienteId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade OrgaoClienteId
ocorrencia.OrgaoClienteId = 1;
# salva modificação da propriedade OrgaoClienteId
Ocorrencia.Salva(ocorrencia)
```
