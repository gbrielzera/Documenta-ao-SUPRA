# APUR_IND_OS

Caminho: Customização > Modelo de dados > Processo > APUR_IND_OS

Apuração de Indicador de Desempenho associado a Ordens de Serviço

Por se tratar de um tipo herdado de ApuracaoIndicador, a tabela APUR_IND_OS possui uma chave estrangeira apontando para a tabela [APURACAO_INDICADOR](dados_apuracao_indicador).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_INDICADOR** | Identificador do(a) Indicador associado(a) | int | number(6,0) | Não |
| **MES** | Mês | int | number(6,0) | Não |
| **ANO** | Ano | int | number(6,0) | Não |
| **SEQUENCIA** | Sequencia | int | number(6,0) | Não |
| **ID_PLANO_GESTAO** | Identificador do Plano de Gestão proprietário da apuração | int | number(6,0) | Não |
| **ID_ORGAO_CLIENTE** | Identificador do Orgao solicitante | int | number(6,0) | Não |
| **ID_SERVICO** | Identificador do Servico associado | int | number(6,0) | Sim |
| **ID_GRUPO_TRABALHO** | Identificador do GrupoTrabalho associado | int | number(6,0) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_PESSOA** | Identificador da Pessoa associada | int | number(6,0) | Sim |

Tabelas referenciadas por APUR_IND_OS

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SERVICO](dados_servico) | \| **SERVICO** \| **APUR_IND_OS** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **APUR_IND_OS** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **APUR_IND_OS** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |

**Exemplo 1: join com a tabela SERVICO**

```
select APUR_IND_OS.*, SERVICO.DESCRICAO
from APUR_IND_OS left outer join SERVICO on APUR_IND_OS.ID_SERVICO = SERVICO.ID_SERVICO
```
