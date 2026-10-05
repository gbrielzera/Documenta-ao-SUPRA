# REL_ATIVIDADE

Caminho: Customização > Modelo de dados > Processo > REL_ATIVIDADE

Relatório de apoio utilizado na execução de alguma tarefa de processo ou relatório anexado no envio de emails configurados no processo como eventos intermediários.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REPORT** | Identificador do relatório de apoio ou utilizado como anexo em evento de mensagem. | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Identificador da tarefa de processo ou evento intermediário que contém a regra de relatório. | int | number(6,0) | Não |
| **FORMATO_EXP** | Formato do arquivo gerado pelo relatório e que será anexado no email. | varchar(250) | varchar(250) | Não |
| **DISP_AA** | Indica que o relatório estará disponível na página de consulta de Ordens de Serviço do sistema de Autoatendimento. O relatório estará acessível por um link que exibirá o conteúdo em outra página web. | char(3) | char(3) | Não |

Tabelas referenciadas por REL_ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_REPORT](dados_sv_report) | \| **SV_REPORT** \| **REL_ATIVIDADE** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **REL_ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

Tabelas que dependem de REL_ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [REL_ATIVIDADE_PARAM](dados_rel_atividade_param) | \| **REL_ATIVIDADE_PARAM** \| **REL_ATIVIDADE** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela ATIVIDADE**

```
select REL_ATIVIDADE.*
from REL_ATIVIDADE, ATIVIDADE
where REL_ATIVIDADE.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```
