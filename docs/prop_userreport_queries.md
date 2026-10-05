# Queries

Caminho: Customização > Modelo de objetos > Utilitários > UserReport > Queries

Consultas utilizadas no relatório. Todo relatório pode conter uma ou mais consultas. Para cada banda Detail Report existirá uma consulta.

**Exemplo 1: percorrer objetos da propriedade Queries**

```
# carrega objeto UserReport de identificador 94
userReport = UserReport.Carrega(94)
# verifica se o objeto foi recuperado com sucesso
if userReport != None:
    # percorre objetos da propriedade Queries e para cada uma escreve conteúdo no log de mensagens
    for reportQuery in userReport.Queries:
        Utils.LogInformation(reportQuery.ToString())
```
