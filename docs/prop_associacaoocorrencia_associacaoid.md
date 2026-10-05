# AssociacaoId

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > AssociacaoId

Identificador do Associacao associado

**Exemplo 1: modificação da propriedade AssociacaoId**

```
# carrega objeto AssociacaoOcorrencia de identificador 1
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(1)
# modifica a propriedade AssociacaoId
associacaoOcorrencia.AssociacaoId = 1;
# salva modificação da propriedade AssociacaoId
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
