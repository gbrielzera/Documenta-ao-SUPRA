# SequencialCampoString1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoString1

Define a sequencia de apresentação do controle utilizado para edição do Campo String 1

**Exemplo 1: modificação da propriedade SequencialCampoString1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoString1
classeApontamento.SequencialCampoString1 = 1;
# salva modificação da propriedade SequencialCampoString1
ClasseApontamento.Salva(classeApontamento)
```
