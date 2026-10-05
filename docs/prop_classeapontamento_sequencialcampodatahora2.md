# SequencialCampoDataHora2

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > SequencialCampoDataHora2

Define a sequencia de apresentação do controle utilizado para edição do Campo Data/hora 2

**Exemplo 1: modificação da propriedade SequencialCampoDataHora2**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade SequencialCampoDataHora2
classeApontamento.SequencialCampoDataHora2 = 1;
# salva modificação da propriedade SequencialCampoDataHora2
ClasseApontamento.Salva(classeApontamento)
```
