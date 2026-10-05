# OrgaoDonoId

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > OrgaoDonoId

Identificador do Órgão proprietário do Processo

**Exemplo 1: modificação da propriedade OrgaoDonoId**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade OrgaoDonoId
classeSubProcesso.OrgaoDonoId = 1;
# salva modificação da propriedade OrgaoDonoId
ClasseSubProcesso.Salva(classeSubProcesso)
```
