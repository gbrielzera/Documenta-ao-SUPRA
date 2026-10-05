# GetEntryByName

Caminho: Recursos Avançados > Objeto OpenLDAP > GetEntryByName

Retorna um objeto do tipo Hashtable contendo os atributos do registro recuperado através do nome da entrada.

## Assinaturas

OpenLDAP.GetEntryByName(string objectClassName, string entryName, bool returnNotNull)

OpenLDAP.GetEntryByName(string objectClassName, string entryName, bool returnNotNull, string searchProperty)

OpenLDAP.GetEntryByName(string objectClassName, string entryName, bool returnNotNull, string ldapHost, string contextUser, string contextPassword)

OpenLDAP.GetEntryByName(string objectClassName, string entryName, bool returnNotNull, string ldapHost, string contextUser, string contextPassword, string searchProperty)

### objectClassName

Nome do tipo de objeto que está procurando.

### entryName

Nome do entrada a que está procurando.

### returnNotNull

Caso seja definido como True, ao não encontrar nenhuma entrada, será lançada uma exceção informando o critério de recuperação. Se for definido como False, retornará False ao não localizar nenhuma entrada.

### searchProperty

Nome da propriedade utilizada para fazer a busca.

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
hash = OpenLDAP.GetEntryByName("person", "'" + OrdemServico.Cliente.UsuarioRede + "'", False)
if hash != None and hash.Contains("uid"):
    OrdemServico.SetCustom("MENSAGEM", "Acesso do usuário " + hash["givenName"].ToString() + " implementado com sucesso." )
```
