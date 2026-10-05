# AddUserToGroup

Caminho: Recursos Avançados > Objeto AD > AddUserToGroup

Adiciona um usuário na lista de membros de um grupo do serviço de diretório. Se o usuário já faz parte da lista de membros do grupo então nenhuma ação é executada e a rotina retorna o valor Falso. Utilizando grupos do serviço de diretório podemos implementar rotinas diversas tais como acesso a pastas de rede, inclusão em listas de distribuição de emails, permissionamentos de sistemas etc.

## Assinaturas

public bool AddUserToGroup(string username, string group)

public bool AddUserToGroup(string username, string group, string LDAPAddress, string contextUser, string contextPassword)

### username

Nome da conta de usuário do serviço de diretório para recuperação de informação. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### group

Nome do grupo do serviço de diretório onde será incluído o usuário como membro. Se o grupo fornecido como parâmetro não existir então ocorrerá um erro de execução. Utilize [AD.GroupExists](ad_groupexists) para verificar se o grupo realmente existe no serviço de diretório.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se foi possível incluir o usuário no grupo com sucesso e Falso caso contrário. Se o usuário já faz parte da lista de membros também é retornado o valor False.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
# Adiciona um usuário de rede do favorecido da Ordem de Serviço ao grupo "Administradores"
AD.AddUserToGroup(OrdemServico.Favorecido.UsuarioRede,"Administradores")
# preenche o campo Solução da Ordem de Serviço com evidência:
OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " adicionado ao grupo Administradores em " +  DateTime.Now.ToString()
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
