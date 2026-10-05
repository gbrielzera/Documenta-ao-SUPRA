# CHARGE_BACK

Caminho: Customização > Modelo de dados > Recurso > CHARGE_BACK

Cobrança por uso de Ativo ou serviço prestado.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHARGE_BACK** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | int | number(6,0) | Não |
| **ANO** | Ano competência | int | number(6,0) | Não |
| **MES** | Mês competência | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DATA_HORA_PROC** | Data e hora de processamento do Charge-back | datetime | date | Não |
| **PUBLICADO** | Indica que os dados do Charge-back são públicos para áreas Clientes na aplicação de Autoatendimento | char(3) | char(3) | Não |

Tabelas que dependem de CHARGE_BACK

| **Tabela** | **Colunas de ligação** |
|---|---|
| [HIST_ITEM](dados_hist_item) | \| **HIST_ITEM** \| **CHARGE_BACK** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| |
| [CHARGE_BACK_ORGAO](dados_charge_back_orgao) | \| **CHARGE_BACK_ORGAO** \| **CHARGE_BACK** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| |
| [HIST_ORGAO](dados_hist_orgao) | \| **HIST_ORGAO** \| **CHARGE_BACK** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| |
