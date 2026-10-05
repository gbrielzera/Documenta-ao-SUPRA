# ModifyEntry

Caminho: Recursos Avançados > Objeto OpenLDAP > ModifyEntry

Realiza modificações em atributos de uma entrada na base do OpenLDAP. Caso seja localizada mais de uma entrada a partir do filtro, o comando não será executado.

Assinaturas

ModifyEntry(string searchFilter, Hashtable attributes)

ModifyEntry(string searchFilter, Hashtable attributes, string ldapHost, string contextUser, string contextPassword)

### searchFilter

Filtro utilizado para selecionar a entrada que será pesquisada.

### Attributes

Hashtable de propriedades que serão modificadas.

**ldapHost**

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ldapHost**).

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

O método retornará True se o comando tiver sido executado com sucesso, caso contrário, retornará False.

**Processo: Remoção de acessos**

**Evento: Remover acessos**

```
hash = Hashtable()
hash["sambaAcctFlags"] = "[D ]"
OpenLDAP.ModifyEntry("cn=joaosilva,dc=linuxvenki,dc=corp", hash, "linuxvenki.corp", "cn=root,dc=linuxvenki,dc=corp", "venki")
```
