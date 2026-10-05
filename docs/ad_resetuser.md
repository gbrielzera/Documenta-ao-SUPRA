# ResetUser

Caminho: Recursos Avançados > Objeto AD > ResetUser

Troca e desbloqueia a senha de um usuário do serviço de diretório. Se ocorrer algum erro durante a criação é levantada uma Exceção que deve ser tratada pela rotina chamadora.

## Assinaturas

public bool ADResetUser(string username, string password)

public bool ADResetUser(string username, string password, string ADAddress, string contextUser, string contextPassword)

public bool ADResetUser(string username, string password, bool changepasswordnextlogon)

public bool ADResetUser(string username, string password, bool changepasswordnextlogon, string ADAddress, string contextUser, string contextPassword)

### username

Usuário do serviço de diretório que terá sua senha trocada ou desbloqueada. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### password

Nova senha do usuário. Esta senha deve respeitar as políticas de segurança configuradas no serviço de diretório, caso contrário será levantada uma exceção.

### changepasswordnextlogon

Indica que o usuário que teve sua senha modificada deverá mudar a senha no próximo logon.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorna

Verdadeiro se foi possível modificar a senha do usuário e falso caso contrário.

**Processo: Desbloquear acesso**

**Evento: Inicialização**

```
# Reseta e desbloqueia a senha do usuário de rede do Favorecido da Ordem de Serviço no Active Directory
AD.ResetUser(OrdemServico.Favorecido.UsuarioRede, "XYZ")
# preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Usuário" + OrdemServico.Favorecido.UsuarioRede + " teve sua senha modificada para XYZ em " +  DateTime.Now.ToString()
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
