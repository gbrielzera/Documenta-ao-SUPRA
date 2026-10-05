# Codigo

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > Codigo

Código

**Exemplo 1: modificação da propriedade Codigo**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade Codigo
classeApontamento.Codigo = "Código";
# salva modificação da propriedade Codigo
ClasseApontamento.Salva(classeApontamento)
```
