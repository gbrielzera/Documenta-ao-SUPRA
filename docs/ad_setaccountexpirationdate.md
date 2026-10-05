# SetAccountExpirationDate

Caminho: Recursos Avançados > Objeto AD > SetAccountExpirationDate

Altera a data em que o registro será expirado.

## Assinaturas

public bool SetAccountExpirationDate(string username, DateTime accountExpirationDate)

public bool SetAccountExpirationDate(string username, DateTime accountExpirationDate, string ADAddress, string contextUser, string contextPassword)

### username

Usuário do serviço de diretório que terá a data de acesso expirada. Se não for encontrado um usuário cujo campo **Nome de logon do usuário (anterior ao Windows 2000)** corresponda ao parâmetro **username**, então ocorrerá um erro de execução.

Na elaboração do script é possível utilizar [AD.UserExists](ad_userexists) para verificar se o usuário realmente existe no serviço de diretório.

Cadastro do usuário no Microsoft Active Directory

### accountExpirationDate

Data em que a conta deverá expirar.

### ADAddress

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ADAddress**). O usuário utilizado neste parâmetro sobrepõe o existente na aplicação (usuário de Logon do Supravizio Server ou usuário do pool de aplicativos IIS) e necessariamente deve estar contido no grupo "Domain Controllers".

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

Verdadeiro se foi possível configurar a data de expiração com sucesso e Falso caso contrário.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Inicialização**

```
#Altera a data em que o registro irá expirar para Data e Hora da solicitação mais 365 dias
AD.SetAccountExpirationDate(OrdemServico.Favorecido.UsuarioRede,OrdemServico.DataHoraSolicitacao + 365)
# preenche o campo Solução da Ordem de Serviço com evidência
OrdemServico.Solucao = "Usuário" + OrdemServico.Favorecido.UsuarioRede + " teve a data de espiração de sua senha modificada em" + DateTime.Now.ToString()
# indica que o sistema deve avançar automaticamente para a próxima atividade do processo
AvancaProximaAtividade = True
```
