# Feriados

Caminho: Customização > Modelo de objetos > Recurso > Calendario > Feriados

Um Feriado constitui uma data especial onde considerada, a princípio, dia não-útil.

**Exemplo 1: percorrer objetos da propriedade Feriados**

```
# carrega objeto Calendario de identificador 51
calendario = Calendario.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if calendario != None:
    # percorre objetos da propriedade Feriados e para cada uma escreve conteúdo no log de mensagens
    for feriado in calendario.Feriados:
        Utils.LogInformation(feriado.ToString())
```
