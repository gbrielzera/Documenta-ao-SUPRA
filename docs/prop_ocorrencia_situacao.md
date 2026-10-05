# Situacao

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Situacao

Situação da ocorrência.

**Exemplo 1: modificação da propriedade Situacao**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade Situacao
ocorrencia.Situacao = "Aberto";
# salva modificação da propriedade Situacao
Ocorrencia.Salva(ocorrencia)
```
