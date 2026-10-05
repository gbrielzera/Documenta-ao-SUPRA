# SequencialCampoBooleano1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoBooleano1

Define a sequencia de apresentação do controle utilizado para edição do Campo Booleano 1

**Exemplo 1: modificação da propriedade SequencialCampoBooleano1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoBooleano1
classeApontamento.SequencialCampoBooleano1 = 1;
# salva modificação da propriedade SequencialCampoBooleano1
ClasseApontamento.Salva(classeApontamento)
```
