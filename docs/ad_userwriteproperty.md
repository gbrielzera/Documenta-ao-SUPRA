# UserWriteProperty

Caminho: Recursos Avançados > Objeto AD > UserWriteProperty

Altera uma propriedade (tipo texto) de um usuário no serviço de diretório.

## Assinaturas

public bool UserWriteProperty(string username, string property, string value)

public bool UserWriteProperty(string username, string property, string value, string ADAddress, string contextUser, string contextPassword)

public bool UserWriteProperty(string username, string property, int value)

public bool UserWriteProperty(string username, string property, int value, string ADAddress, string contextUser, string contextPassword)

### username

Nome do usuário para modificação de propriedade. Se o usuário fornecido como parâmetro não existir ou não corresponder a um valor informado no campo **Nome de logon do usuário (anterior ao Windows 2000)** então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### property

Nome da propriedade do usuário para modificação. Se a propriedade não existir então ocorrerá um erro de execução.

### value

Novo valor string ou numérico para a propriedade.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se foi possível modificar a propriedade com sucesso e Falso caso contrário. Se a propriedade não existir então é retornado o valor nulo

**Processo: Criação de novo Usuário de rede, E-mail e Internet**

**Evento: Inicialização**

```
# Verifica se o Usuário de rede do favorecido existe no Active Directory
existeUsuario = AD.UserExists(OrdemServico.Favorecido.UsuarioRede)
if existeUsuario:
    # Realiza a leitura do campo cargo com a informação da propriedade "Title", que significa "Cargo"
    OrdemServico.Favorecido.Cargo = LDAP.UserReadProperty(OrdemServico.Favorecido.UsuarioRede, "title")
if not existeUsuario:
    # Cria um Usuário de rede do Favorecido da Ordem de serviço no Active Directory
     AD.CreateUser(OrdemServico.Favorecido.UsuarioRede,"Usuarios.Funcionarios" ,"Primeiro Nome","Ultimo Nome",OrdemServico.Favorecido.UsuarioRede,         OrdemServico.Favorecido.Nome)
    # Preenche o campo "Title" com a informação "Analista de Sistemas"
    AD.UserWriteProperty(OrdemServico.Favorecido.UsuarioRede, "title", "Analista de Sistemas")
    # Preenche o campo Solução da Ordem de Serviço com evidência
    OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " criado em " + DateTime.Now.ToString()
    # Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
    AvancaProximaAtividade = True
```
