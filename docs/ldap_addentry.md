# AddEntry

Caminho: Recursos Avançados > Objeto OpenLDAP > AddEntry

Cria uma entrada com seus respectivos atributos.

## Assinaturas

OpenLDAP.AddEntry(string name, string ou, Hashtable attributes)

OpenLDAP.AddEntry(string name, string ou, Hashtable attributes, string newEntryIdentifier)

OpenLDAP.AddEntry(string name, string ou, Hashtable attributes, string ldapHost, string contextUser, string contextPassword, string newEntryIdentifier)

OpenLDAP.AddEntry(string name, string ou, Hashtable attributes, string ldapHost, string contextUser, string contextPassword)

**name**

Nome da nova entrada.

**Ou**

OrganizationUnit na qual será alocada a nova entrada.

**Attributes**

Hashtable contendo as propriedades que serão adicionadas.

**newEntryIdentifier**

Identificador desta nova entrada.

**ldapHost**

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ldapHost**).

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

O método retornará True se o comando tiver sido executado com sucesso, caso contrário, retornará False.

**Processo: Criação de Novo Usuário de Rede, Email e internet**

**Evento: Criar usuário no OpenLDAP**

```
hash = Hashtable()
hash["sn"] = "souza"
hash["objectClass"] = "person"
sucesso = OpenLDAP.AddEntry("souzasilva", "people", hash, "cn")
OrdemServico.SetCustom("SUCESSO", sucesso)
```
