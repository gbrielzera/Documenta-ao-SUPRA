# Componentes

Caminho: Customização > Modelo de objetos > Processo > Servico > Componentes

Itens de Configuração que compoem o Serviço.

**Exemplo 1: percorrer objetos da propriedade Componentes**

```
# carrega objeto Servico de identificador 78
servico = Servico.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if servico != None:
    # percorre objetos da propriedade Componentes e para cada uma escreve conteúdo no log de mensagens
    for componenteServico in servico.Componentes:
        Utils.LogInformation(componenteServico.ToString())
```
