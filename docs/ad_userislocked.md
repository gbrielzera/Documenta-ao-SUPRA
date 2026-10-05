# UserIsLocked

Caminho: Recursos Avançados > Objeto AD > UserIsLocked

Verifica no serviço de diretório se o usuário fornecido como parâmetro está travado. O fato do usuário estar inativo não influencia no resultado da consulta.

## Assinaturas

public bool UserIsLocked(string username)

public bool UserIsLocked(string username, string ADAddress, string contextUser, string contextPassword)

### username

Nome da consta de usuário para consulta. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se o usuário estiver travado e Falso caso contrário. O fato do usuário estar inativo não influencia no resultado da consulta.

**Processo: Desbloqueio de Acesso**

**Evento: Inicialização**

```
# Verifica se o usuário de rede do favorecido da Ordem de serviço está travado no Active Directory
if AD.UserExist(OrdemServico.Favorecido.UsuarioRede):
    if AD.UserIsLocked(OrdemServico.Favorecido.UsuarioRede):
            AD.UnLockUser(OrdemServico.Favorecido.UsuarioRede)
    # preenche o campo Solução da Ordem de Serviço com evidência
    OrdemServico.Solucao = "Usuário" + OrdemServico.Favorecido.UsuarioRede + "desbloqueado em" + DateTime.Now.ToString()
    # indica que o sistema deve avançar automaticamente para a próxima atividade do processo
    AvancaProximaAtividade = True
```
