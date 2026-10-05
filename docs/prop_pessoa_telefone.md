# Telefone

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Telefone

Número do Telefone (ramal) de contato.

**Exemplo 1: modificação da propriedade Telefone**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Telefone
pessoa.Telefone = "3991";
# salva modificação da propriedade Telefone
Pessoa.Salva(pessoa)
```
