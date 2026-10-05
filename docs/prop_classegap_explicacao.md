# Explicacao

Caminho: Customização > Modelo de objetos > Processo > ClasseGap > Explicacao

Explicação

**Exemplo 1: modificação da propriedade Explicacao**

```
# carrega objeto ClasseGap de identificador 1
classeGap = ClasseGap.Carrega(1)
# modifica a propriedade Explicacao
classeGap.Explicacao = "Explicação";
# salva modificação da propriedade Explicacao
ClasseGap.Salva(classeGap)
```
