# Ambiente de execução dos scripts na 19.1.1 (testado)

Fonte: diagnóstico rodado pelo usuário em **Qualidade**, portal web, 2026-11-26 (`dir`/reflexão gravados em comentários). [testado]
Vale para o servidor testado; aparecer aqui não prova que o método funciona nem que o uso é permitido.

## Versões
- .NET CLR 4.0.30319.42000; Windows NT 10.0.26100.0; IronPython 2.7 (`sys.version` 2.7.3).
- Oracle Database 19c; sessão com `NLS_DATE_FORMAT` = `DD-MON-RR` e `NLS_NUMERIC_CHARACTERS` = `.,`.

## Módulos Python
- Importam: `re`, `datetime`, `time`, `math`, `itertools`, `unicodedata`.
- **Não** importam ("No module named"): `json`, `random`, `csv`, `base64`, `hashlib`, `hmac`, `uuid`, `urllib`, `urllib2`, `xml.etree.ElementTree`, `xml.dom.minidom`, `zipfile`, `io`, `os`, `collections`, `decimal`, `textwrap`, `smtplib`.
- Use .NET no lugar da biblioteca padrão. Bibliotecas de scripts do cliente (`validaCNPJ`, `peopleSoft`...) são outra coisa: vêm do cadastro.

## Referências .NET (`clr.AddReference`)
- Carregam: `System.Core`, `System.Data`, `System.Xml`, `System.Xml.Linq`, `System.Web`, `System.Web.Extensions`, `System.Net.Http`, `System.Drawing`, `System.Configuration`, `System.DirectoryServices`, `System.IO.Compression`, `System.IO.Compression.FileSystem`, `Newtonsoft.Json`, `ICSharpCode.SharpZipLib`.
- Não carregam: `DocumentFormat.OpenXml`, `EPPlus`, `ClosedXML`, `NPOI`, `itextsharp`, `Aspose.Cells`, `Aspose.Words`, `Ionic.Zip`.

## Equivalentes para o que falta no Python (sugestão pelas bibliotecas presentes; teste antes)
| Preciso de | Use |
|---|---|
| JSON | `Newtonsoft.Json` (`JsonConvert`, `JObject`; já usado em fluxos) |
| HTTP | `System.Net.Http.HttpClient` (já usado em fluxos) |
| Base64 | `Convert.ToBase64String` / `Convert.FromBase64String` |
| Hash e HMAC | `System.Security.Cryptography` |
| Aleatório e GUID | `Random()`, `Guid.NewGuid()` |
| Arquivos e caminhos | `System.IO` |
| ZIP | `System.IO.Compression.ZipFile` ou `ICSharpCode.SharpZipLib` |
| XML | `System.Xml.Linq` |
| Escapar HTML ou URL | `System.Net.WebUtility`, `Uri.EscapeDataString` |
| Excel, Word, PDF | DevExpress está carregado (`Spreadsheet`, `RichEdit`, `Pdf`). É biblioteca comercial usada pelo produto: **confirme com a equipe/Venki se a licença permite usar em script** antes de adotar |

## Bibliotecas carregadas no servidor (sem as páginas `App_*`)
AngleSharp 0.9.9.0, Core 1.0.9477.28406, Core.Interface 1.0.9477.28409, Core.Interface.Web 19.1.1.0, Core.Server 1.0.9477.28413, EAGetMail 5.2.5.5, EAGetMail40 4.0.0.1, EASendMail 7.9.0.2, EASendMail40 6.0.0.5, EntLibContrib.Data.MySql 5.0.505.0, EntLibContrib.Data.OdpNet 5.0.505.0, HtmlSanitizer 4.0.0.0, ICSharpCode.SharpZipLib 0.85.5.452, Interop.ActiveDs 1.0.0.0, IronPython 2.7.0.40, IronPython.Modules 2.7.0.40, Itenso.Rtf.Converter.Html 1.5.0.0, Itenso.Rtf.Interpreter 1.5.0.0, Itenso.Rtf.Parser 1.5.0.0, Itenso.Sys 2.3.0.0, Microsoft.Build.Framework 4.0.0.0, Microsoft.Build.Utilities.v4.0 4.0.0.0, Microsoft.CSharp 4.0.0.0, Microsoft.Dynamic 1.1.0.20, Microsoft.JScript 10.0.0.0, Microsoft.Practices.EnterpriseLibrary.Caching 5.0.505.0, Microsoft.Practices.EnterpriseLibrary.Common 5.0.505.0, Microsoft.Practices.EnterpriseLibrary.Data 5.0.505.0, Microsoft.Practices.EnterpriseLibrary.Logging 5.0.505.0, Microsoft.Practices.EnterpriseLibrary.Logging.Database 5.0.505.0, Microsoft.Practices.ServiceLocation 1.0.0.0, Microsoft.Practices.Unity 2.1.505.0, Microsoft.Practices.Unity.Interception 2.1.505.0, Microsoft.Scripting 1.1.0.20, Microsoft.Scripting.Metadata 1.1.0.20, Microsoft.Threading.Tasks 1.0.12.0, Microsoft.Threading.Tasks.Extensions 1.0.12.0, Microsoft.Threading.Tasks.Extensions.Desktop 1.0.168.0, Microsoft.Web.SessionState.SqlInMemory 13.0.0.0, MySql.Data 6.8.3.0, Newtonsoft.Json 4.5.0.0, Oracle.DataAccess 4.112.3.0, Oracle.Web 4.112.3.0, PDFSignDll 8.6.0.0, Persistence 1.0.9477.28409, SMDiagnostics 4.0.0.0, Services 19.1.1.0, Services.Custom 19.1.1.0, Services.Interface19.1.1.0, Services.Interface.Web 19.1.1.0, Services.Server 19.1.1.0, Services.Update 1.0.0.0, Services.UpdateMetadata 19.1.1.0, Services.UpdateMetadata& 1.0.0.0, StackExchange.Redis 1.2.1.0, Supravizio 19.1.1.0, Supravizio.Custom 19.1.1.0, Supravizio.Interface 19.1.1.0, Supravizio.Interface.Web 19.1.1.0, Supravizio.Server 19.1.1.0, Supravizio.UpdateMetadata 19.1.1.0, Supravizio.UpdateMetadata& 1.0.0.0, Supravizio.Validar.Interface 19.1.1.0, Supravizio.Validar.Servidor 19.1.1.0, System 4.0.0.0, System.Activities 4.0.0.0, System.ComponentModel.DataAnnotations 4.0.0.0, System.Configuration 4.0.0.0, System.Configuration.Install 4.0.0.0, System.Core 4.0.0.0, System.Data 4.0.0.0, System.Data.DataSetExtensions 4.0.0.0, System.Data.Entity 4.0.0.0, System.Data.Linq 4.0.0.0, System.Data.OracleClient 4.0.0.0, System.Data.Services.Design 4.0.0.0, System.Design 4.0.0.0, System.Diagnostics.Tracing 4.0.0.0, System.DirectoryServices 4.0.0.0, System.Drawing 4.0.0.0, System.EnterpriseServices 4.0.0.0, System.IO 4.0.0.0, System.IdentityModel 4.0.0.0, System.Management 4.0.0.0, System.Management.Automation 3.0.0.0, System.Messaging 4.0.0.0, System.Net 4.0.0.0, System.Net.Http 4.0.0.0, System.Numerics 4.0.0.0, System.Runtime 4.0.0.0, System.Runtime.Caching 4.0.0.0, System.Runtime.InteropServices 4.0.0.0, System.Runtime.Remoting 4.0.0.0, System.Runtime.Serialization 4.0.0.0, System.Security 4.0.0.0, System.ServiceModel 4.0.0.0, System.ServiceModel.Activation 4.0.0.0, System.ServiceModel.Activities 4.0.0.0, System.ServiceModel.Internals 4.0.0.0, System.ServiceModel.Web 4.0.0.0, System.Threading.Tasks 4.0.0.0, System.Transactions 4.0.0.0, System.Web 4.0.0.0, System.Web.ApplicationServices 4.0.0.0, System.Web.DynamicData 4.0.0.0, System.Web.Entity 4.0.0.0, System.Web.Extensions 4.0.0.0, System.Web.Mobile 4.0.0.0, System.Web.RegularExpressions 4.0.0.0, System.Web.Services 4.0.0.0, System.Windows.Forms 4.0.0.0, System.Windows.Interactivity 4.0.0.0, System.WorkflowServices 4.0.0.0, System.Xaml 4.0.0.0, System.Xaml.Hosting 4.0.0.0, System.Xml 4.0.0.0, System.Xml.Linq 4.0.0.0, Updater.Interface 19.1.1.0, Updater.Server 19.1.1.0, WindowsBase 4.0.0.0, mscorlib 4.0.0.0, stdole 7.0.3300.0

DevExpress 17.2 (81 pacotes), entre eles: DevExpress.Docs.v17.2 17.2.7.0, DevExpress.Pdf.v17.2.Core 17.2.7.0, DevExpress.Pdf.v17.2.Drawing 17.2.7.0, DevExpress.Printing.v17.2.Core 17.2.7.0, DevExpress.RichEdit.v17.2.Core 17.2.7.0, DevExpress.RichEdit.v17.2.Export 17.2.7.0, DevExpress.Spreadsheet.v17.2.Core 17.2.7.0, DevExpress.Web.ASPxRichEdit.v17.2 17.2.7.0, DevExpress.Web.ASPxSpreadsheet.v17.2 17.2.7.0, DevExpress.XtraPdfViewer.v17.2 17.2.7.0, DevExpress.XtraPrinting.v17.2 17.2.7.0, DevExpress.XtraRichEdit.v17.2 17.2.7.0, DevExpress.XtraRichEdit.v17.2.Extensions 17.2.7.0, DevExpress.XtraSpreadsheet.v17.2 17.2.7.0.

## Membros dos objetos em tempo de execução
Formato: tipo de retorno, nome e parâmetros; `*` = propriedade gravável. A comparação com `catalogo/api/` (DLLs 18.1.1)
mostrou a mesma API em `OrdemServico`, `Utils`, `DB`, `AD`, `OpenLDAP`, `PowerShell`, `Atividade` e `Criticas` (diferem só
`Name`, o indexador `Item` e membros da classe base). Novidade real: o controle do portal web, `ControleFormularioWeb`.

### Controle (ControleFormularioWeb)
`ControleFormularioWeb`

- `Boolean CarregaItensSobDemanda*`
- `Boolean ControleVisualEhCombo()`
- `Boolean ControleVisualEhLabel()`
- `Boolean Habilitado*`
- `Boolean HabilitadoFormulario*`
- `Boolean MascaraIncluiLiteral*`
- `Boolean PermiteModificar*`
- `Boolean PossuiControleVisual(Object controleVisual)`
- `Boolean Visivel*`
- `ControleFormularioWeb ProximoControle*`
- `IFormulario Formulario*`
- `Object Itens*`
- `Object Valor*`
- `String IdControleVisual`
- `String Mascara*`
- `String Nome`
- `String ScriptModificado*`
- `Void Atualiza()`
- `Void AtualizaControles(Web.UI.Control controleVisual, Web.UI.WebControls.TableRow controlRow)`
- `Void AtualizaItensComboControleVisual()`
- `Void CorrigeNullTextCombobox()`
- `Void Dispose()`
- `Void SalvaEstadoFormulario()`

### Formulario
`Venki.Supravizio.Processo.Script.FormularioTarefa`

- `Boolean IsModified*`
- `Boolean NecessitaAtualizarFormulario*`
- `Boolean PermiteExecutarScriptModificado*`
- `Boolean PossuiControle(Supravizio.Processo.NomeCampo nomeCampo, String nomeCustomizado)`
- `Dictionary'2[String,Supravizio.Processo.Script.ControleFormulario] Controles`
- `String NomeControleFormularioExecucao*`
- `Supravizio.Processo.OrdemServico OrdemServico*`
- `Supravizio.Processo.Script.ControleFormulario Item`
- `Supravizio.Processo.Script.ControleFormulario ObtemControleFormulario(Object controleVisual)`
- `Type TipoControleNaoEncontrado*`
- `Void AdicionaControle(String nomeControle, Supravizio.Processo.Script.ControleFormulario controle)`
- `Void Dispose()`
- `Void ExibeMensagem(String mensagem)`
- `Void ModificaHabilitadoCampo(String campo, Boolean novoValor)`
- `Void ModificaMascaraCampo(String campo, String mascara, Boolean incluiLiteral)`
- `Void ModificaVisibilidadeCampo(String campo, Boolean novoValor)`

### Criticas
`Venki.Supravizio.Processo.CriticaValidacaoList`

- `Boolean Equals(Object obj)`
- `Boolean PossuiAviso`
- `Boolean PossuiPendencia`
- `Collections.ArrayList Itens`
- `String ToString()`
- `Void AdicionaAviso(String mensagem)`
- `Void AdicionaAviso(String mensagem, String grupo)`
- `Void AdicionaAviso(String mensagem, String grupo, Nullable'1[Supravizio.Processo.NomeCampo] campo, String campoAssociado)`
- `Void AdicionaAviso(String mensagem, String grupo, String campoAssociado)`
- `Void AdicionaAviso(Supravizio.Processo.CriticaValidacao criticaOrigem)`
- `Void AdicionaInformacao(String mensagem)`
- `Void AdicionaInformacao(String mensagem, String grupo)`
- `Void AdicionaInformacao(String mensagem, String grupo, Nullable'1[Supravizio.Processo.NomeCampo] campo, String campoAssociado)`
- `Void AdicionaInformacao(String mensagem, String grupo, String campoAssociado)`
- `Void AdicionaInformacao(Supravizio.Processo.CriticaValidacao criticaOrigem)`
- `Void AdicionaPendencia(String mensagem)`
- `Void AdicionaPendencia(String mensagem, String grupo)`
- `Void AdicionaPendencia(String mensagem, String grupo, Nullable'1[Supravizio.Processo.NomeCampo] campo, String campoAssociado)`
- `Void AdicionaPendencia(String mensagem, String grupo, String campoAssociado)`
- `Void AdicionaPendencia(Supravizio.Processo.CriticaValidacao criticaOrigem)`

### DB
`Venki.Services.Connectors.DB`

- `Boolean EnableCache*`
- `Boolean Equals(Object obj)`
- `Data.Common.DbParameter NewDBInputOutputParam(String name, Object value)`
- `Data.Common.DbParameter NewDBInputParam(String name, Object value)`
- `Data.Common.DbParameter NewDBOutputParam(String name)`
- `Data.DataTable ExecuteDataTable(String commandText)`
- `Data.DataTable ExecuteDataTable(String commandText, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Data.DataTable ExecuteDataTable(String commandText, String database)`
- `Data.DataTable ExecuteDataTable(String commandText, String database, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Int32 ExecuteNonQuery(String commandText)`
- `Int32 ExecuteNonQuery(String commandText, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Int32 ExecuteNonQuery(String commandText, Stringdatabase)`
- `Int32 ExecuteNonQuery(String commandText, String database, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Int32 GetHashCode()`
- `Object ExecuteScalar(String commandText)`
- `Object ExecuteScalar(String commandText, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Object ExecuteScalar(String commandText, String database)`
- `Object ExecuteScalar(String commandText, String database, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Object ExecuteStoredProc(String storedProcName, Data.Common.DbParameter[] parameters)`
- `Object ExecuteStoredProc(String storedProcName, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Object ExecuteStoredProc(String storedProcName, String database)`
- `Object ExecuteStoredProc(String storedProcName, String database, Data.Common.DbParameter[] parameters)`
- `Object ExecuteStoredProc(String storedProcName, String database, IronPython.Runtime.List paramListNames, IronPython.Runtime.List paramListValues)`
- `Object ExecuteStoredProc(String storedProcName, String paramName1, Object paramValue1, String paramName2, Object paramValue2, String paramName3, Object paramValue3)`
- `String Name*`
- `String ToString()`

### PowerShell
`Venki.Services.Connectors.PowerShell`

- `Boolean Equals(Object obj)`
- `Int32 GetHashCode()`
- `Object PSExecuteCmdlet(String command)`
- `Object PSExecuteCmdlet(String command, String parName1, Object parValue1, String parName2, Object parValue2, String parName3, Object parValue3)`
- `String Name*`
- `String ToString()`

### WebService
`Venki.Services.Connectors.WebService`

- `Boolean Equals(Object obj)`
- `Int32 GetHashCode()`
- `Object LoadWebService(String url)`
- `String Name*`
- `String ToString()`

### OpenLDAP
`Venki.Services.Connectors.OpenLDAP`

- `Boolean AddEntry(String name, String ou, Collections.Hashtable attributes)`
- `Boolean AddEntry(String name, String ou, Collections.Hashtable attributes, String ldapHost, String contextUser, String contextPassword)`
- `Boolean AddEntry(String name, String ou, Collections.Hashtable attributes, String ldapHost, String contextUser, String contextPassword, String newEntryIdentifier)`
- `Boolean AddEntry(String name, String ou, Collections.Hashtable attributes, String newEntryIdentifier)`
- `Boolean DeleteEntry(String searchFilter)`
- `Boolean DeleteEntry(String searchFilter, String ldapHost, String contextUser, String contextPassword)`
- `Boolean EntryExists(String objectClassName, String entryName)`
- `Boolean EntryExists(String objectClassName, String entryName, String ldapHost, String contextUser, String contextPassword)`
- `Boolean Equals(Object obj)`
- `Boolean ModifyEntry(String searchFilter, Collections.Hashtable attributes)`
- `Boolean ModifyEntry(String searchFilter, Collections.Hashtable attributes, String ldapHost, String contextUser, String contextPassword)`
- `Boolean ModifyEntryDeleteAttribute(String searchFilter, String attributeName, String[] attributeValue)`
- `Boolean ModifyEntryDeleteAttribute(String searchFilter, String attributeName, String[] attributeValue, String ldapHost, String contextUser, String contextPassword)`
- `Collections.Hashtable GetEntry(String searchBase, String searchFilter)`
- `Collections.Hashtable GetEntry(String searchBase, String searchFilter, String ldapHost, String contextUser, String contextPassword)`
- `Collections.Hashtable GetEntryByName(String objectClassName, String entryName, Boolean returnNotNull)`
- `Collections.Hashtable GetEntryByName(String objectClassName, String entryName, Boolean returnNotNull, String ldapHost, String contextUser, String contextPassword)`
- `Collections.Hashtable GetEntryByName(String objectClassName, String entryName, Boolean returnNotNull, String ldapHost, String contextUser, String contextPassword, String searchProperty)`
- `Collections.Hashtable GetEntryByName(String objectClassName, String entryName, Boolean returnNotNull, String searchProperty)`
- `Int32 GetHashCode()`
- `String Name*`
- `String ToString()`

### AD
`Venki.Services.Connectors.AD`

- `Boolean AddUserToGroup(String username, String group)`
- `Boolean AddUserToGroup(String username, String group, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean AuthenticateUser(String username, String password)`
- `Boolean AuthenticateUser(String username, String password, String LDAPAddress)`
- `Boolean CreateGlobalGroup(String name, String ou, Boolean security, String managedby, String description)`
- `Boolean CreateGlobalGroup(String name, String ou, Boolean security, String managedby, String description, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean CreateLocalGroup(String name, String ou, Boolean security, String managedby, String description)`
- `Boolean CreateLocalGroup(String name, String ou, Boolean security, String managedby, String description, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean CreateUniversalGroup(String name, String ou, String managedby, String description)`
- `Boolean CreateUniversalGroup(String name, String ou, String managedby, String description, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean CreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName)`
- `Boolean CreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean CreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName, String userPrincipalName, String fullName)`
- `Boolean CreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName, String userPrincipalName, String fullName, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean DisableUser(String username)`
- `Boolean DisableUser(String username, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean EnableUser(String username)`
- `Boolean EnableUser(String username, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean Equals(Object obj)`
- `Boolean GroupExists(String group)`
- `Boolean GroupExists(String group, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean RemoveUser(String username)`
- `Boolean RemoveUser(String username, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean RemoveUserFromGroup(String username, String group)`
- `Boolean RemoveUserFromGroup(String username, String group, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean ResetUser(String username, String password)`
- `Boolean ResetUser(String username, String password, Boolean changepasswordnextlogon)`
- `Boolean ResetUser(String username, String password, Boolean changepasswordnextlogon, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean ResetUser(String username, String password, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean SetAccountExpirationDate(String username, DateTime accountExpirationDate)`
- `Boolean SetAccountExpirationDate(String username, DateTime accountExpirationDate, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UnLockUser(String username)`
- `Boolean UnLockUser(String username, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UserClearManager(String user)`
- `Boolean UserClearManager(String user, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UserExists(String username)`
- `Boolean UserExists(String username, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UserExistsInGroup(String username, String groupname)`
- `Boolean UserExistsInGroup(String username, String groupname, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UserIsDisabled(String username)`
- `Boolean UserIsDisabled(String username, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UserIsLocked(String username)`
- `Boolean UserIsLocked(String username, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UserWriteManager(String user, String manager)`
- `Boolean UserWriteManager(String user, String manager, String LDAPAddress, String contextUser, String contextPassword)`
- `Boolean UserWriteProperty(String username, String property, Int32 value)`
- `Boolean UserWriteProperty(String username, String property, Int32 value, String LDAPAddress, String contextUser,String contextPassword)`
- `Boolean UserWriteProperty(String username, String property, String value)`
- `Boolean UserWriteProperty(String username, String property, String value, String LDAPAddress, String contextUser, String contextPassword)`
- `Int32 GetHashCode()`
- `Object UserReadProperty(String username, String property)`
- `Object UserReadProperty(String username, String property, String LDAPAddress, String contextUser, String contextPassword)`
- `String Name*`
- `String ToString()`

### Utils
`Venki.Services.Utils`

- `Boolean ADAddUserToGroup(String username, String group)`
- `Boolean ADAddUserToGroup(String username, String group, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADAuthenticateUser(String username, String password)`
- `Boolean ADAuthenticateUser(String username, String password, String ADAddress)`
- `Boolean ADCreateGlobalGroup(String name, String ou, Boolean security, String managedby, String description)`
- `Boolean ADCreateGlobalGroup(String name, String ou, Boolean security, String managedby, String description, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADCreateLocalGroup(String name, String ou, Boolean security, String managedby, String description)`
- `Boolean ADCreateLocalGroup(String name, String ou, Boolean security, String managedby, String description, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADCreateUniversalGroup(String name, String ou, String managedby, String description)`
- `Boolean ADCreateUniversalGroup(String name, String ou, String managedby, String description, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADCreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName)`
- `Boolean ADCreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADCreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName, String userPrincipalName, String fullName)`
- `Boolean ADCreateUser(String username, String ou, String firstName, String lastName, String employeeID, String displayName, String userPrincipalName, String fullName, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADDisableUser(String username)`
- `Boolean ADDisableUser(String username, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADEnableUser(String username)`
- `Boolean ADEnableUser(String username, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADGroupExists(String group)`
- `Boolean ADGroupExists(String group, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADRemoveUser(String username)`
- `Boolean ADRemoveUser(String username, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADRemoveUserFromGroup(String username, String group)`
- `Boolean ADRemoveUserFromGroup(String username, String group, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADResetUser(String username, String password)`
- `Boolean ADResetUser(String username, String password, Boolean changepasswordnextlogon)`
- `Boolean ADResetUser(String username, String password, Boolean changepasswordnextlogon, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADResetUser(String username, String password, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADSetAccountExpirationDate(String username, DateTime accountExpirationDate)`
- `Boolean ADSetAccountExpirationDate(String username, DateTime accountExpirationDate, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUnLockUser(String username)`
- `Boolean ADUnLockUser(String username, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserClearManager(String user)`
- `Boolean ADUserClearManager(String user, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserExists(String username)`
- `Boolean ADUserExists(String username,String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserExistsInGroup(String username, String groupname)`
- `Boolean ADUserExistsInGroup(String username, String groupname, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserIsDisabled(String username)`
- `Boolean ADUserIsDisabled(String username, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserIsLocked(String username)`
- `Boolean ADUserIsLocked(String username, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserWriteManager(String user, String manager)`
- `Boolean ADUserWriteManager(String user, String manager, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserWriteProperty(String username, String property, Int32 value)`
- `Boolean ADUserWriteProperty(String username, String property, Int32 value, String ADAddress, String contextUser, String contextPassword)`
- `Boolean ADUserWriteProperty(String username, String property, String value)`
- `Boolean ADUserWriteProperty(String username, String property, String value, String ADAddress, String contextUser, String contextPassword)`
- `Boolean Equals(Object obj)`
- `Data.Common.DbParameter NewDBInputOutputParam(String name, Object value)`
- `Data.Common.DbParameter NewDBInputParam(String name, Object value)`
- `Data.Common.DbParameter NewDBOutputParam(String name)`
- `Data.DataTable ExecuteDataTable(String commandText)`
- `Data.DataTable ExecuteDataTable(String commandText, String database)`
- `Int32 ExecuteNonQuery(String commandText)`
- `Int32 ExecuteNonQuery(String commandText, String database)`
- `Int32 GetHashCode()`
- `Int32 NewSequenceValue(String sequenceName)`
- `Object ADUserReadProperty(String username, String property)`
- `Object ADUserReadProperty(String username, String property, String ADAddress, String contextUser, String contextPassword)`
- `Object ExecuteScalar(String commandText)`
- `Object ExecuteScalar(String commandText, String database)`
- `Object ExecuteStoredProc(String storedProcName)`
- `Object ExecuteStoredProc(String storedProcName, Data.Common.DbParameter[] parameters)`
- `Object ExecuteStoredProc(String storedProcName, String database)`
- `Object ExecuteStoredProc(String storedProcName, String database, Data.Common.DbParameter[] parameters)`
- `Object ExecuteStoredProc(String storedProcName, String paramName1, Object paramValue1, String paramName2, Object paramValue2, String paramName3, Object paramValue3)`
- `Object IF(Boolean testExpression, Object ifValue, Object elseValue)`
- `Object LoadWebService(String url)`
- `Object PSExecuteCmdlet(String command)`
- `Object PSExecuteCmdlet(String command, String parName1, Object parValue1, String parName2, Object parValue2, String parName3, Object parValue3)`
- `String DecryptParametersQueryString(String cryptedText)`
- `String DecryptUrl(String encryptedUrl)`
- `String EncryptParametersQueryString(String parameters)`
- `String EncryptUrl(String url)`
- `String GetLocalizedObject(Core.Custom.SessionObjectProxy dataItem, String propertyName)`
- `String GetLocalizedObject(Core.Custom.SessionObjectProxy dataItem, String propertyName, String defaultText)`
- `String ToString()`
- `Void ExecuteScript(String script)`
- `Void ExecuteScript(String script, String parName1, Object parValue1, String parName2, Object parValue2, String parName3, Object parValue3)`
- `Void LogError(String message, String category)`
- `Void LogInformation(String message, String category)`
- `Void LogWarning(String message, String category)`
- `Void SendMail(String from, String to, String subject, String body)`
- `Void SendMail(String from, String to, String subject, String body, Core.Custom.SessionObjectProxy dataItem)`
- `Void SendMail(String from, String to, String subject, String body, Core.Custom.SessionObjectProxy dataItem, Int32 temporality)`
- `Void SendMail(String from, String to, String subject, String body, Core.Custom.SessionObjectProxy dataItem, String replyAddress)`
- `Void SendMail(String from, String to, String subject, String body, String recoveryCode)`

### Atividade
`Venki.Supravizio.Processo.Custom.Atividade`

- `Boolean AnexarTodosDocumentos*`
- `Boolean Ativo*`
- `Boolean ChamadaAssincrona*`
- `Boolean CicloAnualUltimoDiaMes*`
- `Boolean CicloDiarioDomingo*`
- `Boolean CicloDiarioQuarta*`
- `Boolean CicloDiarioQuinta*`
- `Boolean CicloDiarioSabado*`
- `Boolean CicloDiarioSegunda*`
- `Boolean CicloDiarioSexta*`
- `Boolean CicloDiarioTerca*`
- `Boolean CicloMensalAbril*`
- `Boolean CicloMensalAgosto*`
- `Boolean CicloMensalDezembro*`
- `Boolean CicloMensalFevereiro*`
- `Boolean CicloMensalJaneiro*`
- `Boolean CicloMensalJulho*`
- `Boolean CicloMensalJunho*`
- `Boolean CicloMensalMaio*`
- `Boolean CicloMensalMarco*`
- `Boolean CicloMensalNovembro*`
- `Boolean CicloMensalOutubro*`
- `Boolean CicloMensalSetembro*`
- `Boolean CicloMensalUltimoDiaMes*`
- `Boolean ConfirmaResponsabilidade*`
- `Boolean EnviaMensagemIndividual*`
- `Boolean Equals(Object obj)`
- `Boolean ExigeApontamento*`
- `Boolean FinalizarInterrupcao*`
- `Boolean IncluiValidacaoFinal*`
- `Boolean IsNew`
- `Boolean Modified`
- `Boolean MultiplasInstancias*`
- `Boolean PassaTodosItens*`
- `Boolean PermissaoRestritaPapel*`
- `Boolean PermiteCancelamentoAA*`
- `Boolean PermiteVoltar*`
- `Boolean PermitirRascunho*`
- `Boolean PreencheClienteSolucionador*`
- `Boolean PreencheMotivoReprovacao*`
- `Boolean ReadOnly`
- `Boolean RelatorioObrigatorio*`
- `Boolean RetornaTodosItens*`
- `Boolean SincronizaCancelamento*`
- `Boolean TransicaoAutomatica*`
- `Core.Custom.SessionProxyList Acoes`
- `Core.Custom.SessionProxyList AssociacoesSubprocesso`
- `Core.Custom.SessionProxyList ClientesAutorizados`
- `Core.Custom.SessionProxyList FluxosSaida`
- `Core.Custom.SessionProxyList Opcoes`
- `Core.Custom.SessionProxyList Operacoes`
- `Core.Custom.SessionProxyList PassagemItens`
- `Core.Custom.SessionProxyList Relatorios`
- `Core.Custom.SessionProxyList RetornoItens`
- `Core.Custom.SessionProxyList TiposAnexosMensagem`
- `Core.Custom.SessionProxyList ValoresInputs`
- `Core.SessionObject Instance`
- `Int32 GetHashCode()`
- `Int32 Id`
- `Nullable'1[Int32] AssociacaoId`
- `Nullable'1[Int32] CaixaEmailId*`
- `Nullable'1[Int32] CicloAnualDiaMes*`
- `Nullable'1[Int32] CicloAnualHora*`
- `Nullable'1[Int32] CicloAnualMes*`
- `Nullable'1[Int32] CicloAnualMinuto*`
- `Nullable'1[Int32] CicloDiarioHora*`
- `Nullable'1[Int32] CicloDiarioMinuto*`
- `Nullable'1[Int32] CicloMensalDiaMes*`
- `Nullable'1[Int32] CicloMensalHora*`
- `Nullable'1[Int32] CicloMensalMinuto*`
- `Nullable'1[Int32] CicloSemanalHora*`
- `Nullable'1[Int32] CicloSemanalMinuto*`
- `Nullable'1[Int32] ClasseAnexoRespostaId*`
- `Nullable'1[Int32] ClassePesquisaSatisfacaoId*`
- `Nullable'1[Int32] ClasseSubProcessoId*`
- `Nullable'1[Int32] ControleId*`
- `Nullable'1[Int32] MaximoExecucao*`
- `Nullable'1[Int32] ModeloComunicadoId*`
- `Nullable'1[Int32] MotivoInterrupcaoSLAId*`
- `Nullable'1[Int32] PapelDestinatarioId*`
- `Nullable'1[Int32] PapelResponsavelId*`
- `Nullable'1[Int32] SubProcessoId*`
- `Nullable'1[Int32] TempoIntervalo*`
- `Nullable'1[Int32] Temporalidade*`
- `Nullable'1[Int32] TipoSolicitacaoId*`
- `Object GetCustom(String propertyName)`
- `Object GetCustom(String propertyName, Object defaultValue)`
- `Object Item*`
- `String CicloSemanalDiaSemana*`
- `String Codigo*`
- `String Configuracao*`
- `String Descricao*`
- `String DisponibilidadeAplicacoes*`
- `String EmailRemetente*`
- `String EnderecoReply*`
- `String GrupoANO*`
- `String ListaDestinatarios*`
- `String NomeMensagem*`
- `String NomeRemetente*`
- `String Referencia*`
- `String ReferenciaContagemTempo*`
- `String Regra*`
- `String RotuloBotaoAvancar*`
- `String RotuloBotaoVoltar*`
- `String ScriptEvento*`
- `String ScriptFim*`
- `String ScriptFormCarregado*`
- `String ScriptInicio*`
- `String ScriptValidacao*`
- `String ScriptVolta*`
- `String Tipo*`
- `String TipoAberturaLinkInicial*`
- `String TipoCiclo*`
- `String TipoFinalizacao*`
- `String TipoMensagem*`
- `String ToString()`
- `String UnidadeANO*`
- `Supravizio.Configuracao.Custom.ClasseConfiguracao ClasseAnexoResposta*`
- `Supravizio.Processo.Atividade AtividadeInstance`
- `Supravizio.Processo.Custom.Associacao Associacao*`
- `Supravizio.Processo.Custom.Atividade Carrega(Int32 id)`
- `Supravizio.Processo.Custom.Atividade Load(Int32 id)`
- `Supravizio.Processo.Custom.CaixaMensagem CaixaEmail*`
- `Supravizio.Processo.Custom.ClassePesquisaSatisfacao ClassePesquisaSatisfacao*`
- `Supravizio.Processo.Custom.ClasseSubProcesso ClasseSubProcesso*`
- `Supravizio.Processo.Custom.ModeloComunicado ModeloComunicado*`
- `Supravizio.Processo.Custom.PapelProcesso PapelDestinatario*`
- `Supravizio.Processo.Custom.PapelProcesso PapelResponsavel*`
- `Supravizio.Processo.Custom.SubProcesso SubProcesso`
- `Supravizio.Processo.Custom.TipoSolicitacao TipoSolicitacao*`
- `Supravizio.Recurso.Custom.MotivoInterrupcaoSLA MotivoInterrupcaoSLA*`
- `Void SetCustom(String propertyName, Object value)`

### OrdemServico
`Venki.Supravizio.Processo.Custom.OrdemServico`

- `Boolean AtendeuANOAtividade(String codigoAtividade)`
- `Boolean AtendeuANOCorrente`
- `Boolean Equals(Object obj)`
- `Boolean IsNew`
- `Boolean LeituraResponsavel*`
- `Boolean Modified`
- `Boolean PermiteRetormarResponsabilidade*`
- `Boolean PossuiAprovacao(String codigoAtividade)`
- `Boolean PossuiArtefato()`
- `Boolean PossuiAssociacaoAlvo(String nomeAssociacao)`
- `Boolean PossuiAssociacaoFonte(String nomeAssociacao)`
- `Boolean PossuiAtividades(String codigoAtividade)`
- `Boolean PossuiDispositivoTelefonico()`
- `Boolean PossuiHardware()`
- `Boolean PossuiItem(String siglaClasseConfiguracao)`
- `Boolean PossuiSoftware()`
- `Boolean PublicaApontamentosAA*`
- `Boolean ReadOnly`
- `Boolean ReferenciaCircular*`
- `Boolean ValidaPendencias()`
- `Boolean ValidaPendenciasAprovacao(Int32 idAssuntoAprovacao, Int32 versao)`
- `Boolean ValidaPendenciasAtividadeExecucao()`
- `Collections.ArrayList ObtemConteudoArquivoTexto(Supravizio.Configuracao.Custom.ItemConfiguracao item)`
- `Core.Custom.SessionProxyList AcoesExecutadasEmAcordos`
- `Core.Custom.SessionProxyList Assuntos`
- `Core.Custom.SessionProxyList AtividadesExecutadas`
- `Core.Custom.SessionProxyList Atores`
- `Core.Custom.SessionProxyList CarregaLista(Object propertyName, Object value)`
- `Core.Custom.SessionProxyList Eventos`
- `Core.Custom.SessionProxyList Interrupcoes`
- `Core.Custom.SessionProxyList ItensAnexados`
- `Core.Custom.SessionProxyList ObtemAssociadasComoAlvo(String nomeAssociacao)`
- `Core.Custom.SessionProxyList ObtemAssociadasComoFonte(String nomeAssociacao)`
- `Core.Custom.SessionProxyList ObtemAtoresProcesso(String nome)`
- `Core.Custom.SessionProxyList ObtemDerivadas()`
- `Core.Custom.SessionProxyList ObtemDerivadas(Supravizio.Processo.Custom.ClasseSubProcesso classeSubProcesso)`
- `Core.Custom.SessionProxyList ObtemOrgaosImpactados()`
- `Core.Custom.SessionProxyList ObtemServicosImpactados()`
- `Core.Custom.SessionProxyList ObtemTodasAssociadas(Boolean recursivo)`
- `Core.Custom.SessionProxyList ObtemUsuariosImpactados()`
- `Core.Custom.SessionProxyList SLA`
- `Core.SessionObject Instance`
- `Data.DataRow AdicionaLinhaRegistro(String nomeCampo, IronPython.Runtime.List nomes, IronPython.Runtime.List valores)`
- `DateTime DataHoraCriacao*`
- `DateTime DataHoraResponsavel*`
- `DateTime DataHoraSolicitacao*`
- `DateTime DataHoraUltimaAtualizacao*`
- `Decimal ObtemHorasApontadas(DateTime dataInicio, DateTime dataFim, Boolean incluiDerivadas)`
- `Decimal ObtemHorasApontandatas(DateTime dataInicio, DateTime dataFim, Boolean incluiDerivadas)`
- `Int32 ClasseSubProcessoId*`
- `Int32 ClasseSubProcessoInicialId*`
- `Int32 ClienteId*`
- `Int32 ContaAssociacaoAlvo(String nomeAssociacao)`
- `Int32 ContaAssociacaoFonte(String nomeAssociacao)`
- `Int32 ContaExecucaoAtividade(String codigoAtividade)`
- `Int32 ContaExecucaoGateway(String codigoGateway)`
- `Int32 ContaExecucaoGateway(String codigoGateway, String textoAlternativa)`
- `Int32 DesenhoProcessoId*`
- `Int32 DesenhoProcessoInicialId*`
- `Int32 DomainId*`
- `Int32 FavorecidoId*`
- `Int32 GetHashCode()`
- `Int32 GrupoTrabalhoId*`
- `Int32 GrupoTrabalhoInicialId*`
- `Int32 Id`
- `Int32 ObtemMaiorValorFatorPrioridadeItensConfiguracao(Int32 valorDefault)`
- `Int32 ObtemMenorValorFatorPrioridadeItensConfiguracao(Int32 valorDefault)`
- `Int32 ObtemVariavelPrioridade(String nomeVariavel)`
- `Int32 OrgaoClienteId*`
- `Int32 ResponsavelId*`
- `Int32 ResponsavelInicialId*`
- `Int32 ServicoId*`
- `Int32 SubProcessoId*`
- `Nullable'1[Boolean] ExpirouTempoSLA*`
- `Nullable'1[DateTime] DataHoraExecucaoMudanca*`
- `Nullable'1[DateTime] DataHoraFimPlan*`
- `Nullable'1[DateTime] DataHoraFimPrevisto*`
- `Nullable'1[DateTime] DataHoraFimPrevistoOriginal*`
- `Nullable'1[DateTime] DataHoraFimReal*`
- `Nullable'1[DateTime] DataHoraInicioPlan*`
- `Nullable'1[DateTime] DataHoraInicioPrevisto*`
- `Nullable'1[DateTime] DataHoraInicioReal*`
- `Nullable'1[Decimal] ValorChargeBack*`
- `Nullable'1[Int32] AtividadeId*`
- `Nullable'1[Int32] CategoriaId*`
- `Nullable'1[Int32] ClassePesquisaSatisfacaoId*`
- `Nullable'1[Int32] ContratoId*`
- `Nullable'1[Int32] DiasAvisoReaberturaAgendamento*`
- `Nullable'1[Int32] EsforcoEstimado*`
- `Nullable'1[Int32] FinalizadorId*`
- `Nullable'1[Int32] GatewayId*`
- `Nullable'1[Int32] GrauPrioridadeCalculadoId*`
- `Nullable'1[Int32] GrauPrioridadeSelecionadoId*`
- `Nullable'1[Int32] ItemSLAId*`
- `Nullable'1[Int32] MetodoPriorizacaoId*`
- `Nullable'1[Int32] NivelSLAId*`
- `Nullable'1[Int32] OcorrenciaPaiId`
- `Nullable'1[Int32] OcorrenciaPrincipalId*`
- `Nullable'1[Int32] PesoPrioridadeCalculado*`
- `Nullable'1[Int32] PesoPrioridadeSelecionado*`
- `Nullable'1[Int32] SplitGatewayId*`
- `Nullable'1[Int32] TempoInterrupcaoSLA*`
- `Nullable'1[Int32] TempoSLA*`
- `Nullable'1[Int32] UsuarioAutenticadoId*`
- `Object GetCustom(String propertyName)`
- `Object GetCustom(String propertyName, Object defaultValue)`
- `Object Item*`
- `Object ObtemPropriedade(Int32 idClasseSubProcesso, String nomePropriedade, Object valorDefault)`
- `String Assunto*`
- `String Causa*`
- `String CelularCliente*`
- `String ClasseNegocio*`
- `String ComentarioContato*`
- `String ContatoResponsavelFornecedor*`
- `String DescricaoDetalhada*`
- `String EstadoFormulario*`
- `String HardwareAutoAtendimento*`
- `String IndicadorRespostaEmail*`
- `String Justificativa*`
- `String JustificativaEsforco*`
- `String MotivoCancelamento*`
- `String Numero*`
- `String NumeroReferenciaFornecedor*`
- `String NumeroSequencial`
- `String NumeroSistema`
- `String ObtemMotivoGateway(String codigoGateway)`
- `String ObtemMotivoReprovacao(String codigoAtividade)`
- `String Origem*`
- `String SegundoContato*`
- `String SintomaAnalisado*`
- `String Situacao*`
- `String SituacaoPesquisa*`
- `String Solucao*`
- `String TelefoneCliente*`
- `String TelefoneSegundoContato*`
- `String ToString()`
- `String UsuarioAutoAtendimento*`
- `String VariaveisPriorizacao*`
- `Supravizio.Configuracao.Custom.Artefato ObtemArtefato()`
- `Supravizio.Configuracao.Custom.Conhecimento ObtemConhecimento()`
- `Supravizio.Configuracao.Custom.DispositivoTelefonico ObtemDispositivoTelefonico()`
- `Supravizio.Configuracao.Custom.Hardware ObtemHardware()`
- `Supravizio.Configuracao.Custom.ItemConfiguracao ObtemItem(String siglaClasseConfiguracao)`
- `Supravizio.Configuracao.Custom.Software ObtemSoftware()`
- `Supravizio.Processo.Custom.Atividade Atividade*`
- `Supravizio.Processo.Custom.Categoria Categoria*`
- `Supravizio.Processo.Custom.ClassePesquisaSatisfacao ClassePesquisaSatisfacao*`
- `Supravizio.Processo.Custom.ClasseSubProcesso ClasseSubProcesso*`
- `Supravizio.Processo.Custom.ClasseSubProcesso ClasseSubProcessoInicial*`
- `Supravizio.Processo.Custom.DesenhoProcesso DesenhoProcesso*`
- `Supravizio.Processo.Custom.DesenhoProcesso DesenhoProcessoInicial*`
- `Supravizio.Processo.Custom.Gateway Gateway*`
- `Supravizio.Processo.Custom.Gateway SplitGateway*`
- `Supravizio.Processo.Custom.GrauPrioridade GrauPrioridadeCalculado*`
- `Supravizio.Processo.Custom.GrauPrioridade GrauPrioridadeSelecionado*`
- `Supravizio.Processo.Custom.InterrupcaoSLA NewInterrupcaoSLA(Supravizio.Processo.Custom.OrdemServico parentOrdemServico)`
- `Supravizio.Processo.Custom.MetodoPriorizacao MetodoPriorizacao*`
- `Supravizio.Processo.Custom.NivelSLA NivelSLA*`
- `Supravizio.Processo.Custom.Ocorrencia Agenda(DateTime dataInicio)`
- `Supravizio.Processo.Custom.Ocorrencia Agenda(DateTime dataInicio, Nullable'1[Int32] diasAvisoReabertura)`
- `Supravizio.Processo.Custom.Ocorrencia Cancela(String motivo)`
- `Supravizio.Processo.Custom.Ocorrencia Encaminha(Supravizio.Recurso.Custom.Tecnico novoTecnicoResponsavel, String explicaAtor)`
- `Supravizio.Processo.Custom.Ocorrencia Finaliza(String codigoAtividade, String causa, String solucao, DateTime dataHoraExecucaoMudanca)`
- `Supravizio.Processo.Custom.Ocorrencia IniciaAprovacao()`
- `Supravizio.Processo.Custom.Ocorrencia IniciaSubProcesso(Supravizio.Processo.Custom.Atividade atividade)`
- `Supravizio.Processo.Custom.Ocorrencia IniciaSubProcesso(Supravizio.Processo.Custom.Atividade atividade, String numero)`
- `Supravizio.Processo.Custom.Ocorrencia Nova(String siglaClasseSubProcesso, String codigoIniciador, String assunto, Supravizio.Processo.Custom.Servico servico, Supravizio.Recurso.Custom.Pessoa cliente, Supravizio.Recurso.Custom.Pessoa responsavel)`
- `Supravizio.Processo.Custom.Ocorrencia Nova(String siglaClasseSubProcesso, String codigoIniciador, String assunto, Supravizio.Processo.Custom.Servico servico, Supravizio.Recurso.Custom.Pessoa cliente, Supravizio.Recurso.Custom.Pessoa responsavel, Collections.Hashtable valoresCustomizados)`
- `Supravizio.Processo.Custom.Ocorrencia Nova(String siglaClasseSubProcesso, String codigoIniciador, String assunto, Supravizio.Processo.Custom.Servico servico, Supravizio.Recurso.Custom.Pessoa cliente, Supravizio.Recurso.Custom.Pessoa responsavel, Collections.Hashtable valoresCustomizados, String numero)`
- `Supravizio.Processo.Custom.Ocorrencia ObtemDerivada(Int32 idClasseSubProcesso)`
- `Supravizio.Processo.Custom.Ocorrencia ObtemPrincipal()`
- `Supravizio.Processo.Custom.Ocorrencia Pai*`
- `Supravizio.Processo.Custom.Ocorrencia Principal*`
- `Supravizio.Processo.Custom.Ocorrencia Reabre()`
- `Supravizio.Processo.Custom.Ocorrencia Reabre(Supravizio.Recurso.Custom.Pessoa autor)`
- `Supravizio.Processo.Custom.Ocorrencia VoltaAtividade()`
- `Supravizio.Processo.Custom.OrdemServico Carrega(Int32 id)`
- `Supravizio.Processo.Custom.OrdemServico Carrega(String propertyName, Object value)`
- `Supravizio.Processo.Custom.OrdemServico Load(Int32 id)`
- `Supravizio.Processo.Custom.OrdemServico Load(String propertyName, Object value)`
- `Supravizio.Processo.Custom.OrdemServico New()`
- `Supravizio.Processo.Custom.OrdemServico Novo()`
- `Supravizio.Processo.Custom.OrdemServico RefazANS()`
- `Supravizio.Processo.Custom.OrdemServico RegistraEntregaServico(Nullable'1[DateTime] dataHoraExecMudanca)`
- `Supravizio.Processo.Custom.SLAOrdemServico NewSLAOrdemServico(Supravizio.Processo.Custom.OrdemServico parentOrdemServico)`
- `Supravizio.Processo.Custom.Servico Servico*`
- `Supravizio.Processo.Custom.SubProcesso SubProcesso*`
- `Supravizio.Processo.Ocorrencia OcorrenciaInstance`
- `Supravizio.Processo.OrdemServico OrdemServicoInstance`
- `Supravizio.Recurso.Custom.Contrato Contrato*`
- `Supravizio.Recurso.Custom.GrupoTrabalho GrupoTrabalho*`
- `Supravizio.Recurso.Custom.GrupoTrabalho GrupoTrabalhoInicial*`
- `Supravizio.Recurso.Custom.ItemSLA ItemSLA*`
- `Supravizio.Recurso.Custom.Orgao OrgaoCliente*`
- `Supravizio.Recurso.Custom.Pessoa Cliente*`
- `Supravizio.Recurso.Custom.Pessoa Favorecido*`
- `Supravizio.Recurso.Custom.Pessoa Finalizador*`
- `Supravizio.Recurso.Custom.Pessoa Responsavel*`
- `Supravizio.Recurso.Custom.Pessoa ResponsavelInicial*`
- `Supravizio.Recurso.Custom.Pessoa UsuarioAutenticado*`
- `TimeSpan ObtemTempoLiquidoAtividade(String codigoAtividade)`
- `Void AdicionaComentario(String comentario, Boolean publicaNoAutoatendimento)`
- `Void AnexaArquivo(String nomeArquivo, String siglaTipoItem, Boolean apagarArquivoOriginal)`
- `Void AnexaExportacaoRelatorio(String nomeRelatorio, String siglaTipoItem, IronPython.Runtime.List nomesParametros, IronPython.Runtime.List valoresParametros, String formato)`
- `Void Aponta(String codigoClasseApontamento, String String1, String String2, Nullable'1[Int32] Inteiro1, Nullable'1[Int32] Inteiro2, Nullable'1[DateTime] DataHora1, Nullable'1[DateTime] DataHora2, Nullable'1[Decimal] Decimal1, Nullable'1[Decimal] Decimal2, Nullable'1[Boolean] Booleano1, Nullable'1[Boolean] Booleano2)`
- `Void Aprova(String codigoAtividade)`
- `Void Aprova(String codigoAtividade, String aprovador, String comentario)`
- `Void AssociaItemConfiguracao(Int32 idItem)`
- `Void AssociaOrdemServico(String numeroAssociadaAlvo, String siglaAssociacao)`
- `Void AvancaAtividade()`
- `Void CancelaAprovacao(String codigoAtividade)`
- `Void EnviaPesquisaSatisfacao(Supravizio.Processo.Custom.Atividade eventoFinal, Boolean forcaEnvio)`
- `Void GeraAvisoMural(String mensagem, Supravizio.Recurso.Custom.GrupoTrabalho grupoProprietario, IronPython.Runtime.List gruposPublicacao, Boolean incluirSubNiveis, Boolean visivelPortal, Nullable'1[DateTime] dataInicial, Nullable'1[DateTime]dataLimite, String mensagemPortal, Supravizio.Configuracao.Custom.Conhecimento artigo)`
- `Void ModificaCampoFormularioHabilitado(String nomeCampo, Boolean campoHabilitado)`
- `Void ModificaCampoFormularioMascara(String nomeCampo, String novaMascara, Boolean incluiLiteral)`
- `Void ModificaCampoFormularioVisivel(String nomeCampo, Boolean campoVisivel)`
- `Void RecalculaANOTempos()`
- `Void Reprova(String codigoAtividade, String motivo)`
- `Void Salva()`
- `Void Salva(Core.Custom.SessionObjectProxy proxy)`
- `Void SetCustom(String propertyName, Object value)`
