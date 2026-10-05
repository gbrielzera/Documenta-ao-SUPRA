# CALENDARIO

Caminho: Customização > Modelo de dados > Recurso > CALENDARIO

Um Acordo de Nível de Serviço define prazos de atendimento para solicitações de um cliente. Além de prazos o acordo define condições tais como períodos de disponibilidade, possibilidades de suspensão do tempo, cobertura por processos e remuneração por serviços. O Acordo de Nível de Serviço é atribuido automaticamente pelo sistema no instante em que abrimos uma Ordem de Serviço ou modificamos campos chave: Cliente, Itens de Configuração, Prioridades, Subprocessos, Data/hora de solicitação entre outros. A data/hora de solicitação é considerada o marco inicial da contagem de tempo e a data/hora de fim é o marco final. A data/hora de fim pode ser sobrescrita pela data/hora de entrega de serviço, que pode ser preenchida durante a execução da Ordem de Serviço.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CALENDARIO** | Número seqüencial gerado por sistema para identificação de um Calendário | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente o conteúdo e a aplicação de um Calendário. | varchar(500) | varchar(500) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas que dependem de CALENDARIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [UNIDADE_NEGOCIO](dados_unidade_negocio) | \| **UNIDADE_NEGOCIO** \| **CALENDARIO** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |
| [TECNICO](dados_tecnico) | \| **TECNICO** \| **CALENDARIO** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |
| [FERIADO](dados_feriado) | \| **FERIADO** \| **CALENDARIO** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |
| [PERIODO_UTIL](dados_periodo_util) | \| **PERIODO_UTIL** \| **CALENDARIO** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |
