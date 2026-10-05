# SequencialCampoInteiro1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoInteiro1

Define a sequencia de apresentação do controle utilizado para edição do Campo Inteiro 1

**Exemplo 1: modificação da propriedade SequencialCampoInteiro1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoInteiro1
classeApontamento.SequencialCampoInteiro1 = 1;
# salva modificação da propriedade SequencialCampoInteiro1
ClasseApontamento.Salva(classeApontamento)
```
