# FonteDados

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > FonteDados

Fonte de dados (válido somente para Artefatos)

**Exemplo 1: modificação da propriedade FonteDados**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade FonteDados
classeConfiguracao.FonteDados = "SistemaArquivos";
# salva modificação da propriedade FonteDados
ClasseConfiguracao.Salva(classeConfiguracao)
```
