# UserId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > UserId

Identificador do Usuário associado

**Exemplo 1: modificação da propriedade UserId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade UserId
pessoa.UserId = 1;
# salva modificação da propriedade UserId
Pessoa.Salva(pessoa)
```
