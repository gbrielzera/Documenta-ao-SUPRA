# SequencialCampoBooleano2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoBooleano2

Define a sequencia de apresentação do controle utilizado para edição do Campo Booleano 2

**Exemplo 1: modificação da propriedade SequencialCampoBooleano2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoBooleano2
classeApontamento.SequencialCampoBooleano2 = 1;
# salva modificação da propriedade SequencialCampoBooleano2
ClasseApontamento.Salva(classeApontamento)
```
