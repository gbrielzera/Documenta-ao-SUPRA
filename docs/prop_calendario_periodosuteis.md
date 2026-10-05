# PeriodosUteis

Caminho: Customização > Modelo de objetos > Recurso > Calendario > PeriodosUteis

Regras que configuram a disponibildade de recursos em função dos dias da semana

**Exemplo 1: percorrer objetos da propriedade PeriodosUteis**

```
# carrega objeto Calendario de identificador 51
calendario = Calendario.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if calendario != None:
    # percorre objetos da propriedade PeriodosUteis e para cada uma escreve conteúdo no log de mensagens
    for periodoUtil in calendario.PeriodosUteis:
        Utils.LogInformation(periodoUtil.ToString())
```
