# EMISSOR

Caminho: Customização > Modelo de dados > Processo > EMISSOR

Saída de um Gateway

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_EMISSOR** | Identificador da alternativa. | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Identificador da Atividade de destino se for selecionada a alternativa. Se preenchido então obrigatoriamente o campo GatewaySaida será nulo. | int | number(6,0) | Sim |
| **ID_GATEWAY** | Identificador do gateway proprietário da alternativa. | int | number(6,0) | Não |
| **OPERADOR** | Operador utilizado para compor a fórmula ou critério de seleção da alternativa. | varchar(250) | varchar(250) | Sim |
| **VALOR_COMPARACAO** | Fórmula Python utilizada para comparação com a outra fórmula definda na decisão | varchar(500) | varchar(500) | Sim |
| **REFERENCIA_DECISION** | Texto utilizado para representar a decisão. No caso de decisões baseadas em eventos este mesmo texto é utilizado como opção de resposta para que o usuário tome sua decisão. | varchar(500) | varchar(500) | Sim |
| **SEQUENCIA_AVAL** | Sequencia utilizada durante avaliação das alternativas. Esta sequência pode influenciar na lógica da decisão visto que o processo seguirá a primeira que atender a fórmula de seleção. | int | number(6,0) | Não |
| **ID_GATEWAY_SAIDA** | Identificador do Gateway de destino do fluxo se for selecionada a alternativa. Se preenchido então obrigatoriamente o campo Atividade será nulo. | int | number(6,0) | Sim |
| **ROTULO_MOTIVO** | Texto que é apresentado para o usuário quando este seleciona a alternativa. Este campo é válido somente para decisões baseadas em respostas. | varchar(500) | varchar(500) | Sim |
| **MOTIVO_OBRIG** | Indica que o preenchimento de um motivo é obrigatório se for selecionada a alternativa. Este campo só faz sentido no caso de decisões baseaadas em respostas do usuário. | char(3) | char(3) | Não |
| **PUB_RESP_AA** | A resposta informada pelo solucionador fica disponível no Autoatendimento para visualização dos interessados | char(3) | char(3) | Não |
| **PERM_CANC_PUB_AA** | Permite o cancelamento da publicação no Autoatendimento da resposta informada pelo solucionador. Caso não seja permitido cancelar, apenas os superiores do solucionador poderão cancelar a publicação (independente desse parâmetro). | char(3) | char(3) | Não |

Tabelas referenciadas por EMISSOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **EMISSOR** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [GATEWAY](dados_gateway) | \| **GATEWAY** \| **EMISSOR** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY_SAIDA \| |
| [GATEWAY](dados_gateway) | \| **GATEWAY** \| **EMISSOR** \| \|---\|---\| \| ID_GATEWAY \| ID_GATEWAY \| |

Tabelas que dependem de EMISSOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GATEWAY](dados_gateway) | \| **GATEWAY** \| **EMISSOR** \| \|---\|---\| \| ID_EMISSOR \| ID_EMISSOR \| |
| [EXECUCAO_GATEWAY](dados_execucao_gateway) | \| **EXECUCAO_GATEWAY** \| **EMISSOR** \| \|---\|---\| \| ID_EMISSOR \| ID_EMISSOR \| |

**Exemplo 1: join com a tabela GATEWAY**

```
select EMISSOR.*, GATEWAY.DESCRICAO
from EMISSOR left outer join GATEWAY on EMISSOR.ID_GATEWAY_SAIDA = GATEWAY.ID_GATEWAY
```

**Exemplo 2: join com a tabela GATEWAY**

```
select EMISSOR.*
from EMISSOR, GATEWAY
where EMISSOR.ID_GATEWAY = GATEWAY.ID_GATEWAY
```
