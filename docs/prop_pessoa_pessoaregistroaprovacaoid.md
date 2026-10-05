# PessoaRegistroAprovacaoId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > PessoaRegistroAprovacaoId

Identificador da Pessoa que realizou o registro de Substituição para Aprovação

**Exemplo 1: modificação da propriedade PessoaRegistroAprovacaoId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade PessoaRegistroAprovacaoId
pessoa.PessoaRegistroAprovacaoId = 1;
# salva modificação da propriedade PessoaRegistroAprovacaoId
Pessoa.Salva(pessoa)
```
