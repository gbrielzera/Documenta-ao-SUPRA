# Name

Caminho: Customização > Modelo de objetos > Utilitários > Job > Name

Nome do job que é exibido na transação Gerenciamento de Ambiente

**Exemplo 1: modificação da propriedade Name**

```
# carrega objeto Job de identificador 1
job = Job.Carrega(1)
# modifica a propriedade Name
job.Name = "Name";
# salva modificação da propriedade Name
Job.Salva(job)
```
