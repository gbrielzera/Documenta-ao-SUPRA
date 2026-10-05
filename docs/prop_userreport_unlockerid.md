# UnlockerId

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > UnlockerId

Identificador do usuário responsável pelo último do relatório.

**Exemplo 1: modificação da propriedade UnlockerId**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade UnlockerId
userReport.UnlockerId = 1;
# salva modificação da propriedade UnlockerId
UserReport.Salva(userReport)
```
