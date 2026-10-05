# UsuarioRede

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > UsuarioRede

Nome do usuário de rede utilizado pela Pessoa para acesso a ambiente de rede

**Exemplo 1: modificação da propriedade UsuarioRede**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade UsuarioRede
pessoa.UsuarioRede = "jose.aparecido";
# salva modificação da propriedade UsuarioRede
Pessoa.Salva(pessoa)
```
