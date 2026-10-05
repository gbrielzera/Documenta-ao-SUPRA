# Usuarios

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > Usuarios

Usuários do Item do Ativo na ocasição do processamento do Charge-back.

**Exemplo 1: percorrer objetos da propriedade Usuarios**

```
# carrega objeto HistoricoItem de identificador 51
historicoItem = HistoricoItem.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if historicoItem != None:
    # percorre objetos da propriedade Usuarios e para cada uma escreve conteúdo no log de mensagens
    for historicoUsuario in historicoItem.Usuarios:
        Utils.LogInformation(historicoUsuario.ToString())
```
