# RecoveryCode

Caminho: Customização > Modelo de objetos > Utilitários > Message > RecoveryCode

Código de recuperação para a Mensagem. Possui uso e preenchimento conforme critérios definidos pelo sistema usuário.

**Exemplo 1: modificação da propriedade RecoveryCode**

```
# carrega objeto Message de identificador 1
message = Message.Carrega(1)
# modifica a propriedade RecoveryCode
message.RecoveryCode = "Código recuperação";
# salva modificação da propriedade RecoveryCode
Message.Salva(message)
```
