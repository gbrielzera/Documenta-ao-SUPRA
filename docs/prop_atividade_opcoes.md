# Opcoes

Caminho: Customização > Modelo de objetos > Processo > Atividade > Opcoes

Caracterísitcas da atividade que não são necessárias durante a execução do processo.

**Exemplo 1: percorrer objetos da propriedade Opcoes**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade Opcoes e para cada uma escreve conteúdo no log de mensagens
    for opcaoAtividade in atividade.Opcoes:
        Utils.LogInformation(opcaoAtividade.ToString())
```
