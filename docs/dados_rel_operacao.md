# REL_OPERACAO

Caminho: Customização > Modelo de dados > Processo > REL_OPERACAO

Relatórios envolvidos em aprovações ou utilizados para geração de arquivos anexados na ocorrência.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REPORT** | Identificador do relatório que será utilizado na aprovação. | int | number(6,0) | Não |
| **ID_OPERACAO_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | int | number(6,0) | Não |
| **FORMATO_EXP** | Formato do arquivo que será gerado pelo relatório e anexado na ocorrência. | varchar(250) | varchar(250) | Não |
| **ROTULO_LINK** | Texto utilizado no link disponível na página de aprovação da aplicação de Autoatendimento. Ao clicar neste link será exibido em uma nova página o conteúdo do relatório. Se não for preenchido então será utilizado o próprio título do relatório. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por REL_OPERACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **REL_OPERACAO** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| |
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **REL_OPERACAO** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

Tabelas que dependem de REL_OPERACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [REL_OPERACAO_PARAM](dados_rel_operacao_param) | \| **REL_OPERACAO_PARAM** \| **REL_OPERACAO** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

**Exemplo 1: join com a tabela OPERACAO_ATIVIDADE**

```
select REL_OPERACAO.*
from REL_OPERACAO, OPERACAO_ATIVIDADE
where REL_OPERACAO.ID_OPERACAO_ATIVIDADE = OPERACAO_ATIVIDADE.ID_OPERACAO_ATIVIDADE
```
