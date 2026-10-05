# SubstitutoAprovacaoId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > SubstitutoAprovacaoId

Identificador do Substituto para Aprovação

**Exemplo 1: modificação da propriedade SubstitutoAprovacaoId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade SubstitutoAprovacaoId
pessoa.SubstitutoAprovacaoId = 1;
# salva modificação da propriedade SubstitutoAprovacaoId
Pessoa.Salva(pessoa)
```
