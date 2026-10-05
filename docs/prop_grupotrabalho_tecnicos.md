# Tecnicos

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > Tecnicos

Pessoas ou Filas do Grupo de Trabalho que atuam no atendimento de Ordens de Serviço

**Exemplo 1: percorrer objetos da propriedade Tecnicos**

```
# carrega objeto GrupoTrabalho de identificador 51
grupoTrabalho = GrupoTrabalho.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if grupoTrabalho != None:
    # percorre objetos da propriedade Tecnicos e para cada uma escreve conteúdo no log de mensagens
    for tecnico in grupoTrabalho.Tecnicos:
        Utils.LogInformation(tecnico.ToString())
```
