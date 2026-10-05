# ExpressaoPercentualEnvio

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > ExpressaoPercentualEnvio

Fórmula que é avaliada para determinar o Percentual de Envio de Pesquisas de Satisfação. Quando preenchido será desconsiderado o campo 'Percentual envio'.

**Exemplo 1: modificação da propriedade ExpressaoPercentualEnvio**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 1
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(1)
# modifica a propriedade ExpressaoPercentualEnvio
classePesquisaSatisfacao.ExpressaoPercentualEnvio = "Fórmula para percentual de envio";
# salva modificação da propriedade ExpressaoPercentualEnvio
ClassePesquisaSatisfacao.Salva(classePesquisaSatisfacao)
```
