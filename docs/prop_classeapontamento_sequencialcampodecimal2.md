# SequencialCampoDecimal2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoDecimal2

Define a sequencia de apresentação do controle utilizado para edição do Campo Decimal 2

**Exemplo 1: modificação da propriedade SequencialCampoDecimal2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoDecimal2
classeApontamento.SequencialCampoDecimal2 = 1;
# salva modificação da propriedade SequencialCampoDecimal2
ClasseApontamento.Salva(classeApontamento)
```
