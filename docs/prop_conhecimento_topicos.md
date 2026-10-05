# Topicos

Caminho: Customização > Modelo de objetos > Ativos > Conhecimento > Topicos

Tópicos que compõem o artigo. Estes tópicos são ordenados pelo sequencial cadastrado do tipo de artigo.

**Exemplo 1: percorrer objetos da propriedade Topicos**

```
# carrega objeto Conhecimento de identificador 73
conhecimento = Conhecimento.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if conhecimento != None:
    # percorre objetos da propriedade Topicos e para cada uma escreve conteúdo no log de mensagens
    for topico in conhecimento.Topicos:
        Utils.LogInformation(topico.ToString())
```
