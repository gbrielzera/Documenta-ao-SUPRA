# Password

Caminho: Customização > Modelo de objetos > Utilitários > User > Password

Senha de acesso do Usuário. Se for configurada uma URL do domínio na tela de configurações então a validação do usuário é feita no Serviço de Diretório e o conteúdo deste campo passa a ser ignorado.

**Exemplo 1: modificação da propriedade Password**

```
# carrega objeto User de identificador 1
user = User.Carrega(1)
# modifica a propriedade Password
user.Password = "Senha";
# salva modificação da propriedade Password
User.Salva(user)
```
