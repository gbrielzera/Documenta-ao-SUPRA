# TelefoneSegundoContato

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > TelefoneSegundoContato

Telefone da Segunda Pessoa de contato

**Exemplo 1: modificação da propriedade TelefoneSegundoContato**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade TelefoneSegundoContato
pessoa.TelefoneSegundoContato = "Telefone segundo contato";
# salva modificação da propriedade TelefoneSegundoContato
Pessoa.Salva(pessoa)
```
