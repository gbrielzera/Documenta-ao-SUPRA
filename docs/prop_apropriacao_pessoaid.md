# PessoaId

Caminho: Customização > Modelo de objetos > Processo > Apropriacao > PessoaId

Identificador da Pessoa associada

**Exemplo 1: modificação da propriedade PessoaId**

```
# carrega objeto Apropriacao de identificador 1
apropriacao = Apropriacao.Carrega(1)
# modifica a propriedade PessoaId
apropriacao.PessoaId = 1;
# salva modificação da propriedade PessoaId
Apropriacao.Salva(apropriacao)
```
