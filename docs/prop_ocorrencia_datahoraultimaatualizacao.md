# DataHoraUltimaAtualizacao

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > DataHoraUltimaAtualizacao

Data e hora da última atualização

**Exemplo 1: modificação da propriedade DataHoraUltimaAtualizacao**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade DataHoraUltimaAtualizacao
ocorrencia.DataHoraUltimaAtualizacao = DateTime;
# salva modificação da propriedade DataHoraUltimaAtualizacao
Ocorrencia.Salva(ocorrencia)
```
