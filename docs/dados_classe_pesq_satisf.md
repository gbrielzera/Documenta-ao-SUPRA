# CLASSE_PESQ_SATISF

Caminho: Customização > Modelo de dados > Processo > CLASSE_PESQ_SATISF

Uma Classe de Pesquisa de Satisfação define um conjunto de configurações utilizado para geração de Pesquisas de Satisfação enviadas para clientes após finalização de uma Ordem de Serviço. O envio da pesquisa está condicionado ao evento terminador utilizado na definição do processo aplicado em Ordens de Serviço alvo da pesquisa.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_PESQ_SATISF** | Número sequencial gerado automaticamente pelo sistema para Identificar uma ClassePesquisaSatisfacao | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada da ClassePesquisaSatisfacao | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que a ClassePesquisaSatisfacao está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | char(3) | char(3) | Não |
| **PERCENTUAL_ENVIO** | Número percentual entre 0 e 100 que indica a probabilidade de envio de Pesquisa de Satisfação. O valor 0 indica que nenhuma Pesquisa será enviada enquanto 100 estabelece que sempre será enviada Pesquisa de Satisfação | int | number(6,0) | Sim |
| **EXPRESSAO_PERC_ENVIO** | Fórmula que é avaliada para determinar o Percentual de Envio de Pesquisas de Satisfação. Quando preenchido será desconsiderado o campo 'Percentual envio'. | text | clob | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_QUESTAO_GERAL** | Identificador da QuestaoPesquisa associada | int | number(6,0) | Sim |

Tabelas referenciadas por CLASSE_PESQ_SATISF

| **Tabela** | **Colunas de ligação** |
|---|---|
| [QUESTAO_PESQUISA](dados_questao_pesquisa) | \| **QUESTAO_PESQUISA** \| **CLASSE_PESQ_SATISF** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO_GERAL \| |

Tabelas que dependem de CLASSE_PESQ_SATISF

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **CLASSE_PESQ_SATISF** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **CLASSE_PESQ_SATISF** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |
| [PESQUISA](dados_pesquisa) | \| **PESQUISA** \| **CLASSE_PESQ_SATISF** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **CLASSE_PESQ_SATISF** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |
| [QUESTAO_CLASSE_PESQ](dados_questao_classe_pesq) | \| **QUESTAO_CLASSE_PESQ** \| **CLASSE_PESQ_SATISF** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |

**Exemplo 1: join com a tabela QUESTAO_PESQUISA**

```
select CLASSE_PESQ_SATISF.*, QUESTAO_PESQUISA.DESCRICAO
from CLASSE_PESQ_SATISF left outer join QUESTAO_PESQUISA on CLASSE_PESQ_SATISF.ID_QUESTAO_GERAL = QUESTAO_PESQUISA.ID_QUESTAO
```
