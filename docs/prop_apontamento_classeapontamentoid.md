# ClasseApontamentoId

Caminho: Customização > Modelo de objetos > Processo > Apontamento > ClasseApontamentoId

Identificador do ClasseApontamento associado

**Exemplo 1: modificação da propriedade ClasseApontamentoId**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade ClasseApontamentoId
apontamento.ClasseApontamentoId = 1;
# salva modificação da propriedade ClasseApontamentoId
Apontamento.Salva(apontamento)
```
