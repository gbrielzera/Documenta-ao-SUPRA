# HIST_USUARIO

Caminho: Customização > Modelo de dados > Recurso > HIST_USUARIO

Histórico de usuários para um Item de Configuração. Este histórico é gerado pela rotina de charge-back para rastreabilidade da base de cálculo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHARGE_BACK** | Identificador da apuração de Charge-back que gerou o histórico | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do Item de Configuração proprietário do histórico | int | number(6,0) | Não |
| **ID_USUARIO** | Identificador da Pessoa usuária do Item de Configuração na ocasião da apuração de Charge-Back | int | number(6,0) | Não |

Tabelas referenciadas por HIST_USUARIO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **HIST_USUARIO** \| \|---\|---\| \| ID_PESSOA \| ID_USUARIO \| |
| [HIST_ITEM](dados_hist_item) | \| **HIST_ITEM** \| **HIST_USUARIO** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela PESSOA**

```
select HIST_USUARIO.*, PESSOA.NOME_ABREVIADO
from HIST_USUARIO, PESSOA
where HIST_USUARIO.ID_USUARIO = PESSOA.ID_PESSOA
```
