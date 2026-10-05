# UNIDADE_NEGOCIO

Caminho: Customização > Modelo de dados > Recurso > UNIDADE_NEGOCIO

A Unidade de Negócio define uma localização (site, filial etc) onde estão localizados os Clientes e Ativos. Para uma Unidade de Negócio é possível cadastrar Prédios e respectivos andares, salas e locais.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_UNIDADE_NEGOCIO** | Número sequencial gerado por sistema para identificar uma Unidade de Negócio. Este número não pode ser modificado pelo usuário do sistema. | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente a localização ou finalidade da Unidade de Negócio | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que a Unidade de Negócio está ativa | char(3) | char(3) | Não |
| **SIGLA** | Nome resumido (código) utilizado para identificar uma Unidade de Negócio | varchar(50) | varchar(50) | Não |
| **LOCALIZACAO** | Endereço, Cidade, Estado ou qualquer outra referência de Localização da Unidade de Negócio. | varchar(500) | varchar(500) | Não |
| **ID_EMPRESA** | Identificador da Empresa associada | int | number(6,0) | Não |
| **ID_CALENDARIO** | Identificador do Calendário associado | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas referenciadas por UNIDADE_NEGOCIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [EMPRESA](dados_empresa) | \| **EMPRESA** \| **UNIDADE_NEGOCIO** \| \|---\|---\| \| ID_EMPRESA \| ID_EMPRESA \| |
| [CALENDARIO](dados_calendario) | \| **CALENDARIO** \| **UNIDADE_NEGOCIO** \| \|---\|---\| \| ID_CALENDARIO \| ID_CALENDARIO \| |

Tabelas que dependem de UNIDADE_NEGOCIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PREDIO](dados_predio) | \| **PREDIO** \| **UNIDADE_NEGOCIO** \| \|---\|---\| \| ID_UNIDADE_NEGOCIO \| ID_UNIDADE_NEGOCIO \| |

**Exemplo 1: join com a tabela EMPRESA**

```
select UNIDADE_NEGOCIO.*, EMPRESA.DESCRICAO
from UNIDADE_NEGOCIO, EMPRESA
where UNIDADE_NEGOCIO.ID_EMPRESA = EMPRESA.ID_EMPRESA
```

**Exemplo 2: join com a tabela CALENDARIO**

```
select UNIDADE_NEGOCIO.*, CALENDARIO.DESCRICAO
from UNIDADE_NEGOCIO, CALENDARIO
where UNIDADE_NEGOCIO.ID_CALENDARIO = CALENDARIO.ID_CALENDARIO
```
