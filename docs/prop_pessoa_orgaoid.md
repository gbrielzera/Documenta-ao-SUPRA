# OrgaoId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > OrgaoId

Identificador do Órgão onde a Pessoa está lotada

**Exemplo 1: modificação da propriedade OrgaoId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade OrgaoId
pessoa.OrgaoId = 1;
# salva modificação da propriedade OrgaoId
Pessoa.Salva(pessoa)
```
