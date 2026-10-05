# Reference

Caminho: Customização > Modelo de objetos > Utilitários > Role > Reference

Texto explicativo para utilização do Perfil de acesso. Pode ser utilizado para esclarecer sobre funções ou transações que podem ser acessadas pelo usuário que detém o perfil.

**Exemplo 1: modificação da propriedade Reference**

```
# carrega objeto Role de identificador 1
role = Role.Carrega(1)
# modifica a propriedade Reference
role.Reference = "Referência";
# salva modificação da propriedade Reference
Role.Salva(role)
```
