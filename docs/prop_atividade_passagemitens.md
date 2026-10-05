# PassagemItens

Caminho: Customização > Modelo de objetos > Processo > Atividade > PassagemItens

Configura uma regra de passagem de Itens de Configuração para Ordens de Serviço invocadas como Subprocessos ou link final.

**Exemplo 1: percorrer objetos da propriedade PassagemItens**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade PassagemItens e para cada uma escreve conteúdo no log de mensagens
    for passagemItens in atividade.PassagemItens:
        Utils.LogInformation(passagemItens.ToString())
```
