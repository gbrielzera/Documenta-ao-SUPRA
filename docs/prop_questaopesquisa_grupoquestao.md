# GrupoQuestao

Caminho: Customização > Modelo de objetos > Processo > QuestaoPesquisa > GrupoQuestao

Grupo associado com a Questão

**Exemplo 1: modificação da propriedade GrupoQuestao**

```
# carrega objeto QuestaoPesquisa de identificador 78
questaoPesquisa = QuestaoPesquisa.Carrega(78)
# modifica a propriedade GrupoQuestao
questaoPesquisa.GrupoQuestao = GrupoQuestao.Carrega(23);
# salva modificação da propriedade GrupoQuestao
QuestaoPesquisa.Salva(questaoPesquisa)
```
