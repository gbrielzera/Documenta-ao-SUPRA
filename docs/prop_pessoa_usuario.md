# Usuario

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Usuario

Usuário relacionado com a Pessoa, caso esta seja um Solucionador

**Exemplo 1: modificação da propriedade Usuario**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade Usuario
pessoa.Usuario = User.Carrega(94);
# salva modificação da propriedade Usuario
Pessoa.Salva(pessoa)
```
