# FatorPrioridadeId

Caminho: Customização > Modelo de objetos > Processo > ClasseServico > FatorPrioridadeId

Identificador do Fator de Prioridade utilizado para priorizar uma ocorrência. Deve ser utilizado em conjunto com um Método de Priorização.

**Exemplo 1: modificação da propriedade FatorPrioridadeId**

```
# carrega objeto ClasseServico de identificador 1
classeServico = ClasseServico.Carrega(1)
# modifica a propriedade FatorPrioridadeId
classeServico.FatorPrioridadeId = 1;
# salva modificação da propriedade FatorPrioridadeId
ClasseServico.Salva(classeServico)
```
