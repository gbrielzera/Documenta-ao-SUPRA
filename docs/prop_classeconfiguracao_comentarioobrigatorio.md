# ComentarioObrigatorio

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > ComentarioObrigatorio

Determina se o Item pertencente a esta Classe de Configuração terá o campo Comentário como Obrigatório

**Exemplo 1: modificação da propriedade ComentarioObrigatorio**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade ComentarioObrigatorio
classeConfiguracao.ComentarioObrigatorio = true;
# salva modificação da propriedade ComentarioObrigatorio
ClasseConfiguracao.Salva(classeConfiguracao)
```
