# ClassePesquisaSatisfacao

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > ClassePesquisaSatisfacao

Uma Classe de Pesquisa de Satisfação define um conjunto de configurações utilizado para geração de Pesquisas de Satisfação enviadas para clientes após finalização de uma Ordem de Serviço. O envio da pesquisa está condicionado ao evento terminador utilizado na definição do processo aplicado em Ordens de Serviço alvo da pesquisa.

**Exemplo 1: modificação da propriedade ClassePesquisaSatisfacao**

```
# carrega objeto Pesquisa de identificador 78
pesquisa = Pesquisa.Carrega(78)
# modifica a propriedade ClassePesquisaSatisfacao
pesquisa.ClassePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(23);
# salva modificação da propriedade ClassePesquisaSatisfacao
Pesquisa.Salva(pesquisa)
```
