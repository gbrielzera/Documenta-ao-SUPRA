# GrupoTrabalhoPai

Caminho: Customização > Modelo de objetos > Recurso > GrupoTrabalho > GrupoTrabalhoPai

Grupo de Trabalho que é o Ancestral na hierarquia. A hierarquia de Grupos de Trabalho não corresponde necessariamente a Estrutura Organizacional da Empresa.

**Exemplo 1: modificação da propriedade GrupoTrabalhoPai**

```
# carrega objeto GrupoTrabalho de identificador 51
grupoTrabalho = GrupoTrabalho.Carrega(51)
# modifica a propriedade GrupoTrabalhoPai
grupoTrabalho.GrupoTrabalhoPai = GrupoTrabalho.Carrega(94);
# salva modificação da propriedade GrupoTrabalhoPai
GrupoTrabalho.Salva(grupoTrabalho)
```
