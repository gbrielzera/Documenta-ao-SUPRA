# SequencialCampoInteiro2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoInteiro2

Define a sequencia de apresentação do controle utilizado para edição do Campo Inteiro 2

**Exemplo 1: modificação da propriedade SequencialCampoInteiro2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoInteiro2
classeApontamento.SequencialCampoInteiro2 = 1;
# salva modificação da propriedade SequencialCampoInteiro2
ClasseApontamento.Salva(classeApontamento)
```
