# Indicadores

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao > Indicadores

Indicadores associados ao Plano de Gestão. Para cada indicador existe um desdobramento de vários Períodos. Possui também uma Meta geral e redefinições por período.

**Exemplo 1: percorrer objetos da propriedade Indicadores**

```
# carrega objeto PlanoGestao de identificador 78
planoGestao = PlanoGestao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if planoGestao != None:
    # percorre objetos da propriedade Indicadores e para cada uma escreve conteúdo no log de mensagens
    for indicadorPlano in planoGestao.Indicadores:
        Utils.LogInformation(indicadorPlano.ToString())
```
