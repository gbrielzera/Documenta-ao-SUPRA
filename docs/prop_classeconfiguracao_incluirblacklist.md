# IncluirBlackList

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > IncluirBlackList

Indica que itens deste tipo fazem parte de um blacklist

**Exemplo 1: modificação da propriedade IncluirBlackList**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade IncluirBlackList
classeConfiguracao.IncluirBlackList = true;
# salva modificação da propriedade IncluirBlackList
ClasseConfiguracao.Salva(classeConfiguracao)
```
