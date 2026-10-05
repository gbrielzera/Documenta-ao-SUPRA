# PermiteMultiplosApontamentos

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > PermiteMultiplosApontamentos

Permite vários apontamentos para uma ocorrência de Processo.

**Exemplo 1: modificação da propriedade PermiteMultiplosApontamentos**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade PermiteMultiplosApontamentos
classeApontamento.PermiteMultiplosApontamentos = true;
# salva modificação da propriedade PermiteMultiplosApontamentos
ClasseApontamento.Salva(classeApontamento)
```
