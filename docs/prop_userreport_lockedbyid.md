# LockedById

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > LockedById

Identificador do usuário que bloqueou o relatório para edição. Usuário que bloqueou o relatório para edição. Durante a existência do bloqueio somente este usuário pode realizar modificações. O desbloqueio pode ser desfeito pelo criador do relatório, autor do bloqueio ou qualquer outro que possua o perfil 'Admin'.

**Exemplo 1: modificação da propriedade LockedById**

```
# carrega objeto UserReport de identificador 1
userReport = UserReport.Carrega(1)
# modifica a propriedade LockedById
userReport.LockedById = 1;
# salva modificação da propriedade LockedById
UserReport.Salva(userReport)
```
