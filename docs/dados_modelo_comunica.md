# MODELO_COMUNICA

Caminho: Customização > Modelo de dados > Processo > MODELO_COMUNICA

Template utilizado para produzir o corpo de um email. Neste template podemos utilizar campos especiais para produção de conteúdo dinâmico.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_MODELO_COMUNICA** | Número sequencial gerado automaticamente pelo sistema para Identificar um ModeloComunicado | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do ModeloComunicado | varchar(500) | varchar(500) | Não |
| **CORPO** | Template utilizado para produção do corpo do email. Neste template é possível introduzir campos que são utilizados para construção de conteúdo dinâmico. | varbinary(4000) | blob | Sim |

Tabelas que dependem de MODELO_COMUNICA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [MENSAGEM_EVENTO](dados_mensagem_evento) | \| **MENSAGEM_EVENTO** \| **MODELO_COMUNICA** \| \|---\|---\| \| ID_MODELO_COMUNICA \| ID_MODELO_COMUNICA \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **MODELO_COMUNICA** \| \|---\|---\| \| ID_MODELO_COMUNICA \| ID_MODELO_COMUNICA \| |
| [ACAO_ACORDO](dados_acao_acordo) | \| **ACAO_ACORDO** \| **MODELO_COMUNICA** \| \|---\|---\| \| ID_MODELO_COMUNICA \| ID_MODELO_COMUNICA \| |
