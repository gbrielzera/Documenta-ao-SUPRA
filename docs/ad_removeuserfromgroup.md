# RemoveUserFromGroup

Caminho: Recursos Avançados > Objeto AD > RemoveUserFromGroup

Retira um usuário da lista de membros um grupo do serviço de diretório. Se ocorrer algum erro durante a criação é levantada uma Exceção que deve ser tratada pela rotina chamadora.

## Assinaturas

public bool RemoveUserFromGroup(string username, string group)

public bool RemoveUserFromGroup(string username, string group, string ADAddress, string contextUser, string contextPassword)

### username

Usuário do serviço de diretório para remoção de grupo. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### group

Grupo do serviço de diretório onde será removido o usuário. Se o grupo fornecido como parâmetro não existir então ocorrerá um erro de execução. Utilize [LDAP.GroupExists](ldap_groupexists) para verificar se o grupo realmente existe no serviço de diretório.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se usuário for removido do grupo com sucesso e Falso caso contrário.

**Processo: Remoção de Acesso**

**Evento: Inicialização**

```
# Remove o grupo "Administradores" no Active Directory
AD.RemoveUserFromGroup(OrdemServico.Favorecido.UsuarioRede,"Administradores")
# preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " foi removido do grupo Administradores em " + DateTime.Now.ToString()
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
