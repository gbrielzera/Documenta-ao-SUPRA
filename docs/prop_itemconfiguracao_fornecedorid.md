# FornecedorId

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > FornecedorId

Identificador do Fornecedor

**Exemplo 1: modificação da propriedade FornecedorId**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade FornecedorId
itemConfiguracao.FornecedorId = 1;
# salva modificação da propriedade FornecedorId
ItemConfiguracao.Salva(itemConfiguracao)
```
