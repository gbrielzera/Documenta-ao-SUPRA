# APROVADOR_OPERACAO

Caminho: Customização > Modelo de dados > Processo > APROVADOR_OPERACAO

Aprovadores

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OPERACAO_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | int | number(6,0) | Não |
| **ID_PAPEL_APROVADOR** | Identificador do Papel em Processo de Aprovação responsável pela Aprovação | int | number(6,0) | Não |
| **OBRIGATORIO** | Indica que o Aprovador é obrigatório ou opcional. | char(3) | char(3) | Não |
| **HIERARQUIA** | Hierarquia | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por APROVADOR_OPERACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **APROVADOR_OPERACAO** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_APROVADOR \| |
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **APROVADOR_OPERACAO** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

**Exemplo 1: join com a tabela PAPEL_PROCESSO**

```
select APROVADOR_OPERACAO.*, PAPEL_PROCESSO.NOME
from APROVADOR_OPERACAO, PAPEL_PROCESSO
where APROVADOR_OPERACAO.ID_PAPEL_APROVADOR = PAPEL_PROCESSO.ID_PAPEL_PROCESSO
```

**Exemplo 2: join com a tabela OPERACAO_ATIVIDADE**

```
select APROVADOR_OPERACAO.*
from APROVADOR_OPERACAO, OPERACAO_ATIVIDADE
where APROVADOR_OPERACAO.ID_OPERACAO_ATIVIDADE = OPERACAO_ATIVIDADE.ID_OPERACAO_ATIVIDADE
```
