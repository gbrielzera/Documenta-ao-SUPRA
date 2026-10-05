# Id

Caminho: Customização > Modelo de objetos > Utilitários > User > Id

Identificador do Usuário gerado automaticamente.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto User de identificador 1
user = User.Carrega(1)
# modifica a propriedade Id
user.Id = 1;
# salva modificação da propriedade Id
User.Salva(user)
```
