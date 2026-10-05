# CreateLocalGroup

Caminho: Recursos Avançados > Objeto AD > CreateLocalGroup

Cria um grupo do tipo local no serviço de diretório. Grupos Locais são grupos que podem receber permissões para os recursos do domínio onde foram criados, porém podem ter como membros grupos e usuários de outros domínios.

## Assinaturas

public bool CreateLocalGroup(string name, string ou, bool security, string managedby, string description)

public bool CreateLocalGroup(string name, string ou, bool security, string managedby, string description, string ADAddress, string contextUser, string contextPassword)

### name

Nome do grupo.

### ou

Unidade Organizacional do serviço de diretório onde será armazenado o novo grupo. A figura abaixo ilustra a localização da OU denominada Usuarios.Funcionarios:

Nomenclatura de OU

### security

Indica que o novo grupo será do tipo segurança.

Criação de um grupo local do tipo Segurança no Active Directory

### managedby

Nome da conta de usuário responsável por gerenciar o novo grupo. A figura abaixo indica o campo onde é mantido o nome do usuário.

Cadastro do usuário no Microsoft Active Directory

A figura abaixo ilustra o campo que é preenchido pelo parâmetro **managedby**:

Informação do responsável pelo grupo no Active Directory

### description

Descritivo detalhado do novo grupo.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro caso o grupo do tipo local tenha sido criado com sucesso e Falso caso contrário.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
#Cria um grupo "Grupo Tipo Local" no Active Directory
AD.CreateLocalGroup("Grupo Tipo Local","Grupo.Local", Falso, "Manager"," Grupos que somente podem receber permissões para os recursos do domínio onde foram criados, porém podem ter como membros grupos e usuários de outros domínios")
# Preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Grupo " + OrdemServico.Favorecido.UsuarioRede + " criado em " + DateTime.Now.ToString()
# Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
