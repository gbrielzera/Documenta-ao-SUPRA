# DateTime

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > DateTime

Data e hora da modificação

**Exemplo 1: modificação da propriedade DateTime**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade DateTime
changeLog.DateTime = DateTime;
# salva modificação da propriedade DateTime
ChangeLog.Salva(changeLog)
```
