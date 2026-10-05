# FatorPrioridadeId

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > FatorPrioridadeId

Identificador do(a) FatorPrioridade associado(a)

**Exemplo 1: modificação da propriedade FatorPrioridadeId**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade FatorPrioridadeId
classeSubProcesso.FatorPrioridadeId = 1;
# salva modificação da propriedade FatorPrioridadeId
ClasseSubProcesso.Salva(classeSubProcesso)
```
