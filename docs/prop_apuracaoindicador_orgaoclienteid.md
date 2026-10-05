# OrgaoClienteId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > OrgaoClienteId

Identificador do Orgao solicitante

**Exemplo 1: modificação da propriedade OrgaoClienteId**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade OrgaoClienteId
apuracaoIndicador.OrgaoClienteId = 1;
# salva modificação da propriedade OrgaoClienteId
ApuracaoIndicador.Salva(apuracaoIndicador)
```
