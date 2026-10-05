# TOPICO_CONH

Caminho: Customização > Modelo de dados > Ativos > TOPICO_CONH

Tópico que deve ser preenchido na elaboração de um artigo da base de conhecimento. Quando um artigo é criado todos os tópicos são preenchidos conforme o template definido por este registro.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_TOPICO_CONH** | Número sequencial gerado automaticamente pelo sistema para Identificar um TopicoConhecimento | int | number(6,0) | Não |
| **SUB_TITULO** | Sub-título do tópico | varchar(500) | varchar(500) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item de Configuração proprietária do template de tópico para artigos da base de conheicmento | int | number(6,0) | Não |
| **SEQUENCIA** | Sequencial utilizado para ordenar (ordenação ascendente) tópicos de um determinado artigo. | int | number(6,0) | Não |

Tabelas referenciadas por TOPICO_CONH

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **TOPICO_CONH** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |

Tabelas que dependem de TOPICO_CONH

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TOPICO_ARTIGO](dados_topico_artigo) | \| **TOPICO_ARTIGO** \| **TOPICO_CONH** \| \|---\|---\| \| ID_TOPICO_CONH \| ID_TOPICO_CONH \| |

**Exemplo 1: join com a tabela CLASSE_CONFIGURACAO**

```
select TOPICO_CONH.*
from TOPICO_CONH, CLASSE_CONFIGURACAO
where TOPICO_CONH.ID_CLASSE_CONFIGURACAO = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```
