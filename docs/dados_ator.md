# ATOR

Caminho: Customização > Modelo de dados > Processo > ATOR

Ator participante na execução de um Processo

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | int | number(6,0) | Não |
| **ID_PAPEL_PROCESSO** | Identificador do PapelProcesso associado | int | number(6,0) | Não |
| **ID_PESSOA** | Identificador da Pessoa associada | int | number(6,0) | Não |

Tabelas referenciadas por ATOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **ATOR** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_PROCESSO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ATOR** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ATOR** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela PAPEL_PROCESSO**

```
select ATOR.*, PAPEL_PROCESSO.NOME
from ATOR, PAPEL_PROCESSO
where ATOR.ID_PAPEL_PROCESSO = PAPEL_PROCESSO.ID_PAPEL_PROCESSO
```

**Exemplo 2: join com a tabela OCORRENCIA**

```
select ATOR.*
from ATOR, OCORRENCIA
where ATOR.ID_OCORRENCIA = OCORRENCIA.ID_OCORRENCIA
```
