# Parametros

Caminho: Customização > Modelo de objetos > Processo > RelatorioAtividade > Parametros

Parâmetros e respectivos valores que serão utilizados no processamento do relatório.

**Exemplo 1: percorrer objetos da propriedade Parametros**

```
# carrega objeto RelatorioAtividade de identificador 78
relatorioAtividade = RelatorioAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if relatorioAtividade != None:
    # percorre objetos da propriedade Parametros e para cada uma escreve conteúdo no log de mensagens
    for paramRelatorioAtividade in relatorioAtividade.Parametros:
        Utils.LogInformation(paramRelatorioAtividade.ToString())
```
