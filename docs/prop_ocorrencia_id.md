# Id

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade Id
ocorrencia.Id = 1;
# salva modificação da propriedade Id
Ocorrencia.Salva(ocorrencia)
```
