# SITUACAO_CLASSE

Caminho: Customização > Modelo de dados > Ativos > SITUACAO_CLASSE

Configura todos os Estados possíveis para um Item do Tipo de Item de Configuração associada.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_SITUACAO_CLASSE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Situação para Tipos de Itens de Configuração | int | number(6,0) | Não |
| **ID_CLASSE_CONFIGURACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Item de Configuração | int | number(6,0) | Não |
| **NOME** | Descrição que é exibida para o Usuário | varchar(50) | varchar(50) | Não |
| **INICIAL** | Indica que a Situação é Inicial. Para uma Classe é possível apenas uma Situação Inicial. | char(3) | char(3) | Não |
| **DISP_AA** | Configuração da disponibilidade do 'Tipo de Configuração' na aplicação no Autoatendimento. Alguns 'Tipos de Configuração' são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente. | char(3) | char(3) | Não |
| **DESATIVADO** | Indica que itens nesta situação foram descontinuados. No caso de artigos da base de conhecimento este campo é utilizado para incluir o item na recuperação feita pelo mecanismo de busca. | char(3) | char(3) | Não |

Tabelas referenciadas por SITUACAO_CLASSE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **SITUACAO_CLASSE** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |

Tabelas que dependem de SITUACAO_CLASSE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **SITUACAO_CLASSE** \| \|---\|---\| \| ID_SITUACAO_CLASSE \| ID_SITUACAO_CLASSE \| |

**Exemplo 1: join com a tabela CLASSE_CONFIGURACAO**

```
select SITUACAO_CLASSE.*
from SITUACAO_CLASSE, CLASSE_CONFIGURACAO
where SITUACAO_CLASSE.ID_CLASSE_CONFIGURACAO = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```
