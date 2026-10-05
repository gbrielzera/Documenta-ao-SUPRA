# ExpressaoPastasAprovacao

Caminho: Customização > Modelo de objetos > Processo > Processo > ExpressaoPastasAprovacao

Fórmula para caminho de pastas de Itens de Configuração para aprovação em Ocorrências

**Exemplo 1: modificação da propriedade ExpressaoPastasAprovacao**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade ExpressaoPastasAprovacao
processo.ExpressaoPastasAprovacao = "Fórmula caminho pastas Aprovação";
# salva modificação da propriedade ExpressaoPastasAprovacao
Processo.Salva(processo)
```
