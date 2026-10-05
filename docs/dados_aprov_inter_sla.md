# APROV_INTER_SLA

Caminho: Customização > Modelo de dados > Recurso > APROV_INTER_SLA

Aprovador de Interrupção em cronometragem de tempo de atendimento de ocorrências.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SLA** | Identificador do Acordo de Nível de Serviço proprietário da regra de interrupção de cronometragem de tempo. | int | number(6,0) | Não |
| **ID_MOTIVO_INTER** | Identificador do Motivo de interrução para cronometragem de tempo de atendimento. | int | number(6,0) | Não |
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do PapelClasseNegocio associado | int | number(6,0) | Não |

Tabelas referenciadas por APROV_INTER_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **APROV_INTER_SLA** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [ACORDO_INTER_SLA](dados_acordo_inter_sla) | \| **ACORDO_INTER_SLA** \| **APROV_INTER_SLA** \| \|---\|---\| \| ID_SLA \| ID_SLA \| \| ID_MOTIVO_INTER \| ID_MOTIVO_INTER \| |
