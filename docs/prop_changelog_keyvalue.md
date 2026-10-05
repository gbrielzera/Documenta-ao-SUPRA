# KeyValue

Caminho: Customização > Modelo de objetos > Utilitários > ChangeLog > KeyValue

Chave de identificação do Objeto de Negócio modificado.

**Exemplo 1: modificação da propriedade KeyValue**

```
# carrega objeto ChangeLog de identificador 1
changeLog = ChangeLog.Carrega(1)
# modifica a propriedade KeyValue
changeLog.KeyValue = "Chave";
# salva modificação da propriedade KeyValue
ChangeLog.Salva(changeLog)
```
