# CLIENTE_AUTORIZADO

Caminho: Customização > Modelo de dados > Processo > CLIENTE_AUTORIZADO

Papel de processo utilizado para identificar as pessoas autorizadas a gerar solicitações em um determinado Subprocesso. Estas autorizações são verificadas no instante em que abrimos uma solicitação no Workspace e também no Autoatendimento. Neste último caso o iniciador associado não é exibido para o usuário conectado caso este não atenda ao mecanismo de restrição.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATIVIDADE** | Identificador da Atividade de processo que contém a regra de autorização descrita pelo objeto. | int | number(6,0) | Não |
| **ID_PAPEL_PROCESSO** | Identificador do Papel de processo autorizado a iniciar uma solicitação | int | number(6,0) | Não |

Tabelas referenciadas por CLIENTE_AUTORIZADO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **CLIENTE_AUTORIZADO** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_PROCESSO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **CLIENTE_AUTORIZADO** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela PAPEL_PROCESSO**

```
select CLIENTE_AUTORIZADO.*, PAPEL_PROCESSO.NOME
from CLIENTE_AUTORIZADO, PAPEL_PROCESSO
where CLIENTE_AUTORIZADO.ID_PAPEL_PROCESSO = PAPEL_PROCESSO.ID_PAPEL_PROCESSO
```

**Exemplo 2: join com a tabela ATIVIDADE**

```
select CLIENTE_AUTORIZADO.*
from CLIENTE_AUTORIZADO, ATIVIDADE
where CLIENTE_AUTORIZADO.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```
