# LocalId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > LocalId

Identificador do Local de trabalho da Pessoa

**Exemplo 1: modificação da propriedade LocalId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade LocalId
pessoa.LocalId = 1;
# salva modificação da propriedade LocalId
Pessoa.Salva(pessoa)
```
