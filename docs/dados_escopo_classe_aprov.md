# ESCOPO_CLASSE_APROV

Caminho: Customização > Modelo de dados > Processo > ESCOPO_CLASSE_APROV

Relação de Tipos de Itens de Configuração que podem ser aprovados na ocorrência.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ESCOPO_CLASSE_APROV** | Número sequencial gerado automaticamente pelo sistema para Identificar um EscopoClasseAprovacao | int | number(6,0) | Não |
| **ID_CLASSE_APROVACAO** | Identificador da Classe de Aprovação que contém a regra de Escopo | int | number(6,0) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item de Configuração | int | number(6,0) | Sim |
| **SUPER_CLASSE** | Super tipo que pode ter itens associados na solicitação de aprovação. Se for preenchida o Tipo de Item de Configuração então este campo é preenchido automaticamente com o Super tipo correspondente. | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por ESCOPO_CLASSE_APROV

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **ESCOPO_CLASSE_APROV** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_APROVACAO](dados_classe_aprovacao) | \| **CLASSE_APROVACAO** \| **ESCOPO_CLASSE_APROV** \| \|---\|---\| \| ID_CLASSE_APROVACAO \| ID_CLASSE_APROVACAO \| |

**Exemplo 1: join com a tabela CLASSE_APROVACAO**

```
select ESCOPO_CLASSE_APROV.*
from ESCOPO_CLASSE_APROV, CLASSE_APROVACAO
where ESCOPO_CLASSE_APROV.ID_CLASSE_APROVACAO = CLASSE_APROVACAO.ID_CLASSE_APROVACAO
```
