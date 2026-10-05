# DesenhoProcessoId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DesenhoProcessoId

Identificador da versão de Processo da Ocorrência.

**Exemplo 1: modificação da propriedade DesenhoProcessoId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DesenhoProcessoId
ocorrencia.DesenhoProcessoId = 1;
# salva modificação da propriedade DesenhoProcessoId
Ocorrencia.Salva(ocorrencia)
```
