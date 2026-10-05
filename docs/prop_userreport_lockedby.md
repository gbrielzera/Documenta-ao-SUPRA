# LockedBy

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > LockedBy

Usuário que bloqueou o relatório para edição. Durante a existência do bloqueio somente este usuário pode realizar modificações. O desbloqueio pode ser desfeito pelo criador do relatório, autor do bloqueio ou qualquer outro que possua o perfil 'Admin'

**Exemplo 1: modificação da propriedade LockedBy**

```
# carrega objeto UserReport de identificador 94
userReport = UserReport.Carrega(94)
# modifica a propriedade LockedBy
userReport.LockedBy = User.Carrega(57);
# salva modificação da propriedade LockedBy
UserReport.Salva(userReport)
```
