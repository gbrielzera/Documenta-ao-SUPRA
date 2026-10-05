# SubProcessoId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > SubProcessoId

Identificador do SubProcesso corrente da ocorrência. Esta informação pode ser obtida também pelo relacionamento da entidade Atividade e está aqui por questão de desempenho da aplicação.

**Exemplo 1: modificação da propriedade SubProcessoId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade SubProcessoId
ocorrencia.SubProcessoId = 1;
# salva modificação da propriedade SubProcessoId
Ocorrencia.Salva(ocorrencia)
```
