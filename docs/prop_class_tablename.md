# TableName

Caminho: Customização > Modelo de objetos > Utilitários > Class > TableName

Nome da tabela que mantém objetos da Classe. Válido apenas para Classes de Entidades.

**Exemplo 1: modificação da propriedade TableName**

```
# carrega objeto Class de identificador 1
class = Class.Carrega(1)
# modifica a propriedade TableName
class.TableName = "Tabela";
# salva modificação da propriedade TableName
Class.Salva(class)
```
