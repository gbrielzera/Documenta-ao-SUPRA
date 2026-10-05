# AtoresServico

Caminho: Customização > Modelo de objetos > Processo > Servico > AtoresServico

Sobrepõe a configuração global de Papéis em ocorrências do Serviço.

**Exemplo 1: percorrer objetos da propriedade AtoresServico**

```
# carrega objeto Servico de identificador 78
servico = Servico.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if servico != None:
    # percorre objetos da propriedade AtoresServico e para cada uma escreve conteúdo no log de mensagens
    for atoresServico in servico.AtoresServico:
        Utils.LogInformation(atoresServico.ToString())
```
