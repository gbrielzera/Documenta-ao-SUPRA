# EmailAlternativo

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > EmailAlternativo

Email alternativo de contato para a Pessoa

**Exemplo 1: modificação da propriedade EmailAlternativo**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade EmailAlternativo
pessoa.EmailAlternativo = "jose_aparecido@hotmail.com";
# salva modificação da propriedade EmailAlternativo
Pessoa.Salva(pessoa)
```
