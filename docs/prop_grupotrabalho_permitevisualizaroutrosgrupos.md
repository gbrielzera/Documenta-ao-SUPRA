# PermiteVisualizarOutrosGrupos

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > PermiteVisualizarOutrosGrupos

Permite visualizar outros Grupos de Trabalho na árvore de Grupos de Trabalho. Caso esta propriedade seja desmarcada o solucionador deste grupo poderá visualizar apenas o seu grupo de trabalho e sub-grupos.

**Exemplo 1: modificação da propriedade PermiteVisualizarOutrosGrupos**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade PermiteVisualizarOutrosGrupos
grupoTrabalho.PermiteVisualizarOutrosGrupos = true;
# salva modificação da propriedade PermiteVisualizarOutrosGrupos
GrupoTrabalho.Salva(grupoTrabalho)
```
