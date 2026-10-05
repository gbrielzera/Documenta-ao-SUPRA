# GrupoTrabalhoPaiId

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > GrupoTrabalhoPaiId

Identificador do Grupo de Trabalho Pai. Esta associação permite a criação de uma hierarquia de Grupos de Trabalho.

**Exemplo 1: modificação da propriedade GrupoTrabalhoPaiId**

```
# carrega objeto GrupoTrabalho de identificador 1
grupoTrabalho = GrupoTrabalho.Carrega(1)
# modifica a propriedade GrupoTrabalhoPaiId
grupoTrabalho.GrupoTrabalhoPaiId = 1;
# salva modificação da propriedade GrupoTrabalhoPaiId
GrupoTrabalho.Salva(grupoTrabalho)
```
