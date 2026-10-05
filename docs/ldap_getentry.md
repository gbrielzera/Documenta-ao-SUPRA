# GetEntry

Caminho: Recursos Avançados > Objeto OpenLDAP > GetEntry

Retorna um objeto do tipo Hashtable contendo os atributos de todos os registros recuperados pelo filtro inserido como parâmetro.

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

Retornará um objeto do tipo Hashtable contendo as entradas localizadas.

**Processo: Acesso a Sistema e Recursos de Rede**

**Evento: Existe usuário?**

```
import clr
hash = OpenLDAP.GetEntry("dc=venki,dc=corp", "(&(objectClass=person)(uid="+ OrdemServico.Cliente.UsuarioRede +"))")
if hash != None and hash.Contains("givenName"):
    OrdemServico.SetCustom("MENSAGEM", "Acesso do usuário " + hash["givenName"].ToString() + " implementado com sucesso." )
```
