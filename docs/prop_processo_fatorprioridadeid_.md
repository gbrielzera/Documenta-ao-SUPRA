# FatorPrioridadeId

Caminho: Customização > Modelo de objetos > Processo > Processo > FatorPrioridadeId

Identificador do(a) FatorPrioridade associado(a)

**Exemplo 1: modificação da propriedade FatorPrioridadeId**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade FatorPrioridadeId
processo.FatorPrioridadeId = 1;
# salva modificação da propriedade FatorPrioridadeId
Processo.Salva(processo)
```
