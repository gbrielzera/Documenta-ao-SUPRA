# Unlocker

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > Unlocker

Pessoa que realizou o desbloqueio na edição do relatório. Somente o criador do relatório, o responsável pelo bloqueio e usuários com o perfil 'Admin' estão autorizados a desbloquear o relatório.

**Exemplo 1: modificação da propriedade Unlocker**

```
# carrega objeto UserReport de identificador 94
userReport = UserReport.Carrega(94)
# modifica a propriedade Unlocker
userReport.Unlocker = User.Carrega(57);
# salva modificação da propriedade Unlocker
UserReport.Salva(userReport)
```
