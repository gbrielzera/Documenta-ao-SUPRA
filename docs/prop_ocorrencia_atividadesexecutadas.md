# AtividadesExecutadas

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > AtividadesExecutadas

Atividades Executadas

**Exemplo 1: percorrer objetos da propriedade AtividadesExecutadas**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade AtividadesExecutadas e para cada uma escreve conteúdo no log de mensagens
    for execucaoAtividade in ocorrencia.AtividadesExecutadas:
        Utils.LogInformation(execucaoAtividade.ToString())
```
