# Afirmacoes

Caminho: Customização > Modelo de objetos > Processo > Controle > Afirmacoes

Afirmações relacionadas ao Controle. Esta coleção é preenchida inicialmente com os mesmos itens de afirmações da associação Risco x Subprocesso e pode ser redefinido pelo usuário neste nível.

**Exemplo 1: percorrer objetos da propriedade Afirmacoes**

```
# carrega objeto Controle de identificador 78
controle = Controle.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if controle != None:
    # percorre objetos da propriedade Afirmacoes e para cada uma escreve conteúdo no log de mensagens
    for controleAfirmacao in controle.Afirmacoes:
        Utils.LogInformation(controleAfirmacao.ToString())
```
