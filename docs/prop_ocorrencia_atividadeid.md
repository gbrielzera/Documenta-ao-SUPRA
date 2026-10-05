# AtividadeId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > AtividadeId

Identificador da Atividade corrente da Ocorrência.

**Exemplo 1: modificação da propriedade AtividadeId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade AtividadeId
ocorrencia.AtividadeId = 1;
# salva modificação da propriedade AtividadeId
Ocorrencia.Salva(ocorrencia)
```
