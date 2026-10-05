# INDICADOR

Caminho: Customização > Modelo de dados > Processo > INDICADOR

Um Indicador de Desempenho, também conhecido como KPI (Key Performance Indicator), define uma medição realizada sobre a execução de Processos ou base de Ativos. Indicadores representam uma importante ferramenta para monitoramento e gerenciamento dos Serviços.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_INDICADOR** | Número sequencial gerado automaticamente pelo sistema para Identificar um Indicador. Este número não pode ser modificado pelo usuário. | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente a finalizada de um Indicador de Desempenho. Este texto é utilizado na publicação do Indicador na página Executive Dashboard da tela Workspace. | varchar(500) | varchar(500) | Não |
| **SENTIDO_MELHOR** | Indica o melhor desempenho para um valor apurado em relação a Meta estipulada para o Indicador. | varchar(250) | varchar(250) | Não |
| **EXPRESSAO_SELECAO** | Fórmula para seleção de registros baseados no Provedor do Indicador. Indicadores do tipo Percentual devem obrigatoriamente definir uma fórmula de seleção. | varchar(500) | varchar(500) | Sim |
| **EXPRESSAO_VALOR** | Fórmula para determinar o Valor do Indicador. Se não for preenchido é assumida a Projeção de Contagem de registros que atendam Fórmula de Seleção. A Fórmula de Valor deve ser utilizada em conjunto com a função de Agregação para determinar o valor final de apuração do Indicador. | varchar(500) | varchar(500) | Sim |
| **AGREGACAO** | Função de agregação utilizada para apuração de Indicador. | varchar(250) | varchar(250) | Não |
| **ID_GRUPO_INDICADOR** | Identificador do(a) GrupoIndicador associado(a) | int | number(6,0) | Não |
| **ID_PROCESSO** | Identificador do Processo associado | int | number(6,0) | Sim |
| **PROVEDOR** | Banco de dados utilizado para apuração do Indicador. | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **OS_FILTRO_ABERTA** | Seleciona Ordens de Serviço Abertas no Período de apuração do Indicador | char(3) | char(3) | Não |
| **OS_FILTRO_FIN_SUC** | Seleciona Ordens de Serviço Finalizadas como Sucesso no Período de apuração do Indicador. Para determinar a finalização no período é utilizada a Data/hora de Execução de Mudança. | char(3) | char(3) | Não |
| **OS_FILTRO_FIN_FALHA** | Seleciona Ordens de Serviço Finalizadas como Falha no Período de apuração do Indicador. | char(3) | char(3) | Não |
| **OS_FILTRO_CAN** | Seleciona Ordens de Serviço Canceladas no Período de apuração do Indicador | char(3) | char(3) | Não |
| **TIPO_APURACAO_PESQUISA** | Tipo de Apuração para Pesquisas de Satisfação. | varchar(250) | varchar(250) | Sim |
| **ID_CLASSE_PESQ_SATISF** | Identificador do ClassePesquisaSatisfacao associado | int | number(6,0) | Sim |
| **OS_FILTRO_FIN_NREAL** | Seleciona Ordens de Serviço Finalizadas como Não-realizada no Período de apuração do Indicador. | char(3) | char(3) | Não |
| **PESQ_FILTRO_CONC** | Seleciona Pesquisas de Satisfação respondidas por Clientes | char(3) | char(3) | Não |
| **PESQ_FILTRO_CAN** | Seleciona Pesquisas de Satisfação canceladas | char(3) | char(3) | Não |
| **PESQ_FILTRO_AN** | Seleciona Pesquisas de Satisfação não respondidas | char(3) | char(3) | Não |
| **CODIGO** | Código de identificação do Indicador | varchar(100) | varchar(100) | Não |
| **REFER_CALCULO** | Texto explicativo sobre como o Indicador é calculado. | text | clob | Não |
| **FORM_FIL_COMP** | Fórmula para filtro complementar | varchar(500) | varchar(500) | Sim |
| **FORM_RESP** | Fórmula para recuperação responsável por uma Ordem de Serviço ou Pesquisa de Satisfação. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por INDICADOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_INDICADOR](dados_grupo_indicador) | \| **GRUPO_INDICADOR** \| **INDICADOR** \| \|---\|---\| \| ID_GRUPO_INDICADOR \| ID_GRUPO_INDICADOR \| |
| [PROCESSO](dados_processo) | \| **PROCESSO** \| **INDICADOR** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |
| [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf) | \| **CLASSE_PESQ_SATISF** \| **INDICADOR** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |

Tabelas que dependem de INDICADOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APURACAO_INDICADOR](dados_apuracao_indicador) | \| **APURACAO_INDICADOR** \| **INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |
| [INDICADOR_PLANO](dados_indicador_plano) | \| **INDICADOR_PLANO** \| **INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |
| [CLASSE_CONF_INDICADOR](dados_classe_conf_indicador) | \| **CLASSE_CONF_INDICADOR** \| **INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |
| [CLASSE_SUBPROC_INDICADOR](dados_classe_subproc_indicador) | \| **CLASSE_SUBPROC_INDICADOR** \| **INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |
| [GRUPO_QUESTAO_INDICADOR](dados_grupo_questao_indicador) | \| **GRUPO_QUESTAO_INDICADOR** \| **INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |

**Exemplo 1: join com a tabela GRUPO_INDICADOR**

```
select INDICADOR.*, GRUPO_INDICADOR.DESCRICAO
from INDICADOR, GRUPO_INDICADOR
where INDICADOR.ID_GRUPO_INDICADOR = GRUPO_INDICADOR.ID_GRUPO_INDICADOR
```

**Exemplo 2: join com a tabela PROCESSO**

```
select INDICADOR.*, PROCESSO.DESCRICAO
from INDICADOR left outer join PROCESSO on INDICADOR.ID_PROCESSO = PROCESSO.ID_PROCESSO
```

**Exemplo 3: join com a tabela CLASSE_PESQ_SATISF**

```
select INDICADOR.*, CLASSE_PESQ_SATISF.DESCRICAO
from INDICADOR left outer join CLASSE_PESQ_SATISF on INDICADOR.ID_CLASSE_PESQ_SATISF = CLASSE_PESQ_SATISF.ID_CLASSE_PESQ_SATISF
```
