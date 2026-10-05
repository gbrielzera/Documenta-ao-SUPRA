# Descricao

Caminho: Customização > Modelo de objetos > Processo > Processo > Descricao

Descrição detalhada do Processo. Este descritivo é utilizado para nomear pastas no repositório de arquivo e por este motivo não pode conter os seguintes caracteres \\ / : > ? * "

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade Descricao
processo.Descricao = "Indicente";
# salva modificação da propriedade Descricao
Processo.Salva(processo)
```
