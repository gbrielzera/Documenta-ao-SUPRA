# OrgaoCliente

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > OrgaoCliente

Órgão Cliente da solicitação

**Exemplo 1: modificação da propriedade OrgaoCliente**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade OrgaoCliente
ocorrencia.OrgaoCliente = Orgao.Carrega(23);
# salva modificação da propriedade OrgaoCliente
Ocorrencia.Salva(ocorrencia)
```
