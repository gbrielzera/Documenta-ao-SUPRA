# Domain

Caminho: Customização > Modelo de objetos > Utilitários > Role > Domain

Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias

**Exemplo 1: modificação da propriedade Domain**

```
# carrega objeto Role de identificador 94
role = Role.Carrega(94)
# modifica a propriedade Domain
role.Domain = Domain.Carrega(57);
# salva modificação da propriedade Domain
Role.Salva(role)
```
