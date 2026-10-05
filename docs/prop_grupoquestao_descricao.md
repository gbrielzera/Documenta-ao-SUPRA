# Descricao

Caminho: Customização > Modelo de objetos > Processo > GrupoQuestao > Descricao

Descrição detalhada do Grupo de Questões

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto GrupoQuestao de identificador 1
grupoQuestao = GrupoQuestao.Carrega(1)
# modifica a propriedade Descricao
grupoQuestao.Descricao = "Descrição";
# salva modificação da propriedade Descricao
GrupoQuestao.Salva(grupoQuestao)
```
