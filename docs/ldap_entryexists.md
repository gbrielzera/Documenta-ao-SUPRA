# EntryExists

Caminho: Recursos Avançados > Objeto OpenLDAP > EntryExists

Verifica se existe na base do OpenLDAP entrada(s) compatíveis com o filtro estabelecido.

## Assinaturas

OpenLDAP.GetEntry(string searchBase, string searchFilter)

OpenLDAP.GetEntry(string searchBase, string searchFilter, string ldapHost, string contextUser, string contextPassword)

### searchBase

Composto pelo hostname do endereço de diretório, como por exemplo 'venki.corp' será definido como 'dc=venki,dc=corp'

### searchFilter

Filtro utilizado para selecionar a entrada que será pesquisada.

**ldapHost**

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ldapHost**).

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

O método retornará True se houverem entradas compatíveis com o filtro, caso contrário, retornará False.

**Processo: Remover acesso**

**Evento: Remover acessos**

```
import clr
hash = OpenLDAP.GetEntry("dc=venki,dc=corp", "(&(objectClass=person)(uid=" + OrdemServico.Cliente.UsuarioRede + "))")
if hash != None and hash.Contains("givenName"):
    hash = Hashtable()
    hash["sambaAcctFlags"] = "[D ]"
    OpenLDAP.ModifyEntry("cn=" + OrdemServico.Cliente.UsuarioRede + ",dc=venki,dc=corp", hash, "venki.corp", "cn=root,dc=venki,dc=corp", "venki")
```
