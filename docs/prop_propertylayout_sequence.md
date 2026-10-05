# Sequence

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > Sequence

Sequencial do Controle dentro do seu agrupamento

**Exemplo 1: modificação da propriedade Sequence**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade Sequence
propertyLayout.Sequence = 1;
# salva modificação da propriedade Sequence
PropertyLayout.Salva(propertyLayout)
```
