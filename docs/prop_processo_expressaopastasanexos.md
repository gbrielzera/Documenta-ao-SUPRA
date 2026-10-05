# ExpressaoPastasAnexos

Caminho: Customização > Modelo de objetos > Processo > Processo > ExpressaoPastasAnexos

Fórmula para caminho de pastas de Itens de Configuração anexados em Ocorrências

**Exemplo 1: modificação da propriedade ExpressaoPastasAnexos**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade ExpressaoPastasAnexos
processo.ExpressaoPastasAnexos = "Fórmula caminho pastas Associação";
# salva modificação da propriedade ExpressaoPastasAnexos
Processo.Salva(processo)
```
