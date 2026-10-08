# OpenLDAP (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Connectors > OpenLDAP

class `Venki.Services.Connectors.OpenLDAP` — services.dll v18.1.1.0
Herda de **Connector**: os membros da classe base também valem aqui.

## Métodos (18)
- Hashtable GetEntryByName(string objectClassName, string entryName, bool returnNotNull)
- Hashtable GetEntryByName(string objectClassName, string entryName, bool returnNotNull, string ldapHost, string contextUser, string contextPassword)
- Hashtable GetEntryByName(string objectClassName, string entryName, bool returnNotNull, string searchProperty)
- Hashtable GetEntryByName(string objectClassName, string entryName, bool returnNotNull, string ldapHost, string contextUser, string contextPassword, string searchProperty)
- bool EntryExists(string objectClassName, string entryName)
- bool EntryExists(string objectClassName, string entryName, string ldapHost, string contextUser, string contextPassword)
- bool AddEntry(string name, string ou, Hashtable attributes, string newEntryIdentifier)
- bool AddEntry(string name, string ou, Hashtable attributes, string ldapHost, string contextUser, string contextPassword, string newEntryIdentifier)
- bool AddEntry(string name, string ou, Hashtable attributes)
- bool AddEntry(string name, string ou, Hashtable attributes, string ldapHost, string contextUser, string contextPassword)
- bool ModifyEntry(string searchFilter, Hashtable attributes)
- bool ModifyEntry(string searchFilter, Hashtable attributes, string ldapHost, string contextUser, string contextPassword)
- Hashtable GetEntry(string searchBase, string searchFilter)
- Hashtable GetEntry(string searchBase, string searchFilter, string ldapHost, string contextUser, string contextPassword)
- bool DeleteEntry(string searchFilter, string ldapHost, string contextUser, string contextPassword)
- bool DeleteEntry(string searchFilter)
- bool ModifyEntryDeleteAttribute(string searchFilter, string attributeName, string[] attributeValue, string ldapHost, string contextUser, string contextPassword)
- bool ModifyEntryDeleteAttribute(string searchFilter, string attributeName, string[] attributeValue)
