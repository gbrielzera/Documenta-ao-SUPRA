# DataHoraAssociacao

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > DataHoraAssociacao

Data e hora em que foi estabelecida a Associação.

**Exemplo 1: modificação da propriedade DataHoraAssociacao**

```
# carrega objeto AssociacaoOcorrencia de identificador 1
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(1)
# modifica a propriedade DataHoraAssociacao
associacaoOcorrencia.DataHoraAssociacao = DateTime;
# salva modificação da propriedade DataHoraAssociacao
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
