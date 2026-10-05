# Principal

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Principal

Ocorrências de Processos

**Exemplo 1: modificação da propriedade Principal**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade Principal
ocorrencia.Principal = Ocorrencia.Carrega(23);
# salva modificação da propriedade Principal
Ocorrencia.Salva(ocorrencia)
```
