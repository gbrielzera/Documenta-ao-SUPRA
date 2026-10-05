# FatorPrioridade

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > FatorPrioridade

Fator utilizado para cálculo de Prioridade em Ocorrências.

**Exemplo 1: modificação da propriedade FatorPrioridade**

```
# carrega objeto ClasseConfiguracao de identificador 73
classeConfiguracao = ClasseConfiguracao.Carrega(73)
# modifica a propriedade FatorPrioridade
classeConfiguracao.FatorPrioridade = FatorPrioridade.Carrega(91);
# salva modificação da propriedade FatorPrioridade
ClasseConfiguracao.Salva(classeConfiguracao)
```
