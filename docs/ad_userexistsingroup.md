# UserExistsInGroup

Caminho: Recursos Avançados > Objeto AD > UserExistsInGroup

Verifica se o usuário está contido na lista de membros de um grupo do serviço de diretório.

## Assinaturas

public bool UserExistsInGroup(string username, string groupname)

public bool UserExistsInGroup(string username, string groupname, string ADAddress, string contextUser, string contextPassword)

### username

Nome da conta de rede para verificação na listagem de membros do grupo fornecido. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### groupname

Nome do grupo para verificação.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Retorna Verdadeiro se o usuário existir e Falso caso contrário.

**Processo: Remoção de Acesso**

**Evento: Remover Acessos**

```
# Remove o grupo "Administradores" no Active Directory caso ele exista no grupo
if AD.UserExistsInGroup(OrdemServico.Favorecido.UsuarioRede,"Administradores")
    AD.RemoveUserFromGroup(OrdemServico.Favorecido.UsuarioRede,"Administradores")
# preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " foi removido do grupo Administradores em " + DateTime.Now.ToString()
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
