# EmailSuccess

Caminho: Customização > Modelo de objetos > Utilitários > Job > EmailSuccess

Email enviado para usuário em caso de sucesso

**Exemplo 1: modificação da propriedade EmailSuccess**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade EmailSuccess
job.EmailSuccess = "Email sucesso";
# salva modificação da propriedade EmailSuccess
Job.Salva(job)
```
