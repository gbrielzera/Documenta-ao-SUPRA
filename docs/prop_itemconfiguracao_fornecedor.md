# Fornecedor

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Fornecedor

Fornecedor para o Item. Se for mantido por equipe própria então não preencher.

**Exemplo 1: modificação da propriedade Fornecedor**

```
# carrega objeto ItemConfiguracao de identificador 73
itemConfiguracao = ItemConfiguracao.Carrega(73)
# modifica a propriedade Fornecedor
itemConfiguracao.Fornecedor = Fornecedor.Carrega(91);
# salva modificação da propriedade Fornecedor
ItemConfiguracao.Salva(itemConfiguracao)
```
