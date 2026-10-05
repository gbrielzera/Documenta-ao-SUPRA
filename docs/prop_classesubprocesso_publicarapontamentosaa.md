# PublicarApontamentosAA

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > PublicarApontamentosAA

Indica a regra de publicação de apontamentos de horas trabalhadas no Autoatendimento

**Exemplo 1: modificação da propriedade PublicarApontamentosAA**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade PublicarApontamentosAA
classeSubProcesso.PublicarApontamentosAA = "Nunca";
# salva modificação da propriedade PublicarApontamentosAA
ClasseSubProcesso.Salva(classeSubProcesso)
```
