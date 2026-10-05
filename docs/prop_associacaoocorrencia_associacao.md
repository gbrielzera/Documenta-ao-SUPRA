# Associacao

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > Associacao

Definição da Associação

**Exemplo 1: modificação da propriedade Associacao**

```
# carrega objeto AssociacaoOcorrencia de identificador 78
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(78)
# modifica a propriedade Associacao
associacaoOcorrencia.Associacao = Associacao.Carrega(23);
# salva modificação da propriedade Associacao
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
