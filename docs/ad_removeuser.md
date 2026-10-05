# RemoveUser

Caminho: Recursos Avançados > Objeto AD > RemoveUser

Remove uma conta de usuário no serviço de diretório. Se ocorrer algum erro durante a criação é levantada uma Exceção que deve ser tratada pela rotina chamadora.

## Assinaturas

public bool RemoveUser(string username)

public bool RemoveUser(string username, string ADAddress, string contextUser, string contextPassword)

### username

Nome do usuário do serviço de diretório para remoção. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então a função retornará o valor **Falso**.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se usuário for removido com sucesso e Falso caso contrário. Se o usuário não existir então será retornado o valor Falso.

**Processo: Remoção de Acesso**

**Evento: Inicialização**

```
# Remove o usuário de rede do favorecido da Ordem de Serviço caso ele exista no Active Directory
if AD.UserExists(OrdemServico.Favorecido.UsuarioRede):
    AD.RemoveUser(OrdemServico.Favorecido.UsuarioRede)
# preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Usuário" + OrdemServico.Favorecido.UsuarioRede + "removido em" + DateTime.Now.ToString()
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
