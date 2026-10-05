# SequencialCampoDataHora1

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoDataHora1

Define a sequencia de apresentação do controle utilizado para edição do Campo Data/hora 1

**Exemplo 1: modificação da propriedade SequencialCampoDataHora1**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoDataHora1
classeApontamento.SequencialCampoDataHora1 = 1;
# salva modificação da propriedade SequencialCampoDataHora1
ClasseApontamento.Salva(classeApontamento)
```
