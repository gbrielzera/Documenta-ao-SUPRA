# OcorrenciaId

Caminho: Customização > Modelo de objetos > Processo > TesteControle > OcorrenciaId

Identificador da Ocorrencia associada

**Exemplo 1: modificação da propriedade OcorrenciaId**

```
# carrega objeto TesteControle de identificador 1
testeControle = TesteControle.Carrega(1)
# modifica a propriedade OcorrenciaId
testeControle.OcorrenciaId = 1;
# salva modificação da propriedade OcorrenciaId
TesteControle.Salva(testeControle)
```
