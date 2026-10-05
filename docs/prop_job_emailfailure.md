# EmailFailure

Caminho: Customização > Modelo de objetos > Utilitários > Job > EmailFailure

Email enviado a usuários em caso de falha na execução

**Exemplo 1: modificação da propriedade EmailFailure**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade EmailFailure
job.EmailFailure = "Email falha";
# salva modificação da propriedade EmailFailure
Job.Salva(job)
```
