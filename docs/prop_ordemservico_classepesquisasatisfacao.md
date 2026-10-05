# ClassePesquisaSatisfacao

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ClassePesquisaSatisfacao

Classe de Pesquisa de Satisfação para geração de Pesquisa. Esta referência é estabelecida na operação de Finalização e utilizada pela rotina que realiza o envio de Pesquisa de Satisfação.

**Exemplo 1: modificação da propriedade ClassePesquisaSatisfacao**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade ClassePesquisaSatisfacao
ordemServico.ClassePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(23);
# salva modificação da propriedade ClassePesquisaSatisfacao
OrdemServico.Salva(ordemServico)
```
