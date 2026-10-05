# Fonte

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > Fonte

Ocorrência Fonte da Associação.

**Exemplo 1: modificação da propriedade Fonte**

```
# carrega objeto AssociacaoOcorrencia de identificador 78
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(78)
# modifica a propriedade Fonte
associacaoOcorrencia.Fonte = Ocorrencia.Carrega(23);
# salva modificação da propriedade Fonte
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
