# Job (API de script)
Caminho: Catálogo > API de scripts > Venki.Services.Custom > Job

class `Venki.Services.Custom.Job` — services.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_job.md

## Propriedades (30)
- Job JobInstance {get;}
- int Id {get;set;}
- string Description {get;set;}
- int ClassId {get;set;}
- DateTime? NextTime {get;set;}
- DateTime? LastTime {get;set;}
- bool Enabled {get;set;}
- int DomainId {get;set;}
- int? UserId {get;set;}
- string ProcessParam {get;set;}
- DateTime CreatedDate {get;set;}
- string ContextApplicationId {get;set;}
- int ContextDomainId {get;set;}
- string ContextUsername {get;set;}
- int ContextUserId {get;set;}
- int NextTimePeriod {get;set;}
- int NextTimePeriodCount {get;set;}
- string EmailSuccess {get;set;}
- string EmailFailure {get;set;}
- DateTime? LastRunningDate {get;set;}
- int? RunningProgress {get;set;}
- string RunningResult {get;set;}
- string RunningServer {get;set;}
- int ErrorCount {get;set;}
- string Name {get;set;}
- int Async {get;set;}
- string ReportExportFormat {get;set;}
- SessionProxyList JobHistory {get;}
- Class ProcessClass {get;set;}
- User Creator {get;set;}

## Métodos (10)
- static Job Load(int id)
- static Job Carrega(int id)
- static Job New()
- static Job Novo()
- static JobHistory NewJobHistory(Job parentJob)
- static Job Load(string propertyName, object value)
- static Job Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
