# ExibeAlertaOSGrupo

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > ExibeAlertaOSGrupo

Regra de autorização para exibição de Ordens de Serviço no Painel de Alertas do Workspace.

**Exemplo 1: modificação da propriedade ExibeAlertaOSGrupo**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade ExibeAlertaOSGrupo
grupoTrabalho.ExibeAlertaOSGrupo = "TodosGrupos";
# salva modificação da propriedade ExibeAlertaOSGrupo
GrupoTrabalho.Salva(grupoTrabalho)
```
