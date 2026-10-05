# Id

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Item de Configuração. Este identificador não pode ser modificado pelo usuário.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade Id
classeConfiguracao.Id = 1;
# salva modificação da propriedade Id
ClasseConfiguracao.Salva(classeConfiguracao)
```
