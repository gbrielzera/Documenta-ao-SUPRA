# GruposSolucionadores

Caminho: Customização > Modelo de objetos > Recurso > RecursoAplicado > GruposSolucionadores

Grupos de trabalho onde estão lotados os Solucionadores correspondentes ao tipo de recurso do contrato.

**Exemplo 1: percorrer objetos da propriedade GruposSolucionadores**

```
# carrega objeto RecursoAplicado de identificador 51
recursoAplicado = RecursoAplicado.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if recursoAplicado != None:
    # percorre objetos da propriedade GruposSolucionadores e para cada uma escreve conteúdo no log de mensagens
    for contratoTecnico in recursoAplicado.GruposSolucionadores:
        Utils.LogInformation(contratoTecnico.ToString())
```
