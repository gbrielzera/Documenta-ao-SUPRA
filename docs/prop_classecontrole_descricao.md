# Descricao

Caminho: Customização > Modelo de objetos > Processo > ClasseControle > Descricao

Descrição detalhada do ClasseControle

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ClasseControle de identificador 1
classeControle = ClasseControle.Carrega(1)
# modifica a propriedade Descricao
classeControle.Descricao = "Descrição";
# salva modificação da propriedade Descricao
ClasseControle.Salva(classeControle)
```
