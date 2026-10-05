# Name

Caminho: Customização > Modelo de objetos > Utilitários > Role > Name

Nome do Perfil de acesso

**Exemplo 1: modificação da propriedade Name**

```
# carrega objeto Role de identificador 1
role = Role.Carrega(1)
# modifica a propriedade Name
role.Name = "Nome";
# salva modificação da propriedade Name
Role.Salva(role)
```
