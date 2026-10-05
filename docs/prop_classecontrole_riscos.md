# Riscos

Caminho: Customização > Modelo de objetos > Processo > ClasseControle > Riscos

Riscos padrão para Controles deste tipo

**Exemplo 1: percorrer objetos da propriedade Riscos**

```
# carrega objeto ClasseControle de identificador 78
classeControle = ClasseControle.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classeControle != None:
    # percorre objetos da propriedade Riscos e para cada uma escreve conteúdo no log de mensagens
    for riscoClasseControle in classeControle.Riscos:
        Utils.LogInformation(riscoClasseControle.ToString())
```
