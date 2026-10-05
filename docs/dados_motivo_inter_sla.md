# MOTIVO_INTER_SLA

Caminho: Customização > Modelo de dados > Recurso > MOTIVO_INTER_SLA

Motivo para interrupção na cronometragem do tempo de atendimento de uma ocorrência.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_MOTIVO_INTER_SLA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Motivo de interrução de cronometragem de tempo de ANS | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Motivo de interrupção de ANS | varchar(500) | varchar(500) | Não |
| **COMENTARIO_OBRIGATORIO** | Quando ativado obriga o usuário que estiver registrando a interrupção (somente inclusão manual) a informar um motivo. Este motivo é replicado no campo de comentários e publicado no Autoatendimento. | char(3) | char(3) | Não |
| **TEMPO_MAXIMO** | Tempo máximo (em horas) para finalização de interrupção manuais (exclui interrupções configuradas no processo). | int | number(6,0) | Sim |

Tabelas que dependem de MOTIVO_INTER_SLA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ACORDO_INTER_SLA](dados_acordo_inter_sla) | \| **ACORDO_INTER_SLA** \| **MOTIVO_INTER_SLA** \| \|---\|---\| \| ID_MOTIVO_INTER \| ID_MOTIVO_INTER_SLA \| |
