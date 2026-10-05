# ATOR_SERVICO

Caminho: Customização > Modelo de dados > Processo > ATOR_SERVICO

Atores

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATOR_SERVICO** | Número sequencial gerado automaticamente pelo sistema para Identificar um AtoresServico | int | number(6,0) | Não |
| **ID_SERVICO** | Identificador do Serviço | int | number(6,0) | Não |
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do PapelClasseNegocio associado | int | number(6,0) | Não |
| **ID_PAPEL_REDIR** | Identificador do Papel utilizado para redirecionamento. | int | number(6,0) | Sim |
| **ID_PESSOA** | Identificador da Pessoa atribuída como Ator para o Papel | int | number(6,0) | Sim |

Tabelas referenciadas por ATOR_SERVICO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **ATOR_SERVICO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **ATOR_SERVICO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_REDIR \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ATOR_SERVICO** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [SERVICO](dados_servico) | \| **SERVICO** \| **ATOR_SERVICO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |

**Exemplo 1: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select ATOR_SERVICO.*, PAPEL_CLASSE_NEGOCIO.NOME
from ATOR_SERVICO, PAPEL_CLASSE_NEGOCIO
where ATOR_SERVICO.ID_PAPEL_CLASSE_NEGOCIO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

**Exemplo 2: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select ATOR_SERVICO.*, PAPEL_CLASSE_NEGOCIO.NOME
from ATOR_SERVICO left outer join PAPEL_CLASSE_NEGOCIO on ATOR_SERVICO.ID_PAPEL_REDIR = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

**Exemplo 3: join com a tabela SERVICO**

```
select ATOR_SERVICO.*
from ATOR_SERVICO, SERVICO
where ATOR_SERVICO.ID_SERVICO = SERVICO.ID_SERVICO
```
