# Enabled

Caminho: Customização > Modelo de objetos > Utilitários > Domain > Enabled

Indica que o Domínio está ativo. Quando desabilitado não é possível ao usuário a operação de Login.

**Exemplo 1: modificação da propriedade Enabled**

```
# carrega objeto Domain de identificador 1
domain = Domain.Carrega(1)
# modifica a propriedade Enabled
domain.Enabled = true;
# salva modificação da propriedade Enabled
Domain.Salva(domain)
```
