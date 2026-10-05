# RetornoItens

Caminho: Customização > Modelo de objetos > Processo > Atividade > RetornoItens

Configura uma regra de retorno de Itens de Configuração para Ordens de Serviço invocadas como Subprocessos ou link final. Quando uma Ordem de Serviço chamada é finalizada então os itens que atenderem a regra serão aidionado a Ordem de Serviço chamadora.

**Exemplo 1: percorrer objetos da propriedade RetornoItens**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade RetornoItens e para cada uma escreve conteúdo no log de mensagens
    for retornoItens in atividade.RetornoItens:
        Utils.LogInformation(retornoItens.ToString())
```
