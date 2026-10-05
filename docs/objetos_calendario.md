# Calendario

Caminho: Customização > Modelo de objetos > Recurso > Calendario

Um Acordo de Nível de Serviço define prazos de atendimento para solicitações de um cliente. Além de prazos o acordo define condições tais como períodos de disponibilidade, possibilidades de suspensão do tempo, cobertura por processos e remuneração por serviços. O Acordo de Nível de Serviço é atribuido automaticamente pelo sistema no instante em que abrimos uma Ordem de Serviço ou modificamos campos chave: Cliente, Itens de Configuração, Prioridades, Subprocessos, Data/hora de solicitação entre outros. A data/hora de solicitação é considerada o marco inicial da contagem de tempo e a data/hora de fim é o marco final. A data/hora de fim pode ser sobrescrita pela data/hora de entrega de serviço, que pode ser preenchida durante a execução da Ordem de Serviço.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Texto que descreve claramente o conteúdo e a aplicação de um Calendário. | String |
| **Feriados** | Um Feriado constitui uma data especial onde considerada, a princípio, dia não-útil. | [Lista de Feriado](objetos_feriado) |
| **Id** | Número seqüencial gerado por sistema para identificação de um Calendário | Inteiro |
| **PeriodosUteis** | Regras que configuram a disponibildade de recursos em função dos dias da semana | [Lista de PeriodoUtil](objetos_periodoutil) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Calendario Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Calendario | Calendario Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Calendario Carrega(string nomePropriedade, object valorPropriedade); |
