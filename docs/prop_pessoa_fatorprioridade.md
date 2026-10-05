# FatorPrioridade

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > FatorPrioridade

Fator utilizado para cálculo de Prioridade em Ocorrências.

**Exemplo 1: modificação da propriedade FatorPrioridade**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade FatorPrioridade
pessoa.FatorPrioridade = FatorPrioridade.Carrega(94);
# salva modificação da propriedade FatorPrioridade
Pessoa.Salva(pessoa)
```
