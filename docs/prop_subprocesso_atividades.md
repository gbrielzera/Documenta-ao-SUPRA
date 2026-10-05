# Atividades

Caminho: Customização > Modelo de objetos > Processo > SubProcesso > Atividades

Uma Atividade de Processo corresponde a Tarefas, Subprocessos e Eventos de Processos.

**Exemplo 1: percorrer objetos da propriedade Atividades**

```
# carrega objeto SubProcesso de identificador 78
subProcesso = SubProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if subProcesso != None:
    # percorre objetos da propriedade Atividades e para cada uma escreve conteúdo no log de mensagens
    for atividade in subProcesso.Atividades:
        Utils.LogInformation(atividade.ToString())
```
