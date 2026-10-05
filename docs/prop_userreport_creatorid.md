# CreatorId

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > CreatorId

Identificador do usuário criador do relatório

**Exemplo 1: modificação da propriedade CreatorId**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade CreatorId
userReport.CreatorId = 1;
# salva modificação da propriedade CreatorId
UserReport.Salva(userReport)
```
