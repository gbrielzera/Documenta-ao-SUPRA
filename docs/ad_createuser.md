# CreateUser

Caminho: Recursos Avançados > Objeto AD > CreateUser

Cria uma conta de usuário no servido de diretório. Além dos parâmetros da função são utilizados nesta criação os seguintes campos configurados na tela **Configurações** do Supravizio:

Parâmetros cadastrados em Configurações

## Assinaturas

• public bool CreateUser(string username, string ou, string firstName, string lastName, string employeeID, string displayName)

• public bool CreateUser(string username, string ou, string firstName, string lastName, string employeeID, string displayName, string ADAddress, string contextUser, string contextPassword)

Indicado para: Windows 2000 Server ou superior

• public bool CreateUser(string username, string ou, string firstName, string lastName, string employeeID, string displayName, string userPrincipalName, string fullName)

• public bool CreateUser(string username, string ou, string firstName, string lastName, string employeeID, string displayName, string userPrincipalName, string fullName, string ADAddress, string contextUser, string contextPassword)

Indicado para: Windows 2008 Server ou superior

### username

Nome da conta de usuário que será criado. Veja na figura abaixo um cadastro de usuário no **Microsoft Active Directory** e observe que o nome informado neste parâmetro será utilizado no campo **Nome de logon do usuário (anterior ao Windows 2000)**.

**Importante: o tamanho máximo para o parâmetro username é de 20 caracteres em decorrência de limitação do campo "Nome de logon do usuário (anterior ao Windows 2000)".**

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário já existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### ou

Unidade Organizacional do serviço de diretório onde será armazenado o novo usuário. Você poderá representar níveis hierárquicos e para isto basta utilize um . (ponto) que representará cada sub-nível. Exemplo: a string Usuarios.Funcionarios representa a OU abaixo:

Nomenclatura de OU

### firstName

Primeiro nome do usuário utilizado para documentação. Este campo não é utilizado para montagem do login. O login é fornecido como parâmetro para ADCreateUser em username.

### lastName

Último nome do usuário utilizado para documentação.

### employeeID

Identificador de empregado do novo usuário de rede.

### displayName

Nome que será exibido.

**userPrincipalName**

Relaciona um UPN (User Principal Name) com a nova conta. Mais informações: http://technet.microsoft.com/en-us/library/cc772007.aspx

**fullName**

Indica o nome completo do usuário.

Propriedade Correspondentes no AD firstName, lastName e displayName

Propriedades correspondentes no AD username e userPrincipalName

Propriedade correspondente no AD fullName

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se o usuário foi criado com sucesso e Falso caso contrário.

**Processo: Criação de Novo Usuário de Rede, Email e internet**

**Evento: Inicialização**

```
# Cria um Usuário de rede do Favorecido da Ordem de serviço no Active Directory
criou = LDAP.CreateUser(OrdemServico.Favorecido.UsuarioRede,"Usuarios.Funcionarios" ,"Primeiro Nome","Ultimo Nome",OrdemServico.Favorecido.UsuarioRede, OrdemServico.Favorecido.Nome)
if criou:
    #Cria no log um registro informando que o usuário foi criado no Active Directory
    Utils.LogInformation("Foi criado o usuário " + OrdemServico.Favorecido.UsuarioRede + " no Active Directory", "Criação Usuário Rede")
    # Preenche o campo Solução da Ordem de Serviço com evidência
    OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " criado em " + DateTime.Now.ToString()
    # Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
    AvancaProximaAtividade = True
if not criou:
    #Cria no log um registro de erro informando que ocorreu uma falha ao tentar criar o usuário no Active Directory
    Utils.LogError("Falha ao criar usuário no Active Directory", "Criação Usuário Rede")
```

No exemplo abaixo, vamos criar uma nova conta, separando nome e sobrenome da a pessoa, e indicar depois um fullName e um userPrincipalName (UPN). Repare que em displayName, vamos fornecer o NomeAbreviado do Favorecido, porém em fullName, vamos fornecer o Nome do Favorecido:

**Processo: Criação de Novo Usuário de Rede, Email e internet com UPN e FullName**

**Evento: Inicialização**

```
# Cria um Usuário de rede do Favorecido da Ordem de serviço no Active Directory, indicando o nome completo e um UPN (User Principal Name)
criou = AD.CreateUser(OrdemServico.Favorecido.UsuarioRede,"Usuarios.Funcionarios" ,"Primeiro Nome","Ultimo Nome",OrdemServico.Favorecido.UsuarioRede, OrdemServico.Favorecido.NomeAbreviado, OrdemServico.Favorecido.UsuarioRede + "@empresa.com.br", OrdemServico.Favorecido.Nome)
if criou:
       #Cria no log um registro informando que o usuário foi criado no Active Directory
       Utils.LogInformation("Foi criado o usuário " + OrdemServico.Favorecido.UsuarioRede + " no Active Directory", "Criação Usuário Rede")
       # Preenche o campo Solução da Ordem de Serviço com evidência
       OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " criado em " + DateTime.Now.ToString()
       # Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
       AvancaProximaAtividade = True
if not criou:
       #Cria no log um registro de erro informando que ocorreu uma falha ao tentar criar o usuário no Active Directory
       Utils.LogError("Falha ao criar usuário no Active Directory", "Criação Usuário Rede")
```
