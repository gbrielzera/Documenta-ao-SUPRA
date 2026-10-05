# LockComment

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > LockComment

Comentário registrado pelo usuário que realizou ou cancelou o bloqueio de edição

**Exemplo 1: modificação da propriedade LockComment**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade LockComment
userReport.LockComment = "Comentário de bloqueio";
# salva modificação da propriedade LockComment
UserReport.Salva(userReport)
```
