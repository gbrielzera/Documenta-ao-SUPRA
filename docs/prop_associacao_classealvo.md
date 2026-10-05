# ClasseAlvo

Caminho: Customização > Modelo de objetos > Processo > Associacao > ClasseAlvo

Tipo de Subprocesso de Ocorrências que é alvo (terminador) em Associações.

**Exemplo 1: modificação da propriedade ClasseAlvo**

```
# carrega objeto Associacao de identificador 78
associacao = Associacao.Carrega(78)
# modifica a propriedade ClasseAlvo
associacao.ClasseAlvo = ClasseSubProcesso.Carrega(23);
# salva modificação da propriedade ClasseAlvo
Associacao.Salva(associacao)
```
