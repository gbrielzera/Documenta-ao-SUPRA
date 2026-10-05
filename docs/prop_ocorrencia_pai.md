# Pai

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Pai

Ocorrência pai

**Exemplo 1: modificação da propriedade Pai**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade Pai
ocorrencia.Pai = Ocorrencia.Carrega(23);
# salva modificação da propriedade Pai
Ocorrencia.Salva(ocorrencia)
```
