# LogError

Caminho: Recursos Avançados > Objeto Utils > LogError

Escreve uma mensagem do tipo **Erro** no mecanismo de log. Para visualização deste log veja [Consulta de Log em Gerenciamento de Ambiente](cadastrar_perfis_sistemas_2).

## Assinatura

public void LogError(string message, string category)

### message

Texto da mensagem de erro.

### category

### Define o agrupamento da mensagem de Log. Este agrupamento é exibido em uma coluna na consulta de log da tela Gerenciamento de ambiente.

**Processo: Criação de Novo Usuário de Rede, Email e Internet**

**Evento: Inicialização**

```
# Cria um usuário de rede do favorecido da ordem de serviço no Active Directory
criou = Utils.ADCreateUser(OrdemServico.Favorecido.UsuarioRede,"Usuarios.Funcionarios" ,"Primeiro Nome","Ultimo Nome",OrdemServico.Favorecido.UsuarioRede, OrdemServico.Favorecido.Nome)
if criou:
    #Cria no log um registro informando que o usuário foi criado no Active Directory
    Utils.LogInformation("Foi criado o usuário " + OrdemServico.Favorecido.UsuarioRede + " no Active Directory", "Criação Usuário Rede")
    # Preenche o campo Solução da Ordem de Serviço com evidência
    OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " criado em " + DateTime.Now.ToString()
    # Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
    AvancaProximaAtividade = True
if not criou:
    #Cria no log um registro de erro informando que ocorreu uma falha ao tentar criar o usuário no Active Directory
    Utils.LogError("Falha ao criar usuário no Active Directory", "Criação Usuário Rede")
```
