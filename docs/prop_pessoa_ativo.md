# Ativo

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Ativo

Indica que a Pessoa está Ativa no sistema.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Ativo
pessoa.Ativo = true;
# salva modificação da propriedade Ativo
Pessoa.Salva(pessoa)
```
