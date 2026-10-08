# ChargeBack (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Recurso.Custom > ChargeBack

class `Venki.Supravizio.Recurso.Custom.ChargeBack` — supravizio.custom.dll v18.1.1.0
Herda de **SessionObjectProxy** (ver catalogo/api/SessionObjectProxy.md): os membros da classe base também valem aqui.
Descrição de cada propriedade: docs/objetos_chargeback.md

## Propriedades (9)
- ChargeBack ChargeBackInstance {get;}
- int Ano {get;set;}
- int Mes {get;set;}
- int DomainId {get;set;}
- int Id {get;set;}
- DateTime DataHoraProcessamento {get;set;}
- bool Publicado {get;set;}
- SessionProxyList Areas {get;}
- SessionProxyList HistoricoOrgao {get;}

## Métodos (13)
- static ChargeBack Load(int id)
- static ChargeBack Carrega(int id)
- static ChargeBack New()
- static ChargeBack Novo()
- static ChargeBackOrgao NewChargeBackOrgao(ChargeBack parentChargeBack)
- static ItemChargeBack NewItemChargeBack(ChargeBackOrgao parentChargeBackOrgao)
- static HistoricoOrgao NewHistoricoOrgao(ChargeBack parentChargeBack)
- static HistoricoPessoa NewHistoricoPessoa(HistoricoOrgao parentHistoricoOrgao)
- static ChargeBack Load(string propertyName, object value)
- static ChargeBack Carrega(string propertyName, object value)
- static SessionProxyList CarregaLista(object propertyName, object value)
- static void Salva(SessionObjectProxy proxy)
- void Salva()
