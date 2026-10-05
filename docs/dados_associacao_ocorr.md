# ASSOCIACAO_OCORR

Caminho: Customização > Modelo de dados > Processo > ASSOCIACAO_OCORR

Estabelece Associações entre Ocorrências de Processo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORR_FONTE** | Identificador da Ocorrência Fonte da Associação. | int | number(6,0) | Não |
| **ID_OCORR_ALVO** | Identificador da Ocorrência Alvo na Associação. | int | number(6,0) | Não |
| **ID_ASSOCIACAO** | Identificador do Associacao associado | int | number(6,0) | Não |
| **DATA_HORA_ASSOC** | Data e hora em que foi estabelecida a Associação. | datetime | date | Não |
| **ID_AUTOR** | Identificador da Pessoa que estabeleceu a Associação. | int | number(6,0) | Não |
| **ID_ATIVIDADE_GER** | Identificador da Atividade do tipo Subprocesso ou Link final que gerou a associação. | int | number(6,0) | Sim |

Tabelas referenciadas por ASSOCIACAO_OCORR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ASSOCIACAO_OCORR** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORR_FONTE \| |
| [ASSOCIACAO](dados_associacao) | \| **ASSOCIACAO** \| **ASSOCIACAO_OCORR** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ASSOCIACAO_OCORR** \| \|---\|---\| \| ID_PESSOA \| ID_AUTOR \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ASSOCIACAO_OCORR** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORR_ALVO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **ASSOCIACAO_OCORR** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE_GER \| |

**Exemplo 1: join com a tabela ASSOCIACAO**

```
select ASSOCIACAO_OCORR.*, ASSOCIACAO.FRASE_ASSOC
from ASSOCIACAO_OCORR, ASSOCIACAO
where ASSOCIACAO_OCORR.ID_ASSOCIACAO = ASSOCIACAO.ID_ASSOCIACAO
```
