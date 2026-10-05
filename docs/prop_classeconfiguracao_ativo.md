# Ativo

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > Ativo

Indica que o Tipo de Item de Configuração está ativo no sistema.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade Ativo
classeConfiguracao.Ativo = true;
# salva modificação da propriedade Ativo
ClasseConfiguracao.Salva(classeConfiguracao)
```
