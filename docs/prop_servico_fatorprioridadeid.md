# FatorPrioridadeId

Caminho: Customização > Modelo de objetos > Processo > Servico > FatorPrioridadeId

Identificador do(a) FatorPrioridade associado(a)

**Exemplo 1: modificação da propriedade FatorPrioridadeId**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade FatorPrioridadeId
servico.FatorPrioridadeId = 1;
# salva modificação da propriedade FatorPrioridadeId
Servico.Salva(servico)
```
