# MetodoPriorizacao

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > MetodoPriorizacao

Método utilizado para Priorizar Ocorrências do Subprocesso.

**Exemplo 1: modificação da propriedade MetodoPriorizacao**

```
# carrega objeto ClasseSubProcesso de identificador 78
classeSubProcesso = ClasseSubProcesso.Carrega(78)
# modifica a propriedade MetodoPriorizacao
classeSubProcesso.MetodoPriorizacao = MetodoPriorizacao.Carrega(23);
# salva modificação da propriedade MetodoPriorizacao
ClasseSubProcesso.Salva(classeSubProcesso)
```
