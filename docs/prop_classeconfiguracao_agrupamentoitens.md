# AgrupamentoItens

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > AgrupamentoItens

Define a forma como itens de charge-back apurado são agrupados no relatório apresentado para gestores de áreas clientes.

**Exemplo 1: modificação da propriedade AgrupamentoItens**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade AgrupamentoItens
classeConfiguracao.AgrupamentoItens = "PorClasseConfiguracao";
# salva modificação da propriedade AgrupamentoItens
ClasseConfiguracao.Salva(classeConfiguracao)
```
