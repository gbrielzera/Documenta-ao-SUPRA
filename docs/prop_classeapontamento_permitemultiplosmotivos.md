# PermiteMultiplosMotivos

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > PermiteMultiplosMotivos

Permite a informação de vários motivos no Apontamento

**Exemplo 1: modificação da propriedade PermiteMultiplosMotivos**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade PermiteMultiplosMotivos
classeApontamento.PermiteMultiplosMotivos = true;
# salva modificação da propriedade PermiteMultiplosMotivos
ClasseApontamento.Salva(classeApontamento)
```
