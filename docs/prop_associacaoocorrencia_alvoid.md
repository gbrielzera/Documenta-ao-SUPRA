# AlvoId

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > AlvoId

Identificador da Ocorrência Alvo na Associação.

**Exemplo 1: modificação da propriedade AlvoId**

```
# carrega objeto AssociacaoOcorrencia de identificador 1
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(1)
# modifica a propriedade AlvoId
associacaoOcorrencia.AlvoId = 1;
# salva modificação da propriedade AlvoId
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
