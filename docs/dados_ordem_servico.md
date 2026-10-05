# ORDEM_SERVICO

Caminho: Customização > Modelo de dados > Processo > ORDEM_SERVICO

Uma Ordem de Serviço é uma ocorrência de Processo em atendimento a uma solicitação de serviço de Tecnologia da Informação. Ordens de Serviço podem ser abertas na aplicação de Autoatendimento ou na transação Workspace do sistema Supravizio.

Por se tratar de um tipo herdado de Ocorrencia, a tabela ORDEM_SERVICO possui uma chave estrangeira apontando para a tabela [OCORRENCIA](dados_ocorrencia).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | int | number(6,0) | Não |
| **DESCRICAO_DETALHADA** | Descrição detalhada da solicitação do Cliente | text | clob | Sim |
| **TELEFONE_CLIENTE** | Telefone de contato do Cliente | varchar(500) | varchar(500) | Sim |
| **CELULAR_CLIENTE** | Telefone celular para contato com o Cliente | varchar(500) | varchar(500) | Sim |
| **SEGUNDO_CONTATO** | Segunda pessoa para contato com o Solicitante da Ordem de Serviço | varchar(500) | varchar(500) | Sim |
| **TELEFONE_SEGUNDO_CONTATO** | Telefone do Segundo contato | varchar(500) | varchar(500) | Sim |
| **DATA_HORA_EXEC_MUDANCA** | Data/hora em que foi Executada a Mudança o ambiente | datetime | date | Sim |
| **ID_SERVICO** | Identificador do Serviço associado | int | number(6,0) | Não |
| **ID_FAVORECIDO** | Identificador do Favorecido | int | number(6,0) | Não |
| **CAUSA** | Causa | varchar(500) | varchar(500) | Sim |
| **SOLUCAO** | Solução | varchar(500) | varchar(500) | Sim |
| **NUM_REF_FORNECEDOR** | Número de referência para Chamado registrado no Fornecedor do Serviço | varchar(500) | varchar(500) | Sim |
| **CONTATO_FORNECEDOR** | Informações de contato no Forncedor incluindo solucionador responsável, email e telefone quando possível. | varchar(500) | varchar(500) | Sim |
| **COMENTARIO_CONTATO** | Comentários gerais sobre contatos com o Cliente | varchar(500) | varchar(500) | Sim |
| **SIT_ENVIO_PESQ** | Situação quanto ao Envio de Pesquisa de Satisfação | varchar(250) | varchar(250) | Não |
| **ID_CLASSE_PESQ_SATISF** | Identificador do ClassePesquisaSatisfacao associado | int | number(6,0) | Sim |
| **ID_GRAU_PRIOR_CALC** | Identificador do Grau da Prioridade inicialmente definido para a Ordem de Serviço. | int | number(6,0) | Sim |
| **ID_GRAU_PRIOR_SELEC** | Identificador do Grau de Prioridade selecionado | int | number(6,0) | Sim |
| **PESO_PRIOR_CALC** | Peso prioridade calculado | int | number(6,0) | Sim |
| **PESO_PRIOR_SELEC** | Peso prioridade selecionado | int | number(6,0) | Sim |
| **VAL_VARIAVEIS_PRIOR** | Valores utilizados nas variáveis de Priorização. | varchar(500) | varchar(500) | Sim |
| **ID_NIVEL_SLA** | Identificador da NivelSLA associada | int | number(6,0) | Sim |
| **TEMPO_SLA** | Tempo em minutos para ANS. | int | number(6,0) | Sim |
| **EXP_TEMPO_SLA** | Indica que o tempo determinado para entrega do serviço foi vencido. Todos os níveis tiveram o seu tempo vencido sem que ocorresse resolução do incidente ou atendimento. | char(3) | char(3) | Sim |
| **ID_METODO_PRIORIZACAO** | Identificador do MetodoPriorizacao associado | int | number(6,0) | Sim |
| **USUARIO_LOG_AA** | Usuário reconhecido pela aplicação de Autoatendimento. Este campo só é preenchido quando a Ordem de Serviço é aberta na aplicação de Autoatendimento. | varchar(100) | varchar(100) | Sim |
| **SINTOMA_ANALISADO** | Sintoma analisado por um Solucionador. Este texto é utilizado em Incidentes para associação de Incidentes pelo próprio Cliente no site de Autoatendimento. | varchar(500) | varchar(500) | Sim |
| **JUSTIFICATIVA** | Justificativa fornecida pelo Cliente para atendimento do Serviço | varchar(500) | varchar(500) | Sim |
| **RESP_LEITURA** | Indica que o responsável atual pela Ordem de Serviço leu o conteúdo da Ordem de Serviço (visualizou na tela de edição). | char(3) | char(3) | Não |
| **HARDWARE_AA** | Computador identificado pela aplicação de Autoatendimento no instante da abertura do chamado | varchar(100) | varchar(100) | Sim |
| **ORIGEM** | Origem da Ordem de Serviço: Workspace, Autoatendimento ou Eventos do Processo | varchar(250) | varchar(250) | Não |
| **ID_ITEM_SLA** | Identificador do critério de atendimento escolhido no Acordo de Nível de Serviço estabelecido com a área do Cliente | int | number(6,0) | Sim |
| **TEMPO_INTER_SLA** | Tempo total de interrupção da contagem de tempo do Acordo de Nível de Serviço. Este tempo é mantido pela inclusão/aprovação de registros de interrupção de ANS definidos no Acordo de Nível de Serviço. | int | number(6,0) | Sim |
| **VALOR_CHARGE_BACK** | Valor para cobrança pela rotina de Charge-back. | decimal(15,2) | number(15,2) | Sim |
| **ID_CONTRATO** | Identificador do Contrato associado | int | number(6,0) | Sim |
| **ID_CATEGORIA** | Identificador da Categoria atribuída manualmente a Ordem de Serviço. | int | number(6,0) | Sim |

Tabelas referenciadas por ORDEM_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SERVICO](dados_servico) | \| **SERVICO** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_PESSOA \| ID_FAVORECIDO \| |
| [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf) | \| **CLASSE_PESQ_SATISF** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |
| [GRAU_PRIORIDADE](dados_grau_prioridade) | \| **GRAU_PRIORIDADE** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_GRAU_PRIORIDADE \| ID_GRAU_PRIOR_CALC \| |
| [GRAU_PRIORIDADE](dados_grau_prioridade) | \| **GRAU_PRIORIDADE** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_GRAU_PRIORIDADE \| ID_GRAU_PRIOR_SELEC \| |
| [NIVEL_SLA](dados_nivel_sla) | \| **NIVEL_SLA** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_NIVEL_SLA \| ID_NIVEL_SLA \| |
| [METODO_PRIORIZACAO](dados_metodo_priorizacao) | \| **METODO_PRIORIZACAO** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |
| [ITEM_SLA](dados_item_sla) | \| **ITEM_SLA** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_ITEM_SLA \| ID_ITEM_SLA \| |
| [CONTRATO](dados_contrato) | \| **CONTRATO** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| |
| [CATEGORIA](dados_categoria) | \| **CATEGORIA** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_CATEGORIA \| ID_CATEGORIA \| |

Tabelas que dependem de ORDEM_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESQUISA](dados_pesquisa) | \| **PESQUISA** \| **ORDEM_SERVICO** \| \|---\|---\| \| OS \|  \| |
| [SLA_OS](dados_sla_os) | \| **SLA_OS** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_OCORRENCIA \|  \| |
| [INTER_SLA](dados_inter_sla) | \| **INTER_SLA** \| **ORDEM_SERVICO** \| \|---\|---\| \| ID_OCORRENCIA \|  \| |

**Exemplo 1: join com a tabela SERVICO**

```
select ORDEM_SERVICO.*, SERVICO.DESCRICAO
from ORDEM_SERVICO, SERVICO
where ORDEM_SERVICO.ID_SERVICO = SERVICO.ID_SERVICO
```

**Exemplo 2: join com a tabela CLASSE_PESQ_SATISF**

```
select ORDEM_SERVICO.*, CLASSE_PESQ_SATISF.DESCRICAO
from ORDEM_SERVICO left outer join CLASSE_PESQ_SATISF on ORDEM_SERVICO.ID_CLASSE_PESQ_SATISF = CLASSE_PESQ_SATISF.ID_CLASSE_PESQ_SATISF
```

**Exemplo 3: join com a tabela GRAU_PRIORIDADE**

```
select ORDEM_SERVICO.*, GRAU_PRIORIDADE.DESCRICAO
from ORDEM_SERVICO left outer join GRAU_PRIORIDADE on ORDEM_SERVICO.ID_GRAU_PRIOR_CALC = GRAU_PRIORIDADE.ID_GRAU_PRIORIDADE
```

**Exemplo 4: join com a tabela GRAU_PRIORIDADE**

```
select ORDEM_SERVICO.*, GRAU_PRIORIDADE.DESCRICAO
from ORDEM_SERVICO left outer join GRAU_PRIORIDADE on ORDEM_SERVICO.ID_GRAU_PRIOR_SELEC = GRAU_PRIORIDADE.ID_GRAU_PRIORIDADE
```

**Exemplo 5: join com a tabela NIVEL_SLA**

```
select ORDEM_SERVICO.*, NIVEL_SLA.SEQUENCIAL
from ORDEM_SERVICO left outer join NIVEL_SLA on ORDEM_SERVICO.ID_NIVEL_SLA = NIVEL_SLA.ID_NIVEL_SLA
```

**Exemplo 6: join com a tabela METODO_PRIORIZACAO**

```
select ORDEM_SERVICO.*, METODO_PRIORIZACAO.DESCRICAO
from ORDEM_SERVICO left outer join METODO_PRIORIZACAO on ORDEM_SERVICO.ID_METODO_PRIORIZACAO = METODO_PRIORIZACAO.ID_METODO_PRIORIZACAO
```

**Exemplo 7: join com a tabela CATEGORIA**

```
select ORDEM_SERVICO.*, CATEGORIA.DESCRICAO
from ORDEM_SERVICO left outer join CATEGORIA on ORDEM_SERVICO.ID_CATEGORIA = CATEGORIA.ID_CATEGORIA
```
