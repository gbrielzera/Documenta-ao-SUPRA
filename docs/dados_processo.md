# PROCESSO

Caminho: Customização > Modelo de dados > Processo > PROCESSO

Um Processo é composto por uma coleção de rotinas denominadas Subprocessos. As rotinas de um Processo são especificadas por uma linguagem gráfica de mercado denominada BPMN - Business Process Management Notation. A execução de um Processo é realizada por Ordens de Serviços que são ocorrências solicitadas por um Cliente, sob responsabilidade de um Solucionador e com um Serviço associado.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PROCESSO** | Identificador do Processo | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Processo. Este descritivo é utilizado para nomear pastas no repositório de arquivo e por este motivo não pode conter os seguintes caracteres \\ / : > ? * " | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Tipo de Serviço está Ativo. Quando ativo o Tipo é visível em formulários de entrada de dados para Ordens de Serviço ou Consultas diversas | char(3) | char(3) | Não |
| **SIGLA** | Nome abreviado para o Processo. Este identificador pode ser utilizado por scripts para automatização de processos. | varchar(50) | varchar(50) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **CLASSE_NEGOCIO** | Classe de Negócio utilizada pelo Processo. | varchar(250) | varchar(250) | Não |
| **ID_FATOR_PRIORIDADE** | Identificador do(a) FatorPrioridade associado(a) | int | number(6,0) | Sim |
| **EXP_PASTAS_ANEXOS** | Fórmula para caminho de pastas de Itens de Configuração anexados em Ocorrências | varchar(500) | varchar(500) | Sim |
| **EXP_PASTAS_APROV** | Fórmula para caminho de pastas de Itens de Configuração para aprovação em Ocorrências | varchar(500) | varchar(500) | Sim |
| **ID_MACRO_PROCESSO** | Identificador do MacroProcesso associado | int | number(6,0) | Não |

Tabelas referenciadas por PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **PROCESSO** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [MACRO_PROCESSO](dados_macro_processo) | \| **MACRO_PROCESSO** \| **PROCESSO** \| \|---\|---\| \| ID_MACRO_PROCESSO \| ID_MACRO_PROCESSO \| |

Tabelas que dependem de PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [MENSAGEM_EVENTO](dados_mensagem_evento) | \| **MENSAGEM_EVENTO** \| **PROCESSO** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **PROCESSO** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **PROCESSO** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |
| [DESENHO_PROCESSO](dados_desenho_processo) | \| **DESENHO_PROCESSO** \| **PROCESSO** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |

**Exemplo 1: join com a tabela FATOR_PRIORIDADE**

```
select PROCESSO.*, FATOR_PRIORIDADE.DESCRICAO
from PROCESSO left outer join FATOR_PRIORIDADE on PROCESSO.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```

**Exemplo 2: join com a tabela MACRO_PROCESSO**

```
select PROCESSO.*, MACRO_PROCESSO.DESCRICAO
from PROCESSO, MACRO_PROCESSO
where PROCESSO.ID_MACRO_PROCESSO = MACRO_PROCESSO.ID_MACRO_PROCESSO
```
