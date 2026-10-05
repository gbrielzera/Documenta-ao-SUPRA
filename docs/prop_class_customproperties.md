# CustomProperties

Caminho: Customização > Modelo de objetos > Utilitários > Class > CustomProperties

Propriedade de uma Classe de Negócio criada pelo próprio usuário com escopo válido para um determinado Domínio de uso. Propriedades customizadas são gravadas em tabelas adicionais criadas dinamicamente pelo sistema na medida em que o usuário extende Classes de Negócio. Para cada Classe de Negócio pode existir uma tabele adicional para manutenção de customizações (todos os campos adicionais são criados nesta mesma tabela)

**Exemplo 1: percorrer objetos da propriedade CustomProperties**

```
# carrega objeto Class de identificador 94
class = Class.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if class != None:
    # percorre objetos da propriedade CustomProperties e para cada uma escreve conteúdo no log de mensagens
    for customProperty in class.CustomProperties:
        Utils.LogInformation(customProperty.ToString())
```
