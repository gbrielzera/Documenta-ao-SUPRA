# FiltroServicoAssociacaoOcorrencia

Caminho: Customização > Modelo de objetos > Ativos > ClasseConfiguracao > FiltroServicoAssociacaoOcorrencia

Sempre que um item deste tipo for associado a uma Ordem de Serviço (na tela de edição ou Autoatendimento) existirá um filtro implícito por componentes do Serviço informado na ocorrência de processo.

**Exemplo 1: modificação da propriedade FiltroServicoAssociacaoOcorrencia**

```
# carrega objeto ClasseConfiguracao de identificador 1
classeConfiguracao = ClasseConfiguracao.Carrega(1)
# modifica a propriedade FiltroServicoAssociacaoOcorrencia
classeConfiguracao.FiltroServicoAssociacaoOcorrencia = true;
# salva modificação da propriedade FiltroServicoAssociacaoOcorrencia
ClasseConfiguracao.Salva(classeConfiguracao)
```
