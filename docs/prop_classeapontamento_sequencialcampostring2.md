# SequencialCampoString2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoString2

Define a sequencia de apresentação do controle utilizado para edição do Campo String 2

**Exemplo 1: modificação da propriedade SequencialCampoString2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoString2
classeApontamento.SequencialCampoString2 = 1;
# salva modificação da propriedade SequencialCampoString2
ClasseApontamento.Salva(classeApontamento)
```
