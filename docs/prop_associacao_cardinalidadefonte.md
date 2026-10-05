# CardinalidadeFonte

Caminho: Customização > Modelo de objetos > Processo > Associacao > CardinalidadeFonte

Cardinalidade da Associação no sentido Alvo para Fonte

**Exemplo 1: modificação da propriedade CardinalidadeFonte**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade CardinalidadeFonte
associacao.CardinalidadeFonte = "ZeroOrMore";
# salva modificação da propriedade CardinalidadeFonte
Associacao.Salva(associacao)
```
