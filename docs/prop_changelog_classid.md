# ClassId

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > ClassId

Identificador da Classe do Objeto modificado.

**Exemplo 1: modificação da propriedade ClassId**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade ClassId
changeLog.ClassId = 1;
# salva modificação da propriedade ClassId
ChangeLog.Salva(changeLog)
```
