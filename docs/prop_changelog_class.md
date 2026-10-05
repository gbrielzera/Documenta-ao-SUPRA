# Class

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > Class

Classe do Objeto modificado

**Exemplo 1: modificação da propriedade Class**

```
# carrega objeto ChangeLog de identificador 94
changeLog = ChangeLog.Carrega(94)
# modifica a propriedade Class
changeLog.Class = Class.Carrega(57);
# salva modificação da propriedade Class
ChangeLog.Salva(changeLog)
```
