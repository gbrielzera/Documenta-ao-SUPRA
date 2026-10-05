# MotivoObrigatorio

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > MotivoObrigatorio

A informação de um Motivo é obrigatória no instante em que é realizado o Apontamento.

**Exemplo 1: modificação da propriedade MotivoObrigatorio**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade MotivoObrigatorio
classeApontamento.MotivoObrigatorio = true;
# salva modificação da propriedade MotivoObrigatorio
ClasseApontamento.Salva(classeApontamento)
```
