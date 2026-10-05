# ErrorCount

Caminho: Customização > Modelo de objetos > Utilitários > Job > ErrorCount

Número de execuções seguindas com ocorrência de Erros. Se for excedido um número máximo de erros seguidos então o Job não é mais processado. Sempre que ocorrer execução com sucesso então este contador é zerado.

**Exemplo 1: modificação da propriedade ErrorCount**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade ErrorCount
job.ErrorCount = 1;
# salva modificação da propriedade ErrorCount
Job.Salva(job)
```
