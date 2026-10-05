# Id

Caminho: Customização > Modelo de objetos > Processo > GrupoQuestao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Grupo de Questões

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto GrupoQuestao de identificador 1
grupoQuestao = GrupoQuestao.Carrega(1)
# modifica a propriedade Id
grupoQuestao.Id = 1;
# salva modificação da propriedade Id
GrupoQuestao.Salva(grupoQuestao)
```
