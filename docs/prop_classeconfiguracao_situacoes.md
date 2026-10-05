# Situacoes

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > Situacoes

Situações possíveis para Itens da Classe

**Exemplo 1: percorrer objetos da propriedade Situacoes**

```
# carrega objeto ClasseConfiguracao de identificador 73
classeConfiguracao = ClasseConfiguracao.Carrega(73)
# verifica se o objeto foi recuperado com sucesso
if classeConfiguracao != None:
    # percorre objetos da propriedade Situacoes e para cada uma escreve conteúdo no log de mensagens
    for situacaoClasseConfiguracao in classeConfiguracao.Situacoes:
        Utils.LogInformation(situacaoClasseConfiguracao.ToString())
```
