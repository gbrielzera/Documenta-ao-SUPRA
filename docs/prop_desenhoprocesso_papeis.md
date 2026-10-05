# Papeis

Caminho: Customização > Modelo de objetos > Processo > DesenhoProcesso > Papeis

Papéis de Pessoas na execução do Processo

**Exemplo 1: percorrer objetos da propriedade Papeis**

```
# carrega objeto DesenhoProcesso de identificador 78
desenhoProcesso = DesenhoProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if desenhoProcesso != None:
    # percorre objetos da propriedade Papeis e para cada uma escreve conteúdo no log de mensagens
    for papelProcesso in desenhoProcesso.Papeis:
        Utils.LogInformation(papelProcesso.ToString())
```
