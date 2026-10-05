# RegraAutorizacao

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > RegraAutorizacao

Regra de autorização para visualização de Ordens de Serviço do Subprocesso. Se este campo não for preenchido o sistema utilizará o parâmetro default cadastrado na tela de Configurações.

**Exemplo 1: modificação da propriedade RegraAutorizacao**

```
# carrega objeto ClasseSubProcesso de identificador 1
classeSubProcesso = ClasseSubProcesso.Carrega(1)
# modifica a propriedade RegraAutorizacao
classeSubProcesso.RegraAutorizacao = "Publico";
# salva modificação da propriedade RegraAutorizacao
ClasseSubProcesso.Salva(classeSubProcesso)
```
