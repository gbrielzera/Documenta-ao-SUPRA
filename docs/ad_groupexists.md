# GroupExists

Caminho: Recursos Avançados > Objeto AD > GroupExists

Verifica se existe no serviço de diretório o grupo fornecido como parâmetro.

## Assinaturas

public bool GroupExists(string group)

public bool GroupExists(string group, string ADAddress, string contextUser, string contextPassword)

### group

Nome do grupo para verificação.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se o grupo existir e Falso caso contrário.

**Processo: Remoção de Acesso**

**Evento: Inicialização**

```
# Verifica se o grupo "Administradores" existe no Active Directory
existeGrupo = AD.DGroupExists("Administradores")
if existeGrupo:
    AD.RemoveUserFromGroup(OrdemServico.Favorecido.UsuarioRede,"Administradores")
    # Preenche o campo Solução da Ordem de Serviço com evidência
    OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " foi removido do grupo Administradores em " + DateTime.Now.ToString()
    # Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
    AvancaProximaAtividade = True
if not existeGrupo:
    #Cria no log um registro de erro informando que ocorreu uma falha ao tentar remover o usuário no Active Directory
    Utils.LogError("Falha ao remover usuário no Active Directory", "Remoção de Usuário Rede")
```
