# Email

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Email

Email da Pessoa

**Exemplo 1: modificação da propriedade Email**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Email
pessoa.Email = "jose.aparecido@supravizio.com";
# salva modificação da propriedade Email
Pessoa.Salva(pessoa)
```
