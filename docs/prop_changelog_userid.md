# UserId

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > UserId

Identificador do Usuário que realizou a modificação.

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade UserId
changeLog.UserId = 1;
# salva modificação da propriedade UserId
ChangeLog.Salva(changeLog)
```
