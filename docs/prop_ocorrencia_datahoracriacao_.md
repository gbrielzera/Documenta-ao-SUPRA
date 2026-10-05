# DataHoraCriacao

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraCriacao

Data e hora de criação da ocorrência. Esta data é preenchida automaticamente pelo sistema e não pode ser modificada pelo usuário.

**Exemplo 1: modificação da propriedade DataHoraCriacao**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraCriacao
ocorrencia.DataHoraCriacao = DateTime;
# salva modificação da propriedade DataHoraCriacao
Ocorrencia.Salva(ocorrencia)
```
