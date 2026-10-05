# AuthenticateUser

Caminho: Recursos Avançados > Objeto AD > AuthenticateUser

Valida usuário e senha no serviço de diretório. A validação é realizada no domínio parametrizado na tela de Configurações.

## Assinaturas

public bool AuthenticateUser(string username, string password)

public bool AuthenticateUser(string username, string password, string ADAddress)

### username

Nome do usuário de rede que será autenticado.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### password

Senha do usuário de rede que será autenticado.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### Retorno

Verdadeiro se o usuário foi autenticado com sucesso e Falso caso contrário.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Validação**

```
# Autentica o usuário no Active Directory se o usuário "Admin" e senha "xyz" forem válidos.
AD.AuthenticateUser("Administrador", "xyz")
# Preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Grupo " + OrdemServico.Favorecido.UsuarioRede + " criado em " + DateTime.Now.ToString()
# Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
