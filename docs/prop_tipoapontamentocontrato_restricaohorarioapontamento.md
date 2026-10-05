# RestricaoHorarioApontamento

Caminho: Customização > Modelo de objetos > Recurso > TipoApontamentoContrato > RestricaoHorarioApontamento

Restrições de horários

**Exemplo 1: percorrer objetos da propriedade RestricaoHorarioApontamento**

```
# carrega objeto TipoApontamentoContrato de identificador 51
tipoApontamentoContrato = TipoApontamentoContrato.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if tipoApontamentoContrato != None:
    # percorre objetos da propriedade RestricaoHorarioApontamento e para cada uma escreve conteúdo no log de mensagens
    for restricaoHorarioApontamento in tipoApontamentoContrato.RestricaoHorarioApontamento:
        Utils.LogInformation(restricaoHorarioApontamento.ToString())
```
