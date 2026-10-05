# OrgaoDono

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > OrgaoDono

Órgão responsável pelo Subprocesso.

**Exemplo 1: modificação da propriedade OrgaoDono**

```
# carrega objeto ClasseSubProcesso de identificador 78
classeSubProcesso = ClasseSubProcesso.Carrega(78)
# modifica a propriedade OrgaoDono
classeSubProcesso.OrgaoDono = Orgao.Carrega(23);
# salva modificação da propriedade OrgaoDono
ClasseSubProcesso.Salva(classeSubProcesso)
```
