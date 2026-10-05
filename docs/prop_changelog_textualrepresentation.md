# TextualRepresentation

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > TextualRepresentation

Representação textual do registro modificado

**Exemplo 1: modificação da propriedade TextualRepresentation**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade TextualRepresentation
changeLog.TextualRepresentation = "Representação textual";
# salva modificação da propriedade TextualRepresentation
ChangeLog.Salva(changeLog)
```
