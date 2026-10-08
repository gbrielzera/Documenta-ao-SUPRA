# Propriedade DefinicoesPapel

Caminho: Propriedade DefinicoesPapel

Definições de Papéis no Sub-processo

**Exemplo 1: percorrer objetos da propriedade DefinicoesPapel**

```
# carrega objeto SubProcesso de identificador 90
subProcesso = SubProcesso.Carrega(90)
# verifica se o objeto foi recuperado com sucesso
if subProcesso != None:
    # percorre objetos da propriedade DefinicoesPapel e para cada uma escreve conteúdo no log de mensagens
    for definicaoPapel in subProcesso.DefinicoesPapel:
        Utils.LogInformation(definicaoPapel.ToString())
```
