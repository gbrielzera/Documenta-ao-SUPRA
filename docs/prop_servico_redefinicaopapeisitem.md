# RedefinicaoPapeisItem

Caminho: Customização > Modelo de objetos > Processo > Servico > RedefinicaoPapeisItem

Define o comportamento da rotina de resolução de Atores quando existirem redefinições de Papéis em Itens de Configuração associados em uma Ordem de Serviço.

**Exemplo 1: modificação da propriedade RedefinicaoPapeisItem**

```
# carrega objeto Servico de identificador 1
servico = Servico.Carrega(1)
# modifica a propriedade RedefinicaoPapeisItem
servico.RedefinicaoPapeisItem = "SobreposicaoPorItem";
# salva modificação da propriedade RedefinicaoPapeisItem
Servico.Salva(servico)
```
