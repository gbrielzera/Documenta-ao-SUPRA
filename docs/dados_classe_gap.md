# CLASSE_GAP

Caminho: Customização > Modelo de dados > Processo > CLASSE_GAP

Classificações de Gaps

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_GAP** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseGAP | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do ClasseGAP | varchar(500) | varchar(500) | Não |
| **EXPLICACAO** | Explicação | varchar(500) | varchar(500) | Não |

Tabelas que dependem de CLASSE_GAP

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GAP](dados_gap) | \| **GAP** \| **CLASSE_GAP** \| \|---\|---\| \| ID_CLASSE_GAP \| ID_CLASSE_GAP \| |
