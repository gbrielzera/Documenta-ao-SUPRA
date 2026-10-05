# CardinalidadeAlvo

Caminho: Customização > Modelo de objetos > Processo > Associacao > CardinalidadeAlvo

Cardinalidade da Associação no sentido Fonte para Alvo. Indica que podemos ter várias ou uma única ocorrência como Alvo no relacionamento.

**Exemplo 1: modificação da propriedade CardinalidadeAlvo**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade CardinalidadeAlvo
associacao.CardinalidadeAlvo = "ZeroOrMore";
# salva modificação da propriedade CardinalidadeAlvo
Associacao.Salva(associacao)
```
