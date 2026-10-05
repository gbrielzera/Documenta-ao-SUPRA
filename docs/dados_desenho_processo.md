# DESENHO_PROCESSO

Caminho: Customização > Modelo de dados > Processo > DESENHO_PROCESSO

Desenho do Processo a ser executado. Permite que uma Etapa do Processo possa armazenar versões do Processo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_DESENHO_PROCESSO** | Número sequencial gerado automaticamente pelo sistema para Identificar um DesenhoProcesso | int | number(6,0) | Não |
| **ATIVO** | Indica que o DesenhoProcesso está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | char(3) | char(3) | Não |
| **VERSAO** | Número incremental indicando a versão do Desenho de Processo | int | number(6,0) | Não |
| **DATA_CRIACAO** | Data de criação da Modelagem | datetime | date | Não |
| **DATA_ATIVACAO** | Data em que o Desenho foi ativado no sistema. | datetime | date | Sim |
| **DATA_DESATIVACAO** | Data em que o modelo foi desativado. | datetime | date | Sim |
| **COMENTARIO** | Comentários sobre a Versão. | varchar(500) | varchar(500) | Sim |
| **ID_PROCESSO** | Identificador do Processo | int | number(6,0) | Não |

Tabelas referenciadas por DESENHO_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PROCESSO](dados_processo) | \| **PROCESSO** \| **DESENHO_PROCESSO** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |

Tabelas que dependem de DESENHO_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **DESENHO_PROCESSO** \| \|---\|---\| \| ID_DESENHO_PROCESSO \| ID_DESENHO_PROCESSO \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **DESENHO_PROCESSO** \| \|---\|---\| \| ID_DESENHO_PROC_INI \| ID_DESENHO_PROCESSO \| |
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **DESENHO_PROCESSO** \| \|---\|---\| \| ID_DESENHO_PROCESSO \| ID_DESENHO_PROCESSO \| |
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **DESENHO_PROCESSO** \| \|---\|---\| \| ID_DESENHO_PROCESSO \| ID_DESENHO_PROCESSO \| |

**Exemplo 1: join com a tabela PROCESSO**

```
select DESENHO_PROCESSO.*
from DESENHO_PROCESSO, PROCESSO
where DESENHO_PROCESSO.ID_PROCESSO = PROCESSO.ID_PROCESSO
```
