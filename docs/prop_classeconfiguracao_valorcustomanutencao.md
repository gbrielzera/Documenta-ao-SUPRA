# ValorCustoManutencao

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > ValorCustoManutencao

Valor do Custo de Manutenção Mensal Padrão para Itens da Classe. Este valor pode ser redefinido com o campo correspondente no Item.

**Exemplo 1: modificação da propriedade ValorCustoManutencao**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade ValorCustoManutencao
classeConfiguracao.ValorCustoManutencao = 0;
# salva modificação da propriedade ValorCustoManutencao
ClasseConfiguracao.Salva(classeConfiguracao)
```
