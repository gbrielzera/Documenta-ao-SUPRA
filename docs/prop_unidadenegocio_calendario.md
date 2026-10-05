# Calendario

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > Calendario

Um Acordo de Nível de Serviço define prazos de atendimento para solicitações de um cliente. Além de prazos o acordo define condições tais como períodos de disponibilidade, possibilidades de suspensão do tempo, cobertura por processos e remuneração por serviços. O Acordo de Nível de Serviço é atribuido automaticamente pelo sistema no instante em que abrimos uma Ordem de Serviço ou modificamos campos chave: Cliente, Itens de Configuração, Prioridades, Subprocessos, Data/hora de solicitação entre outros. A data/hora de solicitação é considerada o marco inicial da contagem de tempo e a data/hora de fim é o marco final. A data/hora de fim pode ser sobrescrita pela data/hora de entrega de serviço, que pode ser preenchida durante a execução da Ordem de Serviço.

**Exemplo 1: modificação da propriedade Calendario**

```
# carrega objeto UnidadeNegocio de identificador 51
unidadeNegocio = UnidadeNegocio.Carrega(51)
# modifica a propriedade Calendario
unidadeNegocio.Calendario = Calendario.Carrega(94);
# salva modificação da propriedade Calendario
UnidadeNegocio.Salva(unidadeNegocio)
```
