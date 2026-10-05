# ASSOCIACAO_SUBPROCESSO

Caminho: Customização > Modelo de dados > Processo > ASSOCIACAO_SUBPROCESSO

Indica uma associação entre uma atividade do tipo Link Inicial de um subprocesso específico e uma Associação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Atividade | int | number(6,0) | Não |
| **ID_ASSOCIACAO** | Identificador do Associacao associado | int | number(6,0) | Não |

Tabelas referenciadas por ASSOCIACAO_SUBPROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ASSOCIACAO](dados_associacao) | \| **ASSOCIACAO** \| **ASSOCIACAO_SUBPROCESSO** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **ASSOCIACAO_SUBPROCESSO** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela ASSOCIACAO**

```
select ASSOCIACAO_SUBPROCESSO.*, ASSOCIACAO.FRASE_ASSOC
from ASSOCIACAO_SUBPROCESSO, ASSOCIACAO
where ASSOCIACAO_SUBPROCESSO.ID_ASSOCIACAO = ASSOCIACAO.ID_ASSOCIACAO
```

**Exemplo 2: join com a tabela ATIVIDADE**

```
select ASSOCIACAO_SUBPROCESSO.*
from ASSOCIACAO_SUBPROCESSO, ATIVIDADE
where ASSOCIACAO_SUBPROCESSO.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```
