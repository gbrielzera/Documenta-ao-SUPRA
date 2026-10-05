# SubstitutoAprovacao

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > SubstitutoAprovacao

Pessoa autorizada a realizar aprovações como substituto. O Substituto pode ser registrado na aplicação Supravizio ou pelo próprio Cliente pelo site de Autoatendimento. A autorização de substituição em aprovações é válida por um período com data de início e data de fim que são obrigatórios no registro da substituição.

**Exemplo 1: modificação da propriedade SubstitutoAprovacao**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade SubstitutoAprovacao
pessoa.SubstitutoAprovacao = Pessoa.Carrega(94);
# salva modificação da propriedade SubstitutoAprovacao
Pessoa.Salva(pessoa)
```
