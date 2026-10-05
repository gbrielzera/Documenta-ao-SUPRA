# DesenhoProcessoInicialId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DesenhoProcessoInicialId

Identificador da Versão de Processo inicialmente atribuída a Ocorrência.

**Exemplo 1: modificação da propriedade DesenhoProcessoInicialId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DesenhoProcessoInicialId
ocorrencia.DesenhoProcessoInicialId = 1;
# salva modificação da propriedade DesenhoProcessoInicialId
Ocorrencia.Salva(ocorrencia)
```
