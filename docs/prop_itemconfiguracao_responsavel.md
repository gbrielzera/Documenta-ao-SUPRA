# Responsavel

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Responsavel

Usuário responsável pelo Item de Configuração.

**Exemplo 1: modificação da propriedade Responsavel**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# modifica a propriedade Responsavel
itemConfiguracao.Responsavel = Pessoa.Carrega(91);
# salva modificação da propriedade Responsavel
ItemConfiguracao.Salva(itemConfiguracao)
```
