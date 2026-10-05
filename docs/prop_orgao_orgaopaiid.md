# OrgaoPaiId

Caminho: Customização > Modelo de objetos > Recurso > Orgao > OrgaoPaiId

Identificador do Orgao pai que define a hierarquia organizacional.

**Exemplo 1: modificação da propriedade OrgaoPaiId**

```
# carrega objeto Orgao de identificador 1
orgao = Orgao.Carrega(1)
# modifica a propriedade OrgaoPaiId
orgao.OrgaoPaiId = 1;
# salva modificação da propriedade OrgaoPaiId
Orgao.Salva(orgao)
```
