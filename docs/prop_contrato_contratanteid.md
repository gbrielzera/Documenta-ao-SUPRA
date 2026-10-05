# ContratanteId

Caminho: Customização > Modelo de objetos > Recurso > Contrato > ContratanteId

Identificador do Orgao Contratante do Serviço

**Exemplo 1: modificação da propriedade ContratanteId**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade ContratanteId
contrato.ContratanteId = 1;
# salva modificação da propriedade ContratanteId
Contrato.Salva(contrato)
```
