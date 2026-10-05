# SERVICO

Caminho: Customização > Modelo de dados > Processo > SERVICO

Um Serviço pode ser definido como um sistema composto por Tecnologia, Facilidades, Processos e Pessoas que habilitam um processo de negócio.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SERVICO** | Identificador do Serviço | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Produto | varchar(500) | varchar(500) | Não |
| **SIGLA** | Nome resumido do Serviço | varchar(50) | varchar(50) | Não |
| **REFERENCIA** | Texto de Referência para utilização do Produto | text | clob | Sim |
| **ID_TECNICO_RESPONSAVEL** | Identificador do Solucionador responsável | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO_CLIENTE** | Descritivo apresentado para Cliente no Catálogo de Serviços. Se não for preenchido é utilizado a Descrição padrão do Serviço | varchar(500) | varchar(500) | Sim |
| **ID_CLASSE_SERVICO** | Identificador do tipo de Serviço associado | int | number(6,0) | Não |
| **ID_RESPONSAVEL_AREA** | Identificador da Pessoa responsável pela área de negócio cliente do Serviço | int | number(6,0) | Não |
| **PRE_REQ_DEPEND** | Pré-requisitos ou Dependências para o perfeito funcionamento do Serviço. | text | clob | Sim |
| **BENEFICIOS** | Benefícios oferecidos pelo Serviço | text | clob | Sim |
| **DISPONIBILIDADE** | Disponibilidade que pode ser esperada pelo Cliente incluindo horários. | text | clob | Sim |
| **PROG_MANUTENCAO** | Detalhes sobre a Programação de Manutenção do Serviço incluíndo janelas semanais de paradas. | text | clob | Sim |
| **SOL_SERVICOS** | Detalhes sobre procedimento de abertura de Chamados. Se não for preenchido é estabelecido o procedimento padrão por meio do Catálogo de Serviços. | varchar(500) | varchar(500) | Sim |
| **ID_FATOR_PRIORIDADE** | Identificador do(a) FatorPrioridade associado(a) | int | number(6,0) | Sim |
| **REDEF_PAPEIS_ITEM** | Define o comportamento da rotina de resolução de Atores quando existirem redefinições de Papéis em Itens de Configuração associados em uma Ordem de Serviço. | varchar(250) | varchar(250) | Não |
| **DISP_AA** | Configuração da disponibilidade do Serviço na aplicação de Autoatendimento. Alguns Serviços são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente. | char(3) | char(3) | Não |
| **ATIVO** | Define se o Serviço está Ativo. Por padrão o valor inicial é sempre Verdadeiro. | char(3) | char(3) | Não |

Tabelas referenciadas por SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **SERVICO** \| \|---\|---\| \| ID_PESSOA \| ID_TECNICO_RESPONSAVEL \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **SERVICO** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL_AREA \| |
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **SERVICO** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **SERVICO** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |

Tabelas que dependem de SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [APUR_IND_OS](dados_apur_ind_os) | \| **APUR_IND_OS** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [APUR_IND_PESQ](dados_apur_ind_pesq) | \| **APUR_IND_PESQ** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [REST_SERVICO](dados_rest_servico) | \| **REST_SERVICO** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [REST_SERV_ANEXO](dados_rest_serv_anexo) | \| **REST_SERV_ANEXO** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [REST_SERV_APROV](dados_rest_serv_aprov) | \| **REST_SERV_APROV** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [COMP_SERVICO](dados_comp_servico) | \| **COMP_SERVICO** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [ATOR_SERVICO](dados_ator_servico) | \| **ATOR_SERVICO** \| **SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |

**Exemplo 1: join com a tabela FATOR_PRIORIDADE**

```
select SERVICO.*, FATOR_PRIORIDADE.DESCRICAO
from SERVICO left outer join FATOR_PRIORIDADE on SERVICO.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```
