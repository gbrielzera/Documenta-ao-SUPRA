# LogWarning

Caminho: Recursos Avançados > Objeto Utils > LogWarning

Escreve uma mensagem do tipo **Aviso** no mecanismo de log. Para visualização deste log veja [Consulta de Log em Gerenciamento de Ambiente](cadastrar_perfis_sistemas_2).

## Assinatura

public void LogWarning(string message, string category)

**message**

Texto da mensagem de Aviso.

**category**

### Define o agrupamento da mensagem de Log. Este agrupamento é exibido em uma coluna na consulta de log da tela Gerenciamento de ambiente.

**Processo: Criação de Novo Usuário de Rede, Email e Internet**

**Evento: Inicialização**

```
# Verifica se o usuário de rede do favorecido da Ordem de Serviço existe no Active Directory
existe = Utils.ADUserExist(OrdemServico.Favorecido.UsuarioRede)
if existe:
    #Cria no log um registro avisando que o usuário ja existe no Active Directory
    Utils.LogWarning("Existe Usuário no Active Directory", "Criação Usuário Rede")
if not existe:
    Utils.ADCreateUser(OrdemServico.Favorecido.UsuarioRede,"Usuarios.Funcionarios" ,"Primeiro Nome","Ultimo Nome",OrdemServico.Favorecido.UsuarioRede,         OrdemServico.Favorecido.Nome)
    # Preenche o campo Solução da Ordem de Serviço com evidência
    OrdemServico.Solucao = "Usuário " + OrdemServico.Favorecido.UsuarioRede + " criado em " + DateTime.Now.ToString()
    # Indica que o sistema deve avançar automaticamente para a próxima atividade do processo
    AvancaProximaAtividade = True
```
