# SequencialCampoDecimal1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoDecimal1

Define a sequencia de apresentação do controle utilizado para edição do Campo Decimal 1

**Exemplo 1: modificação da propriedade SequencialCampoDecimal1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoDecimal1
classeApontamento.SequencialCampoDecimal1 = 1;
# salva modificação da propriedade SequencialCampoDecimal1
ClasseApontamento.Salva(classeApontamento)
```
