# DeleteEntry

Caminho: Recursos Avançados > Objeto OpenLDAP > DeleteEntry

Realiza a exclusão de uma entrada a partir de um filtro realizado. Caso seja localizada mais de uma entrada a partir do filtro, o comando não será executado.

## Assinaturas

OpenLDAP.DeleteEntry(searchFilter)

OpenLDAP.DeleteEntry(searchFilter, ldapHost, contextUser, contextPassword)

### searchFilter

Filtro utilizado para selecionar a entrada que será pesquisada.

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
import clr
OpenLDAP.DeleteEntry("dc=venki,dc=corp", "(&(objectClass=person)(uid=" + OrdemServico.Cliente.UsuarioRede + ")")
```
