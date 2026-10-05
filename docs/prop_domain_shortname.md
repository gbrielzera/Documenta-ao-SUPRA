# ShortName

Caminho: Customização > Modelo de objetos > Utilitários > Domain > ShortName

Nome abreviado (código) que identifica um Domínio.

**Exemplo 1: modificação da propriedade ShortName**

```
# carrega objeto Domain de identificador 1
domain = Domain.Carrega(1)
# modifica a propriedade ShortName
domain.ShortName = "Nome abreviado";
# salva modificação da propriedade ShortName
Domain.Salva(domain)
```
