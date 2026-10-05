# Username

Caminho: Customização > Modelo de objetos > Utilitários > User > Username

Nome de identificação do Usuário utilizado na tela de logon ou em chamadas webservices. Para autenticação via serviço de diretório este username deve corresponder exatamente ao nome de usuário no serviço de diretório.

**Exemplo 1: modificação da propriedade Username**

```
# carrega objeto User de identificador 1
user = User.Carrega(1)
# modifica a propriedade Username
user.Username = "Username";
# salva modificação da propriedade Username
User.Salva(user)
```
