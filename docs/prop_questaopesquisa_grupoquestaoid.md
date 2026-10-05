# GrupoQuestaoId

Caminho: Customização > Modelo de objetos > Processo > QuestaoPesquisa > GrupoQuestaoId

Identificador do GrupoQuestao associado

**Exemplo 1: modificação da propriedade GrupoQuestaoId**

```
# carrega objeto QuestaoPesquisa de identificador 1
questaoPesquisa = QuestaoPesquisa.Carrega(1)
# modifica a propriedade GrupoQuestaoId
questaoPesquisa.GrupoQuestaoId = 1;
# salva modificação da propriedade GrupoQuestaoId
QuestaoPesquisa.Salva(questaoPesquisa)
```
