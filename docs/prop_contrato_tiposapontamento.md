# TiposApontamento

Caminho: Customização > Modelo de objetos > Recurso > Contrato > TiposApontamento

Tipos de Apontamentos previstos no Contrato

**Exemplo 1: percorrer objetos da propriedade TiposApontamento**

```
# carrega objeto Contrato de identificador 51
contrato = Contrato.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if contrato != None:
    # percorre objetos da propriedade TiposApontamento e para cada uma escreve conteúdo no log de mensagens
    for tipoApontamentoContrato in contrato.TiposApontamento:
        Utils.LogInformation(tipoApontamentoContrato.ToString())
```
