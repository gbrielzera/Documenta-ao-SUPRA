# Descricao

Caminho: Customização > Modelo de objetos > Processo > Indicador > Descricao

Texto que descreve claramente a finalizada de um Indicador de Desempenho. Este texto é utilizado na publicação do Indicador na página Executive Dashboard da tela Workspace.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade Descricao
indicador.Descricao = "Percentual de Incidentes atendidos no prazo de ANS";
# salva modificação da propriedade Descricao
Indicador.Salva(indicador)
```
