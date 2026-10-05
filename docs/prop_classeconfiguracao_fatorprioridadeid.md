# FatorPrioridadeId

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > FatorPrioridadeId

Identificador do(a) FatorPrioridade associado(a)

**Exemplo 1: modificação da propriedade FatorPrioridadeId**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade FatorPrioridadeId
classeConfiguracao.FatorPrioridadeId = 1;
# salva modificação da propriedade FatorPrioridadeId
ClasseConfiguracao.Salva(classeConfiguracao)
```
