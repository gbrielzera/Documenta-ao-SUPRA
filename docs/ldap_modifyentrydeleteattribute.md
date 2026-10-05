# ModifyEntryDeleteAttribute

Caminho: Recursos Avançados > Objeto OpenLDAP > ModifyEntryDeleteAttribute

Modifica uma entrada, realizando a exclusão de valores de um de seus atributos. Caso seja localizada mais de uma entrada a partir do filtro, o comando não será executado.

## Assinaturas

OpenLDAP.ModifyEntryDeleteAttribute(searchFilter, attributeName, attributeValue)

OpenLDAP.ModifyEntryDeleteAttribute(searchFilter, attributeName, attributeValue, ldapHost, contextUser, contextPassword)

### searchFilter

Filtro utilizado para selecionar a entrada que será pesquisada.

### attributeName

Nome do atributo que será modificado.

### attributeValues

Array com os valores que serão excluídos da propriedade.

**ldapHost**

Endereço do Serviço de Diretório que sobrepõe a configuração realizada na tela **Configurações**.

### contextUser

Nome de usuário a ser utilizado para acessar o Serviço de Diretório (referente ao diretório destino do endereço configurado em **ldapHost**).

### contextPassword

Senha do usuário definida no parâmetro contextUser.

### Retorno

O método retornará True se o comando tiver sido executado com sucesso, caso contrário, retornará False.

**Processo: Remover acesso**

**Evento: Remover acessos**

```
import System
import clr
member = Array.CreateInstance(str,1)
member[0] = OrdemServico.Cliente.UsuarioRede
OpenLDAP.ModifyEntryDeleteAttribute("(&(objectClass=posixGroup)(cn=func))"), "memberUid", member, "venki.corp", "cn=root,dc=venki,dc=corp", "venki")
```
