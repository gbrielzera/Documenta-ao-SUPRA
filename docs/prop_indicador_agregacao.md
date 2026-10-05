# Agregacao

Caminho: Customização > Modelo de objetos > Processo > Indicador > Agregacao

Função de agregação utilizada para apuração de Indicador.

**Exemplo 1: modificação da propriedade Agregacao**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade Agregacao
indicador.Agregacao = "Count";
# salva modificação da propriedade Agregacao
Indicador.Salva(indicador)
```
