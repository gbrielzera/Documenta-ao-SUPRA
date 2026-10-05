# Transaction

Caminho: Customização > Modelo de objetos > Utilitários > Command > Transaction

Transação que será acessada quando o comando for executado. Quando não preenchido significa que o comando será utilizado como um container para outros sub-comandos.

**Exemplo 1: modificação da propriedade Transaction**

```
# carrega objeto Command de identificador 94
command = Command.Carrega(94)
# modifica a propriedade Transaction
command.Transaction = Transaction.Carrega(57);
# salva modificação da propriedade Transaction
Command.Salva(command)
```
