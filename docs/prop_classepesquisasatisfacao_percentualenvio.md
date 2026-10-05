# PercentualEnvio

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > PercentualEnvio

Número percentual entre 0 e 100 que indica a probabilidade de envio de Pesquisa de Satisfação. O valor 0 indica que nenhuma Pesquisa será enviada enquanto 100 estabelece que sempre será enviada Pesquisa de Satisfação

**Exemplo 1: modificação da propriedade PercentualEnvio**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 1
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(1)
# modifica a propriedade PercentualEnvio
classePesquisaSatisfacao.PercentualEnvio = 1;
# salva modificação da propriedade PercentualEnvio
ClassePesquisaSatisfacao.Salva(classePesquisaSatisfacao)
```
