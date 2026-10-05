# PessoaRegistroAprovacao

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > PessoaRegistroAprovacao

Pessoa que realizou o registro do Substituto pela aprovação. Este pode ser o próprio Cliente quando realizado pelo site de Autoatendimento ou um Profissional utilizando a aplicação Supravizio.

**Exemplo 1: modificação da propriedade PessoaRegistroAprovacao**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade PessoaRegistroAprovacao
pessoa.PessoaRegistroAprovacao = Pessoa.Carrega(94);
# salva modificação da propriedade PessoaRegistroAprovacao
Pessoa.Salva(pessoa)
```
