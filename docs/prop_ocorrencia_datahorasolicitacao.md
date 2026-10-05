# DataHoraSolicitacao

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraSolicitacao

Data e hora de solicitação da ocorrência. Esta data é preenchida automaticamente pelo sistema usando a Data/hora corrente e pode ser modificada pelo usuário (se este possui autorização para modificação de dados).

**Exemplo 1: modificação da propriedade DataHoraSolicitacao**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraSolicitacao
ocorrencia.DataHoraSolicitacao = DateTime;
# salva modificação da propriedade DataHoraSolicitacao
Ocorrencia.Salva(ocorrencia)
```
