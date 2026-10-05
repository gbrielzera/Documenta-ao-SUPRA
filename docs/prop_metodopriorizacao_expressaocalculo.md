# ExpressaoCalculo

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > ExpressaoCalculo

Expressão utilizada para determinar a base de cálculo utilizada para seleção do Grau de Prioridade a partir. Para seleção do Grau de Prioridade é selecionado aquele com Limite Superior maior que o valor resultante na Expressão. A expressão deve retornar obrigatoriamente um número Inteiro não negativo.

**Exemplo 1: modificação da propriedade ExpressaoCalculo**

```
# carrega objeto MetodoPriorizacao de identificador 1
metodoPriorizacao = MetodoPriorizacao.Carrega(1)
# modifica a propriedade ExpressaoCalculo
metodoPriorizacao.ExpressaoCalculo = "Expressão cálculo";
# salva modificação da propriedade ExpressaoCalculo
MetodoPriorizacao.Salva(metodoPriorizacao)
```
