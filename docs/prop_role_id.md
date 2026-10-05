# Id

Caminho: Customização > Modelo de objetos > Utilitários > Role > Id

Identificador do Perfil de acesso

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Role de identificador 1
role = Role.Carrega(1)
# modifica a propriedade Id
role.Id = 1;
# salva modificação da propriedade Id
Role.Salva(role)
```
