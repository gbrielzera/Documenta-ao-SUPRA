# CONHECIMENTO

Caminho: Customização > Modelo de dados > Ativos > CONHECIMENTO

Artigo de Base de Conhecimento

Por se tratar de um tipo herdado de ItemConfiguracao, a tabela CONHECIMENTO possui uma chave estrangeira apontando para a tabela [ITEM](dados_item).

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **TITULO** | Título | varchar(500) | varchar(500) | Não |
| **SUMARIO** | Sumário | text | clob | Não |
| **PALAVRAS_CHAVE** | Palavras Chave para pesquisa | varchar(500) | varchar(500) | Sim |
| **SUMARIO_TEXTO** | Sumário em forma de texto, sem as TAGs html | text | clob | Sim |

Tabelas que dependem de CONHECIMENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [USO_CONHECIMENTO](dados_uso_conhecimento) | \| **USO_CONHECIMENTO** \| **CONHECIMENTO** \| \|---\|---\| \| ID_ITEM \|  \| |
| [TOPICO_ARTIGO](dados_topico_artigo) | \| **TOPICO_ARTIGO** \| **CONHECIMENTO** \| \|---\|---\| \| ID_ITEM \|  \| |
| [APLIC_CONH_SERV](dados_aplic_conh_serv) | \| **APLIC_CONH_SERV** \| **CONHECIMENTO** \| \|---\|---\| \| ID_ITEM \|  \| |
| [PERM_CONH_PAPEL](dados_perm_conh_papel) | \| **PERM_CONH_PAPEL** \| **CONHECIMENTO** \| \|---\|---\| \| ID_CONHECIMENTO \|  \| |
