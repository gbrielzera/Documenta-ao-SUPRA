# OrdemServico

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > OrdemServico

Uma Ordem de Serviço é uma ocorrência de Processo em atendimento a uma solicitação de serviço de Tecnologia da Informação. Ordens de Serviço podem ser abertas na aplicação de Autoatendimento ou na transação Workspace do sistema Supravizio.

**Exemplo 1: modificação da propriedade OrdemServico**

```
# carrega objeto Pesquisa de identificador 78
pesquisa = Pesquisa.Carrega(78)
# modifica a propriedade OrdemServico
pesquisa.OrdemServico = OrdemServico.Carrega(23);
# salva modificação da propriedade OrdemServico
Pesquisa.Salva(pesquisa)
```
