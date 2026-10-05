# Fornecedor

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Fornecedor

Empresa Fornecedora responsável pelo Terceiro. Preencher este campo somente quando a Pessoa for um Terceiro.

**Exemplo 1: modificação da propriedade Fornecedor**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade Fornecedor
pessoa.Fornecedor = Fornecedor.Carrega(94);
# salva modificação da propriedade Fornecedor
Pessoa.Salva(pessoa)
```
