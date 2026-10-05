# Componentes

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > Componentes

Componentes do Item de Configuração na ocasição da apuração de Charge-back.

**Exemplo 1: percorrer objetos da propriedade Componentes**

```
# carrega objeto HistoricoItem de identificador 51
historicoItem = HistoricoItem.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if historicoItem != None:
    # percorre objetos da propriedade Componentes e para cada uma escreve conteúdo no log de mensagens
    for historicoComponente in historicoItem.Componentes:
        Utils.LogInformation(historicoComponente.ToString())
```
