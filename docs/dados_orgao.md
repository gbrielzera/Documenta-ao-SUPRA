# ORGAO

Caminho: Customização > Modelo de dados > Recurso > ORGAO

Diretoria, Gerência, Departamento ou Área que compõe a estrutura organizacional. Em um Órgão, também denominado Área, podemos associar empregados ou terceiros (lotação). Um Órgão pode possuir uma associação com outro Órgão denominado "Pai". Esta associação "pai-filho" define a hierarquia de órgãos de uma Empresa.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ORGAO** | Identificador do Órgão | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente a função do Órgão. Este texto é utilizado por profissionais e clientes para busca por itens da estrutura organizacional. | varchar(500) | varchar(500) | Não |
| **SIGLA** | Nome resumido (código) utilizado para identificar um Órgão. | varchar(50) | varchar(50) | Não |
| **ATIVO** | Indica que o Órgão está Ativo | char(3) | char(3) | Não |
| **ID_GESTOR** | Identificador do Gestor do Órgão. Esta associação é utilizada constantemente na implementação de Processos. | int | number(6,0) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_ORGAO_PAI** | Identificador do Orgao pai que define a hierarquia organizacional. | int | number(6,0) | Sim |
| **ID_EMPRESA** | Identificador da Empresa dona do Órgão. | int | number(6,0) | Não |

Tabelas referenciadas por ORGAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ORGAO** \| \|---\|---\| \| ID_PESSOA \| ID_GESTOR \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO_PAI \| |
| [EMPRESA](dados_empresa) | \| **EMPRESA** \| **ORGAO** \| \|---\|---\| \| ID_EMPRESA \| ID_EMPRESA \| |

Tabelas que dependem de ORGAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **ORGAO** \| \|---\|---\| \| ID_ORGAO_PAI \| ID_ORGAO \| |
| [CHARGE_BACK_ORGAO](dados_charge_back_orgao) | \| **CHARGE_BACK_ORGAO** \| **ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [HIST_ORGAO](dados_hist_orgao) | \| **HIST_ORGAO** \| **ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [HIST_ORGAO](dados_hist_orgao) | \| **HIST_ORGAO** \| **ORGAO** \| \|---\|---\| \| ID_ORGAO_PAI \| ID_ORGAO \| |
| [ORGAO_SLA](dados_orgao_sla) | \| **ORGAO_SLA** \| **ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |

**Exemplo 1: join com a tabela PESSOA**

```
select ORGAO.*, PESSOA.NOME_ABREVIADO
from ORGAO left outer join PESSOA on ORGAO.ID_GESTOR = PESSOA.ID_PESSOA
```

**Exemplo 2: join com a tabela ORGAO**

```
select ORGAO.*, ORGAO2.DESCRICAO
from ORGAO left outer join ORGAO ORGAO2 on ORGAO.ID_ORGAO_PAI = ORGAO2.ID_ORGAO
```

**Exemplo 3: join com a tabela EMPRESA**

```
select ORGAO.*, EMPRESA.DESCRICAO
from ORGAO, EMPRESA
where ORGAO.ID_EMPRESA = EMPRESA.ID_EMPRESA
```
