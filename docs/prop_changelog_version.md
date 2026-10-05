# Version

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > Version

Número de Versão para o registro.

**Exemplo 1: modificação da propriedade Version**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade Version
changeLog.Version = 1;
# salva modificação da propriedade Version
ChangeLog.Salva(changeLog)
```
