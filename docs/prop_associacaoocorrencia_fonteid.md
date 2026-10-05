# FonteId

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > FonteId

Identificador da Ocorrência Fonte da Associação.

**Exemplo 1: modificação da propriedade FonteId**

```
# carrega objeto AssociacaoOcorrencia de identificador 1
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(1)
# modifica a propriedade FonteId
associacaoOcorrencia.FonteId = 1;
# salva modificação da propriedade FonteId
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
