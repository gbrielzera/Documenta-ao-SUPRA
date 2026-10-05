# Opcoes

Caminho: Customização > Modelo de objetos > Processo > VariavelPriorizacao > Opcoes

Opções para a Variável

**Exemplo 1: percorrer objetos da propriedade Opcoes**

```
# carrega objeto VariavelPriorizacao de identificador 78
variavelPriorizacao = VariavelPriorizacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if variavelPriorizacao != None:
    # percorre objetos da propriedade Opcoes e para cada uma escreve conteúdo no log de mensagens
    for enumeracaoVariavel in variavelPriorizacao.Opcoes:
        Utils.LogInformation(enumeracaoVariavel.ToString())
```
