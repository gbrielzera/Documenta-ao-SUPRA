# FatorPrioridade

Caminho: Customização > Modelo de objetos > Recurso > Empresa > FatorPrioridade

Fator utilizado para cálculo de Prioridade em Ocorrências.

**Exemplo 1: modificação da propriedade FatorPrioridade**

```
# carrega objeto Empresa de identificador 51
empresa = Empresa.Carrega(51)
# modifica a propriedade FatorPrioridade
empresa.FatorPrioridade = FatorPrioridade.Carrega(94);
# salva modificação da propriedade FatorPrioridade
Empresa.Salva(empresa)
```
