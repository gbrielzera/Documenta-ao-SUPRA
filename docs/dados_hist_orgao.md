# HIST_ORGAO

Caminho: Customização > Modelo de dados > Recurso > HIST_ORGAO

Histórico de estrutura organizacional na ocasião do processamento do Charge-back.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHARGE_BACK** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | int | number(6,0) | Não |
| **ID_ORGAO** | Identificador do Orgao associado | int | number(6,0) | Não |
| **ID_GESTOR** | Identificador do Gestor da Área na ocasição da apuração do Charge-back | int | number(6,0) | Sim |
| **ID_ORGAO_PAI** | Identificador do Órgão pai na ocasião da apuração do Charge-back. | int | number(6,0) | Sim |

Tabelas referenciadas por HIST_ORGAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORGAO](dados_orgao) | \| **ORGAO** \| **HIST_ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **HIST_ORGAO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO_PAI \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **HIST_ORGAO** \| \|---\|---\| \| ID_PESSOA \| ID_GESTOR \| |
| [CHARGE_BACK](dados_charge_back) | \| **CHARGE_BACK** \| **HIST_ORGAO** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| |

Tabelas que dependem de HIST_ORGAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [HIST_PESSOA](dados_hist_pessoa) | \| **HIST_PESSOA** \| **HIST_ORGAO** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ORGAO \| ID_ORGAO \| |

**Exemplo 1: join com a tabela ORGAO**

```
select HIST_ORGAO.*, ORGAO.DESCRICAO
from HIST_ORGAO, ORGAO
where HIST_ORGAO.ID_ORGAO = ORGAO.ID_ORGAO
```

**Exemplo 2: join com a tabela ORGAO**

```
select HIST_ORGAO.*, ORGAO.DESCRICAO
from HIST_ORGAO left outer join ORGAO on HIST_ORGAO.ID_ORGAO_PAI = ORGAO.ID_ORGAO
```

**Exemplo 3: join com a tabela PESSOA**

```
select HIST_ORGAO.*, PESSOA.NOME_ABREVIADO
from HIST_ORGAO left outer join PESSOA on HIST_ORGAO.ID_GESTOR = PESSOA.ID_PESSOA
```

**Exemplo 4: join com a tabela CHARGE_BACK**

```
select HIST_ORGAO.*
from HIST_ORGAO, CHARGE_BACK
where HIST_ORGAO.ID_CHARGE_BACK = CHARGE_BACK.ID_CHARGE_BACK
```
