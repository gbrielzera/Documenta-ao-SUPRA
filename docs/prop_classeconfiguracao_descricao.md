# Descricao

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > Descricao

Texto que descreve claramente a classificação de um Item de Configuração. No caso de tipos que representam arquivos este descritivo não pode conter os caracteres \\ / : > ? * " pois este descritivo é utilizado para nomear pastas no repositório de arquivos.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade Descricao
classeConfiguracao.Descricao = "Desktop";
# salva modificação da propriedade Descricao
ClasseConfiguracao.Salva(classeConfiguracao)
```
