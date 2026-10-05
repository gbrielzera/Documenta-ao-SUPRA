# Name

Caminho: Customização > Modelo de objetos > Utilitários > Domain > Name

Nome do Domínio

**Exemplo 1: modificação da propriedade Name**

```
# carrega objeto Domain de identificador 1
domain = Domain.Carrega(1)
# modifica a propriedade Name
domain.Name = "Nome";
# salva modificação da propriedade Name
Domain.Salva(domain)
```
