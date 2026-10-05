# Comentario

Caminho: Customização > Modelo de objetos > Ativos > ItemConfiguracao > Comentario

Comentário sobre o Item destinados ao Cliente. Para histórico de observações utilize a relação de Observações.

**Exemplo 1: modificação da propriedade Comentario**

```
# carrega objeto ItemConfiguracao de identificador 1
itemConfiguracao = ItemConfiguracao.Carrega(1)
# modifica a propriedade Comentario
itemConfiguracao.Comentario = "Comentários para Cliente";
# salva modificação da propriedade Comentario
ItemConfiguracao.Salva(itemConfiguracao)
```
