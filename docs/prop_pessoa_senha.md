# Senha

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Senha

Senha do usuário formada por no mínimo 4 caracteres que podem ser somente números ou letras. A comparação é insensível a letras minúsculas ou maiúsculas. Quando preenchida ignora validação de senha no Active Directory.

**Exemplo 1: modificação da propriedade Senha**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Senha
pessoa.Senha = "Senha de Autoatendimento";
# salva modificação da propriedade Senha
Pessoa.Salva(pessoa)
```
