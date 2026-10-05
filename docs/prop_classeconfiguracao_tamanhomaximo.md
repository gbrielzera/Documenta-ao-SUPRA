# TamanhoMaximo

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > TamanhoMaximo

Tamanho máximo (em megabytes) permitido por arquivo deste tipo.

**Exemplo 1: modificação da propriedade TamanhoMaximo**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade TamanhoMaximo
classeConfiguracao.TamanhoMaximo = 1;
# salva modificação da propriedade TamanhoMaximo
ClasseConfiguracao.Salva(classeConfiguracao)
```
