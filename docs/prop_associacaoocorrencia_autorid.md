# AutorId

Caminho: Customização > Modelo de objetos > Processo > AssociacaoOcorrencia > AutorId

Identificador da Pessoa que estabeleceu a Associação.

**Exemplo 1: modificação da propriedade AutorId**

```
# carrega objeto AssociacaoOcorrencia de identificador 1
associacaoOcorrencia = AssociacaoOcorrencia.Carrega(1)
# modifica a propriedade AutorId
associacaoOcorrencia.AutorId = 1;
# salva modificação da propriedade AutorId
AssociacaoOcorrencia.Salva(associacaoOcorrencia)
```
