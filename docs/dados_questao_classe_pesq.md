# QUESTAO_CLASSE_PESQ

Caminho: Customização > Modelo de dados > Processo > QUESTAO_CLASSE_PESQ

Questões de Classes de Pesquisa

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_PESQ_SATISF** | Número sequencial gerado automaticamente pelo sistema para Identificar uma ClassePesquisaSatisfacao | int | number(6,0) | Não |
| **ID_QUESTAO** | Identificador da QuestaoPesquisa associada | int | number(6,0) | Não |

Tabelas referenciadas por QUESTAO_CLASSE_PESQ

| **Tabela** | **Colunas de ligação** |
|---|---|
| [QUESTAO_PESQUISA](dados_questao_pesquisa) | \| **QUESTAO_PESQUISA** \| **QUESTAO_CLASSE_PESQ** \| \|---\|---\| \| ID_QUESTAO \| ID_QUESTAO \| |
| [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf) | \| **CLASSE_PESQ_SATISF** \| **QUESTAO_CLASSE_PESQ** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |

**Exemplo 1: join com a tabela QUESTAO_PESQUISA**

```
select QUESTAO_CLASSE_PESQ.*, QUESTAO_PESQUISA.DESCRICAO
from QUESTAO_CLASSE_PESQ, QUESTAO_PESQUISA
where QUESTAO_CLASSE_PESQ.ID_QUESTAO = QUESTAO_PESQUISA.ID_QUESTAO
```

**Exemplo 2: join com a tabela CLASSE_PESQ_SATISF**

```
select QUESTAO_CLASSE_PESQ.*
from QUESTAO_CLASSE_PESQ, CLASSE_PESQ_SATISF
where QUESTAO_CLASSE_PESQ.ID_CLASSE_PESQ_SATISF = CLASSE_PESQ_SATISF.ID_CLASSE_PESQ_SATISF
```
