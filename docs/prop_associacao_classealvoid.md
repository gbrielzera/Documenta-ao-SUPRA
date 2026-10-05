# ClasseAlvoId

Caminho: Customização > Modelo de objetos > Processo > Associacao > ClasseAlvoId

Identificador do Tipo de Subprocesso que é invocado pela associação.

**Exemplo 1: modificação da propriedade ClasseAlvoId**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade ClasseAlvoId
associacao.ClasseAlvoId = 1;
# salva modificação da propriedade ClasseAlvoId
Associacao.Salva(associacao)
```
