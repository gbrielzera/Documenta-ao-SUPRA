# MetodoPriorizacaoId

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > MetodoPriorizacaoId

Identificador do MetodoPriorizacao associado

**Exemplo 1: modificação da propriedade MetodoPriorizacaoId**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade MetodoPriorizacaoId
classeSubProcesso.MetodoPriorizacaoId = 1;
# salva modificação da propriedade MetodoPriorizacaoId
ClasseSubProcesso.Salva(classeSubProcesso)
```
