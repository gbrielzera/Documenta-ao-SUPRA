# AtividadeGeradoraId

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > AtividadeGeradoraId

Identificador da Atividade do tipo Subprocesso ou Link final que gerou a associação.

**Exemplo 1: modificação da propriedade AtividadeGeradoraId**

```
# carrega objeto AssociacaoOcorrencia de identificador 1
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(1)
# modifica a propriedade AtividadeGeradoraId
associacaoOcorrencia.AtividadeGeradoraId = 1;
# salva modificação da propriedade AtividadeGeradoraId
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
