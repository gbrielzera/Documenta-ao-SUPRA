# EMPRESA

Caminho: Customização > Modelo de dados > Recurso > EMPRESA

Uma Empresa é uma entidade composta por um ou mais órgãos onde estão lotadas pessoas. Uma empresa também pode pertencer a um grupo de empresas. Na aplicação de Autoatendimento empresas são utilizadas para restringir buscas por pessoas. Na tela de substitutos, por exemplo, são listadas apenas as pessoas lotadas na empresa do usuário conectado. Porém, se a empresa do usuário conectado faz parte de um grupo de empresas então são listadas todas as pessoas do mesmo grupo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_EMPRESA** | Número sequencial gerado por sistema para identificar uma Empresa | int | number(6,0) | Não |
| **DESCRICAO** | Nome da Empresa | varchar(500) | varchar(500) | Não |
| **SIGLA** | Nome resumido utilizado para identificar uma Empresa | varchar(50) | varchar(50) | Não |
| **ATIVO** | Indica que a Empresa está ativa | char(3) | char(3) | Não |
| **ID_GRUPO_EMPRESA** | Identificador do Grupo de Empresas ao qual pertence a Empresa | int | number(6,0) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_FATOR_PRIORIDADE** | Identificador do Fator de Prioridade utilizado em cálculos de Prioridade. | int | number(6,0) | Sim |

Tabelas referenciadas por EMPRESA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_EMPRESA](dados_grupo_empresa) | \| **GRUPO_EMPRESA** \| **EMPRESA** \| \|---\|---\| \| ID_GRUPO_EMPRESA \| ID_GRUPO_EMPRESA \| |
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **EMPRESA** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |

Tabelas que dependem de EMPRESA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [UNIDADE_NEGOCIO](dados_unidade_negocio) | \| **UNIDADE_NEGOCIO** \| **EMPRESA** \| \|---\|---\| \| ID_EMPRESA \| ID_EMPRESA \| |
| [CONTRATO](dados_contrato) | \| **CONTRATO** \| **EMPRESA** \| \|---\|---\| \| ID_CONTRATANTE \| ID_EMPRESA \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **EMPRESA** \| \|---\|---\| \| ID_EMPRESA \| ID_EMPRESA \| |

**Exemplo 1: join com a tabela GRUPO_EMPRESA**

```
select EMPRESA.*, GRUPO_EMPRESA.DESCRICAO
from EMPRESA left outer join GRUPO_EMPRESA on EMPRESA.ID_GRUPO_EMPRESA = GRUPO_EMPRESA.ID_GRUPO_EMPRESA
```

**Exemplo 2: join com a tabela FATOR_PRIORIDADE**

```
select EMPRESA.*, FATOR_PRIORIDADE.DESCRICAO
from EMPRESA left outer join FATOR_PRIORIDADE on EMPRESA.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```
