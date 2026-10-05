# Alvo

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > Alvo

Ocorrência Alvo da Ocorrência.

**Exemplo 1: modificação da propriedade Alvo**

```
# carrega objeto AssociacaoOcorrencia de identificador 78
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(78)
# modifica a propriedade Alvo
associacaoOcorrencia.Alvo = Ocorrencia.Carrega(23);
# salva modificação da propriedade Alvo
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
