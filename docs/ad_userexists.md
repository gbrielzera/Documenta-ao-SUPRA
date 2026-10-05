# UserExists

Caminho: Recursos Avançados > Objeto AD > UserExists

Verifica se existe no serviço de diretório uma conta com o username fornecido como parâmetro.

## Assinaturas

public bool UserExists(string username)

public bool UserExists(string username, string ADAddress, string contextUser, string contextPassword)

### username

Nome da conta de rede para verificação no serviço de diretório. Observe na figura abaixo que o campo do serviço de diretório utilizado para verificação é o **Nome de logon do usuário (anterior ao Windows 2000)**.

Cadastro do usuário no Microsoft Active Directory

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Retorna Verdadeiro se o usuário existir e Falso caso contrário.

**Processo: Desbloquear acesso**

**Evento: Inicialização**

```
# Verifica se o usuário de rede do favorecido da Ordem de Serviço existe no Active Directory para remove -lo
if LDAP.UserExists(OrdemServico.Favorecido.UsuarioRede)
    AD.RemoveUser(OrdemServico.Favorecido.UsuarioRede)
# preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Usuário" + OrdemServico.Favorecido.UsuarioRede + "removido em" + DateTime.Now.ToString()
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
