# GroupSequence

Caminho: Customização > Modelo de objetos > Utilitários > PropertyLayout > GroupSequence

Sequencial do Grupo no formulário. Se Group não for preenchido considerar o valor default -1

**Exemplo 1: modificação da propriedade GroupSequence**

```
# carrega objeto PropertyLayout de identificador 1
propertyLayout = PropertyLayout.Carrega(1)
# modifica a propriedade GroupSequence
propertyLayout.GroupSequence = 1;
# salva modificação da propriedade GroupSequence
PropertyLayout.Salva(propertyLayout)
```
