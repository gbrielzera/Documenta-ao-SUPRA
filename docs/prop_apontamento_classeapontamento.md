# ClasseApontamento

Caminho: Customização > Modelo de objetos > Processo > Apontamento > ClasseApontamento

Classe de Apontamento

**Exemplo 1: modificação da propriedade ClasseApontamento**

```
# carrega objeto Apontamento de identificador 94
apontamento = Apontamento.Carrega(94)
# modifica a propriedade ClasseApontamento
apontamento.ClasseApontamento = ClasseApontamento.Carrega(82);
# salva modificação da propriedade ClasseApontamento
Apontamento.Salva(apontamento)
```
