# Id

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > Id

Identificador da Modificação

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade Id
changeLog.Id = 0;
# salva modificação da propriedade Id
ChangeLog.Salva(changeLog)
```
