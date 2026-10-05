# Parametros

Caminho: Customização > Modelo de objetos > Processo > RelatorioOperacao > Parametros

Parâmetros e respectivos valores que serão utilizados no processamento do relatório.

**Exemplo 1: percorrer objetos da propriedade Parametros**

```
# carrega objeto RelatorioOperacao de identificador 78
relatorioOperacao = RelatorioOperacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if relatorioOperacao != None:
    # percorre objetos da propriedade Parametros e para cada uma escreve conteúdo no log de mensagens
    for paramRelatorioOperacao in relatorioOperacao.Parametros:
        Utils.LogInformation(paramRelatorioOperacao.ToString())
```
