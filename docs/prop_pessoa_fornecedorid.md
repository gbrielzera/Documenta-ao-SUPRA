# FornecedorId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > FornecedorId

Identificador do Fornecedor em caso de Terceiros.

**Exemplo 1: modificação da propriedade FornecedorId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade FornecedorId
pessoa.FornecedorId = 1;
# salva modificação da propriedade FornecedorId
Pessoa.Salva(pessoa)
```
