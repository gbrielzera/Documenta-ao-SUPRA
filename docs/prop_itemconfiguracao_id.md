# Id

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Id

Número sequencial gerado automaticamente para Identificar um Item de Configuração

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade Id
itemConfiguracao.Id = 1;
# salva modificação da propriedade Id
ItemConfiguracao.Salva(itemConfiguracao)
```
