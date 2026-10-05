# ParentId

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > ParentId

Identificador da Modificação Pai. Este campo é preenchido para objetos que são Partes em associações do tipo Composition.

**Exemplo 1: modificação da propriedade ParentId**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade ParentId
changeLog.ParentId = 1;
# salva modificação da propriedade ParentId
ChangeLog.Salva(changeLog)
```
