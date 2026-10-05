# ClasseFonteId

Caminho: Customização > Modelo de objetos > Processo > Associacao > ClasseFonteId

Identificador do Tipo de Subprocesso que é responsável por invocar uma outra ocorrência de processo (rotina chamadora).

**Exemplo 1: modificação da propriedade ClasseFonteId**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade ClasseFonteId
associacao.ClasseFonteId = 1;
# salva modificação da propriedade ClasseFonteId
Associacao.Salva(associacao)
```
