# ApontamentosApropriados

Caminho: Customização > Modelo de objetos > Processo > Apropriacao > ApontamentosApropriados

Apontamentos Apropriados

**Exemplo 1: percorrer objetos da propriedade ApontamentosApropriados**

```
# carrega objeto Apropriacao de identificador 78
apropriacao = Apropriacao.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if apropriacao != None:
    # percorre objetos da propriedade ApontamentosApropriados e para cada uma escreve conteúdo no log de mensagens
    for apontamentoApropriado in apropriacao.ApontamentosApropriados:
        Utils.LogInformation(apontamentoApropriado.ToString())
```
