# FREQ_CONTROLE

Caminho: Customização > Modelo de dados > Processo > FREQ_CONTROLE

Frequências de testes ou execução de Controles

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_FREQ_CONTROLE** | Número sequencial gerado automaticamente pelo sistema para Identificar um FrequenciaControle | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do FrequenciaControle | varchar(500) | varchar(500) | Não |

Tabelas que dependem de FREQ_CONTROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **FREQ_CONTROLE** \| \|---\|---\| \| ID_FREQ_CONTROLE \| ID_FREQ_CONTROLE \| |
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **FREQ_CONTROLE** \| \|---\|---\| \| ID_FREQ_TESTE \| ID_FREQ_CONTROLE \| |
