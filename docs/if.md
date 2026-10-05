# IF

Caminho: Recursos Avançados > Objeto Utils > IF

Avalia a expressão booleana do primeiro parâmetro. Se o resultado for verdadeiro então retorna o parâmetro ifValue e se for falso retorna o valor elseValue.

O uso desta função é muito comum na elaboração de fórmulas. Veja um exemplo de uso de IF em fórmula:

Fórmula para recuperação do percentual de envio de pesquisa de satisfação

De acordo com a fórmula acima se o **a sigla da empresa do órgão do cliente da Ordem de Serviço for igual a VENKI** então será retornado o valor **0**, caso contrário deve ser utilizado o valor **100**.

## Assinatura

public object IF(bool testExpression, object ifValue, object elseValue)

### testExpression

Expressão booleana utilizada para teste e retorno do segundo ou terceiro parâmetro.

### ifValue

Valor que será retornado se testExpression retorna o valor verdadeiro.

### elseValue

Valor que será retornado se testExpression retornar o valor falso.
