# APROPRIACAO_APROVACAO

Caminho: Customização > Modelo de dados > Processo > APROPRIACAO_APROVACAO

Apropriação em uma Aprovação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_APROPRIACAO** | Identificador do Apropriacao associado | int | number(6,0) | Não |
| **ID_ASSUNTO_APROVACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um AssuntoAprovacao | int | number(6,0) | Não |
| **VERSAO** | Sequencial gerado automaticamente pelo sistema para cada Assunto de uma determinada Ordem de Serviço | int | number(6,0) | Não |

Tabelas referenciadas por APROPRIACAO_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APROPRIACAO](dados_apropriacao) | \| **APROPRIACAO** \| **APROPRIACAO_APROVACAO** \| \|---\|---\| \| ID_APROPRIACAO \| ID_APROPRIACAO \| |
| [VERSAO_APROVACAO](dados_versao_aprovacao) | \| **VERSAO_APROVACAO** \| **APROPRIACAO_APROVACAO** \| \|---\|---\| \| ID_ASSUNTO_APROVACAO \| ID_ASSUNTO_APROVACAO \| \| VERSAO \| VERSAO \| |

**Exemplo 1: join com a tabela APROPRIACAO**

```
select APROPRIACAO_APROVACAO.*, APROPRIACAO.REFERENCIA
from APROPRIACAO_APROVACAO, APROPRIACAO
where APROPRIACAO_APROVACAO.ID_APROPRIACAO = APROPRIACAO.ID_APROPRIACAO
```
