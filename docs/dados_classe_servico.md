# CLASSE_SERVICO

Caminho: Customização > Modelo de dados > Processo > CLASSE_SERVICO

Um Tipo de Serviço define classificações para Serviços. Registros deste cadastro são utilizados em diversas configurações do sistema incluindo durante a definição de Processos.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_SERVICO** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Classe de Servico | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Tipo de Serviço | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Tipo de Serviço está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_FATOR_PRIORIDADE** | Identificador do Fator de Prioridade utilizado para priorizar uma ocorrência. Deve ser utilizado em conjunto com um Método de Priorização. | int | number(6,0) | Sim |
| **SIGLA** | Nome resumido (código) que identifica unicamente um Tipo de Item de Configuração | varchar(500) | varchar(500) | Não |
| **ID_GRUPO_SERVICO** | Identificador do Grupo de Servicos associado | int | number(6,0) | Sim |

Tabelas referenciadas por CLASSE_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **CLASSE_SERVICO** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [GRUPO_SERVICO](dados_grupo_servico) | \| **GRUPO_SERVICO** \| **CLASSE_SERVICO** \| \|---\|---\| \| ID_GRUPO_SERVICO \| ID_GRUPO_SERVICO \| |

Tabelas que dependem de CLASSE_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SERVICO](dados_servico) | \| **SERVICO** \| **CLASSE_SERVICO** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [REST_SERVICO](dados_rest_servico) | \| **REST_SERVICO** \| **CLASSE_SERVICO** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [REST_SERV_ANEXO](dados_rest_serv_anexo) | \| **REST_SERV_ANEXO** \| **CLASSE_SERVICO** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [REST_SERV_APROV](dados_rest_serv_aprov) | \| **REST_SERV_APROV** \| **CLASSE_SERVICO** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |

**Exemplo 1: join com a tabela FATOR_PRIORIDADE**

```
select CLASSE_SERVICO.*, FATOR_PRIORIDADE.DESCRICAO
from CLASSE_SERVICO left outer join FATOR_PRIORIDADE on CLASSE_SERVICO.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```

**Exemplo 2: join com a tabela GRUPO_SERVICO**

```
select CLASSE_SERVICO.*, GRUPO_SERVICO.DESCRICAO
from CLASSE_SERVICO left outer join GRUPO_SERVICO on CLASSE_SERVICO.ID_GRUPO_SERVICO = GRUPO_SERVICO.ID_GRUPO_SERVICO
```
