# GRUPO_QUESTAO

Caminho: Customização > Modelo de dados > Processo > GRUPO_QUESTAO

Um Grupo de Questões define um agrupamento de questões de Pesquisa de Satisfação que possuem um objetivo comum na avaliação de um Serviço. Todas as questões associadas a um grupo possuem as mesmas opções de respostas. Um Grupo de Questões pode ser alvo de avaliação em um Indicador de Desempenho.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GRUPO_QUESTAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Grupo de Questões | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Grupo de Questões | varchar(500) | varchar(500) | Não |

Tabelas que dependem de GRUPO_QUESTAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [QUESTAO_PESQUISA](dados_questao_pesquisa) | \| **QUESTAO_PESQUISA** \| **GRUPO_QUESTAO** \| \|---\|---\| \| ID_GRUPO_QUESTAO \| ID_GRUPO_QUESTAO \| |
| [GRUPO_QUESTAO_INDICADOR](dados_grupo_questao_indicador) | \| **GRUPO_QUESTAO_INDICADOR** \| **GRUPO_QUESTAO** \| \|---\|---\| \| ID_GRUPO_QUESTAO \| ID_GRUPO_QUESTAO \| |
| [ESCORE_QUESTAO](dados_escore_questao) | \| **ESCORE_QUESTAO** \| **GRUPO_QUESTAO** \| \|---\|---\| \| ID_GRUPO_QUESTAO \| ID_GRUPO_QUESTAO \| |
