# PESQUISA

Caminho: Customização > Modelo de dados > Processo > PESQUISA

Uma Pesquisa de Satisfação é composta por um formulário enviado para Clientes após finalização de uma Ordem de Serviço. As respostas coletadas destas pesquisas podem ser utilizadas para construção de Indicadores de Desempenho - KPI's.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PESQUISA** | Identificador da Pesquisa de Satisfação. | int | number(6,0) | Não |
| **ASSUNTO** | Assunto abordado pela Pesquisa de Satisfação | varchar(500) | varchar(500) | Não |
| **DATA_HORA_CRIACAO** | Data e hora que a Pesquisa de Satisfação foi gerada. | datetime | date | Não |
| **SITUACAO** | Indica a Situação da Pesquisa de Satisfação. | varchar(250) | varchar(250) | Não |
| **MOTIVO_CANCELAMENTO** | Motivo de Cancelamento da Pesquisa | varchar(500) | varchar(500) | Sim |
| **ID_RESP_CANCELAMENTO** | Identificador da Pessoa associada | int | number(6,0) | Sim |
| **OS** | Identificador do OrdemServico associado | int | number(6,0) | Não |
| **COMENTARIO_AVALIADOR** | Comentário gravado pelo Avalidador no instante em que a Pesquisa é respondida | varchar(500) | varchar(500) | Sim |
| **ESCORE_GERAL** | Avaliação geral | int | number(6,0) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_AVALIADOR** | Identificador do Avaliador da Pesquisa | int | number(6,0) | Não |
| **DATA_HORA_RESPOSTA** | Data e hora em que foi respondida a Pesquisa | datetime | date | Sim |
| **ID_CLASSE_PESQ_SATISF** | Identificador do ClassePesquisaSatisfacao associado | int | number(6,0) | Sim |
| **ID_QUESTAO_GERAL** | Identificador da QuestaoPesquisa associada | int | number(6,0) | Sim |
| **RESP_AUTO_ATEND** | Indica que a Pesquisa de Satisfação foi respondida pelo Cliente utilizando a aplicação de Autoatendimento. | char(3) | char(3) | Sim |

Tabelas referenciadas por PESQUISA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PESQUISA** \| \|---\|---\| \| ID_PESSOA \| ID_RESP_CANCELAMENTO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PESQUISA** \| \|---\|---\| \| ID_PESSOA \| ID_AVALIADOR \| |
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **PESQUISA** \| \|---\|---\| \|  \| OS \| |
| [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf) | \| **CLASSE_PESQ_SATISF** \| **PESQUISA** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |
| [QUESTAO_PESQUISA](dados_questao_pesquisa) | \| **QUESTAO_PESQUISA** \| **PESQUISA** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO_GERAL \| |

Tabelas que dependem de PESQUISA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM_PESQUISA](dados_item_pesquisa) | \| **ITEM_PESQUISA** \| **PESQUISA** \| \|---\|---\| \| ID_PESQUISA \| ID_PESQUISA \| |

**Exemplo 1: join com a tabela CLASSE_PESQ_SATISF**

```
select PESQUISA.*, CLASSE_PESQ_SATISF.DESCRICAO
from PESQUISA left outer join CLASSE_PESQ_SATISF on PESQUISA.ID_CLASSE_PESQ_SATISF = CLASSE_PESQ_SATISF.ID_CLASSE_PESQ_SATISF
```

**Exemplo 2: join com a tabela QUESTAO_PESQUISA**

```
select PESQUISA.*, QUESTAO_PESQUISA.DESCRICAO
from PESQUISA left outer join QUESTAO_PESQUISA on PESQUISA.ID_QUESTAO_GERAL = QUESTAO_PESQUISA.ID_QUESTAO
```
