# HIST_PESSOA

Caminho: Customização > Modelo de dados > Recurso > HIST_PESSOA

Pessoas lotadas na área na ocasião do processamento do Charge-back

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHARGE_BACK** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | int | number(6,0) | Não |
| **ID_ORGAO** | Identificador do Orgao associado | int | number(6,0) | Não |
| **ID_PESSOA** | Identificador da Pessoa lotada na área | int | number(6,0) | Não |

Tabelas referenciadas por HIST_PESSOA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **HIST_PESSOA** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [HIST_ORGAO](dados_hist_orgao) | \| **HIST_ORGAO** \| **HIST_PESSOA** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ORGAO \| ID_ORGAO \| |

**Exemplo 1: join com a tabela PESSOA**

```
select HIST_PESSOA.*, PESSOA.NOME_ABREVIADO
from HIST_PESSOA, PESSOA
where HIST_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA
```
