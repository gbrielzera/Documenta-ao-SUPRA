# HIST_ITEM

Caminho: Customização > Modelo de dados > Recurso > HIST_ITEM

Informações do Item de Configuração no instante em que foi apurado o Charge-back

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHARGE_BACK** | Identificador do processamento de Charge-back que gerou o histórico. | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do Item de Configuração em histórico. | int | number(6,0) | Não |
| **PRECO_AQUISICAO** | Valor do Preço de aquisição do Item na ocasição da apuração de charge-back. | decimal(15,2) | number(15,2) | Sim |
| **PRECO_MANUTENCAO** | Valor do Preço de manutenção do Item na ocasição da apuração de charge-back. | decimal(15,2) | number(15,2) | Sim |
| **ID_RESPONSAVEL** | Identificador do Responsável pelo Ativo na ocasião da apuração do Charge-back. | int | number(6,0) | Sim |

Tabelas referenciadas por HIST_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CHARGE_BACK](dados_charge_back) | \| **CHARGE_BACK** \| **HIST_ITEM** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| |
| [ITEM](dados_item) | \| **ITEM** \| **HIST_ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **HIST_ITEM** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |

Tabelas que dependem de HIST_ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [HIST_USUARIO](dados_hist_usuario) | \| **HIST_USUARIO** \| **HIST_ITEM** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ITEM \| ID_ITEM \| |
| [HIST_COMP](dados_hist_comp) | \| **HIST_COMP** \| **HIST_ITEM** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela CHARGE_BACK**

```
select HIST_ITEM.*, CHARGE_BACK.ANO
from HIST_ITEM, CHARGE_BACK
where HIST_ITEM.ID_CHARGE_BACK = CHARGE_BACK.ID_CHARGE_BACK
```

**Exemplo 2: join com a tabela PESSOA**

```
select HIST_ITEM.*, PESSOA.NOME_ABREVIADO
from HIST_ITEM left outer join PESSOA on HIST_ITEM.ID_RESPONSAVEL = PESSOA.ID_PESSOA
```
