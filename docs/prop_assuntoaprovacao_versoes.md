# Versoes

Caminho: Customização > Modelo de objetos > Processo > AssuntoAprovacao > Versoes

Versões para Aprovação

**Exemplo 1: percorrer objetos da propriedade Versoes**

```
# carrega objeto AssuntoAprovacao de identificador 78
assuntoAprovacao = AssuntoAprovacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if assuntoAprovacao != None:
    # percorre objetos da propriedade Versoes e para cada uma escreve conteúdo no log de mensagens
    for versaoAprovacao in assuntoAprovacao.Versoes:
        Utils.LogInformation(versaoAprovacao.ToString())
```
