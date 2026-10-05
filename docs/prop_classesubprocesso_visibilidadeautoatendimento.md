# VisibilidadeAutoAtendimento

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > VisibilidadeAutoAtendimento

Indica o tipo de visibilidade das ocorrências deste tipo de subprocesso no Autoatendimento, levando em consideração o cliente ou favorecido como referência

**Exemplo 1: modificação da propriedade VisibilidadeAutoAtendimento**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade VisibilidadeAutoAtendimento
classeSubProcesso.VisibilidadeAutoAtendimento = "Todos";
# salva modificação da propriedade VisibilidadeAutoAtendimento
ClasseSubProcesso.Salva(classeSubProcesso)
```
