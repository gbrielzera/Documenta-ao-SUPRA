# Id

Caminho: Customização > Modelo de objetos > Processo > ClasseControle > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseControle

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ClasseControle de identificador 1
classeControle = ClasseControle.Carrega(1)
# modifica a propriedade Id
classeControle.Id = 1;
# salva modificação da propriedade Id
ClasseControle.Salva(classeControle)
```
