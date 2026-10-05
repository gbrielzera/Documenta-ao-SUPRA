# Automatizando Exchange com PowerShell

Caminho: Recursos Avançados > Objeto PowerShell > Automatizando Exchange com PowerShell

O servidor de email Microsoft Exchange 2007 disponibiliza uma série de comandos PowerShell para auxiliar a administração de configurações. Com a integração do Supravizio e PowerShell estas configurações podem também ser automatizadas em resposta aos processos da TI.

Para elaboração destes comandos é necessário combinar verbos e nomes de comandos listados abaixo.

| **Verbos** | **Nomes** |
|---|---|
| **Update** | MailboxDatabase |
| **New** | StorageGroup |
| **Get** | SendConnector |
| **Remove** | TransportAgent |
| **Set** | MobileDevice |
| **Add** | SystemHealth |
| **Enable** | ServiceHealth |
| **Mount** | JournalRule |
| **Dismount** | MAPIConnectivity |
| **Disable** | ContentIndex |
| **Test** | DistributionGroup |

Para detalhes sobre a elaboração de comandos PowerShell acesse o link abaixo e baixe a documentação de referência:

[http://www.microsoft.com/downloads/details.aspx?FamilyId=DF8ED469-9007-401C-85E7-46649A32D0E0&displaylang=en](http://www.microsoft.com/downloads/details.aspx?FamilyId=DF8ED469-9007-401C-85E7-46649A32D0E0&displaylang=en)

Veja abaixo exemplos práticos da utilização de PowerShell para automatização do Microsoft Exchange:

**Adicionar Administrador do Exchange**

Use o cmdlet **Add-ExchangeAdministrator** para adicionar um usuário ou grupo a uma função do Microsoft Exchange Server 2007 específica:

Add-ExchangeAdministrator-identity'trial.com.br/Usercristina aguirre'-Role'OrgAdmin'

**Nova Lista de Endereços**

Use o cmdlet **New-AddressList** para criar uma nova lista de endereços e aplicá-la a destinatários:

new-AddressList -Name 'Suporte' -IncludedRecipients 'AllRecipients' -Container 'Todos os Usuários'

Veja abaixo alguns exemplos práticos do PowerShell para automatização do Microsoft Exchange no Supravizio:

**Criação de e-mail compartilhado:**

**Processo: Criação de Novo usuário de Rede, Email e Internet**

**Evento: Criar conta de email**

```
script = "add-pssnapin microsoft.exchange.management.powershell.admin\n"
script = script + "enable-DistributionGroup -Identity 'trial.com.br/Users/Administração de Empresas' -Alias 'Administraçãodeempresas'"
object = PowerShell.PSExecuteCmdlet(script)
if object != None:
    AvancaProximaAtividade = True
    OrdemServico.Solucao = OrdemServico.Solucao + ". Foi criado novo contato de email compartilhado"
```

**Criação de Novo Contato de Email:**

**Processo: Criação de Novo usuário de Rede, Email e Internet**

**Evento: Criar conta de email**

```
script = "add-pssnapin microsoft.exchange.management.powershell.admin\n"
script = script + "($Private:secureString = ConvertTo-SecureString \"x*\" -AsPlainText -Force) | foreach(Enable-Mailbox -Identity 'trial.com.br/Empregados/" + OrdemServico.Favorecido.UsuarioRede + "' -Alias '" + OrdemServico.Favorecido.UsuarioRede + "' -Databas 'TRIAL02\\First Storage Group\\Mailbox Database')"
object = PowerShell.PSExecuteCmdlet(script)
if object != None:
    AvancaProximaAtividade = True
    OrdemServico.Solucao = OrdemServico.Solucao + ". Foi criado o mailbox para o usuário no Exchange"
```

Para obter mais detalhes e exemplos de PowerShell acesse o link abaixo:

[http://www.microsoft.com/technet/scriptcenter/scripts/msh/default.mspx?mfr=true](http://www.microsoft.com/technet/scriptcenter/scripts/msh/default.mspx?mfr=true)
