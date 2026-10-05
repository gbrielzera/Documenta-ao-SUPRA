# Objeto OpenLDAP

Caminho: Recursos Avançados > Objeto OpenLDAP

O objeto OpenLDAP é um utilitário contendo funções utilizadas em scripts Python para acesso à base do LDAP. Nos exemplos citados, utilizamos as propriedades do Samba. Para saber mais sobre este software, acesse a [documentação no site do desenvolvedor](http://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/passdb.html).

Este objeto possui os seguintes métodos:

**Funções:**

| **Nome** | **Descrição** |
|---|---|
| **AddEntry**(string name, string ou, Hashtable attributes) | Cria uma entrada com seus respectivos atributos. |
| **AddEntry**(string name, string ou, Hashtable attributes, string newEntryIdentifier) | Cria uma entrada com seus respectivos atributos. |
| **AddEntry**(string name, string ou, Hashtable attributes, string ldapHost, string contextUser, string contextPassword, string newEntryIdentifier) | Cria uma entrada com seus respectivos atributos. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **AddEntry**(string name, string ou, Hashtable attributes, string ldapHost, string contextUser, string contextPassword) | Cria uma entrada com seus respectivos atributos. Caso a execução do comando não seja bem sucedida, retornará False. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **DeleteEntry**(string searchFilter) | Realiza a exclusão de uma entrada a partir de um filtro realizado. |
| **DeleteEntry**( string searchFilter, string ldapHost, string contextUser, string contextPassword) | Realiza a exclusão de uma entrada a partir de um filtro realizado. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **EntryExists**(string objectClassName, string entryName) | Verifica se existe na base do OpenLDAP entrada(s) compatíveis com o filtro estabelecido. |
| **EntryExists**(string objectClassName, string entryName, string ldapHost, string contextUser, string contextPassword) | Verifica se existe na base do OpenLDAP entrada(s) compatíveis com o filtro estabelecido. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **GetEntry**(string searchBase, string searchFilter) | Retorna um objeto do tipo Hashtable contendo os atributos de todos os registros recuperados pelo filtro inserido como parâmetro. |
| **GetEntry**(string searchBase, string searchFilter, string ldapHost, string contextUser, string contextPassword) | Retorna um objeto do tipo Hashtable contendo os atributos de todos os registros recuperados pelo filtro inserido como parâmetro. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **GetEntryByName**(string objectClassName, string entryName, bool returnNotNull, string ldapHost, string contextUser, string contextPassword) | Retorna um objeto do tipo Hashtable contendo os atributos do registro recuperado através do nome da entrada. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **GetEntryByName**(string objectClassName, string entryName, bool returnNotNull, string ldapHost, string contextUser, string contextPassword, string searchProperty) | Retorna um objeto do tipo Hashtable contendo os atributos do registro recuperado através do nome da entrada. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **GetEntryByName**(string objectClassName, string entryName, bool returnNotNull, string searchProperty) | Retorna um objeto do tipo Hashtable contendo os atributos do registro recuperado através do nome da entrada. |
| **GetEntryByName**(string objectClassName, string entryName, bool returnNotNull) | Retorna um objeto do tipo Hashtable contendo os atributos do registro recuperado através do nome da entrada. |
| **ModifyEntry**(string searchFilter, Hashtable attributes) | Realiza modificações em atributos de uma entrada na base do OpenLDAP. |
| **ModifyEntry**(string searchFilter, Hashtable attributes, string ldapHost, string contextUser, string contextPassword) | Realiza modificações em atributos de uma entrada na base do OpenLDAP. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
| **ModifyEntryDeleteAttribute**(string searchFilter, string attributeName, string[] attributeValues) | Modifica uma entrada, realizando a exclusão de valores de um de seus atributos. |
| **ModifyEntryDeleteAttribute**(string searchFilter, string attributeName, string[] attributeValues, string ldapHost, string contextUser, string contextPassword) | Modifica uma entrada, realizando a exclusão de valores de um de seus atributos. Também é possível sobrepor os dados inseridos na tela de Configurações, através dos parâmetros ldapHost, contextUser e contextPassword. |
