# APONTAMENTO

Caminho: Customização > Modelo de dados > Processo > APONTAMENTO

Apontamento

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_APONTAMENTO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Apontamento | int | number(6,0) | Não |
| **DATA_HORA_APONTAMENTO** | Data e hora do Apontamento | datetime | date | Não |
| **ID_CLASSE_APONTAMENTO** | Identificador do ClasseApontamento associado | int | number(6,0) | Sim |
| **ID_RESPONSAVEL** | Identificador do Responsável pelo Apontamento | int | number(6,0) | Não |
| **CAMPO_INTEIRO_1** | Campo opcional do tipo Inteiro de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | int | number(6,0) | Sim |
| **CAMPO_INTEIRO_2** | Campo opcional do tipo Inteiro de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | int | number(6,0) | Sim |
| **CAMPO_STRING_1** | Campo opcional do tipo String de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | varchar(500) | varchar(500) | Sim |
| **CAMPO_STRING_2** | Campo opcional do tipo String de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | varchar(500) | varchar(500) | Sim |
| **CAMPO_DATAHORA_1** | Campo opcional do tipo Data/Hora de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | datetime | date | Sim |
| **CAMPO_DATAHORA_2** | Campo opcional do tipo Data/Hora de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | datetime | date | Sim |
| **CAMPO_DECIMAL_1** | Campo opcional do tipo Decimal de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | decimal(15,2) | number(15,2) | Sim |
| **CAMPO_DECIMAL_2** | Campo opcional do tipo Decimal de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | decimal(15,2) | number(15,2) | Sim |
| **CAMPO_BOOLEANO_1** | Campo opcional do tipo Booleano de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento. | char(3) | char(3) | Sim |
| **CAMPO_BOOLEANO_2** | Campo opcional do tipo Booleano de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento. | char(3) | char(3) | Sim |
| **SITUACAO** | Situação do Apontamento | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas referenciadas por APONTAMENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_APONTAMENTO](dados_classe_apontamento) | \| **CLASSE_APONTAMENTO** \| **APONTAMENTO** \| \|---\|---\| \| ID_CLASSE_APONTAMENTO \| ID_CLASSE_APONTAMENTO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **APONTAMENTO** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |

Tabelas que dependem de APONTAMENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [MOTIVO_APONTAMENTO](dados_motivo_apontamento) | \| **MOTIVO_APONTAMENTO** \| **APONTAMENTO** \| \|---\|---\| \| ID_APONTAMENTO \| ID_APONTAMENTO \| |

**Exemplo 1: join com a tabela CLASSE_APONTAMENTO**

```
select APONTAMENTO.*, CLASSE_APONTAMENTO.DESCRICAO
from APONTAMENTO left outer join CLASSE_APONTAMENTO on APONTAMENTO.ID_CLASSE_APONTAMENTO = CLASSE_APONTAMENTO.ID_CLASSE_APONTAMENTO
```
