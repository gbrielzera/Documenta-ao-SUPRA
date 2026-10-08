# CriticaValidacaoList (API de script)
Caminho: Catálogo > API de scripts > Venki.Supravizio.Processo > CriticaValidacaoList

class `Venki.Supravizio.Processo.CriticaValidacaoList` — supravizio.dll v18.1.1.0

## Propriedades (3)
- ArrayList Itens {get;}
- bool PossuiPendencia {get;}
- bool PossuiAviso {get;}

## Métodos (15)
- void AdicionaPendencia(string mensagem, string grupo, NomeCampo? campo, string campoAssociado)
- void AdicionaPendencia(string mensagem, string grupo, string campoAssociado)
- void AdicionaPendencia(CriticaValidacao criticaOrigem)
- void AdicionaPendencia(string mensagem, string grupo)
- void AdicionaPendencia(string mensagem)
- void AdicionaAviso(string mensagem, string grupo, NomeCampo? campo, string campoAssociado)
- void AdicionaAviso(string mensagem, string grupo, string campoAssociado)
- void AdicionaAviso(CriticaValidacao criticaOrigem)
- void AdicionaAviso(string mensagem, string grupo)
- void AdicionaAviso(string mensagem)
- void AdicionaInformacao(string mensagem, string grupo, NomeCampo? campo, string campoAssociado)
- void AdicionaInformacao(CriticaValidacao criticaOrigem)
- void AdicionaInformacao(string mensagem, string grupo, string campoAssociado)
- void AdicionaInformacao(string mensagem, string grupo)
- void AdicionaInformacao(string mensagem)
