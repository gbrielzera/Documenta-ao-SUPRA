# Id

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Método de Priorização de Ocorrências.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto MetodoPriorizacao de identificador 1
metodoPriorizacao = MetodoPriorizacao.Carrega(1)
# modifica a propriedade Id
metodoPriorizacao.Id = 1;
# salva modificação da propriedade Id
MetodoPriorizacao.Salva(metodoPriorizacao)
```
