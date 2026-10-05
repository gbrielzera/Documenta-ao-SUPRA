# OrgaoCliente

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > OrgaoCliente

Órgão solicitante de serviço ou usuário de ativo

**Exemplo 1: modificação da propriedade OrgaoCliente**

```
# carrega objeto ApuracaoIndicador de identificador 78
apuracaoIndicador = ApuracaoIndicador.Carrega(78)
# modifica a propriedade OrgaoCliente
apuracaoIndicador.OrgaoCliente = Orgao.Carrega(23);
# salva modificação da propriedade OrgaoCliente
ApuracaoIndicador.Salva(apuracaoIndicador)
```
