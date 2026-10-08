# Ausencia (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > Ausencia

class `Venki.Supravizio.Recurso.Custom.Ausencia` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_ausencia.md

## Propriedades (12)
- Ausencia AusenciaInstance {get;}
- string Motivo {get;set;}
- DateTime DataHoraInicio {get;set;}
- DateTime DataHoraPrevisaoRetorno {get;set;}
- DateTime DataHoraRegistro {get;set;}
- int Id {get;set;}
- int SubstitutoId {get;set;}
- int PessoaId {get;set;}
- bool PermiteSubstitutoModificar {get;set;}
- bool EncaminharSubstituto {get;set;}
- Pessoa Pessoa {get;set;}
- Pessoa Substituto {get;set;}

## Métodos (9)
- static Ausencia Load(int id)
- static Ausencia Carrega(int id)
- static Ausencia New()
- static Ausencia Novo()
- static Ausencia Load(string propertyName, object value)
- static Ausencia Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
