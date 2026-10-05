# Id

Caminho: Customização > Modelo de objetos > Utilitários > Domain > Id

Identificador do Domínio

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Domain de identificador 1
domain = Domain.Carrega(1)
# modifica a propriedade Id
domain.Id = 1;
# salva modificação da propriedade Id
Domain.Salva(domain)
```
