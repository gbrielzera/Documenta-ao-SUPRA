# ClasseFonte

Caminho: Customização > Modelo de objetos > Processo > Associacao > ClasseFonte

Tipo de Subprocesso de Ocorrências que são fonte (iniciadores) em Associações. Indica que podemos ter várias ou uma única ocorrência como Fonte no relacionamento.

**Exemplo 1: modificação da propriedade ClasseFonte**

```
# carrega objeto Associacao de identificador 78
associacao = Associacao.Carrega(78)
# modifica a propriedade ClasseFonte
associacao.ClasseFonte = ClasseSubProcesso.Carrega(23);
# salva modificação da propriedade ClasseFonte
Associacao.Salva(associacao)
```
