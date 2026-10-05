# Descricao

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Descricao

Descrição detalhada sobre o Item de configuração

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade Descricao
itemConfiguracao.Descricao = "Descrição";
# salva modificação da propriedade Descricao
ItemConfiguracao.Salva(itemConfiguracao)
```
